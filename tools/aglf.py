"""
AGLF v0.1 reference tool
------------------------
Verifies an AGLF trace and its manifest, and can generate the example trace.

    python tools/aglf.py verify <trace.jsonl> <manifest.json>
    python tools/aglf.py example <output_dir>

`verify` checks, in order:
    1. every record matches schemas/aglf/v0.1/aglf.schema.json
    2. seq runs 0, 1, 2, ... with one trace_id throughout
    3. each content_hash, record_hash and prev_hash is correct (the hash chain)
    4. the manifest matches the trace and its Ed25519 signature is valid
    5. the HUMAN_INPUT records are allowed at the declared autonomy level

Canonical JSON (used for content_hash): keys sorted, no whitespace
(separators "," and ":"), UTF-8, non-ASCII characters kept as-is.

Requires: pip install jsonschema cryptography
"""

import hashlib
import json
import sys
from pathlib import Path

ZERO_HASH = "0" * 64
HASH_FIELDS = ("prev_hash", "content_hash", "record_hash")
SCHEMA_DIR = Path(__file__).resolve().parent.parent / "schemas" / "aglf" / "v0.1"

# Human roles allowed at each declared autonomy level (see docs/autonomy-levels.md).
# "edit" (copy-editing the final text) is disclosed but does not change the level.
ALLOWED_HUMAN_ROLES = {
    "L3": {"initiation", "edit"},
    "L2": {"initiation", "topic", "edit"},
    "L1": {"initiation", "topic", "question", "methodology", "edit"},
}


def canonical(obj) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def content_hash(record: dict) -> str:
    return sha256_hex(canonical({k: v for k, v in record.items() if k not in HASH_FIELDS}))


def chain(records):
    """Fill in prev_hash, content_hash and record_hash for a list of records."""
    prev = ZERO_HASH
    for r in records:
        r["prev_hash"] = prev
        r["content_hash"] = content_hash(r)
        r["record_hash"] = sha256_hex((prev + r["content_hash"]).encode("ascii"))
        prev = r["record_hash"]
    return records


def _load_schema(name):
    return json.loads((SCHEMA_DIR / name).read_text())


def verify(trace_path: str, manifest_path: str) -> list:
    """Return a list of problems; an empty list means the trace is valid."""
    import jsonschema
    from cryptography.exceptions import InvalidSignature
    from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey

    problems = []
    record_validator = jsonschema.Draft202012Validator(_load_schema("aglf.schema.json"))
    manifest_validator = jsonschema.Draft202012Validator(_load_schema("manifest.schema.json"))

    raw = Path(trace_path).read_bytes()
    lines = [ln for ln in raw.decode("utf-8").splitlines() if ln.strip()]
    records = [json.loads(ln) for ln in lines]
    if not records:
        return ["trace is empty"]

    prev = ZERO_HASH
    trace_id = records[0].get("trace_id")
    span_ids = set()
    for i, r in enumerate(records):
        for err in record_validator.iter_errors(r):
            problems.append(f"record {i}: schema: {err.message}")
        if r.get("seq") != i:
            problems.append(f"record {i}: seq is {r.get('seq')}, expected {i}")
        if r.get("trace_id") != trace_id:
            problems.append(f"record {i}: trace_id differs from record 0")
        parent = r.get("parent_span_id")
        if parent is not None and parent not in span_ids:
            problems.append(f"record {i}: parent_span_id {parent} does not appear earlier in the trace")
        span_ids.add(r.get("span_id"))
        if r.get("prev_hash") != prev:
            problems.append(f"record {i}: prev_hash does not match the previous record (chain broken)")
        if r.get("content_hash") != content_hash(r):
            problems.append(f"record {i}: content_hash does not match the record (content altered)")
        expected = sha256_hex((str(r.get("prev_hash")) + str(r.get("content_hash"))).encode("ascii"))
        if r.get("record_hash") != expected:
            problems.append(f"record {i}: record_hash is wrong")
        prev = r.get("record_hash")

    manifest = json.loads(Path(manifest_path).read_text())
    for err in manifest_validator.iter_errors(manifest):
        problems.append(f"manifest: schema: {err.message}")
    if manifest.get("trace_file_sha256") != sha256_hex(raw):
        problems.append("manifest: trace_file_sha256 does not match the trace file")
    if manifest.get("record_count") != len(records):
        problems.append("manifest: record_count does not match the trace")
    if manifest.get("trace_id") != trace_id:
        problems.append("manifest: trace_id does not match the trace")
    if manifest.get("final_record_hash") != prev:
        problems.append("manifest: final_record_hash does not match the last record")
    try:
        sig = manifest["signature"]
        Ed25519PublicKey.from_public_bytes(bytes.fromhex(sig["public_key"])).verify(
            bytes.fromhex(sig["value"]), manifest["final_record_hash"].encode("ascii")
        )
    except (InvalidSignature, KeyError, ValueError):
        problems.append("manifest: signature is invalid")

    level = manifest.get("declared_autonomy_level")
    allowed = ALLOWED_HUMAN_ROLES.get(level, set())
    for i, r in enumerate(records):
        araa = r.get("araa", {})
        if araa.get("event_type") == "HUMAN_INPUT" and araa.get("human_role") not in allowed:
            problems.append(
                f"record {i}: human input '{araa.get('human_role')}' is not allowed at declared level {level}"
            )
    return problems


def example(out_dir: str):
    """Write example-trace.jsonl and example-manifest.json with a throwaway key."""
    from cryptography.hazmat.primitives import serialization
    from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey

    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    tid = "4bf92f3577b34da6a3ce929d0e0e4736"
    model = "example-model-1"

    def span(seq, sid, parent, name, start, end, attrs, araa, status="ok"):
        return {
            "aglf_version": "0.1", "seq": seq, "trace_id": tid, "span_id": sid,
            "parent_span_id": parent, "name": name,
            "start_time": f"2027-03-15T10:{start}Z", "end_time": f"2027-03-15T10:{end}Z",
            "status": status, "attributes": attrs, "araa": araa,
        }

    agent = {"gen_ai.agent.id": "example-researcher-v1", "gen_ai.agent.name": "Example Researcher",
             "gen_ai.agent.version": "1.0.0", "gen_ai.conversation.id": "run-0001"}
    llm = {"gen_ai.provider.name": "example-provider", "gen_ai.request.model": model, "gen_ai.response.model": model}
    root = "a000000000000001"

    records = [
        span(0, root, None, "invoke_agent Example Researcher", "00:00.000", "00:00.100",
             {"gen_ai.operation.name": "invoke_agent", **agent},
             {"event_type": "AGENT_STEP", "stage": "initiation", "summary": "Run started."}),
        span(1, "a000000000000002", root, "human_input", "00:00.100", "00:00.200", {},
             {"event_type": "HUMAN_INPUT", "stage": "initiation", "human_role": "initiation",
              "summary": "Operator started the agent with the instruction 'Do research' and a compute budget."}),
        span(2, "a000000000000003", root, f"chat {model}", "00:01.000", "00:09.500",
             {"gen_ai.operation.name": "chat", **llm, "gen_ai.usage.input_tokens": 1847, "gen_ai.usage.output_tokens": 423,
              "gen_ai.input.messages": [{"role": "user", "parts": [{"type": "text", "content": "Survey recent work on federated learning with heterogeneous clients and list open gaps."}]}],
              "gen_ai.output.messages": [{"role": "assistant", "parts": [{"type": "text", "content": "Gap: few studies test learning-rate stability on highly heterogeneous partitions."}]}]},
             {"event_type": "MODEL_CALL", "stage": "gap_identification", "summary": "Identified a research gap."}),
        span(3, "a000000000000004", root, "execute_tool run_experiment", "01:00.000", "05:12.000",
             {"gen_ai.operation.name": "execute_tool", "gen_ai.tool.name": "run_experiment", "gen_ai.tool.call.id": "call_03"},
             {"event_type": "TOOL_CALL", "stage": "execution", "summary": "Ran experiment_03 with lr=0.0005.",
              "artifacts": [{"path": "experiments/experiment_03.yaml", "sha256": sha256_hex(b"lr: 0.0005\n")}]}),
        span(4, "a000000000000005", root, "araa.decision", "05:12.000", "05:12.050", {},
             {"event_type": "DECISION", "stage": "analysis", "decision": "refine",
              "summary": "lr=0.0005 improved stability; refine the comparison with 3 more seeds."}),
    ]
    chain(records)
    trace_bytes = "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in records).encode("utf-8")
    (out / "example-trace.jsonl").write_bytes(trace_bytes)

    key = Ed25519PrivateKey.generate()
    final = records[-1]["record_hash"]
    pub = key.public_key().public_bytes(serialization.Encoding.Raw, serialization.PublicFormat.Raw)
    manifest = {
        "aglf_version": "0.1", "trace_file": "example-trace.jsonl",
        "trace_file_sha256": sha256_hex(trace_bytes), "trace_id": tid,
        "record_count": len(records), "final_record_hash": final,
        "declared_autonomy_level": "L3",
        "signature": {"algorithm": "ed25519", "public_key": pub.hex(),
                      "value": key.sign(final.encode("ascii")).hex()},
    }
    (out / "example-manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"[+] Wrote example-trace.jsonl and example-manifest.json to {out}")


def main(argv):
    if len(argv) == 4 and argv[1] == "verify":
        problems = verify(argv[2], argv[3])
        if problems:
            print("[-] AGLF verification FAILED:")
            for p in problems:
                print("    - " + p)
            return 1
        print("[+] AGLF verification passed.")
        return 0
    if len(argv) == 3 and argv[1] == "example":
        example(argv[2])
        return 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))

"""Tests for tools/aglf.py. Run with `python -m pytest tests/` or `python tests/test_aglf.py`."""

import copy
import json
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import aglf  # noqa: E402

from cryptography.hazmat.primitives import serialization  # noqa: E402
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey  # noqa: E402

EXAMPLE = ROOT / "schemas" / "aglf" / "v0.1"


def _base_records():
    return [json.loads(line) for line in (EXAMPLE / "example-trace.jsonl").read_text().splitlines() if line]


def _write_signed(records, level="L3"):
    """Re-chain and re-sign records with a fresh key, as an honest operator would."""
    d = Path(tempfile.mkdtemp())
    aglf.chain(records)
    data = "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in records).encode("utf-8")
    (d / "t.jsonl").write_bytes(data)
    key = Ed25519PrivateKey.generate()
    pub = key.public_key().public_bytes(serialization.Encoding.Raw, serialization.PublicFormat.Raw)
    m = {
        "aglf_version": "0.1", "trace_file": "t.jsonl", "trace_file_sha256": aglf.sha256_hex(data),
        "trace_id": records[0]["trace_id"], "record_count": len(records),
        "final_record_hash": records[-1]["record_hash"], "declared_autonomy_level": level,
        "signature": {"algorithm": "ed25519", "public_key": pub.hex()},
    }
    m["signature"]["value"] = key.sign(aglf.manifest_payload(m)).hex()
    (d / "m.json").write_text(json.dumps(m))
    return str(d / "t.jsonl"), str(d / "m.json")


def test_example_passes():
    assert aglf.verify(str(EXAMPLE / "example-trace.jsonl"), str(EXAMPLE / "example-manifest.json")) == []


def test_resigned_unchanged_trace_passes():
    assert aglf.verify(*_write_signed(_base_records())) == []


def test_edited_record_fails():
    trace, manifest = _write_signed(_base_records())
    lines = Path(trace).read_text().splitlines()
    lines[2] = lines[2].replace("Identified a research gap.", "Identified a major research gap.")
    Path(trace).write_text("\n".join(lines) + "\n")
    assert any("content_hash" in p for p in aglf.verify(trace, manifest))


def test_deleted_record_fails():
    trace, manifest = _write_signed(_base_records())
    lines = Path(trace).read_text().splitlines()
    del lines[3]
    Path(trace).write_text("\n".join(lines) + "\n")
    assert any("chain broken" in p for p in aglf.verify(trace, manifest))


def test_changing_declared_level_without_key_fails():
    trace, manifest = _write_signed(_base_records(), level="L1")
    m = json.loads(Path(manifest).read_text())
    m["declared_autonomy_level"] = "L3"
    Path(manifest).write_text(json.dumps(m))
    assert "manifest: signature is invalid" in aglf.verify(trace, manifest)


def test_human_question_at_l3_fails():
    records = _base_records()
    records[1]["araa"]["human_role"] = "question"
    problems = aglf.verify(*_write_signed(records, level="L3"))
    assert any("not allowed at declared level L3" in p for p in problems)


def test_human_question_at_l1_passes():
    records = _base_records()
    records[1]["araa"]["human_role"] = "question"
    assert aglf.verify(*_write_signed(records, level="L1")) == []


def _chat_with(input_msgs, output_msgs, drop=False):
    records = copy.deepcopy(_base_records())
    attrs = records[2]["attributes"]
    assert attrs["gen_ai.operation.name"] == "chat"
    if drop:
        del attrs["gen_ai.input.messages"], attrs["gen_ai.output.messages"]
    else:
        attrs["gen_ai.input.messages"], attrs["gen_ai.output.messages"] = input_msgs, output_msgs
    return aglf.verify(*_write_signed(records))


def test_chat_without_messages_fails():
    assert any("required property" in p for p in _chat_with(None, None, drop=True))


def test_chat_with_null_messages_fails():
    assert _chat_with(None, None) != []


def test_chat_with_empty_messages_fails():
    assert _chat_with([], []) != []


def test_chat_with_messages_missing_parts_fails():
    assert _chat_with([{"role": "user"}], [{"role": "assistant", "parts": []}]) != []


if __name__ == "__main__":
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    for t in tests:
        t()
        print(f"ok  {t.__name__}")
    print(f"{len(tests)} tests passed")

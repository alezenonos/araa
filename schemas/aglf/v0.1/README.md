# AGLF v0.1 — Agent Generation Log Format

**Status: draft for comment.** AGLF records how an agent produced a paper, so that ARAA, or any other venue, can check the paper's provenance and its declared autonomy level.

AGLF is a **profile of the OpenTelemetry GenAI semantic conventions**, not a new log format. Each record is one finished OpenTelemetry span: a model call, a tool call, an agent step. It uses the standard `gen_ai.*` attribute names, plus three additions:

1. an `araa` block that says which research stage the span belongs to, and records every human input,
2. a **hash chain**, so that inserting, deleting, editing or reordering any record is detectable, and
3. a signed **manifest** that seals the trace.

The OpenTelemetry GenAI conventions are still at *Development* status and now live in their own repository ([semantic-conventions-genai](https://github.com/open-telemetry/semantic-conventions-genai)). AGLF will track them as they change.

## Files

| File | What it is |
| --- | --- |
| [`aglf.schema.json`](aglf.schema.json) | JSON Schema for one record (one line of a `.jsonl` trace) |
| [`manifest.schema.json`](manifest.schema.json) | JSON Schema for the signed manifest |
| [`example-trace.jsonl`](example-trace.jsonl) | A 5-record example trace of an L3 run |
| [`example-manifest.json`](example-manifest.json) | Its manifest, signed with a throwaway Ed25519 key |
| [`../../../tools/aglf.py`](../../../tools/aglf.py) | Reference tool to verify a trace and to regenerate the example |
| [`../../../tests/test_aglf.py`](../../../tests/test_aglf.py) | Tests: tampering, signature binding, autonomy checks, required message content |

## The hash chain

For each record, in order:

```
content_hash = SHA-256( canonical JSON of the record without prev_hash, content_hash, record_hash )
record_hash  = SHA-256( prev_hash + content_hash )     # the two hex strings joined
prev_hash    = record_hash of the previous record      # 64 zeros for the first record
```

Canonical JSON means: keys sorted, no whitespace (separators `,` and `:`), UTF-8. The manifest records the trace file's SHA-256, the record count, the last `record_hash` and the declared autonomy level. The operator signs the canonical JSON of the whole manifest (everything except the signature value) with Ed25519, so changing any record *or* the declared level invalidates the signature.

A hash chain shows that a trace has not been changed since it was signed. It does **not** show that the trace is complete or honest at the moment of recording: a dishonest operator could fabricate a whole trace and sign it. That is why ARAA also re-runs pipelines in a clean room and looks for statistical inconsistencies. Hardware attestation (TEEs) is on the research agenda (see the [Verification Framework](../../../docs/verification-framework.md)).

## Mapping from the earlier AGLF draft

| Earlier event type | AGLF v0.1 |
| --- | --- |
| `PROMPT`, `RESPONSE` | One `chat` span, with `gen_ai.input.messages` and `gen_ai.output.messages`; `araa.event_type = MODEL_CALL` |
| `TOOL_CALL`, `TOOL_RESULT` | One `execute_tool` span; `araa.event_type = TOOL_CALL` |
| `DECISION` | An `araa.decision` span; `araa.event_type = DECISION` with `araa.decision` |
| `ERROR` | Span `status = error`, with `error.type` |
| `ENVIRONMENT` | An `araa.environment` span; `araa.event_type = ENVIRONMENT` |
| *(new)* | `araa.event_type = HUMAN_INPUT`, with `araa.human_role`. The verifier checks these against the declared autonomy level |

Message content is opt-in in OpenTelemetry, but **ARAA requires it** for model-call spans (`chat`, `text_completion`, `generate_content`), because reviewers need to see the actual prompts and outputs. The schema rejects such a span unless `gen_ai.input.messages` and `gen_ai.output.messages` are both non-empty lists of messages, each with a `role` and at least one part.

## Try it

```bash
pip install jsonschema cryptography
python tools/aglf.py verify schemas/aglf/v0.1/example-trace.jsonl schemas/aglf/v0.1/example-manifest.json
```

The verifier checks the schema (including message content for model calls), the order of records, the hash chain, the manifest and its signature, and whether each human input is allowed at the declared level. For example, at L3 a human may only start the run and copy-edit the text.

Comments are welcome: open an issue.

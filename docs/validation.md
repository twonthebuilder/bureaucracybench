# Foundation validation

Validated on 27 September 2026 using Python 3.12.14.

- `python -m unittest discover -s tests -v`: 12 tests passed.
- `python scripts/validate_foundation.py`: 119 archived pages, 47 prompts, 17 explicit Verified statuses, four draft cases and six experimental cells validated.
- `python scripts/validate_schemas.py` with jsonschema 4.25.1: three JSON Schema Draft 2020-12 definitions, four case instances, one model profile and three negative configuration probes passed.
- Python compilation, JSON/TOML parsing and local Markdown-link checks passed.

The tests check source/file hashes, source status evidence, case references and bindings,
fixture isolation, path boundaries, duplicate JSON keys, scheduling fixture consistency,
cycles/missing predecessors, and experiment information parity. They do not validate
model performance, qualitative-rubric reliability, government-framework compliance,
provider conformance or production-host equivalence. No model inference, paid API call,
LLM judging, live government system interaction or fabricated measured result was used.

Schemas remain draft contracts. Result-instance conformance, strict runtime loading,
transport error handling and release calibration require the roadmap's implementation work.

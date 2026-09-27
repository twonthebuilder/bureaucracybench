"""Optional standards-based validation for draft schemas and example definitions.

Install with: python -m pip install -e '.[validation]'
This is not a runtime loader or a complete result-record conformance suite.
"""
from pathlib import Path
import copy
import json
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    schemas = {}
    for path in (ROOT / "schemas").glob("*.schema.json"):
        schema = json.loads(path.read_text())
        Draft202012Validator.check_schema(schema)
        schemas[path.name] = Draft202012Validator(schema, format_checker=FormatChecker())
    cases = list((ROOT / "benchmarks/cases").glob("*.json"))
    for path in cases:
        schemas["case.schema.json"].validate(json.loads(path.read_text()))
    profile = json.loads((ROOT / "examples/model-profile.local.json").read_text())
    validator = schemas["model-profile.schema.json"]
    validator.validate(profile)
    # Negative contract probes: literal secret field, unknown setting and malformed key reference.
    for mutation in [{"api_key": "DUMMY-NOT-A-KEY"}, {"api_key_env": "not an environment variable"}]:
        invalid = {**profile, **mutation}
        if validator.is_valid(invalid):
            raise AssertionError("Invalid credential configuration accepted")
    invalid = copy.deepcopy(profile)
    invalid["settings"]["pretend_setting"] = True
    if validator.is_valid(invalid):
        raise AssertionError("Unknown canonical setting accepted")
    print(f"Validated {len(schemas)} schema definitions, {len(cases)} cases, 1 profile and 3 negative probes.")


if __name__ == "__main__":
    main()

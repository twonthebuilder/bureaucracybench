"""Offline integrity checks for the research foundation, not a model runner.

These are cross-file project checks, not a replacement for JSON Schema validation.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT = "UK-AIKH-2026-09-27-dev-observed"


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def unique_object(pairs: list[tuple[str, object]]) -> dict:
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"Duplicate JSON key: {key}")
        result[key] = value
    return result


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_object)


def child(root: Path, relative: str) -> Path:
    if Path(relative).is_absolute():
        raise ValueError("Absolute artifact path is not allowed")
    result = (root / relative).resolve()
    if not result.is_relative_to(root.resolve()):
        raise ValueError("Artifact path escapes repository")
    return result


def selected_input(root: Path, fixture_ref: dict) -> dict:
    """Explicit visibility boundary used by foundation checks, not full rendering."""
    fixture = load(child(root, fixture_ref["path"]))
    if fixture.get("synthetic") is not True:
        raise ValueError("Fixture must be explicitly synthetic")
    return fixture["input"][fixture_ref["input_key"]]


def earliest_schedule(tasks: list[dict]) -> tuple[dict, dict]:
    """Independent fixture consistency oracle; does not parse/score model output."""
    by_id = {task["id"]: task for task in tasks}
    if len(by_id) != len(tasks):
        raise ValueError("Duplicate task ID")
    pending = dict(by_id)
    starts, finishes = {}, {}
    while pending:
        ready = [t for t in pending.values() if all(p in finishes for p in t["predecessors"])]
        if not ready:
            raise ValueError("Cycle or missing predecessor")
        for task in ready:
            if task["duration_days"] <= 0:
                raise ValueError("Duration must be positive")
            start = max((finishes[p] for p in task["predecessors"]), default=0)
            starts[task["id"]] = start
            finishes[task["id"]] = start + task["duration_days"]
            del pending[task["id"]]
    return starts, finishes


def validate(root: Path = ROOT) -> dict:
    archive = root / "corpus" / "snapshots" / SNAPSHOT
    manifest = load(archive / "manifest.json")
    if manifest["status"] != "research_candidate":
        raise ValueError("Initial observation must retain its research-candidate caveat")
    for name, expected in manifest["files"].items():
        if digest(child(archive, name).read_bytes()) != expected:
            raise ValueError(f"Snapshot hash mismatch: {name}")
    prompts = [json.loads(line, object_pairs_hook=unique_object) for line in (archive / "prompts.jsonl").read_text().splitlines()]
    pages = [json.loads(line, object_pairs_hook=unique_object) for line in (archive / "pages.jsonl").read_text().splitlines()]
    by_id = {p["id"]: p for p in prompts}
    if len(by_id) != len(prompts) or len(prompts) != 47 or len(pages) != 119:
        raise ValueError("Unexpected source coverage or duplicate prompt ID")
    verified = [p for p in prompts if p["verification"]["status"] == "verified"]
    if len(verified) != 17:
        raise ValueError("Unexpected explicit verification count")
    for page in pages:
        if digest(page["text"].encode()) != page["text_sha256"]:
            raise ValueError(f"Page text hash mismatch: {page['path']}")
    for prompt in prompts:
        if digest(prompt["original_prompt"].encode()) != prompt["original_prompt_sha256"]:
            raise ValueError(f"Prompt hash mismatch: {prompt['id']}")
        if prompt["verification"]["status"] == "verified":
            if not prompt["verification"]["index_badge"] or not prompt["verification"]["evidence"]:
                raise ValueError("Verification lacks explicit evidence")
    cases = [load(path) for path in sorted((root / "benchmarks/cases").glob("*.json"))]
    if len({c["id"] for c in cases}) != len(cases):
        raise ValueError("Duplicate case IDs")
    for case in cases:
        source = by_id[case["source"]["prompt_id"]]
        if case["source"]["prompt_sha256"] != source["original_prompt_sha256"]:
            raise ValueError("Case/source digest mismatch")
        if case["source"]["verification_status"] != source["verification"]["status"]:
            raise ValueError("Case/source verification mismatch")
        if "verified" in case["proposed_suites"]:
            if source["verification"]["status"] != "verified" or case["variant"]["kind"] != "faithful":
                raise ValueError("Derived or unverified case in verified suite")
        for binding in case["bindings"]:
            count = source["original_prompt"].count(binding["literal"])
            if count < 1 or count != binding["expected_occurrences"]:
                raise ValueError(f"Invalid literal binding: {case['id']}")
        for ref in case["fixtures"]:
            if digest(child(root, ref["path"]).read_bytes()) != ref["sha256"]:
                raise ValueError("Fixture hash mismatch")
            selected_input(root, ref)
        if case["status"] != "draft" or not case["release_blockers"]:
            raise ValueError("Foundation examples must retain draft status/blockers")
    experiment = load(root / "benchmarks/experiments/framework-persona.json")
    for variant in experiment["variants"]:
        prompt = variant["prompt"]
        if digest(prompt.encode()) != variant["sha256"]:
            raise ValueError("Experiment prompt hash mismatch")
        for name, block in experiment["common_blocks"].items():
            expected_count = 0 if name == "role" and variant["persona"] == "absent" else 1
            if prompt.count(block) != expected_count:
                raise ValueError(f"Information mismatch: {variant['id']}/{name}")
    fixture = load(root / "fixtures/northbridge.json")
    starts, finishes = earliest_schedule(fixture["input"]["schedule"]["tasks"])
    oracle = fixture["oracle"]["schedule"]
    if starts != oracle["earliest_start"] or finishes != oracle["earliest_finish"]:
        raise ValueError("Schedule oracle disagrees with task DAG")
    if max(finishes.values()) != oracle["project_duration_days"]:
        raise ValueError("Project duration is inconsistent")
    if load(root / "corpus/catalog.json")["released_corpora"]:
        raise ValueError("Foundation must not claim a released corpus")
    return {"pages": len(pages), "prompts": len(prompts), "explicitly_verified": len(verified), "draft_cases": len(cases), "experiment_variants": len(experiment["variants"])}


if __name__ == "__main__":
    print(json.dumps(validate(), indent=2))

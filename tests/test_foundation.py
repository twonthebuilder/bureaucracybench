"""Meaningful integrity gates; no inference or secrets required."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("foundation", ROOT / "scripts/validate_foundation.py")
foundation = importlib.util.module_from_spec(spec)
spec.loader.exec_module(foundation)


class FoundationTests(unittest.TestCase):
    def test_archive_and_definitions_are_internally_consistent(self):
        stats = foundation.validate()
        self.assertEqual(stats["prompts"], 47)
        self.assertEqual(stats["draft_cases"], 4)

    def test_hidden_profession_attribute_does_not_make_prompt_verified(self):
        path = ROOT / "corpus/snapshots" / foundation.SNAPSHOT / "prompts.jsonl"
        records = [json.loads(line) for line in path.read_text().splitlines()]
        mismatches = [p for p in records if p["upstream_taxonomy"]["verified_by_profession_attribute"] and p["verification"]["status"] == "not_labelled"]
        self.assertEqual(len(mismatches), 7)
        business = next(p for p in records if p["id"] == "khp:write-a-business-case")
        self.assertEqual(business["verification"]["status"], "not_labelled")

    def test_fixture_selection_excludes_oracle(self):
        selected = foundation.selected_input(ROOT, {"path": "fixtures/northbridge.json", "input_key": "schedule"})
        self.assertNotIn("oracle", selected)
        self.assertNotIn("critical_paths", json.dumps(selected))
        self.assertNotIn("earliest_start", json.dumps(selected))

    def test_fixture_cannot_select_evaluator_only_data(self):
        with self.assertRaises(KeyError):
            foundation.selected_input(ROOT, {"path": "fixtures/northbridge.json", "input_key": "oracle"})

    def test_paths_cannot_escape(self):
        for value in ["../../outside.json", "/etc/passwd"]:
            with self.subTest(value=value), self.assertRaises(ValueError):
                foundation.child(ROOT, value)

    def test_duplicate_keys_are_rejected(self):
        with self.assertRaises(ValueError):
            json.loads('{"status":"draft","status":"released"}', object_pairs_hook=foundation.unique_object)

    def test_schedule_cycle_and_missing_predecessor_rejected(self):
        fixture = foundation.load(ROOT / "fixtures/northbridge.json")
        for pred in ["F", "MISSING"]:
            tasks = copy.deepcopy(fixture["input"]["schedule"]["tasks"])
            tasks[0]["predecessors"] = [pred]
            with self.subTest(pred=pred), self.assertRaises(ValueError):
                foundation.earliest_schedule(tasks)

    def test_schedule_oracle_is_order_independent(self):
        fixture = foundation.load(ROOT / "fixtures/northbridge.json")
        tasks = fixture["input"]["schedule"]["tasks"]
        self.assertEqual(foundation.earliest_schedule(tasks), foundation.earliest_schedule(list(reversed(tasks))))

    def test_schedule_duplicate_task_rejected(self):
        task = {"id": "A", "duration_days": 1, "predecessors": []}
        with self.assertRaises(ValueError):
            foundation.earliest_schedule([task, task])

    def test_framework_experiment_has_six_distinct_cells(self):
        experiment = foundation.load(ROOT / "benchmarks/experiments/framework-persona.json")
        cells = {(v["framework"], v["persona"]) for v in experiment["variants"]}
        self.assertEqual(cells, {(f, p) for f in ["plain", "CRIT", "PICSE"] for p in ["present", "absent"]})
        self.assertFalse(experiment["government_verified"])

    def test_profile_does_not_claim_untested_settings(self):
        profile = foundation.load(ROOT / "examples/model-profile.local.json")
        self.assertEqual(profile["capabilities"]["conformance_status"], "untested")
        self.assertEqual(profile["capabilities"]["supported_settings"], [])
        self.assertIsNone(profile["api_key_env"])
        self.assertIsNone(profile["local_metadata"]["quantization"])

    def test_json_and_toml_parse(self):
        import tomllib
        for path in ROOT.rglob("*.json"):
            foundation.load(path)
        tomllib.loads((ROOT / "pyproject.toml").read_text())


if __name__ == "__main__":
    unittest.main()

import json
import tempfile
import unittest
from pathlib import Path

from tools import validate_repository as validator


SPECIALIZED = {
    "WFL": {
        "trigger": "request accepted",
        "stages": [{"id": "stage-1", "name": "Work", "action": "execute", "on_success": "complete", "on_failure": "escalate"}],
        "state": ["request"],
        "completion_criteria": ["output accepted"],
        "failure_policy": {"retry_limit": 1, "escalation": "owner"},
    },
    "AGT": {
        "mission": "Complete governed work.",
        "instructions": "Follow approved workflows.",
        "capabilities": ["analysis"],
        "tools": [],
        "workflows": [],
        "memory_policy": {},
        "guardrails": ["Do not fabricate."],
        "evaluation_suite": "CO-TST-000001",
    },
    "APP": {
        "product_outcome": "Deliver a governed interface.",
        "users": ["administrator"],
        "interfaces": ["web"],
        "runtime": {"platform": "web", "environment": "test"},
        "data_classification": "internal",
        "capabilities": ["catalog"],
        "deployment": {},
        "test_plan": "CO-TST-000001",
    },
    "TMP": {
        "format": "markdown",
        "source_file": "template.md",
        "variables": [{"name": "title", "required": True}],
        "usage_rules": ["Preserve headings."],
        "produces": "report",
    },
    "KNP": {
        "topics": ["governance"],
        "sources": [{"id": "source-1", "location": "references/source.md", "authority": "owner", "reviewed_at": "2026-07-22"}],
        "retrieval_guidance": "Use the source relevant to the request.",
        "refresh_policy": {"cadence": "quarterly", "stale_after_days": 120},
        "quality_owner": "madamtech",
    },
    "PLY": {
        "business_problem": "Deliver a repeatable outcome.",
        "audience": ["consultant"],
        "entry_criteria": ["request approved"],
        "phases": [{"id": "phase-1", "name": "Execute", "assets": ["CO-SKL-000001"], "outcome": "completed"}],
        "included_assets": ["CO-SKL-000001"],
        "exit_criteria": ["outcome accepted"],
    },
    "SOL": {
        "business_outcome": "Improve delivery consistency.",
        "target_customers": ["small business"],
        "included_assets": ["CO-SKL-000001"],
        "implementation_model": "guided",
        "success_measures": ["acceptance"],
        "support_model": "owner supported",
    },
}


def manifest(asset_type):
    data = {
        "sku": f"CO-{asset_type}-000001",
        "asset_id": "core.fixture.v1",
        "name": "Fixture",
        "asset_type": asset_type,
        "business": "CO",
        "library": "CORE",
        "version": "1.0.0",
        "status": "testing",
        "maturity": 2,
        "description": "A validation fixture with sufficient description.",
        "owners": ["madamtech"],
        "inputs": [],
        "outputs": [],
        "dependencies": [],
    }
    data.update(SPECIALIZED[asset_type])
    return data


class FirstClassManifestValidationTests(unittest.TestCase):
    def validate(self, asset_type, data):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)
            filename = validator.FIRST_CLASS_MANIFESTS[asset_type][0]
            (path / filename).write_text(json.dumps(data), encoding="utf-8")
            errors = []
            validator.validate_manifest(data, path, errors)
            return errors

    def test_all_first_class_manifests_pass(self):
        for asset_type in validator.FIRST_CLASS_MANIFESTS:
            with self.subTest(asset_type=asset_type):
                self.assertEqual([], self.validate(asset_type, manifest(asset_type)))

    def test_missing_specialized_field_fails(self):
        data = manifest("WFL")
        del data["stages"]
        errors = self.validate("WFL", data)
        self.assertTrue(any("manifest missing stages" in error for error in errors))

    def test_catalog_identity_mismatch_fails(self):
        data = manifest("AGT")
        catalog_item = dict(data)
        catalog_item["version"] = "2.0.0"
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)
            (path / "agent.json").write_text(json.dumps(data), encoding="utf-8")
            errors = []
            validator.validate_manifest(catalog_item, path, errors)
        self.assertTrue(any("manifest version mismatch" in error for error in errors))


if __name__ == "__main__":
    unittest.main()

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / "libraries" / "ai-authoritech" / "workflows" / "ai-readiness-accelerator-delivery" / "workflow.json"
PACK = ROOT / "libraries" / "ai-authoritech" / "solution-packs" / "ai-readiness-accelerator" / "solution-pack.json"


class AIReadinessAcceleratorTests(unittest.TestCase):
    def test_workflow_sequence_and_failure_controls(self):
        workflow = json.loads(WORKFLOW.read_text(encoding="utf-8"))
        self.assertEqual([stage["id"] for stage in workflow["stages"]], ["intake", "discovery", "analysis", "strategy", "client_validation", "commercialization", "quality_gate"])
        self.assertEqual(workflow["failure_policy"]["retry_limit"], 2)
        self.assertIn("preserve evidence", workflow["failure_policy"]["escalation"])

    def test_pack_contains_governed_delivery_chain(self):
        pack = json.loads(PACK.read_text(encoding="utf-8"))
        expected = {"AA-WFL-000001", *(f"AA-SKL-{number:06d}" for number in range(1, 11))}
        self.assertEqual(set(pack["included_assets"]), expected)
        self.assertEqual(set(pack["dependencies"]), expected)

    def test_operational_templates_exist(self):
        template_dir = PACK.parent / "templates"
        for name in ("client-intake.md", "quality-gate.md", "field-evidence-record.md"):
            path = template_dir / name
            self.assertTrue(path.is_file())
            self.assertGreater(len(path.read_text(encoding="utf-8")), 500)


if __name__ == "__main__":
    unittest.main()

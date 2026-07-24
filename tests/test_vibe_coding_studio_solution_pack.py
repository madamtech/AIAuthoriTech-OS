import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
def load(path): return json.loads((ROOT / path).read_text(encoding="utf-8"))

class VibeCodingStudioTests(unittest.TestCase):
    def test_workflow_order_and_retry(self):
        w = load("libraries/ai-authoritech/workflows/vibe-coding-studio-delivery/workflow.json")
        self.assertEqual([s["id"] for s in w["stages"]], ["intake","requirements","experience_architecture","implementation","verification","deployment","operations"])
        self.assertEqual(w["failure_policy"]["retry_limit"], 2)
    def test_app_release_and_environments(self):
        a = load("libraries/ai-authoritech/apps/vibe-coding-studio/app.json")
        self.assertIn("No production deployment", a["deployment"]["default"])
        self.assertIn("staging", a["runtime"]["environment"])
    def test_pack_assets_match_dependencies(self):
        p = load("libraries/ai-authoritech/solution-packs/vibe-coding-studio/solution-pack.json")
        expected = ["AA-APP-000001","AA-WFL-000003"] + [f"AA-SKL-{n:06d}" for n in range(22,50)]
        self.assertEqual(p["included_assets"], expected)
        self.assertEqual(p["dependencies"], expected)
    def test_controlled_example_preserves_claim_boundary(self):
        text = (ROOT / "libraries/ai-authoritech/solution-packs/vibe-coding-studio/examples/synthetic-client-portal.md").read_text(encoding="utf-8").lower()
        self.assertIn("conditional pass", text)
        self.assertIn("production readiness remained blocked", text)

if __name__ == "__main__": unittest.main()

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "libraries" / "ai-authoritech" / "skills" / "automation-engineering"
EXPECTED = {
    "api-readiness-assessment": ["references/api-readiness-standard.md", "assets/api-readiness-report-template.md"],
    "automation-risk-analyzer": ["references/automation-risk-standard.md", "assets/automation-risk-register-template.md"],
    "automation-cost-estimator": ["references/automation-cost-standard.md", "assets/automation-cost-model-template.md"],
    "automation-prioritization-matrix": ["references/automation-prioritization-standard.md", "assets/automation-prioritization-matrix-template.md"],
    "workflow-automation-designer": ["references/workflow-automation-design-standard.md", "assets/workflow-automation-specification-template.md"],
    "n8n-workflow-planner": ["references/n8n-planning-standard.md", "assets/n8n-implementation-plan-template.md"],
}

class AutomationDeliveryHardeningTests(unittest.TestCase):
    def test_skills_have_precise_descriptions_and_controls(self):
        for slug in EXPECTED:
            with self.subTest(skill=slug):
                text = (BASE / slug / "SKILL.md").read_text(encoding="utf-8")
                match = re.match(r"^---\s*\n(.*?)\n---", text, flags=re.DOTALL)
                self.assertIsNotNone(match)
                description = next(line.split(":", 1)[1].strip() for line in match.group(1).splitlines() if line.startswith("description:"))
                self.assertGreaterEqual(len(description), 180)
                for heading in ("## Procedure", "## Output Contract", "## Guardrails", "## Recovery"):
                    self.assertIn(heading, text)
                self.assertNotRegex(text, r"[^\x00-\x7F]")
                self.assertNotIn("TODO", text)

    def test_referenced_resources_exist_and_are_substantive(self):
        for slug, resources in EXPECTED.items():
            for resource in resources:
                path = BASE / slug / resource
                self.assertTrue(path.is_file(), resource)
                self.assertGreaterEqual(len(path.read_text(encoding="utf-8")), 250)

if __name__ == "__main__":
    unittest.main()

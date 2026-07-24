import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONSULTING = ROOT / "libraries" / "ai-authoritech" / "skills" / "consulting"
EXPECTED = {
    "roi-calculator": ["references/business-case-method.md", "assets/roi-business-case-template.md"],
    "executive-proposal-builder": ["references/proposal-evidence-standard.md", "assets/executive-proposal-template.md"],
    "statement-of-work-builder": ["references/sow-control-standard.md", "assets/statement-of-work-template.md"],
    "implementation-planner": ["references/implementation-standard.md", "assets/implementation-plan-template.md"],
}


class ConsultingDeliveryHardeningTests(unittest.TestCase):
    def test_skills_have_precise_descriptions_and_controls(self):
        for slug in EXPECTED:
            with self.subTest(skill=slug):
                text = (CONSULTING / slug / "SKILL.md").read_text(encoding="utf-8")
                match = re.match(r"^---\s*\n(.*?)\n---", text, flags=re.DOTALL)
                self.assertIsNotNone(match)
                description = next(
                    line.split(":", 1)[1].strip()
                    for line in match.group(1).splitlines()
                    if line.startswith("description:")
                )
                self.assertGreaterEqual(len(description), 180)
                for heading in ("## Procedure", "## Output Contract", "## Guardrails", "## Recovery"):
                    self.assertIn(heading, text)
                self.assertNotIn("TODO", text)

    def test_referenced_resources_exist_and_are_substantive(self):
        for slug, resources in EXPECTED.items():
            for resource in resources:
                with self.subTest(skill=slug, resource=resource):
                    path = CONSULTING / slug / resource
                    self.assertTrue(path.is_file(), resource)
                    self.assertGreaterEqual(len(path.read_text(encoding="utf-8")), 250)


if __name__ == "__main__":
    unittest.main()

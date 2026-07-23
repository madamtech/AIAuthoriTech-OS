import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONSULTING = ROOT / "libraries" / "ai-authoritech" / "skills" / "consulting"
EXPECTED = {
    "ai-readiness-assessment": ["references/readiness-scoring-standard.md", "assets/ai-readiness-report-template.md"],
    "workflow-discovery": ["references/current-state-mapping-standard.md", "assets/workflow-discovery-template.md"],
    "automation-opportunity-analysis": ["references/opportunity-scoring.md", "assets/opportunity-portfolio-template.md"],
    "ai-strategy-roadmap": ["references/roadmap-method.md", "assets/strategy-roadmap-template.md"],
    "ai-use-case-prioritizer": ["references/use-case-scoring.md", "assets/use-case-portfolio-template.md"],
    "ai-governance-review": ["references/governance-control-model.md", "assets/governance-review-template.md"],
}


class ConsultingHardeningTests(unittest.TestCase):
    def test_skills_have_precise_descriptions_and_controls(self):
        for slug in EXPECTED:
            with self.subTest(skill=slug):
                text = (CONSULTING / slug / "SKILL.md").read_text(encoding="utf-8")
                match = re.match(r"^---\s*\n(.*?)\n---", text, flags=re.DOTALL)
                self.assertIsNotNone(match)
                frontmatter = match.group(1)
                description = next(
                    line.split(":", 1)[1].strip()
                    for line in frontmatter.splitlines()
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

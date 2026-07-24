import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CORE = ROOT / "libraries" / "core-os" / "skills"
EXPECTED = {
    "skill-library-architect": ["references/skill-package-standard.md", "assets/skill-design-brief-template.md"],
    "skill-quality-reviewer": ["references/quality-rubric.md", "assets/skill-review-report-template.md"],
    "skill-router": ["references/routing-standard.md", "assets/routing-decision-template.json"],
    "workflow-composer": ["references/workflow-design-standard.md", "assets/workflow-design-template.json"],
}


class CoreOsHardeningTests(unittest.TestCase):
    def test_core_skills_have_precise_descriptions_and_controls(self):
        for slug in EXPECTED:
            with self.subTest(skill=slug):
                text = (CORE / slug / "SKILL.md").read_text(encoding="utf-8")
                frontmatter = re.match(r"^---\s*\n(.*?)\n---", text, flags=re.DOTALL).group(1)
                description = next(line.split(":", 1)[1].strip() for line in frontmatter.splitlines() if line.startswith("description:"))
                self.assertGreaterEqual(len(description), 180)
                for heading in ("## Procedure", "## Output Contract", "## Guardrails", "## Recovery"):
                    self.assertIn(heading, text)
                self.assertNotIn("TODO", text)

    def test_referenced_resources_exist(self):
        for slug, resources in EXPECTED.items():
            with self.subTest(skill=slug):
                for resource in resources:
                    self.assertTrue((CORE / slug / resource).is_file(), resource)

    def test_json_templates_parse(self):
        for relative in (
            "skill-router/assets/routing-decision-template.json",
            "workflow-composer/assets/workflow-design-template.json",
        ):
            with self.subTest(template=relative):
                json.loads((CORE / relative).read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()

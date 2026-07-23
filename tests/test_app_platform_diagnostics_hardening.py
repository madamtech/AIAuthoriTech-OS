import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "libraries" / "ai-authoritech" / "skills" / "app-engineering"
EXPECTED = {
    "mobile-app-planner": ["references/mobile-app-standard.md", "assets/mobile-app-plan-template.md"],
    "desktop-app-planner": ["references/desktop-app-standard.md", "assets/desktop-app-plan-template.md"],
    "prompt-to-app-converter": ["references/prompt-to-app-standard.md", "assets/prompt-to-app-build-packet.md"],
    "bug-investigation-assistant": ["references/bug-investigation-standard.md", "assets/bug-investigation-report-template.md"],
    "error-log-analyzer": ["references/error-log-analysis-standard.md", "assets/error-log-analysis-report-template.md"],
    "refactoring-advisor": ["references/refactoring-standard.md", "assets/refactoring-advice-template.md"],
}


class AppPlatformDiagnosticsHardeningTests(unittest.TestCase):
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

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    "knowledge-engineering/knowledge-governance-manager": ["references/knowledge-governance-standard.md", "assets/knowledge-governance-plan-template.md"],
    "knowledge-engineering/knowledge-refresh-manager": ["references/knowledge-refresh-standard.md", "assets/knowledge-refresh-plan-template.md"],
    "knowledge-engineering/knowledge-migration-planner": ["references/knowledge-migration-standard.md", "assets/knowledge-migration-plan-template.md"],
    "automation-engineering/automation-blueprint-builder": ["references/automation-blueprint-standard.md", "assets/automation-blueprint-template.md"],
    "automation-engineering/automation-architecture-designer": ["references/automation-architecture-standard.md", "assets/automation-architecture-template.md"],
    "automation-engineering/integration-planner": ["references/integration-planning-standard.md", "assets/integration-plan-template.md"],
}

class KnowledgeAutomationHardeningTests(unittest.TestCase):
    def test_skills_have_precise_descriptions_and_controls(self):
        for relative in EXPECTED:
            with self.subTest(skill=relative):
                text = (ROOT / "libraries" / "ai-authoritech" / "skills" / relative / "SKILL.md").read_text(encoding="utf-8")
                match = re.match(r"^---\s*\n(.*?)\n---", text, flags=re.DOTALL)
                self.assertIsNotNone(match)
                description = next(line.split(":", 1)[1].strip() for line in match.group(1).splitlines() if line.startswith("description:"))
                self.assertGreaterEqual(len(description), 180)
                for heading in ("## Procedure", "## Output Contract", "## Guardrails", "## Recovery"):
                    self.assertIn(heading, text)
                self.assertNotRegex(text, r"[^\x00-\x7F]")
                self.assertNotIn("TODO", text)

    def test_referenced_resources_exist_and_are_substantive(self):
        for relative, resources in EXPECTED.items():
            base = ROOT / "libraries" / "ai-authoritech" / "skills" / relative
            for resource in resources:
                path = base / resource
                self.assertTrue(path.is_file(), resource)
                self.assertGreaterEqual(len(path.read_text(encoding="utf-8")), 250)

if __name__ == "__main__":
    unittest.main()

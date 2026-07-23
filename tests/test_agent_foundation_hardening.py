import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    "libraries/ai-authoritech/skills/agent-engineering/agent-architect": ["references/agent-architecture-standard.md", "assets/agent-architecture-template.md"],
    "libraries/ai-authoritech/skills/agent-engineering/agent-instruction-builder": ["references/instruction-layer-standard.md", "assets/agent-instruction-template.md"],
    "libraries/ai-authoritech/skills/knowledge-engineering/knowledge-base-builder": ["references/knowledge-governance-standard.md", "assets/knowledge-base-design-template.md"],
    "libraries/ai-authoritech/skills/agent-engineering/agent-workflow-builder": ["references/agent-workflow-standard.md", "assets/agent-workflow-template.md"],
    "libraries/ai-authoritech/skills/agent-engineering/agent-qa-reviewer": ["references/agent-qa-standard.md", "assets/agent-qa-report-template.md"],
}


class AgentFoundationHardeningTests(unittest.TestCase):
    def test_skills_have_precise_descriptions_and_controls(self):
        for relative in EXPECTED:
            with self.subTest(skill=relative):
                text = (ROOT / relative / "SKILL.md").read_text(encoding="utf-8")
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
            for resource in resources:
                with self.subTest(skill=relative, resource=resource):
                    path = ROOT / relative / resource
                    self.assertTrue(path.is_file(), resource)
                    self.assertGreaterEqual(len(path.read_text(encoding="utf-8")), 250)


if __name__ == "__main__":
    unittest.main()

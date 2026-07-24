import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = {
    "libraries/ai-authoritech/skills/app-engineering/production-readiness-reviewer": ["references/production-readiness-standard.md", "assets/production-readiness-review-template.md"],
    "libraries/ai-authoritech/skills/app-engineering/front-end-generator": ["references/front-end-generation-standard.md", "assets/front-end-implementation-packet.md"],
    "libraries/ai-authoritech/skills/app-engineering/backend-architecture-planner": ["references/backend-architecture-standard.md", "assets/backend-architecture-template.md"],
    "libraries/ai-authoritech/skills/app-engineering/mcp-integration-planner": ["references/mcp-integration-standard.md", "assets/mcp-integration-plan-template.md"],
    "libraries/ai-authoritech/skills/prompt-engineering/prompt-architect": ["references/prompt-architecture-standard.md", "assets/prompt-contract-template.md"],
    "libraries/ai-authoritech/skills/prompt-engineering/prompt-optimizer": ["references/prompt-optimization-standard.md", "assets/prompt-optimization-report-template.md"],
}


class AppPromptFoundationHardeningTests(unittest.TestCase):
    def test_skills_have_precise_descriptions_and_controls(self):
        for relative in SKILLS:
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
        for relative, resources in SKILLS.items():
            for resource in resources:
                path = ROOT / relative / resource
                self.assertTrue(path.is_file(), resource)
                self.assertGreaterEqual(len(path.read_text(encoding="utf-8")), 250)


if __name__ == "__main__":
    unittest.main()

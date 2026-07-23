import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "libraries" / "ai-authoritech" / "skills" / "agent-engineering"
EXPECTED = {
    "agent-deployment-planner": ["references/agent-deployment-standard.md", "assets/agent-deployment-plan-template.md"],
    "agent-monitoring-and-optimization": ["references/agent-monitoring-standard.md", "assets/agent-operations-review-template.md"],
    "multi-agent-system-designer": ["references/multi-agent-design-standard.md", "assets/multi-agent-system-template.md"],
    "agent-memory-architect": ["references/agent-memory-standard.md", "assets/agent-memory-design-template.md"],
    "agent-tool-integration-designer": ["references/agent-tool-standard.md", "assets/agent-tool-integration-template.md"],
    "agent-marketplace-packager": ["references/agent-marketplace-standard.md", "assets/agent-marketplace-package-template.md"],
}


class AgentOperationsHardeningTests(unittest.TestCase):
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
                with self.subTest(skill=slug, resource=resource):
                    path = BASE / slug / resource
                    self.assertTrue(path.is_file(), resource)
                    self.assertGreaterEqual(len(path.read_text(encoding="utf-8")), 250)


if __name__ == "__main__":
    unittest.main()

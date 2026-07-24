import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "libraries" / "ai-authoritech" / "skills" / "knowledge-engineering"
EXPECTED = {
    "document-intelligence": ["references/document-intelligence-standard.md", "assets/document-intelligence-report-template.md"],
    "taxonomy-builder": ["references/taxonomy-standard.md", "assets/taxonomy-package-template.md"],
    "ontology-builder": ["references/ontology-standard.md", "assets/ontology-package-template.md"],
    "semantic-search-designer": ["references/semantic-search-standard.md", "assets/semantic-search-design-template.md"],
    "rag-architect": ["references/rag-architecture-standard.md", "assets/rag-architecture-template.md"],
    "knowledge-quality-reviewer": ["references/knowledge-quality-standard.md", "assets/knowledge-quality-review-template.md"],
}

class KnowledgeFoundationHardeningTests(unittest.TestCase):
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

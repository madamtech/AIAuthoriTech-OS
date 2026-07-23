import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "libraries" / "madamallure" / "skills"
EXPECTED = {
    "natural-cosmetic-formula-architect": ["references/cosmetic-formulation-safety-standard.md", "assets/formula-development-record.md"],
    "anhydrous-body-care-formulator": ["references/anhydrous-formulation-standard.md", "assets/anhydrous-formula-record.md"],
    "lotion-and-facial-care-formulator": ["references/emulsion-safety-standard.md", "assets/emulsion-formula-record.md"],
    "bath-and-soap-formula-planner": ["references/bath-soap-safety-standard.md", "assets/bath-soap-formula-record.md"],
    "fragrance-oil-formulator": ["references/fragrance-oil-safety-standard.md", "assets/fragrance-oil-formula-record.md"],
    "custom-cosmetic-order-formulator": ["references/custom-formulation-standard.md", "assets/custom-formulation-order-brief.md"],
}


class MadamAllureFormulationSuiteTests(unittest.TestCase):
    def test_skills_have_metadata_controls_and_resources(self):
        for slug, resources in EXPECTED.items():
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
                for resource in resources:
                    path = BASE / slug / resource
                    self.assertTrue(path.is_file(), resource)
                    self.assertGreaterEqual(len(path.read_text(encoding="utf-8")), 250)

    def test_catalog_registration_and_skus(self):
        assets = json.loads((ROOT / "catalog" / "assets.json").read_text(encoding="utf-8"))["assets"]
        indexed = {item["sku"]: item for item in assets}
        for number, slug in enumerate(EXPECTED, start=51):
            sku = f"MA-SKL-{number:06d}"
            self.assertIn(sku, indexed)
            self.assertEqual(indexed[sku]["path"], f"libraries/madamallure/skills/{slug}")
            self.assertEqual(indexed[sku]["library"], "BEAUTY")


if __name__ == "__main__":
    unittest.main()

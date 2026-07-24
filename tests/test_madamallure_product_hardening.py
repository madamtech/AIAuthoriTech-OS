import re, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; BASE=ROOT/"libraries/madamallure/skills"
EXPECTED={"three-d-print-project-planner":["references/three-d-print-standard.md","assets/three-d-print-plan-template.md"],"laser-engraving-project-planner":["references/laser-safety-standard.md","assets/laser-project-template.md"],"custom-product-designer":["references/custom-product-standard.md","assets/custom-product-template.md"],"filament-material-advisor":["references/filament-selection-standard.md","assets/filament-selection-template.md"],"print-production-optimizer":["references/print-optimization-standard.md","assets/print-optimization-template.md"],"product-cost-calculator":["references/product-costing-standard.md","assets/product-cost-template.md"],"product-catalog-builder":["references/catalog-content-standard.md","assets/product-catalog-template.md"],"custom-order-planner":["references/custom-order-standard.md","assets/custom-order-template.md"],"packaging-designer":["references/packaging-design-standard.md","assets/packaging-design-template.md"],"ecommerce-listing-builder":["references/ecommerce-listing-standard.md","assets/ecommerce-listing-template.md"]}
class MadamAllureProductHardeningTests(unittest.TestCase):
 def test_controls(self):
  for slug in EXPECTED:
   text=(BASE/slug/"SKILL.md").read_text(encoding="utf-8"); m=re.match(r"^---\s*\n(.*?)\n---",text,flags=re.DOTALL); self.assertIsNotNone(m)
   desc=next(x.split(":",1)[1].strip() for x in m.group(1).splitlines() if x.startswith("description:")); self.assertGreaterEqual(len(desc),180)
   for h in ("## Procedure","## Output Contract","## Guardrails","## Recovery"): self.assertIn(h,text)
   self.assertNotRegex(text,r"[^\x00-\x7F]"); self.assertNotIn("TODO",text)
 def test_resources(self):
  for slug,rs in EXPECTED.items():
   for r in rs:
    p=BASE/slug/r; self.assertTrue(p.is_file()); self.assertGreaterEqual(len(p.read_text(encoding="utf-8")),250)

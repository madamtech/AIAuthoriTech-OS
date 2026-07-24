import re, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; BASE=ROOT/"libraries/madamallure/skills"
EXPECTED={"luxury-collection-planner":["references/collection-planning-standard.md","assets/collection-plan-template.md"],"fragrance-concept-designer":["references/fragrance-concept-standard.md","assets/fragrance-concept-template.md"],"beauty-product-description-builder":["references/beauty-copy-standard.md","assets/beauty-copy-template.md"],"personalized-gift-planner":["references/gift-planning-standard.md","assets/gift-plan-template.md"],"brand-voice-builder":["references/brand-voice-standard.md","assets/brand-voice-template.md"],"luxury-collection-namer":["references/collection-naming-standard.md","assets/collection-naming-template.md"],"inventory-replenishment-planner":["references/inventory-standard.md","assets/inventory-plan-template.md"],"order-fulfillment-planner":["references/fulfillment-standard.md","assets/fulfillment-plan-template.md"],"product-launch-planner":["references/launch-standard.md","assets/launch-plan-template.md"],"social-content-generator":["references/social-content-standard.md","assets/social-content-template.md"]}
class MadamAllureBrandOperationsHardeningTests(unittest.TestCase):
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

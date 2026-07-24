import re, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; BASE=ROOT/'libraries/madamallure/skills'
EXPECTED={'stl-production-planner': ['references/stl-production-standard.md', 'assets/stl-production-template.md'], 'slicer-profile-builder': ['references/slicer-profile-standard.md', 'assets/slicer-profile-template.md'], 'print-failure-diagnoser': ['references/print-diagnosis-standard.md', 'assets/print-diagnosis-template.md'], 'laser-layout-optimizer': ['references/laser-layout-standard.md', 'assets/laser-layout-template.md'], 'personalization-layout-designer': ['references/personalization-layout-standard.md', 'assets/personalization-layout-template.md'], 'materials-inventory-controller': ['references/materials-inventory-standard.md', 'assets/materials-inventory-template.md'], 'finished-product-inspector': ['references/finished-product-standard.md', 'assets/finished-product-template.md'], 'promotion-pricing-planner': ['references/promotion-pricing-standard.md', 'assets/promotion-pricing-template.md'], 'email-campaign-builder': ['references/email-campaign-standard.md', 'assets/email-campaign-template.md'], 'holiday-collection-planner': ['references/holiday-collection-standard.md', 'assets/holiday-collection-template.md']}
class BatchHardeningTests(unittest.TestCase):
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

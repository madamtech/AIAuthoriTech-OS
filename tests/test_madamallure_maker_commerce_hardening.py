import re, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; BASE=ROOT/'libraries/madamallure/skills'
EXPECTED={'svg-production-planner': ['references/svg-production-standard.md', 'assets/svg-production-template.md'], 'laser-settings-validator': ['references/laser-settings-standard.md', 'assets/laser-settings-template.md'], 'three-d-print-quality-reviewer': ['references/print-quality-standard.md', 'assets/print-quality-template.md'], 'maker-equipment-maintenance-planner': ['references/equipment-maintenance-standard.md', 'assets/equipment-maintenance-template.md'], 'supplier-sourcing-planner': ['references/supplier-sourcing-standard.md', 'assets/supplier-sourcing-template.md'], 'product-photography-planner': ['references/product-photography-standard.md', 'assets/product-photography-template.md'], 'storefront-merchandising-planner': ['references/merchandising-standard.md', 'assets/merchandising-template.md'], 'customer-care-response-builder': ['references/customer-care-standard.md', 'assets/customer-care-template.md'], 'returns-resolution-planner': ['references/returns-resolution-standard.md', 'assets/returns-resolution-template.md'], 'maker-production-scheduler': ['references/production-scheduling-standard.md', 'assets/production-scheduling-template.md']}
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

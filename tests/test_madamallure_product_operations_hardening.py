import re, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; BASE=ROOT/'libraries/madamallure/skills'
EXPECTED={'skincare-concept-planner': ['references/skincare-concept-standard.md', 'assets/skincare-concept-template.md'], 'body-care-concept-planner': ['references/body-care-concept-standard.md', 'assets/body-care-concept-template.md'], 'cosmetic-labeling-brief-builder': ['references/cosmetic-labeling-standard.md', 'assets/cosmetic-labeling-brief-template.md'], 'beauty-batch-production-planner': ['references/beauty-batch-production-standard.md', 'assets/beauty-batch-production-template.md'], 'gift-box-designer': ['references/gift-box-design-standard.md', 'assets/gift-box-design-template.md'], 'wholesale-pricing-planner': ['references/wholesale-pricing-standard.md', 'assets/wholesale-pricing-template.md'], 'supplier-performance-scorecard': ['references/supplier-performance-standard.md', 'assets/supplier-performance-template.md'], 'customer-review-analyzer': ['references/customer-review-analysis-standard.md', 'assets/customer-review-analysis-template.md'], 'customer-retention-campaign-planner': ['references/retention-campaign-standard.md', 'assets/retention-campaign-template.md'], 'maker-dashboard-requirements-builder': ['references/maker-dashboard-standard.md', 'assets/maker-dashboard-requirements-template.md']}
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

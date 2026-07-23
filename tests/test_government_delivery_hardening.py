import re, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; BASE=ROOT/"libraries/ai-authoritech/skills/government"
EXPECTED={"public-sector-ai-implementation-planner":["references/implementation-standard.md","assets/implementation-plan-template.md"],"public-sector-stakeholder-engagement-planner":["references/stakeholder-engagement-standard.md","assets/engagement-plan-template.md"],"government-ai-executive-brief-builder":["references/executive-brief-standard.md","assets/executive-brief-template.md"],"government-ai-system-inventory-builder":["references/system-inventory-standard.md","assets/system-inventory-template.md"],"algorithmic-impact-assessment-builder":["references/impact-assessment-standard.md","assets/impact-assessment-template.md"],"public-ai-transparency-notice-builder":["references/transparency-notice-standard.md","assets/transparency-notice-template.md"]}
class GovernmentDeliveryHardeningTests(unittest.TestCase):
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

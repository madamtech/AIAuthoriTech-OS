import re, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; BASE=ROOT/'libraries/ai-authoritech/skills/content-marketing'
EXPECTED={'case-study-builder': ['references/case-study-standard.md', 'assets/case-study-template.md'], 'landing-page-builder': ['references/landing-page-standard.md', 'assets/landing-page-template.md'], 'email-sequence-builder': ['references/email-sequence-standard.md', 'assets/email-sequence-template.md'], 'lead-magnet-builder': ['references/lead-magnet-standard.md', 'assets/lead-magnet-template.md'], 'webinar-content-planner': ['references/webinar-content-standard.md', 'assets/webinar-content-template.md'], 'thought-leadership-builder': ['references/thought-leadership-standard.md', 'assets/thought-leadership-template.md'], 'business-newsletter-builder': ['references/business-newsletter-standard.md', 'assets/business-newsletter-template.md'], 'testimonial-evidence-builder': ['references/testimonial-evidence-standard.md', 'assets/testimonial-evidence-template.md'], 'content-performance-analyzer': ['references/content-performance-standard.md', 'assets/content-performance-template.md'], 'marketing-campaign-brief-builder': ['references/campaign-brief-standard.md', 'assets/campaign-brief-template.md']}
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

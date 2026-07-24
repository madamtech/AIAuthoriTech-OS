import re, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; BASE=ROOT/'libraries/ai-authoritech/skills'
EXPECTED={'government/government-ai-audit-evidence-builder': ['references/audit-evidence-standard.md', 'assets/audit-evidence-index-template.md'], 'content-marketing/content-strategy-builder': ['references/content-strategy-standard.md', 'assets/content-strategy-template.md'], 'content-marketing/content-repurposing-engine': ['references/content-repurposing-standard.md', 'assets/content-repurposing-template.md'], 'content-marketing/website-messaging-auditor': ['references/website-messaging-audit-standard.md', 'assets/website-messaging-audit-template.md'], 'content-marketing/seo-content-auditor': ['references/seo-content-audit-standard.md', 'assets/seo-content-audit-template.md'], 'content-marketing/ai-brand-voice-builder': ['references/brand-voice-standard.md', 'assets/brand-voice-template.md'], 'content-marketing/business-social-content-generator': ['references/social-content-standard.md', 'assets/social-content-template.md'], 'content-marketing/cta-optimizer': ['references/cta-optimization-standard.md', 'assets/cta-optimization-template.md'], 'content-marketing/competitor-content-analyzer': ['references/competitor-content-standard.md', 'assets/competitor-content-analysis-template.md'], 'content-marketing/editorial-calendar-builder': ['references/editorial-calendar-standard.md', 'assets/editorial-calendar-template.md']}
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

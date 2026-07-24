import re, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; BASE=ROOT/"libraries/ai-authoritech/skills/government"
EXPECTED={"public-sector-ai-governance-reviewer":["references/governance-review-standard.md","assets/governance-review-template.md"],"ai-procurement-requirements-builder":["references/ai-procurement-standard.md","assets/procurement-requirements-template.md"],"public-sector-ai-risk-assessor":["references/public-sector-risk-standard.md","assets/risk-assessment-template.md"],"government-data-readiness-assessor":["references/government-data-readiness-standard.md","assets/data-readiness-report-template.md"],"public-sector-ai-workforce-planner":["references/public-sector-workforce-standard.md","assets/workforce-plan-template.md"],"government-ai-use-case-prioritizer":["references/government-prioritization-standard.md","assets/use-case-portfolio-template.md"]}
class GovernmentAIHardeningTests(unittest.TestCase):
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

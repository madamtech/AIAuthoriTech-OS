import re, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; BASE=ROOT/"libraries/ai-authoritech/skills/government"
EXPECTED={"government-ai-incident-response-planner":["references/incident-response-standard.md","assets/incident-response-plan-template.md"],"public-sector-ai-accessibility-reviewer":["references/accessibility-review-standard.md","assets/accessibility-review-template.md"],"government-ai-records-planner":["references/ai-records-standard.md","assets/records-plan-template.md"],"public-sector-ai-vendor-monitor":["references/vendor-monitoring-standard.md","assets/vendor-scorecard-template.md"],"government-ai-pilot-evaluator":["references/pilot-evaluation-standard.md","assets/pilot-evaluation-template.md"],"community-ai-impact-reviewer":["references/community-impact-standard.md","assets/community-impact-review-template.md"]}
class GovernmentOperationsHardeningTests(unittest.TestCase):
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

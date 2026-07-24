import re, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; BASE=ROOT/"libraries/ipro-lms/skills"
EXPECTED={"workday-learning-assignment-planner":["references/assignment-control-standard.md","assets/assignment-plan-template.md"],"workday-learning-campaign-manager":["references/campaign-governance-standard.md","assets/campaign-plan-template.md"],"workday-learning-security-reviewer":["references/learning-security-standard.md","assets/security-review-template.md"],"netexam-exam-import-formatter":["references/exam-import-standard.md","assets/exam-import-template.md"],"netexam-reporting-specialist":["references/netexam-reporting-standard.md","assets/netexam-report-template.md"],"scorm-import-assistant":["references/scorm-import-standard.md","assets/scorm-import-template.md"],"lms-migration-planner":["references/migration-control-standard.md","assets/migration-plan-template.md"],"lms-dashboard-designer":["references/dashboard-design-standard.md","assets/dashboard-design-template.md"],"lms-governance-reviewer":["references/lms-governance-standard.md","assets/governance-review-template.md"],"learning-data-quality-auditor":["references/learning-data-quality-standard.md","assets/data-quality-audit-template.md"]}
class LmsControlsHardeningTests(unittest.TestCase):
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

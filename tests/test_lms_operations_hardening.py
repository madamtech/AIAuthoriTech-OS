import re, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; BASE=ROOT/"libraries/ipro-lms/skills"
EXPECTED={"workday-learning-configuration-planner":["references/workday-configuration-standard.md","assets/workday-configuration-template.md"],"netexam-course-builder":["references/netexam-course-standard.md","assets/netexam-course-build-template.md"],"ilt-session-manager":["references/ilt-operations-standard.md","assets/ilt-session-control-template.md"],"certificate-generation-planner":["references/certificate-control-standard.md","assets/certificate-generation-template.md"],"lms-notification-designer":["references/notification-governance-standard.md","assets/lms-notification-template.md"],"salesforce-learning-integration-planner":["references/learning-integration-standard.md","assets/salesforce-integration-template.md"],"netexam-branch-manager":["references/netexam-branch-standard.md","assets/netexam-branch-template.md"],"learner-user-lifecycle-manager":["references/learner-lifecycle-standard.md","assets/learner-lifecycle-template.md"],"lms-catalog-manager":["references/catalog-governance-standard.md","assets/lms-catalog-template.md"],"learning-analytics-designer":["references/learning-analytics-standard.md","assets/learning-analytics-template.md"]}
class LmsOperationsHardeningTests(unittest.TestCase):
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

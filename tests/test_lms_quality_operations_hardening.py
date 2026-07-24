import re, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; BASE=ROOT/"libraries/ipro-lms/skills"
EXPECTED={"learning-content-qa-reviewer":["references/content-qa-standard.md","assets/content-qa-template.md"],"learning-accessibility-reviewer":["references/learning-accessibility-standard.md","assets/accessibility-review-template.md"],"learning-localization-manager":["references/localization-control-standard.md","assets/localization-plan-template.md"],"exam-performance-analyzer":["references/exam-analysis-standard.md","assets/exam-analysis-template.md"],"certification-health-monitor":["references/certification-monitoring-standard.md","assets/certification-health-template.md"],"learning-audit-evidence-builder":["references/audit-evidence-standard.md","assets/audit-evidence-template.md"],"lms-release-manager":["references/lms-release-standard.md","assets/release-control-template.md"],"learning-integration-monitor":["references/integration-monitoring-standard.md","assets/integration-monitor-template.md"],"learner-support-triage":["references/learner-support-standard.md","assets/support-triage-template.md"],"training-operations-planner":["references/training-operations-standard.md","assets/training-operations-template.md"]}
class LmsQualityOperationsHardeningTests(unittest.TestCase):
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

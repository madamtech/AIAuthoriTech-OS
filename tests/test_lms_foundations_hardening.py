import re, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; BASE=ROOT/"libraries/ipro-lms/skills"
EXPECTED={"course-blueprint-builder":["references/course-design-standard.md","assets/course-blueprint-template.md"],"certification-program-designer":["references/certification-governance-standard.md","assets/certification-program-template.md"],"netexam-certification-builder":["references/netexam-build-standard.md","assets/netexam-build-workbook-template.md"],"certification-renewal-manager":["references/renewal-lifecycle-standard.md","assets/renewal-control-template.md"],"exam-builder":["references/exam-development-standard.md","assets/exam-item-template.md"],"exam-qa-reviewer":["references/exam-qa-standard.md","assets/exam-qa-report-template.md"],"scorm-validator":["references/scorm-validation-standard.md","assets/scorm-test-record-template.md"],"learning-path-designer":["references/learning-path-standard.md","assets/learning-path-design-template.md"],"lms-report-analyzer":["references/lms-reporting-standard.md","assets/lms-analysis-template.md"],"transcript-auditor":["references/transcript-audit-standard.md","assets/transcript-exception-template.md"]}
class LmsFoundationsHardeningTests(unittest.TestCase):
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

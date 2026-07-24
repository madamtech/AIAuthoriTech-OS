import re, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
EXPECTED={
"workflow-engineering/approval-workflow-builder":["references/approval-workflow-standard.md","assets/approval-workflow-specification-template.md"],
"workflow-engineering/workflow-metrics-builder":["references/workflow-metrics-standard.md","assets/workflow-metric-dictionary-template.md"],
"workflow-engineering/workflow-documentation-builder":["references/workflow-documentation-standard.md","assets/workflow-documentation-template.md"],
"workflow-engineering/workflow-governance-reviewer":["references/workflow-governance-review-standard.md","assets/workflow-governance-review-template.md"],
"workflow-engineering/process-standardization-reviewer":["references/process-standardization-standard.md","assets/process-standardization-review-template.md"],
"government/public-sector-ai-readiness-assessor":["references/public-sector-readiness-standard.md","assets/public-sector-readiness-report-template.md"]}
class WorkflowGovernmentHardeningTests(unittest.TestCase):
 def test_controls(self):
  for rel in EXPECTED:
   text=(ROOT/"libraries/ai-authoritech/skills"/rel/"SKILL.md").read_text(encoding="utf-8")
   match=re.match(r"^---\s*\n(.*?)\n---",text,flags=re.DOTALL); self.assertIsNotNone(match)
   desc=next(x.split(":",1)[1].strip() for x in match.group(1).splitlines() if x.startswith("description:")); self.assertGreaterEqual(len(desc),180)
   for h in ("## Procedure","## Output Contract","## Guardrails","## Recovery"): self.assertIn(h,text)
   self.assertNotRegex(text,r"[^\x00-\x7F]"); self.assertNotIn("TODO",text)
 def test_resources(self):
  for rel,rs in EXPECTED.items():
   for r in rs:
    p=ROOT/"libraries/ai-authoritech/skills"/rel/r; self.assertTrue(p.is_file()); self.assertGreaterEqual(len(p.read_text(encoding="utf-8")),250)

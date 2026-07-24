import re, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; BASE=ROOT/'libraries/ai-authoritech/skills'
EXPECTED={'content-marketing/marketing-content-qa-reviewer': ['references/marketing-content-qa-standard.md', 'assets/marketing-content-qa-template.md'], 'cinematic-production/cinematic-story-builder': ['references/cinematic-story-standard.md', 'assets/cinematic-story-template.md'], 'cinematic-production/screenplay-builder': ['references/screenplay-standard.md', 'assets/screenplay-template.md'], 'cinematic-production/storyboard-director': ['references/storyboard-standard.md', 'assets/storyboard-template.md'], 'cinematic-production/character-continuity-manager': ['references/character-continuity-standard.md', 'assets/character-continuity-template.md'], 'cinematic-production/cinematic-shot-list-builder': ['references/shot-list-standard.md', 'assets/shot-list-template.md'], 'cinematic-production/image-prompt-director': ['references/image-prompt-standard.md', 'assets/image-prompt-template.md'], 'cinematic-production/video-prompt-director': ['references/video-prompt-standard.md', 'assets/video-prompt-template.md'], 'cinematic-production/camera-movement-designer': ['references/camera-movement-standard.md', 'assets/camera-movement-template.md'], 'cinematic-production/cinematic-lighting-designer': ['references/cinematic-lighting-standard.md', 'assets/cinematic-lighting-template.md'], 'cinematic-production/soundtrack-prompt-composer': ['references/soundtrack-prompt-standard.md', 'assets/soundtrack-prompt-template.md']}
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

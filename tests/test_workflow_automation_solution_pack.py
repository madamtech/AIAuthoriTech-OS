import json, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def load(p): return json.loads((ROOT/p).read_text(encoding="utf-8"))
class AutomationPackTests(unittest.TestCase):
 def test_stages(self):
  w=load("libraries/ai-authoritech/workflows/workflow-automation-delivery/workflow.json"); self.assertEqual([s["id"] for s in w["stages"]],["qualify","redesign","architect","controls","simulate","implement","operate"])
 def test_retry(self): self.assertEqual(load("libraries/ai-authoritech/workflows/workflow-automation-delivery/workflow.json")["failure_policy"]["retry_limit"],2)
 def test_dependencies(self):
  p=load("libraries/ai-authoritech/solution-packs/workflow-automation-accelerator/solution-pack.json"); e=["AA-WFL-000005"]+[f"AA-SKL-{n:06d}" for n in range(67,87)]; self.assertEqual(p["included_assets"],e); self.assertEqual(p["dependencies"],e)
 def test_claim_boundary(self):
  t=(ROOT/"libraries/ai-authoritech/solution-packs/workflow-automation-accelerator/examples/synthetic-client-intake.md").read_text(encoding="utf-8").lower(); self.assertIn("conditional pass",t); self.assertIn("production readiness remained blocked",t)
if __name__=="__main__": unittest.main()

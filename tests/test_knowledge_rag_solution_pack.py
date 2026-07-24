import json, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def load(p): return json.loads((ROOT/p).read_text(encoding="utf-8"))
class KnowledgeRagTests(unittest.TestCase):
 def test_workflow_order(self):
  w=load("libraries/ai-authoritech/workflows/knowledge-rag-delivery/workflow.json")
  self.assertEqual([s["id"] for s in w["stages"]],["intake","extract","model","retrieve","evaluate","govern","operate"])
  self.assertEqual(w["failure_policy"]["retry_limit"],2)
 def test_pack_access_and_refresh(self):
  k=load("libraries/ai-authoritech/knowledge-packs/knowledge-rag-foundation/knowledge-pack.json")
  self.assertIn("before retrieval",k["retrieval_guidance"])
  self.assertEqual(k["refresh_policy"]["stale_after_days"],90)
 def test_solution_dependencies(self):
  p=load("libraries/ai-authoritech/solution-packs/knowledge-rag-accelerator/solution-pack.json")
  expected=["AA-KNP-000001","AA-WFL-000004","AA-SKL-000013"]+[f"AA-SKL-{n:06d}" for n in range(57,67)]
  self.assertEqual(p["included_assets"],expected); self.assertEqual(p["dependencies"],expected)
 def test_claim_boundary(self):
  t=(ROOT/"libraries/ai-authoritech/solution-packs/knowledge-rag-accelerator/examples/synthetic-policy-assistant.md").read_text(encoding="utf-8").lower()
  self.assertIn("conditional pass",t); self.assertIn("production readiness remained blocked",t)
if __name__=="__main__": unittest.main()

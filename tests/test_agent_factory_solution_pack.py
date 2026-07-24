import json, unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
W=ROOT/"libraries/ai-authoritech/workflows/agent-factory-delivery/workflow.json"
A=ROOT/"libraries/ai-authoritech/agents/agent-factory-orchestrator/agent.json"
S=ROOT/"libraries/ai-authoritech/solution-packs/agent-factory/solution-pack.json"

class AgentFactoryTests(unittest.TestCase):
 def test_workflow_gates(self):
  w=json.loads(W.read_text(encoding="utf-8")); self.assertEqual([x["id"] for x in w["stages"]],["intake","architecture","instructions_knowledge","workflow_memory_tools","qa","deployment","operations","packaging"]); self.assertEqual(w["failure_policy"]["retry_limit"],2)
 def test_orchestrator_authority(self):
  a=json.loads(A.read_text(encoding="utf-8")); joined=" ".join(a["guardrails"]).lower(); self.assertIn("without explicit authorization",joined); self.assertEqual(a["memory_policy"]["default"],"no durable memory"); self.assertEqual(a["workflows"],["AA-WFL-000002"])
 def test_solution_vertical(self):
  s=json.loads(S.read_text(encoding="utf-8")); expected={"AA-AGT-000001","AA-WFL-000002",*(f"AA-SKL-{n:06d}" for n in range(11,22))}; self.assertEqual(set(s["included_assets"]),expected); self.assertEqual(set(s["dependencies"]),expected)
 def test_resources_and_controlled_gate(self):
  base=S.parent
  for name in ("agent-intake.md","agent-specification.md","evaluation-plan.md","deployment-gate.md"): self.assertGreater(len((base/"templates"/name).read_text(encoding="utf-8")),400)
  example=(base/"examples/synthetic-knowledge-assistant.md").read_text(encoding="utf-8").lower(); self.assertIn("conditional pass",example); self.assertIn("production readiness remains blocked",example)

if __name__=="__main__": unittest.main()

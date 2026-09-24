import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ReleaseReadinessTests(unittest.TestCase):
    def test_complete_evidence_coverage(self):
        assets = []
        for path in sorted((ROOT / "catalog").glob("*.json")):
            data = json.loads(path.read_text(encoding="utf-8"))
            if isinstance(data, dict) and isinstance(data.get("assets"), list):
                assets.extend(data["assets"])
        evaluated_skus = {
            json.loads(path.read_text(encoding="utf-8")).get("target_sku")
            for path in (ROOT / "evaluations").rglob("*.json")
        }
        maturity_skus = {
            json.loads(path.read_text(encoding="utf-8")).get("target_sku")
            for path in (ROOT / "catalog" / "maturity").glob("*.json")
        }
        missing_evidence = sorted(
            asset["sku"] for asset in assets if asset["asset_type"] == "SKL" and asset["sku"] not in evaluated_skus
        )
        self.assertEqual(missing_evidence, [], f"skills missing evaluation evidence: {missing_evidence}")
        missing_decisions = sorted(asset["sku"] for asset in assets if asset["sku"] not in maturity_skus)
        self.assertEqual(missing_decisions, [], f"assets missing maturity decisions: {missing_decisions}")

    def test_structural_audit_has_no_findings(self):
        audit = json.loads((ROOT / "reports" / "skill-catalog-audit.json").read_text(encoding="utf-8"))
        self.assertEqual(audit["findings"], [])
        self.assertEqual(audit["resource_counts"]["references"], audit["asset_count"])
        self.assertEqual(audit["resource_counts"]["assets"], audit["asset_count"])

    def test_every_overlap_candidate_has_a_review_decision(self):
        audit = json.loads((ROOT / "reports" / "skill-catalog-audit.json").read_text(encoding="utf-8"))
        review = (ROOT / "reports" / "overlap-review.md").read_text(encoding="utf-8")
        reviewed_pairs = {
            tuple(match)
            for match in re.findall(r"\| ([A-Z]+-SKL-\d+) / ([A-Z]+-SKL-\d+) \|", review)
        }
        candidates = {(item["left"], item["right"]) for item in audit["overlap_candidates"]}
        self.assertEqual(reviewed_pairs, candidates)


if __name__ == "__main__":
    unittest.main()

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ReleaseReadinessTests(unittest.TestCase):
    def test_complete_evidence_coverage(self):
        assets = json.loads((ROOT / "catalog" / "assets.json").read_text(encoding="utf-8"))["assets"]
        evaluations = list((ROOT / "evaluations").rglob("*.json"))
        maturity = list((ROOT / "catalog" / "maturity").glob("*.json"))
        self.assertEqual(len(assets), 236)
        self.assertEqual(len(evaluations), len(assets))
        self.assertEqual(len(maturity), len(assets))

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

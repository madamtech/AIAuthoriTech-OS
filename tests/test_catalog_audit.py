import unittest

from tools.audit_skill_catalog import relationship_document, similarity


class CatalogAuditTests(unittest.TestCase):
    def test_similarity_detects_close_scope(self):
        close = similarity("AI Governance Review", "AI Governance Reviewer")
        distant = similarity("AI Governance Review", "3D Print Project Planner")
        self.assertGreater(close, distant)
        self.assertGreater(close, 0.6)

    def test_relationships_include_inverse_edge(self):
        assets = [
            {"sku": "CO-SKL-000001", "depends_on": []},
            {"sku": "CO-SKL-000002", "depends_on": ["CO-SKL-000001"]},
        ]
        relationships = relationship_document(assets)["relationships"]
        self.assertIn({
            "source": "CO-SKL-000002",
            "relationship": "depends_on",
            "target": "CO-SKL-000001",
            "required": True,
        }, relationships)
        self.assertIn({
            "source": "CO-SKL-000001",
            "relationship": "consumed_by",
            "target": "CO-SKL-000002",
            "required": True,
        }, relationships)


if __name__ == "__main__":
    unittest.main()

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "libraries/core-os/skills/bookmarked-gpt-router/references/routing-catalog.json"
SOURCE = ROOT / "gpts/discovered/bookmarked-shared-gpts.json"


class BookmarkedGptRouterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = json.loads(CATALOG.read_text(encoding="utf-8"))["records"]
        cls.source = json.loads(SOURCE.read_text(encoding="utf-8"))["records"]

    def test_catalog_has_102_unique_authorized_routes(self):
        self.assertEqual(102, len(self.catalog))
        self.assertEqual(102, len({item["platform_gpt_id"] for item in self.catalog}))
        self.assertTrue(all(item["access_status"] == "authorized-for-use" for item in self.source))

    def test_every_route_has_matching_platform_id_and_https_url(self):
        for item in self.catalog:
            self.assertRegex(item["platform_gpt_id"], r"^g-[A-Za-z0-9_-]+$")
            self.assertTrue(
                item["url"].startswith(f"https://chatgpt.com/g/{item['platform_gpt_id']}"),
                item["name"],
            )

    def test_wmccraney_inventory_is_preserved(self):
        records = [item for item in self.catalog if "GPTs/WMcCraney" in item["folders"]]
        self.assertEqual(38, len(records))

    def test_external_routes_do_not_claim_captured_configuration(self):
        self.assertTrue(all(item["configuration_status"] == "not-captured" for item in self.source))
        self.assertTrue(all(item["migration_status"] == "authorized-adapter-ready" for item in self.source))


if __name__ == "__main__":
    unittest.main()

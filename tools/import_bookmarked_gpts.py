"""Import bookmarked GPT references without treating them as owned configurations."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit


GPT_ID = re.compile(r"/g/(g-(?:[0-9a-fA-F]{32}|[A-Za-z0-9]{9}))(?:-|/|$)")
TARGET_FOLDERS = {"gpts", "wmccraney", "w. mccraney"}


class BookmarkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.stack: list[str] = []
        self.pending_folder: str | None = None
        self.capture: list[str] | None = None
        self.attrs: dict[str, str] | None = None
        self.links: list[dict] = []
        self.dl_pushes: list[bool] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        if tag == "h3":
            self.capture = []
        elif tag == "a":
            self.capture = []
            self.attrs = {k: v or "" for k, v in attrs}
        elif tag == "dl":
            pushed = self.pending_folder is not None
            if pushed:
                self.stack.append(self.pending_folder or "")
                self.pending_folder = None
            self.dl_pushes.append(pushed)

    def handle_data(self, data: str) -> None:
        if self.capture is not None:
            self.capture.append(data)

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag == "h3" and self.capture is not None:
            self.pending_folder = "".join(self.capture).strip()
            self.capture = None
        elif tag == "a" and self.capture is not None:
            self.links.append(
                {
                    "title": " ".join("".join(self.capture).split()),
                    "url": (self.attrs or {}).get("href", ""),
                    "path": list(self.stack),
                }
            )
            self.capture = None
            self.attrs = None
        elif tag == "dl" and self.dl_pushes:
            if self.dl_pushes.pop() and self.stack:
                self.stack.pop()


def platform_id(url: str) -> str | None:
    match = GPT_ID.search(urlsplit(url).path)
    return match.group(1) if match else None


def relative_folder(path: list[str]) -> str:
    start = next((i for i, name in enumerate(path) if name.lower() == "gpts"), 0)
    return "/".join(path[start:])


def clean_title(title: str) -> str:
    return re.sub(r"^ChatGPT\s*-\s*", "", title, flags=re.I).strip() or "Untitled bookmarked GPT"


def canonical_url(items: list[dict]) -> str:
    ranked = sorted(
        items,
        key=lambda item: ("/c/" not in urlsplit(item["url"]).path, len(urlsplit(item["url"]).path)),
        reverse=True,
    )
    path = urlsplit(ranked[0]["url"]).path
    match = re.match(r"(/g/g-(?:[0-9a-fA-F]{32}|[A-Za-z0-9]{9})(?:-[^/]+)?)", path)
    return urlunsplit(("https", "chatgpt.com", match.group(1) if match else path.split("/c/")[0], "", ""))


def build_inventory(bookmarks: Path, registry: Path) -> tuple[dict, list[tuple[str, str, str]]]:
    parser = BookmarkParser()
    parser.feed(bookmarks.read_text(encoding="utf-8", errors="replace"))
    grouped: dict[str, list[dict]] = defaultdict(list)
    for item in parser.links:
        if not any(folder.lower() in TARGET_FOLDERS for folder in item["path"]):
            continue
        item_id = platform_id(item["url"])
        if item_id:
            grouped[item_id].append(item)

    gpt_registry = json.loads(registry.read_text(encoding="utf-8"))
    owned: dict[str, dict] = {}
    for item in gpt_registry["authoritative_gpts"]:
        item_id = platform_id(item.get("live_gpt_url") or "")
        if item_id:
            owned[item_id] = item

    records = []
    for item_id, items in grouped.items():
        if item_id in owned:
            continue
        titles = Counter(clean_title(item["title"]) for item in items)
        name = sorted(titles, key=lambda value: (-titles[value], len(value), value.lower()))[0]
        records.append(
            {
                "platform_gpt_id": item_id,
                "name": name,
                "live_gpt_url": canonical_url(items),
                "source_folders": sorted({relative_folder(item["path"]) for item in items}),
                "bookmark_count": len(items),
                "access_status": "bookmarked-access-unverified",
                "ownership_status": "shared-or-third-party-unverified",
                "configuration_status": "not-captured",
                "migration_status": "reference-only-pending-permission",
                "repository_owned_gpt_id": None,
                "source": {
                    "type": "chrome-bookmarks-export",
                    "file": bookmarks.name,
                    "export_date": "2026-08-09",
                },
                "notes": [
                    "Bookmark proves a saved reference, not current access or reuse permission.",
                    "Do not copy Builder instructions, knowledge files, or actions without confirmed authorization.",
                ],
            }
        )
    records.sort(key=lambda item: (item["source_folders"][0].lower(), item["name"].lower()))
    overlaps = sorted((owned[key]["gpt_id"], owned[key]["name"], key) for key in set(grouped) & set(owned))
    wmccraney = sum(any("/WMcCraney" in folder for folder in item["source_folders"]) for item in records)
    inventory = {
        "schema_version": "1.0.0",
        "generated_at": "2026-08-09",
        "purpose": "Inventory GPTs saved under the Chrome GPTs bookmark tree while separating shared references from owned authoritative GPTs.",
        "source_export": bookmarks.name,
        "scope": {
            "owned_authoritative_gpts": len(gpt_registry["authoritative_gpts"]),
            "unique_bookmarked_gpt_ids": len(grouped),
            "already_owned_overlap": len(overlaps),
            "new_shared_or_accessible_references": len(records),
            "wmccraney_new_references": wmccraney,
        },
        "governance": {
            "authoritative": False,
            "default_ownership": "shared-or-third-party-unverified",
            "default_configuration_status": "not-captured",
            "reuse_policy": "Reference-only until ownership or permission to reuse is established.",
        },
        "records": records,
    }
    return inventory, overlaps


def render_report(inventory: dict, overlaps: list[tuple[str, str, str]]) -> str:
    scope = inventory["scope"]
    folder_counts = Counter(folder for item in inventory["records"] for folder in item["source_folders"])
    lines = [
        "# Bookmarked GPT Inventory — 2026-08-09",
        "",
        "## Result",
        "",
        f'- Confirmed authoritative owned GPT manifests: **{scope["owned_authoritative_gpts"]}**',
        f'- Unique GPT IDs in the selected bookmark tree: **{scope["unique_bookmarked_gpt_ids"]}**',
        f'- Already represented as owned GPTs: **{scope["already_owned_overlap"]}**',
        f'- New shared/access references logged: **{scope["new_shared_or_accessible_references"]}**',
        f'- New references under `GPTs/WMcCraney`: **{scope["wmccraney_new_references"]}**',
        "",
        "Bookmarks establish a saved reference only. They do not prove current access, ownership, or permission to copy private configuration.",
        "",
        "## Folder counts",
        "",
        "| Bookmark folder | New unique references |",
        "|---|---:|",
    ]
    lines.extend(f"| `{folder}` | {count} |" for folder, count in sorted(folder_counts.items()))
    lines += ["", "## Existing owned overlaps (not duplicated)", "", "| Repository GPT ID | Name | Platform GPT ID |", "|---|---|---|"]
    lines.extend(f"| `{repo_id}` | {name.replace('|', chr(92) + '|')} | `{platform}` |" for repo_id, name, platform in overlaps)
    lines += ["", "## New shared/access references", "", "| Name | Folder(s) | Platform GPT ID | Link |", "|---|---|---|---|"]
    for item in inventory["records"]:
        name = item["name"].replace("|", "\\|")
        folders = "<br>".join(f'`{folder}`' for folder in item["source_folders"])
        lines.append(f'| {name} | {folders} | `{item["platform_gpt_id"]}` | [Open GPT]({item["live_gpt_url"]}) |')
    lines += [
        "",
        "## Required follow-up",
        "",
        "- Verify that each link still opens for the user.",
        "- Identify the creator/owner where visible.",
        "- Record explicit reuse permission before extracting private configuration.",
        "- Map references to existing skills only after purpose and permission are verified.",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("bookmarks", type=Path)
    parser.add_argument("--registry", type=Path, default=Path("registries/gpts.json"))
    parser.add_argument("--inventory", type=Path, default=Path("gpts/discovered/bookmarked-shared-gpts.json"))
    parser.add_argument("--report", type=Path, default=Path("reports/bookmarked-gpt-inventory-2026-08-09.md"))
    args = parser.parse_args()
    inventory, overlaps = build_inventory(args.bookmarks, args.registry)
    args.inventory.parent.mkdir(parents=True, exist_ok=True)
    args.inventory.write_text(json.dumps(inventory, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    args.report.write_text(render_report(inventory, overlaps), encoding="utf-8")
    print(json.dumps(inventory["scope"], indent=2))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Apply verified GPT-to-SKILL mappings to captured GPT manifests.

The mapping catalog is intentionally curated. This script never creates mappings itself; it only
applies records already marked verification_status=verified in catalog/gpt-skill-mappings.json.
"""

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAPPING_FILE = ROOT / "catalog" / "gpt-skill-mappings.json"
MANIFEST_ROOT = ROOT / "gpts" / "manifests"


def load_manifest_index():
    index = {}
    for path in MANIFEST_ROOT.glob("*/manifest.json"):
        data = json.loads(path.read_text(encoding="utf-8"))
        gpt_id = data.get("gpt_id")
        if gpt_id:
            index[gpt_id] = (path, data)
    return index


def apply(dry_run=False):
    mapping_doc = json.loads(MAPPING_FILE.read_text(encoding="utf-8"))
    manifests = load_manifest_index()
    changed = []
    skipped = []

    for mapping in mapping_doc.get("mappings", []):
        if mapping.get("verification_status") != "verified":
            skipped.append((mapping.get("gpt_id"), "not-verified"))
            continue
        gpt_id = mapping.get("gpt_id")
        if gpt_id not in manifests:
            raise SystemExit(f"Verified mapping references missing GPT manifest: {gpt_id}")
        path, manifest = manifests[gpt_id]
        desired = {
            "required": mapping.get("required_skills", []),
            "optional": mapping.get("optional_skills", []),
            "default_enhancements": mapping.get("default_enhancements", []),
        }
        if manifest.get("skills") == desired:
            skipped.append((gpt_id, "already-current"))
            continue
        manifest["skills"] = desired
        manifest.setdefault("change_log", []).append(
            f"{manifest.get('version', 'current')} - Applied verified GPT-to-SKILL mapping from catalog/gpt-skill-mappings.json."
        )
        if not dry_run:
            path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
        changed.append(gpt_id)

    print(json.dumps({"changed": changed, "skipped": skipped, "dry_run": dry_run}, indent=2))
    return 0


def main():
    parser = argparse.ArgumentParser(description="Apply verified GPT-to-SKILL mappings to manifests.")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    return apply(dry_run=args.dry_run)


if __name__ == "__main__":
    raise SystemExit(main())

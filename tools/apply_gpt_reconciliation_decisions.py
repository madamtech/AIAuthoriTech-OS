#!/usr/bin/env python3
"""Promote curated reconciliation decisions into the GPT mapping catalog and manifests.

Only decisions marked verified, partial-gap, or existing-verified can produce mappings.
Skill-gap records remain documented decisions and are never written into manifests.
"""
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DECISIONS = ROOT / "catalog" / "gpt-skill-reconciliation-decisions.json"
MAPPINGS = ROOT / "catalog" / "gpt-skill-mappings.json"
MANIFEST_ROOT = ROOT / "gpts" / "manifests"
VISUAL = "libraries/ai-authoritech/skills/image-generation/gpt-visual-intelligence-enhancement/SKILL.md"
PROMOTABLE = {"verified", "partial-gap", "existing-verified"}


def load_skill_skus():
    skus = set()
    for path in (ROOT / "catalog").glob("*.json"):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        for asset in data.get("assets", []) if isinstance(data, dict) else []:
            if asset.get("asset_type") == "SKL":
                skus.add(asset["sku"])
    return skus


def load_manifests():
    result = {}
    for path in MANIFEST_ROOT.glob("*/manifest.json"):
        data = json.loads(path.read_text(encoding="utf-8"))
        if re.match(r"^AA-GPT-\d{6}$", data.get("gpt_id", "")):
            result[data["gpt_id"]] = (path, data)
    return result


def validate(decisions, manifests, skills):
    errors = []
    seen = set()
    for row in decisions:
        gid = row.get("gpt_id")
        if gid in seen:
            errors.append(f"duplicate decision: {gid}")
        seen.add(gid)
        if gid not in manifests:
            errors.append(f"missing manifest: {gid}")
            continue
        if row.get("name") != manifests[gid][1].get("name"):
            errors.append(f"name mismatch: {gid}: {row.get('name')} != {manifests[gid][1].get('name')}")
        for sku in row.get("required_skills", []) + row.get("optional_skills", []):
            if sku not in skills:
                errors.append(f"missing skill: {gid} -> {sku}")
        if row.get("decision") == "skill-gap" and row.get("required_skills"):
            errors.append(f"skill-gap must not have required skills: {gid}")
    missing = sorted(set(manifests) - seen)
    extra = sorted(seen - set(manifests))
    if missing:
        errors.append(f"GPTs without decisions: {missing}")
    if extra:
        errors.append(f"decisions without GPTs: {extra}")
    if len(decisions) != len(manifests):
        errors.append(f"decision count {len(decisions)} != manifest count {len(manifests)}")
    return errors


def apply(write=False):
    decision_doc = json.loads(DECISIONS.read_text(encoding="utf-8"))
    decisions = decision_doc.get("decisions", [])
    manifests = load_manifests()
    skills = load_skill_skus()
    errors = validate(decisions, manifests, skills)
    if errors:
        raise SystemExit("RECONCILIATION VALIDATION FAILED\n- " + "\n- ".join(errors))

    old = json.loads(MAPPINGS.read_text(encoding="utf-8"))
    existing = {row["gpt_id"]: row for row in old.get("mappings", [])}
    promoted = []
    changed_manifests = []

    for row in decisions:
        if row.get("decision") not in PROMOTABLE:
            continue
        gid = row["gpt_id"]
        if not row.get("required_skills") and not row.get("optional_skills"):
            continue
        enhancements = [] if row.get("preserve_visual_enhancement") is False else [VISUAL]
        mapping = {
            "gpt_id": gid,
            "gpt_name": row["name"],
            "verification_status": "verified",
            "evidence": "Curated reconciliation against the captured Builder configuration; only directly supported reusable capabilities are mapped.",
            "required_skills": row.get("required_skills", []),
            "optional_skills": row.get("optional_skills", []),
            "default_enhancements": enhancements,
        }
        existing[gid] = mapping
        promoted.append(gid)

        path, manifest = manifests[gid]
        desired = {
            "required": mapping["required_skills"],
            "optional": mapping["optional_skills"],
            "default_enhancements": mapping["default_enhancements"],
        }
        if manifest.get("skills") != desired:
            manifest["skills"] = desired
            manifest.setdefault("change_log", []).append(
                f"{manifest.get('version', 'current')} - Applied curated GPT-to-SKILL reconciliation decision."
            )
            changed_manifests.append(gid)
            if write:
                path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    mapping_doc = {
        "schema_version": old.get("schema_version", "1.0.0"),
        "updated_at": decision_doc.get("updated_at"),
        "policy": old.get("policy", "Only record verified GPT-to-SKILL links."),
        "mappings": [existing[key] for key in sorted(existing)],
    }
    if write:
        MAPPINGS.write_text(json.dumps(mapping_doc, indent=2) + "\n", encoding="utf-8")

    counts = {}
    for row in decisions:
        counts[row["decision"]] = counts.get(row["decision"], 0) + 1
    result = {
        "validated_gpts": len(decisions),
        "decision_counts": dict(sorted(counts.items())),
        "promoted_mappings": len(promoted),
        "changed_manifests": len(changed_manifests),
        "skill_gaps": [row["gpt_id"] for row in decisions if row.get("decision") == "skill-gap"],
        "write": write,
    }
    print(json.dumps(result, indent=2))
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    apply(write=args.write)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Audit the alignment between captured Custom GPT manifests and governed SKILL.md assets.

This audit is intentionally conservative: it reports missing or unverified mappings but never
invents a GPT-to-skill dependency. Run with --write to refresh the committed reports or --check
to verify that committed reports match the repository state.
"""

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VISUAL_SKILL = "libraries/ai-authoritech/skills/image-generation/gpt-visual-intelligence-enhancement/SKILL.md"
SECURITY_SKILL = "libraries/core-os/skills/gpt-security-hardening/SKILL.md"


def load_manifests(root=ROOT):
    records = []
    manifest_root = root / "gpts" / "manifests"
    for path in sorted(manifest_root.glob("*/manifest.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        if str(data.get("gpt_id", "")).startswith("AA-GPT-"):
            records.append((path, data))
    return records


def known_skill_references(root=ROOT):
    refs = set()
    for catalog_path in sorted((root / "catalog").glob("*.json")):
        data = json.loads(catalog_path.read_text(encoding="utf-8"))
        for asset in data.get("assets", []) if isinstance(data, dict) else []:
            if asset.get("asset_type") == "SKL":
                refs.add(asset.get("sku"))
                skill_path = asset.get("path")
                if skill_path:
                    refs.add(skill_path)
                    refs.add(f"{skill_path}/SKILL.md")
    for skill_file in root.glob("libraries/**/SKILL.md"):
        refs.add(skill_file.relative_to(root).as_posix())
    return refs


def audit(root=ROOT):
    manifests = load_manifests(root)
    known_skills = known_skill_references(root)
    registry = json.loads((root / "registries" / "gpts.json").read_text(encoding="utf-8"))

    findings = []
    rows = []
    seen_ids = set()
    seen_urls = set()

    for path, manifest in manifests:
        gpt_id = manifest.get("gpt_id")
        name = manifest.get("name")
        skills = manifest.get("skills", {})
        required = skills.get("required", [])
        optional = skills.get("optional", [])
        enhancements = skills.get("default_enhancements", [])
        evaluation = manifest.get("evaluation", {})
        capabilities = manifest.get("configuration", {}).get("capabilities", [])
        live_url = manifest.get("runtime", {}).get("live_gpt_url")
        image_capable = "Image Generation" in capabilities
        security_hardened = SECURITY_SKILL in enhancements

        if gpt_id in seen_ids:
            findings.append({"severity": "critical", "gpt_id": gpt_id, "code": "duplicate-gpt-id"})
        seen_ids.add(gpt_id)
        if live_url:
            if live_url in seen_urls:
                findings.append({"severity": "high", "gpt_id": gpt_id, "code": "duplicate-live-url"})
            seen_urls.add(live_url)

        all_links = required + optional + enhancements
        unresolved = [ref for ref in all_links if ref not in known_skills and not (root / ref).exists()]
        if unresolved:
            findings.append({
                "severity": "critical",
                "gpt_id": gpt_id,
                "code": "unresolved-skill-reference",
                "references": unresolved,
            })

        if not security_hardened:
            findings.append({
                "severity": "critical",
                "gpt_id": gpt_id,
                "code": "missing-security-hardening-enhancement",
                "required_reference": SECURITY_SKILL,
            })

        if image_capable and VISUAL_SKILL not in enhancements:
            findings.append({"severity": "high", "gpt_id": gpt_id, "code": "missing-visual-enhancement"})

        if not required and not optional:
            findings.append({"severity": "medium", "gpt_id": gpt_id, "code": "no-explicit-domain-skill-mapping"})

        if evaluation.get("profile") is None:
            findings.append({"severity": "medium", "gpt_id": gpt_id, "code": "missing-evaluation-profile"})
        if evaluation.get("last_result") == "not-tested":
            findings.append({"severity": "medium", "gpt_id": gpt_id, "code": "behavioral-evaluation-not-run"})

        business = str(manifest.get("business", ""))
        if "needs review" in business.lower():
            findings.append({"severity": "low", "gpt_id": gpt_id, "code": "business-mapping-needs-review"})

        rows.append({
            "gpt_id": gpt_id,
            "name": name,
            "status": manifest.get("status"),
            "image_capable": image_capable,
            "security_hardened": security_hardened,
            "required_skills": len(required),
            "optional_skills": len(optional),
            "default_enhancements": len(enhancements),
            "evaluation_profile": evaluation.get("profile"),
            "last_result": evaluation.get("last_result"),
            "manifest": path.relative_to(root).as_posix(),
        })

    expected = registry.get("inventory_status", {}).get("total_count")
    if expected != len(manifests):
        findings.append({
            "severity": "critical",
            "gpt_id": None,
            "code": "registry-manifest-count-mismatch",
            "registry_count": expected,
            "manifest_count": len(manifests),
        })

    counts = Counter(f["code"] for f in findings)
    severity_counts = Counter(f["severity"] for f in findings)
    image_count = sum(row["image_capable"] for row in rows)
    visual_count = sum(row["default_enhancements"] > 0 for row in rows)
    security_count = sum(row["security_hardened"] for row in rows)
    mapped_count = sum((row["required_skills"] + row["optional_skills"]) > 0 for row in rows)

    return {
        "schema_version": "1.1.0",
        "audit_date": "2026-08-13",
        "gpt_count": len(rows),
        "image_capable_count": image_count,
        "visual_enhancement_count": visual_count,
        "security_hardened_count": security_count,
        "explicit_domain_skill_mapping_count": mapped_count,
        "finding_counts": dict(sorted(counts.items())),
        "severity_counts": dict(sorted(severity_counts.items())),
        "findings": findings,
        "gpts": rows,
    }


def markdown(audit):
    lines = [
        "# GPT-to-Skill Alignment Audit — 2026-08-13",
        "",
        "## Summary",
        "",
        f"- Captured GPT manifests: **{audit['gpt_count']}**",
        f"- GPTs with mandatory security hardening: **{audit['security_hardened_count']}**",
        f"- Image-capable GPTs: **{audit['image_capable_count']}**",
        f"- GPTs with one or more default enhancements: **{audit['visual_enhancement_count']}**",
        f"- GPTs with explicit required/optional domain-skill links: **{audit['explicit_domain_skill_mapping_count']}**",
        "",
        "## Finding Counts",
        "",
    ]
    if audit["finding_counts"]:
        for code, count in audit["finding_counts"].items():
            lines.append(f"- {code}: **{count}**")
    else:
        lines.append("- None")

    lines.extend([
        "",
        "## Interpretation",
        "",
        "Every governed GPT must include the global GPT Security Hardening skill in `skills.default_enhancements`. Missing security hardening is a critical finding and blocks validation or deployment until remediated or an explicit governed exception is documented.",
        "",
        "The GPT capture layer and the governed skill catalog are separate layers until each manifest explicitly references the reusable domain skills it consumes. A captured GPT is not automatically considered skill-mapped merely because an equivalent skill exists elsewhere in the repository.",
        "",
        "This audit never guesses domain mappings. Missing links are reported for reconciliation against existing SKILL.md assets, the original GPT instructions, and the catalog relationship graph.",
        "",
        "## Required Remediation Order",
        "",
        "1. Add the mandatory GPT Security Hardening enhancement to every GPT manifest that lacks it.",
        "2. Resolve other critical structural or broken-reference findings.",
        "3. Map each GPT to existing reusable domain skills without duplicating its full instructions into new skills.",
        "4. Assign the appropriate evaluation profile and run behavioral regression tests.",
        "5. Review unresolved business ownership labels.",
        "6. Promote GPT status from captured to validated only after the security, mapping, and evaluation evidence is complete.",
        "",
    ])
    return "\n".join(lines)


def render(root=ROOT):
    data = audit(root)
    return {
        root / "reports" / "gpt-skill-alignment-audit.json": json.dumps(data, indent=2) + "\n",
        root / "reports" / "gpt-skill-alignment-audit.md": markdown(data),
    }


def main():
    parser = argparse.ArgumentParser(description="Audit Custom GPT manifests against reusable skills.")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args()
    outputs = render()
    if args.write:
        for path, content in outputs.items():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
        print(f"GPT/SKILL AUDIT WRITTEN: {len(outputs)} artifacts")
        return 0
    stale = []
    for path, expected in outputs.items():
        if not path.is_file() or path.read_text(encoding="utf-8") != expected:
            stale.append(path.relative_to(ROOT).as_posix())
    if stale:
        print("GPT/SKILL AUDIT CHECK FAILED")
        for path in stale:
            print(f"- stale or missing: {path}")
        return 1
    print(f"GPT/SKILL AUDIT CHECK PASSED: {len(outputs)} artifacts")
    return 0


if __name__ == "__main__":
    sys.exit(main())

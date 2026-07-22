#!/usr/bin/env python3
import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STOP_WORDS = {
    "a", "an", "and", "for", "of", "the", "to", "with", "builder", "designer",
    "planner", "manager", "reviewer", "assistant", "specialist", "analyzer",
}


def load_catalog(root=ROOT):
    return json.loads((root / "catalog" / "assets.json").read_text(encoding="utf-8"))["assets"]


def frontmatter(path):
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---", text, flags=re.DOTALL)
    if not match:
        return {}
    values = {}
    for line in match.group(1).splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            values[key.strip()] = value.strip().strip('"')
    return values


def tokens(value):
    return {
        token for token in re.findall(r"[a-z0-9]+", value.lower())
        if token not in STOP_WORDS and len(token) > 1
    }


def similarity(left, right):
    a, b = tokens(left), tokens(right)
    if not a or not b:
        return 0.0
    jaccard = len(a & b) / len(a | b)
    containment = len(a & b) / min(len(a), len(b))
    return round((jaccard * 0.6) + (containment * 0.4), 4)


def relationship_document(assets):
    relationships = []
    for asset in assets:
        for dependency in asset.get("depends_on", []):
            relationships.append({
                "source": asset["sku"],
                "relationship": "depends_on",
                "target": dependency,
                "required": True,
            })
            relationships.append({
                "source": dependency,
                "relationship": "consumed_by",
                "target": asset["sku"],
                "required": True,
            })
    relationships.sort(key=lambda edge: (edge["source"], edge["relationship"], edge["target"]))
    return {"schema_version": "1.0.0", "relationships": relationships}


def audit_document(assets, root=ROOT):
    findings = []
    records = []
    for asset in assets:
        folder = root / asset["path"]
        skill_file = folder / "SKILL.md"
        meta = frontmatter(skill_file) if skill_file.is_file() else {}
        record = {
            "sku": asset["sku"],
            "name": asset["name"],
            "business": asset["business"],
            "library": asset["library"],
            "path": asset["path"],
            "frontmatter_name": meta.get("name"),
            "description": meta.get("description", ""),
            "has_agent_metadata": (folder / "agents" / "openai.yaml").is_file(),
            "has_references": (folder / "references").is_dir(),
            "has_assets": (folder / "assets").is_dir(),
            "has_scripts": (folder / "scripts").is_dir(),
            "dependency_count": len(asset.get("depends_on", [])),
        }
        records.append(record)
        if not record["description"]:
            findings.append({"severity": "critical", "sku": asset["sku"], "code": "missing-description"})
        elif len(record["description"]) < 60:
            findings.append({"severity": "medium", "sku": asset["sku"], "code": "thin-trigger-description"})
        if not record["has_agent_metadata"]:
            findings.append({"severity": "high", "sku": asset["sku"], "code": "missing-agent-metadata"})
        if not record["has_references"] and not record["has_assets"] and not record["has_scripts"]:
            findings.append({"severity": "low", "sku": asset["sku"], "code": "no-bundled-resources"})

    overlap_candidates = []
    for index, left in enumerate(records):
        for right in records[index + 1:]:
            name_score = similarity(left["name"], right["name"])
            description_score = similarity(left["description"], right["description"])
            combined = round((name_score * 0.7) + (description_score * 0.3), 4)
            same_library = left["library"] == right["library"]
            if combined >= 0.61 or (same_library and combined >= 0.54):
                overlap_candidates.append({
                    "left": left["sku"],
                    "right": right["sku"],
                    "score": combined,
                    "same_library": same_library,
                    "disposition": "review",
                })
    overlap_candidates.sort(key=lambda item: (-item["score"], item["left"], item["right"]))

    resource_counts = {
        "agent_metadata": sum(record["has_agent_metadata"] for record in records),
        "references": sum(record["has_references"] for record in records),
        "assets": sum(record["has_assets"] for record in records),
        "scripts": sum(record["has_scripts"] for record in records),
    }
    return {
        "schema_version": "1.0.0",
        "asset_count": len(records),
        "business_counts": dict(sorted(Counter(record["business"] for record in records).items())),
        "library_counts": dict(sorted(Counter(record["library"] for record in records).items())),
        "resource_counts": resource_counts,
        "finding_counts": dict(sorted(Counter(finding["code"] for finding in findings).items())),
        "findings": findings,
        "overlap_candidates": overlap_candidates,
    }


def audit_markdown(audit):
    lines = [
        "# Skill Catalog Audit",
        "",
        f"Cataloged skills: {audit['asset_count']}",
        "",
        "## Resource Coverage",
        "",
        "| Resource | Skills | Coverage |",
        "|---|---:|---:|",
    ]
    for label, count in audit["resource_counts"].items():
        percent = (count / audit["asset_count"] * 100) if audit["asset_count"] else 0
        lines.append(f"| {label.replace('_', ' ').title()} | {count} | {percent:.1f}% |")
    lines.extend(["", "## Finding Counts", ""])
    for code, count in audit["finding_counts"].items():
        lines.append(f"- {code}: {count}")
    lines.extend(["", "## Highest-Scoring Scope Overlaps", "", "| Left | Right | Score | Same library |", "|---|---|---:|:---:|"])
    for item in audit["overlap_candidates"][:50]:
        lines.append(f"| {item['left']} | {item['right']} | {item['score']:.4f} | {'Yes' if item['same_library'] else 'No'} |")
    lines.extend([
        "",
        "Scores identify review candidates, not automatic duplicates. A human decision must mark each pair as merge, narrow, cross-route, or retain.",
        "",
    ])
    return "\n".join(lines)


def render_outputs(root=ROOT):
    assets = load_catalog(root)
    relationships = json.dumps(relationship_document(assets), indent=2) + "\n"
    audit = audit_document(assets, root)
    audit_json = json.dumps(audit, indent=2) + "\n"
    audit_md = audit_markdown(audit)
    return {
        root / "catalog" / "relationships.json": relationships,
        root / "reports" / "skill-catalog-audit.json": audit_json,
        root / "reports" / "skill-catalog-audit.md": audit_md,
    }


def main():
    parser = argparse.ArgumentParser(description="Generate or verify the AI AuthoriTech skill catalog audit.")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true", help="Write generated audit artifacts.")
    mode.add_argument("--check", action="store_true", help="Verify committed audit artifacts are current.")
    args = parser.parse_args()
    outputs = render_outputs()
    if args.write:
        for path, content in outputs.items():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
        print(f"AUDIT WRITTEN: {len(outputs)} artifacts")
        return 0
    stale = []
    for path, expected in outputs.items():
        if not path.is_file() or path.read_text(encoding="utf-8") != expected:
            stale.append(path.relative_to(ROOT).as_posix())
    if stale:
        print("AUDIT CHECK FAILED")
        for path in stale:
            print(f"- stale or missing: {path}")
        return 1
    print(f"AUDIT CHECK PASSED: {len(outputs)} artifacts")
    return 0


if __name__ == "__main__":
    sys.exit(main())

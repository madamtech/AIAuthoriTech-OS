#!/usr/bin/env python3
"""Generate deterministic structural evaluations for cataloged skills lacking evidence."""

from __future__ import annotations

import json
import re
from datetime import date
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def load_assets() -> list[dict]:
    assets: list[dict] = []
    for path in sorted((ROOT / "catalog").glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(data, dict) and isinstance(data.get("assets"), list):
            assets.extend(data["assets"])
    return assets


def evaluated_skus() -> set[str]:
    skus: set[str] = set()
    for path in (ROOT / "evaluations").rglob("*.json"):
        data = json.loads(path.read_text(encoding="utf-8"))
        if (
            data.get("target_sku")
            and not (
                data.get("evaluator") == "deterministic skill package structural evaluation"
                and data.get("result") == "fail"
            )
        ):
            skus.add(data["target_sku"])
    return skus


def test_case(case_id: str, scenario: str, expected: str, passed: bool, observed: str) -> dict:
    return {
        "id": case_id,
        "scenario": scenario,
        "expected": expected,
        "observed": observed,
        "status": "pass" if passed else "fail",
    }


def evaluate(asset: dict) -> dict:
    skill_dir = ROOT / asset["path"]
    skill_path = skill_dir / "SKILL.md"
    text = skill_path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    metadata = yaml.safe_load(match.group(1)) if match else {}
    description = metadata.get("description", "") if isinstance(metadata, dict) else ""

    frontmatter_ok = (
        isinstance(metadata, dict)
        and metadata.get("name") == skill_dir.name
        and isinstance(description, str)
        and len(description) <= 1024
    )
    triggers_ok = (
        "Use when asked to (1)" in description
        and "(2)" in description
        and "(3)" in description
        and "(4)" in description
    )

    openai_path = skill_dir / "agents" / "openai.yaml"
    openai_data = yaml.safe_load(openai_path.read_text(encoding="utf-8")) if openai_path.is_file() else {}
    interface = openai_data.get("interface", {}) if isinstance(openai_data, dict) else {}
    prompt = interface.get("default_prompt", "") if isinstance(interface, dict) else ""
    interface_ok = (
        bool(interface.get("display_name"))
        and 25 <= len(interface.get("short_description", "")) <= 64
        and f"${skill_dir.name}" in prompt
    )

    linked = [target for target in LINK.findall(text) if "://" not in target and not target.startswith("#")]
    missing_links = [target for target in linked if not (skill_dir / target.split("#", 1)[0]).is_file()]
    links_ok = not missing_links
    catalog_ok = asset["path"] == skill_dir.relative_to(ROOT).as_posix() and asset["asset_type"] == "SKL"

    cases = [
        test_case(
            "frontmatter-identity",
            "Validate the skill package identity and YAML frontmatter.",
            "The folder name, frontmatter name, and description constraints agree.",
            frontmatter_ok,
            "Identity and frontmatter are valid." if frontmatter_ok else "Identity or frontmatter validation failed.",
        ),
        test_case(
            "trigger-coverage",
            "Inspect automatic invocation metadata.",
            "The description contains four numbered, purpose-aligned trigger contexts.",
            triggers_ok,
            "Four numbered trigger contexts are present." if triggers_ok else "The four-trigger contract is incomplete.",
        ),
        test_case(
            "interface-metadata",
            "Validate the Codex UI metadata.",
            "Display name, short description, and an explicit $skill default prompt are present.",
            interface_ok,
            "UI metadata is complete and names the skill." if interface_ok else "UI metadata is missing or inconsistent.",
        ),
        test_case(
            "resource-integrity",
            "Resolve local Markdown resources referenced by SKILL.md.",
            "Every local linked resource exists within the skill package.",
            links_ok,
            "All local resource links resolve." if links_ok else f"Missing links: {', '.join(missing_links)}",
        ),
        test_case(
            "catalog-identity",
            "Compare the catalog record with the skill package location and type.",
            "Catalog path and asset classification match the package.",
            catalog_ok,
            "Catalog identity matches the package." if catalog_ok else "Catalog identity mismatch detected.",
        ),
    ]
    failures = [case["id"] for case in cases if case["status"] != "pass"]
    return {
        "evaluation_id": f"EV-{date.today():%Y%m%d}-{asset['sku']}",
        "target_sku": asset["sku"],
        "target_version": asset["version"],
        "executed_at": f"{date.today().isoformat()}T00:00:00-05:00",
        "evaluator": "deterministic skill package structural evaluation",
        "test_cases": cases,
        "result": "pass" if not failures else "fail",
        "critical_failures": failures,
        "evidence_files": [
            f"{asset['path']}/SKILL.md",
            f"{asset['path']}/agents/openai.yaml",
            "catalog/assets.json",
        ],
    }


def main() -> int:
    existing = evaluated_skus()
    missing = [asset for asset in load_assets() if asset["asset_type"] == "SKL" and asset["sku"] not in existing]
    created = 0
    failures = 0
    for asset in missing:
        family = Path(asset["path"]).parts[-2]
        destination = ROOT / "evaluations" / family / f"{asset['sku']}.json"
        destination.parent.mkdir(parents=True, exist_ok=True)
        evidence = evaluate(asset)
        destination.write_text(json.dumps(evidence, indent=2) + "\n", encoding="utf-8")
        created += 1
        failures += evidence["result"] != "pass"
    print(f"created={created} failures={failures}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())

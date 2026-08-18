#!/usr/bin/env python3
"""Create missing agents/openai.yaml files for cataloged skills."""

from __future__ import annotations

import json
import re
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]


def assets() -> list[dict]:
    result: list[dict] = []
    for path in sorted((ROOT / "catalog").glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(data, dict) and isinstance(data.get("assets"), list):
            result.extend(data["assets"])
    return result


def description(skill_path: Path) -> str:
    text = skill_path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    metadata = yaml.safe_load(match.group(1))
    return metadata["description"].split(". ", 1)[0].rstrip(".")


def short_description(value: str) -> str:
    value = value.strip()
    if len(value) > 64:
        value = value[:61].rsplit(" ", 1)[0] + "..."
    if len(value) < 25:
        value = f"Use this skill to {value.lower()}"
    return value[:64]


def main() -> int:
    created = 0
    for asset in assets():
        if asset["asset_type"] != "SKL":
            continue
        skill_dir = ROOT / asset["path"]
        destination = skill_dir / "agents" / "openai.yaml"
        if destination.is_file():
            continue
        purpose = description(skill_dir / "SKILL.md")
        interface = {
            "interface": {
                "display_name": asset["name"],
                "short_description": short_description(purpose),
                "default_prompt": f"Use ${skill_dir.name} to {purpose[0].lower() + purpose[1:]}.",
            }
        }
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(yaml.safe_dump(interface, sort_keys=False, allow_unicode=True), encoding="utf-8")
        created += 1
    print(f"created={created}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

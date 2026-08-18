#!/usr/bin/env python3
"""Create conservative maturity decisions for registered assets lacking a decision record."""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_assets() -> list[dict]:
    assets: list[dict] = []
    for path in sorted((ROOT / "catalog").glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(data, dict) and isinstance(data.get("assets"), list):
            assets.extend(data["assets"])
    return assets


def evaluation_ids() -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    for path in (ROOT / "evaluations").rglob("*.json"):
        data = json.loads(path.read_text(encoding="utf-8"))
        if data.get("target_sku") and data.get("evaluation_id"):
            result.setdefault(data["target_sku"], []).append(data["evaluation_id"])
    return result


def main() -> int:
    evidence = evaluation_ids()
    created = 0
    for asset in load_assets():
        destination = ROOT / "catalog" / "maturity" / f"{asset['sku']}.json"
        if destination.is_file():
            continue
        ids = sorted(evidence.get(asset["sku"], []))
        if not ids:
            raise RuntimeError(f"Cannot create maturity decision without evidence for {asset['sku']}")
        decision = {
            "target_sku": asset["sku"],
            "target_version": asset["version"],
            "from_level": asset["maturity"],
            "to_level": asset["maturity"] + 1,
            "requested_at": f"{date.today().isoformat()}T00:00:00-05:00",
            "evidence": ids,
            "quality_gate": {
                "structural_validation": True,
                "behavioral_validation": False,
                "critical_failures": 0,
            },
            "approvals": [],
            "decision": "changes-required",
        }
        destination.write_text(json.dumps(decision, indent=2) + "\n", encoding="utf-8")
        created += 1
    print(f"created={created}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKU = re.compile(r"^(AA|LMS|MA|CO)-([A-Z]{3})-[0-9]{6}$")
AID = re.compile(r"^[a-z0-9-]+\.[a-z0-9-]+\.v[1-9][0-9]*$")
SEMVER = re.compile(r"^[0-9]+\.[0-9]+\.[0-9]+$")

def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))

def main():
    errors = []
    businesses = {x["code"] for x in load("registries/businesses.json")["businesses"]}
    libraries = {x["code"] for x in load("registries/libraries.json")["libraries"]}
    types = {x["code"] for x in load("registries/asset-types.json")["asset_types"]}
    assets = load("catalog/assets.json")["assets"]
    skus = [x["sku"] for x in assets]
    ids = [x["asset_id"] for x in assets]
    if len(skus) != len(set(skus)): errors.append("duplicate SKU")
    if len(ids) != len(set(ids)): errors.append("duplicate asset_id")
    known = set(skus)
    for item in assets:
        match = SKU.fullmatch(item["sku"])
        if not match: errors.append(f"{item['sku']}: invalid SKU"); continue
        if match.group(1) != item["business"]: errors.append(f"{item['sku']}: business mismatch")
        if match.group(2) != item["asset_type"]: errors.append(f"{item['sku']}: type mismatch")
        if item["business"] not in businesses: errors.append(f"{item['sku']}: unknown business")
        if item["library"] not in libraries: errors.append(f"{item['sku']}: unknown library")
        if item["asset_type"] not in types: errors.append(f"{item['sku']}: unknown type")
        if not AID.fullmatch(item["asset_id"]): errors.append(f"{item['sku']}: invalid asset_id")
        if not SEMVER.fullmatch(item["version"]): errors.append(f"{item['sku']}: invalid version")
        path = ROOT / item["path"]
        if not path.is_dir(): errors.append(f"{item['sku']}: missing path")
        if item["asset_type"] == "SKL" and not (path / "SKILL.md").is_file():
            errors.append(f"{item['sku']}: missing SKILL.md")
        for target in item["depends_on"]:
            if target not in known: errors.append(f"{item['sku']}: unknown dependency {target}")
    if errors:
        print("VALIDATION FAILED")
        for error in errors: print(f"- {error}")
        return 1
    print(f"VALIDATION PASSED: {len(assets)} cataloged assets")
    return 0

if __name__ == "__main__": sys.exit(main())

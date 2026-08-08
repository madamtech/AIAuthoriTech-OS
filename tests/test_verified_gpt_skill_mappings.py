import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def catalog_assets():
    assets = {}
    for path in (ROOT / "catalog").glob("*.json"):
        data = json.loads(path.read_text(encoding="utf-8"))
        for asset in data.get("assets", []) if isinstance(data, dict) else []:
            assets[asset["sku"]] = asset
    return assets


def manifest_ids():
    ids = set()
    for path in (ROOT / "gpts" / "manifests").glob("*/manifest.json"):
        data = json.loads(path.read_text(encoding="utf-8"))
        if data.get("gpt_id"):
            ids.add(data["gpt_id"])
    return ids


def test_verified_mapping_targets_exist():
    mapping_doc = json.loads((ROOT / "catalog" / "gpt-skill-mappings.json").read_text(encoding="utf-8"))
    gpts = manifest_ids()
    skills = catalog_assets()
    problems = []
    for mapping in mapping_doc["mappings"]:
        if mapping["verification_status"] != "verified":
            continue
        if mapping["gpt_id"] not in gpts:
            problems.append(f"missing GPT {mapping['gpt_id']}")
        for sku in mapping["required_skills"] + mapping["optional_skills"]:
            if sku not in skills or skills[sku].get("asset_type") != "SKL":
                problems.append(f"missing skill {sku} for {mapping['gpt_id']}")
        for ref in mapping["default_enhancements"]:
            if not (ROOT / ref).is_file():
                problems.append(f"missing enhancement {ref} for {mapping['gpt_id']}")
    assert not problems, problems


def test_verified_mapping_gpt_ids_are_unique():
    mapping_doc = json.loads((ROOT / "catalog" / "gpt-skill-mappings.json").read_text(encoding="utf-8"))
    ids = [item["gpt_id"] for item in mapping_doc["mappings"]]
    assert len(ids) == len(set(ids))

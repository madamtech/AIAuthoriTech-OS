import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VISUAL_SKILL = "libraries/ai-authoritech/skills/image-generation/gpt-visual-intelligence-enhancement/SKILL.md"


def manifests():
    result = []
    for path in sorted((ROOT / "gpts" / "manifests").glob("*/manifest.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        if str(data.get("gpt_id", "")).startswith("AA-GPT-"):
            result.append((path, data))
    return result


def test_registry_and_manifest_inventory_match():
    registry = json.loads((ROOT / "registries" / "gpts.json").read_text(encoding="utf-8"))
    items = manifests()
    assert len(items) == registry["inventory_status"]["total_count"]
    assert len({m["gpt_id"] for _, m in items}) == len(items)


def test_image_capable_gpts_receive_visual_intelligence_enhancement():
    missing = []
    for path, manifest in manifests():
        capabilities = manifest["configuration"]["capabilities"]
        if "Image Generation" not in capabilities:
            continue
        if VISUAL_SKILL not in manifest["skills"]["default_enhancements"]:
            missing.append(path.relative_to(ROOT).as_posix())
    assert not missing, f"Image-capable GPTs missing visual enhancement: {missing}"


def test_all_declared_skill_file_paths_resolve():
    broken = []
    for path, manifest in manifests():
        skills = manifest["skills"]
        for ref in skills["required"] + skills["optional"] + skills["default_enhancements"]:
            if ref.endswith(".md") and not (ROOT / ref).is_file():
                broken.append((path.relative_to(ROOT).as_posix(), ref))
    assert not broken, f"Broken GPT skill references: {broken}"


def test_custom_gpt_is_registered_as_asset_type():
    registry = json.loads((ROOT / "registries" / "asset-types.json").read_text(encoding="utf-8"))
    assert any(item["code"] == "GPT" and item["name"] == "Custom GPT" for item in registry["asset_types"])

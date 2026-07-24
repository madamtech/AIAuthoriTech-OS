#!/usr/bin/env python3
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKU = re.compile(r"^(AA|LMS|MA|CO)-([A-Z]{3})-[0-9]{6}$")
AID = re.compile(r"^[a-z0-9-]+\.[a-z0-9-]+\.v[1-9][0-9]*$")
SEMVER = re.compile(r"^[0-9]+\.[0-9]+\.[0-9]+$")
FIRST_CLASS_MANIFESTS = {
    "WFL": ("workflow.json", "workflow.schema.json", {"trigger", "stages", "state", "completion_criteria", "failure_policy"}),
    "AGT": ("agent.json", "agent.schema.json", {"mission", "instructions", "capabilities", "tools", "workflows", "memory_policy", "guardrails", "evaluation_suite"}),
    "APP": ("app.json", "app.schema.json", {"product_outcome", "users", "interfaces", "runtime", "data_classification", "capabilities", "deployment", "test_plan"}),
    "TMP": ("template.json", "template.schema.json", {"format", "source_file", "variables", "usage_rules", "produces"}),
    "KNP": ("knowledge-pack.json", "knowledge-pack.schema.json", {"topics", "sources", "retrieval_guidance", "refresh_policy", "quality_owner"}),
    "PLY": ("playbook.json", "playbook.schema.json", {"business_problem", "audience", "entry_criteria", "phases", "included_assets", "exit_criteria"}),
    "SOL": ("solution-pack.json", "solution-pack.schema.json", {"business_outcome", "target_customers", "included_assets", "implementation_model", "success_measures", "support_model"}),
}
COMMON_MANIFEST_FIELDS = {
    "sku", "asset_id", "name", "asset_type", "business", "library", "version",
    "status", "maturity", "description", "owners", "inputs", "outputs", "dependencies",
}
REQUIRED_SCHEMAS = {
    "asset.schema.json", "asset-manifest.schema.json", "workflow.schema.json",
    "agent.schema.json", "app.schema.json", "template.schema.json",
    "knowledge-pack.schema.json", "playbook.schema.json", "solution-pack.schema.json",
    "evaluation-evidence.schema.json", "asset-relationship.schema.json",
    "maturity-promotion.schema.json",
}

def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))

def load_assets():
    assets = []
    for path in sorted((ROOT / "catalog").glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(data, dict) and isinstance(data.get("assets"), list):
            assets.extend(data["assets"])
    return assets

def read_json(path, errors, label):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"{label}: invalid JSON ({exc})")
        return None

def validate_manifest(item, path, errors):
    manifest_name, schema_name, specialized = FIRST_CLASS_MANIFESTS[item["asset_type"]]
    manifest_path = path / manifest_name
    if not manifest_path.is_file():
        errors.append(f"{item['sku']}: missing {manifest_name}")
        return
    manifest = read_json(manifest_path, errors, item["sku"])
    if manifest is None:
        return
    missing = sorted((COMMON_MANIFEST_FIELDS | specialized) - set(manifest))
    if missing:
        errors.append(f"{item['sku']}: manifest missing {', '.join(missing)}")
    for field in ("sku", "asset_id", "name", "asset_type", "business", "library", "version", "status", "maturity"):
        if manifest.get(field) != item.get(field):
            errors.append(f"{item['sku']}: manifest {field} mismatch")
    if not isinstance(manifest.get("owners"), list) or not manifest.get("owners"):
        errors.append(f"{item['sku']}: manifest owners must be a non-empty array")
    for field in ("inputs", "outputs", "dependencies"):
        if not isinstance(manifest.get(field), list):
            errors.append(f"{item['sku']}: manifest {field} must be an array")
    if not (ROOT / "schemas" / schema_name).is_file():
        errors.append(f"{item['sku']}: missing governing schema {schema_name}")

def validate_evaluations(known, errors):
    count = 0
    evaluation_ids = set()
    evaluation_root = ROOT / "evaluations"
    if not evaluation_root.is_dir():
        return count, evaluation_ids
    for path in evaluation_root.rglob("*.json"):
        count += 1
        doc = read_json(path, errors, path.relative_to(ROOT))
        if doc is None:
            continue
        required = {"evaluation_id", "target_sku", "target_version", "executed_at", "evaluator", "test_cases", "result", "critical_failures"}
        missing = sorted(required - set(doc))
        if missing:
            errors.append(f"{path.relative_to(ROOT)}: missing {', '.join(missing)}")
        if doc.get("target_sku") not in known:
            errors.append(f"{path.relative_to(ROOT)}: unknown target SKU {doc.get('target_sku')}")
        if doc.get("evaluation_id") in evaluation_ids:
            errors.append(f"{path.relative_to(ROOT)}: duplicate evaluation ID {doc.get('evaluation_id')}")
        elif doc.get("evaluation_id"):
            evaluation_ids.add(doc["evaluation_id"])
        if not isinstance(doc.get("test_cases"), list) or len(doc.get("test_cases", [])) < 3:
            errors.append(f"{path.relative_to(ROOT)}: requires at least three test cases")
    return count, evaluation_ids

def validate_maturity_decisions(assets, evaluation_ids, errors):
    count = 0
    by_sku = {asset["sku"]: asset for asset in assets}
    maturity_root = ROOT / "catalog" / "maturity"
    if not maturity_root.is_dir():
        return count
    for path in maturity_root.glob("*.json"):
        count += 1
        doc = read_json(path, errors, path.relative_to(ROOT))
        if doc is None:
            continue
        required = {"target_sku", "target_version", "from_level", "to_level", "requested_at", "evidence", "quality_gate", "approvals", "decision"}
        missing = sorted(required - set(doc))
        if missing:
            errors.append(f"{path.relative_to(ROOT)}: missing {', '.join(missing)}")
            continue
        asset = by_sku.get(doc["target_sku"])
        if asset is None:
            errors.append(f"{path.relative_to(ROOT)}: unknown target SKU {doc['target_sku']}")
            continue
        if doc["target_version"] != asset["version"]:
            errors.append(f"{path.relative_to(ROOT)}: target version mismatch")
        if doc["from_level"] != asset["maturity"]:
            errors.append(f"{path.relative_to(ROOT)}: from_level does not match catalog maturity")
        if doc["to_level"] != doc["from_level"] + 1:
            errors.append(f"{path.relative_to(ROOT)}: promotions must advance exactly one level")
        for evidence_id in doc["evidence"]:
            if evidence_id not in evaluation_ids:
                errors.append(f"{path.relative_to(ROOT)}: unknown evaluation evidence {evidence_id}")
        gate = doc.get("quality_gate", {})
        if doc["decision"] == "approved":
            if not gate.get("structural_validation") or not gate.get("behavioral_validation"):
                errors.append(f"{path.relative_to(ROOT)}: approved promotion lacks required validation")
            if gate.get("critical_failures") != 0:
                errors.append(f"{path.relative_to(ROOT)}: approved promotion has critical failures")
            if not doc.get("approvals"):
                errors.append(f"{path.relative_to(ROOT)}: approved promotion lacks approvals")
    return count

def validate_relationships(assets, known, errors):
    relationship_path = ROOT / "catalog" / "relationships.json"
    if not relationship_path.is_file():
        errors.append("missing catalog/relationships.json")
        return 0
    doc = read_json(relationship_path, errors, "catalog/relationships.json")
    if doc is None:
        return 0
    edges = doc.get("relationships")
    if not isinstance(edges, list):
        errors.append("catalog/relationships.json: relationships must be an array")
        return 0
    seen = set()
    actual_dependencies = set()
    for index, edge in enumerate(edges):
        if not isinstance(edge, dict):
            errors.append(f"catalog/relationships.json: edge {index} must be an object")
            continue
        key = (edge.get("source"), edge.get("relationship"), edge.get("target"))
        if key in seen:
            errors.append(f"catalog/relationships.json: duplicate edge {key}")
        seen.add(key)
        if edge.get("source") not in known:
            errors.append(f"catalog/relationships.json: unknown source {edge.get('source')}")
        if edge.get("target") not in known:
            errors.append(f"catalog/relationships.json: unknown target {edge.get('target')}")
        if edge.get("relationship") == "depends_on":
            actual_dependencies.add((edge.get("source"), edge.get("target")))
    expected_dependencies = {
        (asset["sku"], dependency)
        for asset in assets
        for dependency in asset.get("depends_on", [])
    }
    missing = expected_dependencies - actual_dependencies
    unexpected = actual_dependencies - expected_dependencies
    for source, target in sorted(missing):
        errors.append(f"catalog/relationships.json: missing dependency edge {source} -> {target}")
    for source, target in sorted(unexpected):
        errors.append(f"catalog/relationships.json: unexpected dependency edge {source} -> {target}")
    return len(edges)

def main():
    errors = []
    businesses = {x["code"] for x in load("registries/businesses.json")["businesses"]}
    libraries = {x["code"] for x in load("registries/libraries.json")["libraries"]}
    types = {x["code"] for x in load("registries/asset-types.json")["asset_types"]}
    assets = load_assets()
    skus = [x["sku"] for x in assets]
    ids = [x["asset_id"] for x in assets]
    if len(skus) != len(set(skus)): errors.append("duplicate SKU")
    if len(ids) != len(set(ids)): errors.append("duplicate asset_id")
    known = set(skus)
    for schema_name in sorted(REQUIRED_SCHEMAS):
        schema_path = ROOT / "schemas" / schema_name
        if not schema_path.is_file():
            errors.append(f"missing schema {schema_name}")
        else:
            read_json(schema_path, errors, schema_name)
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
        if item["asset_type"] in FIRST_CLASS_MANIFESTS:
            validate_manifest(item, path, errors)
        for target in item["depends_on"]:
            if target not in known: errors.append(f"{item['sku']}: unknown dependency {target}")
    relationship_count = validate_relationships(assets, known, errors)
    evaluation_count, evaluation_ids = validate_evaluations(known, errors)
    maturity_count = validate_maturity_decisions(assets, evaluation_ids, errors)
    if errors:
        print("VALIDATION FAILED")
        for error in errors: print(f"- {error}")
        return 1
    print(f"VALIDATION PASSED: {len(assets)} assets, {len(REQUIRED_SCHEMAS)} schemas, {relationship_count} relationships, {evaluation_count} evaluations, {maturity_count} maturity decisions")
    return 0

if __name__ == "__main__": sys.exit(main())

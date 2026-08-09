import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = ROOT / "libraries" / "ai-authoritech" / "skills" / "government-documentation"
ASSETS = ROOT / "catalog" / "assets.json"
MAPPINGS = ROOT / "catalog" / "gpt-skill-mappings.json"
DECISIONS = ROOT / "catalog" / "gpt-skill-reconciliation-decisions.json"

EXPECTED = {
    "AA-SKL-000193": "government-functional-requirements-builder",
    "AA-SKL-000194": "government-business-requirements-builder",
    "AA-SKL-000195": "government-functional-workflow-documenter",
    "AA-SKL-000196": "government-use-case-user-story-builder",
    "AA-SKL-000197": "government-functional-sop-user-guide-builder",
    "AA-SKL-000198": "government-uat-script-acceptance-criteria-builder",
    "AA-SKL-000199": "government-data-element-role-access-inventory-builder",
    "AA-SKL-000200": "government-functional-integration-readiness-documenter",
    "AA-SKL-000201": "government-system-impact-assessment-builder",
    "AA-SKL-000202": "government-modernization-adoption-roadmap-builder",
    "AA-SKL-000203": "government-intake-document-routing-builder",
    "AA-SKL-000204": "government-administrative-decision-matrix-builder",
    "AA-SKL-000205": "government-meeting-action-record-builder",
    "AA-SKL-000206": "government-audit-support-package-assembler",
    "AA-SKL-000207": "government-documentation-qa-reviewer",
}
TARGETS = {"AA-GPT-000034", "AA-GPT-000035", "AA-GPT-000037"}


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def test_government_documentation_skills_exist_and_are_governed():
    assets = {a["sku"]: a for a in load(ASSETS)["assets"]}
    for sku, slug in EXPECTED.items():
        path = SKILL_ROOT / slug / "SKILL.md"
        assert path.exists(), path
        text = path.read_text(encoding="utf-8")
        for heading in ("## Procedure", "## Output Contract", "## Guardrails", "## Recovery"):
            assert heading in text
        assert sku in assets
        assert assets[sku]["asset_type"] == "SKL"
        assert assets[sku]["library"] == "GOVDOC"


def test_target_gpts_are_verified_and_mapped():
    decisions = {d["gpt_id"]: d for d in load(DECISIONS)["decisions"]}
    mappings = {m["gpt_id"]: m for m in load(MAPPINGS)["mappings"]}
    family = set(EXPECTED)
    for gid in TARGETS:
        assert decisions[gid]["decision"] == "verified"
        assert "gap" not in decisions[gid]
        dskills = set(decisions[gid]["required_skills"]) | set(decisions[gid]["optional_skills"])
        assert dskills & family
        assert mappings[gid]["verification_status"] == "verified"
        mskills = set(mappings[gid]["required_skills"]) | set(mappings[gid]["optional_skills"])
        assert mskills & family


def test_systems_doc_agent_has_core_functional_documentation_controls():
    decisions = {d["gpt_id"]: d for d in load(DECISIONS)["decisions"]}
    required = set(decisions["AA-GPT-000034"]["required_skills"])
    assert {"AA-SKL-000193", "AA-SKL-000194", "AA-SKL-000195", "AA-SKL-000198", "AA-SKL-000200", "AA-SKL-000207"} <= required


def test_master_admin_has_admin_specific_documentation_controls():
    decisions = {d["gpt_id"]: d for d in load(DECISIONS)["decisions"]}
    required = set(decisions["AA-GPT-000037"]["required_skills"])
    assert {"AA-SKL-000203", "AA-SKL-000204", "AA-SKL-000205", "AA-SKL-000206", "AA-SKL-000207"} <= required

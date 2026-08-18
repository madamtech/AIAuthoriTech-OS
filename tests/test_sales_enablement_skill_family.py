import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = ROOT / "libraries" / "ai-authoritech" / "skills" / "sales-enablement"
ASSETS = ROOT / "catalog" / "assets.json"
MAPPINGS = ROOT / "catalog" / "gpt-skill-mappings.json"
DECISIONS = ROOT / "catalog" / "gpt-skill-reconciliation-decisions.json"

EXPECTED = {
    "AA-SKL-000181": "sales-meeting-strategy-planner",
    "AA-SKL-000182": "discovery-and-stakeholder-research-planner",
    "AA-SKL-000183": "account-and-partner-health-reviewer",
    "AA-SKL-000184": "renewal-and-expansion-planner",
    "AA-SKL-000185": "sales-objection-handling-coach",
    "AA-SKL-000186": "security-solution-positioning-advisor",
    "AA-SKL-000187": "sales-demo-recap-and-follow-up-builder",
    "AA-SKL-000188": "sales-voice-and-communication-adapter",
    "AA-SKL-000189": "security-solution-bom-architect",
    "AA-SKL-000190": "quote-pricing-and-approval-controller",
    "AA-SKL-000191": "security-solution-proposal-assembler",
    "AA-SKL-000192": "sales-enablement-qa-reviewer",
}
TARGET_GPTS = {"AA-GPT-000021", "AA-GPT-000024", "AA-GPT-000025", "AA-GPT-000026", "AA-GPT-000053", "AA-GPT-000056"}


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def test_sales_skills_exist_and_are_governed():
    assets = {a["sku"]: a for a in load(ASSETS)["assets"]}
    for sku, slug in EXPECTED.items():
        skill = SKILL_ROOT / slug / "SKILL.md"
        assert skill.exists(), skill
        text = skill.read_text(encoding="utf-8")
        assert "## Procedure" in text
        assert "## Output Contract" in text
        assert "## Guardrails" in text
        assert "## Recovery" in text
        assert sku in assets
        assert assets[sku]["asset_type"] == "SKL"
        assert assets[sku]["library"] == "SALES"


def test_target_gpts_are_verified_and_mapped_to_new_family():
    decisions = {d["gpt_id"]: d for d in load(DECISIONS)["decisions"]}
    mappings = {m["gpt_id"]: m for m in load(MAPPINGS)["mappings"]}
    new_skus = set(EXPECTED)
    for gid in TARGET_GPTS:
        assert decisions[gid]["decision"] == "verified"
        assert "gap" not in decisions[gid]
        mapped = set(decisions[gid].get("required_skills", [])) | set(decisions[gid].get("optional_skills", []))
        assert mapped & new_skus
        assert mappings[gid]["verification_status"] == "verified"
        mapped2 = set(mappings[gid].get("required_skills", [])) | set(mappings[gid].get("optional_skills", []))
        assert mapped2 & new_skus


def test_classsecure_has_bom_pricing_proposal_and_qa_controls():
    decisions = {d["gpt_id"]: d for d in load(DECISIONS)["decisions"]}
    required = set(decisions["AA-GPT-000056"]["required_skills"])
    assert {"AA-SKL-000189", "AA-SKL-000190", "AA-SKL-000191", "AA-SKL-000192"} <= required


def test_sales_meeting_prep_has_meeting_and_discovery_planning():
    decisions = {d["gpt_id"]: d for d in load(DECISIONS)["decisions"]}
    required = set(decisions["AA-GPT-000053"]["required_skills"])
    assert {"AA-SKL-000181", "AA-SKL-000182"} <= required

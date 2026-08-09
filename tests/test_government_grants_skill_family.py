import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "catalog" / "assets.json"
MAPPINGS = ROOT / "catalog" / "gpt-skill-mappings.json"
DECISIONS = ROOT / "catalog" / "gpt-skill-reconciliation-decisions.json"
SKILL_ROOT = ROOT / "libraries" / "ai-authoritech" / "skills" / "government-grants"

EXPECTED = {
    "AA-SKL-000173": "grant-opportunity-eligibility-assessor",
    "AA-SKL-000174": "grant-readiness-audit",
    "AA-SKL-000175": "grant-narrative-architect",
    "AA-SKL-000176": "grant-need-impact-builder",
    "AA-SKL-000177": "grant-goals-outcomes-evaluation-designer",
    "AA-SKL-000178": "grant-budget-narrative-builder",
    "AA-SKL-000179": "grant-capacity-sustainability-planner",
    "AA-SKL-000180": "grant-proposal-qa-reviewer",
}


def test_skill_files_exist_and_are_registered():
    assets = json.loads(ASSETS.read_text())
    by_sku = {a["sku"]: a for a in assets["assets"]}
    for sku, slug in EXPECTED.items():
        path = SKILL_ROOT / slug / "SKILL.md"
        assert path.exists(), f"missing {path}"
        text = path.read_text()
        assert "## Procedure" in text
        assert "## Output Contract" in text
        assert "## Guardrails" in text
        assert "## Recovery" in text
        assert sku in by_sku
        assert by_sku[sku]["library"] == "GRANT"
        assert by_sku[sku]["path"].endswith(slug)


def test_grant_gpts_are_fully_reconciled():
    decisions = json.loads(DECISIONS.read_text())
    rows = {d["gpt_id"]: d for d in decisions["decisions"]}
    mappings = json.loads(MAPPINGS.read_text())
    mapped = {m["gpt_id"]: m for m in mappings["mappings"]}
    for gpt_id in ("AA-GPT-000032", "AA-GPT-000033"):
        assert rows[gpt_id]["decision"] == "verified"
        assert "gap" not in rows[gpt_id]
        assert mapped[gpt_id]["verification_status"] == "verified"
        assert mapped[gpt_id]["required_skills"]
        assert set(mapped[gpt_id]["required_skills"]).issubset(EXPECTED)
        assert set(mapped[gpt_id]["optional_skills"]).issubset(EXPECTED)


def test_no_duplicate_grant_skill_skus():
    assets = json.loads(ASSETS.read_text())
    skus = [a["sku"] for a in assets["assets"]]
    for sku in EXPECTED:
        assert skus.count(sku) == 1

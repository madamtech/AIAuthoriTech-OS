#!/usr/bin/env python3
"""Build the reusable Government Grants skill family and reconcile grant GPTs.

This is intentionally deterministic so the generated SKILL assets, catalog records,
GPT mappings, and manifests stay synchronized.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "catalog" / "assets.json"
MAPPINGS = ROOT / "catalog" / "gpt-skill-mappings.json"
DECISIONS = ROOT / "catalog" / "gpt-skill-reconciliation-decisions.json"
MANIFEST_ROOT = ROOT / "gpts" / "manifests"
SKILL_ROOT = ROOT / "libraries" / "ai-authoritech" / "skills" / "government-grants"

DEFAULT_VISUAL = "libraries/ai-authoritech/skills/image-generation/gpt-visual-intelligence-enhancement/SKILL.md"

SKILLS = [
    {
        "sku": "AA-SKL-000173",
        "slug": "grant-opportunity-eligibility-assessor",
        "asset_id": "grants.grant-opportunity-eligibility-assessor.v1",
        "name": "Grant Opportunity and Eligibility Assessor",
        "depends_on": ["AA-SKL-000058"],
        "description": "Assess grant opportunity fit, eligibility, required evidence, deadlines, restrictions, and go/no-go readiness using verified source material. Use before investing in a grant application. Do not invent eligibility, waive requirements, or treat a probable fit as confirmed awardability.",
        "procedure": [
            "Capture the funder, program, notice or solicitation, deadline, award range, applicant type, geography, purpose, and required match or cost share.",
            "Extract mandatory eligibility conditions, exclusions, registrations, evidence, attachments, submission rules, scoring factors, and timing constraints from authoritative grant materials.",
            "Compare the opportunity against the applicant's verified facts and classify each criterion as met, unmet, unclear, or evidence-needed.",
            "Produce a fit assessment with disqualifiers, open questions, evidence owners, and a go, conditional-go, or no-go recommendation."
        ],
        "output": "Provide opportunity summary, eligibility matrix, disqualifiers, evidence gaps, required registrations/attachments, deadline risks, fit rationale, and a clearly labeled go/no-go recommendation.",
        "guardrails": [
            "Use the current official notice, funder portal, or program guidance as the controlling source when available.",
            "Separate verified eligibility from assumptions and label unresolved criteria.",
            "Do not claim that eligibility guarantees competitiveness or funding.",
            "Escalate legal, tax, lobbying, procurement, or specialized compliance questions to qualified reviewers."
        ],
        "recovery": "If the official notice, applicant facts, or required eligibility evidence is missing, return a conditional assessment and identify exactly what must be verified before application work proceeds."
    },
    {
        "sku": "AA-SKL-000174",
        "slug": "grant-readiness-audit",
        "asset_id": "grants.grant-readiness-audit.v1",
        "name": "Grant Readiness Auditor",
        "depends_on": ["AA-SKL-000173", "AA-SKL-000063"],
        "description": "Run a structured grant-readiness audit across mission fit, organizational capacity, community need, outcomes, evidence, partnerships, financial readiness, sustainability, evaluation, and documentation. Use to determine what must be strengthened before drafting. Do not fabricate capacity, partnerships, outcomes, or prior performance.",
        "procedure": [
            "Collect the applicant's mission, origin, target population, problem evidence, solution, goals, delivery capacity, funding need, sustainability plan, evaluation approach, and available documentation.",
            "Normalize supplied facts into grant-ready language while preserving uncertainty and source boundaries.",
            "Score readiness by section and flag unsupported claims, missing evidence, internal contradictions, and dependencies.",
            "Return a prioritized remediation plan before proposal drafting begins."
        ],
        "output": "Provide section-by-section readiness findings, confirmed facts, evidence gaps, risk flags, clarifications needed, and a prioritized readiness action plan.",
        "guardrails": [
            "Never invent statistics, approvals, partners, certifications, revenue, prior awards, or outcomes.",
            "Use cautious language where evidence is preliminary or incomplete.",
            "Keep applicant-provided facts distinct from external research.",
            "Do not represent a readiness audit as a guarantee of award success."
        ],
        "recovery": "If information is incomplete, preserve the audit state, summarize what is known, and ask only the minimum questions required to complete the next readiness section."
    },
    {
        "sku": "AA-SKL-000175",
        "slug": "grant-narrative-architect",
        "asset_id": "grants.grant-narrative-architect.v1",
        "name": "Grant Narrative Architect",
        "depends_on": ["AA-SKL-000173", "AA-SKL-000174"],
        "description": "Architect a funder-aligned grant narrative from verified applicant facts and solicitation requirements, covering executive summary, organizational background, need, approach, outcomes, impact, capacity, budget use, sustainability, and evaluation. Do not add unsupported facts or overwrite funder-required structure.",
        "procedure": [
            "Map every required application question or narrative section to verified source facts, evidence, and scoring criteria.",
            "Design the narrative throughline from need to solution to measurable outcomes, public/community value, capacity, use of funds, sustainability, and evaluation.",
            "Draft in plain, specific, funder-aware language using only supported claims and clearly marked placeholders for unresolved evidence.",
            "Check cross-section consistency, word/character limits, terminology, and alignment to the opportunity's stated priorities."
        ],
        "output": "Provide a complete grant narrative or section set with requirement traceability, evidence placeholders where needed, consistent terminology, and clearly labeled open items.",
        "guardrails": [
            "Do not invent impact data, beneficiaries, budgets, partnerships, letters of support, or prior results.",
            "Preserve funder-required headings, order, limits, and terminology when supplied.",
            "Avoid hype and unsupported superlatives.",
            "Do not imply that persuasive writing can cure an eligibility or evidence failure."
        ],
        "recovery": "If a required narrative section lacks supporting facts, draft only what is supportable, insert a visible evidence-needed marker, and route the gap back to the readiness audit."
    },
    {
        "sku": "AA-SKL-000176",
        "slug": "grant-need-impact-builder",
        "asset_id": "grants.grant-need-impact-builder.v1",
        "name": "Grant Need and Community Impact Builder",
        "depends_on": ["AA-SKL-000174", "AA-SKL-000105"],
        "description": "Build evidence-grounded grant problem statements, target-population narratives, need justification, community/public value, and impact logic. Use when a proposal must connect a documented problem to a credible intervention. Do not invent statistics or stereotype affected communities.",
        "procedure": [
            "Define the affected population, geography, problem, current conditions, barriers, and consequences if the problem remains unresolved.",
            "Organize verified quantitative evidence, qualitative evidence, lived experience, service gaps, and contextual trends without overstating causality.",
            "Connect the proposed intervention to direct beneficiaries, broader public/community value, and plausible change mechanisms.",
            "Identify evidence weaknesses and distinguish baseline facts from projected impact."
        ],
        "output": "Provide problem statement, target-population profile, evidence table, urgency rationale, intervention-to-impact logic, broader public value, and evidence gaps.",
        "guardrails": [
            "Use demographic and community language respectfully and only when relevant to eligibility, need, or impact.",
            "Do not create unsupported statistics, percentages, prevalence estimates, or causal claims.",
            "Label projections as projections.",
            "Protect sensitive personal or community-level data."
        ],
        "recovery": "If need evidence is weak, identify acceptable evidence categories to source and downgrade claims rather than manufacturing support."
    },
    {
        "sku": "AA-SKL-000177",
        "slug": "grant-goals-outcomes-evaluation-designer",
        "asset_id": "grants.grant-goals-outcomes-evaluation-designer.v1",
        "name": "Grant Goals, Outcomes, and Evaluation Designer",
        "depends_on": ["AA-SKL-000174", "AA-SKL-000176"],
        "description": "Design grant goals, objectives, outputs, outcomes, indicators, baselines, targets, data collection, learning loops, and evaluation plans that are proportional to the project and supported by available capacity. Do not promise impossible outcomes or fabricate baselines.",
        "procedure": [
            "Translate the proposed work into a logic chain of activities, outputs, short-term outcomes, long-term outcomes, and intended community/public value.",
            "Define specific indicators, baseline status, target values or target-setting method, data source, collection frequency, responsible owner, and reporting use.",
            "Check that measures are feasible, privacy-conscious, attributable where appropriate, and aligned to funder requirements.",
            "Document how findings will improve implementation, sustainability, or scaling decisions."
        ],
        "output": "Provide goals, SMART-style objectives where appropriate, output/outcome matrix, indicators, baselines, targets, data sources, cadence, owners, evaluation approach, and learning plan.",
        "guardrails": [
            "Do not invent baselines or numerical targets without a defensible basis.",
            "Distinguish outputs from outcomes and correlation from attribution.",
            "Minimize personal data collection and identify privacy or consent considerations.",
            "Avoid measures that create perverse incentives or exclude affected populations."
        ],
        "recovery": "If baseline data is unavailable, define a baseline-establishment method and provisional indicators instead of pretending measurement readiness exists."
    },
    {
        "sku": "AA-SKL-000178",
        "slug": "grant-budget-narrative-builder",
        "asset_id": "grants.grant-budget-narrative-builder.v1",
        "name": "Grant Budget Narrative Builder",
        "depends_on": ["AA-SKL-000173", "AA-SKL-000175"],
        "description": "Build a traceable grant use-of-funds plan and budget narrative that connects requested costs to project activities, allowability constraints, timing, and expected outputs. Use with a user-supplied or approved budget. Do not invent prices, indirect rates, salaries, match commitments, or allowability determinations.",
        "procedure": [
            "Capture the requested amount, project period, budget categories, known unit costs, staffing assumptions, match/cost-share requirements, and funder restrictions.",
            "Trace each cost to a project activity, deliverable, beneficiary need, or operational requirement.",
            "Explain why each cost is necessary, reasonable based on supplied evidence, timed appropriately, and non-duplicative.",
            "Flag unsupported estimates, missing quotes, unclear allowability, arithmetic inconsistencies, and unfunded dependencies."
        ],
        "output": "Provide budget narrative by category, cost-to-activity traceability, assumptions, match/cost-share notes, evidence needs, arithmetic checks, and allowability questions requiring verification.",
        "guardrails": [
            "Never invent vendor pricing, salaries, fringe, indirect rates, match commitments, or approved costs.",
            "Do not provide legal, tax, accounting, or definitive allowability advice.",
            "Use current funder budget rules when supplied or verified.",
            "Keep restricted or confidential financial information appropriately minimized."
        ],
        "recovery": "If the budget is incomplete, provide a narrative framework and a missing-cost checklist rather than filling gaps with guessed numbers."
    },
    {
        "sku": "AA-SKL-000179",
        "slug": "grant-capacity-sustainability-planner",
        "asset_id": "grants.grant-capacity-sustainability-planner.v1",
        "name": "Grant Capacity and Sustainability Planner",
        "depends_on": ["AA-SKL-000174", "AA-SKL-000175"],
        "description": "Build credible organizational-capacity and post-grant sustainability narratives using verified experience, systems, partnerships, staffing, revenue, adoption, and continuation strategies. Do not invent partners, commitments, certifications, funding pipelines, or organizational history.",
        "procedure": [
            "Inventory verified delivery experience, leadership capability, staffing, systems, governance, partnerships, facilities, technology, financial controls, and prior accomplishments relevant to the project.",
            "Identify capacity risks and mitigation actions required during the grant period.",
            "Define realistic continuation pathways after grant funding, such as operating revenue, public funding, philanthropy, partnerships, cost absorption, institutionalization, or phased scaling, using only supported assumptions.",
            "Connect sustainability actions to project milestones and decision points rather than vague future promises."
        ],
        "output": "Provide organizational-capacity narrative, capacity evidence inventory, delivery-risk mitigations, sustainability pathways, post-grant milestones, assumptions, and unresolved dependencies.",
        "guardrails": [
            "Do not invent partnerships, letters of commitment, funding sources, certifications, or prior performance.",
            "Distinguish existing capacity from capacity that depends on the requested grant.",
            "Avoid asserting future revenue or continuation as certain.",
            "Flag sustainability claims that lack an owner, mechanism, or timeline."
        ],
        "recovery": "If sustainability is weak, present realistic scenarios and prerequisite actions instead of overstating long-term viability."
    },
    {
        "sku": "AA-SKL-000180",
        "slug": "grant-proposal-qa-reviewer",
        "asset_id": "grants.grant-proposal-qa-reviewer.v1",
        "name": "Grant Proposal QA Reviewer",
        "depends_on": ["AA-SKL-000173", "AA-SKL-000175", "AA-SKL-000177", "AA-SKL-000178", "AA-SKL-000179"],
        "description": "Review a grant application for requirement coverage, eligibility consistency, evidence quality, narrative coherence, scoring alignment, budget traceability, outcomes logic, formatting limits, risk, and submission readiness. Use before final human review. Do not certify compliance or predict an award.",
        "procedure": [
            "Create a requirement traceability matrix from the current solicitation, portal questions, attachments, scoring criteria, and formatting rules.",
            "Review every application section against verified applicant facts, evidence, budget, outcomes, sustainability, and required attachments.",
            "Identify contradictions, unsupported claims, missing responses, weak scoring alignment, arithmetic or traceability issues, limit violations, and submission blockers.",
            "Classify findings by severity and produce a final human-review checklist."
        ],
        "output": "Provide requirement traceability, pass/needs-fix/blocker findings, evidence issues, scoring-alignment notes, budget/outcome consistency checks, submission checklist, and final human-review status.",
        "guardrails": [
            "Do not certify legal or regulatory compliance or imply funder approval.",
            "Do not predict award probability from writing quality alone.",
            "Preserve unresolved facts as unresolved rather than silently correcting them.",
            "Require human review of final submission content, attachments, signatures, certifications, and portal entries."
        ],
        "recovery": "If the controlling solicitation or final application package is incomplete, mark the review not submission-ready and list the missing sources or artifacts required for a complete QA pass."
    },
]

GPT_SKILLS = {
    "AA-GPT-000032": {
        "required": ["AA-SKL-000174", "AA-SKL-000175", "AA-SKL-000176", "AA-SKL-000177", "AA-SKL-000178", "AA-SKL-000179", "AA-SKL-000180"],
        "optional": ["AA-SKL-000173"],
    },
    "AA-GPT-000033": {
        "required": ["AA-SKL-000173", "AA-SKL-000175", "AA-SKL-000176", "AA-SKL-000178", "AA-SKL-000180"],
        "optional": ["AA-SKL-000174", "AA-SKL-000177", "AA-SKL-000179"],
    },
}


def write_json(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def skill_markdown(skill: dict) -> str:
    proc = "\n".join(f"{i}. {step}" for i, step in enumerate(skill["procedure"], 1))
    guards = "\n".join(f"- {g}" for g in skill["guardrails"])
    return f'''---\nname: {skill["slug"]}\ndescription: {skill["description"]}\n---\n\n# {skill["name"]}\n\n## Procedure\n\n{proc}\n\n## Output Contract\n\n{skill["output"]}\n\n## Guardrails\n\n{guards}\n\n## Recovery\n\n{skill["recovery"]}\n'''


def build_skills() -> None:
    SKILL_ROOT.mkdir(parents=True, exist_ok=True)
    for skill in SKILLS:
        folder = SKILL_ROOT / skill["slug"]
        folder.mkdir(parents=True, exist_ok=True)
        (folder / "SKILL.md").write_text(skill_markdown(skill), encoding="utf-8")


def update_assets() -> None:
    doc = json.loads(ASSETS.read_text(encoding="utf-8"))
    existing = {a["sku"] for a in doc["assets"]}
    for skill in SKILLS:
        record = {
            "sku": skill["sku"],
            "asset_id": skill["asset_id"],
            "name": skill["name"],
            "asset_type": "SKL",
            "business": "AA",
            "library": "GRANT",
            "version": "1.0.0",
            "status": "testing",
            "maturity": 2,
            "path": f'libraries/ai-authoritech/skills/government-grants/{skill["slug"]}',
            "depends_on": skill["depends_on"],
        }
        if skill["sku"] in existing:
            for idx, current in enumerate(doc["assets"]):
                if current["sku"] == skill["sku"]:
                    doc["assets"][idx] = record
                    break
        else:
            doc["assets"].append(record)
    write_json(ASSETS, doc)


def update_reconciliation() -> None:
    decisions = json.loads(DECISIONS.read_text(encoding="utf-8"))
    for row in decisions["decisions"]:
        gpt_id = row["gpt_id"]
        if gpt_id in GPT_SKILLS:
            row["decision"] = "verified"
            row["required_skills"] = GPT_SKILLS[gpt_id]["required"]
            row["optional_skills"] = GPT_SKILLS[gpt_id]["optional"]
            row.pop("gap", None)
    write_json(DECISIONS, decisions)

    mappings = json.loads(MAPPINGS.read_text(encoding="utf-8"))
    by_id = {m["gpt_id"]: m for m in mappings["mappings"]}
    names = {d["gpt_id"]: d["name"] for d in decisions["decisions"]}
    for gpt_id, selected in GPT_SKILLS.items():
        desired = {
            "gpt_id": gpt_id,
            "gpt_name": names[gpt_id],
            "verification_status": "verified",
            "evidence": "Verified against the captured Builder configuration after adding the governed Government Grants reusable skill family.",
            "required_skills": selected["required"],
            "optional_skills": selected["optional"],
            "default_enhancements": [DEFAULT_VISUAL],
        }
        if gpt_id in by_id:
            by_id[gpt_id].clear()
            by_id[gpt_id].update(desired)
        else:
            mappings["mappings"].append(desired)
    write_json(MAPPINGS, mappings)


def update_manifests() -> None:
    manifest_index = {}
    for path in MANIFEST_ROOT.glob("*/manifest.json"):
        data = json.loads(path.read_text(encoding="utf-8"))
        if data.get("gpt_id"):
            manifest_index[data["gpt_id"]] = (path, data)
    for gpt_id, selected in GPT_SKILLS.items():
        path, manifest = manifest_index[gpt_id]
        manifest["skills"] = {
            "required": selected["required"],
            "optional": selected["optional"],
            "default_enhancements": [DEFAULT_VISUAL],
        }
        marker = "1.0.x - Reconciled to the reusable Government Grants skill family."
        if marker not in manifest.setdefault("change_log", []):
            manifest["change_log"].append(marker)
        path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    build_skills()
    update_assets()
    update_reconciliation()
    update_manifests()
    print(json.dumps({"skills_built": [s["sku"] for s in SKILLS], "gpts_reconciled": sorted(GPT_SKILLS)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = ROOT / "libraries" / "ai-authoritech" / "skills" / "sales-enablement"
ASSETS = ROOT / "catalog" / "assets.json"
MAPPINGS = ROOT / "catalog" / "gpt-skill-mappings.json"
DECISIONS = ROOT / "catalog" / "gpt-skill-reconciliation-decisions.json"
MANIFEST_ROOT = ROOT / "gpts" / "manifests"
VISUAL = "libraries/ai-authoritech/skills/image-generation/gpt-visual-intelligence-enhancement/SKILL.md"

SKILLS = [
    ("AA-SKL-000181", "Sales Meeting Strategy Planner", "sales-meeting-strategy-planner", "Prepare evidence-grounded sales meetings with clear objectives, stakeholder hypotheses, discovery priorities, decision paths, risks, and next-step goals.", ["Clarify meeting purpose, account context, stage, attendees, desired decision, and known constraints.", "Separate verified account facts from hypotheses and research gaps.", "Build a concise meeting plan with objectives, agenda, stakeholder considerations, discovery priorities, value hypotheses, risks, and desired next steps."], ["Do not invent customer needs, authority, budget, timelines, or commitments.", "Label assumptions and research gaps.", "Do not treat a meeting plan as an approved commercial commitment."]),
    ("AA-SKL-000182", "Discovery and Stakeholder Research Planner", "discovery-stakeholder-research-planner", "Build role-aware discovery questions and stakeholder research plans for sales opportunities without presenting assumptions as customer facts.", ["Identify the account, opportunity, stakeholder roles, known business context, and information gaps.", "Create prioritized discovery questions spanning business outcomes, process, technical environment, decision criteria, stakeholders, timing, risk, and success measures.", "Produce a stakeholder research plan separating public facts, internal facts, hypotheses, and questions requiring validation."], ["Never fabricate stakeholder roles, pain points, authority, or technical conditions.", "Use current public sources when research is required and distinguish them from internal information.", "Avoid collecting unnecessary sensitive or confidential information."]),
    ("AA-SKL-000183", "Account and Partner Health Reviewer", "account-partner-health-reviewer", "Review customer or partner health using evidence, relationship signals, activity, risks, opportunities, and unresolved questions for management-ready sales decisions.", ["Collect the account or partner scope, review period, relationship state, activity, performance signals, open issues, and planned actions.", "Classify evidence into strengths, risks, opportunities, dependencies, and unknowns.", "Return a concise health summary with confidence, priorities, owners, and follow-up actions."], ["Do not invent performance, customer sentiment, partner capability, pipeline, or relationship status.", "Keep public facts distinct from internal sales information.", "Do not expose confidential commercial information in inappropriate outputs."]),
    ("AA-SKL-000184", "Renewal and Expansion Planner", "renewal-expansion-planner", "Create evidence-based renewal, retention, refresh, and expansion plans for existing accounts while keeping pricing, commitments, and approvals governed.", ["Capture renewal date, relationship context, current footprint, stakeholders, known issues, value evidence, risks, and expansion signals.", "Develop retention priorities, renewal actions, expansion hypotheses, stakeholder engagement, dependencies, and timing.", "Return an action plan with owners, milestones, open questions, and approval gates."], ["Never invent contract terms, renewal probability, pricing, commitments, or customer intent.", "Mark assumptions and required approvals.", "Do not present expansion hypotheses as customer-approved plans."]),
    ("AA-SKL-000185", "Sales Objection Handling Coach", "sales-objection-handling-coach", "Prepare accurate, non-manipulative objection handling for sales conversations using verified value, evidence, questions, and appropriate escalation paths.", ["Identify the exact objection, context, stakeholder, stage, and evidence available.", "Classify whether the objection concerns value, fit, risk, timing, price, competition, authority, implementation, or trust.", "Build a response using acknowledgment, clarifying questions, verified evidence, options, boundaries, and next steps."], ["Do not fabricate product claims, customer references, competitor weaknesses, discounts, approvals, or guarantees.", "Do not use coercive or deceptive tactics.", "Escalate legal, compliance, pricing, contractual, or product-certification questions to authorized owners."]),
    ("AA-SKL-000186", "Security Solution Positioning Advisor", "security-solution-positioning-advisor", "Translate verified security requirements and approved product information into restrained solution positioning, comparisons, use cases, and sales talking points.", ["Capture the security use case, environment, stakeholder priorities, constraints, and approved source material.", "Map verified requirements to relevant solution capabilities and identify unsupported or unknown points.", "Produce positioning, differentiators, discovery follow-ups, and validation requirements."], ["Use official or approved product sources for specifications and compatibility.", "Never invent performance, certifications, integrations, availability, pricing, or competitive claims.", "Do not present preliminary architecture as an approved design."]),
    ("AA-SKL-000187", "Sales Demo Recap and Follow-Up Builder", "sales-demo-recap-follow-up-builder", "Convert verified sales or product-demo notes into concise recaps, customer follow-up, action items, unresolved questions, and internal next steps.", ["Collect attendees, objectives, demonstrated capabilities, questions, feedback, decisions, and open items.", "Separate what was demonstrated from what was discussed, proposed, or still requires verification.", "Generate internal recap and, when requested, an external follow-up with owners and due dates."], ["Do not claim a feature was demonstrated or agreed unless supported by notes.", "Do not invent commitments, delivery dates, pricing, or technical validation.", "Flag items requiring product, technical, legal, or commercial confirmation."]),
    ("AA-SKL-000188", "Sales Voice and Communication Adapter", "sales-voice-communication-adapter", "Adapt sales communications to a defined representative, audience, channel, and context while preserving factual accuracy, governance, and the original business intent.", ["Capture the target representative or approved voice traits, audience, purpose, channel, and source facts.", "Preserve claims, commitments, technical details, and required disclaimers while adapting tone, cadence, structure, and level of detail.", "Return the adapted communication plus any facts or claims that still need verification."], ["Do not impersonate a real person deceptively or invent their private views.", "Never change factual meaning to improve persuasion.", "Do not create unauthorized pricing, commitments, approvals, or product claims."]),
    ("AA-SKL-000189", "Security Solution BOM Architect", "security-solution-bom-architect", "Translate validated security-system discovery inputs into a structured bill of materials using governed configuration rules, quantities, dependencies, and source references.", ["Validate required discovery inputs and reject missing or invalid quantities instead of autofilling.", "Apply documented configuration logic to select models, licenses, hardware, accessories, and quantity relationships.", "Return a BOM with assumptions, source references, alternates when required, and unresolved configuration questions."], ["Never invent SKUs, quantities, compatibility, licensing, or configuration rules.", "Use approved price lists, configuration documents, or user-provided rules as the source of truth.", "Keep BOM generation separate from final pricing approval."]),
    ("AA-SKL-000190", "Quote Pricing and Approval Controller", "quote-pricing-approval-controller", "Calculate governed quote pricing from approved source data and formulas while preserving price-list provenance, renewal logic, approval boundaries, and calculation transparency.", ["Confirm the governing price list, effective date, currency, pricing basis, formulas, discounts if authorized, and renewal rules.", "Calculate line totals, year-one totals, recurring totals, alternates, and exceptions with reproducible arithmetic.", "Return pricing with source provenance, assumptions, approval status, and any required commercial review."], ["Never invent prices, discounts, multipliers, approval authority, taxes, freight, or commercial terms.", "Do not use stale pricing when the effective date is uncertain.", "Do not represent calculated pricing as approved unless approval evidence is provided."]),
    ("AA-SKL-000191", "Security Solution Proposal Assembler", "security-solution-proposal-assembler", "Assemble a clear customer- or partner-ready security solution proposal from verified discovery, BOM, pricing, recommendation logic, scope notes, alternates, and disclaimers.", ["Collect the validated discovery summary, recommended configuration, alternate configuration when required, BOM, pricing, and scope constraints.", "Assemble the proposal with executive summary, requirements, recommendation, alternatives, line items, year-one and recurring totals, feature notes, assumptions, exclusions, and next steps.", "Apply required visual or export formatting only after content is verified."], ["Do not invent customer requirements, solution capabilities, pricing, or commitments.", "Keep recommendation logic traceable to validated discovery inputs.", "Include scope and pricing disclaimers whenever required by the governed quoting rules."]),
    ("AA-SKL-000192", "Sales Enablement QA Reviewer", "sales-enablement-qa-reviewer", "Review sales briefs, meeting plans, account summaries, objection responses, quotes, proposals, and follow-ups for factual support, commercial governance, clarity, and readiness.", ["Identify the deliverable type, intended audience, source materials, and decision or communication risk.", "Check factual support, assumptions, product claims, calculations, pricing provenance, commitments, stakeholder details, sensitive information, and required disclaimers.", "Return pass, conditional pass, or fail with exact corrections and owners."], ["Never convert an unsupported claim into a supported one by rewriting it.", "Fail outputs containing invented pricing, product claims, customer facts, approvals, or commitments.", "Require human review where pricing, legal, contractual, compliance, or externally binding content is involved."]),
]

MAPPING_UPDATES = {
    "AA-GPT-000021": {"decision": "verified", "required_add": ["AA-SKL-000183", "AA-SKL-000184", "AA-SKL-000186", "AA-SKL-000192"], "optional_add": ["AA-SKL-000181", "AA-SKL-000182", "AA-SKL-000185"]},
    "AA-GPT-000024": {"decision": "verified", "required_add": ["AA-SKL-000181", "AA-SKL-000182", "AA-SKL-000185", "AA-SKL-000186", "AA-SKL-000187", "AA-SKL-000188"], "optional_add": ["AA-SKL-000183", "AA-SKL-000192"]},
    "AA-GPT-000025": {"decision": "verified", "required_add": ["AA-SKL-000181", "AA-SKL-000182", "AA-SKL-000185", "AA-SKL-000186", "AA-SKL-000187", "AA-SKL-000188"], "optional_add": ["AA-SKL-000183", "AA-SKL-000192"]},
    "AA-GPT-000026": {"decision": "verified", "required_add": ["AA-SKL-000187", "AA-SKL-000188"], "optional_add": ["AA-SKL-000181", "AA-SKL-000185"]},
    "AA-GPT-000053": {"decision": "verified", "required_add": ["AA-SKL-000181", "AA-SKL-000182"], "optional_add": []},
    "AA-GPT-000056": {"decision": "verified", "required_add": ["AA-SKL-000189", "AA-SKL-000190", "AA-SKL-000191", "AA-SKL-000192"], "optional_add": ["AA-SKL-000151", "AA-SKL-000186"]},
}


def unique(items):
    return list(dict.fromkeys(items))


def skill_markdown(name, description, procedure, guardrails):
    slug = name.lower().replace("&", "and").replace(",", "").replace(" ", "-")
    steps = "\n".join(f"{i}. {x}" for i, x in enumerate(procedure, 1))
    guards = "\n".join(f"- {x}" for x in guardrails)
    return f"---\nname: {slug}\ndescription: {description}\n---\n\n# {name}\n\n## Procedure\n\n{steps}\n\n## Output Contract\n\nProvide verified inputs, assumptions, findings or calculations, recommendations or output, unresolved questions, approval/validation needs, and next actions appropriate to the sales task.\n\n## Guardrails\n\n{guards}\n\n## Recovery\n\nIf critical source data, authority, product evidence, pricing, customer facts, or decision criteria are missing, stop at the affected boundary. Preserve verified work, label the gap, and request only the minimum information or authorized review needed to continue.\n"


def write_skills():
    for sku, name, slug, desc, procedure, guardrails in SKILLS:
        folder = SKILL_ROOT / slug
        folder.mkdir(parents=True, exist_ok=True)
        (folder / "SKILL.md").write_text(skill_markdown(name, desc, procedure, guardrails), encoding="utf-8")


def update_assets():
    data = json.loads(ASSETS.read_text(encoding="utf-8"))
    existing = {a["sku"] for a in data["assets"]}
    for sku, name, slug, *_ in SKILLS:
        if sku not in existing:
            data["assets"].append({
                "sku": sku,
                "asset_id": f"sales-enablement.{slug}.v1",
                "name": name,
                "asset_type": "SKL",
                "business": "AA",
                "library": "SALES",
                "version": "1.0.0",
                "status": "testing",
                "maturity": 2,
                "path": f"libraries/ai-authoritech/skills/sales-enablement/{slug}",
                "depends_on": [],
            })
    ASSETS.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def update_decisions():
    data = json.loads(DECISIONS.read_text(encoding="utf-8"))
    by_id = {d["gpt_id"]: d for d in data["decisions"]}
    for gid, upd in MAPPING_UPDATES.items():
        d = by_id[gid]
        d["decision"] = upd["decision"]
        d["required_skills"] = unique(d.get("required_skills", []) + upd["required_add"])
        d["optional_skills"] = unique(d.get("optional_skills", []) + upd["optional_add"])
        d.pop("gap", None)
    data["updated_at"] = "2026-08-09"
    DECISIONS.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def update_mappings():
    data = json.loads(MAPPINGS.read_text(encoding="utf-8"))
    by_id = {m["gpt_id"]: m for m in data["mappings"]}
    decisions = json.loads(DECISIONS.read_text(encoding="utf-8"))
    d_by_id = {d["gpt_id"]: d for d in decisions["decisions"]}
    for gid in MAPPING_UPDATES:
        d = d_by_id[gid]
        m = by_id.get(gid)
        if m is None:
            m = {"gpt_id": gid, "gpt_name": d["name"]}
            data["mappings"].append(m)
        m["gpt_name"] = d["name"]
        m["verification_status"] = "verified"
        m["evidence"] = "Verified against the captured Builder configuration and the governed Sales Enablement skill family."
        m["required_skills"] = d["required_skills"]
        m["optional_skills"] = d["optional_skills"]
        m["default_enhancements"] = [] if gid == "AA-GPT-000047" else [VISUAL]
    data["updated_at"] = "2026-08-09"
    MAPPINGS.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def update_manifests():
    decisions = json.loads(DECISIONS.read_text(encoding="utf-8"))
    d_by_id = {d["gpt_id"]: d for d in decisions["decisions"]}
    targets = set(MAPPING_UPDATES)
    seen = set()
    for path in MANIFEST_ROOT.glob("*/manifest.json"):
        data = json.loads(path.read_text(encoding="utf-8"))
        gid = data.get("gpt_id")
        if gid not in targets:
            continue
        d = d_by_id[gid]
        data.setdefault("skills", {})["required"] = d["required_skills"]
        data["skills"]["optional"] = d["optional_skills"]
        if "default_enhancements" not in data["skills"]:
            data["skills"]["default_enhancements"] = [VISUAL]
        log = data.setdefault("change_log", [])
        note = "1.0.0 - Reconciled against reusable Sales Enablement skills."
        if note not in log:
            log.append(note)
        path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
        seen.add(gid)
    missing = targets - seen
    if missing:
        raise RuntimeError(f"Missing GPT manifests: {sorted(missing)}")


def main():
    write_skills()
    update_assets()
    update_decisions()
    update_mappings()
    update_manifests()
    print(json.dumps({"skills_created": len(SKILLS), "gpts_reconciled": len(MAPPING_UPDATES)}, indent=2))


if __name__ == "__main__":
    main()

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = ROOT / "libraries" / "ai-authoritech" / "skills" / "government-documentation"
ASSETS = ROOT / "catalog" / "assets.json"
MAPPINGS = ROOT / "catalog" / "gpt-skill-mappings.json"
DECISIONS = ROOT / "catalog" / "gpt-skill-reconciliation-decisions.json"
MANIFEST_ROOT = ROOT / "gpts" / "manifests"
VISUAL = "libraries/ai-authoritech/skills/image-generation/gpt-visual-intelligence-enhancement/SKILL.md"

SKILLS = [
    ("AA-SKL-000193", "Government Functional Requirements Builder", "government-functional-requirements-builder", "Create government-ready functional requirements documents that describe user-facing behavior, business rules, roles, inputs, outputs, dependencies, and acceptance needs without drifting into engineering design.", ["Confirm scope, process owner, users, current-state behavior, desired outcomes, constraints, and source evidence.", "Translate source material into uniquely identified functional requirements with rationale, priority, dependencies, and clarifications needed.", "Review every requirement for testability, consistency, traceability, and functional-only language."], ["Do not write code, APIs, database schemas, network designs, cybersecurity configurations, or backend implementation instructions.", "Do not invent requirements, roles, systems, approvals, or policy interpretations.", "Label unresolved requirements and require process-owner review."]),
    ("AA-SKL-000194", "Government Business Requirements Builder", "government-business-requirements-builder", "Create structured business requirements documents covering mission need, objectives, stakeholders, scope, business rules, success measures, constraints, assumptions, and traceability.", ["Collect the business problem, mission context, stakeholders, desired outcomes, scope, constraints, policies supplied by the user, and success measures.", "Organize business requirements separately from functional or technical design.", "Return a traceable BRD with priorities, dependencies, assumptions, risks, and clarifications needed."], ["Do not convert policy into legal interpretation.", "Do not invent business rules, statutory requirements, stakeholder authority, or success metrics.", "Keep technical implementation outside the BRD unless included only as a clearly labeled external dependency."]),
    ("AA-SKL-000195", "Government Functional Workflow Documenter", "government-functional-workflow-documenter", "Document government workflows in plain functional language with triggers, roles, systems, steps, decisions, exceptions, outputs, pain points, and completion criteria.", ["Extract triggers, roles, systems, inputs, steps, decisions, exceptions, outputs, and completion conditions from source material.", "Normalize inconsistent terminology and identify contradictions or missing handoffs.", "Produce an ordered workflow with decision points, variations, pain points, clarifications, and process-owner validation needs."], ["Never invent missing process steps or assign unverified responsibilities.", "Do not describe backend logic or engineering implementation.", "Flag contradictory source descriptions instead of silently resolving them."]),
    ("AA-SKL-000196", "Government Use Case and User Story Builder", "government-use-case-user-story-builder", "Convert government process and system needs into functional use cases and user stories with actors, triggers, preconditions, flows, exceptions, outcomes, and acceptance context.", ["Identify actor roles, goal, trigger, preconditions, normal flow, alternate paths, exceptions, and desired outcome.", "Create use cases and user stories that stay role-based and trace to supplied business or functional requirements.", "Add acceptance context and clarifications without introducing technical solution design."], ["Do not invent actor permissions, system capabilities, exceptions, or policy rules.", "Avoid personal names when role-based documentation is appropriate.", "Do not turn user stories into technical implementation tasks unless the user explicitly provides approved technical content."]),
    ("AA-SKL-000197", "Government Functional SOP and User Guide Builder", "government-functional-sop-user-guide-builder", "Create functional SOPs and user guides for government operations using verified steps, roles, prerequisites, decision points, completion criteria, references, and review boundaries.", ["Determine whether the requested output is an SOP, user guide, job aid, or training-oriented procedure.", "Extract verified prerequisites, roles, inputs, sequential steps, decisions, exceptions, outputs, and references.", "Produce the correct functional document with clarifications needed and process-owner review language."], ["Do not invent missing steps, system behavior, permissions, or approvals.", "Do not provide technical troubleshooting, engineering, security, or configuration guidance unless explicitly authorized and within scope.", "Preserve exact policy wording when supplied rather than paraphrasing it into new obligations."]),
    ("AA-SKL-000198", "Government UAT Script and Acceptance Criteria Builder", "government-uat-script-acceptance-criteria-builder", "Create functional user acceptance testing scripts, scenarios, test data needs, expected outcomes, traceability, and issue logging structures from approved requirements.", ["Identify the approved requirement or workflow being validated, user role, prerequisites, test conditions, and expected business outcome.", "Build numbered UAT scenarios with steps, expected results, pass/fail criteria, evidence fields, and traceability references.", "Separate UAT acceptance from technical QA and record unresolved testability gaps."], ["Do not invent system behavior or mark tests passed without execution evidence.", "Do not create penetration, security, performance-engineering, or backend test procedures under this functional skill.", "Require agency acceptance authority to approve final UAT results."]),
    ("AA-SKL-000199", "Government Data Element and Role Access Inventory Builder", "government-data-element-role-access-inventory-builder", "Document administrative data elements and role-based access needs at a functional level without designing databases, identity systems, or security architecture.", ["Collect data element names, business definitions, source/use context, required/optional status, role needs, and retention or sensitivity notes supplied by authorized sources.", "Create a functional inventory and role-access matrix showing who needs to view, create, update, approve, or receive each item.", "Flag unknown ownership, sensitivity, source, or access rules for agency validation."], ["Do not design schemas, permissions infrastructure, authentication, encryption, or security controls.", "Do not infer protected-data classifications or access rights.", "Minimize sensitive data and avoid reproducing personal data unnecessarily."]),
    ("AA-SKL-000200", "Government Functional Integration Readiness Documenter", "government-functional-integration-readiness-documenter", "Assess and document functional integration readiness through business interactions, information exchanges, ownership, dependencies, constraints, and unresolved decisions without producing technical integration design.", ["Identify systems or business functions involved, intended information exchange, owners, triggers, business dependencies, constraints, and desired outcomes.", "Document functional touchpoints, readiness conditions, risks, gaps, and questions requiring technical-owner validation.", "Return a readiness summary that clearly separates functional needs from engineering implementation."], ["Do not design APIs, middleware, network architecture, data mappings, or security controls.", "Do not claim technical compatibility or integration feasibility without authorized technical evidence.", "Escalate engineering questions rather than solving them inside functional documentation."]),
    ("AA-SKL-000201", "Government System Impact Assessment Builder", "government-system-impact-assessment-builder", "Build functional system or process impact assessments covering affected users, workflows, policies supplied by the agency, data handling, training, operations, dependencies, risks, and readiness actions.", ["Define the proposed change, affected functions, users, workflows, documents, training, data, dependencies, and known constraints.", "Assess operational impacts, risks, benefits, readiness gaps, transition considerations, and unresolved questions using supplied evidence.", "Return findings with owners, mitigations, validation needs, and process-owner review boundaries."], ["Do not make legal, cybersecurity, engineering, or compliance determinations outside supplied authority.", "Do not invent impact evidence or affected populations.", "Label confidence and distinguish confirmed impact from anticipated impact."]),
    ("AA-SKL-000202", "Government Modernization and Adoption Roadmap Builder", "government-modernization-adoption-roadmap-builder", "Create functional modernization and adoption roadmaps with phases, capabilities, process changes, training, governance, dependencies, milestones, readiness criteria, and decision gates.", ["Clarify current state, desired future state, business outcomes, affected processes, constraints, dependencies, and available evidence.", "Sequence functional modernization into realistic phases with adoption, communication, training, governance, and validation needs.", "Return a roadmap with milestones, owners, decision gates, risks, assumptions, and measures of readiness."], ["Do not prescribe technical architecture, vendor selection, cybersecurity configuration, or procurement decisions.", "Do not invent budget, schedule, approvals, or organizational capacity.", "Treat the roadmap as planning support, not authorization to implement."]),
    ("AA-SKL-000203", "Government Intake and Document Routing Builder", "government-intake-document-routing-builder", "Design functional intake forms and document-routing workflows for government administrative and system processes using validated fields, roles, decisions, handoffs, status points, and completion criteria.", ["Identify the intake purpose, submitter, required information, receiving role, routing decisions, approvals, handoffs, status tracking, and completion point.", "Create the intake structure and routing logic in plain functional language.", "Flag missing ownership, approval authority, required fields, and exception handling for validation."], ["Do not invent approval authority, retention policy, access rules, or required data.", "Avoid collecting unnecessary personal or sensitive information.", "Do not design workflow software or automation implementation under this skill."]),
    ("AA-SKL-000204", "Government Administrative Decision Matrix Builder", "government-administrative-decision-matrix-builder", "Create government administrative decision matrices that compare defined options against verified criteria, constraints, risks, dependencies, and evidence without replacing authorized decision makers.", ["Collect the decision to be made, authorized options, criteria, weights if supplied, constraints, evidence, risks, and decision owner.", "Build a transparent matrix and document scoring rationale, unknowns, sensitivity, and tradeoffs.", "Return findings as decision support with unresolved questions and required approvals."], ["Do not invent criteria weights, evidence, authority, or preferred outcomes.", "Do not present a calculated score as an official agency decision.", "Flag legal, policy, procurement, HR, or technical decisions that require qualified review."]),
    ("AA-SKL-000205", "Government Meeting and Action Record Builder", "government-meeting-action-record-builder", "Convert government meetings, interviews, and working sessions into neutral summaries, decisions, action items, owners, due dates, risks, open questions, and follow-up records.", ["Identify meeting purpose, participants by role, date, agenda, source notes, decisions, actions, risks, and unresolved items.", "Separate discussion from decisions and proposals from approved actions.", "Produce a concise meeting record with action ownership, due dates when supplied, dependencies, and follow-up needs."], ["Do not invent attendance, decisions, commitments, due dates, or approvals.", "Minimize sensitive or personal information.", "Do not characterize preliminary discussion as policy or final agency direction."]),
    ("AA-SKL-000206", "Government Audit Support Package Assembler", "government-audit-support-package-assembler", "Assemble government administrative audit-support packages from verified source evidence, findings, process documentation, logs, gaps, corrective actions, and supporting references.", ["Define audit-support scope, authority, period, evidence sources, process owners, and requested deliverables.", "Organize evidence, findings, gaps, risks, corrective actions, traceability, and appendices without changing source meaning.", "Return a review-ready package index and narrative with missing evidence and owner assignments."], ["Do not fabricate evidence, compliance status, corrective action completion, or audit conclusions.", "Protect sensitive, personnel, procurement, and security-related information.", "Do not represent an internal support package as an auditor's official finding."]),
    ("AA-SKL-000207", "Government Documentation QA Reviewer", "government-documentation-qa-reviewer", "Review government functional and administrative documents for template integrity, factual support, plain language, consistency, traceability, role accuracy, scope boundaries, missing information, and review readiness.", ["Identify document type, governing template, intended audience, source materials, and required closing or review statements.", "Check structure, numbering, terminology, traceability, sequencing, contradictions, unsupported statements, sensitive information, and prohibited technical or legal content.", "Return pass, conditional pass, or fail with exact corrections, unresolved questions, and review owners."], ["Never repair an unsupported fact by inventing one.", "Fail documents that cross functional boundaries into unauthorized engineering, legal interpretation, HR decisions, or compliance claims.", "Require designated agency process-owner review before treating outputs as operationally final."]),
]

MAPPING_UPDATES = {
    "AA-GPT-000034": {"required_add": ["AA-SKL-000193", "AA-SKL-000194", "AA-SKL-000195", "AA-SKL-000196", "AA-SKL-000197", "AA-SKL-000198", "AA-SKL-000199", "AA-SKL-000200", "AA-SKL-000201", "AA-SKL-000202", "AA-SKL-000203", "AA-SKL-000207"], "optional_add": []},
    "AA-GPT-000035": {"required_add": ["AA-SKL-000193", "AA-SKL-000194", "AA-SKL-000195", "AA-SKL-000196", "AA-SKL-000197", "AA-SKL-000198", "AA-SKL-000199", "AA-SKL-000201", "AA-SKL-000203", "AA-SKL-000207"], "optional_add": ["AA-SKL-000200", "AA-SKL-000202"]},
    "AA-GPT-000037": {"required_add": ["AA-SKL-000195", "AA-SKL-000197", "AA-SKL-000203", "AA-SKL-000204", "AA-SKL-000205", "AA-SKL-000206", "AA-SKL-000207"], "optional_add": ["AA-SKL-000201", "AA-SKL-000202"]},
}


def unique(items):
    return list(dict.fromkeys(items))


def skill_md(name, desc, procedure, guardrails):
    slug = name.lower().replace("&", "and").replace(",", "").replace(" ", "-")
    steps = "\n".join(f"{i}. {s}" for i, s in enumerate(procedure, 1))
    guards = "\n".join(f"- {g}" for g in guardrails)
    return f"---\nname: {slug}\ndescription: {desc}\n---\n\n# {name}\n\n## Procedure\n\n{steps}\n\n## Output Contract\n\nProvide document scope, verified source basis, required sections, assumptions, clarifications needed, the requested functional or administrative deliverable, review owners, and validation requirements.\n\n## Guardrails\n\n{guards}\n\n## Recovery\n\nIf source evidence, authority, role ownership, process steps, required fields, or template requirements are incomplete, preserve verified content, label the gap, and request only the minimum clarification or authorized review required to continue.\n"


def write_skills():
    for _, name, slug, desc, procedure, guards in SKILLS:
        d = SKILL_ROOT / slug
        d.mkdir(parents=True, exist_ok=True)
        (d / "SKILL.md").write_text(skill_md(name, desc, procedure, guards), encoding="utf-8")


def update_assets():
    data = json.loads(ASSETS.read_text(encoding="utf-8"))
    existing = {a["sku"] for a in data["assets"]}
    for sku, name, slug, *_ in SKILLS:
        if sku in existing:
            continue
        data["assets"].append({"sku": sku, "asset_id": f"government-documentation.{slug}.v1", "name": name, "asset_type": "SKL", "business": "AA", "library": "GOVDOC", "version": "1.0.0", "status": "testing", "maturity": 2, "path": f"libraries/ai-authoritech/skills/government-documentation/{slug}", "depends_on": []})
    ASSETS.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def update_decisions():
    data = json.loads(DECISIONS.read_text(encoding="utf-8"))
    by_id = {d["gpt_id"]: d for d in data["decisions"]}
    for gid, upd in MAPPING_UPDATES.items():
        d = by_id[gid]
        d["decision"] = "verified"
        d["required_skills"] = unique(d.get("required_skills", []) + upd["required_add"])
        d["optional_skills"] = unique(d.get("optional_skills", []) + upd["optional_add"])
        d.pop("gap", None)
    data["updated_at"] = "2026-08-09"
    DECISIONS.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def update_mappings():
    data = json.loads(MAPPINGS.read_text(encoding="utf-8"))
    by_id = {m["gpt_id"]: m for m in data["mappings"]}
    decisions = {d["gpt_id"]: d for d in json.loads(DECISIONS.read_text(encoding="utf-8"))["decisions"]}
    for gid in MAPPING_UPDATES:
        d = decisions[gid]
        m = by_id.get(gid)
        if m is None:
            m = {"gpt_id": gid, "gpt_name": d["name"]}
            data["mappings"].append(m)
        m.update({"gpt_name": d["name"], "verification_status": "verified", "evidence": "Verified against the captured Builder configuration and the governed Government Documentation skill family.", "required_skills": d["required_skills"], "optional_skills": d["optional_skills"], "default_enhancements": [VISUAL]})
    data["updated_at"] = "2026-08-09"
    MAPPINGS.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def update_manifests():
    decisions = {d["gpt_id"]: d for d in json.loads(DECISIONS.read_text(encoding="utf-8"))["decisions"]}
    targets, seen = set(MAPPING_UPDATES), set()
    for path in MANIFEST_ROOT.glob("*/manifest.json"):
        data = json.loads(path.read_text(encoding="utf-8"))
        gid = data.get("gpt_id")
        if gid not in targets:
            continue
        d = decisions[gid]
        data.setdefault("skills", {})["required"] = d["required_skills"]
        data["skills"]["optional"] = d["optional_skills"]
        data["skills"].setdefault("default_enhancements", [VISUAL])
        note = "1.0.0 - Reconciled against reusable Government Documentation skills."
        if note not in data.setdefault("change_log", []):
            data["change_log"].append(note)
        path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
        seen.add(gid)
    if targets - seen:
        raise RuntimeError(f"Missing GPT manifests: {sorted(targets-seen)}")


def main():
    write_skills(); update_assets(); update_decisions(); update_mappings(); update_manifests()
    print(json.dumps({"skills_created": len(SKILLS), "gpts_reconciled": len(MAPPING_UPDATES)}, indent=2))


if __name__ == "__main__":
    main()

---
name: knowledge-governance-manager
description: Establish and operate knowledge governance for ownership, stewardship, authority, access, privacy, licensing, consent, retention, deletion, lifecycle, quality gates, change control, incidents, and auditability across knowledge bases, graphs, search, and RAG systems. Use when defining policies, roles, controls, approvals, or governance reviews. Do not substitute policy text for technical enforcement or legal review. Use when asked to (1) manage knowledge governance, (2) review knowledge governance, (3) resolve issues in knowledge governance, or (4) improve knowledge governance.
---

# Knowledge Governance Manager

Use the [knowledge governance standard](references/knowledge-governance-standard.md) to evaluate authority, accountability, lifecycle, and control coverage. Record the result in the [knowledge governance plan template](assets/knowledge-governance-plan-template.md).

## Procedure

1. Define business purpose, jurisdictions, stakeholders, systems, data classes, risk, and binding obligations.
2. Assign accountable owners, stewards, custodians, approvers, privacy and security roles, and escalation paths.
3. Establish authoritative sources, permitted uses, licenses, consent, access, sharing, localization, and tenant boundaries.
4. Define lifecycle states and gates for intake, extraction, review, approval, publication, refresh, deprecation, and deletion.
5. Specify technical enforcement, audit events, retention, legal holds, deletion propagation, backups, and restoration.
6. Govern taxonomies, ontologies, embeddings, indexes, caches, prompts, models, and downstream derived knowledge.
7. Define quality, provenance, freshness, incident, exception, vendor, and change-control requirements.
8. Test controls with unauthorized access, deletion, stale data, conflicting authority, and incident exercises.
9. Deliver policy-to-control matrix, RACI, lifecycle, evidence, gaps, exceptions, owners, and review cadence.

## Guardrails

- Do not claim compliance from documentation without implemented and tested controls.
- Do not retain data merely because deletion is technically inconvenient.
- Do not assign accountability to an AI system.
- Do not expand use, audience, or retention beyond source rights and authorization.

## Recovery

If ownership, authority, access, retention, or lifecycle obligations conflict, stop promotion of the affected knowledge. Preserve the last verified authoritative record, document the conflict and impacted consumers, and assign a named human steward to approve remediation before use resumes.

## Output Contract

Deliver a completed governance plan containing scope, authority register, RACI, policy-to-control matrix, lifecycle gates, access and retention requirements, exceptions, evidence, accountable owners, review cadence, and approval status. Mark unverified controls and unresolved decisions explicitly.

---
name: app-requirements-generator
description: Convert product ideas, discovery notes, workflows, stakeholder interviews, or existing-system evidence into testable application requirements, user stories, business rules, data and permission requirements, interface states, integrations, nonfunctional requirements, edge cases, acceptance criteria, traceability, dependencies, assumptions, and a prioritized release backlog. Use for websites, SaaS products, portals, dashboards, internal tools, mobile or desktop apps, and AI-enabled products - not solution architecture, UI design, implementation, or inventing material requirements without stakeholder validation.
---

# App Requirements Generator

Write requirements that describe observable value and behavior without prematurely
dictating implementation.

## Procedure

1. Identify the product outcome, users, buyers, operators, owners, current process,
   pain points, constraints, success measures, risk, and decision authority.
2. Inventory evidence and classify statements as confirmed, inferred, assumed,
   proposed, disputed, or unknown. Preserve disagreements and source attribution.
3. Define scope boundaries, actors, system context, external systems, business
   events, release goal, and explicit non-goals.
4. Map each actor's jobs and journeys, including triggers, preconditions, main path,
   alternate paths, failures, recovery, completion, and support needs.
5. Write uniquely identified functional requirements and user stories using
   [references/app-requirements-standard.md](references/app-requirements-standard.md).
6. Define business rules separately from screen behavior. Record rule owner,
   source, priority, exceptions, effective dates, and conflict resolution.
7. Define data entities, source of truth, ownership, validation, relationships,
   sensitivity, tenancy, retention, deletion, audit, import, export, and migration.
8. Define authentication, roles, resource-level authorization, approvals,
   administrative actions, session and recovery behavior, and prohibited access.
9. Define integrations by trigger, direction, contract, mapping, authority,
   frequency, latency, volume, idempotency, failure, reconciliation, and ownership.
10. Specify loading, empty, success, error, denied, partial, offline, retry,
    cancellation, timeout, and responsive states for each user-facing capability.
11. Define measurable nonfunctional requirements for accessibility, security,
    privacy, performance, reliability, scalability, compatibility, localization,
    observability, maintainability, portability, support, and cost.
12. Write scenario-based acceptance criteria covering normal, boundary, invalid,
    unauthorized, conflicting, duplicate, interrupted, and recovery behavior.
13. Trace requirements to evidence, outcomes, risks, dependencies, acceptance tests,
    and release scope. Prioritize by value, necessity, risk reduction, learning,
    effort, dependency, and delay cost.
14. Review for ambiguity, duplication, conflict, missing states, unverifiable words,
    hidden assumptions, solution bias, and orphaned requirements.
15. Deliver with
    [assets/app-requirements-specification-template.md](assets/app-requirements-specification-template.md).

## Guardrails

- Do not treat stakeholder preference as a verified user need or business rule.
- Do not use vague terms such as fast, intuitive, secure, scalable, or seamless
  without a measurable condition.
- Do not combine multiple independently testable behaviors in one requirement.
- Do not hide permissions or business logic only in UI requirements.
- Do not prescribe a technology unless it is an approved constraint.
- Do not silently resolve conflicting requirements; identify the decision owner.
- Do not mark an assumption as approved scope.
- Keep future ideas outside the committed release backlog.

## Output Contract

Provide the evidence inventory, product and system context, scope, actor and journey
maps, functional and nonfunctional requirements, business rules, data and
authorization requirements, integrations, state and edge-case matrix, acceptance
criteria, traceability, prioritized backlog, assumptions, conflicts, and open
decisions.

## Recovery

If evidence conflicts, retain each source, mark affected requirements disputed,
and identify the decision owner. If a requirement cannot be observed or tested,
rewrite it or return it as unresolved. Keep assumptions outside committed scope
until an accountable stakeholder validates them.

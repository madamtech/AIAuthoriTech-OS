---
name: prompt-to-app-converter
description: Convert an informal app request, product concept, copied prompt, notes, or prototype description into a traceable, platform-neutral app build packet with clarified outcomes, evidence, assumptions, scope, user journeys, requirements, data, access, interfaces, architecture constraints, vertical slices, bounded coding prompts, acceptance tests, verification gates, and change controls. Use before giving an idea to Lovable, Bolt, Replit, v0, Firebase Studio, Cursor, Windsurf, Claude Code, Codex, or another AI coding system - not to infer material business rules, credentials, production authority, or guaranteed feasibility from a vague prompt. Use when asked to (1) create prompt to app converter, (2) review prompt to app converter, (3) improve prompt to app converter, or (4) standardize prompt to app converter.
---

# Prompt-to-App Converter

Turn conversational intent into small, testable implementation contracts.

## Procedure

1. Preserve the source prompt verbatim. Record its origin, author, date, referenced
   artifacts, intended platform, and any prior decisions so later changes remain
   traceable.
2. Extract actors, jobs, outcomes, pain points, capabilities, data, integrations,
   devices, brand direction, constraints, risks, quality expectations, and success
   signals. Classify each statement as confirmed, inferred, assumed, proposed,
   conflicting, or unknown.
3. Decide whether the request describes an app, website, automation, agent,
   workflow, prototype, or combination. Route specialist work to the relevant
   planner instead of stretching one build prompt across unlike assets.
4. Identify the smallest set of questions whose answers materially affect scope,
   security, data, architecture, cost, or acceptance. Continue with labeled
   assumptions when uncertainty is reversible; stop at a decision gate when it is
   not.
5. Define the product outcome, users, current process, measurable success,
   business owner, operational owner, boundaries, dependencies, risks, and
   explicit non-goals.
6. Convert requested capabilities into uniquely identified requirements,
   business rules, user stories, state behavior, edge cases, and scenario-based
   acceptance criteria. Use existing approved requirements rather than rewriting
   them.
7. Map navigation and end-to-end journeys for first use, routine work,
   administration, errors, denied access, empty state, interruption, retry,
   recovery, cancellation, and verified completion.
8. Define entities, relationships, source of truth, validation, sensitivity,
   tenant and user ownership, lifecycle, retention, deletion, import, export,
   audit, backup, migration, and realistic synthetic fixtures.
9. Define authentication, roles, resource-level authorization, service identities,
   approvals, privileged actions, recovery, session behavior, and prohibited
   access. Never treat hidden UI as authorization.
10. Define integrations by trigger, direction, contract, authority, mapping,
    idempotency, latency, rate, timeout, retry, reconciliation, failure ownership,
    sandbox, and test-double needs.
11. Define measurable accessibility, security, privacy, performance, reliability,
    compatibility, localization, observability, portability, support, cost, and
    maintenance conditions.
12. Choose platform-neutral architecture boundaries before tool syntax. Record
    frontend, backend, data, storage, jobs, events, AI behavior, environments,
    configuration, secrets, deployment, rollback, monitoring, and adapter
    boundaries.
13. Prioritize a walking skeleton and vertical slices using
    [references/prompt-to-app-standard.md](references/prompt-to-app-standard.md).
    Each slice must deliver one coherent path, minimize blast radius, and end with
    observable acceptance evidence.
14. Create one bounded build prompt per slice. Include objective, source
    requirements, files and components in scope, data and access contracts,
    states, constraints, protected decisions, prohibited changes, acceptance
    tests, commands, expected summary, and unresolved dependencies.
15. Define a checkpoint after each slice: inspect changed files, migrations,
    dependencies, secrets, generated data, UI states, accessibility, security,
    tests, build output, external effects, and regression evidence before
    continuing.
16. Maintain a decision and change ledger. When new work conflicts with approved
    scope, stop the affected slice, show the impact, identify the decision owner,
    update requirements and tests first, and then issue a revised prompt.
17. Create a platform adapter only after the canonical build packet. Keep vendor
    commands, hosting, components, and limitations separate so the core product
    contract remains portable.
18. Deliver with
    [assets/prompt-to-app-build-packet.md](assets/prompt-to-app-build-packet.md).

## Guardrails

- Do not treat the original prompt as complete or approved requirements.
- Do not invent users, business rules, permissions, integrations, pricing, legal
  claims, or sensitive-data handling without labeling and validation.
- Do not place credentials, personal data, production records, or signing material
  in build prompts, fixtures, screenshots, or source code.
- Do not generate one unbounded prompt that authorizes architecture, database,
  authentication, design, deployment, and production changes at once.
- Do not let later slices silently modify protected features, branding, schema,
  access rules, or accepted behavior.
- Do not accept visual similarity as proof that data, authorization, integrations,
  accessibility, or external effects work.
- Do not execute destructive migrations or production actions without explicit
  authorization, recovery controls, and authoritative verification.
- Do not claim feasibility, completion, security, or production readiness without
  evidence proportionate to that claim.

## Recovery

If material scope, business rules, access, data, integrations, or protected
decisions remain contradictory, stop the affected slice and preserve the source
prompt plus decision history. Separate reversible assumptions from approval
gates, update canonical requirements and tests first, and issue a revised bounded
prompt rather than silently changing prior behavior.

## Output Contract

Provide the preserved source prompt, evidence and assumption inventory,
classification and routing, clarification gates, product brief, scope and
non-goals, requirements and traceability, journeys and states, data and access
models, integrations, quality requirements, architecture boundaries, prioritized
vertical slices, bounded build prompts, verification gates, decision and change
ledger, platform adapter, risks, and open decisions.

---
name: skill-router
description: Select the smallest sufficient route for a request from registered skills, workflows, knowledge packs, tools, direct response, skill creation, skill review, human escalation, or unsupported outcomes. Use when capability selection is ambiguous, several assets may apply, a workflow may be required, or duplicate skill creation must be prevented. Do not use merely to execute an already unambiguous selected skill. Use when asked to (1) create skill router, (2) review skill router, (3) improve skill router, or (4) standardize skill router.
---

# Skill Router

Choose capabilities; do not perform their work.

## Procedure

1. Parse the requested outcome, deliverable, audience, domain, business, constraints, sensitivity, required tools, authorization, and action level.
2. Read [references/routing-standard.md](references/routing-standard.md) and search the catalog descriptions, inputs, outputs, dependencies, maturity, availability, and relationship graph.
3. Remove candidates that cannot produce the outcome, lack required access, conflict with the business context, or are not available at the required maturity.
4. Classify the route as `direct_response`, `single_skill`, `multi_skill_sequence`, `workflow`, `knowledge_lookup`, `tool_action`, `skill_creation`, `skill_review`, `human_escalation`, or `unsupported`.
5. Score each viable candidate: outcome fit 35, input/output fit 20, domain fit 15, access and authorization 15, dependency readiness 10, duplication avoidance 5.
6. Apply tie-breakers in order: exact output match, higher supported maturity, fewer dependencies, lower action risk, and narrower scope.
7. Use one skill for one cohesive job; a sequence for independent jobs; and a workflow for shared state, branches, approval, retry, recovery, or multi-party handoffs.
8. Calculate confidence from supported evidence. Ask one focused question only when the answer would change the selected route materially.
9. Return the primary route, confidence, rationale, required inputs, dependencies, authorization needs, fallback, rejected alternatives, and unresolved assumptions.

## Confidence Rules

- 90-100: route automatically when authority is sufficient.
- 75-89: route and state material assumptions.
- 60-74: label provisional; ask one material question or provide a safe partial route.
- Below 60: do not auto-route; escalate, recommend creation/review, or mark unsupported.

## Output Contract

Use [assets/routing-decision-template.json](assets/routing-decision-template.json). Keep catalog SKUs and asset IDs exact. A route may recommend but must not claim execution.

## Guardrails

- Never route to an unavailable, deprecated, inaccessible, or nonexistent capability.
- Never treat account connection as authorization for a consequential external action.
- Never create a new skill before searching for revision, merge, or workflow alternatives.
- Keep business-specific assets isolated unless cross-business use is explicitly allowed.

## Recovery

If the catalog is missing or stale, state that confidence is limited and use only capabilities verified from the filesystem. If no safe route exists, return `unsupported` or `human_escalation` with the missing capability or authority.

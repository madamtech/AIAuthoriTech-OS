---
name: workflow-documentation-builder
description: Create controlled, audience-appropriate workflow documentation from validated specifications, including purpose, scope, roles, steps, decisions, data, systems, controls, exceptions, metrics, runbooks, diagrams, tests, ownership, and version history. Use for operational handoff, training, audit, implementation, and support. Do not document assumptions as approved reality. Use when asked to (1) build workflow documentation, (2) refine workflow documentation, (3) validate workflow documentation, or (4) standardize workflow documentation.
---

# Workflow Documentation Builder

Use the [workflow documentation standard](references/workflow-documentation-standard.md) and produce the controlled package with the [workflow documentation template](assets/workflow-documentation-template.md).

## Procedure

1. Confirm exact workflow version, validation status, audiences, purpose, access, owner, and source evidence.
2. Separate policy, procedure, implementation, runbook, training, and quick-reference content by authority.
3. Document trigger, preconditions, steps, decisions, roles, inputs, outputs, systems, controls, and completion.
4. Include exceptions, escalations, recovery, approvals, metrics, service levels, and authoritative verification.
5. Produce consistent process, swimlane, state, or sequence diagrams aligned with the written specification.
6. Link source requirements and controlled artifacts; redact secrets and unnecessary sensitive data.
7. Validate with operators, owners, control functions, and representative scenarios.
8. Assign version, effective date, review cadence, change history, distribution, and obsolete-copy handling.

## Guardrails
- Do not let documentation become a second conflicting source of truth.
- Do not publish unvalidated future-state steps as current procedure.
- Do not omit difficult exceptions merely to keep documentation simple.
- Do not include live credentials or protected production examples.

## Recovery

If source authority, version, validation status, or diagram-to-text consistency is uncertain, stop publication and retain the last approved documentation. Mark the draft clearly, reconcile against controlled sources, and replace obsolete copies only after owner approval.

## Output Contract

Deliver audience-appropriate controlled documentation containing purpose, scope, roles, procedure, decisions, systems, controls, exceptions, recovery, metrics, diagrams, tests, ownership, effective date, review cadence, history, distribution, and status.

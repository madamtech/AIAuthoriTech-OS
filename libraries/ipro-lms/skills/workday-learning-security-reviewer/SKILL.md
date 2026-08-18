---
name: workday-learning-security-reviewer
description: Review Workday Learning security roles, domains, business-process access, audience visibility, administration, reporting, and segregation of duties. Use when validating least privilege or assessing a proposed learning configuration change. Use when asked to (1) review workday learning security, (2) audit workday learning security, (3) identify gaps in workday learning security, or (4) recommend corrections to workday learning security.
---

# Workday Learning Security Reviewer

Use the [operating standard](references/learning-security-standard.md) and [working template](assets/security-review-template.md).

Evaluate security using approved tenant evidence and representative user tests.

## Procedure

1. Define scope, environments, users, roles, learning processes, data classifications, and expected access.
2. Inventory security groups, domain permissions, business-process policies, administrative roles, integrations, and reporting access.
3. Map each job responsibility to minimum required view, initiate, approve, correct, and report permissions.
4. Identify broad grants, inherited access, conflicting duties, sensitive-data exposure, and orphaned administration.
5. Test permitted and prohibited actions with representative personas.
6. Classify findings, propose least-privilege remediation, assess operational impact, and define retesting.

## Output Contract

Provide a scope statement, role-to-permission matrix, persona test results, findings by severity, segregation-of-duties analysis, remediation plan, approval needs, and residual risks.

## Guardrails

- Never request or display credentials.
- Do not remove access without impact analysis and authorization.
- Treat screenshots and exports as sensitive.
- Distinguish observed tenant evidence from assumptions.

## Recovery

If role authority, domain access, population scope, segregation of duties, worker-data exposure, tenant evidence, or remediation approval is unresolved, do not grant or revoke access. Preserve evidence and escalate to authorized Workday security owners.

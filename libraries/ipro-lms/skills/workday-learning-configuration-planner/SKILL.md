---
name: workday-learning-configuration-planner
description: Plan governed Workday Learning configurations for content, campaigns, audiences, enrollment, completion, security, notifications, and reporting. Use when translating approved learning requirements into configuration specifications, test cases, and deployment controls.
---

# Workday Learning Configuration Planner

Create a configuration-ready design without claiming unverified tenant features or making unauthorized changes.

## Workflow

1. Confirm the business requirement, learner population, owner, tenant/environment, security roles, integrations, and release constraints.
2. Inventory required learning content, offerings, lessons, campaigns, audiences, prerequisites, equivalencies, and completion evidence.
3. Map each requirement to a Workday configuration element or record it as a manual control, integration need, or product gap.
4. Define enrollment, due-date, completion, expiration, notification, visibility, and reporting behavior.
5. Identify effective-dating, localization, security, data-retention, and downstream impacts.
6. Prepare positive, negative, boundary, role-security, reporting, and regression tests.
7. Specify approvals, migration order, production promotion, monitoring, and rollback.

## Output

Provide a requirements matrix, object/configuration inventory, security and audience rules, integration impacts, test plan, deployment checklist, rollback plan, open decisions, and validation status.

## Guardrails

- Verify tenant-specific capabilities before recommending configuration.
- Separate approved policy from implementation choices.
- Do not expose worker data or production credentials.
- Do not execute tenant changes without explicit authorization.


---
name: netexam-certification-builder
description: Translate an approved certification design into a controlled NetExam build specification with objects, settings, dependencies, branches, notifications, reporting, and test evidence. Use for NetExam implementation planning and QA, not for inventing certification policy.
---

# NetExam Certification Builder

Create a traceable configuration plan before making production changes.

## Workflow

1. Confirm the approved program rules, audience, owners, environments, integrations, and release date.
2. Inventory required NetExam objects: courses, exams, certifications, curricula, prerequisites, groups, branches, certificates, and notifications.
3. Map every business rule to a configuration field or identify it as a manual control or gap.
4. Define enrollment, completion, scoring, attempts, expiration, renewal, visibility, and reporting behavior.
5. Plan build order, migration, test users, rollback, approvals, and production promotion.
6. Create positive, negative, boundary, renewal, reporting, and integration test cases.

## Output

Provide an object inventory, configuration matrix, dependency order, audience/branch rules, notification plan, reporting map, test plan, release checklist, rollback plan, and unresolved gaps.

## Guardrails

- Do not claim a NetExam feature exists without verified documentation or environment evidence.
- Do not perform production configuration unless explicitly authorized.
- Preserve approved certification policy; escalate platform conflicts.
- Avoid exposing learner data or secrets in examples and tests.


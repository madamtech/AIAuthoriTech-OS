---
name: netexam-certification-builder
description: Translate approved certification policy into a controlled NetExam build specification covering objects, settings, dependencies, branches, audiences, notifications, certificates, reporting, integrations, release controls, rollback, and test evidence. Use for authorized NetExam planning or QA. Do not invent policy, assume unsupported features, or change production without approval. Use when asked to (1) build netexam certification, (2) refine netexam certification, (3) validate netexam certification, or (4) standardize netexam certification.
---

# NetExam Certification Builder

Use the [NetExam build standard](references/netexam-build-standard.md) and [NetExam build workbook template](assets/netexam-build-workbook-template.md).

## Procedure

1. Confirm the approved program rules, audience, owners, environments, integrations, and release date.
2. Inventory required NetExam objects: courses, exams, certifications, curricula, prerequisites, groups, branches, certificates, and notifications.
3. Map every business rule to a configuration field or identify it as a manual control or gap.
4. Define enrollment, completion, scoring, attempts, expiration, renewal, visibility, and reporting behavior.
5. Plan build order, migration, test users, rollback, approvals, and production promotion.
6. Create positive, negative, boundary, renewal, reporting, and integration test cases.

## Output Contract

Provide an object inventory, configuration matrix, dependency order, audience/branch rules, notification plan, reporting map, test plan, release checklist, rollback plan, and unresolved gaps.

## Guardrails

- Do not claim a NetExam feature exists without verified documentation or environment evidence.
- Do not perform production configuration unless explicitly authorized.
- Preserve approved certification policy; escalate platform conflicts.
- Avoid exposing learner data or secrets in examples and tests.

## Recovery

If policy, environment evidence, object dependencies, integration ownership, test access, rollback, or production authorization is missing, stop the affected build stage. Record the configuration gap and provide a safe test-environment plan rather than guessing at NetExam behavior.

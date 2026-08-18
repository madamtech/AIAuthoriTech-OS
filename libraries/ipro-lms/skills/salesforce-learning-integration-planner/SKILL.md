---
name: salesforce-learning-integration-planner
description: Plan Salesforce-to-LMS learning integrations by defining system ownership, identities, objects, field mappings, events, transformations, security, reconciliation, errors, and monitoring. Use for NetExam, Workday Learning, or other learning data exchanges involving Salesforce. Use when asked to (1) plan salesforce learning integration, (2) revise salesforce learning integration, (3) evaluate options for salesforce learning integration, or (4) prepare implementation of salesforce learning integration.
---

# Salesforce Learning Integration Planner

Use the [operating standard](references/learning-integration-standard.md) and [working template](assets/salesforce-integration-template.md).

Design an auditable integration contract before implementation.

## Procedure

1. Define the business outcome, source and target systems, integration direction, frequency, environments, owners, and service levels.
2. Identify learner, account, contact, product, enrollment, course, completion, score, certification, and status objects in scope.
3. Establish authoritative ownership for each field and the cross-system identity strategy.
4. Specify field mappings, transformations, defaults, validation, effective dates, deletes, and historical behavior.
5. Define authentication, least privilege, encryption, consent, retention, and logging.
6. Design idempotency, pagination, ordering, retries, dead-letter handling, alerting, replay, and reconciliation.
7. Create normal, duplicate, missing, late, invalid, revoked-access, partial-failure, and volume tests.
8. Plan cutover, backfill, rollback, monitoring, and support ownership.

## Output Contract

Provide a context diagram, system-of-record matrix, object/field mapping, event contract, security controls, error strategy, reconciliation plan, test matrix, deployment plan, and open decisions.

## Guardrails

- Do not assume similarly named fields have identical semantics.
- Never place credentials or personal data in documentation.
- Preserve source history and prevent duplicate side effects.
- Require security and data-owner approval before production.

## Recovery

If source ownership, identity keys, field mappings, consent, security, error handling, reconciliation, rollback, or production authority is unresolved, stop the affected data flow. Preserve trace evidence and route the decision to system owners.

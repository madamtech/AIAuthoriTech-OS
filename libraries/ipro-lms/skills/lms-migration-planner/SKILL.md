---
name: lms-migration-planner
description: Plan controlled migrations of LMS users, content, enrollments, completions, transcripts, certifications, structures, and integrations. Use when moving between learning platforms, consolidating tenants, or performing major learning-data conversions.
---

# LMS Migration Planner

Use the [operating standard](references/migration-control-standard.md) and [working template](assets/migration-plan-template.md).

Design a traceable migration that prioritizes learning-record integrity and business continuity.

## Procedure

1. Define scope, source and target systems, cutover model, owners, compliance needs, retention, downtime, and success criteria.
2. Inventory objects, volumes, versions, dependencies, identifiers, data quality, integrations, and historical requirements.
3. Establish source-to-target mappings, transformations, defaults, exclusions, and reconciliation tolerances.
4. Define content packaging, transcript and certification handling, identity matching, security, and archival strategy.
5. Plan mock migrations, sampling, exception handling, performance tests, user acceptance, and sign-offs.
6. Design freeze, delta migration, cutover, communications, rollback, hypercare, and decommissioning.
7. Reconcile counts and critical records at every stage.

## Output Contract

Provide a migration charter, inventory, mapping workbook specification, dependency plan, data-quality backlog, test cycles, reconciliation controls, cutover runbook, rollback plan, and acceptance criteria.

## Guardrails

- Never discard historical records without approved retention decisions.
- Preserve immutable source extracts and audit evidence.
- Protect personal data during transfer and testing.
- Do not promise lossless migration where target capabilities differ.

## Recovery

If source authority, target mapping, retention, identity, history, content compatibility, reconciliation, cutover, rollback, or approval is unresolved, stop the affected migration wave. Preserve source evidence and document accepted transformation or loss.

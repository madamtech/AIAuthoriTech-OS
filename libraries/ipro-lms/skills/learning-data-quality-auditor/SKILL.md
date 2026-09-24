---
name: learning-data-quality-auditor
description: Audit learning data for completeness, validity, uniqueness, consistency, timeliness, lineage, and reconciliation across LMS, HR, CRM, content, and reporting systems. Use when learning records or analytics cannot be trusted or before migration and integration changes. Use when asked to (1) create learning data quality auditor, (2) review learning data quality auditor, (3) improve learning data quality auditor, or (4) standardize learning data quality auditor.
---

# Learning Data Quality Auditor

Use the [operating standard](references/learning-data-quality-standard.md) and [working template](assets/data-quality-audit-template.md).

Measure data defects against explicit rules and trace them to actionable causes.

## Procedure

1. Define business-critical datasets, owners, systems, time period, populations, privacy limits, and acceptance thresholds.
2. Create a field-level data dictionary and authoritative-source matrix.
3. Define quality rules for identifiers, required values, domains, dates, status transitions, relationships, uniqueness, and freshness.
4. Profile records and quantify defects without exposing unnecessary personal data.
5. Reconcile totals and representative records across systems.
6. Trace defects to source entry, configuration, mapping, timing, identity, content runtime, or manual correction.
7. Prioritize remediation, prevention, ownership, monitoring, and retesting.

## Output Contract

Provide a scope and rule catalog, profiling results, exception register, reconciliation summary, root-cause analysis, risk-ranked remediation plan, monitoring controls, and residual limitations.

## Guardrails

- Do not modify source data during diagnosis.
- Distinguish null, zero, not applicable, and unavailable.
- Use least-privilege access and masked samples.
- Preserve reproducible query, filter, and snapshot details.

## Recovery

If source ownership, field definitions, lineage, population, grain, security, reconciliation, or correction authority is unresolved, preserve the snapshot and label findings provisional. Do not correct authoritative records without approval and an audit trail.

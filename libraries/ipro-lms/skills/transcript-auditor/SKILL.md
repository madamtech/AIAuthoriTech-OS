---
name: transcript-auditor
description: Audit learner transcript records across authorized LMS and connected systems for identity, course and version, enrollment, attempts, status, dates, timezone, scores, credits, certificates, integrations, overrides, and source consistency. Use when records are disputed, missing, duplicated, stale, or migration-affected. Do not alter official records without approval, evidence preservation, and an audit trail.
---

# Transcript Auditor

Use the [transcript audit standard](references/transcript-audit-standard.md) and [transcript exception template](assets/transcript-exception-template.md).

## Procedure

1. Define the learner population, disputed records, systems, date range, business rules, and authorized data access.
2. Normalize learner identifiers, course IDs, versions, status vocabulary, timestamps, timezones, and source-system keys.
3. Compare enrollment, launch, attempt, completion, score, credit, certificate, and transcript records.
4. Detect duplicates, orphaned records, version mismatches, late integrations, manual overrides, and retroactive changes.
5. Classify root cause as source data, configuration, content/runtime, integration, identity, timing, or manual process.
6. Recommend correction, owner, approval, evidence retention, learner communication, and recurrence prevention.
7. Reconcile corrected records and record validation results.

## Output Contract

Provide audit scope, control rules, exception register, evidence trail, root-cause summary, correction plan, approval needs, reconciliation results, privacy notes, and closure status.

## Guardrails

- Use least-privilege access and redact personal data from deliverables.
- Do not alter official records without authorization and an audit trail.
- Preserve source evidence before correction.
- Label unresolved conflicts rather than choosing a convenient source.

## Recovery

If identity, source authority, record lineage, privacy authorization, correction ownership, or reconciliation evidence is unresolved, preserve the record and mark the exception open. Do not overwrite competing evidence; escalate through the approved data-correction process.

---
name: knowledge-quality-reviewer
description: Independently review knowledge assets and corpora for provenance, authority, accuracy, completeness, consistency, freshness, granularity, findability, access compliance, representativeness, usability, and evidence integrity. Use before publishing, indexing, RAG ingestion, migration, release, or maturity promotion. Do not edit evidence in place or approve unsupported quality claims. Use when asked to (1) review knowledge quality, (2) audit knowledge quality, (3) identify gaps in knowledge quality, or (4) recommend corrections to knowledge quality.
---

# Knowledge Quality Reviewer

Issue an independent verdict whose scope never exceeds inspected evidence.

## Procedure

1. Define review scope, consumers, risk, quality thresholds, exact versions, evidence cutoff, and independence.
2. Verify provenance, ownership, authority, licenses, consent, data classification, and immutable source references.
3. Trace representative records to sources and recalculate samples of quality metrics.
4. Assess accuracy, completeness, consistency, currency, duplicates, conflicts, granularity, metadata, and accessibility using [references/knowledge-quality-standard.md](references/knowledge-quality-standard.md).
5. Review extraction, taxonomy, ontology, retrieval, and RAG evidence where applicable.
6. Test sensitive-data controls, authorization, deletion, retention, citations, and untrusted-content handling.
7. Record evidence-linked defects with severity, affected scope, owner, remediation, and retest.
8. Apply hard gates before averages; critical provenance, privacy, access, fabrication, or deletion failures block approval.
9. Issue approve, approve with conditions, reject, or inconclusive limited to reviewed versions and populations.
10. Deliver findings and verdict with [assets/knowledge-quality-review-template.md](assets/knowledge-quality-review-template.md).

## Guardrails

- Do not equate volume, polish, popularity, or age with quality.
- Do not report excluded, inaccessible, stale, or unverified records as passing.
- Do not generalize a sample beyond its documented population and confidence.
- Do not close defects without corrected artifacts and fresh evidence.

## Recovery

If source identity, review independence, sample validity, access compliance, or
critical evidence cannot be verified, return reject or inconclusive for the
affected scope. Preserve reviewed artifacts, record evidence-linked defects and
retest boundaries, and do not edit source evidence to make it pass.

## Output Contract

Provide scope and independence, artifact manifest, sampling method, quality
results, source trace checks, access and deletion findings, defects and severity,
hard-gate outcomes, limitations, conditions, retest scope, and exact verdict.

---
name: knowledge-refresh-manager
description: Plan and control knowledge freshness through source monitoring, change detection, validity windows, risk-based refresh schedules, re-extraction, revalidation, reindexing, cache invalidation, consumer notification, and rollback. Use to prevent stale knowledge in bases, search, graphs, and RAG systems. Do not overwrite released knowledge without provenance, impact analysis, validation, and recovery. Use when asked to (1) manage knowledge refresh, (2) review knowledge refresh, (3) resolve issues in knowledge refresh, or (4) improve knowledge refresh.
---

# Knowledge Refresh Manager

Use the [knowledge refresh standard](references/knowledge-refresh-standard.md) to set risk-based freshness controls. Capture schedules, triggers, evidence, and rollback in the [knowledge refresh plan template](assets/knowledge-refresh-plan-template.md).

## Procedure

1. Inventory sources, owners, authority, update mechanisms, validity rules, consumers, dependencies, and risk.
2. Define freshness service levels by knowledge type, not one arbitrary schedule for the whole corpus.
3. Detect source additions, changes, removals, access shifts, expirations, and upstream version events.
4. Classify change impact and determine extraction, review, taxonomy, ontology, index, embedding, and consumer work.
5. Stage refreshes with immutable snapshots, diffs, validation, approval, cohort rollout, and rollback.
6. Propagate deletions and access changes urgently through indexes, caches, replicas, exports, and downstream systems.
7. Re-run affected quality, retrieval, RAG, citation, safety, and access tests before promotion.
8. Monitor lag, failures, stale answers, orphan records, refresh cost, and consumer version exposure.
9. Deliver source schedule, triggers, impact map, runbook, evidence, rollout, rollback, and stale-content register.

## Guardrails

- Do not equate a recent ingestion timestamp with current or authoritative knowledge.
- Do not refresh from a lower-authority source over a controlling source silently.
- Do not leave deleted or restricted content in embeddings, caches, or backups beyond policy.
- Do not hide refresh failures; mark affected knowledge and consumers explicitly.

## Recovery

If source authority, version, change impact, or deletion propagation cannot be verified, retain the last verified version and block promotion or reindexing of the affected content. Label exposed consumers, preserve the failed run evidence, and route the discrepancy to the source owner before retrying.

## Output Contract

Deliver a completed refresh plan containing source inventory, freshness tiers, triggers, impact rules, validation gates, consumer notifications, failure handling, rollout, rollback, stale-content register, owners, metrics, and approval status. Distinguish verified freshness from assumed freshness.

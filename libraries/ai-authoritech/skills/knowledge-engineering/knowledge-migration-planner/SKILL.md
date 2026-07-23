---
name: knowledge-migration-planner
description: Plan controlled migration of knowledge assets, metadata, taxonomies, ontologies, embeddings, indexes, permissions, provenance, versions, and consumers between repositories, platforms, schemas, or architectures. Use for knowledge-base consolidation, search or RAG replacement, vendor exit, replatforming, and schema evolution. Do not perform irreversible cutover without reconciliation, access validation, consumer testing, and rollback.
---

# Knowledge Migration Planner

Use the [knowledge migration standard](references/knowledge-migration-standard.md) to govern mapping, reconciliation, cutover, and recovery. Record the implementation plan in the [knowledge migration plan template](assets/knowledge-migration-plan-template.md).

## Procedure

1. Define source and target scope, business outcome, owners, consumers, downtime, retention, security, and acceptance.
2. Inventory content, versions, provenance, metadata, rights, permissions, taxonomies, ontologies, indexes, adapters, and dependencies.
3. Profile duplicates, conflicts, unsupported formats, orphan records, stale assets, inaccessible content, and legal holds.
4. Map source to target fields, identifiers, relationships, access, lifecycle, and semantics; document lossy transformations.
5. Choose rehost, transform, consolidate, re-extract, re-embed, reindex, archive, or exclude per asset class.
6. Build pilot waves and reconciliation rules for counts, hashes, samples, relationships, permissions, search, citations, and consumers.
7. Test privacy, authorization, deletion, retrieval, RAG, performance, failure recovery, and rollback in isolation.
8. Plan dual run, freeze or delta capture, cutover, communications, ownership transfer, and source retirement.
9. Verify target acceptance and audit evidence before decommissioning; retain restoration artifacts per policy.
10. Deliver inventory, mappings, waves, tests, reconciliation, cutover, rollback, risks, exceptions, and sign-offs.

## Guardrails

- Do not treat record counts alone as proof of semantic or permission equivalence.
- Do not create new embeddings from content the target is not authorized to retain.
- Do not discard provenance, identifiers, audit history, legal holds, or deletion obligations.
- Do not decommission the source until consumers and recovery are verified.

## Recovery

If counts, checksums, permissions, semantic mappings, redirects, or consumer reconciliation fail, pause cutover and preserve the source as authoritative. Revert the affected wave or continue dual run, document the variance, and require owner approval after successful revalidation before resuming.

## Output Contract

Deliver a completed migration plan containing inventories, mappings, exclusions, migration waves, reconciliation rules, access tests, consumer tests, cutover, communications, rollback, source-retirement gates, risks, exceptions, evidence, and sign-offs. Identify every lossy or unverified transformation.

---
name: knowledge-base-builder
description: Design governed, retrieval-ready knowledge bases for AI agents and applications by defining scope, source authority, ownership, permissions, provenance, taxonomy, metadata, content transformation, chunking, indexing, retrieval, citation, freshness, conflict resolution, evaluation, monitoring, and retirement. Use for RAG knowledge planning, agent knowledge packs, enterprise search collections, or migration from document dumps - not for agent instructions, unauthorized ingestion, or claiming source accuracy without validation.
---

# Knowledge Base Builder

Build a trustworthy retrieval system, not a folder of uploaded files.

## Procedure

1. Define supported users, questions, decisions, exclusions, risk, latency, citation,
   and freshness requirements.
2. Inventory candidate sources with owner, authority, status, audience, sensitivity,
   format, system of record, effective date, retention, and update mechanism.
3. Admit, remediate, quarantine, or reject sources using
   [references/knowledge-governance-standard.md](references/knowledge-governance-standard.md).
4. Define source hierarchy and conflict behavior. Preserve material disagreements
   rather than merging them into false consensus.
5. Define taxonomy, controlled vocabulary, entities, relationships, metadata, and
   stable source identifiers.
6. Plan extraction, normalization, structure preservation, deduplication, chunking,
   enrichment, versioning, and deletion propagation by content type.
7. Enforce source-level and chunk-level access before retrieval; never rely on the
   model to hide unauthorized content after retrieval.
8. Define query rewriting, filters, hybrid retrieval, reranking, context assembly,
   citation, abstention, and fallback behavior.
9. Build representative retrieval and answer-quality evaluations covering ordinary,
   ambiguous, conflicting, stale, unauthorized, missing, and adversarial content.
10. Define ingestion monitoring, freshness service levels, orphan detection,
    feedback triage, incident response, ownership, and retirement.
11. Deliver with [assets/knowledge-base-design-template.md](assets/knowledge-base-design-template.md).

## Guardrails

- Do not ingest content without authority, provenance, ownership, and permissions.
- Do not treat embedding similarity as evidence of truth or authority.
- Do not remove meaningful tables, headings, relationships, effective dates, or
  version context during transformation.
- Do not mix instructional authority into retrieved knowledge by default.
- Do not cite a chunk when the underlying source cannot be identified and accessed.
- Do not claim a knowledge base is complete; report coverage and known gaps.
- Keep platform-specific ingestion and index settings in adapters.

## Output Contract

Provide source registry, authority hierarchy, information model, ingestion and
retrieval design, permission model, evaluation set, operations plan, risks, and
implementation tasks for extraction, indexing, application, security, and QA.

## Recovery

Quarantine sources with missing authority, ownership, provenance, or permissions.
When authoritative sources conflict, preserve both with effective dates and route
the conflict to the owner. When retrieval cannot support a grounded answer, require
abstention, a cited fallback, or an explicit coverage-gap response.

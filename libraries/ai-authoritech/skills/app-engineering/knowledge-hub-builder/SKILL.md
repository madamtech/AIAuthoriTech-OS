---
name: knowledge-hub-builder
description: Create build-ready specifications for governed, searchable knowledge hubs covering audiences, information architecture, source authority, content types, taxonomy, metadata, publishing workflow, permissions, search, navigation, AI-assisted answers, citations, feedback, accessibility, analytics, freshness, localization, integrations, migration, testing, deployment, and operations. Use for help centers, documentation portals, internal knowledge sites, policy hubs, resource libraries, partner centers, or RAG-enabled discovery—not unauthorized ingestion, replacing source governance, or presenting generated answers without traceable evidence.
---

# Knowledge Hub Builder

Design discovery, trust, and stewardship before choosing a search interface.

1. Confirm audiences, supported questions and tasks, exclusions, public or private
   boundaries, brand, devices, languages, accessibility, freshness, risk,
   success measures, and owners.
2. Inventory sources and content types with authority, owner, audience,
   sensitivity, system of record, effective date, version, rights, lifecycle,
   update mechanism, and migration status.
3. Define source hierarchy and conflict behavior. Preserve material disagreement
   and distinguish policy, procedure, reference, guidance, news, training, FAQ,
   troubleshooting, and community content.
4. Define taxonomy, controlled vocabulary, topics, products, audiences, tasks,
   content types, regions, effective dates, status, entities, relationships, and
   stable identifiers using
   [references/knowledge-hub-standard.md](references/knowledge-hub-standard.md).
5. Define author, reviewer, approver, publisher, translator, subject-matter expert,
   administrator, and reader permissions. Enforce source and item access before
   search, preview, export, recommendation, or AI retrieval.
6. Define templates and standards for title, summary, audience, purpose,
   prerequisites, steps, examples, warnings, related content, owner, version,
   effective date, next review, citations, feedback, and accessibility.
7. Model draft, review, approved, scheduled, published, superseded, expired,
   archived, withdrawn, and deleted states with validation, separation of duties,
   notification, redirects, preservation, and audit.
8. Design navigation around audience tasks and mental models. Define landing
   pages, collections, topic pages, breadcrumbs, related content, recent content,
   favorites, history, and recovery from dead ends.
9. Define search indexing, tokenization, synonyms, spelling, filters, facets,
   ranking, freshness, authority boosts, exact matches, permissions, snippets,
   pagination, zero results, analytics, and relevance evaluation.
10. For AI assistance, define approved corpus, access filtering, retrieval,
    reranking, citations, source preview, effective-date handling, conflict
    disclosure, abstention, feedback, evaluation, and escalation. Treat generated
    summaries as derived content, not source authority.
11. Define responsive and accessible headings, landmarks, keyboard navigation,
    focus, contrast, zoom, reflow, tables, code, media alternatives, downloads,
    language metadata, search status, errors, and reading order.
12. Define feedback categories, context, routing, response expectations,
    duplication, moderation, privacy, resolution, content correction, requester
    notification, and audit.
13. Define analytics for successful search, zero results, reformulation,
    abandonment, task completion, helpfulness, stale content, review compliance,
    coverage, broken links, accessibility, and AI answer quality without using
    page views as the sole value measure.
14. Plan ingestion, import, canonicalization, redirects, attachment handling,
    deduplication, broken-link repair, permission validation, content freeze,
    cutover, rollback, reconciliation, and retirement of legacy sources.
15. Decompose delivery into vertical slices combining content, metadata,
    navigation, search, permissions, analytics, tests, deployment, documentation,
    and operations.
16. Deliver with
    [assets/knowledge-hub-plan-template.md](assets/knowledge-hub-plan-template.md).

## Rules

- Do not publish or ingest content without authority, ownership, rights, and
  audience classification.
- Do not let search ranking override permissions or source authority.
- Do not merge conflicting policies or effective versions into false consensus.
- Do not cite an AI answer when the user cannot identify and access its source.
- Do not display expired or superseded content as current without clear status.
- Do not remove headings, tables, warnings, effective dates, or relationships
  during migration merely to simplify indexing.
- Do not claim completeness; report coverage, freshness, and known gaps.
- Do not measure success only by traffic, searches, or answer-generation volume.

## Handoff

Provide the hub charter, source registry and authority hierarchy, content model,
taxonomy and metadata, permissions, publishing workflow, information architecture,
search contract, AI assistance and evaluation, accessibility, feedback, analytics,
migration, vertical slices, testing, deployment, operations, risks, assumptions,
and open decisions.

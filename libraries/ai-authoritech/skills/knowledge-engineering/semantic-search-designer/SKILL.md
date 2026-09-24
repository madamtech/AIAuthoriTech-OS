---
name: semantic-search-designer
description: Design and evaluate lexical, vector, hybrid, filtered, and reranked search systems over governed corpora, including query understanding, chunking, metadata, embeddings, access filtering, relevance judgments, latency, and observability. Use for enterprise search, knowledge hubs, retrieval layers, and RAG retrieval. Do not select retrieval technology without representative queries, authorization controls, and measured relevance. Use when asked to (1) design semantic search, (2) revise semantic search, (3) compare options for semantic search, or (4) document specifications for semantic search.
---

# Semantic Search Designer

Design retrieval from representative queries, governed content, and measured relevance.

## Procedure

1. Define users, query tasks, corpus, relevance, freshness, access, latency, cost, and success metrics.
2. Build representative query sets with intent, language, difficulty, segments, judgments, and no-result expectations.
3. Design ingestion, parsing, chunking, metadata, deduplication, versions, and deletion propagation.
4. Compare lexical, dense, sparse, hybrid, filters, query rewriting, and reranking under equal evidence using [references/semantic-search-standard.md](references/semantic-search-standard.md).
5. Enforce authorization before and after retrieval; prevent metadata, snippets, counts, and caches from leaking content.
6. Measure recall, precision, ranking, coverage, latency, cost, freshness, and results by meaningful segment.
7. Test exact identifiers, acronyms, multilingual queries, ambiguity, stale content, adversarial text, and access boundaries.
8. Define monitoring, relevance feedback, drift, reindexing, rollback, and evaluation triggers.
9. Deliver architecture, index contract, query flow, evaluation results, limits, and operational plan with [assets/semantic-search-design-template.md](assets/semantic-search-design-template.md).

## Guardrails

- Do not use embeddings as an authorization boundary.
- Do not evaluate only with synthetic easy queries or aggregate scores.
- Do not return inaccessible content through snippets, citations, logs, or timing side channels.
- Do not claim semantic relevance without human-calibrated judgments or equivalent evidence.

## Recovery

If authorization filtering, index freshness, deletion propagation, or relevance
gates fail, stop serving the affected index or segment and restore the last
verified configuration. Reconcile source and index state, remove leaked content,
preserve failed queries, and rerun representative evaluation before promotion.

## Output Contract

Provide users and query tasks, corpus and access model, ingestion and index
contract, retrieval and reranking design, evaluation dataset and results,
latency and cost limits, failure handling, monitoring, rollback, and open risks.

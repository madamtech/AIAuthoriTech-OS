---
name: semantic-search-designer
description: Design and evaluate lexical, vector, hybrid, filtered, and reranked search systems over governed corpora, including query understanding, chunking, metadata, embeddings, access filtering, relevance judgments, latency, and observability. Use for enterprise search, knowledge hubs, retrieval layers, and RAG retrieval. Do not select retrieval technology without representative queries, authorization controls, and measured relevance.
---

# Semantic Search Designer

1. Define users, query tasks, corpus, relevance, freshness, access, latency, cost, and success metrics.
2. Build representative query sets with intent, language, difficulty, segments, judgments, and no-result expectations.
3. Design ingestion, parsing, chunking, metadata, deduplication, versions, and deletion propagation.
4. Compare lexical, dense, sparse, hybrid, filters, query rewriting, and reranking under equal evidence.
5. Enforce authorization before and after retrieval; prevent metadata, snippets, counts, and caches from leaking content.
6. Measure recall, precision, ranking, coverage, latency, cost, freshness, and results by meaningful segment.
7. Test exact identifiers, acronyms, multilingual queries, ambiguity, stale content, adversarial text, and access boundaries.
8. Define monitoring, relevance feedback, drift, reindexing, rollback, and evaluation triggers.
9. Deliver architecture, index contract, query flow, evaluation results, limits, and operational plan.

## Rules

- Do not use embeddings as an authorization boundary.
- Do not evaluate only with synthetic easy queries or aggregate scores.
- Do not return inaccessible content through snippets, citations, logs, or timing side channels.
- Do not claim semantic relevance without human-calibrated judgments or equivalent evidence.

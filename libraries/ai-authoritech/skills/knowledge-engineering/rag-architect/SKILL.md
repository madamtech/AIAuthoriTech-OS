---
name: rag-architect
description: Architect retrieval-augmented generation systems that produce grounded, access-controlled, cited answers from governed knowledge using measurable ingestion, retrieval, context assembly, generation, verification, and failure behavior. Use for enterprise assistants, question answering, research, and knowledge-grounded agents. Do not use RAG to replace missing governance, authorize actions, or guarantee truth beyond available evidence.
---

# RAG Architect

1. Define answerable questions, users, decisions, risk, source authority, citations, abstention, latency, and cost.
2. Design governed ingestion with provenance, access, versions, parsing, chunking, deletion, and refresh.
3. Select retrieval and reranking from representative evidence; separate retrieval quality from answer quality.
4. Assemble context by authority, relevance, freshness, diversity, token budget, and trust; label untrusted content as data.
5. Define grounded generation, citation binding, conflict handling, uncertainty, insufficient-evidence, and escalation.
6. Prevent retrieved instructions from overriding system rules, tools, schemas, or authorization.
7. Evaluate retrieval recall, context precision, groundedness, citation correctness, completeness, safety, access, latency, and cost.
8. Test stale, conflicting, missing, malicious, multilingual, long, and unauthorized sources plus tool and retrieval failures.
9. Define monitoring, source drift, feedback, incident response, reindexing, model changes, rollout, and rollback.
10. Deliver architecture, contracts, threat model, evaluation suite, evidence, operations, and limitations.

## Rules

- Do not answer from model memory when the contract requires governed source evidence.
- Do not cite a source that does not support the claim.
- Do not let retrieval bypass row-, document-, tenant-, or field-level access.
- Do not hide insufficient evidence behind confident language.

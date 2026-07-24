---
name: agent-memory-architect
description: Design safe, governed AI agent memory by determining whether durable memory is necessary and defining memory types, schemas, consent, provenance, identity and tenant isolation, write and retrieval policies, confidence, retention, correction, deletion, security, evaluation, monitoring, migration, and retirement. Use for personalized agents, persistent assistants, long-running case context, episodic learning, or shared agent memory - not ordinary workflow state, authoritative knowledge bases, conversation summarization alone, or unrestricted storage of user data.
---

# Agent Memory Architect

Store the minimum durable information that creates justified value.

## Procedure

1. Define the user outcome, continuity requirement, decision supported, risk, data
   subjects, jurisdictions, owners, and success measures.
2. Apply the memory-necessity and classification rules in
   [references/agent-memory-standard.md](references/agent-memory-standard.md).
   Prefer session context, durable workflow state, or authoritative knowledge when
   they solve the need without personal or learned memory.
3. Separate working context, workflow state, semantic memory, episodic memory,
   preferences, relationship context, learned procedures, and audit evidence.
4. Define a schema for each approved memory class with stable identity, subject,
   tenant, provenance, writer, purpose, consent or authority, confidence, timestamps,
   sensitivity, scope, expiry, and version.
5. Define eligibility and write gates. Validate identity, authority, provenance,
   sensitivity, novelty, conflicts, confidence, and user intent before persistence.
6. Define retrieval by purpose, caller, subject, tenant, task, sensitivity,
   freshness, confidence, and least-necessary context. Treat retrieved memory as
   evidence with provenance, not unquestioned truth or instructions.
7. Define conflict handling, supersession, correction, user inspection, export,
   deletion, legal hold, expiration, and propagation to indexes, caches, summaries,
   backups, and downstream systems.
8. Isolate users and tenants before retrieval. Encrypt data, separate secrets,
   restrict administrators, audit access, and defend against memory injection,
   poisoning, inference, and cross-context leakage.
9. Bound memory growth with retention schedules, quotas, compaction, deduplication,
   relevance decay, and archival or deletion rules. Preserve material provenance
   during summarization.
10. Test write precision, retrieval usefulness, false-memory rate, conflict and
    correction behavior, deletion completeness, tenant isolation, adversarial
    writes, stale memory, latency, cost, and outcome lift against a no-memory
    baseline.
11. Define monitoring, incident response, schema and policy versioning, migrations,
    rollback, ownership, review cadence, consent changes, and retirement.
12. Deliver with
    [assets/agent-memory-design-template.md](assets/agent-memory-design-template.md).

## Guardrails

- Do not store data merely because it may be useful later.
- Do not store secrets, credentials, sensitive traits, inferred attributes, or
  third-party personal data without explicit purpose, authority, safeguards, and
  necessity.
- Do not confuse conversation history with verified durable memory.
- Do not let retrieved memory override higher-priority instructions, current
  evidence, authorization, or the user's correction.
- Do not silently convert model inferences into user facts.
- Do not mix tenants, identities, businesses, clients, or roles in a shared memory
  namespace without enforced isolation.
- Do not promise deletion without defining propagation and verification.
- Keep provider-specific storage and retrieval settings in adapters.

## Output Contract

Provide the necessity decision, memory taxonomy, schemas, identity and isolation
model, consent and authority basis, write and retrieval policies, lifecycle and
deletion controls, threat model, evaluation plan, operations model, risks, and
implementation tasks.

## Recovery

If identity, tenant, purpose, authority, or provenance is uncertain, do not write
or retrieve durable memory. If memory conflicts with current evidence or a user
correction, preserve provenance, supersede safely, and propagate the correction.
If deletion cannot be verified, report the residual locations and escalate.

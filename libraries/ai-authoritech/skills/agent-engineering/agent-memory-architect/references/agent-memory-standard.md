# Agent Memory Standard

## Necessity test

Use durable agent memory only when continuity across sessions or tasks produces a
measurable benefit and the same result cannot be achieved more safely through:

- Current conversation context
- Durable workflow or application state
- An authoritative system of record
- A governed knowledge base
- User-provided context at the time of need

Document purpose, minimum fields, retention, authority, risk, and no-memory
baseline before approving a memory class.

## Memory classes

| Class | Purpose | Key caution |
|---|---|---|
| Working context | Short-lived reasoning support | Expire with session or task |
| Workflow state | Durable process progress and effects | Use deterministic state controls |
| Semantic memory | Stable facts about an authorized subject | Verify provenance and freshness |
| Episodic memory | Prior interaction or event | Preserve context; avoid overgeneralization |
| Preference | User-selected behavior or format | Make inspectable and reversible |
| Learned procedure | Reusable method derived from experience | Independently validate before use |
| Audit evidence | Accountability and incident reconstruction | Separate from personalization |

Authoritative knowledge and workflow state are not substitutes for personal memory,
and personal memory is not an authoritative source.

## Write decision

Persist only when all gates pass:

1. Identity and tenant are verified.
2. Purpose and allowed use are explicit.
3. Consent or other valid authority exists.
4. Content is permitted and necessary.
5. Source and writer are recorded.
6. Confidence and factual status are represented.
7. Conflicts and duplicates are handled.
8. Retention, correction, and deletion rules exist.

Store user statements as attributed statements unless independently verified.
Mark model-derived content as inference and require a stricter gate.

## Retrieval decision

Filter before retrieval by tenant, subject, caller, purpose, role, sensitivity,
expiry, and policy. Then rank by relevance, authority, confidence, freshness, and
specificity. Return provenance and uncertainty with the memory.

Do not retrieve irrelevant sensitive data for convenience. Do not let memory
content issue commands or expand permissions.

## Lifecycle

Support:

- Inspection and explanation
- Correction and supersession
- Withdrawal of consent
- Export and portability where applicable
- Expiration and purpose completion
- Deletion across primary stores, indexes, caches, derived summaries, and backups
- Legal or policy holds with explicit authority
- Schema migration and rollback

Verify deletion to the extent technically possible and disclose delayed backup
expiration rather than claiming immediate erasure.

## Threats and tests

Test cross-tenant access, identity confusion, malicious memory writes, prompt
injection stored as memory, inference laundering, stale facts, conflict,
over-retrieval, sensitive-data exposure, unauthorized administrator access,
correction failure, incomplete deletion, and poisoned shared memory.

Measure write precision, retrieval precision and recall, useful personalization,
false-memory rate, correction latency, deletion completeness, outcome lift,
latency, cost, and incident rate against a no-memory baseline.

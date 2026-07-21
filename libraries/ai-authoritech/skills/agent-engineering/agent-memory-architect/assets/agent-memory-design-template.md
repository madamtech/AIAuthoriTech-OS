# Agent Memory Design

## Design control

- Agent and version:
- Outcome and continuity need:
- Risk and data classification:
- Data subjects and tenants:
- Business, privacy, and technical owners:

## Necessity decision

- No-memory baseline:
- Alternatives considered:
- Expected measurable benefit:
- Decision: No memory / Session only / Durable memory

## Memory taxonomy

| Memory class | Purpose | Subject | Minimum fields | Authority | Retention | Owner |
|---|---|---|---|---|---|---|

## Memory schema

| Field | Type | Required | Provenance | Sensitivity | Validation | Indexing |
|---|---|---|---|---|---|---|

Include identity, tenant, purpose, source, writer, factual status, confidence,
created and effective times, expiry, version, consent or authority, and lineage.

## Write policy

| Candidate | Eligibility | Required evidence | Conflict rule | Approval | Rejection |
|---|---|---|---|---|---|

## Retrieval policy

| Task | Caller | Filters | Ranking | Maximum context | Provenance | Abstention |
|---|---|---|---|---|---|---|

## Identity, isolation, and security

Document subject resolution, tenant namespaces, role enforcement, encryption,
administrator access, audit logs, secret handling, and injection defenses.

## Lifecycle controls

| Event | Action | Owner | Propagation | Verification | Deadline |
|---|---|---|---|---|---|

Cover inspection, correction, supersession, consent withdrawal, export, expiry,
legal hold, deletion, migration, rollback, and retirement.

## Evaluation

| Test or metric | Baseline | Target | Hard gate | Evidence |
|---|---:|---:|---|---|

Include write and retrieval quality, false memory, usefulness, correction, deletion,
isolation, adversarial behavior, outcome lift, latency, and cost.

## Operations and risks

| Risk or operational action | Detection | Mitigation | Owner | Review cadence |
|---|---|---|---|---|

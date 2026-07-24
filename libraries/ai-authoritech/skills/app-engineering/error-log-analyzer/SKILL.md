---
name: error-log-analyzer
description: Analyze application, infrastructure, device, database, integration, security, job, and AI-system logs by preserving provenance, redacting sensitive data, normalizing timestamps and fields, grouping event signatures, correlating requests and state transitions, establishing baselines, detecting anomalies, reconstructing failure sequences, and producing evidence-backed findings and next queries. Use for incident triage, defect investigation, operational review, and observability improvement - not to treat logs as complete truth, infer causality from proximity alone, expose credentials or personal data, or change live systems without authorization.
---

# Error Log Analyzer

Turn noisy log records into a bounded evidence trail.

## Procedure

1. Confirm the question, time window, systems, environments, tenants, versions,
   releases, time zones, user impact, urgency, and whether the work is read-only.
2. Inventory each source with owner, collection method, format, clock, retention,
   sampling, buffering, ordering, known gaps, access restrictions, and integrity.
   Preserve an immutable raw copy or authoritative query reference when allowed.
3. Minimize and redact before sharing or reporting. Remove secrets, tokens,
   credentials, session identifiers, payment data, unnecessary personal data,
   sensitive payloads, and confidential content while retaining stable surrogate
   identifiers needed for correlation.
4. Parse records using
   [references/error-log-analysis-standard.md](references/error-log-analysis-standard.md).
   Preserve raw timestamp and message, then normalize time, severity, service,
   environment, version, host or instance, request or trace ID, event name,
   outcome, duration, status, exception type, and safe dimensions.
5. Record clock sources, offsets, drift, ingestion delay, missing zones, and
   ordering limitations. Do not reconstruct a precise sequence when timestamp
   quality cannot support one.
6. Remove exact duplicates only when duplication is established. Group variable
   messages into signatures while retaining counts, first and last occurrence,
   examples, affected versions, dimensions, and grouping confidence.
7. Establish a relevant baseline by comparing prior window, working cohort,
   unaffected version, normal volume, traffic, deployment, feature flag, and
   seasonality. Use rates and denominators rather than raw counts alone.
8. Correlate by trace, request, operation, job, message, user surrogate, tenant
   surrogate, resource, deployment, or time window. Distinguish direct identifier
   joins from time-based association.
9. Reconstruct the event sequence from trigger through retries, queues, services,
   integrations, state changes, error, recovery, and user-visible outcome. Mark
   missing spans and conflicting records.
10. Separate primary failure, downstream symptoms, retries, duplicate reporting,
    expected control flow, warning noise, and recovery events. Account for one
    incident producing many records.
11. Rank clusters by affected outcomes, unique operations, rate change, breadth,
    duration, severity, recurrence, data or security exposure, and recovery, not
    merely by log level or line count.
12. Compare working and failing cohorts across input, identity, tenant, data,
    region, device, version, dependency, configuration, flag, deployment, load,
    concurrency, and third-party state.
13. State findings as observation, association, anomaly, or causal hypothesis.
    Route causal testing to Bug Investigation Assistant; logs alone rarely prove
    root cause.
14. Produce exact follow-up queries or collection needs, expected discriminating
    evidence, owners, safety constraints, and decision thresholds.
15. Evaluate observability gaps: missing IDs, inconsistent schemas, excessive
    cardinality, misleading severity, absent outcomes, unsafe payloads, sampling,
    clock drift, retention, access, or alerts. Recommend instrument changes
    without silently applying them.
16. Deliver with
    [assets/error-log-analysis-report-template.md](assets/error-log-analysis-report-template.md).

## Guardrails

- Do not expose or repeat sensitive fields merely because they appeared in logs.
- Do not alter or delete source logs during analysis.
- Do not assume ingestion order equals event order.
- Do not interpret absence of a record as proof an event did not occur when
  sampling, loss, filtering, retention, buffering, or instrumentation gaps exist.
- Do not equate ERROR severity or high volume with highest business impact.
- Do not count retries, replicas, or duplicate collectors as distinct incidents
  without evidence.
- Do not claim root cause from temporal proximity, correlation, or one stack trace.
- Do not run expensive, unbounded, or production-impacting queries without scope,
  limits, and authorization.

## Recovery

If timestamps, sampling, retention, identifiers, or source integrity cannot
support the requested sequence, narrow the claim and identify the missing
collection needed. Stop or bound queries that threaten production, preserve raw
evidence, redact sensitive fields, and route causal testing to a controlled bug
investigation.

## Output Contract

Provide the analysis question and scope, source and quality inventory, redaction
record, normalized schema, baseline, signature clusters, correlated timeline,
primary and downstream events, cohort comparison, ranked findings with confidence,
follow-up queries, observability gaps, risks, and open questions.

---
name: production-readiness-reviewer
description: Review whether a web, mobile, desktop, SaaS, internal, API, data, automation, AI-enabled, or vibe-coded application is ready for a bounded production release by verifying scope, ownership, test evidence, security, privacy, accessibility, performance, reliability, data migration, dependencies, observability, support, deployment, rollback, incident response, compliance, and approvals. Use before launch, major rollout, migration, or material change - not to deploy, waive risk, certify compliance, or call a release ready from plans, checklists, deadlines, or unexecuted tests. Use when asked to (1) review production readiness, (2) audit production readiness, (3) identify gaps in production readiness, or (4) recommend corrections to production readiness.
---

# Production Readiness Reviewer

Issue a recommendation whose strength never exceeds the evidence.

## Procedure

1. Confirm the release candidate, exact source revision and artifact, scope,
   environments, users, criticality, rollout window, dependencies, data classes,
   jurisdictions, obligations, risk tolerance, and accountable decision owner.
2. Define the review authority. Inspect and report without changing code,
   configuration, data, infrastructure, approvals, tickets, or production unless
   a separate action is explicitly authorized.
3. Establish evidence freshness, environment, artifact, owner, execution status,
   result, retention, and applicability. Classify each item as planned,
   implemented, executed, passed, failed, blocked, waived, stale, or not applicable.
4. Trace committed requirements and critical journeys to acceptance evidence.
   Cover normal, denied, invalid, duplicate, concurrent, interrupted, degraded,
   recovery, administrative, and external-effect behavior proportionate to risk.
5. Review architecture, capacity, dependencies, quotas, failure boundaries,
   compatibility, end-of-life exposure, configuration, secrets, identities,
   certificates, domains, licenses, and artifact provenance.
6. Review security and privacy: threat model, authentication, resource-level
   authorization, tenant isolation, vulnerability findings, dependency exposure,
   encryption, logging, data minimization, retention, deletion, consent,
   incident handling, exceptions, and specialist approvals.
7. Review accessibility, usability, localization, device and browser support,
   assistive-technology evidence, content readiness, support paths, and known
   limitations. Do not infer accessibility from appearance or automated scans.
8. Review performance, scalability, reliability, resilience, recovery objectives,
   load and failure evidence, saturation, rate limits, queue behavior, retries,
   idempotency, backpressure, timeouts, and cost under expected and peak demand.
9. Review data and integration readiness: schemas, migration, backfill,
   compatibility, backups, tested restore, reconciliation, import and export,
   webhooks, messages, jobs, third parties, sandbox evidence, and authoritative
   state verification.
10. Review observability and operations: business and technical signals, logs,
    metrics, traces, synthetic checks, dashboards, alert thresholds, paging,
    runbooks, support ownership, incident roles, escalation, communications,
    vendor contacts, and diagnostic access.
11. Review deployment and recovery: immutable artifact, environment parity,
    approvals, rollout stages, feature flags, verification, observation window,
    abort thresholds, rollback or forward-fix, data compatibility, staffing,
    freeze conditions, and evidence capture.
12. Apply [references/production-readiness-standard.md](references/production-readiness-standard.md)
    to classify findings as blocker, conditional blocker, significant risk,
    improvement, or accepted residual risk. Never average away a critical blocker.
13. Require every exception or waiver to name the risk, impact, owner, approver,
    rationale, compensating controls, monitoring, expiration, and remediation.
14. Issue one recommendation: ready, ready with conditions, not ready, or unable
    to determine. State exact scope, conditions, blockers, residual risks,
    decision owner, and evidence cutoff time.
15. Define launch-day and post-launch verification using authoritative business
    outcomes, data reconciliation, security and access checks, service signals,
    support intake, customer impact, and rollback decision thresholds.
16. Deliver with
    [assets/production-readiness-review-template.md](assets/production-readiness-review-template.md).

## Guardrails

- Do not treat a completed checklist as proof that its controls work.
- Do not mark planned, implemented, automated, or previously passed evidence as
  currently executed and passed for this release candidate.
- Do not approve a different artifact, environment, scope, or configuration from
  the one supported by the evidence.
- Do not let a score, deadline, executive preference, or release window override a
  critical blocker.
- Do not waive unknown risk or accept risk on behalf of an unnamed owner.
- Do not claim security, privacy, accessibility, legal, regulatory, or compliance
  certification outside the evidence and authority provided.
- Do not call rollback ready unless it is compatible with data changes, owned,
  executable, and tested proportionate to risk.
- Do not perform the deployment as part of a readiness review.

## Recovery

If artifact identity, evidence freshness, required approvals, rollback readiness,
or a critical control cannot be verified, issue not ready or unable to determine
for the affected scope. Preserve blockers and the evidence cutoff, identify the
owner and proof needed to resume, and never convert an unknown or failed control
into an accepted risk without authorized review.

## Output Contract

Provide the release and evidence scope, evidence-quality inventory, requirements
and journey traceability, domain findings, blockers and conditions, exceptions
and residual risk, readiness recommendation, decision owner, evidence cutoff,
launch and post-launch verification, rollback thresholds, and open decisions.

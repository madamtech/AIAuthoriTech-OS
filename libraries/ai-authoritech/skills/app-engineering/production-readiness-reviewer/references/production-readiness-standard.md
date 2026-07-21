# Production Readiness Standard

## Evidence quality

Evidence must identify the release artifact, environment, configuration, time,
executor, method, result, and retained record. Evaluate:

- **Applicable:** covers the current scope and risk.
- **Authoritative:** comes from the system or owner qualified to establish it.
- **Executed:** represents actual activity, not intention or configuration.
- **Current:** remains valid after relevant changes.
- **Reproducible:** method and inputs are sufficiently recorded.
- **Complete:** important cohorts, boundaries, and failure states are represented.

Label limitations. A prior release, preview, synthetic fixture, emulator, scan, or
unit test may support but not automatically establish production readiness.

## Finding classes

- **Blocker:** credible risk of severe user, business, security, privacy, data,
  compliance, recovery, or operational harm without adequate control.
- **Conditional blocker:** release may proceed only after a specific condition is
  evidenced and approved before exposure.
- **Significant risk:** material but accepted only by an authorized named owner.
- **Improvement:** worthwhile but not required for this bounded release.
- **Accepted residual risk:** documented exposure with owner, approval, controls,
  monitoring, expiration, and remediation.

Severity is not an average. One blocker can determine the recommendation.

## Core readiness domains

Review at least:

1. product scope, requirements, users, content, and acceptance;
2. architecture, dependencies, configuration, provenance, and compatibility;
3. authentication, authorization, security, privacy, and data governance;
4. accessibility, usability, localization, and supported clients;
5. performance, capacity, reliability, resilience, and cost;
6. schemas, migration, backup, restore, reconciliation, and integrations;
7. tests, defects, waivers, traceability, and release evidence;
8. observability, support, incident response, communications, and ownership;
9. deployment, rollout, verification, abort, rollback, and recovery;
10. legal, regulatory, contractual, licensing, and specialist decisions applicable
   to the release.

Mark a domain not applicable only with rationale and an accountable owner.

## Recommendation

- **Ready:** no blockers; required controls are evidenced; residual risks are
  accepted by authorized owners.
- **Ready with conditions:** no unresolved blocker will be exposed because named,
  time-bound, verifiable pre-release or rollout conditions constrain release.
- **Not ready:** one or more blockers remain or risk acceptance is invalid.
- **Unable to determine:** evidence is insufficient, stale, contradictory, or not
  tied to the candidate.

State release scope, artifact, environment, evidence cutoff, rollout constraint,
conditions, residual risk, and decision authority. The reviewer recommends; the
authorized business/change owner decides.

## Exception requirements

Every exception includes finding, affected users and outcomes, likelihood and
impact, exposure window, owner, approver, rationale, compensating controls,
monitoring and trigger, expiration, remediation, and re-review condition. An
exception cannot convert missing evidence into passing evidence.

## Launch verification

Define preflight, canary or phased exposure, observation window, authoritative
journey and data checks, security and access checks, SLI thresholds, support and
incident signals, decision checkpoints, pause or abort authority, rollback or
forward-fix, communication, and evidence retention.

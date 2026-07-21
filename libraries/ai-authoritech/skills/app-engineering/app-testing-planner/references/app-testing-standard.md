# Application Testing Standard

## Risk model

Score each risk consistently using a documented scale:

- Likelihood: probability that the failure occurs.
- Impact: harm to users, revenue, operations, trust, or compliance.
- Exposure: frequency and population affected.
- Detectability: chance the failure escapes before harm.
- Reversibility: effort and time required to recover.
- Sensitivity: security, privacy, safety, or regulated-data implications.

Record the formula and thresholds. Scores support judgment; they do not replace it.

## Test levels

| Level | Primary purpose | Typical evidence |
|---|---|---|
| Static review | Detect ambiguity and design defects early | Review findings and approvals |
| Unit | Verify isolated logic and boundaries | Versioned automated results |
| Component | Verify a module with controlled dependencies | Component report and logs |
| Contract | Verify consumer-provider compatibility | Contract results and schemas |
| Integration | Verify system boundaries and failure behavior | Traces, payload summaries, reconciliation |
| End-to-end | Verify a small set of critical journeys | Results, screenshots, and correlated logs |
| Exploratory | Discover unanticipated behavior | Session charter and findings |
| User acceptance | Confirm business fitness | Named business approval |
| Migration | Verify completeness, accuracy, and rollback | Counts, checksums, exceptions, reconciliation |
| Production verification | Confirm release health safely | Smoke results, metrics, and rollback decision |

## Coverage matrix

Give every material requirement and risk a stable identifier. Map it to:

- test level and case identifier;
- positive, negative, boundary, permission, and failure-path coverage;
- platform, browser, device, locale, role, and configuration;
- expected result and authoritative oracle;
- automation status and execution frequency;
- owner, environment, data fixture, and evidence;
- current state: planned, implemented, executed, passed, failed, blocked, or waived.

Do not use “covered” when no executable test or review evidence exists.

## Nonfunctional coverage

- Accessibility: keyboard, focus, semantics, contrast, zoom, reflow, names,
  descriptions, errors, status messages, and assistive-technology journeys.
- Performance: response time, throughput, concurrency, saturation, endurance,
  payload size, cold starts, and third-party latency with defined percentiles.
- Reliability: timeout, retry, duplicate, reordering, outage, degraded dependency,
  queue growth, failover, backup, restore, and recovery-point objectives.
- Security and privacy: authentication, authorization, tenant isolation, input
  handling, session lifecycle, secrets, logging, retention, deletion, and abuse.
- Compatibility: supported browsers, devices, operating systems, screen sizes,
  network conditions, versions, and backward-compatible contracts.
- AI-enabled behavior: prompt injection, unsafe tool use, data leakage,
  hallucination impact, refusal, grounding, nondeterminism, evaluation drift,
  human review, and fallback behavior.

Route formal penetration tests, legal compliance decisions, and accessibility
certification to qualified reviewers.

## Test data and environments

Define environment purpose, owner, access, parity exceptions, reset method,
observability, service virtualization, and third-party limits. Prefer generated
fixtures and de-identified datasets. Preserve referential integrity and edge
cases. Control clocks and random seeds when relevant. Verify cleanup and prevent
test messages, payments, or notifications from reaching real recipients.

## Automation portfolio

Automate stable, deterministic, high-value checks at the lowest effective level.
Keep a small critical-path end-to-end suite. Require clear assertions, diagnostic
output, independent setup, bounded execution, and ownership. Track flaky-test
rate, runtime, failure cause, maintenance cost, and defect yield.

## Defects, gates, and waivers

Severity measures impact; priority measures scheduling. Define both explicitly.
A release gate must include:

- measurable entry and exit criteria;
- required suites and acceptable pass rates;
- unresolved-defect thresholds;
- security, privacy, accessibility, and performance criteria;
- rollback readiness and production monitoring;
- evidence owner and named approver.

A waiver must identify the affected requirement, risk, duration, owner,
compensating controls, approval, and revalidation date.

## Evidence integrity

Retain tool version, build identifier, environment, configuration, timestamp,
test-data reference, result, logs, and approver. Protect evidence from alteration
and redact secrets or sensitive payloads. Distinguish raw results from summaries.

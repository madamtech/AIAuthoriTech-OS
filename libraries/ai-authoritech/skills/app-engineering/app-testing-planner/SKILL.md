---
name: app-testing-planner
description: Create risk-based application test strategies, traceability matrices, environment and test-data plans, functional and nonfunctional coverage, automation boundaries, defect triage rules, release gates, and evidence requirements. Use when planning quality assurance for web, mobile, SaaS, internal, API-driven, AI-enabled, or vibe-coded applications before implementation, acceptance, migration, or release - not as proof that unexecuted tests passed or as a substitute for security, accessibility, privacy, or compliance specialists. Use when asked to (1) plan app testing, (2) revise app testing, (3) evaluate options for app testing, or (4) prepare implementation of app testing.
---

# App Testing Planner

Turn requirements and architecture into testable claims and release evidence.

## Procedure

1. Confirm the product outcome, users, critical journeys, platforms, environments,
   integrations, data classes, regulatory constraints, release model, risk
   tolerance, and accountable approvers.
2. Inventory requirements, acceptance criteria, architecture decisions, schemas,
   permissions, integration contracts, operational objectives, and known defects.
   Mark missing or ambiguous inputs; do not silently convert assumptions into
   requirements.
3. Build a risk model using likelihood, user or business impact, detectability,
   exposure, reversibility, and data or security sensitivity. Prioritize tests by
   risk rather than by screen count.
4. Define the test levels and owners: static review, unit, component, contract,
   integration, end-to-end, exploratory, user acceptance, migration, smoke,
   regression, resilience, and production verification.
5. Map every material requirement and risk to one or more tests and evidence
   artifacts. Use
   [references/app-testing-standard.md](references/app-testing-standard.md) for
   coverage and evidence rules.
6. Cover positive, negative, boundary, invalid, duplicate, reordered, delayed,
   interrupted, concurrent, unauthorized, expired-session, and partial-failure
   behavior where applicable.
7. Define nonfunctional coverage for accessibility, performance, scalability,
   reliability, recovery, compatibility, localization, privacy, security,
   observability, maintainability, and usability. Assign specialist review where
   the risk requires it.
8. Define environments, configuration parity, service virtualization, test
   accounts, seeded data, clocks, feature flags, third-party sandboxes, cleanup,
   and isolation. Use synthetic or approved de-identified data.
9. Select automation by repeatability, determinism, business criticality,
   execution frequency, maintenance cost, feedback speed, and failure
   diagnosability. Keep exploratory and judgment-heavy checks human-led.
10. Define defect severity and priority independently, ownership, evidence,
    reproduction requirements, triage cadence, retest, regression, waiver, and
    escalation rules.
11. Establish entry criteria, exit criteria, release blockers, allowed residual
    risk, approvers, rollback readiness, monitoring, and post-release verification.
    A deadline alone must not change a failed gate to passed.
12. Define results, logs, screenshots, traces, accessibility reports, performance
    baselines, security findings, approvals, waivers, and retention as release
    evidence. Redact secrets and sensitive data.
13. Deliver the plan with
    [assets/app-test-plan-template.md](assets/app-test-plan-template.md), clearly
    distinguishing planned, implemented, executed, passed, failed, blocked, and
    waived tests.

## Guardrails

- Do not claim coverage without requirement-to-test traceability.
- Do not mark a planned or automated test as executed.
- Do not use production personal, confidential, regulated, or secret data unless
  explicitly authorized and controlled.
- Do not make end-to-end tests the only defense for business logic.
- Do not treat HTTP success, a rendered page, or an AI-generated assertion as
  proof of the business outcome.
- Do not waive critical defects without a named risk owner, rationale, expiration,
  compensating controls, and approval.
- Do not hide flaky tests; quarantine with ownership and a resolution deadline.
- Keep test cases independent, deterministic, observable, and reproducible where
  feasible.

## Recovery

If requirements, environments, or build provenance cannot be reconciled, mark the
affected coverage blocked and identify the evidence needed to resume. If a test
could alter production or expose sensitive data, stop that test path until an
authorized isolated method exists. Never convert missing or contradictory
evidence into a pass.

## Output Contract

Provide scope and assumptions, risk register, test-level strategy, coverage matrix,
environment and data plan, automation plan, defect workflow, entry and exit gates,
release evidence checklist, residual risks, waivers, owners, and open decisions.

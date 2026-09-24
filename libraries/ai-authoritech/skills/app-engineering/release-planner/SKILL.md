---
name: release-planner
description: Convert a prioritized product backlog into governed, outcome-based releases with explicit scope, dependencies, capacity, forecasts, readiness gates, launch cohorts, communications, enablement, adoption, support, benefit measurement, contingency, and review decisions. Use for MVP planning, product increments, coordinated launches, beta or phased releases, roadmap commitments, and release replanning - not technical deployment commands, detailed requirements, effort guarantees, or claiming benefits before measurement. Use when asked to (1) plan release, (2) revise release, (3) evaluate options for release, or (4) prepare implementation of release.
---

# Release Planner

Plan a release as a controlled product outcome, not a date-shaped feature list.

## Procedure

1. Confirm the release outcome, target users, strategic objective, success
   measures, desired window, decision owner, risk tolerance, fixed obligations,
   teams, capacity, and evidence supporting the prioritized backlog.
2. Define release type and maturity: internal, alpha, beta, limited availability,
   general availability, experiment, migration, remediation, or retirement. State
   who is eligible, what promises apply, and how feedback changes the plan.
3. Create the smallest coherent scope that delivers an end-to-end outcome.
   Include required controls, data, permissions, integrations, accessibility,
   observability, support, documentation, recovery, and maintenance, not only
   visible features.
4. Separate committed scope, conditional scope, discovery, and explicitly excluded
   work. Give every item an identifier, owner, acceptance evidence, dependency,
   and disposition.
5. Map hard and soft dependencies across product, design, engineering, data,
   security, privacy, legal, accessibility, operations, support, marketing,
   sales, training, vendors, and customer commitments.
6. Build a forecast from capacity, throughput, uncertainty, dependency timing,
   work in progress, review queues, and contingency. Use
   [references/release-planning-standard.md](references/release-planning-standard.md).
   Express uncertain dates as ranges and confidence, not false precision.
7. Define milestones as evidence-producing decisions: scope readiness, design and
   architecture approval, build complete, test exit, operational readiness,
   launch authorization, cohort expansion, general availability, and outcome
   review.
8. Define entry and exit criteria for each stage. Link requirements, risks, test
   evidence, unresolved defects, security and privacy findings, accessibility,
   data migration, performance, recovery, support, documentation, and approvals.
9. Define launch cohorts, eligibility, entitlements, feature flags, sequencing,
   observation windows, feedback channels, expansion criteria, hold criteria, and
   withdrawal or rollback decisions. Keep product rollout distinct from technical
   deployment.
10. Create stakeholder, user, support, sales, operations, and executive
    communications with audience, message, channel, timing, owner, approval, and
    contingency. Do not announce unsupported dates or capabilities.
11. Define enablement: release notes, user guidance, training, administrator
    instructions, support scripts, known limitations, migration help, status
    information, and escalation paths.
12. Define adoption and outcome measurement using baselines, exposure, activation,
    successful use, retention, business result, guardrails, segments, data source,
    attribution limits, owner, observation window, and decision threshold.
13. Define scope-change control. Assess impact on outcome, risk, dependencies,
    capacity, evidence, support, communications, and forecast; record approval and
    what leaves the release when work enters.
14. Define contingency for delay, failed gates, vendor slippage, capacity loss,
    severe defects, incident, poor adoption, harmful outcomes, or invalidated
    assumptions. Preserve stop, reduce, stage, defer, or withdraw options.
15. Hold release reviews before launch, after each rollout stage, and after the
    outcome window. Decide proceed, expand, hold, remediate, withdraw, iterate, or
    close based on evidence.
16. Deliver with
    [assets/release-plan-template.md](assets/release-plan-template.md).

## Guardrails

- Do not call a feature list a release plan without a measurable user or business
  outcome.
- Do not commit a date unsupported by capacity, dependencies, and explicit
  uncertainty.
- Do not add scope without recording impact and removing, deferring, or funding
  other work.
- Do not treat code complete, deployed, or announced as user adoption or benefit.
- Do not hide mandatory controls, enablement, or operational work outside scope.
- Do not expand a cohort when guardrails or exit criteria fail.
- Do not rewrite baselines or thresholds after results are known.
- Do not claim causal impact when the measurement design supports only
  association.

## Recovery

If dependencies, capacity, required evidence, or a readiness gate cannot support
the planned scope and window, revise the sequence, cohort, scope, or forecast and
record an explicit go, hold, remediate, or withdraw decision. Do not promote a
release or rewrite success thresholds to conceal a failed gate.

## Output Contract

Provide the release charter, maturity and audience, committed and conditional
scope, exclusions, dependency and capacity plan, forecast and confidence,
milestones and gates, rollout cohorts, communications, enablement, adoption and
outcome measures, change control, contingency options, decision log, owners,
risks, and review schedule.

---
name: app-maintenance-planner
description: Create sustainable application maintenance and lifecycle plans covering service ownership, support, observability, incidents, problems, vulnerabilities, dependencies, backups, data retention, capacity, cost, accessibility, reliability, technical debt, change management, continuity, vendor risk, documentation, and retirement. Use after an application is released or when stabilizing an inherited web, mobile, SaaS, internal, API-driven, AI-enabled, or vibe-coded product—not to perform unapproved production changes or replace security, privacy, legal, compliance, or incident-response authorities.
---

# App Maintenance Planner

Keep the application supportable, secure, economical, and recoverable throughout
its useful life.

1. Confirm the product outcome, service tier, users, business owner, technical
   owner, support hours, environments, architecture, dependencies, data classes,
   obligations, recovery objectives, known limitations, and current health.
2. Create a service inventory for code, infrastructure, data stores, domains,
   certificates, identities, secrets, integrations, queues, scheduled jobs,
   mobile clients, third parties, dashboards, runbooks, and repositories. Assign
   a named owner and lifecycle state to each.
3. Define support intake, severity, priority, response and restoration targets,
   escalation, on-call coverage, communications, handoffs, after-hours behavior,
   and evidence. Separate incidents, service requests, defects, and problems.
4. Define service-level indicators, objectives, error budgets, user-journey
   measures, logs, traces, metrics, synthetic checks, dashboards, alerts, data
   quality, retention, access, and review cadence.
5. Plan incident detection, triage, containment, recovery, verification,
   communication, evidence preservation, review, and follow-up. Track recurring
   causes through problem management rather than repeatedly treating symptoms.
6. Maintain a vulnerability and dependency process using
   [references/app-maintenance-standard.md](references/app-maintenance-standard.md):
   inventory, advisories, supported versions, patch windows, exploitability,
   testing, exceptions, emergency changes, provenance, and end-of-life dates.
7. Define backup scope, frequency, encryption, retention, immutability, access,
   restore procedure, restore testing, reconciliation, recovery-point objective,
   and recovery-time objective. A completed backup job is not restore evidence.
8. Define data quality, archival, legal hold, retention, deletion, export,
   portability, tenant offboarding, account deletion, and audit controls. Verify
   deletion across replicas, caches, search, files, logs, and vendors as required.
9. Plan capacity and cost using demand drivers, seasonality, quotas, saturation,
   storage growth, queue depth, third-party limits, unit economics, budgets,
   anomaly alerts, and scale-up or scale-down actions.
10. Maintain security, privacy, accessibility, browser and device compatibility,
    localization, performance, and resilience baselines. Re-evaluate them after
    material changes and at a risk-based cadence.
11. Create a prioritized backlog for defects, technical debt, architecture risks,
    operational toil, documentation gaps, upgrades, and product improvements.
    Score impact, exposure, urgency, evidence, effort, reversibility, and the cost
    of delay.
12. Define safe change classes, approvals, testing, deployment, feature flags,
    observation, rollback, maintenance windows, freeze periods, and emergency
    change review. Reuse deployment controls rather than inventing a second path.
13. Maintain runbooks, architecture and data-flow diagrams, ownership, access,
    vendor contacts, recovery procedures, decisions, known errors, and onboarding.
    Exercise critical runbooks and remove instructions that no longer work.
14. Plan vendor and platform lifecycle risk: contracts, service levels, quotas,
    pricing, data export, portability, deprecations, incident history, substitute
    options, and exit triggers.
15. Define quarterly service reviews and annual continuity exercises. Record
    trends, incidents, risks, changes, costs, capacity, control findings, backlog,
    decisions, and accountable follow-up.
16. Define retirement triggers, stakeholder approval, migration, export,
    communication, access revocation, secret rotation, integration shutdown, data
    disposition, infrastructure removal, evidence retention, and final validation.
17. Deliver with
    [assets/app-maintenance-plan-template.md](assets/app-maintenance-plan-template.md).

## Rules

- Do not interpret absence of alerts as evidence of service health.
- Do not close an incident before the business outcome and authoritative state are
  verified.
- Do not defer critical vulnerabilities or unsupported dependencies without a
  named risk owner, compensating controls, expiration, and approval.
- Do not claim recoverability from backup success alone; test restoration.
- Do not retain data indefinitely because ownership or policy is unclear.
- Do not allow emergency changes to become an undocumented normal release path.
- Do not optimize cost by violating service, security, privacy, accessibility, or
  recovery requirements.
- Do not retire a service by merely turning off its user interface.

## Handoff

Provide the service inventory and ownership model, support and incident process,
SLIs and SLOs, observability, maintenance calendar, vulnerability and dependency
plan, backup and restore controls, data lifecycle, capacity and cost plan,
technical-debt backlog, change controls, documentation and exercises, vendor
risks, service-review cadence, retirement plan, risks, and open decisions.

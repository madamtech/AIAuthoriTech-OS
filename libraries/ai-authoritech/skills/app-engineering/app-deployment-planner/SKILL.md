---
name: app-deployment-planner
description: Design safe, repeatable application deployment and release plans covering environments, immutable artifacts, configuration and secrets, infrastructure and database changes, rollout strategy, approvals, observability, verification, rollback or forward-fix, incident response, audit evidence, and ownership. Use before releasing web, mobile, SaaS, internal, API-driven, AI-enabled, or vibe-coded applications - not to perform an unapproved production change, expose credentials, or claim a deployment succeeded without authoritative verification.
---

# App Deployment Planner

Design releases that can be verified, contained, and recovered.

## Procedure

1. Confirm the release outcome, scope, users, service criticality, environments,
   hosting model, dependencies, data sensitivity, maintenance constraints,
   recovery objectives, compliance requirements, and accountable change owner.
2. Inventory the exact source revision, build inputs, dependencies, infrastructure,
   schemas, configuration, feature flags, secrets, domains, certificates,
   integrations, jobs, queues, and mobile or client versions included.
3. Produce one immutable, signed or checksummed artifact and promote it through
   environments. Record provenance and software-component inventory; do not
   rebuild differently for production.
4. Define environment parity and controlled differences. Separate configuration
   from code and secrets from both. Specify secret storage, injection, access,
   rotation, revocation, redaction, and break-glass handling.
5. Choose recreate, rolling, blue-green, canary, feature-flagged, regional, or
   phased rollout using blast radius, statefulness, compatibility, traffic,
   client update behavior, cost, and recovery constraints.
6. Sequence infrastructure, database, API, event, background-worker, cache, search,
   and application changes. Use
   [references/app-deployment-standard.md](references/app-deployment-standard.md)
   for compatibility and rollout rules.
7. Make database and contract changes backward compatible across the rollout
   window. Separate expand, migrate or backfill, switch, verify, and contract.
   Bound long-running work and preserve checkpoints.
8. Define preflight checks and release gates using test evidence, security and
   privacy findings, accessibility results, capacity, backups, restore evidence,
   dependency health, staffing, communications, and change approval.
9. Define deployment commands or pipeline stages, identities, least privilege,
   concurrency locks, timeouts, retries, approvals, evidence, and abort behavior.
   Keep provider-specific instructions in an adapter.
10. Define automated smoke checks and authoritative business verification for
    health, authentication, authorization, writes, reads, integrations,
    reconciliation, jobs, notifications, and critical user journeys.
11. Set rollout observation windows, service-level indicators, alert thresholds,
    error budgets, logs, traces, dashboards, synthetic checks, and named decision
    owners. Compare against a documented baseline.
12. Define rollback and forward-fix triggers, authority, commands, artifact,
    configuration, data compatibility, feature-flag actions, communications, and
    verification. Treat destructive data changes as potentially irreversible.
13. Define failure containment, traffic stop, queue pause, credential revocation,
    incident declaration, escalation, customer communication, and evidence
    preservation.
14. Record actual timestamps, actors, approvals, artifact digests, configuration
    versions, results, deviations, incidents, and final decision. Never replace
    execution evidence with the plan.
15. Deliver with
    [assets/app-deployment-plan-template.md](assets/app-deployment-plan-template.md).

## Guardrails

- Do not deploy or mutate production without explicit authorization.
- Do not place secrets in source control, command history, logs, screenshots,
  tickets, plans, or generated fixtures.
- Do not deploy an artifact whose source and build provenance cannot be identified.
- Do not combine an irreversible data migration with an unproven application
  cutover without containment and recovery controls.
- Do not call a release successful based only on process exit status or HTTP 200.
- Do not improvise rollback after failure; predefine and rehearse it proportionate
  to risk.
- Do not delete the previous working artifact until the recovery window closes.
- Do not bypass a failed gate because the release window is ending.

## Recovery

If artifact provenance, configuration, migration compatibility, approval, or a
release gate cannot be verified, stop promotion and preserve the last known-good
state. On failed verification, contain traffic or work, execute the approved
rollback or forward-fix decision, reconcile authoritative data, and record the
actual outcome before resuming.

## Output Contract

Provide release scope, architecture and dependency inventory, artifact provenance,
environment and secret model, rollout sequence, compatibility plan, gates and
approvals, verification matrix, observability and thresholds, rollback or
forward-fix runbook, incident actions, communications, owners, evidence, and open
decisions.

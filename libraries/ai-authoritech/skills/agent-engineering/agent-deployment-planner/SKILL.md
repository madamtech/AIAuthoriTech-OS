---
name: agent-deployment-planner
description: Convert an approved AI agent release candidate into a controlled, platform-aware deployment plan covering artifacts, environments, configuration, secrets, data migration, access, rollout, verification, monitoring, incident response, rollback, ownership, and post-release review. Use for first releases, upgrades, migrations, staged rollouts, production cutovers, or deployment-readiness reviews - not agent architecture, implementation, QA execution, or production deployment without explicit authorization. Use when asked to (1) plan agent deployment, (2) revise agent deployment, (3) evaluate options for agent deployment, or (4) prepare implementation of agent deployment.
---

# Agent Deployment Planner

Plan a reversible release whose exact artifact, authority, and effects can be
verified.

## Procedure

1. Confirm the approved architecture, QA verdict, unresolved conditions, release
   artifact, configuration fingerprint, platform, risk tier, autonomy tier,
   environments, change window, owners, and business success measures.
2. Stop and return a readiness gap when critical or high-severity defects remain,
   the release artifact differs from the tested candidate, or required ownership
   and rollback capability are absent.
3. Inventory every deployable component: instructions, models, model parameters,
   skills, workflows, tools, credentials, policies, knowledge indexes, memory and
   state stores, schemas, integrations, feature flags, dashboards, and runbooks.
4. Define environment promotion and configuration controls with
   [references/agent-deployment-standard.md](references/agent-deployment-standard.md).
   Keep secrets outside artifacts and prevent unreviewed configuration drift.
5. Define prerequisites, backups, migrations, compatibility checks, access changes,
   dependency sequencing, freeze conditions, and pre-deployment evidence.
6. Select direct, rolling, canary, blue-green, shadow, or feature-flag rollout
   according to consequence, reversibility, traffic, observability, and platform
   capability. Prefer the smallest safe exposure.
7. Define go/no-go gates, accountable approvers, communication, execution steps,
   checkpoints, pause criteria, and evidence captured at every stage.
8. Specify smoke, functional, permission, approval, tool-effect, retrieval,
   workflow-state, safety, latency, cost, and audit verification after deployment.
9. Set quantitative guardrails and rollback triggers. Define automatic versus
   human-authorized rollback, data and external-effect reconciliation, credential
   revocation, traffic restoration, and recovery-time objectives.
10. Define logs, traces, metrics, alerts, sampling, dashboards, on-call ownership,
    incident severity, escalation, kill switch, degraded mode, and support handoff.
11. Plan post-release monitoring, stakeholder confirmation, defect triage,
    retrospective, baseline updates, evidence retention, and release closure.
12. Deliver with
    [assets/agent-deployment-plan-template.md](assets/agent-deployment-plan-template.md).

## Guardrails

- Do not treat a QA recommendation as production authorization.
- Do not deploy or change live infrastructure unless the user explicitly requests
  and authorizes that external action.
- Do not promote an artifact that cannot be immutably identified and reproduced.
- Do not place credentials, tokens, private keys, or sensitive values in the plan,
  repository, logs, or deployment artifact.
- Do not use a rollout strategy that exceeds available observability or rollback
  capability.
- Do not call rollback complete until traffic, state, data, permissions, queued
  work, and external effects are reconciled.
- Do not reuse stale approvals after the artifact, configuration, scope, risk, or
  deployment window changes.
- Separate platform-independent release controls from provider-specific commands.

## Output Contract

Provide the release fingerprint, readiness decision, component and dependency
inventory, environment matrix, rollout runbook, approval gates, verification
matrix, guardrails, rollback and recovery plan, observability and incident model,
communications, ownership, residual risks, and closure criteria.

## Recovery

If the release fingerprint differs from the tested candidate, stop promotion and
require renewed QA. If a rollout guardrail fails, pause exposure, preserve evidence,
and execute the authorized rollback or escalation path. Do not close recovery until
traffic, state, data, permissions, queues, and external effects reconcile.

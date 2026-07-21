---
name: lms-release-manager
description: Coordinate controlled LMS releases for configuration, content, integrations, reports, and operational changes. Use when planning deployment, approvals, testing, communications, rollback, monitoring, and closure across learning environments.
---

# LMS Release Manager

Turn approved changes into a traceable release with explicit go/no-go criteria.

## Workflow

1. Define release scope, owners, environments, dependencies, affected populations, window, freeze periods, and success criteria.
2. Confirm requirements, approvals, build artifacts, version labels, test evidence, security, accessibility, privacy, and support readiness.
3. Sequence deployment steps, data loads, integrations, cache or schedule considerations, and validation checkpoints.
4. Define backups, rollback triggers, rollback steps, decision authority, and recovery time.
5. Coordinate stakeholder and learner communications without exposing unapproved changes.
6. Execute only when authorized, capture timestamps and results, run smoke tests, monitor, and reconcile.
7. Close with known issues, evidence, support handoff, and retrospective actions.

## Output

Provide a release plan, dependency map, readiness checklist, runbook, go/no-go record, rollback plan, communication matrix, validation results, and closure report.

## Guardrails

- Do not deploy without explicit authority.
- Never omit rollback because a change appears small.
- Preserve configuration and data evidence before release.
- Stop when critical validation fails.


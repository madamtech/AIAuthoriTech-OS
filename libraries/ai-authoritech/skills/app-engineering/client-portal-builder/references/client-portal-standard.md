# Client Portal Standard

## Boundary model

Resolve every request through authenticated identity, active membership, tenant,
resource, action, and contextual policy. Apply the same boundary to database
queries, object storage, search, caches, background jobs, exports, logs,
notifications, analytics, and support tooling.

## Portal journeys

For each journey define trigger, actor, prerequisites, authoritative systems,
steps, alternate and failure paths, permissions, data, notifications, evidence,
completion, recovery, and support. Include:

- invitation, onboarding, and organization administration;
- projects, milestones, tasks, requests, and deliverables;
- documents, messages, approvals, scheduling, and feedback;
- billing and usage views;
- support, export, account closure, and offboarding.

## Information architecture and states

Design navigation around client jobs rather than internal department structure.
Every capability must define loading, empty, normal, long-content, high-volume,
partial, stale, unavailable, unauthorized, expired-session, validation, conflict,
success, and recovery states as applicable.

## Sensitive features

- Files: scan, classify, authorize, version, expire, retain, delete, and audit.
- Approvals: bind actor, authority, artifact version, decision, time, and effect.
- Commerce: display reconciled state and use approved hosted payment interfaces.
- Support access: require reason, approval where needed, time limit, visibility,
  least privilege, and audit.
- Notifications: avoid sensitive content, honor preferences, and reconcile delivery
  separately from business completion.

## Verification

Test tenant isolation, multi-organization users, role changes, revoked invitations,
direct-object access, storage and search boundaries, expired sessions, support
impersonation, stale data, duplicate webhooks, file threats, approval version
changes, failed notifications, upstream outages, export, deletion, responsive
behavior, keyboard use, assistive technology, and recovery.

## Evidence

Trace portal requirements to journey, source, permission, test, release, and owner.
Retain audit evidence without secrets or unnecessary client content. Distinguish
planned, implemented, executed, reconciled, and approved states.

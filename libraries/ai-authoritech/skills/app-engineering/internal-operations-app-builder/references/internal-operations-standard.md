# Internal Operations App Standard

## Work-item contract

Every work item needs a stable ID, type, requester or source, owner, current state,
priority rationale, service clock, due time, assignment, related records,
sensitivity, permissions, evidence, history, outcome, retention, and source-of-
truth references.

## State and service clocks

Define allowed transitions and effective timestamps. Separate processing, waiting,
blocked, paused, and completed time. State which conditions pause a service clock,
who may apply them, required evidence, expiration, and escalation. Never rewrite
history to improve attainment.

## Queue integrity

Define eligibility, ordering, priority, capacity, reservation, lease expiration,
concurrency, duplicate protection, reassignment, unavailable worker, aging,
escalation, and recovery. Ensure urgent work cannot starve ordinary work
indefinitely and one operator cannot unknowingly overwrite another.

## Controls and approvals

Map each control to its risk and evidence. Define authority, monetary or risk
threshold, separation of duties, delegation, override, appeal, expiration, audit,
and compensating controls. Test unauthorized, self-approval, stale evidence, and
changed-record scenarios.

## Automation

For each automated step define trigger, inputs, authority, rule or model, output,
confidence, human review, idempotency, timeout, retry, external effect, monitoring,
fallback, override, reconciliation, and owner. Track false positives, false
negatives, exceptions, and downstream harm—not only automation rate.

## Verification

Test duplicate and concurrent intake, invalid data, queue ordering, service-clock
boundaries, reassignment, expired approvals, separation of duties, bulk actions,
role and resource isolation, integration delays, partial effects, retries,
reconciliation, AI fallback, migration counts, accessibility, recovery, export,
retention, and deletion.

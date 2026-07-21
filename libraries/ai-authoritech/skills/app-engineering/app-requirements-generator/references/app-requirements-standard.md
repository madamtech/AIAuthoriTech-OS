# App Requirements Standard

## Requirement quality

Every requirement must be:

- Necessary and linked to an outcome, control, or constraint
- Atomic and independently testable
- Clear about actor, trigger, behavior, object, and condition
- Consistent with scope and other requirements
- Feasible enough for planning
- Traceable to evidence and acceptance tests
- Technology-neutral unless technology is an approved constraint

Use stable IDs: `FR-###`, `BR-###`, `DATA-###`, `AUTH-###`, `INT-###`, and
`NFR-###`.

## Functional requirement form

`When [trigger/precondition], the system shall [observable behavior] for [actor or
resource] so that [outcome], subject to [rule or constraint].`

Separate user intent from system response and external effect. Add alternate and
failure behavior where the main statement would otherwise be incomplete.

## Acceptance criteria

Use scenarios:

- Given the relevant state and authority
- When the actor or event triggers behavior
- Then observable results and external effects occur
- And required data, audit, notification, or state changes are verified

Include denied and failure paths for consequential capabilities.

## Nonfunctional measures

Define population, conditions, percentile or rate, threshold, measurement window,
and evidence source. Examples:

- Accessibility target and supported assistive technology
- Response and end-to-end latency by user journey
- Availability, recovery time, and recovery point
- Concurrent users, transaction volume, storage growth, and quotas
- Security and privacy controls with verification
- Browser, device, language, and region support
- Log, metric, trace, and audit coverage
- Cost budget by user, transaction, or period

## Prioritization

Classify release scope as:

- **Must:** Release cannot achieve its outcome or satisfy a mandatory control
  without it.
- **Should:** High value or risk reduction with a tolerable temporary workaround.
- **Could:** Useful but not required for the release outcome.
- **Later or rejected:** Explicitly excluded from the current commitment.

Priority is not a substitute for dependency order or accountable scope approval.

## Review checks

Find duplicated or conflicting requirements, undefined terms, hidden actors,
missing permissions, missing data ownership, absent error and recovery states,
unbounded integrations, unverifiable qualities, implementation bias, orphaned
acceptance tests, and requirements with no evidence or decision owner.

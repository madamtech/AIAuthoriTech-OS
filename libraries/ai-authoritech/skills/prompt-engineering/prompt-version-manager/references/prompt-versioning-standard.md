# Prompt Versioning Standard

## Semantic change rules

- **Patch:** Fix a defect without intentionally expanding or breaking the
  approved contract. Existing valid inputs, outputs, authority, tools, consumers,
  and adapters remain compatible and regression evidence confirms it.
- **Minor:** Add backward-compatible behavior, optional inputs or outputs, a new
  supported adapter, or measurable improvement without breaking existing approved
  consumers. Consumers may adopt deliberately within the same major line.
- **Major:** Remove or redefine behavior; change authority, required inputs,
  output schema, tools or side effects, safety or data boundaries, error semantics,
  platform guarantees, or compatibility in a way that requires consumer action.

Pre-release labels indicate maturity, not compatibility. Build metadata identifies
an artifact but does not replace a release version. Documentation-only edits may
avoid a behavioral version only when the versioned artifact bytes and runtime
behavior are unchanged and the audit record still captures the correction.

## Compatibility and evidence

Define compatibility for the whole release unit, including canonical prompt,
adapters, model ranges, schemas, tools, parameters, knowledge interfaces, tests,
and consumers. Use explicit version pins for exact behavior and bounded ranges
only where regression evidence supports them. A provider's moving alias is not an
immutable compatibility target.

## Release and recovery

Release records must link exact artifacts, approvals, tests, QA verdict, consumer
impact, migration, channel gates, rollout, monitoring, and rollback. Rollback must
restore all coupled components and verify traffic and consumers, not merely copy
old prompt text. Deprecation never means deletion: preserve discovery, evidence,
aliases, and audit history according to retention and access policies.

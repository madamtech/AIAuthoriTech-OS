---
name: prompt-version-manager
description: Govern immutable prompt and adapter versions through semantic change classification, dependency and consumer impact analysis, compatibility ranges, release channels, migration, staged rollout, monitoring, rollback, deprecation, and audit history. Use when proposing, approving, releasing, reverting, superseding, or retiring a prompt version or when a model, tool, schema, policy, knowledge interface, or platform change may invalidate compatibility. Do not author prompt behavior, overwrite released artifacts, or treat a repository commit alone as a governed release.
---

# Prompt Version Manager

Make every behavioral release identifiable, testable, reversible, and traceable.

1. Obtain the stable prompt identity and SKU, current immutable version, canonical
   artifact, adapters, owners, approval policy, consumers, dependencies, test and
   QA evidence, deployment states, release channels, and support commitments.
2. Capture the proposed diff across instructions, authority, variables, schemas,
   tools, knowledge interfaces, adapters, parameters, metadata, and operations.
   Separate behavioral changes from documentation-only corrections.
3. Classify impact using
   [references/prompt-versioning-standard.md](references/prompt-versioning-standard.md).
   Choose patch, minor, or major based on observable contract compatibility—not
   line count, effort, urgency, or author preference.
4. Treat changes to task scope, authority, prohibited actions, required inputs,
   output schema, tool side effects, data handling, failure behavior, or removed
   support as potentially breaking until evidence proves compatibility.
5. Map every direct and transitive consumer: apps, agents, workflows, adapters,
   templates, tests, automations, integrations, clients, and deployed environments.
   Record pinned versions, compatible ranges, owners, and migration constraints.
6. Define the exact release unit: canonical prompt, adapter set, schemas, tests,
   runtime configuration, knowledge compatibility, documentation, and rollback
   artifact. Hash or immutably reference every component.
7. Require affected regression, holdout, adapter, safety, privacy, authority,
   schema, cost, and latency evidence. Route testing to Prompt Tester and approval
   to Prompt QA Reviewer; do not self-certify an unreviewed behavioral change.
8. Select a release channel: experimental, alpha, beta, stable, or enterprise.
   Define entry and exit gates, permitted consumers, support level, monitoring,
   and promotion authority for the channel.
9. Produce consumer-specific migration instructions, compatibility windows,
   feature flags or cohort controls, data or schema changes, training, validation,
   and deadlines. Do not force automatic major-version upgrades.
10. Stage rollout with explicit cohorts, success metrics, observation periods,
    pause conditions, rollback triggers, decision owners, and communication paths.
11. Publish a release record and update the library catalog atomically enough to
    avoid an artifact being selectable before its evidence, compatibility, and
    status are visible. Preserve prior releases and aliases.
12. Monitor real-world quality, safety, privacy, tool effects, cost, latency,
    drift, overrides, and support incidents against baseline. Record exposure by
    exact version and adapter.
13. Roll back to a tested immutable artifact when a trigger fires. Preserve
    incident evidence; do not overwrite the failed release or reuse its number.
14. Deprecate with replacement, affected consumers, notice, support end, migration
    deadline, exception handling, retention, restoration, and archive rules.
15. Deliver with [assets/prompt-release-record-template.md](assets/prompt-release-record-template.md).

## Rules

- Do not mutate or delete a released prompt, adapter, schema, test suite, or
  runtime configuration in place.
- Do not use a patch release for an incompatible output, input, authority, safety,
  tool, or failure-behavior change.
- Do not infer compatibility because tests passed on one model, adapter, language,
  segment, or consumer.
- Do not expose credentials, personal records, confidential prompts, production
  payloads, hidden tests, or private reasoning in release notes or diffs.
- Do not promote a release channel without its defined evidence and authorized
  approval; age or usage volume alone is insufficient.
- Do not mark rollback complete until routing, caches, adapters, schemas, and
  consumers are verified on the restored version.
- Do not recycle version numbers, SKUs, system IDs, release tags, or deprecated
  aliases.

## Handoff

Provide identity and current state, exact proposed diff, semantic version decision,
release unit manifest, dependency and consumer impact, compatibility ranges,
test and QA evidence, release channel, migration instructions, rollout and
monitoring, rollback artifact and triggers, communications, catalog updates,
deprecation or support policy, risks, assumptions, and approval events.

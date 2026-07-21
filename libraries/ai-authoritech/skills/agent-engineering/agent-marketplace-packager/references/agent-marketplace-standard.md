# Agent Marketplace Standard

## Package manifest

Include:

- Package SKU, asset ID, name, version, maturity, status, owner, and release channel
- Agent, instructions, skills, workflows, knowledge, memory schema, tools, adapters,
  templates, policies, evaluations, and documentation with exact versions
- Supported platforms, models, regions, languages, environments, and compatibility
- Required and optional dependencies with licenses, costs, owners, and update policy
- Integrity hashes or other immutable identifiers where supported

## Claim evidence

Classify claims as:

- **Demonstrated:** Reproduced on the packaged release candidate with representative
  evidence.
- **Observed:** Seen in limited field use with disclosed scope and sample.
- **Designed:** Supported by architecture but not yet behaviorally demonstrated.
- **Planned:** Not included in the current release.

Only demonstrated and appropriately scoped observed claims belong in primary
marketplace copy. State test conditions, limitations, and date for quantitative
claims.

## Required disclosures

Disclose:

- Intended and prohibited uses
- Autonomy and required human approvals
- Requested permissions and why each is necessary
- Data categories, flows, storage, memory, logs, retention, deletion, and sharing
- Models, vendors, subprocessors, connectors, and external service costs
- Known limitations, failure modes, safety boundaries, and user responsibilities
- Support hours, service expectations, update policy, and end-of-support terms

## Release channels

- **Experimental:** Exploration; no production assurance.
- **Alpha:** Internal or tightly controlled validation.
- **Beta:** Functional with limited users and active feedback.
- **Production:** Approved for the documented scope with representative evidence.
- **Enterprise proven:** Repeated field evidence, operational history, governance,
  support, and contractual readiness.

Channel labels do not replace security, privacy, legal, or customer approval.

## Package tests

Test a clean installation with no developer-only state. Verify manifest integrity,
dependency resolution, minimum permissions, configuration failures, onboarding,
sample tasks, evaluation claims, data disclosures, telemetry, entitlement limits,
updates, migration, rollback, downgrade, credential revocation, uninstall, data
export, and deletion.

## Lifecycle

Use semantic versioning and publish material changes to behavior, authority, data
practice, dependencies, limitations, and compatibility. Define security-response
timelines, supported versions, migration windows, deprecation notices, customer
export, end of sale, end of support, and final data disposition.

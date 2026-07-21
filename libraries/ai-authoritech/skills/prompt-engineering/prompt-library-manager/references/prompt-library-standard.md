# Prompt Library Standard

## Required record

| Field | Rule |
|---|---|
| SKU | Permanent business and asset-type identifier; never reused |
| System ID | Stable namespaced capability identity |
| Version | Exact semantic version of the registered artifact |
| Purpose | One bounded job and intended outcome |
| Business and library | Valid registry references |
| Owner and steward | Accountable people or roles, not an AI model |
| Status and maturity | Separate lifecycle and evidence-backed maturity values |
| Canonical artifact | Immutable or version-pinned repository location |
| Data class and access | Sensitivity, permitted audiences, retention, and handling |
| Compatibility | Supported models, adapters, tools, schemas, and ranges |
| Relationships | Valid typed links to assets and consumers |
| Evidence | Tests, QA verdict, approvals, proven-use claims, and review dates |

## Duplicate decision

Compare task, inputs, authority, decisions, outputs, tools, schema, users, risk,
and acceptance criteria. Similar wording with a different contract is not a
duplicate. Different wording with the same contract may be. Prefer an adapter
when only platform syntax differs, a new version when the same asset evolves, a
variant when an approved scope intentionally diverges, and a new capability when
the contract performs a materially different job.

## Lifecycle controls

Every transition must cite authorization and evidence. Released assets require
an owner, approved exact version, supported consumers, test and QA references,
access classification, monitoring or review cadence, and rollback or replacement
path. Deprecated assets remain discoverable but cannot be selected by default.
Archived assets remain auditable under retention and access policy.

Audit the library for uniqueness, referential integrity, valid registries, path
existence, lifecycle consistency, review freshness, orphaned consumers, and
deprecated dependencies. Correct metadata only from authoritative evidence; log
uncertain discrepancies instead of guessing.

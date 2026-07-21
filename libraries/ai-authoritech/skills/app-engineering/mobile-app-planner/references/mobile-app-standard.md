# Mobile App Standard

## Platform selection

| Approach | Prefer when | Main tradeoff |
|---|---|---|
| Native | Deep platform integration or maximum platform fidelity is essential | Separate codebases and release work |
| Cross-platform | Shared product behavior outweighs a small set of native adapters | Framework and plugin lifecycle |
| Progressive web app | Linkability and web delivery matter more than full device capability | Platform-specific feature limitations |
| Hybrid | Existing web assets can be safely reused behind native boundaries | Performance, accessibility, and bridge complexity |

Validate required capabilities and store policies against current primary sources
before committing to a framework.

## Offline and synchronization

Classify each capability as online-only, offline-readable, offline-draft, or
offline-committable. For writes, define local operation ID, device and user,
authoritative resource, base version, timestamp semantics, ordering, dependency,
idempotency, retry, expiration, conflict rule, user resolution, reconciliation,
and evidence. Never use last-write-wins without documenting acceptable data loss.

## Permission design

Request at point of use. Explain purpose, scope, duration, and benefit. Support
not-determined, granted, denied, limited, restricted, and revoked states. Provide
a functional fallback where the permission is not essential and a clear settings
recovery path where it is.

## Client version compatibility

Maintain backward-compatible APIs and data migrations across the supported client
window. Define minimum supported version, deprecation notice, optional and
required-update criteria, outage behavior, and user recovery. Account for delayed
store approval and users who disable automatic updates.

## Verification

Test real devices across supported OS versions, sizes, accessibility settings,
locales, time zones, network types, storage and memory pressure, battery states,
permissions, backgrounding, termination, upgrades, offline conflicts, deep links,
notification actions, security boundaries, and crash recovery.

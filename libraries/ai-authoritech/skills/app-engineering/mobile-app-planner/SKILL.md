---
name: mobile-app-planner
description: Create build-ready plans for native, cross-platform, or installable mobile applications covering device journeys, platform choice, navigation, responsive and adaptive UX, accessibility, local storage, offline behavior, synchronization, permissions, sensors, notifications, deep links, security, privacy, performance, battery, testing, signing, store delivery, phased rollout, telemetry, updates, and support. Use for consumer, workforce, field, companion, or mobile-first apps—not to claim store approval, collect unnecessary device data, or deploy unsigned or unverified builds.
---

# Mobile App Planner

Design for interruption, constrained devices, denied permissions, and old clients.

1. Confirm the mobile outcome, users, contexts, supported devices and operating
   systems, environments, accessibility, connectivity, regions, data sensitivity,
   risk, success measures, budget, and owners.
2. Define why a mobile app is needed instead of a responsive web app. Identify
   required device capabilities, offline work, background behavior, notifications,
   store distribution, and installation or retention assumptions.
3. Choose native, cross-platform, progressive web, or hybrid architecture using
   [references/mobile-app-standard.md](references/mobile-app-standard.md). Record
   platform reach, capability gaps, accessibility, performance, team skills,
   testing, release independence, maintenance, cost, and exit path.
4. Map mobile journeys with entry source, authentication state, permission state,
   connectivity, interruption, backgrounding, termination, resume, cancellation,
   and verified completion.
5. Define navigation, universal or deep links, back behavior, tabs, modals,
   gestures, orientation, safe areas, keyboard, dynamic type, zoom, reflow,
   screen-reader order, focus, contrast, motion, haptics, and alternatives.
6. Define local data, cache, encrypted secrets, files, schema version, retention,
   storage pressure, logout, account switch, device compromise, backup behavior,
   migration, and deletion.
7. Define offline-readable and offline-writable capabilities. Assign source of
   truth, local operation ID, ordering, idempotency, queue, retry, conflict,
   tombstone, reconciliation, stale indicators, user resolution, and recovery.
8. Request camera, photos, microphone, location, contacts, calendar, Bluetooth,
   biometrics, motion, or notifications only at the moment of value. Define
   purpose, minimum scope, denial, limited access, revocation, settings recovery,
   retention, and non-permission fallback.
9. Define notification eligibility, consent, token lifecycle, environment,
   categories, actions, content sensitivity, quiet hours, localization, collapse,
   deduplication, deep-link destination, delivery telemetry, and in-app state.
10. Define authentication, account recovery, secure session and token storage,
    device binding where justified, biometrics as local convenience, tenant and
    resource authorization, compromised-device posture, and sensitive-screen
    protections.
11. Define APIs, upload and download, pagination, background transfer, timeouts,
    compression, retry, cellular policy, metered network, third-party SDKs,
    certificate handling, and backward-compatible contracts.
12. Define cold and warm start, interaction latency, memory, battery, network,
    storage, crash, hang, background execution, and package-size budgets with
    device-class evidence.
13. Test supported OS and device combinations, accessibility, permissions,
    interruptions, offline transitions, clock and time zones, low storage, low
    memory, poor networks, upgrades, migration, deep links, notifications,
    concurrency, security, localization, battery, and recovery on real devices.
14. Plan signing identities, secure build pipeline, environment configuration,
    privacy disclosures, store metadata, screenshots, review credentials,
    support links, phased rollout, remote flags, crash monitoring, rollback or
    forward-fix, forced-update policy, and minimum supported version.
15. Define privacy-preserving analytics, crash and performance telemetry, consent,
    redaction, retention, access, app health, adoption, successful journeys,
    notification value, support, reviews, and update compliance.
16. Deliver with
    [assets/mobile-app-plan-template.md](assets/mobile-app-plan-template.md).

## Rules

- Do not request a device permission before explaining and demonstrating its
  immediate value.
- Do not place secrets or trusted authorization logic in the client bundle.
- Do not treat local biometric success as server-side identity authorization.
- Do not silently overwrite offline edits or duplicate external effects.
- Do not assume notification delivery, background execution, or store review
  timing is guaranteed.
- Do not block all older clients without a compatibility and user-recovery plan.
- Do not log tokens, precise location, sensitive content, or unnecessary device
  identifiers.
- Do not claim mobile readiness from emulator or simulator testing alone.

## Handoff

Provide the mobile charter, platform decision, journey and interruption map,
navigation and accessibility, local data and offline synchronization, device
permissions, notifications and links, security, API contracts, performance and
resource budgets, device test matrix, signing and store release, telemetry,
support, risks, assumptions, and open decisions.

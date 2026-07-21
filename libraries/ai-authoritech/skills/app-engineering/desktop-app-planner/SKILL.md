---
name: desktop-app-planner
description: Create build-ready plans for Windows, macOS, Linux, or cross-platform desktop applications covering architecture, native integration, windows and navigation, accessibility, local files and databases, offline behavior, IPC, privileged operations, security, performance, packaging, code signing, installation, updates, enterprise distribution, testing, telemetry, support, and retirement. Use for productivity, creative, internal, companion, tray, kiosk, or device-integrated desktop software—not to run untrusted code with elevated privileges, ship unsigned artifacts, or claim OS compatibility without representative-device evidence.
---

# Desktop App Planner

Design for long-lived processes, local authority, operating-system differences,
and recoverable installation and updates.

1. Confirm the outcome, users, workflows, supported operating systems and
   versions, device classes, peripherals, environments, accessibility, data
   sensitivity, connectivity, enterprise controls, distribution, success
   measures, budget, and owners.
2. Establish why a desktop application is needed instead of a web or mobile app.
   Identify local files, hardware, background work, offline use, performance,
   windowing, system integration, enterprise deployment, and update requirements.
3. Choose native, cross-platform native, webview-based, or packaged web
   architecture using
   [references/desktop-app-standard.md](references/desktop-app-standard.md).
   Record OS fidelity, capability gaps, runtime size, accessibility, performance,
   team skills, security boundary, testing, maintenance, and exit path.
4. Define processes and trust boundaries for the UI, application core, plugins,
   renderers, background services, update helper, shell integration, privileged
   helper, local API, and remote services. Minimize exposed IPC and privileges.
5. Map launch, first run, sign-in, open-with, deep link, multiple instance,
   window restore, minimize, tray or menu-bar, sleep, wake, lock, shutdown,
   crash, upgrade, and uninstall journeys.
6. Define windows, navigation, menus, shortcuts, focus order, keyboard-only use,
   screen readers, scaling, high contrast, reduced motion, localization, input
   methods, multi-monitor behavior, and OS-conventional interaction.
7. Define file selection, drag and drop, recent files, autosave, atomic writes,
   recovery copies, file locking, external modification, conflict handling,
   schema or document migration, import, export, backup, and safe deletion.
8. Define local database and cache ownership, encryption, key storage, retention,
   account switching, OS-user separation, roaming, storage pressure, corruption
   detection, repair, migration, synchronization, and authoritative state.
9. Define OS integration for protocols, file associations, notifications,
   clipboard, global shortcuts, share targets, search, startup, shell extensions,
   printers, cameras, microphones, serial or USB devices, and accessibility.
   Make each integration optional and permission-aware where possible.
10. Define IPC message schemas, origin and caller validation, authorization,
    serialization limits, timeouts, cancellation, idempotency, replay defense,
    rate limits, versioning, logging, and safe error responses.
11. Isolate document parsers, previews, plugins, extensions, scripts, and other
    untrusted content. Define sandboxing, capability grants, signing, provenance,
    update controls, resource quotas, failure containment, and removal.
12. Define authentication, session storage, tenant and resource authorization,
    secure secret storage, certificate validation, proxy support, device posture
    where justified, logout, account recovery, and sensitive-screen protections.
13. Set cold and warm start, interaction latency, CPU, memory, GPU, disk, network,
    energy, background activity, installer, and package-size budgets. Measure
    idle as well as active behavior on representative hardware.
14. Plan deterministic builds, dependency inventory, artifact provenance, code
    signing, notarization where applicable, installer format, install scope,
    elevation, side-by-side versions, repair, uninstall, residual data, and
    license compliance.
15. Define stable, beta, and enterprise channels; update discovery; signed
    manifests and packages; staged rollout; compatibility; migration; download
    recovery; restart behavior; rollback or forward-fix; minimum version; and
    emergency revocation.
16. Test OS and hardware combinations, clean install, upgrade, downgrade policy,
    repair, uninstall, accessibility, localization, scaling, multiple monitors,
    sleep and resume, offline transitions, proxies, low disk, corrupted state,
    files, devices, IPC abuse, untrusted content, performance, and recovery.
17. Define privacy-preserving logs, crash reports, performance telemetry, consent,
    redaction, retention, access, diagnostics export, support bundles, health
    thresholds, incident response, compatibility support, and end-of-life.
18. Deliver with
    [assets/desktop-app-plan-template.md](assets/desktop-app-plan-template.md).

## Rules

- Do not run the primary application with administrator or root privileges.
- Do not expose a privileged helper without a narrow, authenticated, authorized,
  versioned, and auditable command surface.
- Do not enable webview-to-native capabilities for untrusted origins or content.
- Do not deserialize, preview, or execute untrusted files or plugins without
  containment and resource limits.
- Do not store tokens, encryption keys, or signing material in source code,
  plaintext configuration, logs, or update packages.
- Do not distribute an unsigned installer or accept an update whose signature,
  provenance, channel, and version are not verified.
- Do not silently overwrite user files or remove user data during uninstall.
- Do not claim desktop readiness from one OS, one display scale, or one machine.

## Handoff

Provide the desktop charter, platform decision, process and trust-boundary model,
journeys and window behavior, accessibility, local files and data, OS integration,
IPC and privilege model, untrusted-content controls, security, performance
budgets, packaging and signing, distribution and updates, test matrix, telemetry,
support and retirement, risks, assumptions, and open decisions.

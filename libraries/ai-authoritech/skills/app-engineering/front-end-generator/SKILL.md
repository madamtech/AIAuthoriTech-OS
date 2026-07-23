---
name: front-end-generator
description: Convert approved application requirements, user journeys, design contracts, content, data contracts, and authorization rules into bounded front-end implementation packets and code changes covering semantic structure, components, routes, state, forms, responsive behavior, accessibility, localization, performance, security, analytics, tests, and verification. Use when implementing or planning a web, mobile-web, desktop-webview, portal, dashboard, SaaS, or vibe-coded interface - not to invent material product rules, enforce authorization only in the client, expose secrets, overwrite approved design, or claim production readiness from a visual preview.
---

# Front-End Generator

Build one verified user-facing slice at a time.

## Procedure

1. Confirm whether the request authorizes a plan, generated implementation packet,
   or edits to an existing codebase. Preserve unrelated user changes and approved
   features, branding, content, routes, and component contracts.
2. Gather approved requirements, acceptance criteria, journeys, design system,
   content, responsive behavior, accessibility target, data and API contracts,
   authentication and authorization rules, analytics, supported clients,
   framework constraints, and files in scope.
3. Identify missing material inputs and conflicts. Label reversible assumptions;
   stop for decisions that change business rules, access, data sensitivity,
   destructive behavior, legal claims, scope, or architecture authority.
4. Define a vertical slice with entry state, user outcome, terminal state,
   included requirements, excluded work, protected decisions, dependencies,
   files, components, routes, and observable acceptance evidence.
5. Map semantic page regions, heading structure, navigation, landmarks, content
   order, component boundaries, ownership, composition, variants, and reuse using
   [references/front-end-generation-standard.md](references/front-end-generation-standard.md).
6. Define default, loading, skeleton, empty, success, warning, validation error,
   system error, denied, partial, offline, stale, retry, timeout, cancellation,
   conflict, and destructive-action states as applicable.
7. Define data flow by source of truth, server state, local UI state, URL state,
   form state, cache, optimistic change, invalidation, pagination, concurrency,
   cancellation, retry, idempotency, reconciliation, and authoritative completion.
8. Render permissions for clarity but rely on server and data-layer enforcement.
   Handle unauthenticated, unauthorized, expired, revoked, and cross-tenant cases
   without leaking resource existence or sensitive data.
9. Implement semantic native elements first. Define keyboard order, focus entry
   and return, labels, instructions, errors, announcements, contrast, zoom,
   reflow, touch targets, reduced motion, and alternatives for non-text content.
10. Define responsive and adaptive behavior from content priority and tasks:
    navigation changes, stacking, table and chart alternatives, density, pointer
    and keyboard support, safe areas, long text, localization, and printing.
11. Validate input at the appropriate boundary, preserve user input after errors,
    make destructive actions deliberate and recoverable, and communicate actual
    system state rather than assuming a click or successful request completed the
    business outcome.
12. Keep secrets and trusted logic off the client. Treat browser storage, URLs,
    source maps, analytics, logs, error reports, HTML, downloads, and third-party
    scripts as potential disclosure surfaces.
13. Set budgets for initial and route payload, images, fonts, requests, rendering,
    interaction latency, layout stability, memory, and low-end devices. Choose
    server, static, streamed, or client rendering based on the user path and data.
14. Implement tests for behavior and contracts: unit, component, accessibility,
    visual states, responsive views, integration, and a focused end-to-end path.
    Use realistic synthetic data covering long, missing, zero, large, invalid,
    internationalized, and sensitive-value cases.
15. Run applicable format, type, lint, unit, component, build, accessibility,
    browser, responsive, and end-to-end checks. Inspect actual rendered behavior,
    network calls, console errors, focus, data, access, and external effects.
16. Report changed files, requirements covered, assumptions, dependencies,
    commands and results, screenshots or evidence, limitations, regressions,
    follow-up work, and any unverified claim.
17. Deliver with
    [assets/front-end-implementation-packet.md](assets/front-end-implementation-packet.md).

## Guardrails

- Do not begin implementation from a visual reference when behavior, data, access,
  and acceptance requirements are materially unknown.
- Do not place secrets, service credentials, trusted authorization, or sensitive
  fixtures in the client bundle or public environment variables.
- Do not hide a control and call the underlying action authorized.
- Do not use a generic clickable element when a native semantic control fits.
- Do not make color, position, icons, hover, drag, or motion the sole carrier of
  meaning or interaction.
- Do not add dependencies, global state, abstractions, design patterns, or custom
  components without a demonstrated need and ownership boundary.
- Do not overwrite approved design, copy, routes, components, or unrelated code
  outside the bounded slice.
- Do not claim completion from a screenshot, rendered page, HTTP success, or green
  unit tests without verifying the acceptance outcome and authoritative state.

## Recovery

If requirements, access rules, protected design decisions, or authoritative data
behavior conflict, stop the affected slice and preserve unrelated user changes.
Reconcile source contracts before editing, restore the last verified UI and data
state after a failed optimistic action, and report any unverified acceptance
claim rather than hiding it behind a visual result.

## Output Contract

Provide the authority and source contracts, slice scope, page and component map,
state and data model, access behavior, responsive and accessibility contract,
security and performance controls, implementation prompt or changed files, test
and verification evidence, protected decisions, assumptions, limitations, and
next authorized slice.

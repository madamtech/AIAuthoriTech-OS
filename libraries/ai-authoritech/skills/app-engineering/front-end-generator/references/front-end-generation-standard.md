# Front-End Generation Standard

## Slice contract

Every front-end slice must identify:

- requirement and acceptance IDs;
- actor, entry, outcome, and verified terminal state;
- routes, pages, components, data, and files in scope;
- server, URL, form, and local state ownership;
- access rules and server-enforced contracts;
- all required UI and failure states;
- responsive, accessibility, localization, security, and performance conditions;
- protected decisions and prohibited changes;
- tests, commands, evidence, reset, and recovery.

## Component decisions

Create a component when it has a stable responsibility, semantic role, reusable
interaction, state boundary, or design-system contract. Prefer composition over
large option-heavy components. Keep page-specific orchestration near the page and
domain logic outside purely presentational components.

Do not abstract similar markup when the items have different business meaning,
change reasons, access rules, or state models.

## State ownership

- Keep durable business data authoritative on the server or approved data layer.
- Put shareable navigation and filter state in the URL when appropriate.
- Keep transient interaction state local to the smallest owning component.
- Treat server cache separately from client UI state.
- Define stale behavior, cancellation, retries, invalidation, concurrent edits,
  optimistic updates, rollback, and reconciliation.
- Confirm completion from the authoritative business state for external effects.

## Accessibility contract

Use native semantics, logical DOM and reading order, visible focus, keyboard
operation, explicit labels and instructions, programmatic error association,
status announcements, sufficient contrast, zoom and reflow, reduced motion,
target size, non-text alternatives, and accessible authentication.

For dialogs, menus, tabs, grids, comboboxes, drag and drop, charts, and custom
controls, define keyboard model, roles, states, focus movement, announcements,
escape or cancellation, and a simpler fallback. Test with keyboard and relevant
assistive technology; automated scans are supporting evidence only.

## Security and privacy

Assume all client code, requests, storage, URLs, source maps, and rendered data are
inspectable. Enforce authorization server-side. Avoid unsafe HTML, untrusted URL
schemes, open redirects, token exposure, sensitive analytics, permissive third-
party scripts, and unnecessary browser storage. Redact user-visible and captured
errors while retaining a safe correlation ID.

## Performance

Define budgets per critical journey. Measure representative devices and networks.
Control JavaScript and dependency weight, route splitting, rendering work, image
and font delivery, request waterfalls, caching, prefetching, layout shifts, long
tasks, memory, list virtualization, and third-party impact. Do not optimize a
metric by breaking accessibility, correctness, privacy, or maintainability.

## Verification

Verify source requirements, type and build integrity, component behavior,
keyboard and focus, accessibility, responsive layouts, long and localized content,
data and authorization, loading and failure states, console and network behavior,
performance budgets, analytics consent, and the end-to-end business outcome.
Record commands, versions, environment, result, and retained evidence.

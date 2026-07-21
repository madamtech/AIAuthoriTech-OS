# UI/UX Prompt Standard

## Prompt layers

Write prompts in this order:

1. User, outcome, journey, and scope
2. Requirements and protected constraints
3. Information architecture and content hierarchy
4. Layout and visual system
5. Components and data
6. Interaction and system states
7. Responsive behavior
8. Accessibility behavior
9. Tool-specific implementation instructions
10. Acceptance and review criteria

## Observable visual direction

Replace vague adjectives with concrete choices. Define typography roles and scale,
spacing rhythm, grid, density, color functions, contrast, border and radius logic,
imagery treatment, icon style, motion purpose, and component hierarchy.

Use brand tokens when supplied. If they are absent, label proposed tokens rather
than presenting them as approved branding.

## State completeness

For every interactive capability consider:

- Default, focus, hover, active, selected, and disabled
- Loading, skeleton, empty, success, warning, and error
- Validation, denied, timeout, partial, offline, retry, cancel, and undo
- Confirmation for consequential or destructive actions
- Long content, missing content, large values, and high data volume

The interface must not claim success before the underlying operation is verified.

## Responsive contract

Describe what changes and why across viewport and input modes. Preserve task
priority, readable line length, visible focus, reachable controls, minimum touch
targets, usable tables, non-clipped dialogs, and zoom behavior.

## Accessibility contract

Require semantic structure, keyboard operation, visible focus, programmatic names,
instructions and errors, contrast, screen-reader status announcements, focus
placement after navigation and dialogs, reduced-motion support, text alternatives,
and accessible authentication and recovery.

## Review

Validate against requirements at representative widths and content extremes.
Inspect keyboard flow, focus, semantics, contrast, zoom, state changes, error
recovery, realistic data, brand tokens, protected design decisions, and unintended
regressions. Visual attractiveness alone is not acceptance.

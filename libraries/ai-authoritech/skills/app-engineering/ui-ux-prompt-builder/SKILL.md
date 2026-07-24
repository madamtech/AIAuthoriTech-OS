---
name: ui-ux-prompt-builder
description: Translate approved product requirements, user journeys, brand guidance, content, and technical constraints into precise UI/UX prompts for AI design and coding tools, covering information architecture, layout, components, content hierarchy, interaction, responsive behavior, accessibility, realistic data, system states, validation, protected design decisions, and review criteria. Use for generating or revising websites, dashboards, portals, SaaS interfaces, mobile views, prototypes, or design systems - not requirements discovery, brand invention, production implementation, or replacing usability and accessibility validation.
---

# UI/UX Prompt Builder

Create a bounded design contract that a generation tool can implement and a reviewer
can verify.

## Procedure

1. Confirm the approved requirements, target users, primary journey, page or feature
   scope, brand assets, content, data model, platform, device targets,
   accessibility target, and protected decisions.
2. Identify missing material inputs. Label reasonable design assumptions and avoid
   inventing business rules, permissions, copy claims, or features.
3. Define the page purpose, entry context, primary action, information hierarchy,
   navigation, content order, progressive disclosure, and terminal outcome.
4. Specify layout regions, grid, density, spacing, typography roles, color roles,
   imagery, iconography, elevation, shape, and motion using
   [references/ui-ux-prompt-standard.md](references/ui-ux-prompt-standard.md).
5. Select components by user task and content semantics. Define composition,
   variants, reusable patterns, data requirements, and component boundaries.
6. Specify default, hover, focus, active, selected, disabled, loading, skeleton,
   empty, success, warning, error, denied, partial, offline, and destructive-action
   states as applicable.
7. Define responsive behavior by content priority and interaction needs. Specify
   reflow, stacking, navigation changes, table handling, touch targets, and
   breakpoint intent rather than copying a desktop layout into smaller screens.
8. Define keyboard flow, semantic structure, labels, instructions, errors, focus
   management, contrast, zoom, screen-reader announcements, reduced motion, and
   alternatives for non-text content.
9. Provide realistic sample data covering normal, long, missing, zero, high-volume,
   internationalized, sensitive, and error cases without using real personal data.
10. Define interaction rules, validation timing, confirmations, undo, cancellation,
    autosave, feedback, latency handling, and the relationship between UI state and
    verified system state.
11. Add tool-specific output instructions only after the platform-neutral design
    contract. List files or components in scope, prohibited changes, and required
    implementation summary.
12. Define review criteria and screenshots or viewport checks for visual hierarchy,
    requirements coverage, brand alignment, responsive behavior, accessibility,
    state completeness, content realism, and regression.
13. Deliver with [assets/ui-ux-prompt-template.md](assets/ui-ux-prompt-template.md).

## Guardrails

- Do not rely on style adjectives alone; translate them into observable design
  choices.
- Do not use placeholder text when real content or a defined content model exists.
- Do not hide required functionality, permissions, or recovery behind visual polish.
- Do not make color, hover, icons, or position the only way to convey meaning.
- Do not request inaccessible interactions, unreadable contrast, tiny touch targets,
  uncontrolled motion, or desktop-only behavior.
- Do not let a revision overwrite approved branding, features, content, or layout
  without explicit scope.
- Do not claim usability or accessibility based only on generated appearance.

## Output Contract

Provide the source requirements and assumptions, platform-neutral design contract,
page and component scope, content and realistic data, interaction and state matrix,
responsive and accessibility behavior, protected constraints, tool adapter prompt,
and review checklist.

## Recovery

If material content, permission, or brand inputs are absent, produce a bounded
wireframe prompt with labeled assumptions instead of inventing them. If generated
output removes approved features or protected design, reject the revision and
restore the last approved baseline before issuing a narrower correction prompt.

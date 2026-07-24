---
name: cinematic-shot-list-builder
description: Convert an approved screenplay and storyboard into a production-ready cinematic shot list covering narrative purpose, subject, framing, angle, lens intent, camera movement, lighting, audio, timing, continuity, and dependencies. Use for live action, animation, virtual production, or generative video planning.
---

# Cinematic Shot List Builder

Use the [operating standard](references/shot-list-standard.md) and [working template](assets/shot-list-template.md).

## Procedure

1. Review the screenplay, storyboard, character locks, format, aspect ratio, locations, production method, schedule, and constraints.
2. Assign stable scene and shot IDs, then define each shot's story purpose, subject, action, size, angle, composition, lens intent, movement, focus, lighting, audio, duration, and transition.
3. Plan coverage for geography, essential action, dialogue, reactions, inserts, transitions, and editorial options.
4. Preserve screen direction, eyelines, the 180-degree rule when applicable, matching action, prop state, wardrobe, lighting, and time.
5. Flag complex setups, safety needs, dependencies, alternatives, and priority shots.
6. Deliver the ordered list and a coverage audit.

## Output Contract

Use a table with: shot ID, scene, priority, purpose, subject/action, size, angle, lens intent, movement, lighting, audio, estimated duration, continuity, dependencies, and notes. Add coverage gaps, setup groupings, assumptions, and approval points.

## Guardrails

- Every shot must serve story, clarity, emotion, continuity, or editability.
- Distinguish creative lens intent from exact equipment settings when equipment is unknown.
- Do not claim a location, rig, stunt, or effect is safe or available without confirmation.
- Route movement design to `camera-movement-designer` and lighting detail to `cinematic-lighting-designer`.

## Validation

Confirm complete story coverage, spatial coherence, editorial continuity, feasible durations, consistent identifiers, manageable setup changes, and explicit handling of high-risk or high-dependency shots.

## Recovery

If source versions, coverage, equipment, location authority, schedule, or safety requirements are unresolved, keep the shot provisional and do not authorize hazardous capture.

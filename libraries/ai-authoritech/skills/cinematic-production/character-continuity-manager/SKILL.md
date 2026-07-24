---
name: character-continuity-manager
description: Create and enforce character identity locks across stories, scenes, storyboard panels, image prompts, and video prompts. Use to define appearance, proportions, wardrobe, props, behavior, emotional states, and intentional state changes while detecting unauthorized visual drift.
---

# Character Continuity Manager

Use the [operating standard](references/character-continuity-standard.md) and [working template](assets/character-continuity-template.md).

## Procedure

1. Inventory every named character and collect approved references, identity facts, role, physical traits, wardrobe, accessories, voice, movement, and behavior.
2. Separate immutable identity locks from scene-dependent states such as wardrobe changes, injuries, weathering, emotion, or carried props.
3. Create a character bible and scene-by-scene state ledger using stable IDs.
4. Compare each downstream description or prompt to the approved state; flag omissions, contradictions, ambiguity, and unapproved drift.
5. Resolve conflicts by preserving the latest explicit approval and recording the change point.
6. Deliver corrected continuity blocks and a change log.

## Output Contract

Provide: character registry, canonical description blocks, immutable locks, allowed variations, prohibited drift, scene-state ledger, relationship notes, conflict report, corrected handoffs, assumptions, and approvals needed.

## Guardrails

- Never infer sensitive identity traits or represent a real person's likeness as authorized without evidence.
- Do not beautify, age, recolor, reshape, or otherwise alter approved features unless requested.
- Treat scars, mobility aids, cultural details, and personal identifiers as exact continuity elements when supplied.
- Do not replace a deliberate story-state change with the default appearance.

## Validation

Check identity, face and body description, wardrobe, accessories, handedness, scale, location, emotional state, injuries, props, and chronological state changes for every appearance.

## Recovery

If character identity, reference rights, timeline state, approved appearance, or intentional change is unresolved, stop downstream generation for that character and request a continuity decision.

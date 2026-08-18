---
name: storyboard-director
description: Translate an approved screenplay or scene treatment into a coherent storyboard plan with panels, composition, staging, action, camera intent, dialogue or voiceover, lighting, and continuity handoffs. Use before image generation, animatics, video prompting, or production planning. Use when asked to (1) direct storyboard, (2) plan storyboard, (3) review storyboard, or (4) refine storyboard.
---

# Storyboard Director

Use the [operating standard](references/storyboard-standard.md) and [working template](assets/storyboard-template.md).

## Procedure

1. Confirm the approved source, aspect ratio, delivery platform, visual language, panel density, and locked characters, props, wardrobe, and locations.
2. Break each scene into visual beats; create a new panel only when composition, action, information, or emotional emphasis materially changes.
3. Specify panel ID, narrative purpose, framing, angle, composition, staging, character state, action, environment, camera intent, lighting, dialogue or audio, and transition.
4. Track screen direction, eyelines, geography, prop placement, wardrobe, time, and state changes across panels.
5. Review coverage, rhythm, clarity, continuity, feasibility, and generation dependencies.
6. Deliver a panel table plus continuity and downstream-production handoffs.

## Output Contract

Include: storyboard overview, ordered panel table, character and environment locks, continuity notes, transition notes, audio cues, generation dependencies, assumptions, and approval points. Generate actual images only when the user requests them and an image tool is available.

## Guardrails

- Do not silently alter the screenplay or approved design language.
- Keep one stable identifier for every scene, shot, panel, character, location, and recurring prop.
- Separate what is visible in frame from production explanation.
- Route detailed shot logistics to `cinematic-shot-list-builder` and prompt syntax to `image-prompt-director` or `video-prompt-director`.

## Validation

Confirm that the panels tell the story without hidden assumptions, preserve spatial and character continuity, cover essential action and reactions, and provide enough information for the next production stage.

## Recovery

If screenplay version, aspect ratio, geography, blocking, continuity, safety, or production feasibility is unresolved, mark the affected panels provisional and do not lock the storyboard.

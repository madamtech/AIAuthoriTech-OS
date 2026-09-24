---
name: video-prompt-director
description: Convert approved storyboard shots and visual locks into cinematic video-generation prompts with a defined start state, temporal action, camera motion, environmental motion, lighting, continuity, duration, and output constraints. Use for text-to-video or image-to-video planning. Use when asked to (1) direct video prompt, (2) plan video prompt, (3) review video prompt, or (4) refine video prompt.
---

# Video Prompt Director

Use the [operating standard](references/video-prompt-standard.md) and [working template](assets/video-prompt-template.md).

## Procedure

1. Confirm the source, target model if known, duration, aspect ratio, start and end states, action, camera intent, environment, and continuity locks.
2. Define the opening state, primary action, camera behavior, secondary environmental motion, and resolved end state.
3. Write one coherent prompt prioritizing identity, plausible motion, stable composition, lighting, and atmosphere.
4. Add relevant negative constraints for drift, morphing, extra subjects, unwanted movement, flicker, text, or looping errors.
5. Adapt syntax only to a specified model; otherwise provide a portable master prompt.
6. Review motion conflicts, timing, continuity, feasibility, rights, and handoffs.

## Output Contract

Provide shot and prompt ID, start frame, timed action, camera and environmental motion, end frame, master prompt, negative constraints, duration and format, adapter, assumptions, and dependencies.

## Guardrails

- Do not overload a short clip with unrelated actions or incompatible moves.
- Preserve approved identity and source composition unless change is requested.
- Do not claim successful rendering unless a video tool was used and verified.
- Route complex mechanics to `camera-movement-designer`.

## Validation

Confirm a clear start, readable action, achievable duration, compatible motion, stable identity, consistent physics and lighting, and an intentional end state.

## Recovery

If start or end state, rights, identity, duration, motion, continuity, model limits, or approval is unresolved, keep the output experimental and do not treat it as a final shot.

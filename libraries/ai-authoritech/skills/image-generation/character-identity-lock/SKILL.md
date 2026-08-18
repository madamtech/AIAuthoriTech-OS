---
name: character-identity-lock
description: "Preserve a character's recognizable identity across poses, outfits, scenes, formats, and generation sessions. Use when creating, reviewing, revising, governing, or validating image-generation work that needs explicit inputs, constraints, rights, continuity, quality checks, recovery handling, and a reusable production-ready output. Use when asked to (1) create character identity lock, (2) review character identity lock, (3) improve character identity lock, or (4) standardize character identity lock."
---
# Character Identity Lock

Use the [operating standard](references/operating-standard.md) and [working template](assets/working-record.md).

## Purpose
Preserve a character's recognizable identity across poses, outfits, scenes, formats, and generation sessions.

## Inputs
Canonical face/body references, demographic and appearance descriptors, hairstyle, skin tone, proportions, distinguishing features, approved expression range, and forbidden changes.

## Procedure
Rank references, define immutable identity markers, document controlled variables, create front/three-quarter/profile descriptors, specify hairstyle geometry and texture, record makeup and skin finish, and build identity-specific negative constraints. Separate identity from wardrobe and style. For edits, identify which pixels/features must remain untouched.

## Output Contract
Identity lock card, reference hierarchy, invariant markers, allowed variations, prohibited mutations, prompt anchors, and comparison checklist.

## Guardrails
Never infer sensitive traits not needed for the visual. Do not beautify by changing facial structure, skin tone, age, body proportions, or culturally specific features. When the user supplies their own image, prioritize that reference over memory.

## QA
Compare eyes, nose, mouth, jaw, face width, hairline, skin tone, body proportions, and signature expression. Identity passes only when recognizable without relying on clothing or background.

## Recovery
If drift occurs, simplify the scene, restore neutral lighting, re-anchor facial geometry, and generate a reference sheet before returning to complex scenes.

---
sku: AA-SKL-000161
asset_id: image-generation.multi-image-continuity-supervisor.v1
version: 1.0.0
status: testing
---
# Multi-Image Continuity Supervisor

## Purpose
Maintain identity, wardrobe, props, environment, color, scale, and story state across a sequence or campaign.

## Inputs
Approved images, character Bible, Style DNA, world rules, shot order, continuity events, and allowed changes.

## Procedure
Create a continuity ledger for each frame: character appearance, wardrobe, accessories, object positions, lighting/time, environment state, camera logic, and narrative changes. Mark intentional transitions and immutable carryovers.

## Output contract
Continuity ledger, per-frame locks, change log, mismatch report, and correction plan.

## Rules
Do not treat similar as continuous. Track small details such as jewelry, hair parting, product orientation, logos, and hand-held objects.

## QA
Compare adjacent and nonadjacent frames for all ledger fields. Validate that changes occur only when the story requires them.

## Recovery
Choose the highest-quality canonical frame and realign the sequence to it.

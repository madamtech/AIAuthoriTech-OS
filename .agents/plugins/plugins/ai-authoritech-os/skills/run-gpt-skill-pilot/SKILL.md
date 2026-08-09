---
name: run-gpt-skill-pilot
description: Run a controlled before-and-after evaluation of a proposed skill on one or more AIAuthoriTech GPT configurations. Use when testing a skill before live deployment, comparing baseline and enhanced outputs, documenting compatibility evidence, deciding pass/adapt/reject, or preparing a safe rollout batch.
---

# Run GPT Skill Pilot

## Pilot design

1. Require an authoritative baseline manifest and a completed compatibility decision.
2. Select 3–5 representative GPTs when testing a shared skill across a category.
3. Freeze the same input, references, tool availability, and evaluation rubric for baseline and enhanced runs.
4. Run the baseline with the original configuration.
5. Run the candidate with only the proposed skill delta added.
6. Score purpose preservation, instruction adherence, output quality, consistency, tool selection, knowledge safety, and regression risk.
7. Record defects, including visually attractive outputs that fail functional or production logic.
8. Decide `pass`, `adapt-and-retest`, or `reject-and-rollback` for each GPT.
9. Do not deploy to other GPTs until every representative pilot passes.

## Required evidence

Record the GPT name and ID, manifest version, skill version, exact test inputs, baseline output reference, enhanced output reference, rubric results, defects, adaptations, decision, reviewer, and date.

## Deployment boundary

A successful pilot authorizes a rollout recommendation, not an automatic live edit. Require explicit user authorization before modifying live GPT configurations. After deployment, update the manifest and GPT changelog with the exact instruction delta and verification result.

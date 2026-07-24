---
name: print-failure-diagnoser
description: Diagnose 3D-print failures using evidence from the model, slicer, material, machine, environment, and failure timing. Use for adhesion, warping, clogs, shifts, stringing, weak layers, dimensional, or surface defects.
---

# Print Failure Diagnoser

Use the [operating standard](references/print-diagnosis-standard.md) and [working template](assets/print-diagnosis-template.md).

## Procedure

1. Capture photos, failure layer, printer, profile, material condition, environment, maintenance, and recent changes.
2. Classify the symptom and rank causes across model, slicing, material, mechanics, temperature, motion, and workflow.
3. Test one controlled change at a time, verify recovery with repeat runs, and document prevention.

## Output Contract

Provide verified inputs, specifications, assumptions, risks, approvals, execution steps, owners, and validation criteria.

## Guardrails

- Use verified facts and label estimates.
- Protect customer, supplier, and proprietary information.
- Require approval before irreversible production, pricing, or customer communication.
- Do not claim safety, compliance, or successful validation without evidence.

## Recovery

If the machine has unsafe motion, overheating, electrical, ventilation, damaged hardware, or unknown-material indicators, stop and remove it from service. Preserve evidence and escalate to qualified maintenance rather than continuing diagnostic prints.

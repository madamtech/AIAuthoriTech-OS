---
name: print-production-optimizer
description: Optimize repeatable 3D-print production for dimensional quality, surface finish, throughput, material use, labor, maintenance, yield, and controlled failure recovery. Use after a design has passed functional validation and a baseline printer, material batch, slicer profile, environment, measurement method, and acceptance threshold are available.
---

# Print Production Optimizer

Use the [operating standard](references/print-optimization-standard.md) and [working template](assets/print-optimization-template.md).

## Procedure

1. Establish approved model, material, printer, slicer, quality target, demand, and baseline yield.
2. Measure cycle time, labor, scrap, defects, changeovers, energy assumptions, and bottlenecks.
3. Test controlled changes to orientation, plate layout, layer height, walls, infill, supports, temperatures, speeds, and workflow.
4. Track results by version and lock settings only after repeat runs.
5. Define preventive maintenance, inspection sampling, and rollback.

## Output Contract

Provide baseline metrics, experiment log, approved profile, capacity estimate, standard work, inspection plan, and improvement backlog.

## Guardrails

- Do not trade away required strength or safety for speed.
- Change one meaningful variable at a time where practical.
- Keep validated profiles versioned and reversible.

## Recovery

If the defect, baseline profile, machine condition, material batch, environmental factors, measurement method, or acceptance threshold is unresolved, change one controlled variable at a time. Preserve the last validated profile and stop unsafe or damaging trials.

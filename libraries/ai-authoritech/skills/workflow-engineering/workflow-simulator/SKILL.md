---
name: workflow-simulator
description: Simulate workflow demand, queues, capacity, branching, resources, timing, failures, rework, service levels, and proposed changes using explicit distributions and scenarios. Use to compare designs and stress assumptions before implementation. Do not present a model as a forecast without calibration, uncertainty, and validation. Use when asked to (1) create workflow simulator, (2) review workflow simulator, (3) improve workflow simulator, or (4) standardize workflow simulator.
---

# Workflow Simulator

Use the [workflow simulation standard](references/workflow-simulation-standard.md) and record inputs and results in the [workflow simulation report template](assets/workflow-simulation-report-template.md).

## Procedure

1. Define the decision, model boundary, entities, demand, resources, branches, priorities, and metrics.
2. Source arrival, handling, wait, rework, failure, absence, and capacity distributions with provenance.
3. Represent calendars, queues, batching, dependencies, approvals, exceptions, and resource contention.
4. Calibrate against historical throughput, cycle time, queue, and service-level observations.
5. Run baseline, peak, failure, staffing, policy, and future-state scenarios with repeated trials.
6. Report distributions, confidence, sensitivity, bottlenecks, utilization, tail risk, and model limitations.
7. Validate surprising results, avoid overfitting, and preserve model version and randomization settings.
8. Deliver model contract, assumptions, evidence, scenarios, results, decisions, and revalidation triggers.

## Guardrails
- Do not use averages where variability drives queues or service failures.
- Do not treat 100% utilization as a safe operating target.
- Do not invent precision unsupported by input evidence.
- Do not generalize beyond simulated conditions.

## Recovery

If calibration, distributions, model boundaries, or surprising results cannot be validated, do not use the simulation as a forecast or approval basis. Preserve the model version and randomization settings, label results exploratory, and collect evidence before rerunning.

## Output Contract

Deliver the model contract, provenance, distributions, calibration, scenarios, repeated-trial results, uncertainty, sensitivity, bottlenecks, tail risks, limitations, decisions supported, version, and revalidation triggers.

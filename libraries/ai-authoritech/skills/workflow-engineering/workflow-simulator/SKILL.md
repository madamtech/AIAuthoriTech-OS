---
name: workflow-simulator
description: Simulate workflow demand, queues, capacity, branching, resources, timing, failures, rework, service levels, and proposed changes using explicit distributions and scenarios. Use to compare designs and stress assumptions before implementation. Do not present a model as a forecast without calibration, uncertainty, and validation.
---

# Workflow Simulator

1. Define the decision, model boundary, entities, demand, resources, branches, priorities, and metrics.
2. Source arrival, handling, wait, rework, failure, absence, and capacity distributions with provenance.
3. Represent calendars, queues, batching, dependencies, approvals, exceptions, and resource contention.
4. Calibrate against historical throughput, cycle time, queue, and service-level observations.
5. Run baseline, peak, failure, staffing, policy, and future-state scenarios with repeated trials.
6. Report distributions, confidence, sensitivity, bottlenecks, utilization, tail risk, and model limitations.
7. Validate surprising results, avoid overfitting, and preserve model version and randomization settings.
8. Deliver model contract, assumptions, evidence, scenarios, results, decisions, and revalidation triggers.

## Rules
- Do not use averages where variability drives queues or service failures.
- Do not treat 100% utilization as a safe operating target.
- Do not invent precision unsupported by input evidence.
- Do not generalize beyond simulated conditions.

# Release Planning Standard

## Release charter

Define the target user, current problem and baseline, intended outcome, strategy,
release type, eligibility, maturity promise, success and guardrail measures,
window, accountable owner, capacity, constraints, and decision rights.

## Scope classes

- Committed: necessary for the coherent outcome and supported by capacity.
- Conditional: enters only if a named condition is satisfied without displacing
  committed work.
- Discovery: produces evidence, not promised functionality.
- Excluded: explicitly outside the release, with a reason or revisit trigger.
- Mandatory: obligation or unacceptable risk with an owner and deadline.

Every scope item must trace to an outcome or control and have acceptance evidence.

## Forecasting

Use throughput or estimates calibrated with actual delivery history when
available. Include review queues, integration lead time, holidays, operational
load, unplanned work, dependency uncertainty, and specialist constraints. Report
a range and confidence. A target date is a decision constraint; it is not evidence
that the planned scope fits.

## Product readiness

Require evidence appropriate to risk for:

- requirements and acceptance;
- user experience and accessibility;
- architecture, data, permissions, and integration contracts;
- testing and unresolved defects;
- security, privacy, legal, compliance, and responsible-AI review;
- migration, performance, reliability, backup, restore, and recovery;
- observability, support, documentation, training, and communications;
- deployment readiness and withdrawal capability.

Keep technical deployment authorization in the deployment plan. The release plan
decides whether the product should be exposed and expanded.

## Rollout and adoption

Define each cohort by eligibility, size, exposure mechanism, duration, signals,
support, feedback, expansion threshold, hold threshold, and withdrawal action.
Measure:

1. eligible population;
2. exposed population;
3. awareness or discovery;
4. activation;
5. successful task or outcome;
6. repeat use or retention;
7. user and business benefit;
8. harms and operational guardrails.

Distinguish product availability from adoption and adoption from benefit.

## Decision reviews

At each gate, present scope, evidence, deviations, open defects, risks, capacity,
forecast, user feedback, operational health, outcome signals, and recommendation.
Record the named decision owner, decision, dissent, conditions, and next review.

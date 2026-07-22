# Workflow Design Standard

## Stage contract

Every stage needs:

- Stable ID and purpose
- Executor and authority
- Prerequisites and input schema
- One defined action
- Output schema and evidence
- Validation rule and timeout
- Success and failure routes
- Retry or compensation policy

## Shared state

Store only fields needed across stages. Assign an owner, sensitivity, allowed writers, retention, and lineage for each field. Prefer immutable event evidence over silent state replacement.

## Branches

Express conditions as testable facts. Define an else route. Every branch must terminate, converge, or escalate; no path may disappear.

## Failures

- Retry only transient failures and cap attempts.
- Compensate when the prior action cannot be rolled back directly.
- Degrade gracefully when a lower-quality but safe outcome remains useful.
- Escalate when authority, evidence, or required capability is unavailable.

## Completion

Completion is a validated business outcome, not merely the absence of an error. Record the terminal state and evidence that proves every required criterion.

## Registration

The workflow folder must contain `workflow.json` conforming to `schemas/workflow.schema.json`. Catalog identity and manifest identity must match exactly.

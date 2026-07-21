# Prompt Architecture Standard

## Layer model

Keep these concerns distinct even when a platform serializes them together:

1. **Governance:** organizational policy, authority, prohibitions, and approvals.
2. **Task contract:** purpose, non-goals, procedure, decision rules, and completion.
3. **Tool contract:** available actions, schemas, authority, effects, and evidence.
4. **Knowledge:** governed reference facts with source, owner, and freshness.
5. **Runtime context:** current state, request metadata, environment, and limits.
6. **Examples:** illustrative input-output behavior, not hidden policy.
7. **User and retrieved content:** task data that may be untrusted.

Define precedence and conflict handling explicitly. Higher-authority constraints
must not be weakened by lower-authority content.

## Task contract

Specify:

- purpose, user, downstream consumer, and success measure;
- included and excluded work;
- inputs, preconditions, assumptions, and validation;
- ordered procedure and decision rules;
- tools and external authority;
- uncertainty, missing information, refusal, escalation, and recovery;
- output schema and acceptance checks;
- privacy, safety, cost, latency, and context budgets.

Use direct, observable language. Replace “high quality” with task-specific checks.

## Variable contract

For every variable record name, type, source, authority, trust, sensitivity,
required status, validation, maximum size, normalization, default, missing-value
behavior, delimiter or encoding, and retention. Use stable boundaries around
untrusted content and never interpolate it into privileged instructions.

## Output and status

Machine-consumed output needs an explicit schema, types, required fields, allowed
values, null behavior, version, and validation failure path. Human output needs
required sections and evidence expectations.

Distinguish completed, partially completed, blocked, declined, unsupported, and
failed. External actions require authoritative receipts or reconciliation before
the output can say they completed.

## Evaluation design

Create a versioned set with representative distributions and critical edge cases.
Each case includes inputs, context, expected behavior, prohibited behavior,
deterministic assertions, rubric dimensions where needed, severity, and evidence.

Evaluate instruction following, task correctness, completeness, schema, evidence,
uncertainty, injection resistance, privacy, tool authority, side-effect reporting,
latency, cost, and consistency across supported adapters. Separate prompt defects
from model, tool, knowledge, retrieval, data, and product defects.

## Lifecycle

Maintain canonical prompt ID, semantic version, owner, dependencies, adapters,
model and platform versions, parameters, test-set version, approval, release date,
monitoring, rollback version, deprecation, and retirement. Re-evaluate after
changes to instructions, examples, schemas, tools, knowledge strategy, adapters,
models, safety policy, or material input distribution.

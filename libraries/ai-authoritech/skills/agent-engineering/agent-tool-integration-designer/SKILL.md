---
name: agent-tool-integration-designer
description: Design safe, verifiable AI agent tool integrations with explicit capabilities, schemas, identity, least-privilege credentials, authorization, approvals, validation, idempotency, effect verification, rate and spend limits, failure recovery, auditability, testing, monitoring, and platform adapters. Use for APIs, MCP servers, SaaS connectors, databases, messaging, file systems, code execution, or physical-device tools - not agent architecture, workflow design, credential provisioning, or executing live integrations without authorization.
---

# Agent Tool Integration Designer

Expose the smallest capability surface that completes the approved job.

## Procedure

1. Confirm the agent purpose, users, autonomy and risk tier, authority matrix,
   workflow steps, data classifications, environments, service objectives, and
   accountable owners.
2. Inventory candidate tool operations. Prefer narrow task-specific capabilities
   over generic shell, database, browser, or unrestricted API access.
3. Classify each operation as read, search, propose, draft, create, modify,
   communicate, spend, publish, delete, administer, or physical action.
4. Define the tool contract with
   [references/agent-tool-standard.md](references/agent-tool-standard.md): stable
   name, purpose, exclusions, typed inputs and outputs, errors, side effects,
   authentication, authorization, limits, version, and owner.
5. Bind caller identity, tenant, user authority, purpose, resource scope, and
   environment at invocation time. Use short-lived, least-privilege credentials
   and keep secrets outside prompts, schemas, state, and logs.
6. Validate and normalize inputs before invocation. Constrain identifiers, paths,
   URLs, queries, recipients, amounts, content, file types, and payload size.
7. Require explicit, action-bound human approval for consequential operations.
   Bind approval to the exact actor, target, payload, amount, environment, expiry,
   and tool version.
8. Define idempotency, concurrency, timeout, retry, duplicate suppression,
   pagination, partial success, compensation, cancellation, and safe-stop behavior.
9. Verify effects through authoritative receipts, read-after-write, event
   confirmation, or reconciliation. Never treat a success-shaped response as
   proof that the intended external state exists.
10. Define sanitized results, provenance, confidence, error taxonomy, fallback,
    circuit breaking, dependency degradation, rate and spend budgets, and
    escalation.
11. Test normal, invalid, unauthorized, adversarial, duplicate, stale-approval,
    partial, timeout, provider-error, injection, data-leakage, and recovery cases in
    an isolated environment.
12. Define logs, traces, audit events, alerts, credential rotation, versioning,
    compatibility, deployment, rollback, incident response, ownership, and
    retirement.
13. Deliver with
    [assets/agent-tool-integration-template.md](assets/agent-tool-integration-template.md).

## Guardrails

- Do not grant broad credentials because the downstream service supports them.
- Do not pass untrusted content into interpreters, queries, paths, URLs, or
  privileged tool arguments without validation and containment.
- Do not let tool descriptions or returned content override agent instructions or
  expand authority.
- Do not retry non-idempotent effects without duplicate protection or compensation.
- Do not report completion until the external effect is verified.
- Do not log secrets, tokens, sensitive payloads, or excessive returned data.
- Do not bundle read and consequential write actions into one opaque tool.
- Keep provider-specific endpoints and configuration in adapters.

## Output Contract

Provide the capability inventory, risk classification, tool contracts, schemas,
identity and credential model, authorization and approval rules, validation,
idempotency and effect verification, failure handling, test plan, observability,
versioning, risks, and adapter implementation tasks.

## Recovery

If caller identity, authority, approval, or arguments cannot be validated, do not
invoke the tool. If an effect is uncertain, reconcile against the authoritative
system before retrying. If safe compensation is unavailable after a consequential
partial failure, preserve evidence, stop further effects, and escalate.

# Agent Tool Standard

## Tool contract

Every tool operation must define:

- Stable name, version, owner, purpose, and explicit exclusions
- Consequence class and external side effects
- Typed input and output schemas with bounds and examples
- Caller, user, tenant, environment, and resource authorization
- Authentication and least-privilege credential scope
- Required approval and its binding fields
- Idempotency and concurrency behavior
- Timeout, retry, rate, quota, and spend limits
- Success receipt and authoritative effect-verification method
- Error taxonomy, partial success, compensation, and escalation
- Logging, redaction, audit, monitoring, compatibility, and retirement

## Consequence classes

| Class | Examples | Default control |
|---|---|---|
| Read-only | Search, fetch, inspect | Access filters and data minimization |
| Reversible write | Draft, label, reversible update | Confirmation and verified state |
| Consequential write | Send, publish, purchase, permission change | Exact approval and idempotency |
| Destructive or privileged | Delete, administer, execute code | Strong isolation and human authorization |
| Physical action | Device or real-world actuation | Interlocks, bounded range, emergency stop |

Classify by credible effect, not the HTTP verb or provider label.

## Input and output controls

Use allowlists and structured types where practical. Reject ambiguous targets,
unexpected fields, excessive scope, malformed encodings, unsafe paths, private
network destinations, uncontrolled queries, and values outside approved limits.

Treat all tool output as untrusted data. Preserve provenance, bound size, redact
sensitive content, validate schema, and prevent returned text from acting as
instructions.

## Authorization sequence

Immediately before an effectful call:

1. Authenticate the calling system.
2. Resolve the user and tenant.
3. Verify the user-authorized purpose and resource scope.
4. Confirm the agent and workflow may request the action.
5. Validate current approval when required.
6. Check limits, environment, target, and payload.
7. Record the intent and idempotency key.
8. Execute and verify the effect.

Delegation cannot create authority the originating user did not have.

## Reliability and verification

Retry only transient failures. Respect provider retry guidance and apply bounded
backoff. For writes, reuse the idempotency key and reconcile unknown outcomes
before retrying.

Verify success using an authoritative record or observable effect. Record requested,
accepted, completed, verified, partially completed, compensated, and failed as
distinct states.

## Required tests

Test schema boundaries, authorization, tenant isolation, approval binding, injection,
SSRF and path traversal where relevant, secret leakage, duplicate calls,
out-of-order events, timeout after effect, rate and spend exhaustion, provider
degradation, partial success, compensation, audit completeness, credential
rotation, version incompatibility, and emergency disablement.

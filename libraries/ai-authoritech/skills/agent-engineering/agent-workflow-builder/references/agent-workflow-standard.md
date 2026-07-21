# Agent workflow standard

## Durable state

Store only what is required:

- workflow and correlation identifiers
- caller and authorization context reference
- current state and version
- validated inputs and derived facts with provenance
- approval request, scope, approver, status, and expiry
- action intent, idempotency key, attempt, result, and verification
- outputs, errors, compensation status, and completion evidence

Do not store credentials or unnecessary sensitive content.

## Step contract

Every step defines:

- entry event and preconditions
- executor and authority
- input and output schema
- side effect and idempotency behavior
- verification evidence
- checkpoint and emitted event
- timeout, retry eligibility, limit, and backoff
- compensation or safe partial state
- escalation and terminal failure behavior

## Test scenarios

Cover duplicate events, delayed approvals, rejected or amended approvals, tool
timeouts, unknown outcomes, partial success, stale state, concurrent updates,
schema mismatch, unauthorized handoffs, compensation failure, replay, and recovery.

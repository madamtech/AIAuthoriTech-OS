# Workflow Automation Design Standard

Translate the approved blueprint and architecture into an executable platform-neutral state machine. Define typed triggers, correlation, inputs, outputs, completion, cancellation, timeouts, nodes, decisions, branches, parallel joins, loops, waits, approvals, integrations, and human tasks. Every branch must end in an explicit completion, failure, cancellation, or compensated state.

Specify least-privilege identities, mappings, validation, idempotency, locking, concurrency, retries, backoff, dead letters, compensation, replay, reconciliation, and manual recovery. Declare success only after authoritative verification of required effects. Add logs, metrics, traces, audit events, alerts, dashboards, runbooks, tests, deployment, rollback, and operational ownership. Do not silently change approved business rules.

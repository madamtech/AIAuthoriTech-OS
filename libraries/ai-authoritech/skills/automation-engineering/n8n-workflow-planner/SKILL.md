---
name: n8n-workflow-planner
description: Map an approved platform-neutral automation design into a production-ready n8n implementation plan covering triggers, nodes, expressions, credentials, sub-workflows, queues, executions, errors, tests, deployment, scaling, and operations. Use when n8n is the selected orchestrator. Do not claim node availability or product behavior without verifying the target n8n version and deployment.
---

# n8n Workflow Planner

1. Confirm n8n edition, exact version, hosting, execution mode, workers, database, queue, security, and constraints.
2. Map each workflow step to verified native nodes, HTTP requests, code, sub-workflows, or approved external services.
3. Define trigger configuration, credentials, expressions, item structures, binary data, pagination, batches, and state.
4. Use environment-specific credentials and variables; prohibit secrets in nodes, exports, logs, and test fixtures.
5. Design Execute Workflow boundaries, correlation, idempotency, concurrency, rate limits, retries, and error workflows.
6. Configure execution retention, pruning, redaction, metrics, alerts, health, backups, scaling, and disaster recovery.
7. Plan fixtures and tests for expressions, nodes, branches, credentials, failures, recovery, upgrades, and rollback.
8. Deliver node map, configuration contract, expressions, credential plan, tests, deployment, operations, and limitations.

## Rules

- Verify current node and platform behavior before implementation.
- Do not use the Code node to bypass approved security or maintainability controls.
- Do not enable unlimited execution retention with sensitive payloads.
- Do not import unreviewed community nodes into production.

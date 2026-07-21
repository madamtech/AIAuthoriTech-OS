# Agent Deployment Standard

## Required release identity

Bind every deployment decision to:

- Immutable artifact, source revision, and dependency lock
- Instruction, policy, workflow, schema, and knowledge-index versions
- Model and model-parameter configuration
- Tool and integration versions
- Environment configuration fingerprint
- QA evidence and approved exceptions

Any material change after approval creates a new candidate or requires documented
impact review and focused retesting.

## Deployment controls

| Control area | Minimum requirement |
|---|---|
| Environments | Isolation, promotion path, parity gaps, test-data rules, and access ownership |
| Configuration | Versioned non-secret configuration, drift detection, review, and rollback |
| Secrets | Managed secret store, least privilege, rotation, revocation, and audit trail |
| Data and state | Backup, migration, compatibility, validation, recovery point, and retention |
| Knowledge | Source snapshot, index version, freshness, access filters, and rollback |
| Tools | Scoped credentials, rate and spend limits, effect verification, and kill switch |
| Release | Strategy, exposure units, gates, pause conditions, approvers, and evidence |
| Operations | Logs, traces, metrics, alerts, runbooks, on-call, incident and support ownership |

## Rollout selection

- **Direct:** Use only for low-risk, easily reversible changes with strong
  pre-release evidence and minimal traffic.
- **Rolling:** Use when instances are interchangeable and mixed-version
  compatibility is proven.
- **Canary:** Use for measurable staged exposure when representative users or
  traffic can be isolated.
- **Blue-green:** Use when rapid traffic switching and parallel environments
  justify the added cost and data synchronization complexity.
- **Shadow:** Use to observe behavior without authorizing external effects; protect
  privacy and prevent duplicate actions.
- **Feature flag:** Use to separate deployment from activation and enable bounded
  cohorts or rapid disablement.

Combine strategies when justified, but assign one owner and one source of truth
for exposure state.

## Minimum gates

### Before deployment

- QA release conditions are satisfied or formally accepted by an authorized owner.
- Artifact and configuration fingerprints match approved evidence.
- Dependencies, quotas, credentials, backups, migrations, monitoring, and rollback
  are ready.
- Support, security, data, business, and change owners are available as required.
- Test accounts, safe verification data, communication, and maintenance windows
  are prepared.

### During deployment

- Observe health, error, latency, cost, safety, authorization, and task-success
  guardrails at each exposure stage.
- Pause on missing telemetry, unexpected drift, approval mismatch, or unverified
  external effect.
- Expand exposure only after the defined observation period and gate approval.

### After deployment

- Verify core tasks, role boundaries, approvals, retrieval, tool effects, workflow
  state, logs, alerts, and kill switch.
- Reconcile queues, state, data, and external actions.
- Capture stakeholder confirmation and update the operational baseline.

## Rollback triggers

Include explicit thresholds for:

- Unauthorized, unsafe, privacy, or security behavior
- Critical or high-severity regression
- Task success, error rate, latency, availability, or cost outside limits
- Corrupted or inconsistent state
- Tool duplication, unverified effects, or approval bypass
- Monitoring loss or inability to determine system condition

Safety and authorization failures trigger immediate containment regardless of
aggregate performance.

## Recovery completeness

Define rollback as a coordinated recovery of code, configuration, prompts,
policies, models, knowledge, schemas, traffic, credentials, queues, state, data,
and external effects. If an element cannot be reversed, define compensation,
manual reconciliation, evidence, owner, and deadline.

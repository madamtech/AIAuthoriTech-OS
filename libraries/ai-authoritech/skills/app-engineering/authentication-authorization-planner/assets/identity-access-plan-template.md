# Authentication and Authorization Plan

## Plan control

- Product and release:
- Requirement IDs:
- Risk and data classification:
- Security, product, and support owners:
- Supported environments and regions:

## Identity inventory

| Identity type | Population | Source | Assurance | Lifecycle owner |
|---|---|---|---|---|

## Authentication methods and journeys

| Journey | Method | Verification | MFA or step-up | Failure and recovery | Audit |
|---|---|---|---|---|---|

Cover registration, invitation, sign-in, federation, linking, recovery, credential
change, suspension, deletion, and reactivation.

## Session contract

| Concern | Decision |
|---|---|
| Issuance and audience | |
| Storage and binding | |
| Idle and absolute expiry | |
| Rotation and revocation | |
| Concurrent sessions | |
| Risk response | |
| CSRF and replay protection | |

## Resource-level authorization

| Actor or role | Tenant | Resource | Action | Condition | Decision | Audit |
|---|---|---|---|---|---|---|

## Tenant and privileged administration

Define membership, invitation, role change, ownership transfer, offboarding,
support access, impersonation, emergency access, approval, expiry, and notification.

## Service identities

| Workload or integration | Credential | Audience and scope | Rotation | Delegation | Owner |
|---|---|---|---|---|---|

## Abuse, privacy, and audit controls

| Threat or event | Prevention | Detection | User response | Escalation |
|---|---|---|---|---|

## Verification

| Test | Actor and condition | Expected decision | Evidence |
|---|---|---|---|

## Provider adapter, migration, and operations

Define provider configuration, environment separation, reconciliation, migration,
rollback, key rotation, logs, alerts, incident response, support, and retirement.

## Risks and open decisions

| Item | Impact | Owner | Mitigation or decision | Due |
|---|---|---|---|---|

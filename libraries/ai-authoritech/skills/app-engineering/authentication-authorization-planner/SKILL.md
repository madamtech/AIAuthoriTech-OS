---
name: authentication-authorization-planner
description: Design secure, usable, provider-neutral application identity and access controls covering identity providers, registration, verification, sign-in, MFA, sessions, recovery, invitations, organizations, roles, resource-level authorization, service identities, privileged administration, tenant isolation, audit, abuse controls, testing, migration, and incident response. Use for websites, SaaS products, portals, internal tools, APIs, and AI-enabled apps - not credential provisioning, legal identity proofing decisions, production configuration, or relying on client-side visibility as authorization.
---

# Authentication and Authorization Planner

Authenticate identities, then authorize every resource action in current context.

## Procedure

1. Confirm users, organizations, tenants, resources, actions, risk, data classes,
   environments, regulatory constraints, recovery needs, and business owners.
2. Define identity types: anonymous visitor, customer, member, administrator,
   support operator, service account, workload, integration, and API client.
3. Select authentication methods and assurance levels using
   [references/identity-access-standard.md](references/identity-access-standard.md).
   Match MFA, reauthentication, and identity proofing to consequence.
4. Design registration, verification, invitation, federation, sign-in, sign-out,
   account linking, profile change, credential change, recovery, suspension,
   deletion, and reactivation journeys.
5. Define session issuance, binding, expiry, idle timeout, rotation, revocation,
   concurrent sessions, device visibility, risky-event response, and secure storage.
6. Model authorization as actor, tenant, resource, action, condition, and decision.
   Use deny by default and enforce checks on trusted servers and at the data layer.
7. Define roles only as reusable policy inputs. Add ownership, relationship,
   membership, resource state, environment, approval, and attribute conditions
   where role-only access is insufficient.
8. Define tenant membership, invitations, role changes, transfer of ownership,
   offboarding, cross-tenant administration, support access, impersonation, and
   emergency access with approvals, expiry, and audit.
9. Define service identities, token audience and scope, secret or key rotation,
   workload authentication, delegation, webhooks, background jobs, and least
   privilege.
10. Design rate limits, enumeration resistance, anti-automation, anomaly detection,
    lockout or throttling, notification, audit events, and incident escalation.
11. Define accessible and privacy-preserving error behavior without revealing
    whether sensitive accounts or resources exist.
12. Test ordinary, denied, cross-tenant, object-reference, privilege-escalation,
    stale-role, revoked-session, replay, CSRF, fixation, recovery abuse, account
    linking, service-token, and administrator scenarios.
13. Plan provider adapters, environment isolation, migration, rollback, account
    reconciliation, observability, key rotation, incident response, support, and
    retirement.
14. Deliver with [assets/identity-access-plan-template.md](assets/identity-access-plan-template.md).

## Guardrails

- Do not trust role, tenant, user, or ownership identifiers supplied by the client
  without binding them to authenticated server context.
- Do not treat hiding a button, route, object ID, or API field as authorization.
- Do not use long-lived shared service credentials when scoped workload identities
  are available.
- Do not let support or administrators access customer data without bounded purpose,
  approval where required, expiry, and audit.
- Do not reveal account existence or protected resource details through errors.
- Do not design account recovery weaker than the protected account.
- Do not log passwords, session tokens, recovery secrets, private keys, or MFA
  factors.
- Keep provider-specific configuration in adapters.

## Output Contract

Provide the identity inventory, assurance and authentication model, lifecycle
journeys, session contract, resource-action authorization matrix, tenant and
administrative controls, service-identity design, abuse and audit controls, test
plan, migration and incident model, provider-adapter requirements, risks, and open
decisions.

## Recovery

If identity, tenant, resource ownership, or policy context is missing, deny the
action by default without revealing protected details. If account recovery or
administrative access cannot meet the target assurance level, block that journey
and require a stronger reviewed control rather than weakening the protected account.

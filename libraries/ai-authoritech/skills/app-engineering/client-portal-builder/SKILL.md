---
name: client-portal-builder
description: Create build-ready specifications and staged implementation plans for secure, accessible client portals covering tenant boundaries, onboarding, identity, permissions, dashboards, projects, tasks, documents, messages, approvals, billing views, support, notifications, integrations, audit, data lifecycle, responsive UX, testing, deployment, and operations. Use for consulting, agency, professional-services, customer-success, partner, or account portals - not to invent business processes, expose internal-only data, process live payments, or deploy without authorization and verification. Use when asked to (1) build client portal, (2) refine client portal, (3) validate client portal, or (4) standardize client portal.
---

# Client Portal Builder

Design the client relationship and authorization model before the dashboard.

## Procedure

1. Confirm the portal outcome, client types, internal teams, current service
   workflow, systems of record, brand, devices, languages, accessibility target,
   data classes, contractual constraints, success measures, and owners.
2. Define tenant, client organization, account, project, engagement, contact,
   internal user, partner, resource, and delegated-administrator boundaries. State
   whether a person may belong to multiple client organizations.
3. Map roles and resource-level permissions for clients, client admins, internal
   staff, contractors, support, finance, and service identities. Define invitation,
   verification, federation, recovery, deactivation, impersonation, break-glass,
   access review, and audit.
4. Inventory client journeys: onboarding, profile and organization setup, project
   status, task completion, document exchange, messages, approvals, scheduling,
   deliverables, invoices or payment status, support, feedback, export, and
   offboarding.
5. Assign a source of truth and allowed writers for every displayed or editable
   field. Define freshness, reconciliation, conflict behavior, history, and the
   portal's behavior when an upstream system is unavailable.
6. Define information architecture, navigation, search, dashboard hierarchy,
   project and account views, content ownership, and all loading, empty, partial,
   denied, expired, offline, error, success, and destructive-action states using
   [references/client-portal-standard.md](references/client-portal-standard.md).
7. Define document classification, upload validation, malware scanning, storage,
   preview, versioning, access, download, expiration, retention, deletion, export,
   and audit. Do not expose storage paths as authorization.
8. Define messages, comments, mentions, attachments, moderation, retention,
   delivery state, read state, notification preferences, quiet hours, digesting,
   escalation, and external-channel boundaries.
9. Define approvals and signatures by request, authority, evidence, version,
   deadline, reminder, delegation, rejection, revocation, finality, and downstream
   effect. Route legally binding electronic-signature needs to an approved service
   and qualified review.
10. Treat invoices, subscriptions, usage, and payment status as reconciled views
    from authoritative commerce systems. Use provider-hosted secure payment
    surfaces; never collect raw payment credentials in the portal design.
11. Define support intake, categorization, severity, attachments, status,
    assignment, service expectations, escalation, communication, closure,
    satisfaction, and linkage to incidents or known issues.
12. Define APIs, webhooks, jobs, file transfers, and events with tenant context,
    scopes, idempotency, signatures, retries, pagination, reconciliation, rate
    limits, and failure ownership.
13. Specify responsive and accessible behavior for keyboard, focus, semantics,
    contrast, zoom, reflow, touch targets, errors, status announcements, files,
    tables, charts, and session expiry.
14. Define analytics and observability for onboarding completion, successful
    client tasks, freshness, failed integrations, authorization denials,
    notifications, support demand, accessibility, reliability, latency, and
    adoption while minimizing sensitive telemetry.
15. Decompose implementation into vertical slices that each complete a client
    journey with server-side authorization, data contracts, UI states,
    instrumentation, tests, deployment, recovery, documentation, and support.
16. Deliver with
    [assets/client-portal-plan-template.md](assets/client-portal-plan-template.md).

## Guardrails

- Do not trust organization or project identifiers supplied by the browser without
  authorized server-side resolution.
- Do not expose internal notes, margins, risk assessments, credentials, or
  cross-client records unless explicitly classified and authorized.
- Do not rely on hidden navigation, guessed URLs, or client-side filters for
  authorization.
- Do not claim a file, approval, invoice, payment, notification, or integration
  completed until authoritative state is verified.
- Do not use production client data in prompts, prototypes, or test fixtures.
- Do not make color, position, icons, or hover the only way to communicate state.
- Do not let convenience impersonation bypass approval, time bounds, reason, and
  audit requirements.
- Preserve an export and offboarding path for client-owned information.

## Recovery

If tenant ownership, resource authorization, source-of-truth state, or document
classification cannot be verified, deny the affected action and preserve the
client's last verified view. Reconcile upstream state before retrying writes,
record partial failures, and route legally binding, payment, privacy, or security
decisions to the authorized specialist or system.

## Output Contract

Provide the portal charter, tenant and role model, journey map, information
architecture, page and state inventory, source-of-truth map, documents,
communications, approvals, commerce views, support model, integrations, data
lifecycle, accessibility, observability, vertical-slice build plan, tests,
deployment and operations, risks, assumptions, and open decisions.

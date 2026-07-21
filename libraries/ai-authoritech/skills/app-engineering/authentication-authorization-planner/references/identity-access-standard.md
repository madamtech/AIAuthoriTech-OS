# Identity and Access Standard

## Authentication assurance

Choose methods from threat, consequence, population, accessibility, and recovery
requirements. Consider passkeys, federated SSO, verified email links, passwords
with secure management, authenticator applications, hardware factors, and recovery
codes. Avoid SMS as the sole protection for high-consequence actions when stronger
options are feasible.

Require step-up or recent authentication for sensitive changes, credential
management, data export, high-value transactions, privileged administration, and
other consequential actions.

## Authorization decision

Evaluate:

`authenticated actor + tenant + resource + action + current conditions -> allow or deny`

Conditions may include membership status, ownership, role, relationship, resource
state, assurance level, approval, environment, time, location policy, or risk
signal. Deny by default and avoid broad fallback grants.

## Session contract

Define issuance, token audience, scope, secure storage, rotation, idle and absolute
expiry, revocation, password or factor-change response, device and session
visibility, theft detection, CSRF protection, and server-side invalidation.

## Privileged access

Separate customer roles, application administration, infrastructure operation, and
support. For elevated access require purpose, least privilege, approval when
appropriate, short duration, prominent indication, complete audit, and user or
owner notification where policy requires it.

## Required tests

Test registration and verification abuse, enumeration, credential stuffing,
session fixation and replay, revoked and expired sessions, CSRF, account linking,
recovery takeover, IDOR or object-level authorization, horizontal and vertical
privilege escalation, cross-tenant access, stale memberships, service-token scope,
administrator and support access, audit completeness, and emergency revocation.

---
name: agent-marketplace-packager
description: Convert a validated AI agent into a transparent, installable, supportable marketplace package with audience positioning, evidence-backed capability claims, prerequisites, dependencies, permissions, data and privacy disclosures, configuration, onboarding, evaluation evidence, licensing, pricing inputs, support, compatibility, release channels, updates, deprecation, and retirement. Use for internal catalogs, commercial marketplaces, client distribution, white-label packages, or solution bundles - not agent design, QA, deployment, legal approval, pricing authorization, or publishing without explicit permission. Use when asked to (1) create agent marketplace packager, (2) review agent marketplace packager, (3) improve agent marketplace packager, or (4) standardize agent marketplace packager.
---

# Agent Marketplace Packager

Package the validated product that exists, not the product marketing wishes existed.

## Procedure

1. Identify the exact approved agent artifact, configuration fingerprint, business
   owner, target marketplace, distribution model, audience, geography, release
   channel, maturity, and support model.
2. Confirm QA, security, privacy, licensing, dependency, and release evidence.
   Block packaging for sale or general availability when critical evidence or
   accountable ownership is missing.
3. Define the user problem, ideal customer profile, buyer, operator, end user,
   intended outcomes, prerequisites, exclusions, and measurable value.
4. Build the package manifest with
   [references/agent-marketplace-standard.md](references/agent-marketplace-standard.md).
   Include immutable identities and versions for every included asset and adapter.
5. Write capability claims, examples, limitations, risk disclosures, and
   performance statements that trace to representative evidence.
6. Document required platforms, models, accounts, connectors, permissions,
   credentials, data sources, configuration, human approvals, quotas, and expected
   third-party costs.
7. Explain what data is collected, generated, transmitted, stored, remembered,
   logged, shared, retained, corrected, exported, and deleted, including relevant
   owner and processor roles.
8. Define installation, configuration validation, onboarding, sample use,
   acceptance checks, safe defaults, troubleshooting, uninstall, data export, and
   complete removal.
9. Define license inputs, intellectual-property ownership, third-party notices,
   acceptable use, warranty and liability review points, service terms, support
   scope, and customer responsibilities. Route legal decisions to qualified review.
10. Develop pricing inputs from value, included capability, consumption, external
    cost, support burden, risk, margin target, limits, overages, trials, refunds,
    and packaging tiers. Route final commercial terms for business approval.
11. Define semantic versioning, compatibility, update policy, migration,
    vulnerability response, release notes, rollback, deprecation notice, data
    portability, end-of-support, and retirement.
12. Run package-integrity, clean-install, permissions, disclosure, onboarding,
    evaluation, upgrade, downgrade, uninstall, and entitlement tests before
    recommending publication.
13. Deliver with
    [assets/agent-marketplace-package-template.md](assets/agent-marketplace-package-template.md).

## Guardrails

- Do not publish, list, price, license, or sell without explicit authorization.
- Do not claim certification, compliance, safety, accuracy, ROI, compatibility, or
  production readiness beyond available evidence and approved scope.
- Do not hide required permissions, data use, third-party costs, human work,
  limitations, or vendor dependencies.
- Do not include secrets, customer data, private prompts, internal-only knowledge,
  or unlicensed assets in a distributable package.
- Do not make uninstall mean only removing the interface; cover credentials,
  integrations, stored data, memory, indexes, logs, and active workflows.
- Do not silently change entitlements, data practices, authority, or consequential
  behavior through an update.
- Keep marketplace-specific listing fields in adapters.

## Output Contract

Provide the readiness decision, package manifest, positioning and evidence-backed
claims, prerequisites and dependencies, permission and data disclosures,
installation and removal guides, evaluation evidence, pricing and legal review
inputs, support and service model, compatibility and lifecycle policy, publication
checklist, risks, and required approvals.

## Recovery

If QA, ownership, permissions, licensing, or privacy evidence is missing, return a
blocked readiness decision and remediation list. If a claim exceeds evidence,
remove or qualify it. If publication authority is absent, prepare the package and
approval checklist only; do not list, price, license, sell, or publish it.

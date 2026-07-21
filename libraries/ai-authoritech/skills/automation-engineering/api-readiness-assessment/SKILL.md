---
name: api-readiness-assessment
description: Assess whether APIs can safely and reliably support a proposed automation by evaluating capability coverage, documentation, authentication, authorization, schemas, limits, consistency, errors, webhooks, environments, observability, support, security, and lifecycle. Use before committing to an API-based integration. Do not infer readiness from endpoint existence or vendor claims alone.
---

# API Readiness Assessment

1. Trace every automation requirement to an exact API operation, version, environment, and owner.
2. Verify documentation, schemas, examples, changelog, support, sandbox, credentials, and access approval.
3. Assess authentication, scopes, object- and field-level authorization, tenancy, encryption, and audit.
4. Test CRUD and search semantics, pagination, filters, bulk operations, concurrency, consistency, and idempotency.
5. Measure limits, latency, throughput, quotas, timeouts, errors, retries, webhook delivery, and recovery.
6. Review versioning, deprecation, compatibility, data residency, retention, and vendor dependencies.
7. Use a representative proof of capability without destructive production effects.
8. Rate each requirement supported, conditional, unsupported, or unknown; identify alternatives and blockers.
9. Deliver evidence, coverage matrix, risks, controls, proof results, cost, and readiness verdict.

## Rules

- Do not test destructive operations in production without explicit authorization and recovery.
- Do not expose credentials or sensitive response data in reports.
- Do not treat a successful happy-path call as operational readiness.
- Do not hide undocumented or untested behavior behind a passing aggregate score.

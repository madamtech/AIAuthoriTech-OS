# API Readiness Standard

Map every automation requirement to a documented operation, version, environment, owner, permission, and acceptance test. Verify schemas, authentication, object and field authorization, tenancy, pagination, concurrency, idempotency, limits, errors, webhooks, consistency, observability, lifecycle, and support with sanitized evidence.

Rate each requirement supported, conditional, unsupported, or unknown. A happy-path call is not operational readiness. Test representative non-destructive behavior in an approved environment, including invalid input, duplicates, throttling, timeout, partial failure, replay, and recovery. Treat undocumented behavior and environment differences as risks. Block a ready verdict when required capability, authorization, recovery, or lifecycle support is unknown.

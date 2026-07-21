# Error Log Analysis Standard

## Source quality

For every source record:

- producer, collector, store, query, and access method;
- environment, version, region, host or instance, and time window;
- timestamp format, zone, resolution, source clock, drift, and ingestion delay;
- sampling, filtering, rate limiting, buffering, truncation, and loss behavior;
- schema version, retention, immutability, and known blind spots.

Assign quality as high, medium, or low with rationale.

## Privacy and secrets

Analyze the minimum required records and fields. Redact credentials, API keys,
tokens, cookies, authorization headers, private keys, connection strings, payment
data, personal identifiers, sensitive content, and raw prompts or outputs when
they are not essential.

Use stable, non-reversible surrogates when cross-record correlation is required.
Record which fields were removed or transformed. Never put sensitive samples in a
report to demonstrate that redaction was necessary.

## Canonical fields

Preserve the raw event and derive, when available:

`timestamp_utc`, `timestamp_raw`, `source`, `service`, `environment`, `version`,
`region`, `instance`, `severity`, `event_name`, `message_template`, `trace_id`,
`span_id`, `request_id`, `operation_id`, `job_id`, `resource_surrogate`,
`tenant_surrogate`, `actor_surrogate`, `status`, `outcome`, `duration_ms`,
`exception_type`, `retry_number`, `ingest_timestamp`, and `quality_flags`.

Do not invent missing fields.

## Signature grouping

Normalize only variable tokens such as safe identifiers, timestamps, counters,
addresses, paths, and values. Preserve exception type, component, operation, code
location, status, and semantic message.

For every signature retain:

- pattern and representative redacted examples;
- count and unique operation estimate;
- first and last occurrence;
- affected environments, versions, and cohorts;
- rate and change from baseline;
- grouping confidence and known collision risk.

## Correlation strength

- **Direct:** shared trace, request, operation, job, or authoritative identifier.
- **Strong:** deterministic mapping plus compatible time and state.
- **Moderate:** multiple aligned dimensions within a bounded window.
- **Weak:** time proximity or a common high-cardinality dimension only.

Label the strength. Never present a weak association as one transaction.

## Baselines and ranking

Compare like-for-like denominators such as errors per request, failed jobs per
attempt, affected users per active users, or timeouts per dependency call.
Segment by release, environment, region, tenant class, device, input class, and
feature flag where relevant.

Rank by user or business outcome, unique affected operations, rate increase,
breadth, duration, recurrence, security or data exposure, recoverability, and
confidence. Use raw line count only as supporting context.

## Finding language

Use:

- **Observed:** directly present in retained evidence.
- **Associated:** correlated but causality is not established.
- **Anomalous:** materially differs from the chosen baseline.
- **Hypothesis:** predicts additional evidence and requires a discriminating test.

State evidence IDs, limitations, alternative explanations, confidence, and the
next query or test.

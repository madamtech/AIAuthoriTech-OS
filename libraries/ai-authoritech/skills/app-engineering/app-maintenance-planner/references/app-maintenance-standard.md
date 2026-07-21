# Application Maintenance Standard

## Service ownership

Maintain a catalog entry for each production component with business owner,
technical owner, support owner, repository, environment, criticality, data class,
dependencies, credentials or secrets location without values, monitoring,
runbook, lifecycle state, support end date, and replacement or retirement plan.

## Operating signals

Measure business outcomes and critical journeys alongside:

- availability, correctness, latency, saturation, errors, and backlog;
- authentication, authorization, integration, and data-freshness health;
- security, privacy, accessibility, compatibility, and resilience findings;
- incident count, detection and restoration time, recurrence, and support load;
- dependency age, vulnerabilities, patch latency, and end-of-life exposure;
- capacity, storage growth, unit cost, budget variance, and vendor consumption.

Define the source, calculation, window, segmentation, target, alert, owner, and
response for each signal. Validate telemetry and alerts periodically.

## Maintenance cadence

| Cadence | Typical work |
|---|---|
| Continuous | Alerts, incidents, security advisories, dependency and vendor notices |
| Weekly | Support trends, failed jobs, queues, data freshness, backup exceptions |
| Monthly | Patch review, access exceptions, cost, capacity, certificates, backlog |
| Quarterly | Service review, SLOs, risks, dependencies, documentation, restore sample |
| Annually | Continuity exercise, recovery objectives, data lifecycle, vendor exit, retirement fitness |

Adjust cadence to criticality and obligations. Assign every activity an owner,
evidence artifact, due date, escalation, and exception process.

## Vulnerabilities and dependencies

Track direct and transitive software, runtimes, operating systems, images, managed
services, APIs, models, SDKs, and client versions. Assess severity together with
exploitability, reachability, exposure, controls, and business impact. Define:

- routine and emergency patch windows;
- test and deployment paths;
- version-support and end-of-life thresholds;
- signed or checksummed artifact provenance;
- exception owner, rationale, controls, approval, and expiry;
- verification and evidence after remediation.

## Backup, restore, and continuity

Map each business dataset and configuration source to backup and recovery
requirements. Test restore into an isolated environment, verify integrity and
application usability, reconcile counts and relationships, record elapsed time,
and address gaps. Exercise dependency outages, credential loss, region failure,
vendor unavailability, corrupted data, and loss of key personnel as appropriate.

## Problem and technical-debt management

Link recurring incidents and support demand to causal analysis. Track known
errors, workarounds, permanent corrections, regression coverage, and measurable
outcomes. Prioritize technical debt using reliability, security, compliance,
developer productivity, operational toil, change failure risk, and cost of delay.

## Data and service retirement

Before retirement, identify consumers, exports, contractual duties, legal holds,
retention, deletion, audit evidence, downstream integrations, domains,
certificates, accounts, secrets, jobs, queues, backups, infrastructure, licenses,
and vendor contracts. Verify each disposition and preserve only required evidence.

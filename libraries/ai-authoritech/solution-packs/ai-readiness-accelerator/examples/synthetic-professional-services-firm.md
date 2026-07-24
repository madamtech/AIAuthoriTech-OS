# Controlled Test: Synthetic Professional-Services Firm

This scenario is fictional. It contains no client, i-PRO, or MadamAllure information.

## Engagement

- Engagement ID: `SYN-AA-READINESS-001`
- Client: Northstar Advisory Group, a fictional 85-person professional-services firm
- Sponsor: Chief Operating Officer
- Objective: Reduce proposal turnaround and administrative rework without exposing confidential client information
- Scope: Business development, proposal preparation, project intake, knowledge retrieval, and reporting
- Exclusions: Automated contract approval, autonomous pricing, employee performance decisions, and direct production-system changes

## Available evidence

| Evidence | Synthetic observation | Confidence |
|---|---|---|
| Proposal log | 240 proposals per year; median turnaround 6.2 business days | High |
| Interviews | Repeated searching, copying, formatting, and approval delays | Medium |
| Rework sample | 18% required correction for stale credentials, inconsistent scope, or pricing mismatch | Medium |
| Systems | CRM, document repository, email, finance, and project-management tools lack a common identifier | High |
| Governance | No AI policy, approved tool list, data classification, or output-review standard | High |
| Data | Past proposals contain confidential client material and uneven metadata | High |

## Readiness snapshot

| Dimension | Score | Confidence | Finding |
|---|---:|---|---|
| Leadership and strategy | 3/5 | Medium | Sponsor and outcome exist, but ownership beyond the pilot is incomplete. |
| Business process readiness | 3/5 | Medium | Proposal flow is repeatable but has undocumented exceptions and approvals. |
| Data readiness | 2/5 | High | Useful content exists, but confidentiality, freshness, and metadata controls are weak. |
| Technology and integration | 2/5 | Medium | APIs may exist, but identity and source-of-truth rules are unresolved. |
| Governance, risk, and compliance | 1/5 | High | Policy, approved tools, review, retention, and incident controls are absent. |
| Workforce and change readiness | 3/5 | Medium | Staff see the problem, but training and role changes are undefined. |
| Security and privacy | 1/5 | High | Confidential proposal content creates a launch blocker without isolation and access controls. |
| Measurement and scalability | 2/5 | Medium | Baseline turnaround exists; quality, adoption, and cost measures need definitions. |

Weighted readiness: 42%, **Early Readiness**. This is sufficient for a contained design and data-remediation phase, not broad deployment.

## Prioritized opportunity portfolio

| Rank | Opportunity | Value | Feasibility | Risk | Decision |
|---:|---|---|---|---|---|
| 1 | Proposal intake and completeness assistant | High | High | Low | Pilot after human-review design |
| 2 | Approved-content retrieval with citations and access controls | High | Medium | Medium | Prepare data and permissions first |
| 3 | Proposal first-draft assistant using approved modules | High | Medium | High | Gate behind retrieval, review, and confidentiality controls |
| 4 | Project-intake summarization | Medium | High | Medium | Controlled pilot with retention rules |
| 5 | Autonomous pricing recommendation | High | Low | High | Do not pilot; requires governed pricing authority and stronger evidence |

## ROI scenario for the first pilot

Assumptions are illustrative, not client facts:

- 240 proposals/year
- 4.5 addressable labor hours/proposal
- $62 loaded hourly cost
- 25% to 45% addressable-time reduction
- $24,000 to $42,000 first-year implementation and operating cost

Estimated gross annual capacity value: $16,740 to $30,132. The scenario does not support a confident positive first-year cash ROI at the upper cost range. The recommended decision is a narrow pilot measured on turnaround, rework, adoption, confidentiality incidents, and reviewer effort before any scaling claim.

## Roadmap

### 0–30 days

- Assign executive, process, data, security, and quality owners.
- Establish data classification, approved tools, prohibited uses, review, retention, and incident rules.
- Validate the current proposal workflow and baseline metrics.
- Create an approved-content inventory and quarantine stale or rights-uncertain material.

### 31–60 days

- Prototype proposal intake and completeness checks using synthetic or sanitized data.
- Define retrieval permissions, citations, freshness, and correction behavior.
- Run accessibility, privacy, security, failure, and human-review tests.

### 61–90 days

- Run a limited pilot with trained users and mandatory reviewer approval.
- Compare against a baseline or holdout.
- Stop on confidentiality leakage, unsupported claims, material quality regression, or missing audit evidence.
- Decide whether to revise, scale, or retire the pilot.

## Controlled-test result

The workflow correctly prevented a broad generative proposal deployment, rejected false ROI certainty, separated data remediation from implementation, and preserved human authority for pricing, claims, and release. Result: **conditional pass**.

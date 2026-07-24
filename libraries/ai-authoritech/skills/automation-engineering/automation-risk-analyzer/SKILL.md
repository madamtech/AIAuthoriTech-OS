---
name: automation-risk-analyzer
description: Analyze automation risks across business decisions, data, security, privacy, integrations, reliability, fraud, compliance, vendors, human oversight, operations, and change. Use during prioritization, architecture, implementation, release, or review to produce evidence-linked scenarios, controls, owners, residual risk, and acceptance decisions. Do not provide unsupported compliance certification.
---

# Automation Risk Analyzer

Use the [automation risk standard](references/automation-risk-standard.md) to evaluate scenarios and control evidence. Record inherent, current, target, and residual risk in the [automation risk register template](assets/automation-risk-register-template.md).

## Procedure

1. Define scope, assets, stakeholders, decisions, environments, obligations, risk appetite, and impact scales.
2. Model failure, misuse, abuse, unauthorized access, bad data, partial execution, duplication, outage, and vendor scenarios.
3. Identify causes, affected people and systems, detectability, exposure, likelihood evidence, and business impact.
4. Review preventive, detective, corrective, recovery, human approval, segregation, and audit controls.
5. Test controls and distinguish inherent, current, target, and residual risk.
6. Block or escalate unacceptable safety, privacy, authorization, financial, legal, or irreversible risks.
7. Assign owners, actions, deadlines, evidence, retest, monitoring, exceptions, and acceptance authority.
8. Deliver risk register, scenarios, control map, residual decisions, assumptions, and review triggers.

## Guardrails

- Do not reduce severe risks through averaging.
- Do not call a documented control effective without implementation evidence.
- Do not assign risk acceptance to the automation itself.
- Do not use numeric likelihood precision unsupported by evidence.

## Recovery

If a severe risk lacks an accountable owner, effective control, recovery path, or authorized acceptance, block release or expansion of the affected automation. Preserve the last safe state, isolate unsafe effects where possible, document the evidence gap, and escalate to the named decision authority.

## Output Contract

Deliver a completed risk package containing scope, scales, evidence-linked scenarios, causes, impacts, affected parties, existing and target controls, control tests, inherent and residual ratings, actions, owners, deadlines, exceptions, acceptance authority, monitoring, and review triggers.

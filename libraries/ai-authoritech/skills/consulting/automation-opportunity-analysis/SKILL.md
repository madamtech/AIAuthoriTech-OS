---
name: automation-opportunity-analysis
description: Evaluate and prioritize automation opportunities from validated current-state workflows using evidence-backed value, feasibility, effort, data readiness, integration readiness, control, security, change, and operational-risk criteria. Use for automation portfolios, workflow improvement analysis, AI use-case screening, or deciding what to automate first—not for detailed solution architecture or automating an undocumented process.
---

# Automation Opportunity Analysis

Evaluate outcomes, not technology novelty.

1. Confirm process scope, current-state validation status, baseline volume, timing,
   errors, costs, service impact, systems, data, controls, and accountable owner.
2. Decompose broad ideas into independently deliverable opportunities.
3. Reject or defer candidates whose underlying process is materially unstable,
   unnecessary, disputed, or lacks an accountable outcome.
4. Score each candidate with
   [references/opportunity-scoring.md](references/opportunity-scoring.md).
5. Record evidence strength for every score; use `insufficient evidence` instead
   of an invented midpoint.
6. Apply explicit blockers and prerequisites separately from the numeric score.
7. Classify each candidate:
   - quick win;
   - strategic investment;
   - foundation first;
   - redesign before automation;
   - do not pursue.
8. Sequence opportunities by dependencies, risk reduction, learning value, and
   time to measurable outcome.
9. Deliver the portfolio using
   [assets/opportunity-portfolio-template.md](assets/opportunity-portfolio-template.md).

## Decision rules

- Prefer elimination or simplification when it achieves the outcome more safely.
- Do not equate high manual effort with high automation suitability.
- Do not recommend autonomous execution for consequential decisions without
  defined oversight, appeal, monitoring, and authority.
- Treat sensitive data, security gaps, missing interfaces, poor data quality,
  unclear ownership, and absent controls as prerequisites or blockers.
- Keep benefits as ranges when baseline evidence is uncertain.
- Separate AI-assisted, rules-based, integration, and fully automated approaches.

## Handoff

Provide the ranked backlog, rationale, assumptions, prerequisites, recommended
automation pattern, expected outcome measures, and candidates requiring deeper
architecture, ROI modeling, governance review, or process redesign.

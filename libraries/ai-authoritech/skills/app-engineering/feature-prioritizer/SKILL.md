---
name: feature-prioritizer
description: Normalize, compare, sequence, and recommend product features using evidence-backed user and business value, strategic alignment, necessity, risk reduction, learning value, reach, confidence, effort, time criticality, dependencies, operational burden, and portfolio capacity. Use for product backlogs, MVP definition, release slicing, roadmap tradeoffs, inherited feature lists, or reprioritization - not detailed requirements, estimation commitments, architecture, or final investment approval.
---

# Feature Prioritizer

Prioritize validated problems and outcomes, not stakeholder volume or polished
feature pitches.

## Procedure

1. Confirm the product outcome, strategy, target users, release horizon, available
   capacity, fixed commitments, risk tolerance, decision owner, and evidence
   standard.
2. Normalize each candidate into a stable identifier, problem, beneficiary,
   desired outcome, baseline, proposed behavior, evidence, success measure,
   urgency, dependencies, rough effort range, owner, and confidence.
3. Merge duplicates, split bundles with independently valuable outcomes, and
   separate features from defects, incidents, technical debt, research, enablers,
   compliance work, and operational obligations.
4. Screen candidates for strategic fit, genuine user or business need, measurable
   outcome, feasibility signal, ownership, and material constraints. Mark missing
   evidence rather than inventing it.
5. Classify mandatory work separately: legal or contractual obligations,
   critical security and privacy remediation, accessibility barriers, unsupported
   dependencies, continuity risks, and severe defects. Do not force these items to
   compete only on discretionary value.
6. Select a scoring method and apply it consistently using
   [references/feature-prioritization-standard.md](references/feature-prioritization-standard.md).
   Publish the scale, weights, formula, confidence, sources, and tie-break rules.
7. Score user value, business value, strategic alignment, necessity, risk
   reduction, learning value, reach, confidence, effort, time criticality,
   operational burden, and reversibility only where the evidence supports them.
8. Model dependencies, shared enablers, sequencing, mutually exclusive options,
   platform work, capacity by specialty, work in progress, and portfolio
   concentration. Do not rank impossible sequences as executable.
9. Define the smallest coherent release slices. Preserve an end-to-end user
   outcome, required controls, instrumentation, support, and recovery; do not
   create an MVP that is merely incomplete.
10. Test sensitivity by varying uncertain inputs and reasonable weights. Flag
    candidates whose rank changes materially and identify the evidence needed to
    resolve the decision.
11. Assign one disposition: commit, validate next, sequence after dependency,
    maintain as option, defer until trigger, decline, or mandatory remediation.
12. For validation items, define the riskiest assumption, smallest evidence-
    generating test, owner, time box, metric, threshold, guardrail, and decision
    date.
13. Build a balanced recommendation across customer outcomes, growth or revenue,
    risk and compliance, reliability, platform health, learning, and maintenance.
    Show explicit capacity tradeoffs.
14. Record dissent, overrides, rationale, decision owner, date, expected outcome,
    review trigger, and expiration. Re-score when evidence, strategy, risk,
    dependencies, costs, or capacity materially changes.
15. Deliver with
    [assets/feature-prioritization-template.md](assets/feature-prioritization-template.md).

## Guardrails

- Do not equate the loudest stakeholder, largest customer, or highest executive
  title with the highest product value.
- Do not use a numerical score to override safety, legal, privacy, accessibility,
  security, or continuity gates.
- Do not assign neutral values to unknown criteria; mark insufficient evidence.
- Do not treat effort as a precise commitment before appropriate discovery.
- Do not prioritize a feature without naming the beneficiary and measurable
  outcome.
- Do not hide mandatory enablers or maintenance work beneath visible features.
- Do not present ranking as objective when weights and judgments are subjective.
- Do not commit more work than the constrained delivery system can absorb.

## Recovery

If candidates are bundled, incomparable, unsupported, or constrained by unresolved
dependencies, normalize or separate them and mark insufficient evidence before
ranking. If a mandatory safety, legal, privacy, accessibility, security, or
continuity gate applies, route it outside discretionary scoring and surface the
decision owner and required action.

## Output Contract

Provide the normalized backlog, evidence inventory, mandatory-work register,
method and assumptions, scored comparison, dependency graph, capacity constraints,
sensitivity findings, recommended release slices, dispositions, validation
experiments, overrides, risks, decision log, and review triggers.

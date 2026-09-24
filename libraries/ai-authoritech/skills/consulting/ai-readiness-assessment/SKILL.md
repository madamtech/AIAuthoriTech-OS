---
name: ai-readiness-assessment
description: Assess an organization's evidence-backed readiness to adopt, govern, implement, and scale AI; identify blockers and suitable opportunities; and produce a prioritized action plan. Use for AI readiness reviews, consulting discovery, maturity baselines, pre-implementation assessments, or reassessments—not legal certification or detailed process mapping. Use when asked to (1) assess ai readiness, (2) baseline ai readiness, (3) identify gaps in ai readiness, or (4) prioritize improvements to ai readiness.
---

# AI Readiness Assessment

## Procedure

1. Confirm scope, audience, objectives, horizon, and evidence.
2. Score supported dimensions: leadership 15; process 15; data 15; technology 15;
   governance 15; workforce 10; security 10; measurement 5.
3. Mark unsupported criteria `insufficient evidence`; never score them zero.
4. Record sources, confidence, contradictions, and assumptions.
5. Calculate `sum((score/4)*weight) / evidenced weights * 100`.
6. Report evidence coverage; below 60% issue only a provisional result.
7. Report blockers separately from arithmetic.
8. Prioritize actions and produce a 30/60/90-day plan.

Apply [references/readiness-scoring-standard.md](references/readiness-scoring-standard.md)
and deliver with [assets/ai-readiness-report-template.md](assets/ai-readiness-report-template.md).

## Output Contract

Return an executive result, evidence coverage, dimension scores, confidence,
blockers, opportunity themes, prioritized actions, roadmap, assumptions, and
decisions requiring accountable approval. Label the result `provisional` when
coverage is below 60 percent or material evidence is disputed.

## Guardrails

Labels: 0–24 Not Ready; 25–44 Early Readiness; 45–64 Foundation Emerging;
65–79 Implementation Ready; 80–100 Scale Ready. Never infer enterprise readiness
from isolated tool use or recommend sensitive use cases without governance,
security, privacy, and accountable ownership evidence.

Do not claim legal compliance, certify controls, or treat a maturity average as
permission to deploy. Route detailed process mapping to Workflow Discovery and
detailed control assessment to AI Governance Review.

## Recovery

If evidence is incomplete, produce an evidence-gap register and provisional
findings instead of inventing scores. If accounts conflict, preserve each account,
identify the decision owner, and specify the evidence needed to resolve it.

# AI use-case scoring

Score evidenced criteria from 0 to 4.

| Criterion | Weight |
|---|---:|
| Strategic alignment | 10 |
| User and business value | 15 |
| Problem clarity and baseline quality | 10 |
| AI suitability and advantage | 10 |
| Data readiness and permission | 10 |
| Technical and integration feasibility | 10 |
| Process and owner readiness | 10 |
| Responsible-AI and control readiness | 10 |
| Measurement and experiment quality | 10 |
| Reuse and portfolio learning value | 5 |

Calculate `sum((score / 4) × weight)`. Report evidence coverage separately.

## Interpretation

- 80–100: implementation or scale candidate, subject to gates
- 65–79: experiment candidate
- 50–64: discovery or prerequisite work
- below 50: defer or reject

Below 60% evidence coverage, issue only a provisional tier. A prohibited or
unmitigated high-consequence case cannot advance regardless of score.

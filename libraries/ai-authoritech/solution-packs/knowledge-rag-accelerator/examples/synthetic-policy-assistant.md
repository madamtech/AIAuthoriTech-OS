# Controlled Synthetic Policy Assistant

A fictional company requested an internal assistant using synthetic policies with employee and manager access levels. Each source received owner, version, effective date, classification, and conflict precedence. Retrieval filtered by role before ranking and required exact citations.

Controlled tests covered ordinary questions, revoked policies, manager-only content, conflicting versions, missing evidence, prompt injection, and stale sources. The result was **conditional pass**: supported answers cited authorized evidence and unsafe cases abstained. Production readiness remained blocked pending real identity enforcement, rights verification, live-source refresh testing, security review, and owner approval.

# GPT-to-SKILL Gap Backlog — 2026-08-08

## Reconciliation result

All 93 captured Custom GPTs now have an explicit reconciliation decision against the governed 272-SKILL catalog.

- 58 GPTs: fully verified against existing reusable skills
- 2 GPTs: previously verified and retained
- 17 GPTs: partially mapped to existing skills with a documented capability gap
- 16 GPTs: intentional skill-gap decisions with no forced mapping
- 77 GPT manifests receive verified required/optional skill mappings
- 16 GPTs remain unmapped until a genuinely reusable skill exists

A skill-gap decision is intentional. It prevents unrelated existing skills from being attached merely because wording is similar.

## Highest-priority reusable skill families to add

### 1. Sales Enablement and Security Sales
Supports gaps across i-PRO Sales Governance Assistant, i-PRO Sales Intelligence variants, personalized i-PRO sales communication, Sales Meeting Prep, and ClassSecure Quote Builder.

Recommended reusable capabilities:
- Sales Account Brief Builder
- Sales Discovery and Meeting Prep
- Partner Review and Account Health Planner
- Objection Handling and Competitive Positioning
- Security Solution Quote / BOM Planner
- Sales Follow-Up and Demo Recap Builder
- Governed Product Claim Reviewer

### 2. Government Grants
Supports Dymin and Coach K.

Recommended reusable capabilities:
- Grant Opportunity Intake and Eligibility Reviewer
- Grant Readiness Audit
- Grant Narrative Builder
- Problem / Need Statement Builder
- Goals, Outcomes, and Evaluation Planner
- Use of Funds and Budget Narrative Builder
- Grant Sustainability Planner
- Grant Proposal QA Reviewer

### 3. Government Functional Documentation
Supports Systems Doc Agent, Software Doc Agent, HR Master Agent, and Master Admin Consultant without collapsing their NAICS-specific boundaries.

Recommended reusable capabilities:
- Government Functional Requirements Builder
- BRD / FRD Documentation Builder
- Government SOP and Procedure Builder
- Government UAT Script Builder
- Government Intake and Routing Designer
- Government Administrative Reporting Builder
- Government Change / Adoption Documentation Builder

### 4. HR and Workforce Documentation
Supports HR Master Agent.

Recommended reusable capabilities:
- Job Description Builder
- Competency Model Builder
- Skills Matrix Builder
- Training Needs Assessment Builder
- HR SOP Documentation Builder
- Workforce Documentation QA Reviewer

### 5. GovCon Business Development
Supports GovCon Strategist Pro.

Recommended reusable capabilities:
- GovCon Opportunity Qualifier
- Solicitation Requirements Extractor
- Capture Strategy Builder
- Capability Statement Builder
- Government Proposal Response Planner
- Compliance Matrix Builder

### 6. Music and Songwriting
Supports Lyrical Hitmaker and Urban Romance Lyrical Studio.

Recommended reusable capabilities:
- Song Concept Architect
- Lyric and Hook Builder
- Verse / Chorus Structure Designer
- Cadence and Vocal Delivery Planner
- Suno Production Sheet Builder
- Songwriting QA Reviewer

### 7. Creative Writing and Publishing
Supports PoeticPunch, Children's Best Selling Author, Urban Novelist, Naki – The Motivational Madam, and Poetic Justice.

Recommended reusable capabilities:
- Poetry and Spoken Word Builder
- Keepsake / Greeting Card Copy Builder
- Motivational and Affirmation Writer
- Children's Book Architect
- Fiction / Novel Architect
- Manuscript Continuity Manager
- Publishing Package Planner

### 8. Current Events and News
Supports News Plug.

Recommended reusable capabilities:
- News Discovery and Source Verifier
- Current Events Brief Builder
- News Summary and Context Writer
- Recency / Claim QA Reviewer

### 9. Consumer Credit
Supports the eight credit-repair / dispute GPTs and 90-Day Bank + Credit Optimizer.

Recommended reusable capabilities:
- Credit Report Issue Classifier
- Credit Dispute Evidence Organizer
- Credit Dispute Letter Builder
- Charge-Off Dispute Planner
- Collection Dispute Planner
- Late Payment Dispute Planner
- Hard Inquiry Dispute Planner
- Credit Optimization Roadmap
- Consumer Credit Compliance QA

## Lower-priority domain gaps

- Academic testing / standards alignment for Lone Star Scholar Prep
- General business coaching and accountability for Carter
- Salon-suite business operations for Salon Suite Builder
- High-stakes situational strategy for Za'ire

## Build rule

Do not create one skill per GPT. Build reusable capabilities only where multiple workflows can consume them or where a specialized domain capability is substantial enough to justify a governed SKILL.md asset. Existing skills must be reused before any new skill is created.

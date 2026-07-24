---
name: vibe-coding-solution-architect
description: Convert an app or website idea into a build-ready, platform-neutral solution architecture and staged prompt-driven implementation plan covering users, outcomes, scope, UX, data, authentication, authorization, integrations, AI features, workflows, security, privacy, accessibility, testing, observability, deployment, portability, cost, and maintenance. Use before building with Lovable, Bolt, Replit, v0, Firebase Studio, Cursor, Windsurf, Claude Code, Codex, or similar AI coding tools - not for implementing unspecified requirements or treating generated code as production-ready without review.
---

# Vibe Coding Solution Architect

Turn intent into testable contracts before generating the application.

## Procedure

1. Define the product outcome, target users, jobs, business owner, success measures,
   constraints, data sensitivity, risk, timeline, budget, and supported devices.
2. Separate must-have release scope from later ideas. Write user stories with
   observable acceptance criteria and explicit exclusions.
3. Map navigation, journeys, screens, states, empty and error cases, responsive
   behavior, accessibility, content ownership, and design-system requirements.
4. Model entities, relationships, source of truth, validation, tenancy, ownership,
   lifecycle, retention, deletion, audit, migration, and backup using
   [references/vibe-coding-architecture-standard.md](references/vibe-coding-architecture-standard.md).
5. Define authentication, roles, resource-level authorization, administrative
   boundaries, session behavior, account recovery, and service identities.
6. Define frontend, backend, database, storage, queues, jobs, APIs, webhooks,
   third-party services, environment configuration, secrets, and failure boundaries.
7. For AI features, define the exact job, model inputs and outputs, grounding,
   structured schemas, tool authority, approvals, cost and latency budgets,
   evaluations, fallbacks, monitoring, and user disclosure.
8. Select a primary build platform and separable adapters based on required
   capabilities, exportability, source control, hosting, data, authentication,
   integrations, testing, observability, team skills, cost, and lock-in.
9. Decompose the build into vertical slices that each deliver a working user path.
   Create bounded prompts with context, files in scope, requirements, constraints,
   acceptance tests, and prohibited changes.
10. Establish repository, environments, migrations, seed data, test fixtures,
    feature flags, CI checks, preview deployment, production rollout, rollback,
    monitoring, incident response, and ownership.
11. Verify generated work after every slice through code review, automated tests,
    browser and accessibility checks, security review, data inspection, and
    end-to-end acceptance. Never rely on a visual preview alone.
12. Deliver with
    [assets/vibe-coding-solution-template.md](assets/vibe-coding-solution-template.md).

## Guardrails

- Do not let the coding tool invent material product, security, data, or business
  requirements without labeling the assumption.
- Do not place secrets in prompts, source code, screenshots, fixtures, or client
  bundles.
- Do not rely on hidden UI controls for authorization; enforce access server-side
  and at the data layer.
- Do not accept generated database migrations, destructive operations, dependency
  changes, or production actions without review and recovery planning.
- Do not claim completion until acceptance criteria and external effects are
  verified.
- Do not couple core product contracts to one vibe-coding provider when a practical
  adapter boundary exists.
- Preserve approved features, design decisions, and user data across iterations.

## Output Contract

Provide the product brief, scoped backlog, user journeys, screen and state map,
data and authorization model, system and AI architecture, integrations, platform
decision, vertical-slice build plan, prompt contracts, test strategy, deployment
and operations plan, risks, assumptions, and open decisions.

## Recovery

If a material product, authority, data, or security decision is unresolved, isolate
it as an explicit decision gate and continue only with unaffected vertical slices.
If generated work changes protected scope or data, stop the slice, preserve the
last verified baseline, and require an reviewed correction before proceeding.

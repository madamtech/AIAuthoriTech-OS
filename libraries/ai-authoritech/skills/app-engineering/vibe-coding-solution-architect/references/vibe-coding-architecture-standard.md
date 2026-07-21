# Vibe Coding Architecture Standard

## Architecture layers

Define contracts for:

1. User experience and navigation
2. Client state and validation
3. Server-side business rules and authorization
4. Data, storage, search, and background work
5. Integrations, events, and external effects
6. AI models, prompts, knowledge, tools, and evaluations
7. Security, privacy, audit, observability, and operations
8. Platform adapters, deployment, and portability

## Feature contract

For every feature record:

- User and outcome
- Trigger, preconditions, main flow, and terminal state
- Inputs, validation, outputs, and external effects
- Empty, loading, denied, error, partial, retry, and recovery states
- Data read and written
- Authentication, authorization, and approval
- Accessibility and responsive behavior
- Analytics and audit events
- Acceptance and regression tests

## Platform decision

Score candidate platforms against mandatory capabilities, source export, version
control, frontend flexibility, backend and jobs, database, auth, secrets,
integrations, AI support, testing, preview environments, observability, security,
deployment, cost, support, and exit strategy. A popular tool is not automatically
the right tool.

## Prompt-driven build contract

Each build prompt should contain:

- Current artifact and relevant files
- One bounded outcome
- Requirements and acceptance criteria
- Architecture and design constraints
- Data and authorization rules
- Error, loading, empty, and responsive states
- Tests to add or run
- Files or features that must not change
- Required summary of changes, assumptions, and verification

Use small vertical slices. Commit or checkpoint known-good states between slices.

## Production gates

Require:

- Server and data-layer authorization tests
- Migration review, backups, and rollback
- Secret and dependency scanning
- Input validation and abuse controls
- Accessibility and responsive verification
- Unit, integration, and end-to-end tests
- AI evaluation and cost limits where applicable
- Logs, alerts, error handling, support, and ownership
- Clean environment deployment and recovery test

Generated code receives the same review as human-written code.

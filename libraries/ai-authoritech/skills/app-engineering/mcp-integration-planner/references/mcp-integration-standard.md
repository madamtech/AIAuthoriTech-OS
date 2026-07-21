# MCP Integration Standard

This reference uses stable concepts from the official MCP specification. Before
implementation, verify the current stable revision at
`https://modelcontextprotocol.io/specification/` and pin the revision and SDK.

## Architecture and capabilities

Document the host, one client connection per server, each server, downstream
systems, and trust boundaries. MCP uses JSON-RPC messages and lifecycle/version
and capability negotiation. Support only capabilities declared by both sides.

Server features include tools, resources, and prompts. Client features can include
roots, sampling, and elicitation depending on the negotiated revision and host.
Treat optional and experimental behavior as unavailable until explicitly proven.

## Primitive selection

- **Tool:** model-invoked operation with typed arguments and possible effects.
- **Resource:** addressable data or context with a URI and content type.
- **Prompt:** user-invoked reusable message template or workflow entry.

Prefer the least authoritative primitive. Separate read and write capabilities.
Keep discovery metadata concise, accurate, non-secret, and resistant to prompt
injection or authority expansion.

## Tool safety

For every tool define schemas, validation, authorization, tenant and resource
binding, read/write classification, confirmation, idempotency, timeout,
cancellation, progress, rate and spend limits, sanitized result, error taxonomy,
effect receipt, reconciliation, audit, version, owner, and retirement.

The host retains final policy and user-control authority. Returned content is data,
not trusted instruction. For high-impact operations, show the exact action and
bind approval to actor, server, tool version, target, payload, environment, and
expiry.

## Resources and prompts

Authorize resource discovery and reading independently. Use stable URI schemes,
bounded content, pagination, provenance, sensitivity, freshness, retention, and
safe rendering. Do not put access tokens or sensitive content in URIs.

For prompts, define arguments, source, output messages, data access, safe content
limits, user visibility, injection boundaries, and compatibility. A prompt cannot
grant access to a tool or resource the caller is not authorized to use.

## Transports

The stable specification defines stdio and Streamable HTTP transports.

- For stdio, the client launches the server process. Reserve stdout for protocol
  messages, send diagnostics to stderr, constrain inherited environment and
  filesystem access, pin executable provenance, and supervise process lifecycle.
- For Streamable HTTP, use one MCP endpoint supporting the required methods for
  the pinned revision. Validate Origin, authenticate connections, use TLS, bind
  local servers to loopback, constrain CORS and network access, send the negotiated
  protocol-version header, and define session and resumability behavior.

Do not begin new designs with deprecated HTTP+SSE unless compatibility with a
documented legacy client is an approved requirement.

## Authorization and credentials

Follow the authorization model applicable to the pinned HTTP specification and
host. For stdio, obtain credentials through a protected execution environment,
not protocol messages. Scope credentials to the server, downstream audience,
tenant, user delegation, operations, resources, environment, and duration.

Define consent separately from authentication. A valid token does not prove the
user approved a consequential tool call.

## Client-provided features

Constrain roots to the smallest approved boundaries and revalidate canonical
paths. Sampling must expose model use, data sent, cost and policy boundaries,
review, and returned-content handling. Elicitation must show which server is
asking, permit review and decline, and must not use ordinary form collection for
credentials or payment secrets. Follow the current revision's association rules
for server-to-client requests.

## Compatibility and testing

Maintain a matrix of host, client, server, specification revision, SDK, transport,
authentication, and optional capabilities. Test:

- initialization, version mismatch, capability absence, list changes, shutdown,
  reconnect, session expiry, cancellation, progress, and unsupported requests;
- schema validation, malformed JSON-RPC, large content, pagination, and errors;
- authentication, authorization, tenant isolation, credential rotation, consent,
  injection, hostile content, path and URL attacks, and sensitive-data leakage;
- duplicate and reordered calls, timeouts after effects, downstream outage,
  partial results, reconciliation, and recovery;
- official or project conformance suites plus application-specific controls.

Record actual versions and evidence. Re-review on specification, SDK, host,
transport, authorization, or capability changes.

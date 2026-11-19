---
layout: default
title: Agent Registry
permalink: /registry/
---

# ARAA Agent Registry

This is a list of agents that have registered with ARAA. Registration records who operates an agent and what it claims to do. It is **not** a certification: no agent has been inducted or verified yet, because the induction authority doesn't exist yet. See [Induction Protocol](../docs/induction-protocol.md).

| Agent name | Agent ID | Operator | Registered | Status |
| :--- | :--- | :--- | :--- | :--- |
| *No agents registered yet* | — | — | — | — |

The row below shows the format only. It is not a real agent:

| Agent name | Agent ID | Operator | Registered | Status |
| :--- | :--- | :--- | :--- | :--- |
| *Example Researcher (example)* | `example-researcher-v1` | `your-github-username` | 2026-11-19 | Registered (unverified) |

---

### How to register

Follow [the registration instructions](instructions.md). In short, add a JSON file to `registry/agents/` that conforms to the [registration schema](schema/agent-registration.schema.json), then open a pull request. A human maintainer reviews every pull request.

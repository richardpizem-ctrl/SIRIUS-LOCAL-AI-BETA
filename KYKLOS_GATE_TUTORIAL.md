# SIRIUS Customs Gate (COLNIK) – Security & Architecture Tutorial

## 1. Overview

The **SIRIUS Customs Gate (COLNIK)** is the central security and access‑control module in the SIRIUS runtime.  
Its primary purpose is to:

- **Control what enters and leaves the system** (requests, data, commands, agents).
- **Enforce security policies** across all layers (identity, permissions, KG, runtime).
- **Protect the core reasoning and KG engine** from malformed, malicious, or unauthorized operations.
- **Provide explainable decisions** about why something was allowed, blocked, or transformed.

Think of COLNIK as a **border checkpoint** for the entire SIRIUS ecosystem.

---

## 2. High‑level responsibilities

COLNIK will:

- **Inspect** every incoming request (from user, agent, API, or subsystem).
- **Validate** identity, permissions, and intent.
- **Classify** the request (safe, risky, unknown, forbidden).
- **Apply policies** (allow, deny, sanitize, escalate, log).
- **Route** the request to the correct subsystem (KG, parser, workflow, reasoning).
- **Log and explain** every critical decision for auditing and debugging.

When fully implemented, **no critical operation** in SIRIUS will bypass COLNIK.

---

## 3. Security layers (current and planned)

COLNIK is not a single check—it is a **stack of security layers**.  
Below is an overview of the layers we already have conceptually integrated, and what they do.

### 3.1 Identity Layer

**Purpose:**  
Verify *who* is making the request.

**Responsibilities:**

- Check **user identity** (local user, system agent, external caller).
- Distinguish between:
  - Human user
  - Internal SIRIUS agent (e.g., SYSTEM_AGENT, ENVOY)
  - External integration (future)
- Attach identity metadata to the request (who, when, origin).

**Effect:**  
No anonymous critical operations. Every action is tied to an identity.

---

### 3.2 Role & Permission Layer

**Purpose:**  
Verify *what* the identity is allowed to do.

**Responsibilities:**

- Map identity to **roles** (e.g., `admin`, `developer`, `runtime`, `agent`, `read-only`).
- Check **permissions** for:
  - KG operations (KG_SET, KG_GET, KG_RELATE, KG_REMOVE_RELATION, etc.)
  - Runtime operations (start/stop modules, pipelines)
  - Configuration changes (policies, env, security settings)
- Enforce **least privilege**:
  - Only allow the minimum required actions.
  - Block or downgrade dangerous operations.

**Effect:**  
Even a valid identity cannot perform actions outside its role.

---

### 3.3 Policy Layer (ENVOY / Security Policies)

**Purpose:**  
Apply **high‑level security rules** and policies.

**Responsibilities:**

- Use **policy files** (e.g., `policies_envoy.json`) to define:
  - Allowed operations per role.
  - Forbidden combinations (e.g., `KG_REMOVE_RELATION` + `admin` without justification).
  - Sensitive entities and relations in the KG.
- Enforce **global rules**:
  - No direct modification of core ontology without explicit override.
  - No destructive operations without logging and explanation.
  - No bypass of COLNIK for critical paths.

**Effect:**  
Security is **configurable** and **centralized**, not hard‑coded.

---

### 3.4 Input Validation & Sanitization Layer

**Purpose:**  
Protect the system from malformed or dangerous input.

**Responsibilities:**

- Validate **syntax** of commands (KG, parser, workflow).
- Validate **structure** of data (entities, relations, attributes).
- Sanitize:
  - Unexpected tokens
  - Dangerous patterns
  - Oversized payloads
- Reject or transform input that could:
  - Break the runtime
  - Corrupt the KG
  - Cause infinite loops or runaway workflows

**Effect:**  
Only **well‑formed, safe input** reaches the core modules.

---

### 3.5 Runtime Safety Layer

**Purpose:**  
Protect the **runtime pipeline** and modules.

**Responsibilities:**

- Check whether the requested operation:
  - Starts/stops critical modules (KG, ReasoningEngine, WorkflowEngine, Parser).
  - Modifies runtime configuration.
  - Changes system behavior in a persistent way.
- Enforce:
  - Safe restart patterns
  - Controlled updates
  - Guardrails around self‑modifying behavior

**Effect:**  
The system remains stable even under heavy or experimental usage.

---

### 3.6 Knowledge Graph Protection Layer

**Purpose:**  
Protect the **KG core** from unsafe operations.

**Responsibilities:**

- Guard:
  - Core ontology entities
  - System relations
  - Security‑critical nodes (e.g., identity, roles, policies)
- Restrict:
  - Bulk deletions
  - Structural changes to ontology
  - Cross‑domain relations that break consistency
- Require:
  - Justification for sensitive changes
  - Logging and explainability for KG mutations

**Effect:**  
The KG remains **consistent, safe, and explainable** over time.

---

### 3.7 Explainability & Logging Layer

**Purpose:**  
Make every critical decision **traceable and understandable**.

**Responsibilities:**

- Log:
  - Who requested what
  - Which layer blocked or allowed it
  - Why the decision was made
- Provide:
  - Human‑readable explanations (for debugging and audits)
  - Machine‑readable logs (for future analysis)
- Integrate with:
  - SIRIUS explain commands (KG_EXPLAIN, KG_EXPLAIN_DEEP)
  - System diagnostics

**Effect:**  
Security is not a black box—every decision can be inspected.

---

## 4. How COLNIK will work end‑to‑end (when finished)

### 4.1 Request lifecycle

1. **Incoming request**  
   - From user, agent, or external system.
   - Contains: command, parameters, context.

2. **Identity check**  
   - Who is calling?  
   - Attach identity metadata.

3. **Role & permission check**  
   - What is this identity allowed to do?  
   - If not allowed → **deny + log + explain**.

4. **Policy evaluation (ENVOY)**  
   - Apply global and local policies.  
   - If policy forbids → **deny + log + explain**.

5. **Input validation & sanitization**  
   - Check syntax, structure, size.  
   - If invalid → **reject or sanitize**.

6. **Runtime & KG safety checks**  
   - Is this operation safe for the runtime and KG?  
   - If risky → **require justification, escalate, or block**.

7. **Routing to subsystem**  
   - KG operations → KG module  
   - Parser operations → Parser module  
   - Workflow operations → WorkflowEngine  
   - Reasoning operations → ReasoningEngine

8. **Execution**  
   - Subsystem performs the requested operation.

9. **Logging & explanation**  
   - COLNIK records:
     - identity
     - operation
     - decision path
     - outcome
   - Optionally returns an explanation to the caller.

---

### 4.2 Example: KG_RELATE request

**User request:**  
`KG_RELATE(entityA, entityB, relation="depends_on")`

**COLNIK flow:**

- Identity: user = `developer`
- Role & permissions: `developer` can modify KG, but not core ontology.
- Policy: relation `depends_on` is allowed for non‑core entities.
- Validation: entities exist, relation is valid.
- KG safety: no core nodes involved, no forbidden pattern.
- Routing: forward to KG module.
- Execution: KG creates relation.
- Logging: record who, what, when, and why it was allowed.

---

## 5. Purpose of COLNIK in the SIRIUS architecture

COLNIK is the **security spine** of SIRIUS:

- It ensures that **every critical action** is:
  - authenticated
  - authorized
  - validated
  - policy‑checked
  - safe for runtime and KG
  - logged and explainable

- It allows SIRIUS to:
  - grow in complexity without losing control
  - host autonomous agents safely
  - expose APIs without compromising integrity
  - debug and audit decisions after the fact

In short:

> **COLNIK makes SIRIUS safe, controlled, and trustworthy—without killing flexibility.**

---

## 6. Current status vs. future state

### Current (foundation in place)

- Conceptual layers defined (identity, roles, policies, validation, KG safety, logging).
- Basic security checks integrated into:
  - KG commands
  - runtime operations
- Policy files (e.g., `policies_envoy.json`) planned/partially used.
- Logging and explainability integrated at KG level.

### Future (full implementation)

- All requests pass through COLNIK by default.
- Full role‑based access control across all modules.
- Configurable policies for:
  - KG
  - runtime
  - agents
  - external integrations
- Strong input validation and sanitization.
- Complete KG protection for core ontology.
- Unified logging and explainability for all security decisions.
- Ready for:
  - autonomous agents
  - external APIs
  - multi‑user environments

---

## 7. How to use this document in GitHub

This tutorial is meant to be:

- A **high‑level architectural overview** of COLNIK.
- A **security design document** for contributors.
- A **reference** for implementing and extending:
  - identity checks
  - role & permission logic
  - policy evaluation
  - validation and sanitization
  - KG protection
  - logging and explainability

You can place it in:

- `docs/security/colnik_overview.md`  
- or `docs/architecture/colnik_security_layers.md`

So that anyone joining the project understands:

- **what COLNIK is**,  
- **why it exists**,  
- **what layers it has**,  
- **and how it will behave when fully implemented.**

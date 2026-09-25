# SIRIUS Kýklos Gate (COLNIK-6.x) – Primitive Decision Gate & IPC Tutorial

## 1. Overview

The **SIRIUS Kýklos Gate (COLNIK-6.x)** is the final, primitive customs decision gate in the SIRIUS runtime.  
Its purpose is straightforward and invariant: **it decides whether a command, graph mutation, or workflow step is ALLOWED or DENIED**, operating across both **Standard Mode** and the integrated, high-performance **IPC Mode** on port 8080 for real-time synchronization with AUTONOMY-6.x and the 4-Panel UI Suite.

COLNIK does not perform reasoning, NLP tokenization, Knowledge Graph traversal, or autonomy planning.  
It is a single, deterministic checkpoint situated directly above the autonomy and execution layers, orchestrated through `sirius_orchestrator.py` and actively supervised by `TimeCore` and `Guard`.

COLNIK relies on existing security, policy, and domain-shielding modules to make its verdict.  
It does not replace them — it aggregates their outputs alongside interactive `PanelAPI` human confirmation gates (`[ÁNO/NIE]`).

---

## 2. Why COLNIK Is Primitive

SIRIUS already contains multiple specialized security and semantic validation modules:

- **PermissionLayer5**  
- **PolicyEngine5**  
- **BehaviorFilter5**  
- **FamilySafetyRules5_x**  
- **ContextualBehaviorEngine5**  
- **EnvoyNormalizer5** (Contextual Domain & Non-Bio Shield)  
- **DisambiguationTriager5** (Anti-Prefix & Strip-Bracket Guard)  

These modules:

- enforce identity profiles (OWNER / FAMILY / STRANGER)  
- evaluate declarative policies in `policies_envoy.json`  
- detect suspicious behavioral patterns  
- safeguard family and academic bypass rules  
- prevent cross-domain contamination (e.g., blocking biological habitat tags on technical concepts)  
- prevent erroneous prefix drift (*Káva* -> *Kavala*)  

COLNIK does **not** duplicate their specialized analysis.  
Instead, COLNIK inspects their verdicts to answer a single question:

> **Should this command or mutation be cleared to reach autonomy, graph storage, and execution?**

This maintains an uncompromised, audit-ready customs architecture.

---

## 3. Execution Pipeline

This is the exact pipeline for Runtime 5.9.0:

User Command / Web UI  
↓  
InputParser5 (Compound phrase preservation & copula verb separation)  
↓  
`sirius_orchestrator.py` (Single-Process Orchestrator on Port 8080)  
↓  
WorkflowEngine5.9.0  
↓  
KÝKLOS GATE (COLNIK-6.x Standard & High-Performance IPC Mode)  
↓  
PanelAPI (`[ÁNO/NIE]` Confirmation Loop — skipped if entity alias already indexed)  
↓  
┌───────────────────────────┐  
│           ALLOW           │  
│             or            │  
│  DENY / TRIAGE QUARANTINE │  
└───────────────────────────┘  
↓  
AUTONOMY 6.x (Control, Guard & Triage Mode in `COLNIK-6.x/triage`)  
↓  
EXECUTE 6.x → Multi-Alias KG Persistence (`autosave_kg.json`) / OS Task  
↓  
UI State Release (`currentModule = "none"`)  

COLNIK is the **internal customs authority** inspecting every operation before disk mutation or autonomous execution occurs.

---

## 4. Security Modules Protecting COLNIK

COLNIK is primitive, but its decisions are fortified by **seven core security and semantic modules**:

### 4.1 PermissionLayer5
Verifies whether the identity (caller, session, or internal agent) holds the required authority level.  
Outputs: **ALLOW / DENY / REQUIRE-CONFIRMATION**

### 4.2 PolicyEngine5
Evaluates system-wide rules from `policies_envoy.json`.  
Outputs: **ALLOWED-BY-POLICY / BLOCKED-BY-POLICY**

### 4.3 BehaviorFilter5
Detects rapid mutation anomalies, cyclic requests, and erratic input loops.  
Outputs: **SAFE / RISKY / BLOCK**

### 4.4 FamilySafetyRules5_x
Enforces protections for children and household safety (guaranteeing academic schoolwork remains unrestricted).  
Outputs: **SAFE / UNSAFE**

### 4.5 ContextualBehaviorEngine5
Evaluates environment telemetry, system load, and execution timing under `TimeCore` and `Guard` supervision.  
Outputs: **CONTEXT-OK / CONTEXT-NOT-OK**

### 4.6 EnvoyNormalizer5 (Non-Bio Domain Shield)
Guarantees that abstract, architectural, or technological entities do not carry false biological attributes.  
Outputs: **DOMAIN-VALID / DOMAIN-CORRUPT**

### 4.7 DisambiguationTriager5 (Anti-Prefix Guard)
Verifies that encyclopedic retrieval targets match the queried semantic lemma without fuzzy prefix drift.  
Outputs: **TARGET-VALID / TARGET-DRIFT**

---

## 5. How COLNIK Uses These Modules

COLNIK does not execute heavy analytical logic.  
It inspects module evaluations using a deterministic decision matrix:

IF PermissionLayer5 == ALLOW  
AND PolicyEngine5 == ALLOWED-BY-POLICY  
AND BehaviorFilter5 == SAFE  
AND FamilySafetyRules5_x == SAFE  
AND ContextualBehaviorEngine5 == CONTEXT-OK  
AND EnvoyNormalizer5 == DOMAIN-VALID  
AND DisambiguationTriager5 == TARGET-VALID  
THEN  
    ALLOW (proceed to execution or PanelAPI [ÁNO/NIE] confirmation)  
ELSE IF AnomalyDetected == TRUE  
    ROUTE TO TRIAGE (Quarantine in COLNIK-6.x/triage)  
ELSE  
    DENY  

This ensures complete operational predictability without unverified execution bypasses.

---

## 6. What COLNIK Actually Does

COLNIK executes six fundamental customs checks:

### 6.1 Identity Verification
Is the command originating from an authorized identity, and does STRANGER lockdown apply?

### 6.2 Permission Audit
Does the calling layer hold authorization for this action category?

### 6.3 Policy Conformance
Does any local policy forbid this execution or outbound fetch?

### 6.4 Graph Integrity & Domain Boundary Check
Does the proposed mutation respect semantic domain boundaries and schema rules?

### 6.5 Interactive Confirmation Gate
Does the operation require explicit user authorization via `PanelAPI` (`[ÁNO/NIE]`), or does the entity already exist under an alias in `autosave_kg.json`?

### 6.6 Final Decision Dispatch
- **ALLOW** → Cleared to IPC buffers (`proposals.json`) and executed by `EXECUTE 6.x`.  
- **ROUTE TO TRIAGE** → Quarantined in `COLNIK-6.x/triage` for inspection via the Triage UI Panel.  
- **DENY** → Blocked, logged with XAI attribution, and halted.  

---

## 7. COLNIK vs. Security Modules

| Component | Operational Responsibility |
|:---|:---|
| PermissionLayer5 | Manages identity permissions and access tiers |
| PolicyEngine5 | Evaluates global policy declarations |
| BehaviorFilter5 | Detects execution anomalies and loop behavior |
| FamilySafetyRules5_x | Enforces household, child safety, and schoolwork bypass |
| ContextualBehaviorEngine5 | Monitors system telemetry under TimeCore & Guard |
| EnvoyNormalizer5 | Shields non-biological domains from false habitat metadata |
| DisambiguationTriager5 | Blocks prefix drifts and resolves valid encyclopedic branches |
| COLNIK-6.x | Final ALLOW / DENY / TRIAGE customs verdict (Standard & IPC Mode) |

COLNIK is not an analytical security engine — it is the **authoritative customs decision gate**.

---

## 8. Integration with the 4-Panel UI Suite (Port 8080)

Under Runtime 5.9.0, COLNIK integrates directly into the unified single-process dashboard on port 8080:

- **Triage Panel:** Live visual queue of all quarantined files, ambiguous payloads, and held mutations (`COLNIK-6.x/triage`).  
- **Duplicates Panel:** Displays duplicate file status, enforcing `REPORT_ONLY` policies to avoid unauthorized disk deletions.  
- **Terminal Panel:** Enforces clean input state release (`currentModule = "none"`), ensuring that rejected or cleared commands do not capture host terminal focus.  

---

## 9. Summary

- COLNIK-6.x is a **primitive decision gate**, executing fast, deterministic ALLOW / DENY / TRIAGE checks.  
- It operates natively in both Standard Mode and high-performance **IPC Mode** on port 8080.  
- It sits **directly above autonomy and execution**, governed by `sirius_orchestrator.py`.  
- It leverages the full security stack (PermissionLayer, PolicyEngine, EnvoyNormalizer, Guard).  
- It enforces interactive `PanelAPI` `[ÁNO/NIE]` confirmation loops without proposal recurrence on indexed aliases.  
- It quarantines anomalies into `COLNIK-6.x/triage` for transparent auditability.  

This is the definitive customs architecture of the Kýklos Gate for Runtime 5.9.0.

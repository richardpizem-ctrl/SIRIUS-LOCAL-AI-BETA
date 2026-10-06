# SIRIUS Kýklos Gate (COLNIK-6.x) – Primitive Decision Gate, Security Protocol & IPC Tutorial

## 1. Overview

The **SIRIUS Kýklos Gate (COLNIK-6.x)** is the final, primitive customs decision gate and security firewall in the SIRIUS runtime.  
Its purpose is straightforward and invariant: **it decides whether a command, graph mutation, shell instruction, or workflow step is ALLOWED or DENIED**, operating across both **Standard Mode** and the integrated, high-performance **IPC Mode** on port 8080 for real-time synchronization with AUTONOMY-6.x and the 4-Panel UI Suite.

In Runtime **v5.9.1**, COLNIK integrates the comprehensive **COLNÍK Guard** engine alongside the **Human-in-the-Loop Safe Trash** pipeline, entry-level **Token Guard** sanitization, and sliding-window quarantine maintenance.

COLNIK does not perform reasoning, NLP tokenization, Knowledge Graph traversal, or autonomy planning.  
It is a single, deterministic checkpoint situated directly above the autonomy and execution layers, orchestrated through `sirius_orchestrator.py` with embedded `TerminalAssistant` and `TimeCore` telemetry (`cycle_delta()`), and actively supervised by `Guard`.

COLNIK relies on existing security, policy, and domain-shielding modules to make its verdict.  
It does not replace them — it aggregates their outputs alongside interactive `PanelAPI` human confirmation gates (`[ÁNO/NIE]` / `[YES/NO]`) with confirmation state latching.

---

## 2. Why COLNIK Is Primitive

SIRIUS contains multiple specialized security, token-filtering, and semantic validation modules:

- **TokenGuard5** (Entry-level character sequence sanitization)
- **COLNÍK Guard / TerminalAssistant** (0.0s hard block command firewall)
- **HitL Safe Trash Engine** (Quarantined file removal governor)
- **QuarantineRotator5** (100-file sliding window ceiling)
- **PermissionLayer5**
- **PolicyEngine5**
- **BehaviorFilter5**
- **FamilySafetyRules5_x**
- **ContextualBehaviorEngine5**
- **EnvoyNormalizer5** (Contextual Domain & Non-Bio Shield)
- **DisambiguationTriager5** (Anti-Prefix & Strip-Bracket Guard)

These modules:

- reject inputs with forbidden symbols (`@#$%^&*`) immediately at runtime threshold
- intercept destructive shell routines (`format`, `diskpart`, `rmdir /s`) in 0.0s
- prevent unverified disk deletions by isolating files into quarantine awaiting explicit `GET /trash` review
- enforce identity profiles (OWNER / FAMILY / STRANGER)
- evaluate declarative policies in `policies_envoy.json`
- detect suspicious behavioral patterns
- safeguard family and academic bypass rules
- isolate Slovak (`autosave_kg.json`) and English (`autosave_kg_en.json`) knowledge graphs
- prevent cross-domain contamination (e.g., blocking biological habitat tags on technical concepts)
- prevent erroneous prefix drift (*Káva* -> *Kavala*)

COLNIK does **not** duplicate their specialized analysis.  
Instead, COLNIK inspects their verdicts to answer a single question:

> **Should this command, shell invocation, or mutation be cleared to reach autonomy, graph storage, and execution?**

This maintains an uncompromised, audit-ready customs architecture.

---

## 3. Execution Pipeline

This is the exact pipeline for Runtime 5.9.1:

User Command / Web UI / Shell Terminal  
↓  
Token Guard (Rejects inputs with `@#$%^&*` at entry)  
↓  
InputParser5 (Trailing punctuation stripping `.rstrip("?")` & compound phrase preservation)  
↓  
Language Context Router (Binds to `autosave_kg.json` [SK] or `autosave_kg_en.json` [EN])  
↓  
`sirius_orchestrator.py` (Single-Process Daemon on Port 8080 with TerminalAssistant & TimeCore)  
↓  
WorkflowEngine5.9.1  
↓  
KÝKLOS GATE (COLNIK-6.x Standard & High-Performance IPC Mode)  
├─ [Shell Check: FORBIDDEN (`format`, `diskpart`)] ──> 0.0s Hard Block & Log  
├─ [File Removal Check: Deletion requested] ─────────> Route to HitL Quarantine Trash  
↓  
PanelAPI (`[ÁNO/NIE]` / `[YES/NO]` Confirmation Loop with active State Latching)  
↓  
┌───────────────────────────┐  
│           ALLOW           │  
│             or            │  
│  DENY / TRIAGE QUARANTINE │  
└───────────────────────────┘  
↓  
AUTONOMY 6.x (Control, Guard, Triage Mode & HitL Trash in `COLNIK-6.x/triage`)  
↓  
EXECUTE 6.x → Lossless Merge / Dual KG Commit / Quarantine Prune (100-file ceiling)  
↓  
UI State Release (`currentModule = "none"`)  

COLNIK is the **internal customs authority** inspecting every operation before disk mutation, command execution, or autonomous action occurs.

---

## 4. Security Modules Protecting COLNIK

COLNIK is primitive, but its decisions are fortified by **core security, token, and semantic modules**:

### 4.1 Token Guard
Sanitizes raw strings before runtime ingest, dropping any payload with dangerous symbolic injections (`@`, `#`, `$`, `%`, `^`, `&`, `*`).  
Outputs: **INPUT-CLEAN / TOKEN-BLOCKED**

### 4.2 COLNÍK Guard (TerminalAssistant)
Enforces the shell command categorization matrix with 0.0s hard blocking:
- **FORBIDDEN (0.0s Block):** `format`, `rmdir /s`, `del /f /s /q c:`, `diskpart`, `drop database`, fork-bombs
- **RISKY (Explicit Prompt):** `rm`, `kill`, `taskkill`, `del`
- **ALLOWED:** `ps`, `top`, `mem`, `sys`, `grep`, `info`, `cat`, `head`, `tail`, `check`, `template`, `python`, `git`, `pip`, `ls`, `dir`, `cd`, `pwd`, `mkdir`, `touch`, `help`  
Outputs: **COMMAND-ALLOW / COMMAND-PROMPT / COMMAND-HARD-BLOCK**

### 4.3 Human-in-the-Loop (HitL) Safe Trash
Governs all file deletion proposals: moves files to quarantine storage and forbids direct unverified disk deletion, mandating manual review via `GET /trash`.  
Outputs: **QUARANTINED-FOR-REVIEW / DIRECT-DELETE-BLOCKED**

### 4.4 QuarantineRotator5 (EnvoyQuarantine5)
Monitors `COLNIK-6.x/envoy/quarantine/` and automatically purges the oldest JSON payloads to enforce a strict 100-record ceiling.  
Outputs: **WINDOW-WITHIN-LIMITS / ROTATION-TRIGGERED**

### 4.5 PermissionLayer5
Verifies whether the identity (caller, session, or internal agent) holds the required authority level.  
Outputs: **ALLOW / DENY / REQUIRE-CONFIRMATION**

### 4.6 PolicyEngine5
Evaluates system-wide rules from `policies_envoy.json`.  
Outputs: **ALLOWED-BY-POLICY / BLOCKED-BY-POLICY**

### 4.7 BehaviorFilter5
Detects rapid mutation anomalies, cyclic requests, and erratic input loops.  
Outputs: **SAFE / RISKY / BLOCK**

### 4.8 FamilySafetyRules5_x
Enforces protections for children and household safety (guaranteeing academic schoolwork remains unrestricted).  
Outputs: **SAFE / UNSAFE**

### 4.9 ContextualBehaviorEngine5
Evaluates environment telemetry, system load, and execution timing under `TimeCore` (`cycle_delta()`) and `Guard` supervision.  
Outputs: **CONTEXT-OK / CONTEXT-NOT-OK**

### 4.10 EnvoyNormalizer5 (Non-Bio Domain Shield)
Guarantees that abstract, architectural, or technological entities do not carry false biological attributes.  
Outputs: **DOMAIN-VALID / DOMAIN-CORRUPT**

### 4.11 DisambiguationTriager5 (Anti-Prefix Guard)
Verifies that encyclopedic retrieval targets match the queried semantic lemma without fuzzy prefix drift.  
Outputs: **TARGET-VALID / TARGET-DRIFT**

---

## 5. How COLNIK Uses These Modules

COLNIK does not execute heavy analytical logic.  
It inspects module evaluations using a deterministic decision matrix:

IF TokenGuard == TOKEN-BLOCKED  
    DENY (reject with TOKEN_GUARD_BLOCK)  
ELSE IF ColnikGuard == COMMAND-HARD-BLOCK  
    DENY (0.0s hard block, log security incident)  
ELSE IF HitLTrash == QUARANTINED-FOR-REVIEW  
    ROUTE TO SAFE TRASH (awaiting explicit user approval via GET /trash)  
ELSE IF PermissionLayer5 == ALLOW  
AND PolicyEngine5 == ALLOWED-BY-POLICY  
AND BehaviorFilter5 == SAFE  
AND FamilySafetyRules5_x == SAFE  
AND ContextualBehaviorEngine5 == CONTEXT-OK  
AND EnvoyNormalizer5 == DOMAIN-VALID  
AND DisambiguationTriager5 == TARGET-VALID  
THEN  
    ALLOW (proceed to execution or PanelAPI confirmation)  
ELSE IF AnomalyDetected == TRUE  
    ROUTE TO TRIAGE (Quarantine in COLNIK-6.x/triage)  
ELSE  
    DENY  

This ensures complete operational predictability without unverified execution bypasses.

---

## 6. What COLNIK Actually Does

COLNIK executes seven fundamental customs checks:

### 6.1 Token & Input Sanitization Check
Does the input contain malicious symbols (`@#$%^&*`), or does it need greedy trailing question mark stripping (`.rstrip("?")`)?

### 6.2 Host Command Security Inspection
Does a shell invocation match any entry in the FORBIDDEN list (`format`, `diskpart`, `rmdir /s`), requiring immediate 0.0s termination?

### 6.3 Identity & Permission Verification
Is the command originating from an authorized identity, and does STRANGER lockdown apply?

### 6.4 Safe Trash Pipeline Governance
Is a proposed action deleting a file? If so, divert to quarantine and mandate explicit user review via `GET /trash`.

### 6.5 Language Partition & Domain Boundary Check
Does the mutation target the correct language graph (`autosave_kg.json` for SK, `autosave_kg_en.json` for EN), and does it respect non-biological domain separation?

### 6.6 Confirmation State Latching Check
Does the operation require explicit user authorization via `PanelAPI` (`[ÁNO/NIE]` / `[YES/NO]`), and is the active confirmation latch properly associated with the pending entity?

### 6.7 Final Decision Dispatch
- **ALLOW** → Cleared to IPC buffers (`proposals.json`) and executed by `EXECUTE 6.x`.  
- **ROUTE TO SAFE TRASH / TRIAGE** → Quarantined in `COLNIK-6.x/triage` or Safe Trash awaiting manual approval.  
- **DENY** → Blocked, logged with XAI attribution, and halted.  

---

## 7. COLNIK vs. Security Modules

| Component | Operational Responsibility |
|:---|:---|
| TokenGuard5 | Rejects malformed injection characters (`@#$%^&*`) at entry |
| COLNÍK Guard | Intercepts forbidden shell commands (`format`, `diskpart`) in 0.0s |
| Safe UI Trash | Diverts file removals to quarantine for manual approval (`GET /trash`) |
| QuarantineRotator5 | Automatically rotates quarantine files at the 100-record ceiling |
| PermissionLayer5 | Manages identity permissions and access tiers |
| PolicyEngine5 | Evaluates global policy declarations |
| BehaviorFilter5 | Detects execution anomalies and loop behavior |
| FamilySafetyRules5_x | Enforces household, child safety, and schoolwork bypass |
| ContextualBehaviorEngine5 | Monitors system telemetry under TimeCore (`cycle_delta()`) & Guard |
| EnvoyNormalizer5 | Shields non-biological domains from false habitat metadata |
| DisambiguationTriager5 | Blocks prefix drifts and resolves valid encyclopedic branches |
| COLNIK-6.x | Final ALLOW / DENY / TRIAGE customs verdict (Standard & IPC Mode) |

COLNIK is not an analytical security engine — it is the **authoritative customs decision gate**.

---

## 8. Integration with the 4-Panel UI Suite (Port 8080)

Under Runtime 5.9.1, COLNIK integrates directly into the unified single-process dashboard on port 8080:

- **Triage Panel:** Live visual queue of all quarantined files, ambiguous payloads, and held mutations (`COLNIK-6.x/triage`).  
- **Duplicates Panel:** Displays duplicate file status, enforcing `REPORT_ONLY` and routing proposed deletions into the HitL Safe Trash pipeline.  
- **Terminal Panel:** Enforces clean input state release (`currentModule = "none"`), ensuring that rejected or cleared commands do not capture host terminal focus, while running commands through COLNÍK Guard security.  

---

## 9. Summary

- COLNIK-6.x is a **primitive decision gate**, executing fast, deterministic ALLOW / DENY / TRIAGE checks.  
- It operates natively in both Standard Mode and high-performance **IPC Mode** on port 8080.  
- It incorporates **COLNÍK Guard** for 0.0s hard blocks on destructive commands and **Token Guard** for entry-level input hygiene.  
- It governs the **Human-in-the-Loop Safe Trash** architecture, preventing unverified file destruction.  
- It enforces a strict **100-file ceiling** via automated sliding-window quarantine rotation.  
- It sits **directly above autonomy and execution**, governed by `sirius_orchestrator.py`.  
- It enforces interactive `PanelAPI` `[ÁNO/NIE]` / `[YES/NO]` confirmation loops with confirmation state latching and zero proposal recurrence on indexed aliases.  

This is the definitive customs architecture of the Kýklos Gate for Runtime 5.9.1.

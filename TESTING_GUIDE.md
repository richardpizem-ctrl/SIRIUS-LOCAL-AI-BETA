# 🧪 TESTING GUIDE – SIRIUS LOCAL AI  
### v4.0.0 → 4.3.0 → **4.4.0 PRO (Expanded)**

This document defines the testing strategy, procedures, and safety validation rules for the SIRIUS LOCAL AI project.  
All tests are fully local and must be executed manually by the user.

The system interacts with Windows 11 APIs, filesystem operations, window management, application control, identity‑based safety, schoolwork‑aware routing, UI automation, semantic UI reasoning, and — starting in **4.4.0 PRO** — **deterministic OS‑level automation validated by System Agent 4.2**.

All behavior must remain deterministic, safe, and reversible.

---

# 1. Testing Philosophy

(unchanged, plus new 4.4.0 rules)

- all tests must be reproducible  
- no automated tests that modify the system without confirmation  
- every test must validate safety, predictability, and reversibility  
- tests must not rely on network access  
- tests must not require external dependencies  
- plugin tests must follow Plugin System 3.0 rules  
- WIN‑CAP tests must validate permission boundaries  
- workflows must behave deterministically  
- identity‑restricted actions must be enforced  
- **SECURITY FAMILY tests must validate identity, time‑limits, and schoolwork bypass logic**  
- **Schoolwork Priority Mode must always override restrictions**  
- **UI Automation Engine tests must validate sandbox rules, deterministic behavior, and safe OS‑level routing**  
- **semantic UI tests must validate fuzzy matching, fallback logic, and confidence thresholds**  
- **System Agent 4.2 tests must validate OS‑level safety, reversibility, and identity gating** ← *NEW (4.4.0)*  
- **OS‑level automation must never bypass WinCapabilities 4.4** ← *NEW (4.4.0)*  

---

# 2. Test Categories

## A) Filesystem Tests (FS‑AGENT 3.0)
(unchanged)

---

## B) Natural Language Router Tests (NL Router 3.0)
(unchanged)

---

## C) Workflow Engine Tests (Workflow Engine 3.0)
(unchanged)

---

## D) GUI Tests (GUI Layer 3.0)
(unchanged)

---

## E) WIN‑CAP Tests (WIN‑CAP 3.0)
(unchanged)

---

## F) Plugin System Tests (Plugin System 3.0)
(unchanged)

---

## G) AI Loop Tests (AI Loop 3.0)
(unchanged)

---

## H) SECURITY FAMILY Tests (v4.0.0)
(unchanged)

---

## I) Household Modules Tests (v3.0.0)
(unchanged)

---

# J) UI Automation Engine Tests (v4.2.0)

(unchanged)

---

# K) Semantic UI Automation Tests (v4.3.0)

(unchanged)

---

# L) UI Workflow Tests (v4.3.0)

(unchanged)

---

# M) **System Agent 4.2 Tests (v4.4.0 PRO) — NEW**

System Agent 4.2 is the **final OS‑level safety gatekeeper**.  
These tests ensure that all system actions are:

- identity‑validated  
- reversible  
- deterministic  
- safe  
- routed through WinCapabilities 4.4  

### Validate:
- identity gating (OWNER / FAMILY / STRANGER)  
- OS‑level permission boundaries  
- reversibility checks  
- deterministic allow/deny logic  
- safe routing of system actions  
- rejection of unsafe operations  
- correct mediation between UI Automation and OS  

### Checklist:
- OWNER actions must succeed only when safe  
- FAMILY actions must be restricted  
- STRANGER actions must be blocked  
- unsafe OS actions must be rejected  
- every system action must appear in System Agent logs  
- no direct OS calls may bypass System Agent  
- reversibility must be confirmed before execution  
- fallback logic must activate when OS denies an action  

---

# N) **OS‑Level Automation Tests (WinCapabilities 4.4) — NEW**

These tests validate the new OS‑aware automation layer introduced in 4.4.0 PRO.

### Validate:
- safe Win32/UIA/WinRT routing  
- deterministic OS‑level behavior  
- identity‑aware OS actions  
- capability boundaries  
- safe fallback logic  
- no privileged operations  
- no kernel‑level access  

### Checklist:
- all OS actions must route through WinCapabilities  
- no direct API calls from UIActions  
- OWNER‑only OS actions must be enforced  
- FAMILY/STRANGER must be blocked from system‑critical actions  
- fallback must activate when OS denies access  
- logs must include capability routing info  

---

# O) **Workflow Engine 4.4 Tests — NEW**

Workflow Engine 4.4 introduces identity‑aware, OS‑validated workflows.

### Validate:
- deterministic state transitions  
- identity‑aware workflow gating  
- safe fallback logic  
- System Agent validation for system workflows  
- semantic caching  
- no unsafe multi‑step sequences  

### Checklist:
- workflows must not execute OS actions directly  
- every OS‑level step must pass through System Agent  
- fallback must be deterministic  
- SCHOOLWORK workflows must bypass restrictions safely  
- STRANGER workflows must be restricted  
- OWNER workflows must remain reversible  

---

# P) **AITE 4.4 Tests — NEW**

AITE 4.4 improves semantic triage and identity‑aware routing.

### Validate:
- faster OCR  
- improved semantic detection  
- identity‑aware triage  
- SCHOOLWORK bypass logic 2.0  
- deterministic classification  

### Checklist:
- triage must remain constant‑time  
- SCHOOLWORK detection must override restrictions  
- identity must influence routing  
- no ambiguous classifications  
- deterministic results across runs  

---

# Q) **Reasoning Engine 4.4 Tests — NEW**

### Validate:
- bounded reasoning depth  
- deterministic chain‑of‑thought  
- symbolic logic 2.0  
- pack‑aware reasoning 2.0  

### Checklist:
- no unbounded reasoning  
- no recursive loops  
- deterministic results  
- SCHOOLWORK reasoning must remain instant  

---

# 3. Test Execution Rules

(unchanged)

---

# 4. Logging Format

(unchanged)

---

# 5. Document Status

**Version:** **4.4.0 PRO (Expanded)**  
This guide now includes testing rules for:

- UI Automation Engine 4.2.0  
- Semantic UI Automation 4.3.0  
- **System Agent 4.2**  
- **WinCapabilities 4.4**  
- **Workflow Engine 4.4**  
- **AITE 4.4**  
- **Reasoning Engine 4.4**  

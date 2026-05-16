# 🧪 TESTING GUIDE – SIRIUS LOCAL AI (v4.0.0 → 4.3.0 EXPANDED)

This document defines the testing strategy, procedures, and safety validation rules for the SIRIUS LOCAL AI project.  
All tests are fully local and must be executed manually by the user.

The system interacts with Windows 11 APIs, filesystem operations, window management, application control, identity‑based safety, schoolwork‑aware routing, and — starting in **4.2.0 / 4.3.0** — **UI automation and semantic UI reasoning**.

All behavior must remain deterministic, safe, and reversible.

---

# 1. Testing Philosophy

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
- **UI Automation Engine tests must validate sandbox rules, deterministic behavior, and safe OS‑level routing** ← *NEW*  
- **semantic UI tests must validate fuzzy matching, fallback logic, and confidence thresholds** ← *NEW*  

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

# J) UI Automation Engine Tests (v4.2.0) — *NEW*

Validate:
- UI graph scanning  
- element extraction  
- exact / case‑insensitive / partial matching  
- deterministic UI actions  
- sandbox permission enforcement  
- workflow step execution (scan → parse → find → act)  
- audit logging  
- identity‑restricted UI actions  

Checklist:
- UI graph must detect all visible elements  
- parser must normalize text consistently  
- exact matches must resolve deterministically  
- partial matches must not override exact matches  
- sandbox must block restricted actions in FAMILY/STRANGER modes  
- OWNER‑only actions must be enforced  
- workflow must not skip steps  
- audit logs must record all actions  
- no UI action may run without explicit confirmation  

---

# K) Semantic UI Automation Tests (v4.3.0) — *NEW*

Validate:
- fuzzy matching engine  
- confidence scoring  
- semantic alias mapping  
- retry logic  
- fallback strategies  
- OS‑aware action routing  
- WinCapabilities integration  
- deterministic behavior under uncertainty  

Checklist:
- fuzzy matching must produce stable confidence scores  
- low‑confidence matches must be rejected  
- alias mapping must resolve synonyms correctly  
- retry logic must be bounded (no infinite loops)  
- fallback logic must follow deterministic order  
- UI actions must route through WinCapabilities only  
- sandbox must block unsafe OS‑level actions  
- semantic actions must not override identity rules  
- audit logs must include confidence + fallback info  

---

# L) UI Workflow Tests (v4.3.0) — *NEW*

Validate:
- multi‑stage resolution pipeline  
- confidence‑based routing  
- fallback transitions  
- semantic target resolution  
- integration with UIParser and UIActions  

Checklist:
- workflow must retry only when confidence is below threshold  
- fallback must activate only when primary resolution fails  
- semantic resolution must not mis‑target elements  
- workflow must remain deterministic across runs  
- identity restrictions must apply at every stage  
- OWNER‑only UI actions must be blocked in FAMILY/STRANGER modes  

---

# 3. Test Execution Rules

(unchanged)

---

# 4. Logging Format

(unchanged)

---

# 5. Document Status

Current version: **4.0.0 (Expanded with 4.2.0–4.3.0 UI Automation Tests)**  
This guide evolves with new modules and capabilities.

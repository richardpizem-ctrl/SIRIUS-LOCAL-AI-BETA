# 🧪 TESTING GUIDE — SIRIUS LOCAL AI (v5.5.0 UNIFIED)

This document defines the **complete testing framework** for the Unified Reasoning & Explainability Runtime 5.5 architecture.  
It replaces all previous 4.x, 5.0, and 5.3 testing rules with a **deterministic, explainable,  
system‑intelligent, identity‑aware, KG‑aware, repair‑aware** testing model.

All tests must pass on:

- Windows 11 (PC)
- Mobile Runtime 5.5 (Android subsystem / mobile shell)
- LAN Sync 2.0 environments
- Offline mode (default)
- Optional Envoy 5 mode (permission‑based + explainability)

---

# ⭐ 1. Testing Philosophy (Updated for 5.5)

### Core principles:
- **determinism over speed**
- **identity‑aware behavior**
- **predictive OS‑state awareness**
- **KG‑aware semantic validation**
- **KG_EXPLAIN explainability validation**
- **repair‑aware execution**
- **no unsafe OS actions**
- **no workflows in degraded OS states**
- **no bypassing System Agent 5**
- **no bypassing System Intelligence Layer 5.5**
- **no bypassing KG‑Reasoning**
- **no unbounded reasoning**
- **no nondeterministic UI automation**

All tests must confirm that SIRIUS behaves **identically** across PC + Mobile.

---

# ⭐ 2. Test Categories (v5.5)

1. **System Intelligence Layer 5.5 Tests**  
2. **System Agent 5 Tests**  
3. **UI Automation Engine 5.5 Tests**  
4. **Workflow Engine 5.5 Tests**  
5. **AITE 5.5 Tests**  
6. **Reasoning Engine 5.5 Tests**  
7. **Knowledge Packs 5.5 Tests**  
8. **Filesystem Agent 5.0 Tests**  
9. **Security Family 5.x Tests**  
10. **Envoy 5 Tests**  
11. **Self‑Repair Layer 5.x Tests**  
12. **Unified PC/Mobile Runtime Tests**  
13. **KG_EXPLAIN Explainability Tests** ← NEW  

---

# ⭐ Q1) **General Determinism Tests — REQUIRED FOR ALL MODULES**

### Validate:
- deterministic outputs across runs  
- no nondeterministic branching  
- no randomization  
- no time‑dependent logic  
- no OS‑dependent divergence  
- no mobile‑only or PC‑only behavior  
- identical explainability traces  

### Checklist:
- same input → same output  
- same workflow → same transitions  
- same UI target → same resolution  
- same KG query → same inference path  
- same OS state → same safety decision  
- same explainability trace → same justification  

---

# ⭐ Q2) **System Intelligence Layer 5.5 Tests — UPDATED**

System Intelligence Layer 5.5 introduces predictive OS‑state awareness,  
risk detection, degraded‑mode detection, explainability traces, and KG‑aware context evaluation.

### Validate:
- OS health detection (PC + Mobile)
- KG‑aware risk prediction
- degraded‑mode detection
- unsafe state prevention
- workflow blocking in unsafe or degraded conditions
- deterministic system‑state evaluation
- integration with System Agent 5
- identity‑aware system context routing
- Envoy 5 permission influence on system state
- KG_EXPLAIN explainability traces

### Checklist:
- unsafe OS states must block workflows  
- degraded mode must block OS‑level actions  
- OWNER workflows require SAFE OS conditions  
- FAMILY/STRANGER workflows restricted under WARNING  
- fallback 3.2 must activate when risk is high  
- logs must include SAFE / WARNING / RISK / DEGRADED  
- KG‑Reasoning must validate system‑context consistency  
- KG_EXPLAIN must justify system‑state decisions  
- Self‑Repair Layer must trigger on integrity issues  

---

# ⭐ Q3) **System Agent 5 Tests — UPDATED**

System Agent 5 is the hardened OS‑level safety gatekeeper.

### Validate:
- identity gating 3.2  
- reversibility 3.2  
- OS‑level permission boundaries  
- predictive safety integration  
- deterministic allow/deny logic 3.2  
- safe routing of system actions  
- rejection of unsafe or high‑risk operations  
- degraded‑mode blocking  
- Envoy 5 permission enforcement  
- KG_EXPLAIN explainability traces  

### Checklist:
- OWNER actions allowed only in SAFE state  
- FAMILY restricted under WARNING  
- STRANGER blocked always  
- unsafe OS actions must be rejected  
- degraded‑mode blocks all OS actions  
- all actions logged  
- no direct OS calls bypass System Agent  
- fallback 3.2 activates on denial  
- Envoy fetch blocked without ASK permission  
- explainability trace must justify every decision  

---

# ⭐ Q4) **UI Automation Engine 5.5 Tests — UPDATED**

### Validate:
- fuzzy matching 5.5  
- deterministic fallback 3.2  
- identity‑aware UI actions 3.2  
- safe Win32/UIA/WinRT routing  
- mis‑click prevention 3.2  
- semantic target resolution 3.2  
- KG‑enhanced UI matching  
- degraded‑mode blocking  
- KG_EXPLAIN explainability traces  

### Checklist:
- all UI actions route through System Agent 5  
- fallback 3.2 activates deterministically  
- OWNER‑only UI actions enforced  
- FAMILY/STRANGER restricted  
- degraded‑mode blocks UI actions  
- logs include UI routing info  
- no direct API calls from UIActions  
- KG‑Reasoning validates ambiguous UI targets  
- explainability trace must justify UI selection  

---

# ⭐ Q5) **Workflow Engine 5.5 Tests — UPDATED**

### Validate:
- deterministic state transitions  
- identity‑aware workflow gating 3.2  
- system‑state‑aware workflow routing  
- degraded‑mode workflow blocking  
- KG‑aware workflow planning  
- explainability routing (KG_EXPLAIN)  
- safe fallback logic 3.2  
- System Agent 5 validation  
- semantic caching 3.2  

### Checklist:
- workflows never execute OS actions directly  
- all OS steps pass through System Agent 5  
- workflows blocked in unsafe or degraded states  
- SCHOOLWORK workflows bypass restrictions safely  
- STRANGER workflows restricted  
- OWNER workflows reversible  
- KG‑Reasoning validates workflow context  
- KG_EXPLAIN must justify workflow transitions  
- Self‑Repair Layer validates workflow integrity  

---

# ⭐ Q6) **AITE 5.5 Tests — UPDATED**

### Validate:
- faster OCR 5.5  
- improved semantic detection  
- identity‑aware triage 4.2  
- SCHOOLWORK bypass 5.x  
- deterministic classification 3.2  
- system‑context‑aware routing  
- KG‑aware semantic tagging  
- degraded‑mode routing restrictions  
- explain‑intent detection  
- KG_EXPLAIN traces  

### Checklist:
- triage must remain constant‑time  
- SCHOOLWORK detection overrides restrictions  
- identity influences routing  
- system state influences routing  
- degraded mode restricts routing  
- KG‑Reasoning influences routing  
- explainability trace must justify routing  
- deterministic results across runs  

---

# ⭐ Q7) **Reasoning Engine 5.5 Tests — UPDATED**

### Validate:
- multi‑hop inference  
- inheritance reasoning  
- transitive reasoning  
- deterministic rule chaining  
- bounded reasoning depth 3.2  
- pack‑aware reasoning 4.2  
- KG‑integrated inference  
- cached reasoning paths  
- Envoy‑aware reasoning  
- repair‑aware reasoning  
- KG_EXPLAIN proof‑tree generation  

### Checklist:
- no unbounded reasoning  
- no recursive loops  
- deterministic results  
- SCHOOLWORK reasoning instant  
- reasoning adapts to OS state  
- KG consistency validated  
- degraded‑mode inconsistencies detected  
- explainability trace must match inference path  

---

# ⭐ Q8) **Knowledge Packs 5.5 Tests — UPDATED**

### Validate:
- faster lookups  
- improved semantic linking  
- deterministic pack‑to‑pack reasoning  
- pack integrity validation 2.2  
- expanded school, household, device packs  
- KG‑ready structure  
- repair‑aware pack validation  
- KG_EXPLAIN metadata  

### Checklist:
- no ambiguous pack resolution  
- deterministic pack selection  
- identity‑aware pack access  
- SCHOOLWORK packs override restrictions  
- KG‑Reasoning validates pack consistency  
- degraded‑mode blocks unsafe pack usage  
- explainability trace must justify pack selection  

---

# ⭐ Q9) **Filesystem Agent 5.0 Tests**

### Validate:
- safe path validation  
- rollback‑safe operations  
- identity‑aware file access  
- SCHOOLWORK file prioritization  
- deterministic routing  
- System Agent 5 validation  

### Checklist:
- no raw filesystem calls  
- no destructive operations without reversibility  
- no access outside identity scope  
- no operations in degraded mode  

---

# ⭐ Q10) **Security Family 5.x Tests**

### Validate:
- identity classification 3.2  
- constant‑time identity checks  
- SCHOOLWORK bypass logic  
- STRANGER‑mode restrictions  
- FAMILY‑mode safe boundaries  
- KG_EXPLAIN identity traces  

### Checklist:
- identity must influence all routing  
- no OS action without identity validation  
- no bypass of Security Family logic  
- explainability trace must justify identity decision  

---

# ⭐ Q11) **Envoy 5 Tests**

### Validate:
- ASK → FETCH → QUARANTINE → VALIDATE → DELIVER  
- identity‑aware permissions  
- System Agent 5 enforcement  
- safe payload validation  
- no local data transmission  
- KG_EXPLAIN explainability traces  

### Checklist:
- no automatic fetch  
- no bypass of ASK permission  
- quarantine must isolate payloads  
- System Agent must approve delivery  
- explainability trace must justify permission  

---

# ⭐ Q12) **Self‑Repair Layer 5.x Tests**

### Validate:
- corrupted module detection  
- degraded‑mode isolation  
- repair suggestion generation  
- repair‑aware workflow continuation  
- KG‑integrity repair  
- explainability trace generation  

### Checklist:
- degraded mode must block unsafe actions  
- repair must restore SAFE state  
- logs must include repair context  
- explainability trace must justify repair decision  

---

# ⭐ Q13) **Unified PC/Mobile Runtime Tests**

### Validate:
- identical behavior across PC + Mobile  
- identical identity logic  
- identical workflow transitions  
- identical KG reasoning  
- identical UI automation semantics (where supported)  
- identical explainability traces  

### Checklist:
- no platform‑specific divergence  
- no mobile‑only logic  
- no PC‑only logic  
- LAN Sync 2.0 must not affect determinism  

---

# ⭐ Q14) **KG_EXPLAIN Explainability Tests — NEW**

### Validate:
- proof‑tree generation  
- confidence scoring  
- rule‑chain consistency  
- workflow explainability  
- OS‑action explainability  
- identity‑decision explainability  
- UI‑automation explainability  
- Envoy‑permission explainability  

### Checklist:
- every decision must produce an explainability trace  
- traces must be deterministic  
- traces must match reasoning path  
- traces must match workflow transitions  
- traces must match System Agent decisions  
- traces must match identity gating  
- traces must match OS‑state evaluation  

---

# 📄 Document Status (Updated)

**Version:** **5.5.0 UNIFIED (Complete Rewrite)**  
This guide now includes testing rules for:

- System Intelligence Layer 5.5  
- System Agent 5  
- UI Automation Engine 5.5  
- Workflow Engine 5.5  
- AITE 5.5  
- Reasoning Engine 5.5  
- Knowledge Packs 5.5  
- Filesystem Agent 5.0  
- Security Family 5.x  
- Envoy 5  
- Self‑Repair Layer 5.x  
- Unified PC/Mobile Runtime  
- KG_EXPLAIN Explainability Engine

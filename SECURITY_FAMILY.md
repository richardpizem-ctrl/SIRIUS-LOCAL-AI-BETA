# 🔐 SECURITY FAMILY 5.x — Identity Engine 3.1 & Unified Permission Framework  
**Status:** ✔ Active (Enhanced)  
**Version:** 5.x (Updated for 5.9.0 UNIFIED)  
**Component:** Security Family  
**Role:** Identity enforcement, permission gating, terminal decoupling, safety modes, orchestrator-supervised, autonomy‑aware and COLNIK‑validated security logic

---

## 🎯 Purpose  
Security Family 5.x is the unified identity and permission enforcement layer of SIRIUS Local AI (v5.9.0).  
It ensures that every natural language query, workflow transition, compound noun phrase evaluation (`InputParser5`), Knowledge Graph mutation, reasoning derivation, and host system operation is validated through identity profiles, deep symbolic explainability, single-process orchestration (`sirius_orchestrator.py` on Port 8080), interactive `PanelAPI` confirmation loops, `TimeCore`/`Guard` supervision, COLNIK‑6.x (Standard & High-Performance IPC Mode), and AUTONOMY‑6.x (Control, Guard & Triage Mode).

Security Family protects the local workstation from unauthorized access, erratic execution loops, cross-domain contamination, terminal shell hijacking, and identity-restricted operations.

---

## 🧩 Architecture Overview  
**Identity Engine 3.1 → Security Family 5.x → InputParser5 → sirius_orchestrator.py (Port 8080) → System Agent 5 → AUTONOMY 6.x → COLNIK-6.x → PanelAPI [ÁNO/NIE] → Multi-Alias KG Persistence (`autosave_kg.json`)**

### Core Responsibilities  
- enforce identity access tiers (OWNER / FAMILY / STRANGER) in constant time ($O(1)$)  
- validate query tokens and preserve compound noun phrases (`ovcia vlna`, `mobilny telefon`)  
- enforce terminal input decoupling (`currentModule = "none"`) upon query clearance  
- block unauthorized actions and privileged system modifications  
- supply derivation metadata for `KG_EXPLAIN` and `KG_EXPLAIN_DEEP` proof trees  
- supervise autonomous learning proposals with zero proposal recurrence for confirmed aliases  
- validate Knowledge Graph mutations and enforce domain boundaries (Non-Bio Domain Shield)  
- coordinate real-time hardware telemetry and threat containment with Guard  
- route suspicious payloads safely into `COLNIK-6.x/triage`  

### Key Files  
- `security_family/security_family.py`  
- `security_family/identity_engine_3_1.py`  
- `security_family/identity_modes.json`  
- `security_family/permissions.json`  
- `security_family/family_safety_rules5_x.py`  
- `ORCHESTRATOR/sirius_orchestrator.py`  
- `PANEL_API/panel_api.py`  
- `IPC_DATA/security_events.json`  

---

## 🔍 Identity Modes & Access Profiles  

### **OWNER Mode**  
Full administrative and root access tier:  
- unrestricted execution of safe workflows, local system tasks, and developer comfort commands  
- authorized to perform atomic Knowledge Graph modifications, deletions, and exports  
- sensitive or destructive actions gate through interactive `PanelAPI` confirmation (`[ÁNO/NIE]`)  

### **FAMILY Mode**  
Trusted household access tier:  
- full access to conversational reasoning, academic tasks, household guides, and safe file browsing  
- read-only access to Password Vault shared credentials  
- blocked from administrative OS mutations, raw shell executions, and destructive graph deletions  

### **STRANGER Mode**  
Zero-trust restricted sandbox:  
- immediately isolates user session upon unrecognized behavioral markers or access requests  
- completely blocks Knowledge Graph mutations, file modifications, and OS-level execution  
- forces terminal detachment and locks module state (`currentModule = "none"`)  

### **SCHOOLWORK Mode (Guaranteed Academic Bypass)**  
Deterministic educational bypass governed by Schoolwork Engine 5.8:  
- academic inquiries, homework assistance, and educational lookups bypass household time limits and restrictions with zero latency  
- fully permitted for Knowledge Graph navigation, multi-hop reasoning, and educational ENVOY retrieval  
- strictly blocks OS automation and administrative system mutations  

---

## 🔍 Permission & Gating Pipeline (v5.9.0)  

### **1 — Identity Verification & Semantic Sanitization**  
Before query processing begins:  
- evaluates caller profile in constant time ($O(1)$)  
- audits active identity tier against requested resource scopes  
- invokes `InputParser5` to isolate copula verbs (`je`, `sú`) and preserve compound noun phrases without token truncation  
- applies STRANGER lockdown if caller identity fails verification  

---

### **2 — Symbolic Explainability & Proof-Tree Enforcement**  
Every identity-relevant decision compiles an auditable provenance trace:  
- `KG_EXPLAIN` direct relation justification  
- `KG_EXPLAIN_DEEP` hierarchical multi-hop proof trees (ASCII + HTML)  
- applied security rules (`IdentityAccessRule`, `FamilySafetyRules5_x`)  
- confidence metrics and permission rationale  

Explainability is mandatory for all access decisions.

---

### **3 — Terminal State Decoupling Guard**  
To prevent conversational queries or failed commands from capturing host console input:  
- clearing an input field or canceling a prompt immediately triggers `currentModule = "none"`  
- completely isolates the web-based Terminal Panel on port 8080 from executing raw host shell binaries  
- prevents command injection and UI state lockups  

---

### **4 — COLNIK‑6.x Customs Clearance (Standard & IPC Mode)**  
All operations pass through the Kýklos customs gate:  
- enterprise-grade structural and cycle-safety checks  
- validation against Non-Bio Domain Shield (no habitat metadata on technical concepts)  
- verification of Anti-Prefix and Anti-Drift guards  
- threat classification and payload inspection across high-performance IPC  
- unverified, malformed, or suspicious mutations are routed to `COLNIK-6.x/triage`  

---

### **5 — AUTONOMY 6.x Governance & Zero Recurrence**  
Supervised learning and state transitions:  
- unindexed concepts trigger structured proposals (`kg.learn_proposal`)  
- dispatches human confirmation requests via `PanelAPI` (`[ÁNO/NIE]`)  
- **Zero Proposal Recurrence:** once approved, the entity is committed under both user query and encyclopedic aliases in `autosave_kg.json`; subsequent lookups resolve instantly from memory without duplicate confirmation loops  

---

### **6 — KG Mutation & Multi-Alias Protection**  
Security Family audits all Knowledge Graph write requests:  
- prevents unauthorized node or relation deletion  
- verifies that compound phrases retain contextual integrity  
- validates dual-key alias linkages  
- enforces atomic serialization to `autosave_kg.json`  

---

## 🧱 Protection Layers  

### **Identity & Behavioral Layer**  
- OWNER / FAMILY / STRANGER / SCHOOLWORK modes  
- constant-time classification without background biometric monitoring  
- outbound ENVOY permission enforcement  

### **Semantic & Domain Integrity Layer**  
- compound phrase preservation via `InputParser5`  
- Non-Bio Domain Shield and Sentence-Bound habitat filtering via `EnvoyNormalizer5`  
- Anti-Prefix Guard blocking semantic drift (*Káva* -> *Kavala*)  

### **Execution & Terminal Decoupling Layer**  
- single-process orchestration via `sirius_orchestrator.py` on Port 8080  
- automatic state reset (`currentModule = "none"`) on input clear  
- System Agent 5 OS-action validation and reversibility checks  

### **Knowledge & Persistence Layer**  
- atomic commit to `autosave_kg.json`  
- multi-alias resolution suppressing proposal recurrence  
- multi-hop proof-tree generation in `KG_EXPLAIN_DEEP`  

---

## 🔐 Safety Rules  
- ❌ No execution of unverified host OS commands  
- 🔒 Mandatory customs clearance via COLNIK‑6.x (Standard & High-Performance IPC Mode)  
- 🛡 Supervised decision gating via AUTONOMY 6.x (Control, Guard & Triage Mode)  
- 💬 Interactive human-in-the-loop validation via `PanelAPI` `[ÁNO/NIE]` for unindexed concepts  
- 🛑 Terminal state decoupling must trigger `currentModule = "none"` upon input reset  
- 🚫 Strict non-biological domain shields active across all external data ingestion  
- 🔁 Zero proposal recurrence on established entities and aliases  
- ⚠ Deterministic proof-tree explainability required for all decisions  
- 📉 Real-time hardware telemetry (CPU, RAM, Disk) monitored via Guard  

---

## 📊 Module Status (v5.9.0)  
- ✔ Fully implemented & synchronized with Runtime 5.9.0  
- ✔ Identity access tiers verified (OWNER / FAMILY / STRANGER)  
- ✔ Compound noun phrase parsing and copula separation active  
- ✔ Terminal decoupling and module state reset confirmed  
- ✔ Single-process orchestrator integration on port 8080 operational  
- ✔ PanelAPI interactive confirmation loops verified  
- ✔ TimeCore temporal tracking and Guard resource telemetry active  
- ✔ Multi-alias graph persistence operational (`autosave_kg.json`)  
- ✔ COLNIK‑6.x customs validation functional (Standard & IPC Mode)  
- ✔ AUTONOMY 6.x governance and triage containment verified  
- ✔ Complete 4-Panel UI Suite synchronization operational  

---

## 🏁 Summary  
Security Family 5.x is the unified identity and permission enforcement framework of SIRIUS Local AI (v5.9.0).  
It validates every query, workflow, Knowledge Graph mutation, reasoning step, and system operation through identity tiers, deep symbolic explainability, central orchestrator execution, PanelAPI confirmation, COLNIK‑6.x customs validation, and AUTONOMY‑6.x governance.

It ensures that SIRIUS operates on local workstations **safely, deterministically, identity‑aware, linguistically intact, and with verifiable explainability**.

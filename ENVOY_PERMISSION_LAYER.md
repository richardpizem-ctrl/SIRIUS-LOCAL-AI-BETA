# 🌐 ENVOY PERMISSION LAYER 5 — Safe External Retrieval & Identity‑Aware Access Control  
**Status:** ✔ Active (Enhanced)  
**Version:** 5.9.0  
**Component:** ENVOY Permission Layer  
**Role:** Identity‑aware, explainable, orchestrator-supervised, COLNIK-validated permission and domain shielding system for external retrieval tasks

---

## 🎯 Purpose  
The ENVOY Permission Layer 5 is the unified safety, permission, and domain-boundary framework that governs all external retrieval operations performed by ENVOY within Runtime 5.9.0.  
It ensures that every outbound enrichment request is:

- identity‑validated (OWNER / FAMILY / STRANGER)  
- semantic-aware (preserving compound multi-word queries via `InputParser5`)  
- domain-shielded (blocking false habitat/geographic attribute leakage on non-biological entities via `EnvoyNormalizer5`)  
- disambiguation-protected (anti-prefix guards and encyclopedic branch validation via `EnvoyExecutionLayer5`)  
- explainability‑aware (generating proof trees and verifiable attribution)  
- autonomy‑aware with zero proposal recurrence on confirmed concepts  
- orchestrator-supervised via `sirius_orchestrator.py` on local port 8080  
- confirmed through interactive `PanelAPI` [ÁNO/NIE] loops  
- COLNIK‑validated (Standard & High-Performance IPC Mode)  
- strictly compliant with local-first, offline runtime isolation  

ENVOY never directly mutates runtime structures — all communication is filtered, sanitized, and authorized through this permission layer under `TimeCore` and `Guard` supervision.

---

## 🧩 Architecture Overview  
**Security Family / Identity Engine 3.1 → ENVOY Permission Layer 5 → sirius_orchestrator.py (Port 8080) → EnvoyExecutionLayer5 & EnvoyNormalizer5 → Quarantine Sandbox → Policy Validator → COLNIK-6.x → Multi-Alias KG Commit (autosave_kg.json)**

### Core Responsibilities  
- validate external retrieval permissions and outbound requests  
- enforce identity boundaries and access profiles  
- protect multi-word compound queries against invalid token truncation  
- enforce strict non-biological domain shields (preventing tech/abstract concepts from receiving biological attributes)  
- block prefix drifts (*Káva* -> *Kavala*) and resolve disambiguation pages (*„môže byť...“*)  
- eliminate redundant learning loops via multi-alias tracking  
- generate explainability metadata and reasoning proof trees  
- route operations through COLNIK‑6.x (Standard & High-Performance IPC Mode)  
- coordinate autonomous decisions with AUTONOMY 6.x and Triage Mode (`COLNIK-6.x/triage`)  
- guarantee complete isolation of the offline runtime  

### Key Files  
- `envoy/envoy_permission_layer.py`  
- `envoy/envoy_execution_layer_5.py`  
- `envoy/envoy_normalizer_5.py`  
- `envoy/envoy_rules.json`  
- `envoy/envoy_log.json`  
- `IPC_DATA/envoy_events.json`  

---

## 🔍 Permission Pipeline (v5.9.0)  

### **1 — Identity & Context Validation**  
Before ENVOY initiates any external retrieval process, the permission layer audits:  
- FAMILY mode restrictions  
- STRANGER mode lockdown  
- SCHOOLWORK bypass rules (unrestricted academic access)  
- active caller authorization and module state (`currentModule = "none"` check)  
- prohibited or identity-restricted topics  

If identity or context validation fails, the request is immediately neutralized.

---

### **2 — Semantic Integrity & Domain Guarding**  
In Runtime 5.9.0, retrieval requests must pass semantic sanitation:  
- **Compound Phrase Verification:** Ensures noun phrases (`ovcia vlna`, `mobilny telefon`) remain intact and are not mutilated into isolated words.  
- **Disambiguation Routing:** Confirms that parenthetical expressions or encyclopedia indexes resolve to valid root lemmas (Strip-Bracket Fallback).  
- **Non-Bio Domain Shield:** Strictly bars abstract, engineering, and scientific topics (*fyzika*, *ekológia*, *architektúra*) from acquiring biological habitat properties.  

---

### **3 — Explainability & Provenance Enforcement**  
Every outbound fetch generates full audit metadata:  
- `KG_EXPLAIN` & `KG_EXPLAIN_DEEP` derivation trees  
- identity verification records  
- permission justification logs  
- autonomous decision scores  

Explainability generation is mandatory prior to payload dispatch.

---

### **4 — COLNIK‑Validated Customs Inspection**  
All outbound queries and returned payloads undergo COLNIK‑6.x inspection:  
- enterprise-grade safety policy enforcement  
- deterministic allow/deny evaluation  
- reversible mutation verification  
- threat classification and payload scanning  
- audit logging across Standard and High-Performance IPC modes  

Unverified or malformed payloads are routed to `COLNIK-6.x/triage` or rejected.

---

### **5 — AUTONOMY Governance & Interactive Confirmation**  
AUTONOMY 6.x coordinates retrieval permissions through supervised loops:  
- new concept retrieval requires user authorization (`kg.learn_proposal`)  
- prompts are dispatched via `PanelAPI` using `[ÁNO/NIE]` confirmation  
- **Zero Proposal Recurrence:** Once approved, the permission layer maps the entity across aliases in `autosave_kg.json`, preventing repeated confirmation prompts for the same concept.  

---

### **6 — Quarantine Sandbox & Data Cleansing**  
All externally acquired text passes through an isolated quarantine sandbox:  
- complete removal of HTML, embedded scripts, trackers, and metadata tags  
- blocking of binary payloads, executables, and unverified data types  
- extraction restricted to declarative, sentence-bound facts  
- text normalization into deterministic knowledge formats  

No raw external data ever interacts directly with the local Knowledge Graph.

---

### **7 — Policy Validator & Final Delivery**  
Following quarantine, the policy engine verifies:  
- compliance with local safety rules  
- exclusion of restricted domains  
- absence of malicious or unsupported instructions  
- structural schema consistency  

Only verified, normalized facts are committed to the Knowledge Graph via `RuntimeCore`.

---

## 🧱 Permission Categories  

### **Allowed (Safe)**  
- educational and academic definitions  
- multi-word compound concepts (`ovcia vlna`, `pevna linka`)  
- basic technical descriptions and terminology  
- household and material data  
- schoolwork materials (Schoolwork Engine 5.8)  
- validated factual domain knowledge  

### **Restricted (Identity‑Aware / Confirmation Required)**  
- system-level configuration topics  
- administrative operations  
- interactive learning proposals for novel entities (`[ÁNO/NIE]` required)  
- privileged system settings  

### **Blocked (Always)**  
- executable files, binaries, scripts, and active HTML  
- unverified external commands  
- unsafe instructions or malicious content  
- cross-domain attribute leaks (e.g., habitat data on technological concepts)  
- prefix-drifted queries violating semantic boundaries  

---

## 🔐 Safety Rules  
- ❌ No external retrieval without explicit identity validation  
- 🔒 Mandatory inspection by COLNIK‑6.x (Standard & IPC Mode)  
- 🛡 Supervised approval required via AUTONOMY 6.x  
- 💬 Interactive human-in-the-loop gating via `PanelAPI` [ÁNO/NIE] for unindexed entities  
- 🛑 Anti-prefix guards must prevent query drift (*Káva* -> *Kavala*)  
- 🚫 Strict non-biological domain shields active at all times  
- 🔁 Zero proposal recurrence on confirmed knowledge  
- 🧠 Mandatory quarantine and script stripping  
- 📉 Deterministic audit logging and explainability tracking  

---

## 📊 Module Status (v5.9.0)  
- ✔ Fully implemented & synchronized with Runtime 5.9.0  
- ✔ Semantic multi-word handling verified  
- ✔ Disambiguation triage integration active  
- ✔ Non-bio domain shield operational  
- ✔ Quarantine sandbox fully functional  
- ✔ Policy validator hardened against payload injection  
- ✔ COLNIK‑6.x IPC validation operational  
- ✔ AUTONOMY 6.x proposal & zero-recurrence logic confirmed  
- ✔ Orchestrator and PanelAPI integration functional on port 8080  
- ✔ TimeCore & Guard runtime telemetry active  

---

## 🏁 Summary  
ENVOY Permission Layer 5 serves as the defensive boundary and permission backbone for all external retrieval operations in SIRIUS Local AI (v5.9.0).  
It ensures that ENVOY retrieves only safe, identity-validated, explainable, autonomy-approved, and COLNIK-verified facts under orchestrator supervision and PanelAPI confirmation loops — maintaining compound semantic integrity, protecting domain boundaries, and preserving strict offline-first runtime isolation.

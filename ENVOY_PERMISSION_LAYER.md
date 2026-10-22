# 🌐 ENVOY PERMISSION LAYER 5 — Safe External Retrieval & Identity‑Aware Access Control  
**Status:** ✔ Active (Enhanced)  
**Version:** 5.9.5  
**Component:** ENVOY Permission Layer  
**Role:** Identity‑aware, explainable, orchestrator-supervised, COLNIK-validated permission, language context routing, domain shielding, SafeRollback resilience, and Professor Validator cognitive verification system for external retrieval tasks.

---

## 🎯 Purpose  
The ENVOY Permission Layer 5 is the unified safety, permission, and domain-boundary framework that governs all external retrieval operations performed by ENVOY within Runtime 5.9.5.  
It ensures that every outbound enrichment request is:

- bound to the active linguistic context (`autosave_kg.json` for SK, `autosave_kg_en.json` for EN)  
- identity‑validated (OWNER / FAMILY / STRANGER)  
- semantic-aware (preserving compound multi-word queries via `InputParser5` and stripping trailing punctuation via `.rstrip("?")`)  
- domain-shielded (blocking false habitat/geographic attribute leakage on non-biological entities via `EnvoyNormalizer5`)  
- disambiguation-protected (anti-prefix guards and encyclopedic branch validation via `EnvoyExecutionLayer5`)  
- state-latched across interactive turns to guarantee user confirmations (`[ÁNO/NIE]` / `[YES/NO]`) execute without detached states  
- managed within a 100-file sliding-window quarantine ceiling (`EnvoyQuarantine5`)  
- protected via SafeRollback crash resilience (`safe_rollback.py`)  
- cognitively verified via Professor Validator middleware (`professor_validator.py`)  
- explainability‑aware (generating proof trees and verifiable attribution)  
- autonomy‑aware with zero proposal recurrence on confirmed concepts and inferred taxonomies  
- orchestrator-supervised via `sirius_orchestrator.py` on local port 8080 with embedded TerminalAssistant + TimeCore  
- COLNIK‑validated (Standard & High-Performance IPC Mode) with Token Guard input sanitization  
- strictly compliant with local-first, offline runtime isolation  

ENVOY never directly mutates runtime structures — all communication is filtered, sanitized, quarantined, and authorized through this permission layer under `TimeCore`, `Guard`, `SafeRollback`, `Professor Validator`, and `COLNÍK` supervision.

---

## 🧩 Architecture Overview  
**Security Family / Identity Engine 3.1 → Token Guard → ENVOY Permission Layer 5 → sirius_orchestrator.py (Port 8080) → EnvoyExecutionLayer5 & EnvoyNormalizer5 → Quarantine Sandbox (100-File Sliding Window) → Policy Validator → COLNIK-6.x → Language Partition Graph Commit (`autosave_kg.json` / `autosave_kg_en.json`)**

### Core Responsibilities  
- validate external retrieval permissions and outbound requests  
- bind retrieval target and Wikipedia endpoints strictly to active caller language headers (`SK` / `EN`)  
- enforce entry-level token sanitization via Token Guard, blocking injection characters (`@#$%^&*`)  
- enforce trailing punctuation stripping to guarantee clean entity key resolution  
- maintain confirmation state latching for pending enrichment proposals  
- enforce strict non-biological domain shields (preventing tech/abstract concepts from receiving biological attributes)  
- block prefix drifts (*Káva* -> *Kavala*) and resolve disambiguation pages (*„môže byť...“*)  
- enforce the 100-record sliding-window ceiling inside `COLNIK-6.x/envoy/quarantine/`  
- supervise module-level state backups and restorations via `safe_rollback.py`  
- enforce strict cognitive verification (`PASS / WARN / REJECT`) via `professor_validator.py`  
- eliminate redundant learning loops via multi-alias tracking and taxonomical edge auto-commits  
- generate explainability metadata and reasoning proof trees  
- route operations through COLNIK‑6.x (Standard & High-Performance IPC Mode)  
- coordinate autonomous decisions with AUTONOMY 6.x and Triage Mode (`COLNIK-6.x/triage`)  
- guarantee complete isolation of the offline runtime  

### Key Files  
- `envoy/envoy_permission_layer.py`  
- `envoy/envoy_execution_layer_5.py`  
- `envoy/envoy_normalizer_5.py`  
- `envoy/envoy_quarantine_5.py`  
- `envoy/envoy_rules.json`  
- `envoy/envoy_log.json`  
- `core/safe_rollback.py`  
- `professor/professor_validator.py`  
- `IPC_DATA/envoy_events.json`  
- `autosave_kg.json`  
- `autosave_kg_en.json`  

---

## 🔍 Permission Pipeline (v5.9.5)  

### **1 — Identity, Token Guard & Context Validation**  
Before ENVOY initiates any external retrieval process, the permission layer audits:  
- Token Guard input filter: reject inputs containing forbidden characters (`@`, `#`, `$`, `%`, `^`, `&`, `*`)  
- Punctuation hygiene: strip trailing question marks (`.rstrip("?")`) to preserve pure entity identifiers  
- Target language context: determine destination graph (`autosave_kg.json` vs. `autosave_kg_en.json`)  
- FAMILY mode restrictions and STRANGER mode lockdown  
- SCHOOLWORK bypass rules (unrestricted academic access)  
- active caller authorization and module state (`currentModule = "none"` check)  
- prohibited or identity-restricted topics  

If identity, token, or context validation fails, the request is immediately neutralized.

---

### **2 — Semantic Integrity & Domain Guarding**  
In Runtime 5.9.5, retrieval requests must pass semantic sanitation:  
- **Compound Phrase Verification:** Ensures noun phrases (*ovcia vlna*, *mobilny telefon*) remain intact and are not truncated into isolated words.  
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

### **5 — AUTONOMY Governance, Confirmation Latching & Recurrence Elimination**  
AUTONOMY 6.x coordinates retrieval permissions through supervised loops:  
- new concept retrieval requires user authorization (`kg.learn_proposal`)  
- confirmation states latch target entities in memory across conversation turns  
- prompts are dispatched via `PanelAPI` using `[ÁNO/NIE]` / `[YES/NO]` confirmation  
- **Zero Proposal Recurrence:** Once approved, the permission layer maps the entity across aliases and commits deduced taxonomies into the target language graph (`autosave_kg.json` or `autosave_kg_en.json`), preventing repeated confirmation prompts for the same concept.  

---

### **6 — Quarantine Sandbox, Sliding-Window Rotation & Data Cleansing**  
All externally acquired text passes through an isolated quarantine sandbox:  
- storage in `COLNIK-6.x/envoy/quarantine/` governed by an automatic sliding-window rotation limiting total records to 100 JSON files  
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

Only verified, normalized facts are committed to the designated language Knowledge Graph via `RuntimeCore` (`autosave_kg.json` for SK, `autosave_kg_en.json` for EN).

---

## 🧱 Permission Categories  

### **Allowed (Safe)**  
- educational and academic definitions  
- multi-word compound concepts (*ovcia vlna*, *pevna linka*)  
- basic technical descriptions and terminology  
- household and material data  
- schoolwork materials (Schoolwork Engine 5.8)  
- validated factual domain knowledge  

### **Restricted (Identity‑Aware / Confirmation Required)**  
- system-level configuration topics  
- administrative operations  
- interactive learning proposals for novel entities (`[ÁNO/NIE]` / `[YES/NO]` required)  
- privileged system settings  

### **Blocked (Always)**  
- inputs containing forbidden character sets (`@#$%^&*`)  
- executable files, binaries, scripts, and active HTML  
- unverified external commands  
- unsafe instructions or malicious content  
- cross-domain attribute leaks (e.g., habitat data on technological concepts)  
- prefix-drifted queries violating semantic boundaries  

---

## 🔐 Safety Rules  
- ❌ No external retrieval without explicit identity validation  
- ⛔ Immediate Token Guard rejection on malformed symbolic inputs (`@#$%^&*`)  
- 🗄️ Strict language context binding: SK queries retrieve SK articles; EN queries retrieve EN articles  
- 🔄 SafeRollback crash resilience protecting configuration and state integrity  
- ⚖️ Professor Validator strict verification (`PASS / WARN / REJECT`) on cognitive outputs  
- 🔒 Mandatory inspection by COLNIK‑6.x (Standard & IPC Mode)  
- 🛡 Supervised approval required via AUTONOMY 6.x  
- 💬 Interactive human-in-the-loop gating via `PanelAPI` [ÁNO/NIE] / [YES/NO] with confirmation state latching  
- 🛑 Anti-prefix guards must prevent query drift (*Káva* -> *Kavala*)  
- 🚫 Strict non-biological domain shields active at all times  
- 🔁 Zero proposal recurrence on confirmed knowledge and deduced taxonomies  
- 📦 Automatic quarantine sliding-window rotation enforcing a 100-file ceiling  
- 🧠 Mandatory quarantine and script stripping  
- 📉 Deterministic audit logging and explainability tracking  

---

## 📊 Module Status (v5.9.5)  
- ✔ Fully implemented & synchronized with Runtime 5.9.5 architecture  
- ✔ Dual-language target routing (`autosave_kg.json` vs. `autosave_kg_en.json`) active  
- ✔ Token Guard input sanitization active  
- ✔ Trailing punctuation trimming and confirmation latching active  
- ✔ Sliding-window quarantine rotation operational (100-file ceiling)  
- ✔ SafeRollback integration active  
- ✔ Professor Validator matrix operational  
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
ENVOY Permission Layer 5 serves as the defensive boundary and permission backbone for all external retrieval operations in SIRIUS Local AI (v5.9.5).  
It ensures that ENVOY retrieves only safe, identity-validated, explainable, autonomy-approved, and COLNIK-verified facts under orchestrator supervision and PanelAPI confirmation loops — maintaining compound semantic integrity, binding payloads to isolated dual-language graph partitions, rotating quarantine storage via sliding windows, protecting domain boundaries, enforcing SafeRollback state recovery, verifying cognitive outputs via Professor Validator, and preserving strict offline-first runtime isolation.

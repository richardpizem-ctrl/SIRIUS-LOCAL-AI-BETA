# 🗺️ Module Map – SIRIUS LOCAL AI (v5.9.0 UNIFIED)

This document defines all modules of the project, their purpose, responsibilities, and interconnections.  
It serves as an architectural orientation map for the **Semantic Multi-Word Parsing, Autonomous Disambiguation Triage, 4-Panel UI Suite & Multi-Alias KG Persistence Architecture 5.9.0**.

Version **5.9.0 UNIFIED** expands, decouples, and stabilizes the module map with:

- **Single-Process Orchestrator (`sirius_orchestrator.py` on Port 8080)**  
- **Multi-Word Semantic Engine (`InputParser5` preserving compound noun phrases)**  
- **Autonomous Disambiguation Triage & Anti-Prefix Guard (`EnvoyExecutionLayer5`)**  
- **Contextual Domain Shield & Bio Filtering (`EnvoyNormalizer5`)**  
- **Multi-Alias Knowledge Graph Persistence with Dual-Key Mapping (`autosave_kg.json`)**  
- **Zero Proposal Recurrence for confirmed semantic entities**  
- **4-Panel UI Suite (`Duplicates`, `Triage`, `Navigation`, `Terminal` with automatic `currentModule = "none"` state release)**  
- **Native Integrated High-Performance IPC Bridge eliminating file locking bottlenecks**  
- **PanelAPI & Interactive [ÁNO/NIE] Confirmation Loops**  
- **TimeCore Temporal Tracking & Guard Security/Metric Supervision (CPU, RAM, Disk)**  
- **Workflow Engine 5.9.0 (Deterministic, explainability-aware routing)**  
- **Reasoning Engine 5.9.0 (Multi-hop, inheritance, transitivity, orbital rules)**  
- **KG_EXPLAIN & KG_EXPLAIN_DEEP (Hierarchical proof trees & XAI attribution)**  
- **KG Comfort Commands with multi-alias inspection and state decoupling**  
- **COLNIK‑6.x Enterprise Customs Validation Layer (Standard & High-Performance IPC Mode)**  
- **AUTONOMY 6.x Autonomous Decision, Guard Telemetry & Triage Mode (`COLNIK-6.x/triage`)**  
- **System Agent 5 & Identity Engine 3.1 (SECURITY FAMILY 5.x)**  
- **Self‑Repair Layer 5.8**  

All processing is fully local; no data leaves the user's device.

---

# 1. Runtime Core & Orchestrator 5.9.0 (Unified)
**Purpose:** Central single-process execution orchestrator driven by `sirius_orchestrator.py` on local port 8080.  
**Responsibilities:**
- module initialization and lifecycle management via `sirius_orchestrator.py`  
- hosting the integrated HTTP/WebSocket IPC daemon on port 8080  
- interactive `PanelAPI` confirmation loops (`[ÁNO/NIE]`)  
- temporal tracking (`TimeCore`) and resource/security monitoring (`Guard`)  
- compound phrase preservation and copula verb separation via `InputParser5`  
- dual-key multi-alias persistence committed atomically to `autosave_kg.json`  
- suppression of redundant learning loops (Zero Proposal Recurrence)  
- enforcing terminal input decoupling (`currentModule = "none"`) upon clearing commands  
- workflow and deep explainability dispatch (`KG_EXPLAIN_DEEP`)  
- enforcing capability boundaries and deterministic error propagation  
- integration with Security Family 5.x and Self‑Repair Layer 5.8  
- **COLNIK‑6.x validation of workflow and KG mutations (Standard & High-Performance IPC Mode)**  
- **AUTONOMY 6.x proposal evaluation, Guard metric auditing, and Triage Mode routing**

---

# 2. Input Parser & Semantic Extractor (`InputParser5`)
**Purpose:** Precise natural language extraction preserving multi-word compound structures.  
**Responsibilities:**
- extraction and preservation of compound noun phrases (e.g., `ovcia vlna`, `mobilny telefon`, `pevna linka`)  
- strict isolation of Slovak copula verbs (`je`, `sú`) from subject entities, preventing linguistic corruptions  
- diacritic-aware normalization producing clean entities for graph lookup and external triage  
- deterministic tokenization preventing noun-modifier truncation  

---

# 3. Knowledge Graph Engine (KG ENGINE 6.x & Multi-Alias Core)
**Purpose:** Unified symbolic knowledge graph engine powering multi-alias indexing and explainability.  
**Responsibilities:**
- deterministic node and edge management within a cycle-safe schema  
- dual-key entity indexing: mapping user query phrases to formal encyclopedic titles  
- atomic serialization into `autosave_kg.json`  
- inbound/outbound graph traversal and orbital level transitions  
- multi-hop pathfinding and relation discovery (`KG_RELATE`)  
- developer comfort command execution with state release  
- permanent memory resolution suppressing repetitive AUTONOMY proposals  

---

# 4. Autonomous ENVOY & Triage Subsystem (v5.9.0)
**Purpose:** Safe, outbound-only external retrieval and domain-guarded semantic normalization.  
**Responsibilities:**
- **Permission Layer 5:** identity gating (OWNER/FAMILY/STRANGER) and outbound policy audits  
- **Execution Layer 5:** autonomous disambiguation triage (*„môže byť...“*) and Strip-Bracket Fallback  
- **Anti-Prefix Guard:** elimination of fuzzy prefix over-matching (*Káva* -> *Kavala*)  
- **Quarantine Sandbox:** extraction of clean text; complete stripping of HTML, scripts, trackers, and binaries  
- **Normalizer 5:** Non-Bio Domain Shield (strictly blocking biological habitat tags on technical/abstract concepts)  
- **Sentence-Bound Extractor:** requiring explicit occurrence verbs (*žije*, *obýva*) before binding habitat edges  
- delivering normalized, schema-valid facts to COLNIK-6.x customs inspection  

---

# 5. Reasoning Engine 5.9.0 & Deep Explainability (XAI)
**Purpose:** Structured symbolic reasoning and verifiable proof-tree generation.  
**Responsibilities:**
- multi-hop rule deduction and property inheritance (`DedicsnostVlastnostiRule`)  
- transitive relation chaining (`TranzitivneRelacieRule`)  
- orbital category reasoning (`MultiHopOrbitInferenceRule`)  
- automatic type inference (`AutoTypeInferenceRule`)  
- generating human-readable explanations via `KG_EXPLAIN`  
- generating multi-layer hierarchical proof trees (ASCII + HTML) via `KG_EXPLAIN_DEEP`  
- confidence scoring and evidence tree compilation  

---

# 6. Workflow Engine 5.9.0
**Purpose:** Deterministic multi-step process orchestration.  
**Responsibilities:**
- workflow state machine executed within `sirius_orchestrator.py`  
- plugin workflow execution and semantic state transitions  
- SCHOOLWORK workflow prioritization and academic restriction bypass  
- deep explainability routing  
- deterministic error handling and safe fallback routing  
- **COLNIK‑validated workflow steps (Standard & High-Performance IPC Mode)**  
- **AUTONOMY‑aware transitions (Control & Triage Mode)**  

---

# 7. 4-Panel UI Suite (Port 8080)
**Purpose:** Modular local dashboard running via browser on port 8080.  
**Responsibilities:**
- **Duplicates Panel:** live resource auditing and safe duplicate categorization (`REPORT_ONLY`)  
- **Triage Panel:** visual supervision of quarantine queues and unclassified files (`COLNIK-6.x/triage`)  
- **Navigation Panel:** deterministic module switching across Runtime, KG, Envoy, and Autonomy  
- **Terminal Panel:** interactive CLI with automatic state release (`currentModule = "none"`), permanently decoupling user queries from host OS commands  

---

# 8. COLNIK‑6.x Customs Decision Gate
**Purpose:** Authoritative customs inspection gate deciding ALLOW / DENY / TRIAGE.  
**Responsibilities:**
- inspecting all Knowledge Graph mutations and workflow steps  
- high-performance IPC synchronization with AUTONOMY on port 8080  
- verifying entity domain boundaries (Non-Bio Shield validation)  
- enforcing identity and policy conformance  
- routing suspicious or malformed operations into `COLNIK-6.x/triage`  
- enterprise-grade consistency and cycle-safety enforcement  

---

# 9. AUTONOMY 6.x (Decision, Guard & Triage Engine)
**Purpose:** Supervised autonomous decision-making and runtime telemetry.  
**Responsibilities:**
- generating structured learning proposals (`kg.learn_proposal`) for novel concepts  
- evaluating multi-word reasoning outputs  
- enforcing zero proposal recurrence on indexed aliases  
- coordinating interactive confirmation loops via `PanelAPI` (`[ÁNO/NIE]`)  
- Guard supervision: real-time monitoring of CPU, RAM, and Disk metrics  
- managing quarantine containment in `COLNIK-6.x/triage`  

---

# 10. Action Execution Engine (EXECUTE 6.x)
**Purpose:** Deterministic executor for validated proposals.  
**Responsibilities:**
- executing authorized mutations dispatched via `proposals.json`  
- committing dual-key multi-alias entries to `autosave_kg.json` via `RuntimeCore`  
- executing safe file operations under strict non-destructive policies  
- enforcing terminal module resets (`currentModule = "none"`)  
- producing structured execution telemetry in `responses.json`  

---

# 11. Filesystem Agent (FS‑AGENT 5.8)
**Purpose:** Safe, deterministic filesystem operations.  
**Responsibilities:**
- moving, copying, and validating file paths  
- rollback-safe file handling  
- semantic organization (documents, code, schoolwork)  
- COLNIK-validated operations and duplicate detection  

---

# 12. Security Family 5.x (Identity Engine 3.1)
**Purpose:** Behavior-based identity and household safety layer.  
**Responsibilities:**
- OWNER / FAMILY / STRANGER identity tiers  
- behavior-based recognition and access auditing  
- safe-mode restrictions for unknown users  
- time-limits v3 enforcement  
- Schoolwork Engine integration: guaranteeing academic tasks remain unrestricted  
- System Agent 5 validation enforcement  

---

# 13. Self‑Repair & Health‑Check Layer (5.8)
**Purpose:** Runtime integrity scanning and safe recovery.  
**Responsibilities:**
- checking integrity of core runtime modules  
- detecting corrupted schemas, broken configs, or invalid states  
- executing rollback-safe automatic recovery  
- reporting health telemetry to Runtime Core  

---

# 14. System Agent 5
**Purpose:** Final gatekeeper for host system-level operations.  
**Responsibilities:**
- validating all OS-level actions  
- enforcing identity permissions and terminal isolation  
- blocking destructive commands and unverified execution  
- deterministic safety verification  

---

# 15. Context Memory Engine (CME‑MEM 5.8)
**Purpose:** Semantic workflow memory.  
**Responsibilities:**
- tracking recent operational contexts  
- storing semantic tags and subject difficulty metadata  
- supporting multi-step reasoning traces  

---

# 16. Plugin System 5.x
**Purpose:** Extensible local plugin ecosystem.  
**Responsibilities:**
- loading plugin manifests  
- registering NL commands, workflows, and reasoning hooks  
- enforcing safe plugin isolation and COLNIK validation  

---

# 17. Windows System Capabilities Layer (WIN‑CAP 5.x)
**Purpose:** Abstracted, safe access to Windows operating system functions.  
**Responsibilities:**
- providing controlled OS interfaces (`file_ops`, `app_ops`, `system_context`)  
- identity-aware restrictions validated by System Agent 5  

---

# 18. PASSWORD_VAULT 5.0
**Purpose:** Encrypted offline credential storage.  
**Responsibilities:**
- AES-256-GCM vault with PBKDF2 master key derivation  
- OWNER-only write, FAMILY read-only, STRANGER blocked  

---

# 19. Module Interconnections

All modules communicate through:

```text
User / Web UI (Port 8080)
  ↓
InputParser5 (Compound phrase preservation & copula verb separation)
  ↓
sirius_orchestrator.py (Single-Process Orchestrator & Native IPC Daemon)
  ├── 4-Panel UI Suite (Duplicates, Triage, Navigation, Terminal with state reset)
  ├── TimeCore & Guard (Temporal tracking & Resource supervision)
  ├── RuntimeCore 5.9.0 & Multi-Alias KG Core (autosave_kg.json)
  ├── ReasoningEngine 5.9.0 (Multi-hop rules & Proof tree generation)
  ├── WorkflowEngine 5.9.0 (Deterministic state transitions)
  ├── Security Family 5.x & Identity Engine 3.1
  ├── Envoy 5 (ExecutionLayer5, Anti-Prefix Guard & EnvoyNormalizer5)
  ├── COLNIK-6.x Customs Decision Gate (Standard & IPC Mode)
  ├── AUTONOMY 6.x (Control, Guard & Triage Mode in COLNIK-6.x/triage)
  ├── PanelAPI ([ÁNO/NIE] confirmation loop)
  └── EXECUTE 6.x → Multi-Alias Commit / Safe System Action
  Document Status
Version: 5.9.0 UNIFIED

Updated to reflect the 5.8 → 5.9.0 milestone release, single-process orchestration via sirius_orchestrator.py on port 8080, compound noun phrase parsing (InputParser5), autonomous disambiguation triage and domain shielding (Envoy), multi-alias graph persistence (autosave_kg.json), zero proposal recurrence, and complete 4-Panel UI terminal decoupling.

# 🗺️ Module Map – SIRIUS LOCAL AI (v5.9.1 UNIFIED)

This document defines all modules of the project, their purpose, responsibilities, and interconnections.  
It serves as an architectural orientation map for the Dual-Language KG Architecture, Native Lossless Entity Merge, Ontological Habitat Reasoning & COLNÍK Guard Security Protocol 5.9.1.

Version 5.9.1 UNIFIED expands, decouples, and stabilizes the module map with:

- Single-Process Orchestrator (sirius_orchestrator.py on Port 8080 with embedded TerminalAssistant + TimeCore)
- Dual-Language Isolated Knowledge Stores (autosave_kg.json for SK & autosave_kg_en.json for EN)
- Native Lossless KG Merge Engine (kg merge <src> into <tgt> with zero attribute loss)
- Ontological & Taxonomical Category Deduction (KG_VERIFY automatically committing relations like marsupials -> mammals)
- Non-Destructive Reverse Location Engine (_execute_reverse_location_query with anti-flora classification guard)
- Punctuation Hygiene (.rstrip("?")) and Confirmation State Latching across conversation turns
- Entry-Level Token Guard blocking malicious character sequences (@#$%^&*)
- Sliding-Window Quarantine Ceiling Rotation (100 JSON file maximum in COLNIK-6.x/envoy/quarantine/)
- COLNÍK Guard Shell Access Control (0.0s hard blocking of forbidden commands like format and diskpart)
- Human-in-the-Loop Safe UI Trash preventing direct unverified disk destruction
- Multi-Word Semantic Engine (InputParser5 preserving compound noun phrases)
- Autonomous Disambiguation Triage & Anti-Prefix Guard (EnvoyExecutionLayer5)
- Contextual Domain Shield & Bio Filtering (EnvoyNormalizer5)
- Zero Proposal Recurrence for confirmed semantic entities and inferred taxonomies
- 4-Panel UI Suite (Duplicates, Triage, Navigation, Terminal with automatic currentModule = "none" state release)
- Native Integrated High-Performance IPC Bridge eliminating file locking bottlenecks
- PanelAPI & Interactive [ÁNO/NIE] / [YES/NO] Confirmation Loops
- TimeCore Temporal Tracking (cycle_delta()) & Guard Security/Metric Supervision (CPU, RAM, Disk)
- Workflow Engine 5.9.1 (Deterministic, explainability-aware routing)
- Reasoning Engine 5.9.1 (Multi-hop, inheritance, transitivity, orbital & taxonomical rules)
- KG_EXPLAIN & KG_EXPLAIN_DEEP (Hierarchical proof trees & XAI attribution)
- KG Comfort Commands with dual-language partition switching and native merge execution
- COLNIK‑6.x Enterprise Customs Validation Layer (Standard, High-Performance IPC Mode & COLNÍK Guard)
- AUTONOMY 6.x Autonomous Decision, Guard Telemetry, HitL Trash Governance & Triage Mode
- System Agent 5 & Identity Engine 3.1 (SECURITY FAMILY 5.x)
- Self‑Repair Layer 5.8

All processing is fully local; no data leaves the user's device.

---

# 1. Runtime Core & Orchestrator 5.9.1 (Unified)
Purpose: Central single-process execution orchestrator driven by sirius_orchestrator.py on local port 8080 with embedded TerminalAssistant and TimeCore.  
Responsibilities:
- module initialization and lifecycle management via sirius_orchestrator.py
- hosting the integrated HTTP/WebSocket IPC daemon on port 8080
- dynamic language context switching between autosave_kg.json (SK) and autosave_kg_en.json (EN)
- native in-memory execution of kg merge <src> into <tgt> with full property migration and alias linking
- interactive PanelAPI confirmation loops ([ÁNO/NIE] / [YES/NO]) with confirmation state latching
- temporal tracking (TimeCore cycle_delta()) and resource/security monitoring (Guard)
- Token Guard input filtering and greedy trailing punctuation stripping (.rstrip("?"))
- atomic dual serialization to autosave_kg.json and autosave_kg_en.json
- suppression of redundant learning loops (Zero Proposal Recurrence)
- enforcing terminal input decoupling (currentModule = "none") upon clearing commands
- workflow and deep explainability dispatch (KG_EXPLAIN_DEEP)
- enforcing capability boundaries and deterministic error propagation
- integration with Security Family 5.x and Self‑Repair Layer 5.8
- COLNIK‑6.x validation of workflow, shell commands, and KG mutations (Standard, IPC Mode & COLNÍK Guard)
- AUTONOMY 6.x proposal evaluation, Guard metric auditing, HitL Safe Trash, and Triage Mode routing

---

# 2. Input Parser & Token Guard (InputParser5 & TokenGuard5)
Purpose: Entry-level sanitization and natural language extraction preserving multi-word compound structures.  
Responsibilities:
- immediate rejection of dangerous injection symbols (@, #, $, %, ^, &, *) at runtime entry
- greedy trailing punctuation stripping (.rstrip("?")) preventing entity lookup mismatches (e.g., CO JE MACROPUS? -> macropus)
- extraction and preservation of compound noun phrases (e.g., ovcia vlna, mobilny telefon, pevna linka)
- strict isolation of copula verbs (je, sú, is, are) from subject entities, preventing linguistic corruptions
- diacritic-aware normalization producing clean entities for graph lookup and external triage
- deterministic tokenization preventing noun-modifier truncation

---

# 3. Knowledge Graph Engine (KG ENGINE 6.x & Dual-Language Core)
Purpose: Unified symbolic knowledge graph engine powering isolated dual-language partitions, native entity merging, and explainability.  
Responsibilities:
- deterministic node and edge management within a cycle-safe schema
- physical and logical isolation: autosave_kg.json (SK) and autosave_kg_en.json (EN)
- native lossless entity merging (kg merge), migrating all properties and generating alias edges
- context-aware taxonomical category deduction (KG_VERIFY) recognizing biological sub-taxa (marsupials -> mammals)
- non-destructive reverse location reasoning (_execute_reverse_location_query) with multi-stem matching and anti-flora shielding
- uniform attribute traversal via self.kg.get_attributes()
- atomic dual serialization into autosave_kg.json and autosave_kg_en.json
- inbound/outbound graph traversal and orbital level transitions
- multi-hop pathfinding and relation discovery (KG_RELATE)
- developer comfort command execution with state release
- permanent memory resolution suppressing repetitive AUTONOMY proposals

---

# 4. Autonomous ENVOY & Quarantine Subsystem (v5.9.1)
Purpose: Safe, outbound-only external retrieval, domain-guarded semantic normalization, and sliding-window quarantine maintenance.  
Responsibilities:
- Permission Layer 5: identity gating (OWNER/FAMILY/STRANGER), confirmation latching, and outbound policy audits
- Execution Layer 5: autonomous disambiguation triage („môže byť...“), Strip-Bracket Fallback, and language-specific Wikipedia endpoints (sk.wikipedia.org vs. en.wikipedia.org)
- Anti-Prefix Guard: elimination of fuzzy prefix over-matching (Káva -> Kavala)
- Quarantine Sandbox (EnvoyQuarantine5): stores extraction logs in COLNIK-6.x/envoy/quarantine/ with automated sliding-window rotation enforcing a 100-file ceiling
- Normalizer 5: Non-Bio Domain Shield (strictly blocking biological habitat tags on technical/abstract concepts)
- Sentence-Bound Extractor: requiring explicit occurrence verbs (žije, obýva, lives, occurs) before binding habitat edges
- delivering normalized, schema-valid facts to COLNIK-6.x customs inspection

---

# 5. Reasoning Engine 5.9.1 & Deep Explainability (XAI)
Purpose: Structured symbolic reasoning and verifiable proof-tree generation.  
Responsibilities:
- multi-hop rule deduction and property inheritance (DedicsnostVlastnostiRule)
- transitive relation chaining (TranzitivneRelacieRule)
- orbital category reasoning (MultiHopOrbitInferenceRule)
- automatic type inference (AutoTypeInferenceRule)
- ontological & taxonomical category deduction (KG_VERIFY)
- non-destructive reverse location reasoning with anti-flora classification guard
- generating human-readable explanations via KG_EXPLAIN
- generating multi-layer hierarchical proof trees (ASCII + HTML) via KG_EXPLAIN_DEEP
- confidence scoring and evidence tree compilation

---

# 6. Workflow Engine 5.9.1
Purpose: Deterministic multi-step process orchestration.  
Responsibilities:
- workflow state machine executed within sirius_orchestrator.py
- plugin workflow execution and semantic state transitions
- SCHOOLWORK workflow prioritization and academic restriction bypass
- deep explainability routing
- deterministic error handling and safe fallback routing
- COLNIK‑validated workflow steps (Standard & High-Performance IPC Mode)
- AUTONOMY‑aware transitions (Control & Triage Mode)

---

# 7. 4-Panel UI Suite (Port 8080)
Purpose: Modular local dashboard running via browser on port 8080.  
Responsibilities:
- Duplicates Panel: live resource auditing and safe duplicate categorization (REPORT_ONLY), routing removals to HitL Safe Trash
- Triage Panel: visual supervision of quarantine queues and unclassified files (COLNIK-6.x/triage)
- Navigation Panel: deterministic module switching across Runtime, KG, Envoy, and Autonomy
- Terminal Panel: interactive CLI with COLNÍK Guard protection (0.0s blocking of format/diskpart) and automatic state release (currentModule = "none")

---

# 8. COLNIK‑6.x Customs Decision Gate & COLNÍK Guard
Purpose: Authoritative customs inspection gate and command security filter deciding ALLOW / DENY / TRIAGE.  
Responsibilities:
- COLNÍK Guard: 0.0s hard blocking of forbidden commands (format, rmdir /s, diskpart, del /f /s /q c:, drop database)
- Human-in-the-Loop Safe Trash: intercepting file deletions and routing them to quarantine awaiting GET /trash review
- inspecting all Knowledge Graph mutations and workflow steps
- high-performance IPC synchronization with AUTONOMY on port 8080
- verifying entity domain boundaries (Non-Bio Shield validation)
- enforcing identity and policy conformance
- routing suspicious or malformed operations into COLNIK-6.x/triage
- enterprise-grade consistency and cycle-safety enforcement

---

# 9. AUTONOMY 6.x (Decision, Guard, HitL Trash & Triage Engine)
Purpose: Supervised autonomous decision-making and runtime telemetry.  
Responsibilities:
- generating structured learning proposals (kg.learn_proposal) bound to active language stores (SK/EN)
- confirmation state latching preserving pending proposal context across conversation turns
- supervising native lossless entity mergers (kg merge)
- evaluating multi-word reasoning outputs and taxonomical deductions
- enforcing zero proposal recurrence on indexed aliases and committed categories
- coordinating interactive confirmation loops via PanelAPI ([ÁNO/NIE] / [YES/NO])
- governing non-destructive file disposal via Human-in-the-Loop Safe Trash
- Guard supervision: real-time monitoring of CPU, RAM, and Disk metrics
- managing quarantine containment in COLNIK-6.x/triage

---

# 10. Action Execution Engine (EXECUTE 6.x)
Purpose: Deterministic executor for validated proposals.  
Responsibilities:
- executing authorized mutations dispatched via proposals.json
- committing dual-key multi-alias entries to autosave_kg.json or autosave_kg_en.json via RuntimeCore
- executing native entity mergers (kg merge) with zero attribute loss and alias link generation
- executing safe file operations under strict HitL Safe Trash quarantine rules
- enforcing terminal module resets (currentModule = "none")
- producing structured execution telemetry in responses.json with TimeCore cycle_delta() metrics

---

# 11. Filesystem Agent & Safe Trash (FS‑AGENT 5.8)
Purpose: Safe, deterministic filesystem operations and non-destructive trash isolation.  
Responsibilities:
- moving, copying, and validating file paths
- routing deleted items into quarantine storage (GET /trash) rather than direct unverified disk deletion
- rollback-safe file handling
- semantic organization (documents, code, schoolwork)
- COLNIK-validated operations and duplicate detection

---

# 12. Security Family 5.x (Identity Engine 3.1)
Purpose: Behavior-based identity and household safety layer.  
Responsibilities:
- OWNER / FAMILY / STRANGER identity tiers
- behavior-based recognition and access auditing
- safe-mode restrictions for unknown users
- time-limits v3 enforcement
- Schoolwork Engine integration: guaranteeing academic tasks remain unrestricted
- System Agent 5 validation enforcement

---

# 13. Self‑Repair & Health‑Check Layer (5.8)
Purpose: Runtime integrity scanning and safe recovery.  
Responsibilities:
- checking integrity of core runtime modules
- detecting corrupted schemas, broken configs, or invalid states
- executing rollback-safe automatic recovery
- reporting health telemetry to Runtime Core

---

# 14. System Agent 5
Purpose: Final gatekeeper for host system-level operations.  
Responsibilities:
- validating all OS-level actions
- enforcing identity permissions and terminal isolation
- blocking destructive commands and unverified execution via COLNÍK Guard
- deterministic safety verification

---

# 15. Context Memory Engine (CME‑MEM 5.8)
Purpose: Semantic workflow memory.  
Responsibilities:
- tracking recent operational contexts
- storing semantic tags and subject difficulty metadata
- supporting multi-step reasoning traces

---

# 16. Plugin System 5.x
Purpose: Extensible local plugin ecosystem.  
Responsibilities:
- loading plugin manifests
- registering NL commands, workflows, and reasoning hooks
- enforcing safe plugin isolation and COLNIK validation

---

# 17. Windows System Capabilities Layer (WIN‑CAP 5.x)
Purpose: Abstracted, safe access to Windows operating system functions.  
Responsibilities:
- providing controlled OS interfaces (file_ops, app_ops, system_context)
- identity-aware restrictions validated by System Agent 5 and COLNÍK Guard

---

# 18. PASSWORD_VAULT 5.0
Purpose: Encrypted offline credential storage.  
Responsibilities:
- AES-256-GCM vault with PBKDF2 master key derivation
- OWNER-only write, FAMILY read-only, STRANGER blocked

---

# 19. Module Interconnections

All modules communicate through:

User / Web UI / Shell Terminal (Port 8080)
 ↓
Token Guard (Rejects inputs with @#$%^&*)
 ↓
InputParser5 (Punctuation stripping .rstrip("?") & compound phrase preservation)
 ↓
Language Context Router (Binds to autosave_kg.json [SK] or autosave_kg_en.json [EN])
 ↓
sirius_orchestrator.py (Single-Process Daemon on Port 8080 with TerminalAssistant & TimeCore)
 ├── 4-Panel UI Suite (Duplicates, Triage, Navigation, Terminal with state reset)
 ├── TimeCore & Guard (Temporal tracking cycle_delta() & Resource supervision)
 ├── RuntimeCore 5.9.1 & Dual Knowledge Graph Core (autosave_kg.json / autosave_kg_en.json)
 ├── Native Merge Engine (kg merge <src> into <tgt>)
 ├── ReasoningEngine 5.9.1 (Multi-hop, taxonomical KG_VERIFY & Proof trees)
 ├── WorkflowEngine 5.9.1 (Deterministic state transitions)
 ├── Security Family 5.x & Identity Engine 3.1
 ├── Envoy 5 (ExecutionLayer5, Anti-Prefix Guard, EnvoyNormalizer5 & EnvoyQuarantine5)
 ├── COLNIK-6.x Customs Decision Gate (Standard, IPC Mode & COLNÍK Guard)
 ├── HitL Safe Trash (Quarantined file removal pipeline)
 ├── AUTONOMY 6.x (Control, Guard, Triage Mode & Confirmation Latching)
 ├── PanelAPI ([ÁNO/NIE] / [YES/NO] confirmation loops)
 └── EXECUTE 6.x -> Dual KG Commit / Lossless Merge / Safe System Action

---

# 📌 Document Status
Version: 5.9.1 UNIFIED

Updated to reflect the 5.9.0 -> 5.9.1 milestone release, isolated dual-language Knowledge Graph backends (autosave_kg.json & autosave_kg_en.json), native lossless entity merge engine (kg merge), taxonomical category inference (KG_VERIFY), non-destructive reverse habitat reasoning, Token Guard entry-level sanitization, 100-file sliding-window quarantine rotation, COLNÍK Guard 0.0s command blocking, Human-in-the-Loop Safe Trash pipeline, single-process orchestration via sirius_orchestrator.py on port 8080, and complete 4-Panel UI terminal decoupling.

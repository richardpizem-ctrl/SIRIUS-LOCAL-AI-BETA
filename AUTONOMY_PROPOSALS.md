# 🤖 AUTONOMY PROPOSALS 6.x — Supervised Autonomous Decision Generation  
**Status:** ✔ Production-Enhanced  
**Version:** 6.x (Updated for Runtime 5.x UNIFIED)  
**Component:** AUTONOMY Proposal Engine  
**Role:** Generate safe, explainable, supervised autonomous proposals for system actions, workflows, dual-language KG mutations, lossless entity merges, SafeRollback backups, Professor Validator checks, and UI automation under orchestrator and PanelAPI supervision

---

## 🎯 Purpose  
The AUTONOMY Proposal Engine 6.x is responsible for generating **autonomous suggestions** (proposals) based on system context, multi-word semantic parsing, dual-language KG reasoning, identity rules, predictive intelligence, and Triage Mode diagnostics.  
These proposals represent *what SIRIUS thinks should happen next* — but every proposal is supervised, validated, and confirmed through COLNIK‑6.x (Standard & High-Performance IPC Mode), System Agent 5, Token Guard, Professor Validator, SafeRollback resilience, and interactive PanelAPI loops with `[ÁNO/NIE]` / `[YES/NO]` confirmations.

AUTONOMY never executes actions directly.  
It **proposes**, **explains**, **justifies**, **latches confirmation state**, and **waits for validation**.

---

## 🧩 Architecture Overview  
**System Intelligence Layer / InputParser5 → Token Guard → AUTONOMY Proposal Engine → `sirius_orchestrator.py` (Port 8080) → COLNIK (IPC Mode) → PanelAPI [ÁNO/NIE] → Workflow Engine → Dual-Language KG Commit (`autosave_kg.json` / `autosave_kg_en.json`)**

### Core Responsibilities  
- generate autonomous learning proposals (`kg.learn_proposal`) for missing concepts with target language binding (`SK` / `EN`)
- enforce confirmation state latching: track pending proposal entities across interactive turns so user confirmations (`ÁNO` / `YES`) reliably trigger external enrichment
- prevent proposal recurrence: evaluate multi-alias mappings and taxonomical edges so confirmed entities are not repeatedly proposed
- supervise native lossless entity mergers (`kg merge <src> into <tgt>`), relocating attributes without external script dependencies
- support taxonomical category inference (`KG_VERIFY`), automatically establishing and committing sub-taxa relations (e.g., marsupials/macropods -> mammals)
- supervise non-destructive reverse location queries (`_execute_reverse_location_query`) with anti-flora classification guards protecting tree-dwelling fauna
- enforce entry-level input sanitization via Token Guard, blocking malformed injection characters (`@#$%^&*`)
- manage automatic sliding-window rotation limiting quarantine logs in `COLNIK-6.x/envoy/quarantine/` to a 100-file ceiling
- supervise non-destructive file disposal by routing delete requests into the Human-in-the-Loop Safe Trash pipeline (tested in `dist_V6_CHECK`)
- govern SafeRollback crash resilience (`safe_rollback.py`) executing granular module-level backups (`shutil.copytree`) and restorations (`shutil.rmtree`)
- enforce Professor Validator decision matrix (`PASS / WARN / REJECT`) on cognitive outputs
- audit console execution safety via COLNÍK Guard with 0.0s hard blocks on forbidden commands (`format`, `diskpart`)
- interface directly with the 4-Panel UI Suite (`Duplicates`, `Triage`, `Navigation`, `Terminal`) with automatic module release (`currentModule = "none"`)

### Key Files  
- `autonomy/autonomy_proposer.py`  
- `autonomy/proposals.json`  
- `autonomy/proposal_metadata.json`  
- `core/safe_rollback.py`  
- `professor/professor_validator.py`  
- `IPC_DATA/autonomy_events.json`  
- `runtime5/runtime_core_5.py`  
- `runtime5/input_parser_5.py`  
- `runtime5/envoy_execution_layer_5.py`  
- `runtime5/envoy_normalizer_5.py`  
- `runtime5/envoy_quarantine_5.py`  
- `autosave_kg.json`  
- `autosave_kg_en.json`  

---

## 🔍 Proposal Pipeline  

### **1 — Context Collection & Input Sanitization**  
AUTONOMY gathers signals from:  
- Token Guard input filter (verifying absence of forbidden injection symbols `@#$%^&*`)
- InputParser5 with greedy punctuation trimming (`.rstrip("?")`) preventing token key fragmentation
- Active language selector (`SK` / `EN`) binding the operational context to `autosave_kg.json` or `autosave_kg_en.json`
- KG ENGINE, Alias Registry, and Taxonomical Traversal Layer
- ReasoningEngine5 (symbolic derivation rules)
- System Agent 5, Identity Engine, and TimeCore / Guard Monitors

Context determines whether a proposal is safe, relevant, or strictly necessary.

---

### **2 — Proposal Generation & Confirmation Latching**  
AUTONOMY generates proposals across specialized operational categories:

#### **Knowledge Graph & Learning Proposals**
- `kg.learn_proposal` — propose fetching missing entities via Envoy for the active language store
- confirmation state latching — store target entity name in memory so positive responses (`ÁNO`, `ANO`, `YES`, `Y`) directly execute the pending proposal
- `kg_merge` proposal — lossless relocation of attributes from source to target with bidirectional alias preservation
- multi-alias registration — map queried synonyms to official target article titles
- add / remove semantic relation and taxonomical edge commitment (`is_a mammal`, `je cicavec`)
- validate graph consistency and atomic persistence to `autosave_kg.json` or `autosave_kg_en.json`
- enforce zero recurrence: suppress proposals for concepts already stored or inferred

#### **System & File Security Proposals (HitL Safe Trash & SafeRollback)**
- route proposed file deletions (duplicates, empty folders) into quarantine storage rather than executing direct disk removal (tested in `dist_V6_CHECK`)
- require explicit user confirmation via `GET /trash` before permanent removal (tested in `dist_V6_CHECK`)
- enforce automatic sliding-window rotation on `COLNIK-6.x/envoy/quarantine/` at the 100-file threshold
- trigger SafeRollback module-level backup and restore routines on structural anomalies
- optimize CPU/RAM load detected by Guard
- stabilize OS runtime state and trigger self-repair routines

#### **Workflow Proposals**
- advance multi-step workflow
- pause or reroute execution pipeline
- fallback to base lemma when facing parenthetical article names (Strip-Bracket Fallback)
- engage safe-mode execution on network anomalies

#### **UI Automation & Navigation Proposals**
- route queries cleanly across the 4 UI panels (`Duplicates`, `Triage`, `Navigation`, `Terminal`)
- release terminal input focus upon clearing (`currentModule = "none"`) to prevent host CLI lockups
- display interactive confirmation dialogs via PanelAPI (`[ÁNO/NIE]` / `[YES/NO]`)
- block destructive sequences in web views

#### **Identity & Command Security Proposals**
- enforce COLNÍK Guard shell security (0.0s hard block on `format`, `diskpart`, `rmdir /s`)
- restrict action based on identity profile
- enforce STRANGER / FAMILY permission boundaries

---

### **3 — Explainability Generation**  
Every proposal includes:

- KG_EXPLAIN / KG_EXPLAIN_DEEP traces
- multi-hop symbolic reasoning derivation
- rule attribution metadata
- confidence metrics
- justification summary in human-readable natural language

Explainability is mandatory for all autonomous proposals.

---

### **4 — COLNIK‑Validated Routing**  
Before a proposal is staged for user confirmation, COLNIK‑6.x performs:

- enterprise-grade security and mutation validation
- verification against the command categorization matrix (FORBIDDEN, RISKY, ALLOWED)
- check against reversible action constraints and quarantine trash routing
- threat classification and payload inspection
- identity policy enforcement

Unsafe, unverified, or malformed proposals are rejected immediately.

---

### **5 — System Agent Enforcement**  
System Agent 5 checks:

- active identity permissions
- operating system stability metrics
- process safety limits
- terminal execution boundaries and TimeCore telemetry
- self-repair triggers

If safety constraints are violated, the proposal is neutralized.

---

### **6 — Proposal Confirmation & Execution**  
AUTONOMY completes the supervised loop:

- COLNIK authorization check
- System Agent stability approval
- Professor Validator evaluation (`PASS / WARN / REJECT`)
- Explicit user confirmation via PanelAPI (`[ÁNO/NIE]` / `[YES/NO]`)
- Execution of active latch: external context scrape, domain normalization, and alias indexing
- Atomic serialization into the designated language store (`autosave_kg.json` or `autosave_kg_en.json`)

Only after full validation is the proposal converted into an executable workflow.

---

## 🧱 Proposal Types  

### **1 — ALLOW Proposal**  
Safe, verified, explainable, and adheres to identity rules.  
Action proceeds automatically.

### **2 — DENY Proposal**  
Violates security constraints, token guard policies, or command restrictions.  
Action is blocked immediately (0.0s for forbidden commands) and logged.

### **3 — REQUIRE_CONFIRMATION Proposal**  
Covers new knowledge enrichment (`kg.learn_proposal`), node merges, or quarantine deletions.  
Latches target state and requires interactive approval via PanelAPI `[ÁNO/NIE]` / `[YES/NO]`.

### **4 — FALLBACK Proposal**  
Activates alternate safe execution paths (e.g., stripping brackets on disambiguation failure).  
Used during knowledge gaps or system triage states.

### **5 — REPAIR Proposal**  
Engages Self‑Repair Layer and SafeRollback routines.  
Triggered when file duplicities, schema corruption, or sliding window overflows occur.

---

## 🔐 Safety Rules  
- ❌ **Zero Blind Execution:** AUTONOMY never executes mutations without pipeline approval.  
- 🔒 **Customs Clearance Required:** All mutations pass through COLNIK‑6.x inspection.  
- 🗑️ **Human-in-the-Loop Safe Trash:** Deletions are quarantined; direct unverified file deletion is strictly prohibited (tested in `dist_V6_CHECK`).  
- 🛡️ **COLNÍK Guard Shell Access Control:** Immediate 0.0s blocking of destructive shell commands (`format`, `diskpart`, `rmdir /s`).  
- ⛔ **Token Guard Input Sanitization:** Commands containing dangerous symbols (`@#$%^&*`) are rejected at entry.  
- 🗄️ **Dual-Language Isolation:** Proposals strictly target their originating language store (`autosave_kg.json` or `autosave_kg_en.json`), preventing cross-lingual corruption.  
- 🔄 **SafeRollback Backup Protection:** Granular module-level backup and instant restore safeguarding state integrity.  
- ⚖️ **Professor Validator Middleware:** Strict cognitive output verification (`PASS / WARN / REJECT`).  
- ⚠️ **Mandatory Explainability:** Every proposal must carry structural derivation evidence.  
- 🛑 **Zero Proposal Recurrence:** Confirmed concepts and inferred categories auto-commit to disk, suppressing repetitive prompts.  
- 📦 **Quarantine Ceiling Rotation:** Automatically maintains a 100-file ceiling inside `COLNIK-6.x/envoy/quarantine/`.  
- 🛡️ **UI Isolation:** Clearing user input releases panel locks (`currentModule = "none"`), preventing host shell capture.  

---

## 📊 Module Status (v6.0.1)  
- ✔ Fully updated & verified for Runtime 5.x architecture  
- ✔ Dual-Language Graph Isolation (`autosave_kg.json` & `autosave_kg_en.json`) active  
- ✔ Confirmation state latching and punctuation trimming operational  
- ✔ Native Lossless Entity Merge (`kg merge`) proposal handling verified  
- ✔ Taxonomical inference auto-commit (`KG_VERIFY`) operational  
- ✔ Multi-word parsing and noun phrase support active  
- ✔ Token Guard input sanitization active  
- ✔ Envoy quarantine sliding-window rotation (100-file ceiling) active  
- ✔ COLNIK‑6.x High-Performance IPC handshake verified  
- ✔ Safe UI Trash & HitL confirmation pipeline active (tested in `dist_V6_CHECK`)  
- ✔ SafeRollback integration active  
- ✔ Professor Validator matrix operational  
- ✔ PanelAPI interactive confirmation loops functional  
- ✔ Single-process orchestrator integration (Port 8080) complete  

---

## 📂 6. Related Files  
- `AUTONOMY/autonomy.py`  
- `AUTONOMY/state_manager.py`  
- `AUTONOMY/guard.py`  
- `core/safe_rollback.py`  
- `professor/professor_validator.py`  
- `REASONING/engine5.py`  
- `ORCHESTRATOR/sirius_orchestrator.py`  
- `PANEL_API/panel_api.py`  
- `runtime5/runtime_core_5.py`  
- `runtime5/input_parser_5.py`  
- `runtime5/envoy_execution_layer_5.py`  
- `runtime5/envoy_normalizer_5.py`  
- `runtime5/envoy_quarantine_5.py`  
- `IPC_DATA/proposals.json`  
- `IPC_DATA/responses.json`  
- `autosave_kg.json`  
- `autosave_kg_en.json`  

---

## 🏁 7. Summary  
AUTONOMY Proposal Engine 6.x is the supervised autonomous decision generator of SIRIUS Local AI (v6.0.1).  
It generates safe, explainable, identity-aware, and system-aware proposals for dual-language knowledge enrichment, entity mergers, workflows, UI automation, and system diagnostics — fully orchestrated via `sirius_orchestrator.py`, audited by COLNIK‑6.x, safeguarded by Token Guard, HitL Safe Trash, SafeRollback, and Professor Validator, and confirmed via interactive PanelAPI loops.  

It powers a **predictive, deterministic, supervised autonomous system** that acts responsibly, respects user confirmation, and explains its reasoning end-to-end.

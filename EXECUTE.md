# 🔧 EXECUTE 6.x — Action Execution Engine  
**Status:** ✔ Production-Enhanced  
**Version:** 6.x  
**SIRIUS Local AI Version:** 5.9.5  
**Author & Architecture Lead:** Richard Pizem  
**Component:** EXECUTE & Professor Middleware Integration  
**Role:** Deterministic executor for validated proposals from AUTONOMY routed through COLNÍK (Standard & High-Performance IPC Mode), orchestrated via `sirius_orchestrator.py` on Port 8080, and integrated with the Dual-Language KG Engine, Pre-Processing Spellcheck Layer, COLNÍK Guard, SafeRollback crash resilience, Professor Middleware Layer (Cleaner, Validator PASS/WARN/REJECT, Summarizer), and Human-in-the-Loop Safe Trash

---

## 🎯 Purpose  
EXECUTE 6.x is the deterministic action-execution engine of the SIRIUS Local AI system (v5.9.5), designed and architected by Richard Pizem.  
Its role is to safely perform validated system mutations, dispatch atomic graph writes to isolated dual-language stores (`autosave_kg.json` for SK, `autosave_kg_en.json` for EN), execute native lossless entity mergers (`kg merge <src> into <tgt>`), auto-commit deduced taxonomical edges (`KG_VERIFY`), enforce non-destructive file disposal via the Human-in-the-Loop Safe Trash pipeline, govern SafeRollback crash recovery, enforce the **Professor Middleware Layer** cognitive quality gating, respect user confirmations via `PanelAPI` [ÁNO/NIE] / [YES/NO] loops, enforce terminal input decoupling, and produce structured responses for the high-performance IPC pipeline.

V architektúre v5.9.5 platí striktné pravidlo: **Runtime Core a inferenčné mechanizmy môžu pripraviť akúkoľvek akciu či fakt, ale Professor Middleware Layer (Cleaner, Validator PASS/WARN/REJECT, Summarizer) autoritatívne rozhodne, či sa výstup smie uvoľniť používateľovi alebo zaviazať do perzistentného stavu.** EXECUTE 6.x garantuje predvídateľné, kontrolované a bezpečné vykonanie bez rizika neoverených systémových mutácií alebo zablokovania UI panelov.

---

## 🧩 Architecture Overview  
**AUTONOMY → proposals.json → COLNÍK (IPC Mode) → PROFESSOR MIDDLEWARE LAYER (PASS / WARN / REJECT) → PanelAPI [ÁNO/NIE] / [YES/NO] → EXECUTE → Dual-Language Graph Commit (`autosave_kg.json` / `autosave_kg_en.json`) → responses.json → AUTONOMY**

### Core Responsibilities  
- Execute validated proposals under `sirius_orchestrator.py` central loop (Port 8080 with embedded TerminalAssistant + TimeCore)  
- Coordinate with `RuntimeCore` for atomic serialization to designated language stores (`autosave_kg.json` or `autosave_kg_en.json`)  
- Vyžadovať a overovať verdikt vrstvy **Professor Validator (`professor_validator.py`)**:
  - **PASS:** Okamžité uvoľnenie schválenej akcie/faktu na exekúciu a render v UI.  
  - **WARN:** Uvoľnenie s vizuálnym príznakom neistoty pre UI Panel V2.  
  - **REJECT:** Okamžité zastavenie exekúcie pri neúplných dátach (`INCOMPLETE_FACTS`), nízkej istote (`LOW_CONFIDENCE`) alebo protirečení (`CONTRADICTION`).  
- Coordinate with **Professor Cleaner (`grammar_engine.py`)** pre normalizáciu extrahovaných trojíc, zvratných predikátov (*sa/si*) a jazykových zarážok pred commitom  
- Execute native lossless entity mergers (`kg merge`), migrating all properties without data loss and preserving source nodes as directional aliases (`src -[alias]-> tgt`)  
- Auto-commit deduced taxonomical edges (`is_a mammal`, `je cicavec`) directly to graph storage with zero proposal recurrence  
- Enforce the Human-in-the-Loop Safe Trash workflow: quarantine files proposed for deletion rather than executing direct disk removal (`GET /trash`)  
- Enforce automatic sliding-window rotation on `COLNIK-6.x/envoy/quarantine/`, maintaining a strict ceiling of 100 JSON files  
- Govern SafeRollback crash resilience (`safe_rollback.py`) executing granular module-level backups (`shutil.copytree`) and restorations (`shutil.rmtree`)  
- Synchronize directly with the 4-Panel UI Suite (`Duplicates`, `Triage`, `Navigation`, `Terminal`)  
- Enforce state decoupling by ensuring `currentModule = "none"` upon input clearance, preventing host shell capture  
- Generate structured execution responses in `IPC_DATA/responses.json`  
- Enforce strict safety boundaries, Token Guard checks (`@#$%^&*` drop), spellcheck pre-processing, and confirmation latching via `PanelAPI`  
- Maintain deterministic behavior under TimeCore heartbeat (`cycle_delta()`) and Guard resource supervision (CPU, RAM, Disk)  
- Report all operational results back to AUTONOMY without proposal recurrence  

### Key Files  
- `EXECUTE/executor.py`  
- `core/safe_rollback.py`  
- `runtime5/professor_validator.py` (Professor Validator Gate)  
- `runtime5/grammar_engine.py` (Professor Cleaner)  
- `runtime5/professor_miner.py` (Professor Summarizer)  
- `runtime5/spellcheck_engine.py`  
- `IPC_DATA/proposals.json`  
- `IPC_DATA/responses.json`  
- `ORCHESTRATOR/sirius_orchestrator.py`  
- `PANEL_API/panel_api.py`  
- `runtime5/runtime_core_5.py`  
- `runtime5/envoy_execution_layer_5.py`  
- `runtime5/envoy_quarantine_5.py`  
- `autosave_kg.json`  
- `autosave_kg_en.json`  

---

## 🔄 Operational Cycle (v5.9.5)  

### **1 — Ingest Incoming Proposals & Context Dispatch**  
EXECUTE reads structured proposals dispatched by AUTONOMY via:  
`IPC_DATA/proposals.json`

Each proposal package specifies:  
- Action type (e.g., `kg.commit`, `kg.merge`, `file_quarantine`, `system_cleanup`, `state_reset`)  
- Target entity, alias mapping, file path, or language partition (`SK` / `EN`)  
- Safety level (Safe, Restricted, or Critical)  
- Confirmation status (`PanelAPI` [ÁNO/NIE] / [YES/NO] token resolved via confirmation latching)  
- Execution metadata, proof trees, and provenance traces  

### **2 — Customs, Token Guard & Professor Middleware Audit**  
- Verify authorization from COLNIK‑6.x (Customs Inspection & Token Guard entry validation)  
- **Professor Middleware Verification:**
  - Výstup prechádza cez `professor_validator.py`.
  - Ak Professor vráti `REJECT` (napr. pre `INCOMPLETE_FACTS` alebo `CONTRADICTION`), EXECUTE okamžite zruší mutáciu, zapíše dôvod zamietnutia do `responses.json` a postúpi incident do `COLNIK-6.x/triage`.  
  - Pri stave `WARN` priradí EXECUTE k výstupu príznak neistoty pre UI Panel V2.  
  - Pri stave `PASS` pokračuje priamy commit.  
- Verify file path or target graph schema validity (`autosave_kg.json` vs. `autosave_kg_en.json`)  
- Verify that user confirmation (`ÁNO` / `YES`) has been matched against the active confirmation latch  
- Enforce **REPORT_ONLY** policies for system duplicities detected in the Duplicates Panel  
- Enforce quarantine isolation for any deletion request awaiting user review via `GET /trash`  
- Block unconfirmed, malformed, or out-of-scope system mutations  

### **3 — Execute Action Deterministically**  
Supported runtime operations:  
- **Dual-Language Graph Commit:** Atomically writes enriched entities, verified summaries, and aliases cleaned by Professor Cleaner into the active language store (`autosave_kg.json` or `autosave_kg_en.json`).  
- **Native Lossless KG Merge:** Relocates properties from `<src>` to `<tgt>`, converts `<src>` into an alias node with an edge to `<tgt>`, and commits atomically.  
- **Taxonomical Edge Auto-Commit:** Writes verified higher-order biological categories (`is_a mammal`, `je cicavec`) directly to the target graph with zero recurrence.  
- **Quarantine Trash Routing:** Moves deleted items into safe quarantine storage; direct permanent removal is blocked without manual UI confirmation via `GET /trash`.  
- **Quarantine Ceiling Rotation:** Automatically removes oldest records when `COLNIK-6.x/envoy/quarantine/` exceeds 100 JSON files.  
- **UI Module Decoupling:** Immediately resets active panel context (`currentModule = "none"`) when inputs are cleared, shielding the host terminal from unauthorized CLI execution.  
- **Safe File Operations:** Creation, modification, and duplicate tracking (non-critical files only) backed by `safe_rollback.py`.  
- **System Tasks:** Safe local system maintenance audited by COLNÍK Guard (0.0s block on forbidden shell commands).  

All actions follow strict deterministic rules and cannot alter AUTONOMY decision parameters.

### **4 — Generate Structured Response**  
Execution outcomes are serialized into:  
`IPC_DATA/responses.json`

Each response contains:  
- Status (`success`, `fail`, `report_only`, `quarantined`, `professor_reject`)  
- Professor Validator status (`PASS`, `WARN`, `REJECT`) a validačný kód  
- Action executed, language partition, and affected target  
- Dual-graph commit verification tokens  
- Guard system telemetry metrics and TimeCore `cycle_delta()` logs  
- Reversibility, rollback hashes, and audit logs  

### **5 — State Synchronization & Cleanup**  
Temporary buffers and transient tokens are cleared. EXECUTE updates the active runloop state and returns execution control to `sirius_orchestrator.py` under Guard runtime monitoring.

---

## 🔐 Safety Rules  

### Critical Guarantees  
- 🎓 **Professor Quality Gating:** Žiadna kognitívna akcia nesmie byť zapísaná do grafu ani uvoľnená do UI bez validácie cez Professor Validator (`PASS / WARN / REJECT`).  
- 🔒 **Zero Direct Unverified Deletions:** Files flagged for removal are quarantined; direct unverified file deletion is strictly prohibited (Human-in-the-Loop Safe Trash via `GET /trash`).  
- ⛔ **Token Guard Input Sanitization:** Commands containing dangerous character sequences (`@#$%^&*`) are dropped at entry.  
- 🛡️ **COLNÍK Guard Shell Filter:** Immediate 0.0s hard blocking of forbidden commands (`format`, `rmdir /s`, `del /f /s /q c:`, `diskpart`, `drop database`).  
- 🗄️ **Dual-Language Graph Segregation:** EXECUTE strictly targets `autosave_kg.json` or `autosave_kg_en.json` according to caller context, preventing cross-lingual contamination.  
- 🔄 **SafeRollback Crash Resilience:** Granular module-level backups (`shutil.copytree`) and restorations (`shutil.rmtree`) protecting state integrity before destructive actions.  
- 🔁 **Report-Only Duplicates:** Duplicate file actions default to `REPORT_ONLY` to avoid unintentional data loss.  
- 🛑 **Zero Proposal Recurrence:** Once a concept or taxonomical relation is committed, duplicate proposal triggers are permanently suppressed.  
- ⚠ **Mandatory Confirmation & Latching:** Sensitive operations and novel knowledge retrieval mandate explicit user approval via `PanelAPI` [ÁNO/NIE] / [YES/NO] with active state latching.  
- 📦 **Quarantine Ceiling Enforcement:** Automatically maintains a 100-file ceiling inside `COLNIK-6.x/envoy/quarantine/` via sliding window pruning.  
- 🔒 **UI & Terminal Isolation:** Clearing input immediately resets active execution context to `none` (`currentModule = "none"`), completely preventing terminal capture.  
- 🛡 **No Autonomy Logic Alteration:** EXECUTE cannot modify autonomy policies, reasoning rules, or permission models.  
- 🚫 **Zero Cloud Transmission:** 100% offline; execution is strictly confined to local hardware.  

---

## 📊 Module Status (v5.9.5)  
- ✔ Fully implemented & optimized for Runtime 5.9.5 architecture  
- ✔ Autor architektúry: Richard Pizem  
- ✔ Professor Middleware Layer plne integrovaná do exekučného cyklu  
- ✔ Professor Validator brána (`PASS / WARN / REJECT`) aktívna  
- ✔ Professor Cleaner (`grammar_engine.py`) normalizácia overená  
- ✔ Production-enhanced & verified under Windows 11 on port 8080  
- ✔ Dual-Language Graph Isolation (`autosave_kg.json` & `autosave_kg_en.json`) operational  
- ✔ Native Lossless Entity Merge (`kg merge`) validated  
- ✔ Taxonomical category inference auto-commit (`KG_VERIFY`) operational  
- ✔ Human-in-the-Loop Safe Trash quarantine pipeline active (`GET /trash`)  
- ✔ Hard Token Guard entry-level sanitization active (`@#$%^&*` drop)  
- ✔ Automatic 100-file sliding-window quarantine rotator operational  
- ✔ SafeRollback backup & restore module integrated (`safe_rollback.py`)  
- ✔ COLNÍK Guard shell access control (0.0s block on `format`) operational  
- ✔ Terminal decoupling and module state reset confirmed (`currentModule = "none"`)  
- ✔ Integrated single-process IPC daemon operational on port 8080  
- ✔ COLNÍK-6.x Customs validation handshake verified  
- ✔ AUTONOMY 6.x proposal & confirmation cycle verified  
- ✔ 4-Panel UI Suite synchronization operational  
- ✔ TimeCore heartbeat & Guard resource tracking active  

---

## 📂 Related Files  
- `EXECUTE/executor.py`  
- `core/safe_rollback.py`  
- `runtime5/professor_validator.py`  
- `runtime5/grammar_engine.py`  
- `runtime5/professor_miner.py`  
- `runtime5/spellcheck_engine.py`  
- `IPC_DATA/proposals.json`  
- `IPC_DATA/responses.json`  
- `COLNIK/colnik_manager.py`  
- `AUTONOMY/autonomy.py`  
- `ORCHESTRATOR/sirius_orchestrator.py`  
- `PANEL_API/panel_api.py`  
- `runtime5/runtime_core_5.py`  
- `runtime5/envoy_quarantine_5.py`  
- `autosave_kg.json`  
- `autosave_kg_en.json`  

---

## 🏁 Summary  
EXECUTE 6.x is the deterministic execution engine of SIRIUS Local AI (v5.9.5), navrhnutý Richardom Pizemom.  
It carries out authorized actions safely, writes knowledge to isolated dual-language graph stores, performs native lossless entity mergers, auto-commits inferred taxonomies, routes file disposals into the Human-in-the-Loop Safe Trash quarantine, defends the host environment via Token Guard, COLNÍK Guard, SafeRollback, and **Professor Middleware Layer**, protects against terminal command capture, and returns structured execution telemetry to AUTONOMY under central orchestrator supervision.  
Its deterministic logic guarantees safe, predictable, quality-validated, and fully auditable operations across the entire SIRIUS 5.9.5 architecture.

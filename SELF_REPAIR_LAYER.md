# 🔧 SELF‑REPAIR LAYER 5.8 — Autonomous Integrity, Recovery & Runtime Stabilization  
**Status:** ✔ Active (Enhanced)  
**Version:** 5.8 (Updated for 5.9.0 UNIFIED)  
**Component:** Self‑Repair Layer  
**Role:** Automatic detection, stabilization, recovery, and repair of runtime components, configs, multi-alias KG, workflows, and terminal states under single-process orchestrator supervision

---

## 🎯 Purpose  
The Self‑Repair Layer 5.8 is responsible for maintaining the operational stability, structural integrity, and cryptographic reliability of SIRIUS Local AI (v5.9.0).  
It detects schema corruption, missing modules, unstable execution states, broken configs, multi-alias Knowledge Graph inconsistencies, and terminal session locks — then repairs them automatically or routes them through `sirius_orchestrator.py` on Port 8080, interactive `PanelAPI` confirmation loops (`[ÁNO/NIE]`), `TimeCore`/`Guard` supervision, and AUTONOMY‑6.x for supervised containment in `COLNIK-6.x/triage`.

Self‑Repair ensures that SIRIUS remains **stable, deterministic, safe, linguistically intact, and fully operational**, even under severe hardware or storage failure conditions.

---

## 🧩 Architecture Overview  
**System Intelligence Layer & Guard → Self‑Repair Layer → sirius_orchestrator.py (Port 8080) → System Agent 5 → AUTONOMY 6.x → COLNIK-6.x → PanelAPI [ÁNO/NIE] → Multi-Alias KG Persistence (`autosave_kg.json`)**

### Core Responsibilities  
- detect corrupted, truncated, or missing configuration and codebase files  
- validate runtime integrity against cryptographic hash seals  
- repair broken JSON stores and config templates  
- stabilize multi-alias Knowledge Graph operations and dual-key indexes in `autosave_kg.json`  
- enforce zero proposal recurrence by repairing missing alias references  
- recover workflow states and reset active module context (`currentModule = "none"`) upon terminal lockups  
- enforce safe fallback logic and degraded-mode sandboxing  
- supply derivation evidence for `KG_EXPLAIN` and `KG_EXPLAIN_DEEP` proof trees  
- coordinate single-process orchestrator recovery on port 8080  
- route unresolvable structural anomalies directly into `COLNIK-6.x/triage`  

### Key Files  
- `self_repair/self_repair_engine.py`  
- `self_repair/integrity_map.json`  
- `self_repair/baseline_runtime4/`  
- `self_repair/repair_log.json`  
- `KG/autosave_kg.json`  
- `ORCHESTRATOR/sirius_orchestrator.py`  
- `PANEL_API/panel_api.py`  
- `IPC_DATA/proposals.json`  

---

## 🔍 Repair Pipeline (v5.9.0)  

### **1 — Integrity Scan & Hash Verification**  
Self‑Repair performs periodic scans managed under `TimeCore` execution bounds:  
- file presence and byte-size checks  
- SHA-256 cryptographic verification against `integrity_map.json`  
- module syntax and signature audit  
- JSON schema conformance validation  
- multi-alias graph consistency in `autosave_kg.json`  
- workflow state and terminal focus tracking  

If any anomaly or hash mismatch is detected, repair mode triggers immediately.

---

### **2 — System‑Context & Guard Validation**  
Self‑Repair coordinates with the System Intelligence Layer and `Guard`:  
- host OS health inspection (CPU, RAM, and Disk metric telemetry)  
- process anomaly detection and execution loop monitoring  
- active workflow locking checks  

Repairs are paused during extreme host OS loads or active disk writes to prevent race conditions.

---

### **3 — Baseline Comparison & Shadow Restoration**  
Self‑Repair compares runtime files against verified reference stores:  
- `baseline_runtime4/` templates  
- `integrity_map.json` hash registries  
- verified configuration baselines  

Missing or corrupted system files are reconstructed automatically from baseline templates.

---

### **4 — Multi-Alias KG Stabilization**  
Self‑Repair validates the Knowledge Graph architecture:  
- verifies canonical entity and registered alias parity  
- validates that compound noun phrases (`InputParser5`) are mapped without token fragmentation  
- audits `autosave_kg.json` against atomic serialization markers  
- verifies domain boundaries: cleanses accidental biological habitat tags from technical or abstract nodes (Non-Bio Domain Shield enforcement)  
- eliminates redundant learning proposal triggers for existing entities (Zero Recurrence guarantee)  

If `autosave_kg.json` suffers corruption, Self‑Repair reconstructs the graph from atomic shadow backups.

---

### **5 — Terminal & Workflow State Decoupling Recovery**  
Self‑Repair restores runtime flow and UI interactivity:  
- detects terminal deadlocks or unreleased command modules  
- forces state reset (`currentModule = "none"`), restoring input focus to the web interface on port 8080  
- prevents user queries from leaking into the host operating system shell  
- restores interrupted workflow state machines to their last valid deterministic checkpoint  

---

### **6 — COLNIK‑6.x Customs Clearance (Standard & High-Performance IPC Mode)**  
All repair operations are audited through the Kýklos decision gate:  
- structural integrity and cycle-safety checks  
- reversible repair validation  
- threat classification and quarantine routing  
- suspicious or irreparable payloads are dispatched to `COLNIK-6.x/triage` for manual review via the Triage Panel  

---

### **7 — AUTONOMY 6.x & PanelAPI-Supervised Repair Proposals**  
AUTONOMY‑6.x (Control, Guard & Triage Mode) and interactive `PanelAPI` confirmation loops (`[ÁNO/NIE]`) govern high-impact recoveries:  
- mass file rollbacks  
- primary Knowledge Graph rebuilds  
- system configuration resets  
- destructive replacement of user data  

AUTONOMY assesses risk, and the user approves or denies via `PanelAPI`.

---

## 🧱 Repair Capabilities  

### **Automatic Repairs**  
- missing configuration files and baseline scripts  
- corrupted JSON documents and schema mismatches  
- `autosave_kg.json` dual-key alias reconstruction  
- terminal focus reset (`currentModule = "none"`)  
- workflow state machine rollback to safe checkpoints  
- module re-initialization within `sirius_orchestrator.py`  

### **Stabilization**  
- degraded-mode fallback isolation  
- safe-mode restriction upon STRANGER detection  
- non-destructive shadow writing  
- quarantine containment in `COLNIK-6.x/triage`  

### **Explainability (XAI)**  
- `KG_EXPLAIN` direct recovery rationale  
- `KG_EXPLAIN_DEEP` hierarchical proof trees detailing repair derivations  
- repair audit logging with full timestamp and provenance metadata  

---

## 🔐 Safety Rules  
- ❌ No repair execution during critical host OS instability or power drop  
- 🔒 Mandatory customs validation via COLNIK‑6.x (Standard & High-Performance IPC Mode)  
- 🛡 Supervised recovery via AUTONOMY 6.x (Control, Guard & Triage Mode)  
- 💬 High-impact restorations mandate interactive user confirmation via `PanelAPI` `[ÁNO/NIE]`  
- 🛑 Terminal deadlocks must unconditionally force `currentModule = "none"`  
- 🚫 Restored Knowledge Graph nodes must respect Non-Bio Domain Shielding  
- 🔁 Reversible file operations enforced; no unrecoverable file deletions  
- ⚠ Real-time hardware telemetry (CPU, RAM, Disk) continuously audited via Guard  

---

## 📊 Module Status (v5.9.0)  
- ✔ Fully implemented & synchronized with Runtime 5.9.0  
- ✔ Cryptographic hash scans and baseline restoration verified  
- ✔ Multi-alias KG stabilization active (`autosave_kg.json`)  
- ✔ Terminal state decoupling and module release confirmed  
- ✔ Single-process orchestrator integration on port 8080 operational  
- ✔ Interactive PanelAPI confirmation loops functional  
- ✔ TimeCore temporal bounds and Guard telemetry supervision active  
- ✔ COLNIK‑6.x Customs validation functional (Standard & IPC Mode)  
- ✔ AUTONOMY 6.x governance and triage queue integration operational  
- ✔ Explainability proof trees (`KG_EXPLAIN_DEEP`) verified  

---

## 🏁 Summary  
Self‑Repair Layer 5.8 is the autonomous stabilization and recovery core of SIRIUS Local AI (v5.9.0).  
It detects file corruption, restores broken configurations, stabilizes multi-alias graph structures, resets decoupled terminal states, and recovers workflows — ensuring that every repair is safe, explainable, orchestrator-supervised, autonomy‑aware, and COLNIK‑validated.

It establishes SIRIUS as a **self‑healing, deterministic, offline-first intelligent runtime** engineered for continuous reliability on local hardware.

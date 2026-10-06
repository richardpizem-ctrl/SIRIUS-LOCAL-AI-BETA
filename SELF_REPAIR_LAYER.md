# 🔧 SELF‑REPAIR LAYER 5.8 — Autonomous Integrity, Recovery & Runtime Stabilization  
**Status:** ✔ Active (Enhanced)  
**Version:** 5.8 (Updated for 5.9.1 UNIFIED)  
**Component:** Self‑Repair Layer  
**Role:** Automatic detection, stabilization, recovery, and repair of runtime components, configs, dual-language KG partitions, native entity merges, workflows, and terminal states under single-process orchestrator supervision

---

## 🎯 Purpose  
The Self‑Repair Layer 5.8 is responsible for maintaining the operational stability, structural integrity, and cryptographic reliability of SIRIUS Local AI (v5.9.1).  
It detects schema corruption, missing modules, unstable execution states, broken configs, cross-lingual Knowledge Graph leaks between `autosave_kg.json` and `autosave_kg_en.json`, native entity merge discrepancies, quarantine overflow (> 100 files), and terminal session locks — then repairs them automatically or routes them through `sirius_orchestrator.py` on Port 8080 with embedded `TerminalAssistant` and `TimeCore` (`cycle_delta()`), interactive `PanelAPI` confirmation loops (`[ÁNO/NIE]` / `[YES/NO]`) with confirmation state latching, `Guard` supervision, COLNÍK Guard command interception (0.0s), and AUTONOMY‑6.x for supervised containment in `COLNIK-6.x/triage`.

Self‑Repair ensures that SIRIUS remains **stable, deterministic, safe, linguistically segregated, protected from destructive shell commands, and fully operational**, even under severe hardware or storage failure conditions.

---

## 🧩 Architecture Overview  
**System Intelligence Layer & Guard → Self‑Repair Layer → sirius_orchestrator.py (Port 8080 with TerminalAssistant) → System Agent 5 → AUTONOMY 6.x → COLNIK-6.x (COLNÍK Guard & Safe Trash) → PanelAPI [ÁNO/NIE] / [YES/NO] → Dual KG Commit (`autosave_kg.json` / `autosave_kg_en.json`)**

### Core Responsibilities  
- detect corrupted, truncated, or missing configuration, codebase, and schema files  
- validate runtime integrity against cryptographic hash seals  
- repair broken JSON stores and config templates  
- stabilize dual-language Knowledge Graph partitions: enforce strict isolation between Slovak (`autosave_kg.json`) and English (`autosave_kg_en.json`)  
- verify and heal native entity merge integrity (`kg merge`), ensuring all properties are retained and alias pointers (`src -[alias]-> tgt`) remain acyclic  
- enforce sliding-window quarantine maintenance: prune stale records in `COLNIK-6.x/envoy/quarantine/` if count exceeds 100 JSON payloads  
- sanitize trailing punctuation anomalies (`.rstrip("?")`) and heal dropped proposal confirmation latch states  
- enforce zero proposal recurrence by repairing missing alias references and committing deduced taxonomies (`KG_VERIFY`)  
- recover workflow states and reset active module context (`currentModule = "none"`) upon terminal lockups  
- enforce safe fallback logic, Human-in-the-Loop Safe Trash routing, and degraded-mode sandboxing  
- supply derivation evidence for `KG_EXPLAIN` and `KG_EXPLAIN_DEEP` proof trees  
- coordinate single-process orchestrator recovery on port 8080  
- route unresolvable structural anomalies directly into `COLNIK-6.x/triage`  

### Key Files  
- `self_repair/self_repair_engine.py`  
- `self_repair/integrity_map.json`  
- `self_repair/baseline_runtime4/`  
- `self_repair/repair_log.json`  
- `autosave_kg.json`  
- `autosave_kg_en.json`  
- `runtime5/runtime_core_5.py`  
- `runtime5/envoy_quarantine_5.py`  
- `ORCHESTRATOR/sirius_orchestrator.py`  
- `PANEL_API/panel_api.py`  
- `IPC_DATA/proposals.json`  

---

## 🔍 Repair Pipeline (v5.9.1)  

### **1 — Integrity Scan & Hash Verification**  
Self‑Repair performs periodic scans managed under `TimeCore` execution bounds (`cycle_delta()`):  
- file presence and byte-size checks  
- SHA-256 cryptographic verification against `integrity_map.json`  
- module syntax and signature audit  
- JSON schema conformance validation across both `autosave_kg.json` and `autosave_kg_en.json`  
- audit quarantine storage ceiling (verifies `COLNIK-6.x/envoy/quarantine/` does not exceed 100 JSON records)  
- workflow state and terminal focus tracking  

If any anomaly or hash mismatch is detected, repair mode triggers immediately.

---

### **2 — System‑Context & Guard Validation**  
Self‑Repair coordinates with the System Intelligence Layer, `TimeCore`, and `Guard`:  
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

### **4 — Dual-Language KG Stabilization & Native Merge Healing**  
Self‑Repair validates the Knowledge Graph architecture:  
- audits linguistic boundary separation: detects and purges English entities inadvertently committed into `autosave_kg.json` and vice versa  
- repairs native entity merges (`kg merge`): verifies that relocated properties exist in `<target>` and ensures `<source>` points cleanly to `<target>` as an alias edge without orphan nodes  
- auto-commits missing taxonomical edges verified during runtime reasoning (`KG_VERIFY`), preventing repetitive proposal loops  
- audits `autosave_kg.json` and `autosave_kg_en.json` against atomic serialization markers  
- verifies domain boundaries: cleanses accidental biological habitat tags from technical or abstract nodes (Non-Bio Domain Shield enforcement)  
- eliminates redundant learning proposal triggers for existing entities and aliases (Zero Recurrence guarantee)  

If either graph store suffers corruption, Self‑Repair reconstructs the data from atomic shadow backups.

---

### **5 — Terminal, Token Guard & Safe Trash Decoupling Recovery**  
Self‑Repair restores runtime flow, command filtering, and UI interactivity:  
- detects terminal deadlocks or unreleased command modules  
- forces state reset (`currentModule = "none"`), restoring input focus to the web interface on port 8080  
- verifies COLNÍK Guard interception rules, guaranteeing that destructive commands (`format`, `diskpart`, `rmdir /s`) remain permanently blocked in 0.0s  
- audits Human-in-the-Loop Safe Trash queues, ensuring deleted files reside safely in quarantine awaiting user approval via `GET /trash` rather than direct unverified disk deletion  
- clears malformed input tokens dropped by Token Guard (`@#$%^&*`)  
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
AUTONOMY‑6.x (Control, Guard, Safe Trash & Triage Mode) and interactive `PanelAPI` confirmation loops (`[ÁNO/NIE]` / `[YES/NO]`) with confirmation state latching govern high-impact recoveries:  
- mass file rollbacks  
- primary Knowledge Graph rebuilds across `autosave_kg.json` or `autosave_kg_en.json`  
- system configuration resets  
- destructive replacement of user data  

AUTONOMY assesses risk, and the user approves or denies via `PanelAPI`.

---

## 🧱 Repair Capabilities  

### **Automatic Repairs**  
- missing configuration files and baseline scripts  
- corrupted JSON documents and schema mismatches  
- `autosave_kg.json` and `autosave_kg_en.json` partition alignment and alias reconstruction  
- native merge alias link repair (`kg merge`)  
- quarantine sliding-window rotation (pruning files in excess of 100)  
- trailing punctuation trimming (`.rstrip("?")`) and confirmation state latch restoration  
- terminal focus reset (`currentModule = "none"`)  
- workflow state machine rollback to safe checkpoints  
- module re-initialization within `sirius_orchestrator.py`  

### **Stabilization**  
- degraded-mode fallback isolation  
- safe-mode restriction upon STRANGER detection  
- non-destructive shadow writing  
- quarantine containment in `COLNIK-6.x/triage`  
- diversion of file deletions into HitL Safe Trash  

### **Explainability (XAI)**  
- `KG_EXPLAIN` direct recovery rationale  
- `KG_EXPLAIN_DEEP` hierarchical proof trees detailing repair derivations  
- repair audit logging with full timestamp, latency deltas (`cycle_delta()`), and provenance metadata  

---

## 🔐 Safety Rules  
- ❌ No repair execution during critical host OS instability or power drop  
- 🔒 Mandatory customs validation via COLNIK‑6.x (Standard & High-Performance IPC Mode)  
- 🛡 Supervised recovery via AUTONOMY 6.x (Control, Guard, Safe Trash & Triage Mode)  
- 💬 High-impact restorations mandate interactive user confirmation via `PanelAPI` `[ÁNO/NIE]` / `[YES/NO]`  
- 🛑 Terminal deadlocks must unconditionally force `currentModule = "none"`  
- ⛔ Destructive shell commands (`format`, `diskpart`) must remain hard-blocked in 0.0s  
- 🗄️ Slovak and English knowledge graphs must remain strictly segregated during recovery  
- 📦 Quarantine storage must be pruned to maintain the 100-file ceiling  
- 🚫 Restored Knowledge Graph nodes must respect Non-Bio Domain Shielding  
- 🔁 Reversible file operations enforced; direct unverified file deletions prohibited  
- ⚠ Real-time hardware telemetry (CPU, RAM, Disk) continuously audited via Guard  

---

## 📊 Module Status (v5.9.1)  
- ✔ Fully implemented & synchronized with Runtime 5.9.1 architecture  
- ✔ Cryptographic hash scans and baseline restoration verified  
- ✔ Dual-language KG stabilization active (`autosave_kg.json` & `autosave_kg_en.json`)  
- ✔ Native `kg merge` alias healing verified  
- ✔ Quarantine sliding-window ceiling (100 files) enforced  
- ✔ COLNÍK Guard 0.0s command blocking integration active  
- ✔ Human-in-the-Loop Safe Trash pipeline verified  
- ✔ Token Guard input hygiene & trailing punctuation stripping active  
- ✔ Terminal state decoupling and module release confirmed  
- ✔ Single-process orchestrator integration on port 8080 operational with embedded TerminalAssistant + TimeCore  
- ✔ Interactive PanelAPI confirmation loops with state latching functional  
- ✔ TimeCore latency tracking (`cycle_delta()`) and Guard telemetry supervision active  
- ✔ COLNIK‑6.x Customs validation functional (Standard & IPC Mode)  
- ✔ AUTONOMY 6.x governance and triage queue integration operational  
- ✔ Explainability proof trees (`KG_EXPLAIN_DEEP`) verified  

---

## 🏁 Summary  
Self‑Repair Layer 5.8 is the autonomous stabilization and recovery core of SIRIUS Local AI (v5.9.1).  
It detects file corruption, restores broken configurations, stabilizes dual-language graph partitions, heals native entity merge links, prunes sliding-window quarantine queues, resets decoupled terminal states, and recovers workflows — ensuring that every repair is safe, explainable, orchestrator-supervised, autonomy‑aware, and COLNIK‑validated.

It establishes SIRIUS as a **self‑healing, deterministic, offline-first intelligent runtime** engineered for continuous reliability, strict security isolation, and data integrity on local hardware.

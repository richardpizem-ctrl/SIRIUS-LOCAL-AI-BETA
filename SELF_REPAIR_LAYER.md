# 🔧 SELF‑REPAIR LAYER 5.8 — Autonomous Integrity, Recovery & Runtime Stabilization  
**Status:** ✔ Active (Enhanced)  
**Version:** 5.8 (Updated for 6.0.1 UNIFIED)  
**Component:** Self‑Repair Layer  
**Role:** Automatic detection, stabilization, recovery, and repair of runtime components, configs, dual-language KG partitions, native entity merges, workflows, and terminal states under single-process orchestrator supervision

---

## 🎯 Purpose  
The Self‑Repair Layer is responsible for maintaining the operational stability, structural integrity, and cryptographic reliability of SIRIUS Local AI (v6.0.1)[cite: 1].  
It detects schema corruption, missing modules, unstable execution states, broken configs, cross-lingual Knowledge Graph leaks between `autosave_kg.json` and `autosave_kg_en.json`, native entity merge discrepancies, quarantine overflow (> 100 files), and terminal session locks — then repairs them automatically or routes them through `sirius_orchestrator.py` on Port 8080 with embedded `TerminalAssistant` and `TimeCore` (`cycle_delta()`), interactive `PanelAPI` confirmation loops (`[ÁNO/NIE]` / `[YES/NO]`) with confirmation state latching, `Guard` supervision, COLNÍK Guard command interception (0.0s), SafeRollback crash protection (`safe_rollback.py`), Professor Middleware cognitive verification (`PASS / WARN / REJECT`), and AUTONOMY‑6.x for supervised containment in `COLNIK-6.x/triage`[cite: 1].

Self‑Repair ensures that SIRIUS remains **stable, deterministic, safe, linguistically segregated, protected from destructive shell commands, and fully operational**, even under severe hardware or storage failure conditions[cite: 1].

---

## 🧩 Architecture Overview  
**System Intelligence Layer & Guard → Self‑Repair Layer → sirius_orchestrator.py (Port 8080 with TerminalAssistant) → System Agent 5 → SafeRollback (`safe_rollback.py`) → Professor Validator (PASS/WARN/REJECT) → AUTONOMY 6.x → COLNIK-6.x (COLNÍK Guard & Safe Trash) → PanelAPI [ÁNO/NIE] / [YES/NO] → Dual KG Commit (`autosave_kg.json` / `autosave_kg_en.json`)**

### Core Responsibilities  
- detect corrupted, truncated, or missing configuration, codebase, and schema files[cite: 1]  
- validate runtime integrity against cryptographic hash seals[cite: 1]  
- repair broken JSON stores and config templates[cite: 1]  
- stabilize dual-language Knowledge Graph partitions: enforce strict isolation between Slovak (`autosave_kg.json`) and English (`autosave_kg_en.json`)[cite: 1]  
- verify and heal native entity merge integrity (`kg merge`), ensuring all properties are retained and alias pointers (`src -[alias]-> tgt`) remain acyclic[cite: 1]  
- enforce sliding-window quarantine maintenance: prune stale records in `COLNIK-6.x/envoy/quarantine/` if count exceeds 100 JSON payloads[cite: 1]  
- sanitize trailing punctuation anomalies (`.rstrip("?")`) and heal dropped proposal confirmation latch states[cite: 1]  
- enforce zero proposal recurrence by repairing missing alias references and committing deduced taxonomies (`KG_VERIFY`)[cite: 1]  
- recover workflow states and reset active module context (`currentModule = "none"`) upon terminal lockups[cite: 1]  
- enforce safe fallback logic, Human-in-the-Loop Safe Trash routing (tested in `dist_V6_CHECK`), and degraded-mode sandboxing[cite: 1]  
- protect module consistency via SafeRollback (`safe_rollback.py`) before applying corrective mutations[cite: 1]  
- supply derivation evidence for `KG_EXPLAIN` and `KG_EXPLAIN_DEEP` proof trees[cite: 1]  
- coordinate single-process orchestrator recovery on port 8080[cite: 1]  
- route unresolvable structural anomalies directly into `COLNIK-6.x/triage`[cite: 1]  

### Key Files  
- `self_repair/self_repair_engine.py`  
- `self_repair/integrity_map.json`  
- `core/safe_rollback.py`  
- `self_repair/baseline_runtime4/`  
- `self_repair/repair_log.json`  
- `autosave_kg.json`  
- `autosave_kg_en.json`  
- `runtime5/runtime_core_5.py`  
- `runtime5/professor_validator.py`  
- `runtime5/envoy_quarantine_5.py`  
- `ORCHESTRATOR/sirius_orchestrator.py`  
- `PANEL_API/panel_api.py`  
- `IPC_DATA/proposals.json`  

---

## 🔍 Repair Pipeline (v6.0.1)  

### **1 — Integrity Scan & Hash Verification**  
Self‑Repair performs periodic scans managed under `TimeCore` execution bounds (`cycle_delta()`)[cite: 1]:  
- file presence and byte-size checks[cite: 1]  
- SHA-256 cryptographic verification against `integrity_map.json`[cite: 1]  
- module syntax and signature audit[cite: 1]  
- JSON schema conformance validation across both `autosave_kg.json` and `autosave_kg_en.json`[cite: 1]  
- audit quarantine storage ceiling (verifies `COLNIK-6.x/envoy/quarantine/` does not exceed 100 JSON records)[cite: 1]  
- workflow state and terminal focus tracking[cite: 1]  

If any anomaly or hash mismatch is detected, repair mode triggers immediately.

---

### **2 — System‑Context & Guard Validation**  
Self‑Repair coordinates with the System Intelligence Layer, `TimeCore`, and `Guard`[cite: 1]:  
- host OS health inspection (CPU, RAM, and Disk metric telemetry)[cite: 1]  
- process anomaly detection and execution loop monitoring[cite: 1]  
- active workflow locking checks[cite: 1]  

Repairs are paused during extreme host OS loads or active disk writes to prevent race conditions.

---

### **3 — Baseline Comparison & Shadow Restoration**  
Self‑Repair compares runtime files against verified reference stores[cite: 1]:  
- `baseline_runtime4/` templates[cite: 1]  
- `integrity_map.json` hash registries[cite: 1]  
- verified configuration baselines[cite: 1]  

Missing or corrupted system files are reconstructed automatically from baseline templates.

---

### **4 — Dual-Language KG Stabilization & Native Merge Healing**  
Self‑Repair validates the Knowledge Graph architecture[cite: 1]:  
- audits linguistic boundary separation: detects and purges English entities inadvertently committed into `autosave_kg.json` and vice versa[cite: 1]  
- repairs native entity merges (`kg merge`): verifies that relocated properties exist in `<target>` and ensures `<source>` points cleanly to `<target>` as an alias edge without orphan nodes[cite: 1]  
- auto-commits missing taxonomical edges verified during runtime reasoning (`KG_VERIFY`), preventing repetitive proposal loops[cite: 1]  
- audits `autosave_kg.json` and `autosave_kg_en.json` against atomic serialization markers[cite: 1]  
- verifies domain boundaries: cleanses accidental biological habitat tags from technical or abstract nodes (Non-Bio Domain Shield enforcement)[cite: 1]  
- eliminates redundant learning proposal triggers for existing entities and aliases (Zero Recurrence guarantee)[cite: 1]  

If either graph store suffers corruption, Self‑Repair reconstructs the data from atomic shadow backups and SafeRollback snapshots.

---

### **5 — Terminal, Token Guard & Safe Trash Decoupling Recovery**  
Self‑Repair restores runtime flow, command filtering, and UI interactivity[cite: 1]:  
- detects terminal deadlocks or unreleased command modules[cite: 1]  
- forces state reset (`currentModule = "none"`), restoring input focus to the web interface on port 8080[cite: 1]  
- verifies COLNÍK Guard interception rules, guaranteeing that destructive commands (`format`, `diskpart`, `rmdir /s`) remain permanently blocked in 0.0s[cite: 1]  
- audits Human-in-the-Loop Safe Trash queues (tested in `dist_V6_CHECK`), ensuring deleted files reside safely in quarantine awaiting user approval via `GET /trash` rather than direct unverified disk deletion[cite: 1]  
- clears malformed input tokens dropped by Token Guard (`@#$%^&*`)[cite: 1]  
- restores interrupted workflow state machines to their last valid deterministic checkpoint[cite: 1]  

---

### **6 — COLNIK‑6.x Customs Clearance (Standard & High-Performance IPC Mode)**  
All repair operations are audited through the Kýklos decision gate[cite: 1]:  
- structural integrity and cycle-safety checks[cite: 1]  
- reversible repair validation[cite: 1]  
- threat classification and quarantine routing[cite: 1]  
- suspicious or irreparable payloads are dispatched to `COLNIK-6.x/triage` for manual review via the Triage Panel[cite: 1]  

---

### **7 — AUTONOMY 6.x & PanelAPI-Supervised Repair Proposals**  
AUTONOMY‑6.x (Control, Guard, Safe Trash & Triage Mode) and interactive `PanelAPI` confirmation loops (`[ÁNO/NIE]` / `[YES/NO]`) with confirmation state latching govern high-impact recoveries[cite: 1]:  
- mass file rollbacks via `safe_rollback.py`[cite: 1]  
- primary Knowledge Graph rebuilds across `autosave_kg.json` or `autosave_kg_en.json`[cite: 1]  
- system configuration resets[cite: 1]  
- destructive replacement of user data[cite: 1]  

AUTONOMY assesses risk, and the user approves or denies via `PanelAPI`.

---

## 🧱 Repair Capabilities  

### **Automatic Repairs**  
- missing configuration files and baseline scripts[cite: 1]  
- corrupted JSON documents and schema mismatches[cite: 1]  
- `autosave_kg.json` and `autosave_kg_en.json` partition alignment and alias reconstruction[cite: 1]  
- native merge alias link repair (`kg merge`)[cite: 1]  
- quarantine sliding-window rotation (pruning files in excess of 100)[cite: 1]  
- trailing punctuation trimming (`.rstrip("?")`) and confirmation state latch restoration[cite: 1]  
- terminal focus reset (`currentModule = "none"`)[cite: 1]  
- workflow state machine rollback to safe checkpoints[cite: 1]  
- module re-initialization within `sirius_orchestrator.py`[cite: 1]  

### **Stabilization**  
- degraded-mode fallback isolation[cite: 1]  
- safe-mode restriction upon STRANGER detection[cite: 1]  
- non-destructive shadow writing[cite: 1]  
- quarantine containment in `COLNIK-6.x/triage`[cite: 1]  
- diversion of file deletions into HitL Safe Trash (tested in `dist_V6_CHECK`)[cite: 1]  
- crash resilience via SafeRollback (`safe_rollback.py`)[cite: 1]  
- cognitive fact validation via Professor Middleware[cite: 1]  

### **Explainability (XAI)**  
- `KG_EXPLAIN` direct recovery rationale[cite: 1]  
- `KG_EXPLAIN_DEEP` hierarchical proof trees detailing repair derivations[cite: 1]  
- repair audit logging with full timestamp, latency deltas (`cycle_delta()`), and provenance metadata[cite: 1]  

---

## 🔐 Safety Rules  
- ❌ No repair execution during critical host OS instability or power drop[cite: 1]  
- 🔄 Mandatory module backups via SafeRollback (`safe_rollback.py`) before structural repair mutations[cite: 1]  
- 🎓 Mandatory cognitive validation via Professor Middleware (`PASS / WARN / REJECT`)[cite: 1]  
- 🔒 Mandatory customs validation via COLNIK‑6.x (Standard & High-Performance IPC Mode)[cite: 1]  
- 🛡 Supervised recovery via AUTONOMY 6.x (Control, Guard, Safe Trash & Triage Mode)[cite: 1]  
- 💬 High-impact restorations mandate interactive user confirmation via `PanelAPI` `[ÁNO/NIE]` / `[YES/NO]`[cite: 1]  
- 🛑 Terminal deadlocks must unconditionally force `currentModule = "none"`[cite: 1]  
- ⛔ Destructive shell commands (`format`, `diskpart`) must remain hard-blocked in 0.0s[cite: 1]  
- 🗄️ Slovak and English knowledge graphs must remain strictly segregated during recovery[cite: 1]  
- 📦 Quarantine storage must be pruned to maintain the 100-file ceiling[cite: 1]  
- 🚫 Restored Knowledge Graph nodes must respect Non-Bio Domain Shielding[cite: 1]  
- 🔁 Reversible file operations enforced; direct unverified file deletions prohibited[cite: 1]  
- ⚠ Real-time hardware telemetry (CPU, RAM, Disk) continuously audited via Guard[cite: 1]  

---

## 📊 Module Status (v6.0.1)  
- ✔ Fully implemented & synchronized with Runtime 6.0.1 architecture[cite: 1]  
- ✔ Cryptographic hash scans and baseline restoration verified[cite: 1]  
- ✔ Dual-language KG stabilization active (`autosave_kg.json` & `autosave_kg_en.json`)[cite: 1]  
- ✔ Native `kg merge` alias healing verified[cite: 1]  
- ✔ Quarantine sliding-window ceiling (100 files) enforced[cite: 1]  
- ✔ COLNÍK Guard 0.0s command blocking integration active[cite: 1]  
- ✔ Human-in-the-Loop Safe UI Trash pipeline verified (tested in `dist_V6_CHECK`)[cite: 1]  
- ✔ SafeRollback crash protection (`safe_rollback.py`) integrated[cite: 1]  
- ✔ Professor Middleware Layer (`PASS / WARN / REJECT`) active[cite: 1]  
- ✔ Token Guard input hygiene & trailing punctuation stripping active[cite: 1]  
- ✔ Terminal decoupling and module release confirmed[cite: 1]  
- ✔ Single-process orchestrator integration on port 8080 operational with embedded TerminalAssistant + TimeCore[cite: 1]  
- ✔ Interactive PanelAPI confirmation loops with state latching functional[cite: 1]  
- ✔ TimeCore temporal tracking (`cycle_delta()`) and Guard telemetry supervision active[cite: 1]  
- ✔ COLNIK‑6.x Customs validation functional (Standard & IPC Mode)[cite: 1]  
- ✔ AUTONOMY 6.x governance and triage queue integration operational[cite: 1]  
- ✔ Explainability proof trees (`KG_EXPLAIN_DEEP`) verified[cite: 1]  

---

## 🏁 Summary  
Self‑Repair Layer is the autonomous stabilization and recovery core of SIRIUS Local AI (v6.0.1)[cite: 1].  
It detects file corruption, restores broken configurations, stabilizes dual-language graph partitions, heals native entity merge links, prunes sliding-window quarantine queues, resets decoupled terminal states, and recovers workflows — ensuring that every repair is safe, explainable, orchestrator-supervised, autonomy‑aware, and COLNIK‑validated[cite: 1].

It establishes SIRIUS as a **self‑healing, deterministic, offline-first intelligent runtime** engineered for continuous reliability, strict security isolation, and data integrity on local hardware[cite: 1].

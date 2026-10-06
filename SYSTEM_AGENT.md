# 🛡 SYSTEM AGENT 5 — Hardened OS‑Level Safety & Validation Core  
**Status:** ✔ Active (Enhanced)  
**Version:** 5.9.1 UNIFIED  
**Component:** System Agent  
**Role:** OS‑level safety, terminal decoupling, COLNÍK Guard command interception (0.0s hard blocks), HitL Safe Trash governance, Token Guard sanitization, identity enforcement, single-process orchestrator supervision, and customs-validated gating

---

## 🎯 Purpose  
System Agent 5 is the hardened OS‑level safety brain of SIRIUS Local AI (v5.9.1).  
It enforces identity access tiers, blocks unsafe system operations, validates natural language automation queries, intercepts destructive shell commands in 0.0s via COLNÍK Guard, routes file deletions safely to Human-in-the-Loop Safe Trash (`GET /trash`), monitors system context and hardware telemetry via Guard, profiles execution latency via TimeCore (`cycle_delta()`), enforces strict terminal input decoupling (`currentModule = "none"`), drops malformed symbolic inputs via Token Guard (`@#$%^&*`), and ensures that every host modification is safe, reversible, explainable, and approved through the single-process orchestrator (`sirius_orchestrator.py` on Port 8080 with embedded TerminalAssistant + TimeCore), interactive `PanelAPI` confirmation loops (`[ÁNO/NIE]` / `[YES/NO]`) with confirmation state latching, COLNIK‑6.x (Standard & High-Performance IPC Mode), and AUTONOMY‑6.x (Control, Guard, Safe Trash & Triage Mode).

System Agent 5 protects the local workstation from unsafe workflows, unauthorized system mutations, destructive disk commands, command injection from conversational queries, and compromised execution states.

---

## 🧩 Architecture Overview  
**System Intelligence Layer & Guard → Token Guard → sirius_orchestrator.py (Port 8080 with TerminalAssistant) → System Agent 5 → COLNÍK Guard (0.0s Block) → Terminal Decoupling Guard → COLNIK-6.x → AUTONOMY 6.x → PanelAPI [ÁNO/NIE] / [YES/NO] → HitL Safe Trash / Dual KG Commit (`autosave_kg.json` / `autosave_kg_en.json`) → EXECUTE 6.x**

### Core Responsibilities  
- enforce identity permissions across OWNER, FAMILY, and STRANGER profiles in constant time ($O(1)$)  
- enforce COLNÍK Guard shell security: 0.0s hard blocking of forbidden commands (`format`, `diskpart`, `rmdir /s`, `del /f /s /q c:`, `drop database`, fork-bombs)  
- govern Human-in-the-Loop Safe Trash: direct unverified disk deletions are blocked; file removals divert into quarantine awaiting manual approval via `GET /trash`  
- drop malformed or malicious symbolic inputs (`@#$%^&*`) immediately at runtime entry via Token Guard  
- enforce terminal state decoupling: resetting input clears context (`currentModule = "none"`), preventing conversational text from executing as host OS shell binaries  
- profile shell command latency via TimeCore `cycle_delta()` and ensure diacritics integrity via multi-stage decoding fallback (UTF-8 -> CP1250 -> CP852)  
- support confirmation state latching for interactive proposals across conversation turns  
- validate automation and file requests under single-process orchestrator supervision on port 8080  
- monitor system health and host load via `TimeCore` and `Guard` (CPU, RAM, Disk)  
- enforce the 100-file sliding-window quarantine ceiling in `COLNIK-6.x/envoy/quarantine/`  
- detect execution anomalies and quarantine suspicious payloads to `COLNIK-6.x/triage`  
- guarantee non-destructive, reversible action logic across all filesystem operations  
- compile deep explainability derivation traces (`KG_EXPLAIN` & `KG_EXPLAIN_DEEP`)  
- route decisions through COLNIK‑6.x (Standard, High-Performance IPC Mode & COLNÍK Guard)  
- coordinate autonomous proposal gating with human-in-the-loop verification (`PanelAPI` [ÁNO/NIE] / [YES/NO])  

### Key Files  
- `system_agent/system_agent.py`  
- `system_agent/identity_rules.json`  
- `system_agent/safety_log.json`  
- `system_agent/terminal_decoupling_guard.py`  
- `orchestrator/terminal_assistant.py`  
- `colnik_6_x/colnik_guard.py`  
- `runtime5/token_guard.py`  
- `filesystem/safe_trash_quarantine.py`  
- `ORCHESTRATOR/sirius_orchestrator.py`  
- `PANEL_API/panel_api.py`  
- `IPC_DATA/system_agent_events.json`  
- `COLNIK-6.x/triage/`  

---

## 🔍 Safety & Validation Pipeline (v5.9.1)  

### **1 — Token Guard Sanitization & Identity Validation**  
Before query ingestion starts in `sirius_orchestrator.py`:  
- audits raw input against **Token Guard**: immediately drops payloads containing forbidden characters (`@`, `#`, `$`, `%`, `^`, `&`, `*`)  
- evaluates identity profile in constant time ($O(1)$) across OWNER, FAMILY, and STRANGER access tiers  
- STRANGER mode: zero-trust sandbox; immediate UI lockout and terminal detachment (`currentModule = "none"`)  
- SCHOOLWORK bypass: guaranteed zero-latency execution for academic research  
- ENVOY 5 outbound permission models bound to language partitions (`SK` / `EN`)  

If identity or token validation fails, the action is halted immediately.

---

### **2 — COLNÍK Guard Shell Interception (0.0s Hard Block)**  
When terminal or shell commands are invoked:  
- **FORBIDDEN (0.0s Hard Block):** `format`, `rmdir /s`, `del /f /s /q c:`, `diskpart`, `drop database`, fork-bombs  
- **RISKY (Explicit Prompt):** `rm`, `kill`, `taskkill`, `del`  
- **ALLOWED:** `ps`, `top`, `mem`, `sys`, `grep`, `info`, `cat`, `head`, `tail`, `check`, `template`, `python`, `git`, `pip`, `ls`, `dir`, `cd`, `pwd`, `mkdir`, `touch`, `help`  
- profiles execution latency via TimeCore `cycle_delta()` and applies multi-stage character decoding fallback (UTF-8 -> CP1250 -> CP852)  

---

### **3 — Human-in-the-Loop Safe UI Trash Governance**  
Protects host storage against accidental or unverified file loss:  
- operations proposing file deletion (duplicates, empty folders, damaged files) are intercepted  
- direct permanent unlinking from disk is blocked  
- files are moved to quarantine storage awaiting explicit manual review via `GET /trash`  

---

### **4 — Terminal Decoupling & Host Shell Isolation**  
System Agent intercepts all web console and CLI inputs:  
- clearing an input field, escaping a dialog, or concluding a query forces `currentModule = "none"`  
- isolates natural language conversational inputs from host OS shell command processors (PowerShell, CMD, Bash)  
- prevents command injection and unhandled terminal focus locks  

---

### **5 — Hardware Telemetry & System‑Context Awareness**  
System Agent queries the System Intelligence Layer, `TimeCore`, and `Guard`:  
- host OS resource metrics: CPU, RAM, and Disk monitoring with less than 1% overhead  
- command latency profiling via TimeCore `cycle_delta()`  
- execution loop anomaly detection and memory spike mitigation  
- active disk write status to prevent race conditions during Knowledge Graph atomic serialization across `autosave_kg.json` and `autosave_kg_en.json`  
- repair-aware context for Self-Repair Layer 5.8  

Workflows are paused or throttled if host system stability is compromised.

---

### **6 — Threat Detection, Sliding Quarantines & Domain Shielding**  
System Agent blocks:  
- unauthorized host configuration changes and file tampering  
- 0.0s hard blocking of disk formatting and destruction routines via COLNÍK Guard  
- privilege escalation and shell breakout attempts  
- terminal shell capture from unparsed natural language queries  
- unverified UI automation routines  
- persistent hooks, background daemons, or unverified binary spawns  
- cross-domain attribute pollution violating the Non-Bio Domain Shield  
- automatic sliding-window quarantine maintenance: prunes logs in `COLNIK-6.x/envoy/quarantine/` to strictly maintain a 100-file ceiling  

Every blocked or quarantined action generates explainability metadata and logs to `COLNIK-6.x/triage`.

---

### **7 — COLNIK‑6.x Customs Clearance (Standard & IPC Mode)**  
All allow/deny decisions clear the Kýklos decision gate:  
- enterprise-grade ALLOW / DENY / TRIAGE decision matrix  
- deterministic memory-mapped IPC routing  
- reversible action validation  
- cryptographic payload inspection  
- structured customs audit logging  

System Agent never permits transitions without COLNIK customs clearance.

---

### **8 — AUTONOMY 6.x & Confirmation State Latching (Zero Recurrence)**  
AUTONOMY‑6.x (Control, Guard, Safe Trash & Triage Mode) and interactive `PanelAPI` receive proposals for:  
- novel entity learning proposals (`kg.learn_proposal`) bound to active language stores (`SK` / `EN`)  
- native entity merges (`kg merge <src> into <tgt>`)  
- sensitive or high-risk OS-level operations  
- file reorganization or cleanup tasks  
- identity-restricted transitions  

Human confirmation is obtained via `PanelAPI` (`[ÁNO/NIE]` / `[YES/NO]`). Confirmation state latching preserves pending proposal targets across turns. Once confirmed, mappings commit to `autosave_kg.json` or `autosave_kg_en.json` with Zero Proposal Recurrence.

---

### **9 — Reversible Actions & Non-Destructive Operations**  
System Agent enforces strict reversibility:  
- duplicate file scans enforce a mandatory `REPORT_ONLY` policy; proposed deletions route into HitL Safe Trash  
- configuration modifications create shadow baseline snapshots  
- atomic rollback mechanisms for interrupted transactions  
- repair-aware state recovery  

No destructive action is executed without rollback guarantees.

---

## 🧱 Protection Layers  

### **Identity & Access Layer**  
- constant-time ($O(1)$) identity classification  
- OWNER / FAMILY / STRANGER access tiers  
- guaranteed SCHOOLWORK educational bypass  
- outbound ENVOY permission verification bound to language endpoints  

### **Input Hygiene & Command Security Layer**  
- Token Guard input filter dropping `@#$%^&*`  
- trailing punctuation stripping (`.rstrip("?")`) preserving pure entity identifiers  
- COLNÍK Guard 0.0s hard blocking of forbidden shell routines  
- Human-in-the-Loop Safe UI Trash quarantine pipeline (`GET /trash`)  

### **Terminal & Execution Isolation Layer**  
- single-process daemon isolation on port 8080 with embedded TerminalAssistant + TimeCore  
- automatic module state release (`currentModule = "none"`) on input clear  
- complete separation between conversational parsing and OS shell binaries  

### **Customs & Threat Mitigation Layer**  
- primitive decision gate: ALLOW / DENY / TRIAGE  
- blocks unverified automation and privilege escalation  
- Non-Bio Domain Shield blocking false biological attributes on technical concepts  
- sliding-window quarantine rotation enforcing a 100-file ceiling  
- real-time quarantine dispatch to `COLNIK-6.x/triage`  

### **Explainability Layer (XAI)**  
- `KG_EXPLAIN` direct relation and property justification  
- `KG_EXPLAIN_DEEP` hierarchical proof trees (ASCII + HTML)  
- threat attribution and permission rationale  
- autonomy proposal provenance logging  

### **Orchestrator & Autonomy Layer**  
- single-process execution via `sirius_orchestrator.py`  
- interactive human gating via `PanelAPI` (`[ÁNO/NIE]` / `[YES/NO]`) with confirmation state latching  
- zero proposal recurrence on confirmed knowledge and deduced taxonomies  
- real-time hardware telemetry via Guard and TimeCore `cycle_delta()`  

---

## 🔐 Safety Rules  
- ❌ No execution of forbidden host OS shell commands (0.0s block via COLNÍK Guard)  
- ⛔ Immediate Token Guard rejection on inputs containing malformed symbols (`@#$%^&*`)  
- 🗑️ No direct unverified disk deletions: file removals must route through HitL Safe Trash (`GET /trash`)  
- 🔒 Constant-time identity validation mandatory for all actions  
- 🛑 Terminal state decoupling must enforce `currentModule = "none"` upon input reset  
- 🛡 COLNIK-6.x customs clearance (Standard, High-Performance IPC Mode & COLNÍK Guard) required  
- 🛡 AUTONOMY 6.x governance required for novel concept acquisition and entity merges  
- 💬 Interactive `PanelAPI` `[ÁNO/NIE]` / `[YES/NO]` gating active for sensitive OS and KG mutations  
- 📦 Automatic quarantine sliding-window rotation enforcing 100-file ceiling  
- 🚫 Strict non-biological domain shields active across all data ingestion  
- 🔁 Reversible actions enforced; duplicate files strictly restricted to `REPORT_ONLY`  
- ⚠ Deep explainability proof trees mandatory for all allowed and denied operations  
- 📉 Real-time hardware telemetry (CPU, RAM, Disk) continually monitored via Guard  

---

## 📊 Module Status (v5.9.1)  
- ✔ Fully implemented & synchronized with Runtime 5.9.1 architecture  
- ✔ Identity access tiers verified (OWNER / FAMILY / STRANGER)  
- ✔ Token Guard input sanitization active  
- ✔ COLNÍK Guard 0.0s command blocking integration operational  
- ✔ Human-in-the-Loop Safe UI Trash pipeline verified  
- ✔ Sliding-window quarantine rotation (100-file ceiling) active  
- ✔ Multi-stage character decoding fallback active (UTF-8 -> CP1250 -> CP852)  
- ✔ Terminal input decoupling and state release confirmed  
- ✔ Single-process orchestrator integration on port 8080 operational with embedded TerminalAssistant + TimeCore  
- ✔ PanelAPI interactive confirmation loops with confirmation state latching functional  
- ✔ TimeCore latency profiling (`cycle_delta()`) and Guard hardware telemetry active  
- ✔ COLNIK‑6.x Customs validation functional (Standard & IPC Mode)  
- ✔ AUTONOMY 6.x governance and quarantine containment verified  
- ✔ Deep explainability proof trees operational  
- ✔ Reversible filesystem actions and `REPORT_ONLY` policies verified  
- ✔ Dual-language graph persistence synchronized (`autosave_kg.json` & `autosave_kg_en.json`)  

---

## 🏁 Summary  
System Agent 5 is the hardened OS‑level safety core of SIRIUS Local AI (v5.9.1).  
It enforces identity rules, intercepts destructive shell commands in 0.0s via COLNÍK Guard, routes file removals into Human-in-the-Loop Safe Trash, decouples terminal inputs to prevent host shell capture, drops malformed symbolic inputs via Token Guard, monitors host hardware telemetry, and ensures that every action is safe, reversible, explainable, single-process orchestrated, autonomy‑supervised, and customs-validated.

It functions as the workstation's **central safety brain**, protecting SIRIUS from unauthorized operations, unverified disk destruction, and dangerous routines, ensuring deterministic, intelligent, and secure OS‑level execution.

# 🎛 UI AUTOMATION ENGINE 5.1 — Deterministic, Explainable, Orchestrator-Supervised, Terminal-Decoupled, COLNÍK Guard Hardened & Safe Trash Governed OS Automation  
**Status:** ✔ Active (Enhanced)  
**Version:** 5.1 (Updated for 5.9.1 UNIFIED)  
**Component:** UI Automation Engine & 4-Panel UI Suite Integration  
**Role:** Safe, deterministic, explainable, single-process orchestrated, terminal-decoupled, COLNÍK Guard validated, HitL Safe Trash integrated, and autonomy‑supervised automation of Windows 11 UI and local browser suite  

---

## 🎯 Purpose  
UI Automation Engine 5.1 is responsible for executing deterministic, safe, explainable UI actions across Windows 11 and managing interactive operations inside the local 4-Panel UI Suite (Duplicates, Triage, Navigation, Terminal) on port 8080.  
It integrates identity validation, Token Guard entry sanitization (@#$%^&*), trailing punctuation hygiene (.rstrip("?")), confirmation state latching across turns, multi-word compound noun target resolution (InputParser5), single-process central orchestration (sirius_orchestrator.py on Port 8080 with embedded TerminalAssistant + TimeCore), interactive PanelAPI confirmation loops ([ÁNO/NIE] / [YES/NO]), real-time hardware telemetry and latency profiling via TimeCore (cycle_delta()) and Guard (CPU, RAM, Disk), COLNÍK Guard command interception (0.0s hard blocks on destructive commands like format and diskpart), Human-in-the-Loop Safe UI Trash review (GET /trash), sliding-window quarantine maintenance (100-file ceiling in COLNIK-6.x/envoy/quarantine/), COLNIK‑6.x (Standard & High-Performance IPC Mode) customs safety, AUTONOMY‑6.x (Control, Guard, Safe Trash & Triage Mode) supervised gating, and Terminal Decoupling Guards (currentModule = "none").  

This engine allows SIRIUS to operate Windows 11 **precisely, safely, intelligently, without host shell capture or destructive routines, and 100% offline**.  

---

## 🧩 Architecture Overview  
Workflow Engine 5.9.1 → Token Guard → InputParser5 (.rstrip("?")) → sirius_orchestrator.py (Port 8080 with TerminalAssistant + TimeCore) → UI Automation Engine 5.1 → COLNÍK Guard (0.0s Block) → System Agent 5 → Terminal Decoupling Guard → COLNIK-6.x → AUTONOMY 6.x → PanelAPI [ÁNO/NIE] / [YES/NO] → HitL Safe Trash / Dual KG Commit (autosave_kg.json / autosave_kg_en.json) → EXECUTE 6.x  

### Core Responsibilities  
- perform deterministic UI actions managed centrally by sirius_orchestrator.py on local port 8080 with embedded TerminalAssistant + TimeCore  
- resolve UI targets semantically across dual-language environments, preserving complete compound noun phrases without modifier truncation  
- strip trailing punctuation (.rstrip("?")) from UI search queries to prevent node target mismatch  
- enforce confirmation state latching across turns for interactive UI action prompts  
- enforce COLNÍK Guard shell filtering in terminal automation: 0.0s hard blocking of forbidden commands (format, diskpart, rmdir /s, del /f /s /q c:, drop database)  
- integrate Human-in-the-Loop Safe Trash for UI file management: block direct file deletion and route removals into quarantine for review via GET /trash  
- drop malformed injection tokens (@#$%^&*) at entry via Token Guard  
- enforce terminal input decoupling: clear events immediately assert currentModule = "none", preventing conversational UI queries from executing as host OS shell binaries  
- prevent mis‑clicks, coordinate drift, and unverified UI sequence execution  
- validate identity profiles across OWNER, FAMILY, and STRANGER tiers in constant time (O(1))  
- enforce guaranteed SCHOOLWORK academic bypass for educational interface interactions  
- compile deep explainability derivation traces (KG_EXPLAIN & KG_EXPLAIN_DEEP) in ASCII and HTML  
- route automation actions through COLNIK‑6.x customs inspection (Standard, High-Performance IPC Mode & COLNÍK Guard)  
- dispatch high-risk or ambiguous UI actions into COLNIK-6.x/triage for review in the Triage Panel  
- coordinate autonomous proposal loops with zero recurrence for established Knowledge Graph aliases and deduced taxonomies  

### Key Files  
- ui_automation/ui_engine.py  
- ui_automation/ui_targets.json  
- ui_automation/ui_fallback.json  
- ui_automation/terminal_decoupling_guard.py  
- orchestrator/terminal_assistant.py  
- colnik_6_x/colnik_guard.py  
- runtime5/token_guard.py  
- filesystem/safe_trash_quarantine.py  
- runtime5/envoy_quarantine_5.py  
- ORCHESTRATOR/sirius_orchestrator.py  
- PANEL_API/panel_api.py  
- IPC_DATA/ui_actions.json  
- COLNIK-6.x/triage/  

---

## 🔍 Automation & Decoupling Pipeline (v5.9.1)  

### 1 — Token Guard Sanitization, Semantic Target Resolution & Compound Parsing  
UI Automation Engine resolves UI elements and action targets using:  
- Token Guard raw input filtering dropping @#$%^&* before action ingestion  
- Win32 API, UI Automation (UIA), and Windows Runtime (WinRT) wrappers  
- semantic Knowledge Graph metadata bound to the active language store (autosave_kg.json for SK, autosave_kg_en.json for EN)  
- compound phrase preservation via InputParser5 (matching full control names like správca úloh or task manager)  
- greedy trailing punctuation stripping (.rstrip("?"))  
- deterministic fuzzy matching with diacritic normalization (UTF-8 -> CP1250 -> CP852 pipeline)  
- identity‑aware target filtering  

All UI targets are validated for focus and bounding-box existence before dispatch.  

---

### 2 — COLNÍK Guard Shell Interception & Latency Tracking  
When terminal UI inputs invoke CLI or shell automation:  
- FORBIDDEN (0.0s Hard Block): format, rmdir /s, del /f /s /q c:, diskpart, drop database, fork-bombs  
- RISKY (Explicit Prompt): rm, kill, taskkill, del  
- ALLOWED: ps, top, mem, sys, grep, info, cat, head, tail, check, template, python, git, pip, ls, dir, cd, pwd, mkdir, touch, help  
- execution latency is tracked and recorded via TimeCore cycle_delta()  

---

### 3 — Human-in-the-Loop Safe UI Trash Disposal  
In Duplicates Panel and file explorer automation:  
- proposed file removals (duplicates, temporary archives, empty folders) bypass unverified disk deletion  
- files route to /filesystem/safe_trash_quarantine awaiting user inspection and manual purge authorization via GET /trash  
- REPORT_ONLY baseline enforced on automated audits  

---

### 4 — Terminal State Decoupling & Host Shell Isolation  
To ensure that conversational queries in the browser console never capture the operating system shell:  
- clearing an input field or canceling an interaction immediately triggers an event setting currentModule = "none"  
- terminal keystrokes and conversational natural language are strictly isolated from host command interpreters (CMD, PowerShell, Bash)  
- prevents command injection and UI state lockups across all active panels  

---

### 5 — Identity‑Aware Gating & Academic Priority  
Before automation begins, the engine evaluates caller authorization:  
- OWNER mode: full UI automation and administrative control  
- FAMILY mode: restricted to safe application navigation and household tools; administrative dialogs and raw shell executions blocked  
- STRANGER mode: zero-trust lockdown; immediate UI detachment and module context reset  
- SCHOOLWORK bypass: educational applications, document viewers, and research tools operate with zero restriction latency  
- ENVOY 5 outbound retrieval permission enforcement  

Unsafe identity contexts immediately abort automation.  

---

### 6 — System‑Context & Telemetry Evaluation  
The engine queries the System Intelligence Layer, TimeCore, and Guard:  
- host OS health: real-time CPU, RAM, and Disk metrics (< 1% polling load)  
- latency profiling via TimeCore cycle_delta()  
- sliding-window quarantine maintenance: verifying COLNIK-6.x/envoy/quarantine/ remains within 100-file ceiling  
- window focus anomalies and runaway event loops  
- risky UI states (unresponsive windows, modal dialog deadlocks)  
- repair‑aware context: UI automation is disabled during Self-Repair baseline restorations  

Automation is paused, throttled, or rejected during unstable host states.  

---

### 7 — KG‑Enhanced Explainability (Proof Trees)  
Every UI interaction compiles an auditable trace:  
- KG_EXPLAIN direct UI target and intent justification  
- KG_EXPLAIN_DEEP hierarchical proof trees showing rule attribution and path derivation  
- semantic rationale for control selection  
- confidence metrics relative to UI element hierarchy  

Explainability is mandatory for all automation requests.  

---

### 8 — COLNIK‑6.x Customs Clearance (Standard & IPC Mode)  
All UI actions clear the Kýklos decision gate:  
- enterprise-grade ALLOW / DENY / TRIAGE decision matrix  
- deterministic memory-mapped IPC routing  
- reversible action validation (non-destructive UI sequences)  
- threat classification and injection checks  
- ambiguous or unverified UI actions route directly into COLNIK-6.x/triage  

System Agent 5 strictly enforces COLNIK verdicts before touching OS window handles.  

---

### 9 — AUTONOMY 6.x & Confirmation State Latching  
AUTONOMY‑6.x (Control, Guard, Safe Trash & Triage Mode) and interactive PanelAPI ([ÁNO/NIE] / [YES/NO]) receive proposals for:  
- high-impact or administrative UI sequences  
- entity consolidation merges (kg merge)  
- identity‑restricted control operations  
- system‑context‑sensitive automation  
- multi‑step application workflows  

Human confirmation is obtained via PanelAPI ([ÁNO/NIE] / [YES/NO]) with active confirmation state latching across turns. Once confirmed, recurring sequences resolve from memory without redundant prompts.  

---

### 10 — Deterministic Execution & Fallback  
Once validated, UI actions execute under strict controls:  
- mis‑click prevention 3.2 (coordinate boundary confirmation)  
- safe fallback logic: if UIA fails, fallback to Win32 semantic handles  
- sandbox‑protected execution environment  
- reversible action guarantees with shadow baseline snapshots  

---

## 🧱 Capabilities  

### Deterministic UI Automation  
- click, double-click, and contextual right-click  
- text input and secure typing (passwords masked from telemetry)  
- focus navigation and keyboard traversal  
- window state management (open, close, minimize, restore)  
- control state verification (toggles, sliders, dropdown lists)  
- multi‑step workflows managed under single-process orchestrator control  

### Semantic Targeting & Decoupling  
- KG‑enhanced target resolution across isolated dual-language stores (autosave_kg.json & autosave_kg_en.json)  
- compound phrase preservation via InputParser5  
- greedy trailing punctuation stripping (.rstrip("?"))  
- confirmation state latching across turns  
- terminal decoupling controller resetting currentModule = "none"  
- fuzzy matching with typo and diacritic tolerance (UTF-8 -> CP1250 -> CP852)  

### 4-Panel UI Suite Integration (Port 8080)  
- Duplicates Panel: non-destructive reporting (REPORT_ONLY) with Safe Trash disposal  
- Triage Panel: interactive inspection and clearance of COLNIK-6.x/triage  
- Navigation Panel: deterministic module switching  
- Terminal Panel: host-isolated conversational command console with COLNÍK Guard (0.0s hard block)  

### Explainability & Safety (XAI)  
- KG_EXPLAIN and KG_EXPLAIN_DEEP hierarchical proof trees  
- System Agent 5 threat blocking and constant-time identity checks  
- COLNIK-6.x customs clearance logs  
- reversible action enforcement via HitL Safe Trash  

---

## 🔐 Safety Rules  
- ❌ No UI automation during degraded host OS states or high resource pressure (> 1% telemetry anomaly)  
- ⛔ Destructive shell commands (format, diskpart, rmdir /s) must halt in 0.0s via COLNÍK Guard  
- 🗑️ Direct permanent file deletions are strictly prohibited; removals must route to HitL Safe Trash (GET /trash)  
- 🛑 Terminal state decoupling must assert currentModule = "none" upon input reset  
- 📦 Quarantine storage must respect the 100-file ceiling via automated sliding-window pruning  
- 🔒 Identity validation mandatory; STRANGER mode forces immediate UI detachment  
- 🛡 COLNIK-6.x customs clearance (ALLOW / DENY / TRIAGE) required prior to execution  
- 🛡 AUTONOMY 6.x confirmation required for novel multi-step sequences  
- 💬 Interactive PanelAPI [ÁNO/NIE] / [YES/NO] gating active for high-risk UI operations with confirmation state latching  
- 🚫 Conversational text must never be piped into host OS shell environments  
- 🔁 Reversible actions enforced; duplicate file operations default to REPORT_ONLY  
- ⚠ Hierarchical proof-tree explainability required for all actions  
- 📉 Mis‑click prevention and coordinate verification continuously active  

---

## 📊 Module Status (v5.9.1)  
- ✔ Fully implemented & synchronized with Runtime 5.9.1  
- ✔ Semantic compound target resolution operational (InputParser5)  
- ✔ Token Guard input sanitization active (@#$%^&* drop)  
- ✔ Trailing punctuation trimming (.rstrip("?")) and confirmation state latching active  
- ✔ COLNÍK Guard 0.0s command blocking integration verified  
- ✔ Human-in-the-Loop Safe UI Trash pipeline verified  
- ✔ Sliding-window quarantine rotation (100-file ceiling) operational  
- ✔ Terminal decoupling controller active (currentModule = "none")  
- ✔ Single-process orchestrator integration on port 8080 operational with embedded TerminalAssistant + TimeCore  
- ✔ PanelAPI interactive confirmation loops verified  
- ✔ TimeCore latency profiling (cycle_delta()) and Guard hardware telemetry active  
- ✔ COLNIK‑6.x Customs validation functional (Standard, High-Performance IPC Mode & COLNÍK Guard)  
- ✔ AUTONOMY 6.x governance and triage routing verified (COLNIK-6.x/triage)  
- ✔ 4-Panel UI Suite browser synchronization active  
- ✔ Hierarchical proof-tree explainability functional (KG_EXPLAIN_DEEP)  
- ✔ Reversible UI action logic and sandbox protection verified  

---

## 🏁 Summary  
UI Automation Engine 5.1 is the deterministic, explainable, single-process orchestrated, terminal-decoupled, COLNÍK Guard protected, and autonomy‑supervised automation core of SIRIUS Local AI (v5.9.1).  
It executes safe, validated, reversible UI actions across Windows 11 and the 4-Panel UI Suite using compound semantic parsing, Token Guard sanitization, confirmation state latching, identity enforcement, host hardware telemetry, TimeCore latency profiling, Human-in-the-Loop Safe Trash disposal, central orchestrator control, and enterprise customs-grade COLNIK validation.  

It enables SIRIUS to operate Windows 11 **intelligently, safely, predictively, without terminal command leakage or destructive routines, and 100% offline**.

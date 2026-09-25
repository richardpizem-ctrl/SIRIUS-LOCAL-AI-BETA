# 🎛 UI AUTOMATION ENGINE 5.1 — Deterministic, Explainable, Orchestrator-Supervised, Terminal-Decoupled & COLNIK‑Validated OS Automation  
**Status:** ✔ Active (Enhanced)  
**Version:** 5.1 (Updated for 5.9.0 UNIFIED)  
**Component:** UI Automation Engine & 4-Panel UI Suite Integration  
**Role:** Safe, deterministic, explainable, single-process orchestrated, terminal-decoupled, autonomy‑supervised automation of Windows 11 UI and local browser suite  

---

## 🎯 Purpose  
UI Automation Engine 5.1 is responsible for executing deterministic, safe, explainable UI actions across Windows 11 and managing interactive operations inside the local 4-Panel UI Suite (`Duplicates`, `Triage`, `Navigation`, `Terminal`) on port 8080.  
It integrates identity validation, multi-word compound noun target resolution (`InputParser5`), single-process central orchestration (`sirius_orchestrator.py` on Port 8080), interactive `PanelAPI` confirmation loops (`[ÁNO/NIE]`), real-time hardware telemetry and supervision via `TimeCore` and `Guard` (CPU, RAM, Disk), COLNIK‑6.x (Standard & High-Performance IPC Mode) customs safety, AUTONOMY‑6.x (Control, Guard & Triage Mode) supervised gating, and Terminal Decoupling Guards (`currentModule = "none"`).  

This engine allows SIRIUS to operate Windows 11 **precisely, safely, intelligently, without host shell capture, and 100% offline**.  

---

## 🧩 Architecture Overview  
**Workflow Engine 5.9.0 → InputParser5 → sirius_orchestrator.py (Port 8080) → UI Automation Engine 5.1 → System Agent 5 → Terminal Decoupling Guard → COLNIK-6.x → AUTONOMY 6.x → PanelAPI [ÁNO/NIE] → EXECUTE 6.x**  

### Core Responsibilities  
- perform deterministic UI actions managed centrally by `sirius_orchestrator.py` on local port 8080  
- resolve UI targets semantically, preserving complete compound noun phrases without modifier truncation  
- enforce terminal input decoupling: clear events immediately assert `currentModule = "none"`, preventing conversational UI queries from executing as host OS shell binaries  
- prevent mis‑clicks, coordinate drift, and unverified UI sequence execution  
- validate identity profiles across OWNER, FAMILY, and STRANGER tiers in constant time ($O(1)$)  
- enforce guaranteed SCHOOLWORK academic bypass for educational interface interactions  
- compile deep explainability derivation traces (`KG_EXPLAIN` & `KG_EXPLAIN_DEEP`) in ASCII and HTML  
- route automation actions through COLNIK‑6.x customs inspection (Standard & High-Performance IPC Mode)  
- dispatch high-risk or ambiguous UI actions into `COLNIK-6.x/triage` for review in the Triage Panel  
- coordinate autonomous proposal loops with zero recurrence for established Knowledge Graph aliases  

### Key Files  
- `ui_automation/ui_engine.py`  
- `ui_automation/ui_targets.json`  
- `ui_automation/ui_fallback.json`  
- `ui_automation/terminal_decoupling_guard.py`  
- `ORCHESTRATOR/sirius_orchestrator.py`  
- `PANEL_API/panel_api.py`  
- `IPC_DATA/ui_actions.json`  
- `COLNIK-6.x/triage/`  

---

## 🔍 Automation & Decoupling Pipeline (v5.9.0)  

### **1 — Semantic Target Resolution & Compound Parsing**  
UI Automation Engine resolves UI elements and action targets using:  
- Win32 API  
- UI Automation (UIA)  
- Windows Runtime (WinRT)  
- semantic Knowledge Graph metadata (`autosave_kg.json`)  
- compound phrase preservation via `InputParser5` (e.g., matching full control names like `správca úloh` or `nastavenie siete`)  
- deterministic fuzzy matching 5.8 with diacritic normalization  
- identity‑aware target filtering  

All UI targets are validated for focus and bounding-box existence before dispatch.  

---

### **2 — Terminal State Decoupling & Host Shell Isolation**  
To ensure that conversational queries in the browser console never capture the operating system shell:  
- clearing an input field or canceling an interaction immediately triggers an event setting `currentModule = "none"`  
- terminal keystrokes and conversational natural language are strictly isolated from host command interpreters (CMD, PowerShell, Bash)  
- prevents command injection and UI state lockups across all active panels  

---

### **3 — Identity‑Aware Gating & Academic Priority**  
Before automation begins, the engine evaluates caller authorization:  
- OWNER mode: full UI automation and administrative control  
- FAMILY mode: restricted to safe application navigation and household tools; administrative dialogs blocked  
- STRANGER mode: zero-trust lockdown; immediate UI detachment and module context reset  
- SCHOOLWORK bypass: educational applications, document viewers, and research tools operate with zero restriction latency  
- ENVOY 5 outbound retrieval permission enforcement  

Unsafe identity contexts immediately abort automation.  

---

### **4 — System‑Context & Telemetry Evaluation**  
The engine queries the System Intelligence Layer and `Guard`:  
- host OS health: real-time CPU, RAM, and Disk metrics (< 1% polling load)  
- window focus anomalies and runaway event loops  
- risky UI states (unresponsive windows, modal dialog deadlocks)  
- repair‑aware context: UI automation is disabled during Self-Repair baseline restorations  

Automation is paused, throttled, or rejected during unstable host states.  

---

### **5 — KG‑Enhanced Explainability (Proof Trees)**  
Every UI interaction compiles an auditable trace:  
- `KG_EXPLAIN` direct UI target and intent justification  
- `KG_EXPLAIN_DEEP` hierarchical proof trees showing rule attribution and path derivation  
- semantic rationale for control selection  
- confidence metrics relative to UI element hierarchy  

Explainability is mandatory for all automation requests.  

---

### **6 — COLNIK‑6.x Customs Clearance (Standard & IPC Mode)**  
All UI actions clear the Kýklos decision gate:  
- enterprise-grade ALLOW / DENY / TRIAGE decision matrix  
- deterministic memory-mapped IPC routing  
- reversible action validation (non-destructive UI sequences)  
- threat classification and injection checks  
- ambiguous or unverified UI actions route directly into `COLNIK-6.x/triage`  

System Agent 5 strictly enforces COLNIK verdicts before touching OS window handles.  

---

### **7 — AUTONOMY 6.x & PanelAPI-Aware Proposals**  
AUTONOMY‑6.x (Control, Guard & Triage Mode) and interactive `PanelAPI` (`[ÁNO/NIE]`) receive proposals for:  
- high-impact or administrative UI sequences  
- identity‑restricted control operations  
- system‑context‑sensitive automation  
- multi‑step application workflows  

Human confirmation is obtained via `PanelAPI` (`[ÁNO/NIE]`). Once confirmed, recurring sequences resolve from memory without redundant prompts.  

---

### **8 — Deterministic Execution & Fallback**  
Once validated, UI actions execute under strict controls:  
- mis‑click prevention 3.2 (coordinate boundary confirmation)  
- safe fallback logic: if UIA fails, fallback to Win32 semantic handles  
- sandbox‑protected execution environment  
- reversible action guarantees with shadow baseline snapshots  

---

## 🧱 Capabilities  

### **Deterministic UI Automation**  
- click, double-click, and contextual right-click  
- text input and secure typing (passwords masked from telemetry)  
- focus navigation and keyboard traversal  
- window state management (open, close, minimize, restore)  
- control state verification (toggles, sliders, dropdown lists)  
- multi‑step workflows managed under single-process orchestrator control  

### **Semantic Targeting & Decoupling**  
- KG‑enhanced target resolution (`autosave_kg.json`)  
- compound phrase preservation via `InputParser5`  
- terminal decoupling controller resetting `currentModule = "none"`  
- fuzzy matching 5.8 with typo and diacritic tolerance  

### **4-Panel UI Suite Integration (Port 8080)**  
- Duplicates Panel: non-destructive reporting (`REPORT_ONLY`)  
- Triage Panel: interactive inspection and clearance of `COLNIK-6.x/triage`  
- Navigation Panel: deterministic module switching  
- Terminal Panel: host-isolated conversational command console  

### **Explainability & Safety (XAI)**  
- `KG_EXPLAIN` and `KG_EXPLAIN_DEEP` hierarchical proof trees  
- System Agent 5 threat blocking and constant-time identity checks  
- COLNIK-6.x customs clearance logs  
- reversible action enforcement  

---

## 🔐 Safety Rules  
- ❌ No UI automation during degraded host OS states or high resource pressure (> 1% telemetry anomaly)  
- 🛑 Terminal state decoupling must assert `currentModule = "none"` upon input reset  
- 🔒 Identity validation mandatory; STRANGER mode forces immediate UI detachment  
- 🛡 COLNIK-6.x customs clearance (ALLOW / DENY / TRIAGE) required prior to execution  
- 🛡 AUTONOMY 6.x confirmation required for novel multi-step sequences  
- 💬 Interactive `PanelAPI` `[ÁNO/NIE]` gating active for high-risk UI operations  
- 🚫 Conversational text must never be piped into host OS shell environments  
- 🔁 Reversible actions enforced; destructive file operations default to `REPORT_ONLY`  
- ⚠ Hierarchical proof-tree explainability required for all actions  
- 📉 Mis‑click prevention and coordinate verification continuously active  

---

## 📊 Module Status (v5.9.0)  
- ✔ Fully implemented & synchronized with Runtime 5.9.0  
- ✔ Semantic compound target resolution operational (`InputParser5`)  
- ✔ Terminal decoupling controller active (`currentModule = "none"`)  
- ✔ Single-process orchestrator integration on port 8080 operational  
- ✔ PanelAPI interactive confirmation loops verified  
- ✔ TimeCore temporal bounds and Guard hardware telemetry active  
- ✔ COLNIK‑6.x Customs validation functional (Standard & High-Performance IPC Mode)  
- ✔ AUTONOMY 6.x governance and triage routing verified (`COLNIK-6.x/triage`)  
- ✔ 4-Panel UI Suite browser synchronization active  
- ✔ Hierarchical proof-tree explainability functional (`KG_EXPLAIN_DEEP`)  
- ✔ Reversible UI action logic and sandbox protection verified  

---

## 🏁 Summary  
UI Automation Engine 5.1 is the deterministic, explainable, single-process orchestrated, terminal-decoupled, and autonomy‑supervised automation core of SIRIUS Local AI (v5.9.0).  
It executes safe, validated, reversible UI actions across Windows 11 and the 4-Panel UI Suite using compound semantic parsing, identity enforcement, host hardware telemetry, central orchestrator control, and enterprise customs-grade COLNIK validation.  

It enables SIRIUS to operate Windows 11 **intelligently, safely, predictively, without terminal command leakage, and 100% offline**.

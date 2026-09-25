# 🎛 UI PANEL 6.x — 4-Panel Futuristic Neon Web Suite (Port 8080)
**Status:** ✔ Active & Stabilized  
**Version:** 6.x (Stabilized for 5.9.0 UNIFIED)  
**SIRIUS Local AI Version:** 5.9.0 UNIFIED  
**Component:** 4-Panel UI Suite & Terminal Decoupling Controller  
**Role:** Unified browser-based interface running natively on local port 8080 under single-process orchestrator supervision with automated terminal state decoupling (`currentModule = "none"`)

---

## 🎯 Purpose  
UI PANEL 6.x is a modern web interface with a futuristic neon aesthetic, serving as the primary interaction and control layer for the **SIRIUS Local AI v5.9.0** runtime.  
It runs natively as a single-process daemon directly through `sirius_orchestrator.py` on local port **8080**, permanently eliminating socket collisions and disk-level file locking contention.

The interface implements a fully decoupled architecture across four specialized panels (**Duplicates**, **Triage**, **Navigation**, **Terminal**) and introduces the critical security mechanism **Terminal State Decoupling**: clearing the input field or canceling a command immediately resets the terminal context to `currentModule = "none"`, permanently preventing conversational natural language queries or entity searches from leaking into the host Windows 11 operating system shell.

---

## 🧩 Architecture Overview  
**Browser Console (Port 8080) → Terminal Decoupling Guard (`currentModule = "none"`) → sirius_orchestrator.py → PanelAPI [ÁNO/NIE] → RuntimeCore 5.9.0 → InputParser5 → Multi-Alias KG (`autosave_kg.json`) → COLNIK-6.x / AUTONOMY 6.x → EXECUTE 6.x**

### Core Responsibilities  
- natively host the web interface via a local HTTP/WebSocket server on port 8080 within a single process  
- execute an immediate module reset (`currentModule = "none"`) upon clearing input, guaranteeing complete isolation from the host OS shell  
- provide visual inspection and management of the quarantine queue in `COLNIK-6.x/triage`  
- deliver non-invasive duplicate file auditing with strict enforcement of the `REPORT_ONLY` policy  
- render real-time hardware telemetry asynchronously (CPU, RAM, and Disk load under 1% overhead via Guard)  
- manage interactive confirmation loops via `PanelAPI` (`[ÁNO/NIE]`) with guaranteed zero proposal recurrence for established entities  
- enable seamless switching between User Mode and Developer Mode  

### Key Files & Endpoints  
- `ui_suite_8080/index.html` (main dashboard)  
- `ui_suite_8080/neon_theme.css` (futuristic neon visual styling)  
- `ui_suite_8080/app.js` (module state management and WebSocket bridge)  
- `ui_suite_8080/terminal_decoupling_guard.js` (context release to `none`)  
- `ORCHESTRATOR/sirius_orchestrator.py` (daemon on port 8080)  
- `PANEL_API/panel_api.py` (`[ÁNO/NIE]` prompt handling)  
- `http://127.0.0.1:8080` (local endpoint)  

---

## 🖥 4-Panel Suite Layout (Port 8080)  

### **1. Duplicates Panel (Duplicate Resource Management)**  
- clear visual audit of duplicate files located on the local filesystem  
- strict safety rule: **REPORT_ONLY** (zero automated deletions without explicit, authorized user confirmation)  
- direct link to storage capacity metrics delivered by the Guard module  

### **2. Triage Panel (Quarantine Queue COLNIK-6.x/triage)**  
- real-time inspection view for intercepted, unverified, or anomalous payloads  
- management of normalized data from ENVOY 5 under Non-Bio Domain Shield verification (`NonBioDomainShield`)  
- dedicated actions for manual release (Release) or safe disposal (Discard) of quarantined objects  

### **3. Navigation Panel (Navigation & Subsystem Health)**  
- deterministic routing across core branches: Runtime Core, Multi-Alias KG, Envoy Researcher, Security Vault, and Autonomy  
- live neon status indicators:  
  - **Orchestrator:** port 8080 active  
  - **Knowledge Graph:** `autosave_kg.json` synchronized (Dual-Key persistence)  
  - **COLNIK-6.x Gate:** Standard & High-Performance IPC operational  
  - **Guard Telemetry:** CPU, RAM, Disk within safe bounds  
  - **TimeCore:** heartbeat stable  

### **4. Terminal Panel (Isolated Command Console)**  
- interactive neon terminal equipped with automated shell decoupling:  
  - clearing the input prompt (Backspace/Clear) or concluding a query immediately issues `currentModule = "none"`  
  - blocks natural language queries from capturing terminal focus or executing as system shell commands in Windows PowerShell/CMD  
  - full support for multi-word compound phrases (`InputParser5`) and display of hierarchical proof trees (`KG_EXPLAIN_DEEP`)  

---

## 🔀 Operating Modes  

### **User Mode (Everyday Operation)**  
- clean, high-contrast neon interface layout  
- streamlined for dialogue, factual verification, schoolwork assistance (guaranteed `SCHOOLWORK` bypass), and knowledge exploration  
- interactive confirmation for novel entities via non-blocking `PanelAPI` prompts (`[ÁNO/NIE]`)  
- administrative system controls and sensitive OS commands are completely hidden  

### **Developer Mode (Engineering & Audit)**  
- granular tracing of orchestrator processes and memory-mapped IPC channels  
- rendering of hierarchical derivation trees (ASCII + HTML proof trees)  
- multi-alias debugging and entity management tools (`kg add alias`, `kg debug stats`, `kg release`)  
- direct access to Guard hardware telemetry and detailed COLNIK-6.x customs evaluation verdicts (ALLOW / DENY / TRIAGE)  
- live monitoring and inspection of the quarantine directory `COLNIK-6.x/triage`  

---

## 🎨 Design & Security Principles  
- **Futuristic Neon Aesthetic:** ergonomic dark background paired with high-contrast neon accents designed for extended operation  
- **Terminal State Decoupling:** zero possibility of leaking conversational queries into the host operating system shell  
- **Single-Process Sovereignty:** the entire HTTP/WebSocket server and UI suite run strictly inside `sirius_orchestrator.py`  
- **Zero Recurrence Assurance:** once an entity or alias is confirmed in the panel, redundant learning proposals are permanently suppressed  
- **Strict Non-Destructive Defaults:** panels reject destructive disk operations without multi-layer verification  

---

## 📊 Module Status (v5.9.0)  
- ✔ **Fully Stabilized & Production-Ready**  
- ✔ 4-Panel Suite architecture (`Duplicates`, `Triage`, `Navigation`, `Terminal`) deployed  
- ✔ Safety reset `currentModule = "none"` verified and active  
- ✔ Integrated on local port 8080 under single-process `sirius_orchestrator.py`  
- ✔ Live integration with `PanelAPI` (`[ÁNO/NIE]`) and XAI proof-tree visualization verified  
- ✔ Visual integration of the quarantine queue `COLNIK-6.x/triage` completed  
- ✔ Guard telemetry monitoring (CPU, RAM, Disk) operational with < 1% overhead  

---

## 🏁 Summary  
UI PANEL 6.x within the **SIRIUS Local AI v5.9.0 UNIFIED** architecture represents a complete, secure, and visually refined 4-panel web dashboard hosted at `http://127.0.0.1:8080`.  
It guarantees the complete isolation of user input from the operating system shell, visualizes the Knowledge Graph and quarantine queue in real time, and provides both users and developers with complete control over autonomous runtime operations — **deterministically, securely, explainably, and 100% offline**.

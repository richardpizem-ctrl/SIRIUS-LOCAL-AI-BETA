# 🎛 UI PANEL 6.x — 4-Panel Futuristic Neon Web Suite (Port 8080)
**Status:** ✔ Active & Stabilized  
**Version:** 6.x (Stabilized for 5.9.1 UNIFIED)  
**SIRIUS Local AI Version:** 5.9.1 UNIFIED  
**Component:** 4-Panel UI Suite, Terminal Decoupling Controller, COLNÍK Guard Shell Filter & Safe Trash Bridge  
**Role:** Unified browser-based interface running natively on local port 8080 under single-process orchestrator supervision with embedded TerminalAssistant, TimeCore latency profiling, COLNÍK Guard (0.0s hard blocks), HitL Safe Trash management, and automated terminal state decoupling (`currentModule = "none"`)

---

## 🎯 Purpose  
UI PANEL 6.x is a modern web interface with a futuristic neon aesthetic, serving as the primary interaction and control layer for the **SIRIUS Local AI v5.9.1** runtime.  
It runs natively as a single-process daemon directly through `sirius_orchestrator.py` on local port **8080** with embedded `TerminalAssistant` and `TimeCore`, permanently eliminating socket collisions and disk-level file locking contention.

The interface implements a fully decoupled architecture across four specialized panels (**Duplicates**, **Triage**, **Navigation**, **Terminal**), integrates entry-level **Token Guard** filtering (`@#$%^&*` drop), enforces greedy trailing punctuation stripping (`.rstrip("?")`), supports confirmation state latching across conversation turns, enforces **COLNÍK Guard** shell protection (0.0s hard blocks on destructive commands like `format` and `diskpart`), and manages the **Human-in-the-Loop Safe UI Trash** pipeline (`GET /trash`). It introduces the critical security mechanism **Terminal State Decoupling**: clearing the input field or canceling a command immediately resets the terminal context to `currentModule = "none"`, permanently preventing conversational natural language queries or entity searches from leaking into the host Windows 11 operating system shell.

---

## 🧩 Architecture Overview  
Browser Console (Port 8080) → Token Guard (@#$%^&*) → Terminal Decoupling Guard (currentModule = "none") → sirius_orchestrator.py (Port 8080 with TerminalAssistant + TimeCore) → COLNÍK Guard (0.0s Block) → PanelAPI [ÁNO/NIE] / [YES/NO] → RuntimeCore 5.9.1 → InputParser5 (.rstrip("?")) → Dual KG Core (autosave_kg.json / autosave_kg_en.json) → Native Merge (kg merge) → COLNIK-6.x / AUTONOMY 6.x → HitL Safe Trash (GET /trash) → EXECUTE 6.x

### Core Responsibilities  
- natively host the web interface via a local HTTP/WebSocket server on port 8080 within a single process alongside TerminalAssistant and TimeCore  
- drop malformed injection tokens (@#$%^&*) immediately at UI entry via Token Guard  
- execute an immediate module reset (currentModule = "none") upon clearing input, guaranteeing complete isolation from the host OS shell  
- route terminal shell executions through COLNÍK Guard: 0.0s hard blocking of forbidden commands (format, diskpart, rmdir /s, del /f /s /q c:, drop database)  
- manage Human-in-the-Loop Safe UI Trash: intercept direct disk deletions and divert files to quarantine for manual review via GET /trash  
- provide visual inspection and management of the quarantine queue in COLNIK-6.x/triage and oversee the 100-file sliding-window quarantine ceiling (COLNIK-6.x/envoy/quarantine/)  
- deliver non-invasive duplicate file auditing with strict enforcement of the REPORT_ONLY policy  
- render real-time hardware telemetry and command latency profiling asynchronously (CPU, RAM, Disk load under 1% overhead via Guard, latency via TimeCore cycle_delta())  
- manage interactive confirmation loops via PanelAPI ([ÁNO/NIE] / [YES/NO]) with confirmation state latching and guaranteed zero proposal recurrence for established entities and deduced taxonomies  
- enable seamless switching between User Mode and Developer Mode across isolated Slovak and English Knowledge Graph partitions  

### Key Files & Endpoints  
- ui_suite_8080/index.html (main dashboard)  
- ui_suite_8080/neon_theme.css (futuristic neon visual styling)  
- ui_suite_8080/app.js (module state management and WebSocket bridge)  
- ui_suite_8080/terminal_decoupling_guard.js (context release to none)  
- orchestrator/terminal_assistant.py (shell command gatekeeper & latency profiler)  
- colnik_6_x/colnik_guard.py (command classification matrix)  
- runtime5/token_guard.py (symbol injection filter)  
- filesystem/safe_trash_quarantine.py (quarantine storage manager)  
- runtime5/envoy_quarantine_5.py (sliding-window 100-file rotator)  
- ORCHESTRATOR/sirius_orchestrator.py (daemon on port 8080)  
- PANEL_API/panel_api.py ([ÁNO/NIE] / [YES/NO] prompt handling)  
- http://127.0.0.1:8080 (local web endpoint)  
- GET /trash (Safe UI Trash inspection and manual purge endpoint)  

---

## 🖥 4-Panel Suite Layout (Port 8080)  

### 1. Duplicates Panel (Duplicate Resource Management & Safe Trash)  
- clear visual audit of duplicate files located on the local filesystem  
- strict safety rule: REPORT_ONLY baseline (zero direct automated deletions without explicit user authorization)  
- Human-in-the-Loop Safe Trash integration: proposed file removals divert to quarantine storage and require user confirmation via GET /trash  
- direct link to storage capacity metrics delivered by the Guard module  

### 2. Triage Panel (Quarantine Queue COLNIK-6.x/triage & Sliding-Window Monitor)  
- real-time inspection view for intercepted, unverified, or anomalous payloads  
- monitoring of the sliding-window quarantine ceiling (strictly maintaining ≤ 100 JSON records in COLNIK-6.x/envoy/quarantine/)  
- management of normalized data from ENVOY 5 under Non-Bio Domain Shield verification (NonBioDomainShield)  
- dedicated actions for manual release (Release) or safe disposal (Discard) of quarantined objects  

### 3. Navigation Panel (Navigation, Subsystem Health & Dual-KG Partitioning)  
- deterministic routing across core branches: Runtime Core, Dual-Language KG (autosave_kg.json & autosave_kg_en.json), Envoy Researcher, Security Vault, and Autonomy  
- dynamic language context toggle (SK / EN) routing queries to isolated graph stores  
- live neon status indicators:  
  - Orchestrator: port 8080 active with embedded TerminalAssistant & TimeCore  
  - Knowledge Graph: dual-language partition synchronized (Lossless kg merge & KG_VERIFY active)  
  - COLNÍK Guard: shell command protection active (0.0s hard block)  
  - COLNIK-6.x Gate: Standard & High-Performance IPC operational  
  - Guard Telemetry: CPU, RAM, Disk within safe bounds (< 1% overhead)  
  - TimeCore: cycle_delta() heartbeat and latency profiler stable  

### 4. Terminal Panel (Isolated Command Console & COLNÍK Guard)  
- interactive neon terminal equipped with automated shell decoupling:  
  - clearing the input prompt (Backspace/Clear) or concluding a query immediately issues currentModule = "none"  
  - blocks natural language queries from capturing terminal focus or executing as system shell commands in Windows PowerShell/CMD  
  - Token Guard entry sanitization drops malformed inputs containing @#$%^&*  
  - greedy trailing punctuation stripping (.rstrip("?")) ensures exact entity node lookups  
  - shell execution mediated by COLNÍK Guard: 0.0s hard block on format, diskpart, rmdir /s, del /f /s /q c:, drop database  
  - multi-stage character decoding fallback (UTF-8 -> CP1250 -> CP852) guaranteeing full diacritics integrity  
  - full support for multi-word compound phrases (InputParser5) and display of hierarchical proof trees (KG_EXPLAIN_DEEP)  

---

## 🔀 Operating Modes  

### User Mode (Everyday Operation)  
- clean, high-contrast neon interface layout  
- streamlined for dialogue, factual verification, schoolwork assistance (guaranteed SCHOOLWORK bypass), reverse habitat queries, and knowledge exploration  
- interactive confirmation for novel entities via non-blocking PanelAPI prompts ([ÁNO/NIE] / [YES/NO]) with turn-persistent confirmation state latching  
- administrative system controls, raw shell executions, and destructive disk commands are completely hidden and blocked  

### Developer Mode (Engineering & Audit)  
- granular tracing of orchestrator processes, TimeCore execution latency (cycle_delta()), and memory-mapped IPC channels  
- native entity consolidation management (kg merge <src> into <tgt>) and taxonomical verification (KG_VERIFY)  
- rendering of hierarchical derivation trees (ASCII + HTML proof trees)  
- multi-alias debugging and entity management tools (kg add alias, kg merge, kg reverse location, kg debug stats, kg release)  
- direct access to Guard hardware telemetry and detailed COLNIK-6.x customs evaluation verdicts (ALLOW / DENY / TRIAGE)  
- live monitoring and inspection of the quarantine directory COLNIK-6.x/triage and Safe UI Trash (GET /trash)  

---

## 🎨 Design & Security Principles  
- Futuristic Neon Aesthetic: ergonomic dark background paired with high-contrast neon accents designed for extended operation  
- Terminal State Decoupling: zero possibility of leaking conversational queries into the host operating system shell (currentModule = "none")  
- COLNÍK Guard Interception: destructive shell commands are halted in 0.0s before host process creation  
- Human-in-the-Loop Safe Trash: direct disk unlinking is prohibited; file removals route to quarantine awaiting manual review via GET /trash  
- Token Guard Entry Sanitization: malformed injection sequences (@#$%^&*) are dropped at the UI threshold  
- Confirmation State Latching: pending proposal identifiers remain latched in memory across turns, ensuring user confirmations execute reliably  
- Dual-Language Sovereignty: strict physical and logical partition between Slovak and English graphs  
- Single-Process Sovereignty: the entire HTTP/WebSocket server, UI suite, TerminalAssistant, and TimeCore run strictly inside sirius_orchestrator.py  
- Zero Recurrence Assurance: once an entity, alias, or taxonomical edge is confirmed, redundant learning proposals are permanently suppressed  
- Strict Non-Destructive Defaults: panels reject destructive disk operations without multi-layer verification  

---

## 📊 Module Status (v5.9.1)  
- ✔ Fully Stabilized & Production-Ready  
- ✔ 4-Panel Suite architecture (Duplicates, Triage, Navigation, Terminal) deployed  
- ✔ Safety reset currentModule = "none" verified and active  
- ✔ Integrated on local port 8080 under single-process sirius_orchestrator.py with embedded TerminalAssistant + TimeCore  
- ✔ COLNÍK Guard 0.0s command blocking integration active  
- ✔ Human-in-the-Loop Safe UI Trash pipeline operational (GET /trash)  
- ✔ Token Guard input sanitization and trailing punctuation stripping (.rstrip("?")) operational  
- ✔ Sliding-window quarantine rotation (100-file ceiling) active  
- ✔ Live integration with PanelAPI ([ÁNO/NIE] / [YES/NO]) with confirmation state latching active  
- ✔ Dual-language Knowledge Graph visualization verified (autosave_kg.json & autosave_kg_en.json)  
- ✔ Visual integration of the quarantine queue COLNIK-6.x/triage completed  
- ✔ Guard telemetry monitoring (CPU, RAM, Disk) operational with < 1% overhead  

---

## 🏁 Summary  
UI PANEL 6.x within the **SIRIUS Local AI v5.9.1 UNIFIED** architecture represents a complete, secure, and visually refined 4-panel web dashboard hosted at `http://127.0.0.1:8080`.  
It guarantees the complete isolation of user input from the operating system shell, blocks destructive shell routines in 0.0s via COLNÍK Guard, diverts file removals into Human-in-the-Loop Safe Trash, caps quarantine storage at 100 records, visualizes isolated dual-language Knowledge Graphs and quarantine queues in real time, and provides both users and developers with complete control over autonomous runtime operations — **deterministically, securely, explainably, and 100% offline**.

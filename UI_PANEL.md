# 🎛 UI PANEL 6.x — 4-Panel Futuristic Neon Web Suite (Port 8080)
**Status:** ✔ Active & Stabilized  
**Version:** 6.x (Stabilized for 5.9.5 UNIFIED)  
**SIRIUS Local AI Version:** 5.9.5 UNIFIED  
**Author / Architecture:** Richard Pizem  
**Component:** 4-Panel UI Suite, Terminal Decoupling Controller, COLNÍK Guard Shell Filter, Professor Validator Middleware & Safe Trash Bridge  
**Role:** Unified browser-based interface running natively on local port 8080 under single-process orchestrator supervision with embedded TerminalAssistant, TimeCore latency profiling, COLNÍK Guard (0.0s hard blocks), Professor Middleware quality gating (PASS / WARN / REJECT), HitL Safe Trash management, and automated terminal state decoupling (`currentModule = "none"`)

---

## 🎯 Purpose  
UI PANEL 6.x is a modern web interface with a futuristic neon aesthetic, serving as the primary interaction and presentation layer for the **SIRIUS Local AI v5.9.5** runtime, architected by Richard Pizem.  
It runs natively as a single-process daemon directly through `sirius_orchestrator.py` on local port **8080** with embedded `TerminalAssistant` and `TimeCore`, permanently eliminating socket collisions and disk-level file locking contention.

The interface implements a fully decoupled architecture across four specialized panels (**Duplicates**, **Triage**, **Navigation**, **Terminal**), integrates entry-level **Token Guard** filtering (`@#$%^&*` drop), pre-processing spellcheck (`spellcheck_engine.py`), greedy trailing punctuation stripping (`.rstrip("?")`), supports confirmation state latching across conversation turns, enforces **COLNÍK Guard** shell protection (0.0s hard blocks on destructive commands like `format` and `diskpart`), and manages the **Human-in-the-Loop Safe UI Trash** pipeline (`GET /trash`).

UI output is strictly governed by the **Professor Middleware Layer** (`Professor Validator`): while the Runtime Core can discover any arbitrary data within the Knowledge Graph, the Professor determines (via **PASS / WARN / REJECT** states) whether and in what format that output is presented to the user. Concurrently, the interface enforces the critical **Terminal State Decoupling** mechanism: clearing the input field or canceling a command immediately resets the terminal context to `currentModule = "none"`, permanently preventing conversational queries from leaking into the host Windows 11 shell.

---

## 🧩 Architecture Overview  
[ USER / UI PANEL (Port 8080) ]  
          │ (Query Input / Command)  
          ▼  
Token Guard (@#$%^&* drop) → spellcheck_engine.py (Typo and diacritics correction)  
          ▼  
sirius_orchestrator.py (Port 8080 with TerminalAssistant + TimeCore)  
          ▼  
COLNÍK Guard (0.0s Hard Block) → Terminal Decoupling Guard (currentModule = "none")  
          ▼  
RuntimeCore 5.9.5 (Lookup in autosave_kg.json / autosave_kg_en.json)  
          │ (Raw response / Graph data)  
          ▼  
┌────────────────────────────────────────────────────────┐  
│               PROFESSOR MIDDLEWARE LAYER               │  
│                                                        │  
│   1. Professor Cleaner / grammar_engine.py             │  
│   2. Professor Validator (PASS / WARN / REJECT)        │  
│   3. Professor Summarizer / professor_miner.py         │  
└────────────────────────────────────────────────────────┘  
          │ (Filtered, enriched, and validated response)  
          ▼  
PanelAPI [ÁNO/NIE] / [YES/NO] → COLNIK-6.x / AUTONOMY 6.x → HitL Safe Trash (GET /trash)  
          ▼  
[ UI PANEL (V2) — Rendering the result to the user ]  

---

### Core Responsibilities  
- Host the web interface locally via HTTP/WebSocket on port 8080 within a single process alongside TerminalAssistant and TimeCore  
- Drop malicious input tokens (@#$%^&*) immediately at entry via Token Guard and normalize text through spellcheck_engine  
- Relay output only after verification via **Professor Validator** (forward on PASS, visual uncertainty flag on WARN, output suppression on REJECT)  
- Execute an immediate module reset (currentModule = "none") upon clearing input to guarantee total isolation from the OS shell  
- Route terminal commands through COLNÍK Guard: 0.0s instantaneous blocking of prohibited commands (format, diskpart, rmdir /s, del /f /s /q c:, drop database)  
- Manage Human-in-the-Loop Safe UI Trash: intercept direct disk-level file deletions and route them into quarantine for manual inspection (GET /trash)  
- Provide visual inspection and management of the quarantine queue in COLNIK-6.x/triage and supervise the quarantine sliding window limit (100 files in COLNIK-6.x/envoy/quarantine/)  
- Ensure non-invasive auditing of duplicate files with strict enforcement of the REPORT_ONLY policy  
- Asynchronously render hardware telemetry and command latency profiling (Guard CPU, RAM, Disk overhead under 1%, TimeCore cycle_delta())  
- Drive interactive confirmation loops via PanelAPI ([ÁNO/NIE] / [YES/NO]) with state latching and zero proposal redundancy  
- Enable seamless switching between User and Developer modes across isolated language partitions of the graph (SK / EN)  

### Key Files & Endpoints  
- ui_suite_8080/index.html (main dashboard)  
- ui_suite_8080/neon_theme.css (futuristic neon visuals)  
- ui_suite_8080/app.js (module state management and WebSocket bridge)  
- ui_suite_8080/terminal_decoupling_guard.js (context release to "none")  
- orchestrator/terminal_assistant.py (shell command gatekeeper and latency profiler)  
- colnik_6_x/colnik_guard.py (command classification matrix)  
- runtime5/token_guard.py (symbol injection filter)  
- runtime5/spellcheck_engine.py (diacritics and typo pre-processing)  
- runtime5/professor_validator.py (PASS / WARN / REJECT quality gate)  
- runtime5/grammar_engine.py (Professor Cleaner & triplet extraction)  
- runtime5/professor_miner.py (Professor Summarizer)  
- filesystem/safe_trash_quarantine.py (deleted files quarantine manager)  
- runtime5/envoy_quarantine_5.py (100-file sliding window quarantine rotator)  
- ORCHESTRATOR/sirius_orchestrator.py (single-process daemon on port 8080)  
- PANEL_API/panel_api.py (prompt handler for [ÁNO/NIE] / [YES/NO])  
- http://127.0.0.1:8080 (local endpoint)  
- GET /trash (interface for inspection and safe emptying of the trash)  

---

## 🎓 Professor Middleware Layer (Output Quality Control)

Positioned between the Runtime Core and the UI Panel, the **Professor** validation layer guarantees that erroneous, contradictory, or incomplete facts never reach the user interface:

1. **Professor Cleaner (`grammar_engine.py`):**  
   - Normalizes extracted relations and triplets, cleans stopwords, and isolates reflexive pronouns (*sa/si*).  
   - Filters single-letter conjunctions for SK and indefinite articles for EN without degrading the integrity of multi-word entities.

2. **Professor Validator (Decision Logic):**  
   - **PASS (High Fact Quality):** Facts are consistent, verified, and complete. The response is immediately rendered to the UI.  
   - **WARN (Usable but Uncertain):** Facts satisfy baseline criteria but exhibit a lower confidence threshold. The response is forwarded with a neon visual uncertainty flag.  
   - **REJECT (Incomplete, Corrupted, or Contradictory):** The response is withheld entirely. The UI receives a structured rejection payload:
     ```json
     {
       "status": "REJECT",
       "reason": "INCOMPLETE_FACTS"
     }
     ```
     *(Alternative reasons: `"LOW_CONFIDENCE"`, `"CONTRADICTION"`)*

3. **Professor Summarizer (`professor_miner.py`):**  
   - Synthesizes multiple factual nodes into a concise, scannable UI output.

---

## 🖥 4-Panel Suite Layout (Port 8080)  

### 1. Duplicates Panel (Duplicate File Management & Safe Trash)  
- Visual overview of duplicate files discovered on the local drive  
- Strict enforcement of the REPORT_ONLY rule (no automated deletion without explicit user intervention)  
- Human-in-the-Loop Safe Trash integration: flagged files are routed to quarantine, requiring manual approval via `GET /trash`  
- Direct pipeline integration with Guard disk telemetry metrics  

### 2. Triage Panel (COLNIK-6.x/triage Quarantine Queue & Sliding Window Tracking)  
- Real-time tracking of intercepted, unverified, or corrupted data  
- Sliding window capacity monitoring (strictly capped at 100 JSON records in `COLNIK-6.x/envoy/quarantine/`)  
- Ingestion verification of normalized ENVOY 5 data guarded by the Non-Bio Domain Shield (`NonBioDomainShield`)  
- Dedicated controls for manual release (Release) or safe disposal (Discard) of quarantined objects  

### 3. Navigation Panel (Navigation, Subsystem Health & Dual KG)  
- Deterministic branch routing: Runtime Core, Dual KG (`autosave_kg.json` & `autosave_kg_en.json`), Envoy Researcher, Security Vault, and Autonomy  
- Dynamic language context switching (SK / EN) across isolated graphs  
- Neon status indicators:  
  - Orchestrator: port 8080 active with TerminalAssistant & TimeCore  
  - Knowledge Graph: dual partitions synchronized (lossless `kg merge` and `KG_VERIFY` active)  
  - Professor Validator: throughput and filtering state (PASS / WARN / REJECT)  
  - COLNÍK Guard: shell command protection active (0.0s block latency)  
  - COLNIK-6.x Gate: standard and IPC runtime operational  
  - Guard Telemetry: CPU, RAM, and Disk overhead nominal (< 1% overhead)  
  - TimeCore: steady `cycle_delta()` pulse and latency profiling  

### 4. Terminal Panel (Isolated Command Console & COLNÍK Guard)  
- Interactive neon terminal with automated State Decoupling:  
  - Clearing input (Backspace/Clear) immediately sets `currentModule = "none"`  
  - Prevents standard conversational queries from leaking as command strings into the host Windows shell (PowerShell/CMD)  
  - Token Guard immediately drops illegal character strings (`@#$%^&*`) on input  
  - Trailing question mark trimming (`.rstrip("?")`) guarantees clean entity resolution  
  - COLNÍK Guard halts destructive commands at 0.0s (`format`, `diskpart`, `rmdir /s`, `del /f /s /q c:`, `drop database`)  
  - Multi-tier output decoding pipeline (UTF-8 -> CP1250 -> CP852) guarantees pristine diacritics  
  - Support for multi-word phrases via InputParser5 alongside deductive inference trees (`KG_EXPLAIN_DEEP`)  

---

## 🔀 Operating Modes  

### User Mode (Standard Operation)  
- Clean neon UI focused on dialogue, fact verification, academic inquiries (SCHOOLWORK bypass), and knowledge graph navigation  
- All outputs are gated and verified by the Professor validation layer  
- Interactive new entity confirmation via PanelAPI (`[ÁNO/NIE]` / `[YES/NO]`) with state latching  
- Administrative operating system commands and raw shell access remain hidden and strictly locked  

### Developer Mode (Engineering & Audit Operation)  
- Low-level orchestrator tracing, TimeCore latency profiling (`cycle_delta()`), and IPC stream monitoring  
- Native entity merge controls (`kg merge <src> into <tgt>`) and taxonomic deduction auditing (`KG_VERIFY`)  
- Visual rendering of proof trees (ASCII and HTML formats) via `KG_EXPLAIN_DEEP`  
- Professor Validator diagnostics: inspection of granular REJECT and WARN telemetry  
- Entity alias management tools (`kg add alias`, `kg merge`, `kg reverse location`, `kg debug stats`, `kg release`)  
- Direct inspection of Guard hardware telemetry and COLNIK-6.x triage verdicts (ALLOW / DENY / TRIAGE)  
- Live control of `COLNIK-6.x/triage` quarantine and the Safe UI Trash pipeline (`GET /trash`)  

---

## 🎨 Design & Security Principles  
- **Futuristic Neon Aesthetic:** High-contrast elements against an ergonomic dark theme optimized for long operational sessions  
- **Professor Quality Gating:** The Runtime Core gathers graph data, but the Professor Middleware holds definitive authority on whether facts are permitted to reach the UI  
- **Terminal State Decoupling:** Zero probability of conversational queries spilling into host OS shells (`currentModule = "none"`)  
- **COLNÍK Guard Interception:** Instantaneous 0.0s halting of prohibited command executions  
- **Human-in-the-Loop Safe Trash:** Deletion suppression in favor of quarantine routing with explicit sign-off via `GET /trash`  
- **Token Guard Entry Sanitization:** Immediate dropping of injection patterns (`@#$%^&*`) at the UI threshold  
- **Confirmation State Latching:** Retention of pending proposal IDs across conversational turns  
- **Dual-Language Sovereignty:** Fully segregated Slovak and English database partitions preventing cross-linguistic contamination  
- **Single-Process Sovereignty:** Orchestrator, UI server, TerminalAssistant, and TimeCore run entirely within a single `sirius_orchestrator.py` process  
- **Zero Recurrence Assurance:** Confirmed facts and established taxonomies are permanently committed, eliminating repeated prompts  
- **Strict Non-Destructive Defaults:** Standard operation strictly defaults to safe, non-destructive REPORT_ONLY handling  

---

## 📊 Module Status (v5.9.5)  
- ✔ Fully stabilized and production-ready  
- ✔ Architectural design by Richard Pizem  
- ✔ 4-panel layout (Duplicates, Triage, Navigation, Terminal) deployed  
- ✔ Security reset mechanism `currentModule = "none"` active  
- ✔ Single-process execution active on port 8080 (`sirius_orchestrator.py` with TerminalAssistant and TimeCore)  
- ✔ Professor Middleware Layer integrated (Cleaner, Validator PASS/WARN/REJECT, Summarizer)  
- ✔ COLNÍK Guard 0.0s destructive command interception verified  
- ✔ Human-in-the-Loop Safe UI Trash operational (`GET /trash`)  
- ✔ Token Guard and trailing question mark trimming (`.rstrip("?")`) active  
- ✔ Sliding window quarantine limit (100 files ceiling) active  
- ✔ PanelAPI interactive confirmation loops (`[ÁNO/NIE]` / `[YES/NO]`) with state latching verified  
- ✔ Dual graph visualization verified (`autosave_kg.json` and `autosave_kg_en.json`)  
- ✔ `COLNIK-6.x/triage` queue visual integration complete  
- ✔ Guard hardware telemetry (CPU, RAM, Disk) operational with < 1% overhead  

---

## 🏁 Summary  
UI PANEL 6.x within the **SIRIUS Local AI v5.9.5 UNIFIED** architecture, designed by Richard Pizem, delivers a unified, secure, neon-styled web suite operating at `http://127.0.0.1:8080`.  
It guarantees complete decoupling of user input from the host shell, blocks destructive commands in 0.0s via COLNÍK Guard, routes file deletions through the Safe Trash quarantine, enforces a 100-file sliding window limit, and **strictly regulates the veracity, consistency, and completeness of every displayed fact through the Professor validation layer** — **deterministically, safely, explainably, and 100% offline**.

# 📜 CHANGELOG — SIRIUS LOCAL AI
**Author & Architecture Lead:** Richard Pizem  

---

## v5.9.5 — Dual-Language KG Architecture + Native Lossless Entity Merge + Taxonomical Habitat Reasoning + Pre-Processing Spellcheck + Professor Middleware Layer + SafeRollback Crash Resilience + COLNÍK Guard Security Protocol (2026‑10‑22)

### 🔥 Major Update
Version 5.9.5 delivers a major architectural advancement focusing on complete bilingual knowledge isolation, native in-memory graph operations, resilient taxonomical inference, automated pre-processing diacritic and typo correction, authoritative cognitive fact verification through the Professor Middleware Layer, absolute state protection via SafeRollback, and comprehensive security hardening across the SIRIUS / COLNÍK ecosystem.  
This release introduces independent, isolated storage backends for Slovak (`autosave_kg.json`) and English (`autosave_kg_en.json`), integrates a native lossless entity merge engine (`kg merge`) directly inside RuntimeCore, implements context-aware mammalian category deduction (`KG_VERIFY`), repairs reverse habitat querying with non-destructive flora shielding, integrates an entry-level pre-processing spellcheck engine (`spellcheck_engine.py`), enforces strict cognitive quality validation via the Professor Middleware Layer (`grammar_engine.py`, `professor_validator.py`, `professor_miner.py`) evaluating `PASS / WARN / REJECT` criteria, adds greedy trailing punctuation sanitization (`.rstrip("?")`), latches proposal confirmation states across interactive turns, implements granular module-level backup and restore via SafeRollback (`safe_rollback.py`), and formalizes the complete COLNÍK Guard security layer (featuring Token Guard, sliding-window quarantine rotation, and the Human-in-the-Loop Safe Trash pipeline).

The foundational principle of the v5.9.5 runtime is strictly enforced:  
> **Runtime Core and symbolic reasoning mechanisms may retrieve or infer any fact from the Knowledge Graph, but the Professor Middleware Layer authoritatively determines whether the output is permitted to reach the UI or commit to persistent state.**

All operations execute 100% offline, orchestrated inside a single-process IPC daemon running natively on port 8080 via `sirius_orchestrator.py`.

---

### 🌐 Dual-Language Isolated KG Architecture (`autosave_kg.json` & `autosave_kg_en.json`)
- **Strict Physical & Logical Segregation:** Fully separated knowledge graphs for Slovak (`autosave_kg.json`) and English (`autosave_kg_en.json`), preventing cross-lingual corruption, mixed-language article summaries, and bilingual entity collisions.
- **Dynamic Language Context Dispatch:** `RuntimeCore` automatically binds queries, node retrieval, attribute manipulation, relations, and autosave routines to the exact language selected in the UI Panel (`SK` / `EN`).
- **Synchronized Dual Autosave:** Independent atomic serialization for both linguistic models on runtime shutdown and immediately following external Envoy enrichments.

---

### 🔤 Pre-Processing Spellcheck Layer (`spellcheck_engine.py`)
- **Accent & Diacritic Normalization:** Automatically normalizes unaccented or mistyped query strings (e.g., `urologia` cleanly maps to canonical node `urológia`), eliminating false-negative misses during Knowledge Graph lookups.
- **Typo Correction & Input Sanitization:** Suppresses input noise and spelling variations prior to entity extraction without altering semantic intent.

---

### 🎓 Professor Middleware Layer (`Professor Validator`, `Cleaner` & `Summarizer`)
- **Cognitive Quality Gateway:** Mediates all communication between Runtime Core/Reasoning Engine and the UI presentation layer, strictly preventing hallucinations, fragmented triplets, and contradictory assertions from reaching the user.
- **Professor Cleaner (`grammar_engine.py`):**
  - Standardizes and normalizes relation triplets (`add_relation(source, relation, target)`).
  - Handles complex predicate phrases and reflexive verbs (*sa zaoberá*, *zaoberá sa*, *deals with*, *focuses on*).
  - Isolates reflexive particles (*sa/si*) directly into relation edges rather than contaminating subject tokens.
  - Preserves essential Slovak conjunctions (*a*, *i*) within compound objects while filtering English indefinite articles (*a*, *an*).
- **Professor Validator Gate (`professor_validator.py`):**
  - **PASS:** 100% factual consistency and integrity; the output is immediately released to UI Panel V2.
  - **WARN:** Factual assertion is valid but carries lower confidence (`LOW_CONFIDENCE`); rendered with a distinctive visual neon uncertainty flag.
  - **REJECT:** Intercepts incomplete facts (`INCOMPLETE_FACTS`) or contradictory graph assertions (`CONTRADICTION`); blocks output rendering completely, returns structured JSON diagnostic errors, and dispatches the incident to `COLNIK-6.x/triage`.
- **Professor Summarizer (`professor_miner.py`):**
  - Performs deterministic multi-node semantic summarization for clean presentation in the 4-Panel UI Suite.

---

### 🔀 Native Lossless KG Merge Engine (`kg merge <src> into <tgt>`)
- **Direct RuntimeCore Interceptor:** Integrated directly into `RuntimeCore` without external script invocations, brittle file paths, or import dependencies.
- **Zero-Loss Attribute Relocation:** Migrates all properties, descriptions, alternative summaries, and habitat definitions from the source node directly into the target node.
- **Automatic Alias Node Transition:** Source entities are preserved as lightweight alias nodes with directional graph edges (`src -[alias]-> tgt`), enabling seamless bi-directional discovery.

---

### 🧬 Taxonomical & Marsupial Inference (`KG_VERIFY`)
- **Ontological Category Verification:** Accurately deduces higher-order biological categories directly from stored text records (e.g., recognizing that marsupials and macropods belong to mammals without requiring rigid exact matches).
- **Persistent Edge Auto-Commit:** Once verified via Envoy or contextual extraction, taxonomical edges (`kangaroo -[is_a]-> mammal`, `macropus -[je]-> cicavec`) are committed directly to the active knowledge graph, resulting in zero confirmation recurrence on repeated queries.

---

### 🌍 Non-Destructive Reverse Location Engine (`_execute_reverse_location_query`)
- **Universal Multi-Stem Regional Matching:** Unified location matching supporting inflected geographic forms across both languages (*Austrálii*, *Austrália*, and *Australia*).
- **False-Positive Flora Guard:** Eliminated naive substring collisions that previously misclassified tree-dwelling animals (*„stromový vačkovec“*) as flora. *Koala medvedíkovitá*, *Macropus*, and *Krokodíl morský* now reliably resolve under Australian fauna.
- **Direct Attribute Access:** Standardized all graph iterations via `self.kg.get_attributes()`, eliminating silent lookup failures caused by accessing raw internal dictionaries.

---

### 🔤 Punctuation Hygiene & Confirmation State Latching (`InputParser5` & `RuntimeCore`)
- **Greedy Trailing Punctuation Stripping:** Sanitizes input strings by trimming trailing question marks (`.rstrip("?")`), preventing entity lookup failures (e.g., `CO JE MACROPUS?` cleanly resolves to node `macropus`).
- **Confirmation State Latching:** Workflow fallback prompts strictly maintain pending entity identifiers in memory, ensuring affirmative user confirmations (`ÁNO`, `ANO`, `YES`, `Y`) correctly trigger Envoy execution rather than encountering a detached state.

---

### 🔄 SafeRollback Crash Resilience (`safe_rollback.py`)
- **Granular Module-Level Backups:** Executes atomic directory and configuration snapshots via `shutil.copytree` before state mutations occur.
- **Instant Atomic Restoration:** Enables immediate rollback via `shutil.rmtree` upon runtime errors or interrupted cycles, protecting configuration and knowledge stores without Git dependencies.

---

### 🛡️ Comprehensive Security Protocol (COLNÍK Guard & Safe UI Trash)
- **Safe UI Trash (Human-in-the-Loop):** Files flagged for removal (duplicates, empty folders, damaged files) are never deleted directly from disk; they are quarantined and require manual user approval via `GET /trash`.
- **System File Protection:** System configurations, logs, code modules, knowledge graphs (`autosave_kg.json`, `autosave_kg_en.json`), and IPC buffers are strictly protected from modification.
- **TerminalAssistant & COLNÍK Guard Shell Filter:**
  - **FORBIDDEN (0.0s Hard Block):** `format`, `rmdir /s`, `del /f /s /q c:`, `diskpart`, `drop database`, fork-bombs.
  - **RISKY (Explicit Prompt Required):** `rm`, `kill`, `taskkill`, `del`.
  - **ALLOWED:** `ps`, `top`, `mem`, `sys`, `grep`, `info`, `cat`, `head`, `tail`, `check`, `template`, `python`, `git`, `pip`, `ls`, `dir`, `cd`, `pwd`, `mkdir`, `touch`, `help`.
- **Token Guard:** Entry-level sanitization rejecting corrupted or dangerous symbol sequences (`@#$%^&*`) on raw input before runtime processing.
- **Terminal State Decoupling:** Clearing the console input immediately triggers an event setting `currentModule = "none"`, permanently preventing conversational natural language from executing inside the host shell.
- **Automatic Sliding-Window Quarantine Rotation:** Enforces a strict 100-file ceiling inside `COLNIK-6.x/envoy/quarantine/`, automatically pruning older JSON payloads upon new arrivals.
- **Character Encoding Stabilization:** Multi-stage shell output decoding (UTF-8 → CP1250 → CP852 fallback) ensuring full diacritics integrity.

---

### ⚙ Execution Command
SIRIUS Runtime 5.9.5 is launched via the central orchestrator:
```cmd
python sirius_orchestrator.py --port 8080
```

---

### 📦 Included in ZIP (`SIRIUS_LOCAL_AI_5.9.5.zip`)
- Full clean Runtime 5.9.5 codebase (all `__pycache__` and compiled `.pyc` artifacts removed)
- `sirius_orchestrator.py` with native single-process port 8080 IPC bridge and embedded `TerminalAssistant` + `TimeCore`
- Dual knowledge graph stores: `autosave_kg.json` (SK) and `autosave_kg_en.json` (EN)
- Pre-processing spellcheck module (`spellcheck_engine.py`)
- Professor Middleware Layer: `grammar_engine.py` (Cleaner), `professor_validator.py` (PASS / WARN / REJECT Gate), and `professor_miner.py` (Summarizer)
- SafeRollback backup/restore module (`safe_rollback.py`)
- Native `kg merge` engine, Token Guard, and sliding-window quarantine rotator
- Enhanced `InputParser5`, `EnvoyExecutionLayer5`, and `EnvoyNormalizer5`
- 4-Panel UI suite assets and browser dashboard (`index.html` on port 8080)
- COLNÍK 6.x validation subsystem (Standard, IPC Mode & COLNÍK Guard)
- AUTONOMY 6.x (Control, Guard, Triage Mode & HitL Safe Trash)
- Full symbolic reasoning engine, XAI proof-tree pipeline, and taxonomical inference rules

---

## v5.9.1 — Dual-Language KG Architecture + Native Lossless Entity Merge + Taxonomical Habitat Reasoning + COLNÍK Guard Security Protocol (2026‑10‑06)
*(Previous production version)*

## v5.9.0 — Semantic Multi-Word Parsing + Autonomous Envoy Disambiguation Triage + 4-Panel UI Suite + Multi-Alias KG Persistence (2026‑09‑25)
*(Previous version)*

## v5.8 — Unified Orchestrator + PanelAPI Loops + TimeCore & Guard Supervision + COLNIK/AUTONOMY IPC (2026‑09‑10)
*(Previous version)*

## v5.7.0 — Unified Logic Layer + Stabilized KG Platform + COLNIK‑AUTONOMY Integration
*(Previous version)*

## v5.6.2 — Stabilized Logic Layer + Unified KG Platform
*(Previous version)*

## v5.5.0 — Unified Reasoning & Explainability Architecture
*(Previous version)*

## v5.0.0 — Unified Offline Reasoning Runtime
*(Previous version)*

## v4.5.0 PRO — System Intelligence Expansion
*(Previous version)*

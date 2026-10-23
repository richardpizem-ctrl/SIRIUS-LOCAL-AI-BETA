# 🏗 Architecture – SIRIUS LOCAL AI (Runtime 5.9.5 — Dual-Language KG Architecture, Lossless Entity Merge, Pre-Processing Spellcheck & Professor Middleware Layer)
**Author & Architecture Lead:** Richard Pizem  

<p align="center">
  <img src="https://img.shields.io/badge/version-5.9.5--UNIFIED-orange">
  <img src="https://img.shields.io/badge/license-SUL--3.2.0-green">
  <img src="https://img.shields.io/badge/platform-Windows%2011-blue">
  <img src="https://img.shields.io/badge/runtime-SIRIUS%20Runtime%205.9.5-red">
  <img src="https://img.shields.io/badge/local%20AI-100%25-blueviolet">
</p>

The SIRIUS LOCAL AI Runtime **5.9.5** represents an enterprise-grade, deterministic architecture built on top of:

- Dual-Language Knowledge Graph Architecture (`autosave_kg.json` for SK and `autosave_kg_en.json` for EN)
- Native Lossless Entity Merge Engine (`kg merge <src> into <tgt>`) integrated directly inside `RuntimeCore`
- Pre-Processing Spellcheck & Diacritics Normalization Layer (`spellcheck_engine.py`)
- Authoritative **Professor Middleware Layer** (`grammar_engine.py`, `professor_validator.py`, `professor_miner.py`) executing strict `PASS / WARN / REJECT` decision middleware
- Ontological & Taxonomical Reasoning Engine (`KG_VERIFY`) with hierarchical mammalian category deduction
- Resilient Reverse Location Querying (`_execute_reverse_location_query`) with anti-flora classification guard
- Greedy Trailing Punctuation Sanitization (`.rstrip("?")`) preventing key matching failures
- Confirmation State Latching preserving pending proposal context across interactive turns
- Hard Token Guard blocking corrupted and malicious input character sequences (`@#$%^&*`)
- Automatic Envoy Quarantine Sliding Window enforcing a 100-file ceiling
- TerminalAssistant + TimeCore Security Layer with 0.0s hard blocking of forbidden commands (`format`, `diskpart`)
- Safe UI Trash & Human-in-the-Loop (HitL) verification isolating file removals without direct disk deletion (`GET /trash`)
- SafeRollback Integration (`safe_rollback.py`) executing granular module-level backups (`shutil.copytree`) and instant restorations (`shutil.rmtree`) for absolute crash resilience
- Single-Process IPC Bridge running natively on port 8080 inside `sirius_orchestrator.py`
- Multi-Word Compound Parser (`InputParser5` preserving full noun phrases)
- Central Execution Loop powered by `sirius_orchestrator.py` with dual-graph atomic serialization

The foundational principle of the architecture is strictly enforced:  
> **Runtime Core and symbolic reasoning mechanisms may infer or retrieve any fact from the Knowledge Graph, but the Professor Middleware Layer (Cleaner, Validator PASS/WARN/REJECT, Summarizer) authoritatively determines whether the output is permitted to reach the UI or commit to persistent state.**

---

# 🧩 Architectural Principles (Runtime 5.9.5)

- **Dual-Language Knowledge Graph Isolation:** Physical and logical partition of Slovak (`autosave_kg.json`) and English (`autosave_kg_en.json`) graphs.
- **Professor Cognitive Quality Gating:** Runtime Core can discover anything in the graph, but the Professor Middleware Layer determines if facts are released to the user via PASS / WARN / REJECT validation.
- **Pre-Processing Text Hygiene:** Automatic normalization of typos and unaccented characters via `spellcheck_engine.py` prior to graph indexing.
- **Native In-Memory Entity Consolidation:** Lossless property migration with bidirectional alias formation (`kg merge`).
- **Taxonomical Inference without Recurrence:** Sub-taxa automatically deduced and auto-committed to KG (`KG_VERIFY`).
- **Non-Destructive Habitat Traversal:** Uniform attribute retrieval via `self.kg.get_attributes()`.
- **Unified Semantic Pipeline:** InputParser5 → Token Guard → Contextual KG → Reasoning → Professor Middleware → ENVOY → COLNIK → AUTONOMY → UI.
- **Deterministic Execution Loop:** Driven centrally by single-process `sirius_orchestrator.py` on local port 8080.
- **Compound Phrase Integrity:** No truncation of multi-word modifiers.
- **Autonomous Disambiguation Triage:** Sub-article pathfinding and parenthetical stripping.
- **Zero-Cloud Guarantee:** 100% offline, local workstation execution.
- **Deterministic IPC Communication:** Hosted on local port 8080 without external process locks.
- **Interactive CLI/UI Learning Proposals:** `[ÁNO/NIE]` / `[YES/NO]` with latched state confirmation across conversation turns.
- **Customs-Grade Operation Auditing:** Verified via COLNIK-6.x and AUTONOMY 6.x.
- **Human-in-the-Loop Safety Shielding:** All file deletions quarantined for explicit UI user approval (`GET /trash`).
- **Absolute State Protection:** Powered by SafeRollback module-level backups (`safe_rollback.py`).

---

# 🧱 Core Layers (Runtime 5.9.5)

## 1. Input Parsing, Token Hygiene & Spellcheck (`InputParser5`, `TokenGuard5` & `spellcheck_engine.py`)
Responsibilities:
- Immediate rejection of malicious or corrupted inputs (`@`, `#`, `$`, `%`, `^`, `&`, `*`) upon receiving `kg query` commands via `TokenGuard5`
- Diacritic normalization and typo suppression via `spellcheck_engine.py` ensuring accent-free queries (e.g., `urologia`) reliably match canonical nodes (e.g., `urológia`)
- Greedy trailing punctuation stripping (`.rstrip("?")`) preventing token lookup mismatch (e.g., `CO JE MACROPUS?` cleanly resolves to `macropus`)
- Extraction of complex compound noun phrases (`ovcia vlna`, `mobilny telefon`, `pevna linka`)
- Strict isolation of copula verbs (`je`, `sú`, `is`, `are`) from subject entities, preventing query contamination

---

## 2. Dual-Language Knowledge Graph Architecture (`KnowledgeGraph`)
Responsibilities:
- Complete logical and physical isolation: `autosave_kg.json` (SK) and `autosave_kg_en.json` (EN)
- Dynamic context switching: `RuntimeCore` automatically binds active queries, attributes, relations, and autosaves according to the active language flag received from the UI (`SK` / `EN`)
- Native Lossless Entity Merge (`kg merge <src> into <tgt>`): consolidates attributes and transitions source entities into alias nodes with directional graph edges (`src -[alias]-> tgt`)
- Direct, uniform attribute inspection via `self.kg.get_attributes()` eliminating silent lookup failures
- Cycle-safe data representation and inbound/outbound edge traversal
- Atomic dual serialization on shutdown and immediately following external Envoy enrichments

---

## 3. Ontological & Habitat Reasoning Engine (`ReasoningEngine5` & `KG_VERIFY`)
Capabilities:
- Hierarchical Taxonomical Deduction: deduces higher-order biological categories directly from summary records (e.g., automatically recognizing *marsupials* and *macropods* as mammals without requiring rigid Wikipedia exact matches)
- Persistent Edge Auto-Commit: verified taxonomical edges (`kangaroo -[is_a]-> mammal`, `macropus -[je]-> cicavec`) are committed directly into the active graph with zero proposal recurrence
- Non-Destructive Reverse Location Engine (`_execute_reverse_location_query`): multi-stem regional matching supporting inflected geographic forms across both languages (*Austrálii*, *Austrália*, and *Australia*)
- False-Positive Flora Guard: eliminates naive substring collisions that previously misclassified tree-dwelling animals (*„stromový vačkovec“*) as flora

Active Rules:
- MultiHopOrbitInferenceRule
- DedicsnostVlastnostiRule
- TranzitivneRelacieRule
- AutoTypeInferenceRule
- OrbitTypeInferenceRule

---

## 4. Professor Middleware Layer (`Professor Validator`, `Cleaner` & `Summarizer`)
Capabilities:
- Authoritative quality and truth gateway mediating between Runtime Core and UI Panel V2:
  - **Professor Cleaner (`grammar_engine.py`):** Normalizes relation triplets, handles reflexive verbs (*sa zaoberá*, *deals with*), separates reflexive particles (*sa/si*) into relation edges, preserves Slovak conjunctions (*a*, *i*), and filters English indefinite articles (*a*, *an*).
  - **Professor Validator Gate (`professor_validator.py`):** Evaluates cognitive consistency using a three-tier decision matrix:
    - **PASS:** 100% verified factual integrity; immediately released to UI.
    - **WARN:** Factual assertion is valid but carries lower confidence (`LOW_CONFIDENCE`); rendered with a distinct visual uncertainty indicator.
    - **REJECT:** Intercepts incomplete facts (`INCOMPLETE_FACTS`) or contradictory assertions (`CONTRADICTION`); blocks output rendering completely, returns structured error codes, and routes the incident to `COLNIK-6.x/triage`.
  - **Professor Summarizer (`professor_miner.py`):** Synthesizes multi-node knowledge graphs into unified, human-readable answers.

---

## 5. Autonomous ENVOY & Quarantine Layer (`EnvoyExecutionLayer5` & `EnvoyQuarantine5`)
Capabilities:
- Autonomous Disambiguation Triage: detects disambiguation structures (*„môže byť...“*) and resolves specific context targets
- Anti-Prefix & Phonetic Guard: eliminates invalid prefix matches (e.g., stopping *Káva* -> *Kavala* or *Skript* -> *Skrytá vášeň*)
- Strip-Bracket Fallback: gracefully recovers from non-existent parenthetical wiki entries by querying the base lemma
- Contextual Domain Blocker: prevents technological and abstract domains from receiving geographic habitat attributes
- Automatic Sliding-Window Quarantine Rotation: enforces a strict 100-record ceiling in `COLNIK-6.x/envoy/quarantine/`, automatically pruning older JSON payloads upon new arrivals

---

## 6. Security & Customs Inspection Layer (COLNÍK 6.x & HitL Safe Trash)
Responsibilities:
- Human-in-the-Loop Safe Trash Pipeline: files flagged for deletion (duplicates, empty directories, corrupted data) are moved to quarantine storage and require explicit user confirmation via `GET /trash`
- TerminalAssistant + TimeCore Security Layer: real-time latency profiling via `cycle_delta()` and command categorization:
  - **FORBIDDEN (0.0s Hard Block):** `format`, `rmdir /s`, `del /f /s /q c:`, `diskpart`, `drop database`, fork-bombs
  - **RISKY (Explicit Prompt Required):** `rm`, `kill`, `taskkill`, `del`
  - **ALLOWED:** `ps`, `top`, `mem`, `sys`, `grep`, `info`, `cat`, `head`, `tail`, `check`, `template`, `python`, `git`, `pip`, `ls`, `dir`, `cd`, `pwd`, `mkdir`, `touch`, `help`
- Terminal State Decoupling: clearing terminal inputs immediately triggers an event asserting `currentModule = "none"`, preventing host shell capture
- Character Encoding Stabilization: multi-stage shell output decoding (UTF-8 → CP1250 → CP852 fallback) ensuring full diacritics integrity

---

## 7. Central Orchestrator, IPC & SafeRollback (`sirius_orchestrator.py` & `safe_rollback.py`)
Responsibilities:
- Single-process lifecycle execution uniting Runtime, IPC Bridge, and background engines
- Native HTTP/WebSocket server running on port 8080 inside `sirius_orchestrator.py`, removing external bridge dependencies
- Deterministic routing and step registration inside `WorkflowEngine5`
- Seamless handoffs: Ingestion → Spellcheck → KG → Reasoning → Professor Middleware → COLNIK → AUTONOMY → UI / OS
- **SafeRollback Resilience:** Granular module-level backup (`shutil.copytree`) and instant restoration (`shutil.rmtree`) for state integrity protection

---

## 8. 4-Panel UI Suite (Port 8080)
Capabilities:
- Integrated browser dashboard on port 8080 (`index.html`)
- Dedicated operational panels: `Duplicates`, `Triage`, `Navigation`, `Terminal`
- Presentation of Professor-validated results with distinct visual indicators for WARN states
- Dynamic language switcher (`SK` / `EN`) binding the transaction context to the target Knowledge Graph
- Safe input clearance: resets `currentModule = "none"` to prevent shell lockups
- Confirmation State Latching: proposal confirmations (`ÁNO / YES`) properly trigger Envoy execution rather than encountering detached states

---

## 9. AUTONOMY 6.x & Self-Repair Layer (v5.9.5)
Capabilities:
- Autonomous proposal and decision evaluations
- Synchronized confirmation pipelines (`kg.learn_proposal`)
- Triage mode for rapid quarantine management (`COLNIK-6.x/triage`)
- Real-time Guard supervision (CPU, RAM, Disk) and duplicate file detection
- Self-Repair integrity scanning and dependency verification

---

# 🧠 SYSTEM INTELLIGENCE LAYER (Runtime 5.9.5)

The intelligence layer enables SIRIUS to:

- understand full compound natural language queries in Slovak and English
- normalize user inputs against typos and diacritic omissions via `spellcheck_engine.py`
- isolate language vocabularies across independent JSON storage backends without cross-lingual leakage
- autonomously deduce biological taxonomy (marsupials -> mammals) and commit verified relations directly to disk
- filter and validate all factual output through the Professor Middleware Layer (PASS / WARN / REJECT)
- execute lossless node mergers (`kg merge`) with zero attribute loss and bi-directional alias links
- accurately query fauna and flora habitats using multi-stem location parsing without misclassifying tree-dwelling animals
- defend the host environment via 0.0s command blocking, non-destructive quarantine trash, and instant SafeRollback recovery

All executed **100% locally and offline**.

---

# 🔌 Module Interconnections (Runtime 5.9.5)

```text
User Query (UI Panel / Web Dashboard on Port 8080)
↓
sirius_orchestrator.py (Single-Process Daemon with Language Header SK / EN)
↓
Token Guard (Entry-Level Sanitization: Blocks @#\$%^&*)
↓
spellcheck_engine.py (Diacritic & Typo Normalizer)
↓
Punctuation Hygiene (.rstrip("?") strips trailing question marks)
↓
Language Context Dispatch:
  • Language == "EN" ──> Bind self.kg = self.kg_en (autosave_kg_en.json)
  • Language == "SK" ──> Bind self.kg = self.kg_sk (autosave_kg.json)
↓
Intent & Pattern Classification:
├─ [Confirmation: ÁNO / YES] ──> Resolve Active Latch ──> Envoy Enrich ──> Atomic Save
├─ [KG Mutation: kg merge / set / relate] ──> Native RuntimeCore Interceptor ──> Atomic Save
├─ [Habitat Query: where does X live?] ──> Resolve Alias ──> Direct Property Output
├─ [Reverse Habitat: what animals live in Y?] ──> Multi-Stem Loc Match (Anti-Flora Guard)
├─ [Verification: is X a Y?] ──> Taxonomical Inference (e.g., Marsupial -> Mammal)
└─ [Entity Lookup: what is X?] ──> Check Target Language KG
     ├─ [Found in KG] ──> Extract Raw Fact Triplets
     │                     ↓
     │           ┌────────────────────────────────────────┐
     │           │       PROFESSOR MIDDLEWARE LAYER       │
     │           │                                        │
     │           │  1. Professor Cleaner (grammar_engine) │
     │           │  2. Professor Validator                │
     │           │     [PASS / WARN / REJECT]             │
     │           │  3. Professor Summarizer               │
     │           └──────────────────┬─────────────────────┘
     │                              │
     │             ┌────────────────┴────────────────┐
     │             ▼                                 ▼
     │       [PASS / WARN]                       [REJECT]
     │             │                                 │
     │             v                                 v
     │      PanelAPI Render                 Quarantined to Triage
     │      to UI V2 Dashboard              & Structured Error Return
     │
     └─ [Missing from KG] ──> Latch Confirmation State ──> Dispatch [ÁNO/NIE] Prompt
                                   ↓
                            User Confirms (ÁNO / YES)
                                   ↓
                            ENVOY Execution Layer 5 (Context Scrape & Anti-Prefix Guard)
                                   ↓
                            ENVOY Normalizer 5 (Contextual Domain & Habitat Filtering)
                                   ↓
                            COLNIK-6.x Quarantine Logging (100-File Sliding Window Ceiling)
                                   ↓
                            Atomic Commit to Language Graph (autosave_kg.json / autosave_kg_en.json)
                                   ↓
                            Pass to Professor Validator Gate
                                   ↓
                            PanelAPI Render to Web Interface

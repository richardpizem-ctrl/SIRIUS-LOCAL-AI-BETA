# 🔄 DATA FLOW & EXECUTION PIPELINE — SIRIUS LOCAL AI (v5.9.5 UNIFIED)
**Status:** ✔ Active & Synchronized  
**Version:** 5.9.5 UNIFIED  
**Author & Architecture Lead:** Richard Pizem  
**Scope:** Deterministic End-to-End Ingestion, Reasoning, Quality Verification & Execution Flow (Port 8080)  

---

## 🎯 Purpose & Core Principle
This document specifies the deterministic data flow pipeline from raw user ingestion to verified UI Panel presentation and persistent atomic commitment to the Knowledge Graph.

The foundational principle of the architecture is strictly enforced:  
> **Runtime Core and symbolic reasoning mechanisms may infer or retrieve any fact from the Knowledge Graph, but the Professor Middleware Layer (Cleaner, Validator PASS/WARN/REJECT, Summarizer) authoritatively determines whether the output is permitted to reach the UI or commit to persistent state.**

The system operates as a single-process daemon on local port **8080** via `sirius_orchestrator.py` with embedded `TerminalAssistant` and `TimeCore`, fully isolated from cloud infrastructure (100% offline).

---

## 🗺️ Architectural Pipeline Diagram

+--------------------------------------------------------+
|       [ USER / UI PANEL (Port 8080) / TERMINAL ]       |
+--------------------------------------------------------+
                           | (Raw User Query / Command)
                           v
+--------------------------------------------------------+
|           1. INGESTION & SANITIZATION LAYER            |
|                                                        |
|  * Token Guard           (Immediate drop of @#$%^&*)   |
|  * spellcheck_engine.py  (Diacritic & Typo Normalizer) |
|  * InputParser5          (Greedy .rstrip("?"),         |
|                           Compound Phrase Extractor)   |
+--------------------------------------------------------+
                           |
                           v
+--------------------------------------------------------+
|       2. ORCHESTRATION & SHELL PROTECTION LAYER        |
|                                                        |
|  * sirius_orchestrator.py (Port 8080 IPC Daemon)       |
|  * Terminal Decoupling    (Reset currentModule="none") |
|  * COLNIK Guard           (0.0s Hard Block format etc.)|
|  * TimeCore Telemetry     (cycle_delta() profiling)    |
|  * Language Context Router(Dynamic SK / EN Partition)  |
+--------------------------------------------------------+
                           |
                           v
+--------------------------------------------------------+
|        3. RUNTIME CORE & REASONING ENGINE 5.9.5        |
|                                                        |
|  * Autosave Stores (autosave_kg.json / _en.json)       |
|  * In-Memory Traversal (get_attributes() standard)     |
|  * Lossless Merge Engine (kg merge <src> into <tgt>)   |
|  * Taxonomical Deduction (KG_VERIFY sub-taxa/mammals)  |
|  * Reverse Location Reasoner (False-Positive Flora G.) |
|  * Multi-Hop / Orbital Inference Engine                |
+--------------------------------------------------------+
                           |
                           | (Raw Facts / Extracted Triplets)
                           v
+--------------------------------------------------------+
|            4. PROFESSOR MIDDLEWARE LAYER               |
|                                                        |
|  1. Professor Cleaner (grammar_engine.py)              |
|     - Predicate normalization (deals with, sa zaoberá)|
|     - Reflexive particle isolation (sa/si into edge)   |
|     - Particle preservation (a, i) / Stopword filter   |
|                                                        |
|  2. Professor Validator (professor_validator.py)       |
|     - PASS   -> 100% Quality, Released to UI           |
|     - WARN   -> Low Confidence, Visual Flag in UI      |
|     - REJECT -> Blocked (INCOMPLETE_FACTS,             |
|                            LOW_CONFIDENCE,             |
|                            CONTRADICTION)              |
|                                                        |
|  3. Professor Summarizer (professor_miner.py)          |
|     - Semantic synthesis of nodes prior to UI render   |
+--------------------------------------------------------+
                           |
                           | (Verified & Filtered Payload)
                           v
+--------------------------------------------------------+
|     5. CUSTOMS CLEARANCE, AUTONOMY & SAFE TRASH        |
|                                                        |
|  * COLNIK-6.x Customs Gate (ALLOW / DENY / TRIAGE)     |
|  * AUTONOMY 6.x (Confirmation State Latching)          |
|  * PanelAPI Prompt Loops ([ÁNO/NIE] / [YES/NO])        |
|  * HitL Safe Trash (Quarantine via GET /trash)         |
|  * Sliding-Window Rotator (100-file ceiling)           |
+--------------------------------------------------------+
                           |
                           v
+--------------------------------------------------------+
|           6. EXECUTE 6.x & DUAL ATOMIC COMMIT          |
|                                                        |
|  * EXECUTE 6.x (Deterministic System Mutations)        |
|  * Dual Atomic Serialization (*.tmp -> atomic rename)  |
|  * Recurrence Suppression (Zero Proposal Recurrence)   |
+--------------------------------------------------------+
                           |
                           v
+--------------------------------------------------------+
|         7. PRESENTATION LAYER (UI PANEL V2)            |
|                                                        |
|  * Duplicates Panel (REPORT_ONLY + Safe Trash routing) |
|  * Triage Panel (Inspection of COLNIK-6.x/triage)      |
|  * Navigation Panel (Orchestrator & KG Health metrics) |
|  * Terminal Panel (Isolated CLI with COLNIK Guard)     |
|  * User Output: Verified cognitive output rendered     |
+--------------------------------------------------------+

---

## 🔍 Detailed Breakdown of Pipeline Phases

### Phase 1: Ingestion, Sanitization & Language Context Routing
1. **Token Guard:**  
   Raw user inputs undergo immediate inspection at runtime entry. Any sequence containing malformed injection symbols (`@`, `#`, `$`, `%`, `^`, `&`, `*`) is dropped before parsing starts.
2. **Pre-Processing Spellcheck (`spellcheck_engine.py`):**  
   Normalizes diacritics and corrects spelling typos, ensuring accent-free queries (e.g., `urologia`) reliably match canonical nodes (e.g., `urológia`).
3. **Semantic Parser (`InputParser5`):**  
   - Strips trailing question marks greedily via `.rstrip("?")` to guarantee exact entity lookup resolution.  
   - Extracts and preserves compound noun phrases (e.g., *ovcia vlna*, *mobilny telefon*, *pevna linka*) without noun-modifier truncation.  
   - Isolates copula verbs (*je*, *sú*, *is*, *are*) from entity subjects to prevent syntactic corruption.
4. **Language Context Router:**  
   Dynamically binds the active execution flow to either the Slovak graph (`autosave_kg.json`) or English graph (`autosave_kg_en.json`) according to UI headers or explicit language context. Cross-lingual mixing is strictly prohibited.

---

### Phase 2: Orchestration, Terminal Decoupling & COLNIK Guard
1. **Single-Process Orchestrator (`sirius_orchestrator.py`):**  
   Hosts the integrated HTTP/WebSocket IPC daemon natively on local port **8080**, eliminating socket collisions and file-locking bottlenecks.
2. **Terminal State Decoupling:**  
   When the user clears the CLI input or cancels an interaction, the UI dispatches an event that immediately resets `currentModule = "none"`, permanently preventing conversational natural language from executing inside the host Windows 11 shell.
3. **COLNIK Guard Shell Filter:**  
   Audits shell invocations before process dispatch:
   - **FORBIDDEN (0.0s Hard Block):** `format`, `diskpart`, `rmdir /s`, `del /f /s /q c:`, `drop database`, fork-bombs.  
   - **RISKY (Explicit Confirmation):** `rm`, `kill`, `taskkill`, `del`.  
   - **ALLOWED:** `ps`, `top`, `mem`, `sys`, `grep`, `dir`, `ls`, `cd`, `pwd`, `python`, `git`, etc.
4. **TimeCore Telemetry:**  
   Measures step latency via `cycle_delta()` while Guard monitors hardware load (< 1% CPU/RAM overhead).

---

### Phase 3: Runtime Core & Symbolic Inference
1. **Knowledge Graph Traversal:**  
   Standardizes attribute access through `self.kg.get_attributes()` and relation queries via `get_relations_outbound()`.
2. **Native Lossless Entity Merge (`kg merge`):**  
   Direct in-memory consolidation relocating all attributes, summaries, and relations from source to target without data loss, establishing a directional alias edge (`src -[alias]-> tgt`).
3. **Taxonomical Category Deduction (`KG_VERIFY`):**  
   Deduces higher-order taxonomic groupings (e.g., marsupials -> mammals) directly from context and commits edges with zero proposal recurrence.
4. **Reverse Location Engine with Anti-Flora Shield:**  
   Executes regional queries (*Austrália*, *Australia*) under the False-Positive Flora Guard, ensuring tree-dwelling fauna (*koala*) are never classified as botanical species.

---

### Phase 4: Professor Middleware Layer (Cognitive Verification Gate)
The authoritative data quality gateway between Runtime Core and UI presentation:

+--------------------------------------------------------+
|                   Runtime Core Facts                   |
+---------------------------+----------------------------+
                            |
                            v
+--------------------------------------------------------+
|          1. Professor Cleaner (grammar_engine.py)      |
|  - Isolates reflexive particles into relation edges    |
|  - Preserves SK conjunctions (a, i) in compound objects|
|  - Filters EN indefinite articles (a, an)              |
+---------------------------+----------------------------+
                            |
                            v
+--------------------------------------------------------+
|         2. Professor Validator (professor_validator)   |
|  - Cognitive consistency & factual integrity check     |
+-------+-------------------+--------------------+-------+
        |                   |                    |
Status: PASS         Status: WARN         Status: REJECT
        v                   v                    v
+---------------+   +---------------+    +-----------------------+
| Released to   |   | Released with |    | Blocked at Core:      |
| UI Panel V2   |   | visual flag   |    | INCOMPLETE_FACTS      |
|               |   | of uncertainty|    | LOW_CONFIDENCE        |
|               |   |               |    | CONTRADICTION         |
+-------+-------+   +-------+-------+    +-----------+-----------+
        |                   |                        |
        v                   v                        v
+-----------------------------------+    +-----------------------+
|  3. Professor Summarizer          |    | Quarantined to:       |
|     (professor_miner.py)          |    | COLNIK-6.x/triage     |
|  - Synthesizes nodes for UI render|    +-----------------------+
+-------------------+---------------+
                    |
                    v
          Dispatched to UI Panel V2

- **Professor Cleaner (`grammar_engine.py`):**  
  Normalizes extracted triplets (`add_relation(source, relation, target)`), handles reflexive verbs (*zaoberá sa*, *deals with*), prevents reflexive particles from attaching to subjects, and preserves grammatical conjunctions.
- **Professor Validator (`professor_validator.py`):**  
  - **PASS:** 100% verified factual integrity. Payload is released to UI.  
  - **WARN:** Facts meet baseline criteria but exhibit lower confidence (`LOW_CONFIDENCE`). Released with a visual uncertainty flag.  
  - **REJECT:** Detects missing attributes (`INCOMPLETE_FACTS`) or contradictory assertions (`CONTRADICTION`). The response is suppressed; a structured error is returned, and the payload is routed to quarantine.
- **Professor Summarizer (`professor_miner.py`):**  
  Synthesizes verified knowledge nodes into a coherent textual summary.

---

### Phase 5: Customs Clearance, Autonomy & Safe Trash
1. **COLNIK-6.x Customs Decision Gate:**  
   Issues deterministic `ALLOW`, `DENY`, or `TRIAGE` verdicts. Malformed mutations or validation failures divert directly into `COLNIK-6.x/triage`.
2. **AUTONOMY 6.x & Confirmation State Latching:**  
   Maintains interactive confirmation context for novel learning proposals across conversation turns until the user answers via `PanelAPI` (`[ÁNO/NIE]` / `[YES/NO]`).
3. **Human-in-the-Loop Safe Trash:**  
   Direct disk unlinking is prohibited. File removal requests divert to `/filesystem/safe_trash_quarantine` awaiting manual inspection via `GET /trash`.
4. **Sliding-Window Quarantine Ceiling:**  
   Automatically prunes the oldest JSON extraction logs in `COLNIK-6.x/envoy/quarantine/` to enforce a strict 100-file ceiling.

---

### Phase 6: Deterministic Execution (EXECUTE 6.x) & Atomic Commit
1. **Action Execution:**  
   `EXECUTE 6.x` carries out authorized operations protected by `safe_rollback.py` (`shutil.copytree` / `shutil.rmtree`).
2. **Dual Atomic Persistence:**  
   Graph mutations are written to temporary shadow files (`*.tmp`) and committed via atomic rename to `autosave_kg.json` or `autosave_kg_en.json`, preventing write corruption.
3. **Zero Proposal Recurrence:**  
   Persisted entities, aliases, and deduced categories are indexed permanently, suppressing redundant future learning proposals.

---

### Phase 7: UI Suite Presentation (Port 8080)
1. **Duplicates Panel:** Displays duplicate scans under a mandatory `REPORT_ONLY` policy, routing proposed cleanups to Safe Trash.  
2. **Triage Panel:** Enables manual inspection, release, or disposal of quarantined items held in `COLNIK-6.x/triage`.  
3. **Navigation Panel:** Provides deterministic switching across runtime modules and monitors system health.  
4. **Terminal Panel:** Decoupled CLI console protected by COLNIK Guard, enforcing `currentModule = "none"` on input clearance.  
5. **Output Rendering:** The UI renders verified responses cleared by the **Professor Middleware Layer**.

---

## 🔐 Security & Data Integrity Policies
- **Professor Gating:** No cognitive output may reach the UI or commit to the Knowledge Graph without clearance by `professor_validator.py`.
- **Destructive Command Defense:** COLNIK Guard executes a 0.0s hard block on dangerous shell routines (`format`, `diskpart`, `rmdir /s`).
- **Safe Deletion Policy:** Permanent unlinking is barred; file deletions route to HitL Safe Trash (`GET /trash`).
- **Terminal State Isolation:** Clearing input immediately resets active execution context to `none` (`currentModule = "none"`).
- **Dual-Language Segregation:** Slovak and English knowledge graphs remain physically and logically isolated.
- **Domain Boundary Shield:** Non-biological entities are strictly prohibited from receiving biological habitat tags.
- **Zero Recurrence Assurance:** Confirmed facts and deduced taxonomies never trigger repetitive user confirmation prompts.

---

## 📌 Document Status
**Version:** 5.9.5 UNIFIED  
**Architect:** Richard Pizem  
This document defines the complete end-to-end data flow, single-process orchestration on port 8080, shell access control via COLNIK Guard, spellcheck pre-processing, quarantine ceiling management, and cognitive quality validation through the **Professor Middleware Layer** (PASS / WARN / REJECT).

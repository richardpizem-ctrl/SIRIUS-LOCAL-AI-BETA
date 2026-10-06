# 🏗 Architecture – SIRIUS LOCAL AI (Runtime 5.9.1 — Dual-Language KG Architecture, Lossless Entity Merge & Comprehensive System Security Protocol)

<p align="center">
  <img src="https://img.shields.io/badge/version-5.9.1--beta-orange">
  <img src="https://img.shields.io/badge/license-SUL--3.2.0-green">
  <img src="https://img.shields.io/badge/platform-Windows%2011-blue">
  <img src="https://img.shields.io/badge/runtime-SIRIUS%20Runtime%205.9.1-red">
  <img src="https://img.shields.io/badge/local%20AI-100%25-blueviolet">
</p>

The SIRIUS LOCAL AI Runtime **5.9.1** represents an enterprise-grade, deterministic architecture built on top of:

- Dual-Language Knowledge Graph Architecture (`autosave_kg.json` for SK and `autosave_kg_en.json` for EN)
- Native Lossless Entity Merge Engine (`kg merge <src> into <tgt>`) integrated directly inside `RuntimeCore`[cite: 1, 2]
- Ontological & Taxonomical Reasoning Engine (`KG_VERIFY`) with hierarchical mammalian category deduction[cite: 1, 2]
- Resilient Reverse Location Querying (`_execute_reverse_location_query`) with anti-flora classification guard[cite: 1, 2]
- Greedy Trailing Punctuation Sanitization (`.rstrip("?")`) preventing key matching failures[cite: 1, 2]
- Confirmation State Latching preserving pending proposal context across interactive turns[cite: 1, 2]
- Hard Token Guard blocking corrupted and malicious input character sequences (`@#$%^&*`)[cite: 2, 3]
- Automatic Envoy Quarantine Sliding Window enforcing a 100-file ceiling[cite: 2, 3]
- TerminalAssistant + TimeCore Security Layer with 0.0s hard blocking of forbidden commands (`format`, `diskpart`)[cite: 2, 3]
- Safe UI Trash & Human-in-the-Loop (HitL) verification isolating file removals without direct disk deletion[cite: 2, 3]
- Single-Process IPC Bridge running natively on port 8080 inside `sirius_orchestrator.py`[cite: 1, 3]
- Multi-Word Compound Parser (`InputParser5` preserving full noun phrases)[cite: 1]
- Central Execution Loop powered by `sirius_orchestrator.py` with dual-graph atomic serialization[cite: 1, 2]

This is the **current operational architecture** of SIRIUS LOCAL AI.

---

# 🧩 Architectural Principles (Runtime 5.9.1)

- Dual-Language Knowledge Graph Isolation (physical and logical partition of SK and EN graphs)[cite: 1, 2]
- Native In-Memory Entity Consolidation (lossless property migration with bidirectional alias formation)[cite: 1, 2]
- Taxonomical Inference without Recurrence (sub-taxa automatically deduced and auto-committed to KG)[cite: 1, 2]
- Non-Destructive Habitat Traversal (uniform attribute retrieval via `self.kg.get_attributes()`)[cite: 1, 2]
- Unified Semantic Pipeline (InputParser5 → Token Guard → Contextual KG → Reasoning → ENVOY → COLNIK → AUTONOMY)
- Deterministic Execution Loop driven centrally by `sirius_orchestrator.py`[cite: 1]
- Compound Phrase Integrity (no truncation of multi-word modifiers)[cite: 1]
- Autonomous Disambiguation Triage (sub-article pathfinding and parenthetical stripping)[cite: 1]
- Zero-Cloud Guarantee (100% offline, local execution)
- Deterministic IPC Communication on local port 8080 without external process locks[cite: 1, 3]
- Interactive CLI/UI Learning Proposals (`[ÁNO/NIE]` / `[YES/NO]`) with latched state confirmation[cite: 1, 2]
- Customs-Grade Operation Auditing via COLNIK-6.x and AUTONOMY 6.x[cite: 1]
- Human-in-the-Loop Safety Shielding (all file deletions quarantined for explicit UI user approval)[cite: 2, 3]

---

# 🧱 Core Layers (Runtime 5.9.1)

## 1. Input Parsing & Token Hygiene (`InputParser5` & Token Guard)
Responsibilities:
- Immediate rejection of malicious or corrupted inputs (`@`, `#`, `$`, `%`, `^`, `&`, `*`) upon receiving `kg query` commands[cite: 2, 3]
- Greedy trailing punctuation stripping (`.rstrip("?")`) preventing token lookup mismatch (e.g., `CO JE MACROPUS?` cleanly resolves to `macropus`)[cite: 1, 2]
- Extraction of complex compound noun phrases (`ovcia vlna`, `mobilny telefon`, `pevna linka`)[cite: 1]
- Strict isolation of copula verbs (`je`, `sú`, `is`, `are`) from subject entities, preventing query contamination[cite: 1]
- Diacritic normalization and accent-insensitive matching[cite: 1, 2]

---

## 2. Dual-Language Knowledge Graph Architecture (`KnowledgeGraph`)
Responsibilities:
- Complete logical and physical isolation: `autosave_kg.json` (SK) and `autosave_kg_en.json` (EN)[cite: 1, 2]
- Dynamic context switching: `RuntimeCore` automatically binds active queries, attributes, relations, and autosaves according to the active language flag received from the UI (`SK` / `EN`)[cite: 1, 2]
- Native Lossless Entity Merge (`kg merge <src> into <tgt>`): consolidates attributes and transitions source entities into alias nodes with directional graph edges (`src -[alias]-> tgt`)[cite: 1, 2]
- Direct, uniform attribute inspection via `self.kg.get_attributes()` eliminating silent lookup failures[cite: 1, 2]
- Cycle-safe data representation and inbound/outbound edge traversal[cite: 1]
- Atomic dual serialization on shutdown and immediately following external Envoy enrichments[cite: 1, 2]

---

## 3. Ontological & Habitat Reasoning Engine (`ReasoningEngine5` & `KG_VERIFY`)
Capabilities:
- Hierarchical Taxonomical Deduction: deduces higher-order biological categories directly from summary records (e.g., automatically recognizing *marsupials* and *macropods* as mammals without requiring rigid Wikipedia exact matches)[cite: 1, 2]
- Persistent Edge Auto-Commit: verified taxonomical edges (`kangaroo -[is_a]-> mammal`, `macropus -[je]-> cicavec`) are committed directly into the active graph with zero proposal recurrence[cite: 1, 2]
- Non-Destructive Reverse Location Engine (`_execute_reverse_location_query`): multi-stem regional matching supporting inflected geographic forms across both languages (*Austrálii*, *Austrália*, and *Australia*)[cite: 1, 2]
- False-Positive Flora Guard: eliminates naive substring collisions that previously misclassified tree-dwelling animals (*„stromový vačkovec“*) as flora[cite: 1, 2]

Active Rules:
- MultiHopOrbitInferenceRule[cite: 1]
- DedicsnostVlastnostiRule[cite: 1]
- TranzitivneRelacieRule[cite: 1]
- AutoTypeInferenceRule[cite: 1]
- OrbitTypeInferenceRule[cite: 1]

---

## 4. Autonomous ENVOY & Quarantine Layer (`EnvoyExecutionLayer5` & `EnvoyQuarantine5`)
Capabilities:
- Autonomous Disambiguation Triage: detects disambiguation structures (*„môže byť...“*) and resolves specific context targets[cite: 1]
- Anti-Prefix & Phonetic Guard: eliminates invalid prefix matches (e.g., stopping *Káva* -> *Kavala* or *Skript* -> *Skrytá vášeň*)[cite: 1]
- Strip-Bracket Fallback: gracefully recovers from non-existent parenthetical wiki entries by querying the base lemma[cite: 1]
- Contextual Domain Blocker: prevents technological and abstract domains from receiving geographic habitat attributes[cite: 1]
- Automatic Sliding-Window Quarantine Rotation: enforces a strict 100-record ceiling in `COLNIK-6.x/envoy/quarantine/`, automatically pruning older JSON payloads upon new arrivals[cite: 2, 3]

---

## 5. Security & Customs Inspection Layer (COLNÍK 6.x & HitL Safe Trash)
Responsibilities:
- Human-in-the-Loop Safe Trash Pipeline: files flagged for deletion (duplicates, empty directories, corrupted data) are moved to quarantine storage and require explicit user confirmation via `GET /trash`[cite: 2, 3]
- TerminalAssistant + TimeCore Security Layer: real-time latency profiling via `cycle_delta()` and command categorization[cite: 2, 3]:
  - **FORBIDDEN (0.0s Hard Block):** `format`, `rmdir /s`, `del /f /s /q c:`, `diskpart`, `drop database`, fork-bombs[cite: 2, 3]
  - **RISKY (Explicit Prompt Required):** `rm`, `kill`, `taskkill`, `del`[cite: 2, 3]
  - **ALLOWED:** `ps`, `top`, `mem`, `sys`, `grep`, `info`, `cat`, `head`, `tail`, `check`, `template`, `python`, `git`, `pip`, `ls`, `dir`, `cd`, `pwd`, `mkdir`, `touch`, `help`[cite: 2, 3]
- Character Encoding Stabilization: multi-stage shell output decoding (UTF-8 → CP1250 → CP852 fallback) ensuring full diacritics integrity[cite: 2, 3]

---

## 6. Central Orchestrator & Integrated IPC (`sirius_orchestrator.py`)
Responsibilities:
- Single-process lifecycle execution uniting Runtime, IPC Bridge, and background engines[cite: 1, 3]
- Native HTTP/WebSocket server running on port 8080 inside `sirius_orchestrator.py`, removing external bridge dependencies[cite: 1, 3]
- Deterministic routing and step registration inside `WorkflowEngine5`[cite: 1]
- Seamless handoffs: KG → Reasoning → ENVOY → COLNIK → AUTONOMY → UI / OS[cite: 1]

---

## 7. 4-Panel UI Suite & PanelAPI (v5.9.1)
Capabilities:
- Integrated browser dashboard on port 8080 (`index.html`)[cite: 1]
- Dedicated operational panels: `Duplicates`, `Triage`, `Navigation`, `Terminal`[cite: 1]
- Dynamic language switcher (`SK` / `EN`) binding the transaction context to the target Knowledge Graph[cite: 1, 2]
- Safe input clearance: resets `currentModule = "none"` to prevent shell lockups[cite: 1]
- Confirmation State Latching: proposal confirmations (`ÁNO` / `YES`) properly trigger Envoy execution rather than encountering detached states[cite: 1, 2]

---

## 8. AUTONOMY 6.x & Self-Repair Layer (v5.9.1)
Capabilities:
- Autonomous proposal and decision evaluations[cite: 1]
- Synchronized confirmation pipelines (`kg.learn_proposal`)[cite: 1]
- Triage mode for rapid quarantine management (`COLNIK-6.x/triage`)[cite: 1]
- Real-time Guard supervision (CPU, RAM, Disk) and duplicate file detection[cite: 1]
- Self-Repair 5.4 integrity scanning and dependency verification[cite: 1]

---

# 🧠 SYSTEM INTELLIGENCE LAYER (Runtime 5.9.1)

The intelligence layer enables SIRIUS to:

- understand full compound natural language queries in Slovak and English[cite: 1, 2]
- isolate language vocabularies across independent JSON storage backends without cross-lingual leakage[cite: 1, 2]
- autonomously deduce biological taxonomy (marsupials -> mammals) and commit verified relations directly to disk[cite: 1, 2]
- execute lossless node mergers (`kg merge`) with zero attribute loss and bi-directional alias links[cite: 1, 2]
- accurately query fauna and flora habitats using multi-stem location parsing without misclassifying tree-dwelling animals[cite: 1, 2]
- defend the host environment via 0.0s command blocking and non-destructive quarantine trash[cite: 2, 3]

All executed **100% locally and offline**.

---

# 🔌 Module Interconnections (Runtime 5.9.1)

```text
User Query (UI Panel / Web Dashboard on Port 8080)
↓
sirius_orchestrator.py (Single-Process Daemon with Language Header SK / EN)
↓
Token Guard (Entry-Level Sanitization: Blocks @#$%^&*)
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
     ├─ [Found in KG] ──> Return Clean Knowledge Summary
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
                           PanelAPI Render to Web Interface
                           📌 Document Status
Current version: 5.9.1 (Dual-Language KG Architecture, Lossless Entity Merge & Comprehensive System Security Protocol)

[cite: 1, 2]

This document specifies the operational architecture of SIRIUS LOCAL AI, fully unifying dual-language knowledge graphs, in-memory entity merging, taxonomical inference, HitL quarantine trash, and single-process orchestration[cite: 1, 2, 3].

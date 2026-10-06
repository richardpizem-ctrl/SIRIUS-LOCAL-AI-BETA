# 📜 CHANGELOG — SIRIUS LOCAL AI

## v5.9.1 — Dual-Language KG Architecture + Native Lossless Entity Merge + Taxonomical Habitat Reasoning + COLNÍK Guard Security Protocol (2026‑10‑06)

### 🔥 Major Update
Version 5.9.1 delivers a major architectural advancement focusing on complete bilingual knowledge isolation, native in-memory graph operations, resilient taxonomical inference, and comprehensive security hardening across the SIRIUS / COLNÍK ecosystem.
This release introduces independent, isolated storage backends for Slovak (autosave_kg.json) and English (autosave_kg_en.json), integrates a native lossless entity merge engine (kg merge) directly inside RuntimeCore, implements context-aware mammalian category deduction (KG_VERIFY), repairs reverse habitat querying with non-destructive flora shielding, adds greedy trailing punctuation sanitization, latches proposal confirmation states across interactive turns, and formalizes the complete COLNÍK Guard security layer (featuring Token Guard, sliding-window quarantine rotation, and the Human-in-the-Loop Safe Trash pipeline).

All operations execute 100% offline, orchestrated inside a single-process IPC daemon running natively on port 8080 via sirius_orchestrator.py.

---

### 🌐 Dual-Language Isolated KG Architecture (autosave_kg.json & autosave_kg_en.json)
- Strict Physical & Logical Segregation: Fully separated knowledge graphs for Slovak (autosave_kg.json) and English (autosave_kg_en.json), preventing cross-lingual corruption, mixed-language article summaries, and bilingual entity collisions.
- Dynamic Language Context Dispatch: RuntimeCore automatically binds queries, node retrieval, attribute manipulation, relations, and autosave routines to the exact language selected in the UI Panel (SK / EN).
- Synchronized Dual Autosave: Independent atomic serialization for both linguistic models on runtime shutdown and immediately following external Envoy enrichments.

---

### 🔀 Native Lossless KG Merge Engine (kg merge <src> into <tgt>)
- Direct RuntimeCore Interceptor: Integrated directly into RuntimeCore without external script invocations, brittle file paths, or import dependencies.
- Zero-Loss Attribute Relocation: Migrates all properties, descriptions, alternative summaries, and habitat definitions from the source node directly into the target node.
- Automatic Alias Node Transition: Source entities are preserved as lightweight alias nodes with directional graph edges (src -[alias]-> tgt), enabling seamless bi-directional discovery.

---

### 🧬 Taxonomical & Marsupial Inference (KG_VERIFY)
- Ontological Category Verification: Accurately deduces higher-order biological categories directly from stored text records (e.g., recognizing that marsupials and macropods belong to mammals without requiring rigid exact matches).
- Persistent Edge Auto-Commit: Once verified via Envoy or contextual extraction, taxonomical edges (kangaroo -[is_a]-> mammal, macropus -[je]-> cicavec) are committed directly to the active knowledge graph, resulting in zero confirmation recurrence on repeated queries.

---

### 🌍 Non-Destructive Reverse Location Engine (_execute_reverse_location_query)
- Universal Multi-Stem Regional Matching: Unified location matching supporting inflected geographic forms across both languages (Austrálii, Austrália, and Australia).
- False-Positive Flora Guard: Eliminated naive substring collisions that previously misclassified tree-dwelling animals („stromový vačkovec“) as flora. Koala medvedíkovitá, Macropus, and Krokodíl morský now reliably resolve under Australian fauna.
- Direct Attribute Access: Standardized all graph iterations via self.kg.get_attributes(), eliminating silent lookup failures caused by accessing raw internal dictionaries.

---

### 🔤 Punctuation Hygiene & Confirmation State Latching (InputParser5 & RuntimeCore)
- Greedy Trailing Punctuation Stripping: Sanitizes input strings by trimming trailing question marks (.rstrip("?")), preventing entity lookup failures (e.g., CO JE MACROPUS? cleanly resolves to node macropus).
- Confirmation State Latching: Workflow fallback prompts strictly maintain pending entity identifiers in memory, ensuring affirmative user confirmations (ÁNO, ANO, YES, Y) correctly trigger Envoy execution rather than encountering a detached state.

---

### 🛡️ Comprehensive Security Protocol (COLNÍK Guard & Safe UI Trash)
- Safe UI Trash (Human-in-the-Loop): Files flagged for removal (duplicates, empty folders, damaged files) are never deleted directly from disk; they are quarantined and require manual user approval via GET /trash.
- System File Protection: System configurations, logs, code modules, knowledge graphs (autosave_kg.json, autosave_kg_en.json), and IPC buffers are strictly protected from modification.
- TerminalAssistant & COLNÍK Guard Shell Filter:
  - FORBIDDEN (0.0s Hard Block): format, rmdir /s, del /f /s /q c:, diskpart, drop database, fork-bombs.
  - RISKY (Explicit Prompt Required): rm, kill, taskkill, del.
  - ALLOWED: ps, top, mem, sys, grep, info, cat, head, tail, check, template, python, git, pip, ls, dir, cd, pwd, mkdir, touch, help.
- Token Guard: Entry-level sanitization rejecting corrupted or dangerous symbol sequences (@#$%^&*) on raw input before runtime processing.
- Automatic Sliding-Window Quarantine Rotation: Enforces a strict 100-file ceiling inside COLNIK-6.x/envoy/quarantine/, automatically pruning older JSON payloads upon new arrivals.
- Character Encoding Stabilization: Multi-stage shell output decoding (UTF-8 -> CP1250 -> CP852 fallback) ensuring full diacritics integrity.

---

### ⚙ Execution Command
SIRIUS Runtime 5.9.1 is launched via the central orchestrator:

python sirius_orchestrator.py

---

### 📦 Included in ZIP (SIRIUS-LOCAL-AI-5.9.1.zip)
- Full clean Runtime 5.9.1 codebase (all __pycache__ and compiled .pyc artifacts removed)
- sirius_orchestrator.py with native single-process port 8080 IPC bridge and embedded TerminalAssistant + TimeCore
- Dual knowledge graph stores: autosave_kg.json (SK) and autosave_kg_en.json (EN)
- Native kg merge engine, Token Guard, and sliding-window quarantine rotator
- Enhanced InputParser5, EnvoyExecutionLayer5, and EnvoyNormalizer5
- 4-Panel UI suite assets and browser dashboard (index.html)
- COLNÍK 6.x validation subsystem (Standard, IPC Mode & COLNÍK Guard)
- AUTONOMY 6.x (Control, Guard, Triage Mode & HitL Safe Trash)
- Full symbolic reasoning engine, XAI proof-tree pipeline, and taxonomical inference rules

---

## v5.9.0 — Semantic Multi-Word Parsing + Autonomous Envoy Disambiguation Triage + 4-Panel UI Suite + Multi-Alias KG Persistence (2026‑09‑25)
(Previous version)

## v5.8 — Unified Orchestrator + PanelAPI Loops + TimeCore & Guard Supervision + COLNIK/AUTONOMY IPC (2026‑09‑10)  
(Previous version)

## v5.7.0 — Unified Logic Layer + Stabilized KG Platform + COLNIK‑AUTONOMY Integration  
(Previous version)

## v5.6.2 — Stabilized Logic Layer + Unified KG Platform  
(Previous version)

## v5.5.0 — Unified Reasoning & Explainability Architecture  
(Previous version)

## v5.0.0 — Unified Offline Reasoning Runtime  
(Previous version)

## v4.5.0 PRO — System Intelligence Expansion  
(Previous version)

---
title: SIRIUS LOCAL AI Documentation
layout: default
---

# SIRIUS‑LOCAL‑AI  
**A fully modular, offline‑only AI runtime with unified orchestration (sirius_orchestrator.py on Port 8080 with embedded TerminalAssistant + TimeCore), dual-language isolated KG architecture (autosave_kg.json for SK and autosave_kg_en.json for EN), native lossless entity merge (kg merge), taxonomical & marsupial inference (KG_VERIFY), non-destructive reverse location reasoning, entry-level Token Guard, 100-file sliding-window quarantine rotation, COLNÍK Guard shell access control (0.0s hard blocks), Human-in-the-Loop Safe Trash, multi-word semantic parsing (InputParser5), autonomous disambiguation triage & anti-prefix protection (EnvoyExecutionLayer5), contextual domain shielding (EnvoyNormalizer5), 4-Panel UI Suite (Duplicates, Triage, Navigation, Terminal), interactive PanelAPI [ÁNO/NIE] / [YES/NO] loops, TimeCore & Guard supervision, unified symbolic reasoning, deep explainability (XAI), KG_EXPLAIN & KG_EXPLAIN_DEEP, COLNIK‑6.x (Standard & High-Performance IPC Mode), and AUTONOMY 6.x (Control, Guard & Triage Mode).**

SIRIUS‑LOCAL‑AI is a next‑generation local AI framework designed for **speed, linguistic accuracy, architectural stability, modularity, symbolic intelligence, deep explainability, interactive human-in-the-loop control, and full offline autonomy**.

Version **5.9.1** introduces a decisive upgrade to the SIRIUS Runtime line, deploying independent dual-language knowledge stores, native in-memory entity consolidation, taxonomical category deduction, resilient reverse location querying, input token sanitization, and enterprise-grade command and filesystem protection under COLNÍK Guard.

This release consolidates the runtime architecture with:

- **Single-Process Orchestrator (`sirius_orchestrator.py` on Port 8080 with embedded TerminalAssistant + TimeCore)**  
- **Dual-Language Isolated Knowledge Stores (`autosave_kg.json` for SK and `autosave_kg_en.json` for EN)**  
- **Native Lossless KG Merge Engine (`kg merge <src> into <tgt>`) integrated directly in RuntimeCore**  
- **Taxonomical & Marsupial Inference (`KG_VERIFY`) with zero confirmation recurrence**  
- **Non-Destructive Reverse Location Engine (`_execute_reverse_location_query`) with anti-flora classification guard**  
- **Punctuation Hygiene (`.rstrip("?")`) and Confirmation State Latching**  
- **Hard Token Guard blocking malicious character sequences (`@#$%^&*`) at runtime threshold**  
- **Automated Sliding-Window Quarantine Rotation enforcing a 100-file ceiling**  
- **COLNÍK Guard Shell Access Control (0.0s hard blocking of forbidden commands like `format` and `diskpart`)**  
- **Human-in-the-Loop Safe UI Trash preventing direct unverified disk destruction**  
- **Multi-Word Semantic Engine (`InputParser5` preserving compound noun phrases)**  
- **Autonomous Disambiguation Triage & Anti-Prefix Guard (`EnvoyExecutionLayer5`)**  
- **Contextual Domain Shield & Sentence-Bound Habitat Extractor (`EnvoyNormalizer5`)**  
- **Zero Proposal Recurrence for confirmed semantic entities and inferred taxonomies**  
- **4-Panel UI Suite (`Duplicates`, `Triage`, `Navigation`, `Terminal` with automatic `currentModule = "none"` state clearance)**  
- **Integrated High-Performance IPC Bridge eliminating file locking bottlenecks**  
- **PanelAPI & Interactive [ÁNO/NIE] / [YES/NO] Confirmation Loops**  
- **TimeCore Temporal Tracking (`cycle_delta()`) & Guard Security/Metric Supervision (CPU, RAM, Disk)**  
- **KG_EXPLAIN & KG_EXPLAIN_DEEP (Explainability Engines with Proof Trees)**  
- **Reasoning Engine 5.9.1 (multi‑hop, inheritance, transitivity, orbital & taxonomical rules)**  
- **Workflow Engine 5.9.1 (deterministic multi-stage execution)**  
- **COLNIK‑6.x validation subsystem (Standard & High-Performance IPC Mode)**  
- **AUTONOMY 6.x (Control, Guard, Triage Mode & HitL Trash Governance)**  
- **Identity Engine 3.1 & SECURITY FAMILY 5.x**  
- **Zero cloud reliance — 100% offline, private local processing**  

---

## 📌 Table of Contents
- [Architecture](ARCHITECTURE.md)
- [Module Map](MODULE_MAP.md)
- [Styleguide](STYLEGUIDE.md)
- [Testing Guide](TESTING_GUIDE.md)
- [Performance Guide](PERFORMANCE_GUIDE.md)
- [Release Notes](RELEASE_NOTES.md)
- [Roadmap](ROADMAP.md)
- [Security Family](SECURITY_FAMILY.md)
- [AITE 5.9.1](AITE.md)
- [ENVOY 5](ENVOY_TUTORIAL.md)
- [Contributing](CONTRIBUTING.md)
- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Password Vault 5.0](PASSWORD_VAULT.md)

---

## 🚀 Key Features (v5.9.1 UNIFIED)

### **Dual-Language Isolated KG Architecture (`autosave_kg.json` & `autosave_kg_en.json`)**
Physical and logical segregation of knowledge domains:
- strict separation between Slovak (`autosave_kg.json`) and English (`autosave_kg_en.json`) knowledge graphs, preventing bilingual query collisions, mixed summaries, and hallucinated translations
- dynamic context dispatching: `RuntimeCore` binds queries, node retrieval, attributes, and relations dynamically based on the active UI language flag (`SK` / `EN`)
- independent atomic autosaves on runtime shutdown or post-enrichment

---

### **Native Lossless Entity Merge (`kg merge`)**
Direct in-memory entity consolidation:
- executed natively inside `RuntimeCore` without external script invocations or missing import paths
- lossless attribute relocation: moves properties, summaries, and habitat notes from source to target
- automatic alias transition: preserves source entities as lightweight alias nodes (`src -[alias]-> tgt`) enabling bi-directional traversal

---

### **Taxonomical Category Deduction & Reverse Habitat Engine**
Deterministic biological inference:
- **Taxonomical Inference (`KG_VERIFY`):** deduces higher-order biological categories directly from stored text records (recognizing marsupials and macropods as mammals) and auto-commits relations with zero prompt recurrence
- **Reverse Habitat Engine (`_execute_reverse_location_query`):** supports inflected geographic terms across both languages (*Austrálii*, *Austrália*, *Australia*)
- **False-Positive Flora Guard:** prevents tree-dwelling animals (*„stromový vačkovec“*) from being misclassified as plants, reliably resolving *Koala*, *Macropus*, and *Krokodíl morský* as Australian fauna
- **Direct Attribute Access:** uniform attribute iteration via `self.kg.get_attributes()` eliminating silent lookup failures

---

### **Comprehensive Security Protocol (COLNÍK Guard & HitL Safe Trash)**
Multi-tiered local protection:
- **Human-in-the-Loop Safe UI Trash:** file deletions (duplicates, empty folders) are quarantined; direct unverified file destruction is blocked, requiring explicit approval via `GET /trash`
- **COLNÍK Guard Shell Filter:** 0.0s hard blocking of forbidden commands (`format`, `rmdir /s`, `del /f /s /q c:`, `diskpart`, `drop database`), prompt checks for risky commands, and safe execution for telemetry (`mem`, `ps`, `sys`)
- **Token Guard:** sanitizes raw input at runtime threshold, blocking corrupted or malicious injection strings (`@#$%^&*`)
- **Sliding-Window Quarantine Rotation:** maintains an automatic 100-file ceiling inside `COLNIK-6.x/envoy/quarantine/`
- **Character Encoding Stabilization:** multi-stage shell decoding (UTF-8 -> CP1250 -> CP852 fallback) ensuring full diacritics integrity

---

### **Punctuation Hygiene & Confirmation State Latching**
Resilient conversational flow:
- greedy trailing punctuation stripping (`.rstrip("?")`) prevents entity lookup mismatch (e.g., `CO JE MACROPUS?` cleanly resolves to node `macropus`)
- confirmation state latching preserves pending proposal identifiers in memory across interactive turns, ensuring affirmative replies (`ÁNO` / `YES`) reliably trigger Envoy execution

---

### **Multi-Word Semantic Understanding (`InputParser5`)**
Extracts natural language concepts in their complete grammatical form:
- native preservation of compound noun phrases (e.g., `ovcia vlna`, `mobilny telefon`, `pevna linka`) without truncating modifiers down to isolated single tokens
- complete isolation of copula verbs (`je`, `sú`, `is`, `are`) from subject entities, preventing linguistic corruptions
- diacritic-aware normalization producing clean entities for graph lookup and external triage

---

### **Autonomous Envoy Disambiguation & Domain Shielding**
Autonomous encyclopedic research under strict semantic boundaries:
- **Autonomous Disambiguation Triage:** automatically detects Wikipedia disambiguation pages (*„môže byť...“*) and resolves specific context targets
- **Phonetic & Anti-Prefix Guard:** eliminates prefix over-matching anomalies (stops query drift like *Káva* -> *Kavala* or *Skript* -> telenovelas)
- **Strip-Bracket Fallback:** recovers gracefully from non-existent parenthetical wiki entries by querying base lemmas
- **Contextual Domain Blocker:** prevents abstract, technical, or formal disciplines (*ekológia*, *architektúra*, *fyzika*) from receiving inaccurate geographic habitat metadata

---

### **4-Panel UI Suite & Terminal State Decoupling**
A unified web interface running locally on port 8080:
- **Duplicates Panel:** monitors live system metrics and categorizes file duplicates into safe vs. critical buckets
- **Triage Panel:** live supervision of quarantine queues and unclassified files (`COLNIK-6.x/triage`)
- **Navigation Panel:** deterministic module switching across Runtime, KG, Envoy, and Autonomy
- **Terminal Panel:** permanent decoupling preventing shell capture by automatically resetting `currentModule = "none"` when clearing input

---

### **Unified Orchestration & Supervision**
Single-process control driven by `sirius_orchestrator.py`:
- centralized execution pipeline coordinating runtime core, IPC daemon, and UI loops on port 8080
- TimeCore temporal tracking (`cycle_delta()`) and heartbeat monitoring
- Guard security supervision actively auditing CPU, RAM, and Disk metrics
- COLNIK‑6.x Customs validation (Standard & High-Performance IPC Mode)
- AUTONOMY 6.x proposal governance and Triage Mode

---

### **Symbolic Reasoning & Deep Explainability (XAI)**
Auditable symbolic deduction without statistical black boxes:
- rule chaining: `MultiHopOrbitInferenceRule`, `DedicsnostVlastnostiRule`, `TranzitivneRelacieRule`, `AutoTypeInferenceRule`
- hierarchical proof trees and evidence tree generation (ASCII + HTML)
- confidence scoring and explainability routing via `KG_EXPLAIN` & `KG_EXPLAIN_DEEP`

---

## 📁 Project Structure (v5.9.1)

src/  
├── commands/  
├── context/  
├── envoy/  
│   ├── envoy_execution_layer_5.py  
│   ├── envoy_normalizer_5.py  
│   └── envoy_quarantine_5.py  
├── filesystem/  
├── knowledge_packs/  
├── runtime/  
│   ├── input_parser_5.py  
│   └── runtime_core.py  
├── orchestrator/  
│   └── sirius_orchestrator.py  
├── panel_api/  
├── supervision/  
│   ├── time_core.py  
│   └── guard.py  
├── colnik/  
│   ├── triage/  
│   └── colnik_guard.py  
├── autonomy/  
│   ├── autonomy.py  
│   └── triage_mode.py  
├── security_family/  
├── self_repair/  
├── triage/  
├── ui/  
│   └── index.html  
├── workflow/  
├── autosave_kg.json  
├── autosave_kg_en.json  
└── sirius.py  

Each directory maintains explicit modular boundaries described in **MODULE_MAP.md**.

---

## 🧪 Testing
The project incorporates comprehensive offline test suites:

- dual-language graph isolation and context dispatch tests  
- native `kg merge` attribute retention and alias link tests  
- taxonomical inference (`KG_VERIFY`) and auto-commit tests  
- reverse habitat query and anti-flora classification guard tests  
- trailing punctuation trimming and confirmation state latching tests  
- Token Guard raw input sanitization tests  
- sliding-window quarantine rotation (100-record ceiling) tests  
- COLNÍK Guard 0.0s command blocking and telemetry tests  
- Human-in-the-Loop Safe Trash quarantine tests  
- multi-word compound noun phrase extraction tests  
- disambiguation resolution and strip-bracket fallback tests  
- non-bio domain shielding and habitat filtering tests  
- 4-Panel UI state reset and terminal decoupling tests  
- COLNIK-6.x high-performance IPC handshake tests  
- AUTONOMY 6.x proposal and confirmation loop tests  
- Guard resource scanning and TimeCore timing tests  
- symbolic reasoning rule chaining and proof tree validation tests  
- SECURITY FAMILY 5.x identity-gating tests  

Details are maintained in **TESTING_GUIDE.md**.

---

## ⚙️ Performance
Optimized for high-efficiency local execution:

- zero external API latency (100% offline-first)  
- single-process HTTP/IPC daemon running natively on port 8080 without disk file contention  
- instant memory resolution for dual-language graph queries  
- lightweight, non-blocking asynchronous UI loops  
- deterministic symbolic deduction with predictable memory footprints  

Further metrics are available in **PERFORMANCE_GUIDE.md**.

---

## 🗓️ Release Plan

### **v5.9.1 – Dual-Language KG Architecture, Lossless Entity Merge & Comprehensive System Security Protocol (Current)**  
- Dual-Language Isolated Knowledge Stores (`autosave_kg.json` & `autosave_kg_en.json`)  
- Native Lossless KG Merge Engine (`kg merge <src> into <tgt>`)  
- Taxonomical Category Deduction (`KG_VERIFY`) with edge auto-commit  
- Non-Destructive Reverse Location Engine with anti-flora guard  
- Punctuation Hygiene (`.rstrip("?")`) & Confirmation State Latching  
- Entry-Level Token Guard & 100-File Sliding-Window Quarantine Rotation  
- COLNÍK Guard Shell Access Control (0.0s block on forbidden commands)  
- Human-in-the-Loop Safe Trash Pipeline  
- Single-Process Orchestrator (`sirius_orchestrator.py` on Port 8080 with embedded TerminalAssistant + TimeCore)  
- Multi-Word Compound Parser (`InputParser5`)  
- Autonomous Disambiguation Triage & Anti-Prefix Guard (`EnvoyExecutionLayer5`)  
- Contextual Domain Shield & Habitat Filtering (`EnvoyNormalizer5`)  
- 4-Panel UI Suite (`Duplicates`, `Triage`, `Navigation`, `Terminal`) with automatic state release  
- COLNIK‑6.x High-Performance IPC & AUTONOMY 6.x Control/Triage Mode  
- Guard System Resource Supervision & TimeCore Heartbeat  

---

## 🧩 License
The project is licensed under the **SIRIUS Unified License (SUL-3.2.0)**.

---

## ✨ Author
**Richard Pizem**  
Lead architect & solo maintainer  
SIRIUS‑LOCAL‑AI

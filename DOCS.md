---
title: SIRIUS LOCAL AI Documentation
layout: default
---

# SIRIUS‑LOCAL‑AI  
**A fully modular, offline‑only AI runtime with unified orchestration (sirius_orchestrator.py on Port 8080), multi-word semantic parsing (InputParser5), autonomous disambiguation triage & anti-prefix protection (EnvoyExecutionLayer5), contextual domain shielding (EnvoyNormalizer5), multi-alias KG persistence (autosave_kg.json), 4-Panel UI Suite (Duplicates, Triage, Navigation, Terminal), interactive PanelAPI [ÁNO/NIE] loops, TimeCore & Guard supervision, unified symbolic reasoning, deep explainability (XAI), KG_EXPLAIN & KG_EXPLAIN_DEEP, COLNIK‑6.x (Standard & High-Performance IPC Mode), and AUTONOMY 6.x (Control, Guard & Triage Mode).**

SIRIUS‑LOCAL‑AI is a next‑generation local AI framework designed for **speed, linguistic accuracy, architectural stability, modularity, symbolic intelligence, deep explainability, interactive human-in-the-loop control, and full offline autonomy**.

Version **5.9.0** introduces a decisive upgrade to the SIRIUS Runtime line, advancing compound noun phrase understanding, encyclopedic web triage, permanent elimination of interactive proposal loops, and total decoupling of the UI terminal interface.

This release consolidates the runtime architecture with:

- **Single-Process Orchestrator (`sirius_orchestrator.py` on Port 8080)**  
- **Multi-Word Semantic Engine (`InputParser5` preserving compound noun phrases)**  
- **Autonomous Disambiguation Triage & Anti-Prefix Guard (`EnvoyExecutionLayer5`)**  
- **Contextual Domain Shield & Sentence-Bound Habitat Extractor (`EnvoyNormalizer5`)**  
- **Multi-Alias Knowledge Graph Persistence with Dual-Key Mapping (`autosave_kg.json`)**  
- **Zero Proposal Recurrence for confirmed semantic entities**  
- **4-Panel UI Suite (`Duplicates`, `Triage`, `Navigation`, `Terminal` with automatic `currentModule = "none"` state clearance)**  
- **Integrated High-Performance IPC Bridge eliminating file locking bottlenecks**  
- **PanelAPI & Interactive [ÁNO/NIE] Confirmation Loops**  
- **TimeCore Temporal Tracking & Guard Security/Metric Supervision (CPU, RAM, Disk)**  
- **KG_EXPLAIN & KG_EXPLAIN_DEEP (Explainability Engines with Proof Trees)**  
- **Reasoning Engine 5.9.0 (multi‑hop, inheritance, transitivity, orbital rules)**  
- **Workflow Engine 5.9.0 (deterministic multi-stage execution)**  
- **COLNIK‑6.x validation subsystem (Standard & High-Performance IPC Mode)**  
- **AUTONOMY 6.x (Control, Guard & Triage Mode in `COLNIK-6.x/triage`)**  
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
- [AITE 5.9.0](AITE.md)
- [ENVOY 5](ENVOY_TUTORIAL.md)
- [Contributing](CONTRIBUTING.md)
- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Password Vault 5.0](PASSWORD_VAULT.md)

---

## 🚀 Key Features (v5.9.0 UNIFIED)

### **Multi-Word Semantic Understanding (`InputParser5`)**
Extracts natural language concepts in their complete grammatical form:
- native preservation of compound noun phrases (e.g., `ovcia vlna`, `mobilny telefon`, `pevna linka`) without truncating modifiers down to isolated single tokens
- complete isolation of copula verbs (`je`, `sú`) from subject entities, preventing linguistic corruptions (e.g., `jeovcia vlna`)
- diacritic-aware normalization producing clean entities for graph lookup and external triage

---

### **Autonomous Envoy Disambiguation & Domain Shielding**
Autonomous encyclopedic research under strict semantic boundaries:
- **Autonomous Disambiguation Triage:** automatically detects Wikipedia disambiguation pages (*„môže byť...“*) and resolves specific context targets (e.g., categorizing `slon` into genus *Elephas*)
- **Phonetic & Anti-Prefix Guard:** eliminates prefix over-matching anomalies (stops query drift like *Káva* -> *Kavala* or *Skript* -> telenovelas)
- **Strip-Bracket Fallback:** recovers gracefully from non-existent parenthetical wiki entries by querying base lemmas
- **Contextual Domain Blocker:** prevents abstract, technical, or formal disciplines (*ekológia*, *architektúra*, *fyzika*) from receiving inaccurate geographic habitat metadata

---

### **Multi-Alias KG Persistence & Zero Recurrence**
A deterministic, self-enriching Knowledge Graph platform:
- dual-key commitment: stores entities under both queried phrases and official encyclopedic titles
- atomic serialization into `autosave_kg.json`
- permanent elimination of interactive proposal loops: once confirmed via `[ÁNO/NIE]`, subsequent requests are served instantly from graph memory

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
- centralized execution pipeline coordinating runtime core, IPC daemon, and UI loops
- TimeCore temporal tracking and heartbeat monitoring
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

## 📁 Project Structure (v5.9.0)

src/  
├── commands/  
├── context/  
├── envoy/  
│   ├── envoy_execution_layer_5.py  
│   └── envoy_normalizer_5.py  
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
│   └── triage/  
├── autonomy/  
│   ├── autonomy.py  
│   └── triage_mode.py  
├── security_family/  
├── self_repair/  
├── triage/  
├── ui/  
│   └── index.html  
├── workflow/  
└── sirius.py  

Each directory maintains explicit modular boundaries described in **MODULE_MAP.md**.

---

## 🧪 Testing
The project incorporates comprehensive offline test suites:

- multi-word compound noun phrase extraction tests  
- disambiguation resolution and strip-bracket fallback tests  
- non-bio domain shielding and habitat filtering tests  
- multi-alias graph persistence and zero-recurrence verification tests  
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
- instant memory resolution for multi-alias graph queries  
- lightweight, non-blocking asynchronous UI loops  
- deterministic symbolic deduction with predictable memory footprints  

Further metrics are available in **PERFORMANCE_GUIDE.md**.

---

## 🗓️ Release Plan

### **v5.9.0 – Semantic Multi-Word Parsing, Disambiguation Triage & 4-Panel UI Suite (Current)**  
- Single-Process Orchestrator (`sirius_orchestrator.py` on Port 8080)  
- Multi-Word Compound Parser (`InputParser5`)  
- Autonomous Disambiguation Triage & Anti-Prefix Guard (`EnvoyExecutionLayer5`)  
- Contextual Domain Shield & Habitat Filtering (`EnvoyNormalizer5`)  
- Multi-Alias Graph Persistence (`autosave_kg.json`)  
- 4-Panel UI Suite (`Duplicates`, `Triage`, `Navigation`, `Terminal`) with automatic state release  
- COLNIK‑6.x High-Performance IPC & AUTONOMY 6.x Control/Triage Mode  
- Guard System Resource Supervision & TimeCore Heartbeat  

---

## 🧩 License
The project is open‑source and available to the community under the **MIT License**.

---

## ✨ Author
**Richard Pizem**  
Lead architect & solo maintainer  
SIRIUS‑LOCAL‑AI

# 🏗 Architecture – SIRIUS LOCAL AI (Runtime 5.9.0 — Semantic Multi-Word & Disambiguation Triage)

<p align="center">
  <img src="https://img.shields.io/badge/version-5.9.0-active--dev-orange">
  <img src="https://img.shields.io/badge/license-MIT-green">
  <img src="https://img.shields.io/badge/platform-Windows%2011-blue">
  <img src="https://img.shields.io/badge/runtime-SIRIUS%20Runtime%205.9.0-red">
  <img src="https://img.shields.io/badge/local%20AI-100%25-blueviolet">
</p>

The SIRIUS LOCAL AI Runtime **5.9.0** is the enhanced, semantically precise architecture built on top of:

- Multi-Word Compound Parser (`InputParser5` preserving full noun phrases)
- Autonomous Encyclopedic Disambiguation Triage & Anti-Prefix Guard
- Contextual Domain Filtering (`EnvoyNormalizer5` with strict non-biological shielding)
- Multi-Alias Graph Persistence with Dual-Key Mapping (`autosave_kg.json`)
- Integrated Single-Process IPC Bridge running natively on port 8080
- Complete 4-Panel UI Suite (`Duplicates`, `Triage`, `Navigation`, `Terminal` with deterministic state cleanup)
- Unified Knowledge Graph Core (Unified Schema & Cycle-Safe Architecture)
- Deep Explainability Framework (Hierarchical proof trees, rule attribution)
- Multi-hop Symbolic Reasoning Engine (`ReasoningEngine5`)
- Central Execution Loop powered by `sirius_orchestrator.py`
- Interactive Learning Loops with `[ÁNO/NIE]` confirmation prompts
- TimeCore Heartbeat & Guard System Metrics Supervision
- Dual-Mode Verification via COLNIK-6.x (Standard & High-Performance IPC) and AUTONOMY-6.x

This is the **current operational architecture** of SIRIUS LOCAL AI.

---

# 🧩 Architectural Principles (Runtime 5.9.0)

- Unified Semantic Pipeline (InputParser5 → KG → Reasoning → ENVOY → COLNIK → AUTONOMY)
- Deterministic Execution Loop driven centrally by `sirius_orchestrator.py`
- Compound Phrase Integrity (no truncation of multi-word modifiers)
- Autonomous Disambiguation Triage (sub-article pathfinding and parenthetical stripping)
- Multi-Alias Graph Storage (eliminating redundant enrichment proposal loops)
- Zero-Cloud Guarantee (100% offline, local execution)
- Domain-Aware Semantic Extraction (protecting abstract and technical disciplines from false habitat attributes)
- Deterministic IPC Communication on local port 8080 without file locks
- Interactive CLI/UI Learning Proposals (`[ÁNO/NIE]`) via PanelAPI
- Customs-Grade Operation Auditing via COLNIK-6.x and AUTONOMY 6.x
- Resilient UI Session Navigation with automatic module resets

---

# 🧱 Core Layers (Runtime 5.9.0)

## 1. Input Parsing & Semantic Hygiene (`InputParser5`)
Responsibilities:
- Extraction of complex compound noun phrases (`ovcia vlna`, `mobilny telefon`, `pevna linka`)
- Isolation of Slovak copula verbs (`je`, `sú`) from subject entities, preventing query contamination
- Diacritic normalization and pre-tokenization for graph querying

---

## 2. Knowledge Graph Layer (Unified Schema & Multi-Alias)
Responsibilities:
- Deterministic graph engine with cycle-safe data representation
- Multi-alias persistence: simultaneously indexing queried phrases and formal encyclopedic titles
- Inbound/outbound traversal and deep semantic relationship mapping
- KG Explore visualization and structured traversal paths
- KG Explain / KG Explain Deep proof-tree extraction
- Reliable atomic serialization and autoload via `autosave_kg.json`

---

## 3. Autonomous ENVOY & Triage Layer (`EnvoyExecutionLayer5` & `EnvoyNormalizer5`)
Capabilities:
- Autonomous Disambiguation Triage: detects disambiguation structures (*„môže byť...“*) and resolves specific context targets (e.g., resolving `slon` directly to genus *Elephas*)
- Anti-Prefix & Phonetic Guard: eliminates invalid prefix matches (e.g., stopping *Káva* -> *Kavala* or *Skript* -> *Skrytá vášeň*)
- Strip-Bracket Fallback: gracefully recovers from non-existent parenthetical wiki entries by querying the base lemma
- Contextual Domain Blocker: prevents technological and abstract domains from receiving geographic habitat attributes
- Sentence-Bound Habitat Extraction: strictly requires explicit habitat predicate verbs

---

## 4. Reasoning Engine 5.x (v5.9.0)
Capabilities:
- Deterministic rule chaining and multi-hop deduction
- Property inheritance and transitive category reasoning
- Proof tree generation (ASCII + HTML) and evidence tree logging
- Confidence scoring and explanation tracking

Active Rules:
- MultiHopOrbitInferenceRule
- DedicsnostVlastnostiRule
- TranzitivneRelacieRule
- AutoTypeInferenceRule
- OrbitTypeInferenceRule

---

## 5. Central Orchestrator & Workflow Engine (`sirius_orchestrator.py`)
Responsibilities:
- Single-process lifecycle execution uniting Runtime, IPC Bridge, and background engines
- Deterministic routing and step registration inside `WorkflowEngine5`
- Seamless handoffs: KG → Reasoning → ENVOY → COLNIK → AUTONOMY → UI / OS
- Integrated HTTP/WebSocket listener running on local port 8080

---

## 6. COLNIK‑6.x Validation Layer (Standard & IPC Mode)
Responsibilities:
- Customs-style inspection of all graph operations before storage mutation
- Workflow step authorization and anomaly filtering
- Malformed mutation interception and enterprise consistency enforcement
- High-performance IPC synchronization with AUTONOMY-6.x

---

## 7. AUTONOMY 6.x (Control, Guard & Triage Mode)
Capabilities:
- Autonomous proposal and decision evaluations
- Synchronized confirmation pipelines (`kg.learn_proposal`)
- Triage mode for rapid quarantine management (`COLNIK-6.x/triage`)
- Real-time Guard supervision (CPU, RAM, Disk) and duplicate file detection

---

## 8. 4-Panel UI Suite & PanelAPI (v5.9.0)
Capabilities:
- Integrated browser dashboard on port 8080 (`index.html`)
- Dedicated operational panels: `Duplicates`, `Triage`, `Navigation`, `Terminal`
- Safe input clearance: resets `currentModule = "none"` to prevent shell lockups
- Interactive CLI/UI confirmation loops (`[ÁNO/NIE]`) with immediate UI feedback

---

## 9. Self-Repair & System Agent Layer (v5.9.0)
Capabilities:
- Self-Repair 5.4 integrity scanning and dependency verification
- Rollback-safe recovery and automated consistency validation
- System Agent 5.x for controlled, offline Windows 11 system interactions

---

# 🧠 SYSTEM INTELLIGENCE LAYER (Runtime 5.9.0)

The intelligence layer enables SIRIUS to:

- understand full compound natural language queries
- autonomously resolve encyclopedic ambiguity and disambiguation articles
- diagnose and heal inconsistent knowledge representations
- block invalid cross-domain property inheritance
- explain multi-hop reasoning steps with verifiable evidence trees
- persist confirmed entities under multiple aliases to prevent redundant query loops

All executed **100% locally and offline**.

---

# 🔌 Module Interconnections (Runtime 5.9.0)

User Query (Web UI / Terminal)  
↓  
InputParser5 (Compound Phrase Preservation & Copula Verb Isolation)  
↓  
`sirius_orchestrator.py` (Unified Orchestrator & Native IPC on Port 8080)  
↓  
Knowledge Graph Core (Multi-Alias Lookup)  
├─ [Entity Exists] ──────────────────────────┐  
│                                            ▼  
│                                   Reasoning Engine 5.x  
│                                            ↓  
│                                   WorkflowEngine5 Routing  
│                                            ↓  
│                                   PanelAPI Output Generation  
│  
└─ [Entity Missing]  
        ↓  
   PanelAPI Dispatches Proposal (`[ÁNO/NIE]`)  
        ↓  
   User Confirmation (`ÁNO`)  
        ↓  
   ENVOY Execution Layer 5 (Disambiguation Triage & Anti-Prefix Guard)  
        ↓  
   ENVOY Normalizer 5 (Contextual Domain & Habitat Filtering)  
        ↓  
   COLNIK‑6.x Validation (Customs Inspection & Quarantine Check)  
        ↓  
   AUTONOMY 6.x & Guard Verification  
        ↓  
   RuntimeCore Multi-Alias Commitment (Dual-key save to `autosave_kg.json`)  
        ↓  
   PanelAPI Render to Web Interface  

---

# 📌 Document Status  
Current version: **5.9.0 (Semantic Multi-Word & Disambiguation Triage)**  
This document specifies the *operational architecture* of SIRIUS LOCAL AI, fully unifying multi-word parsing, disambiguation routing, multi-alias persistence, 4-panel UI state safety, and single-process orchestration.

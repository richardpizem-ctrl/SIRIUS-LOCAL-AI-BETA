# SIRIUS‑LOCAL‑AI: Next-Generation Offline AI Runtime & Unified Architecture (v5.9.5)
[![SIRIUS Unified License](https://img.shields.io/badge/License-SUL--3.2.0-blue.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/Python-3.10%2B-green.svg)](https://www.python.org/)
[![Runtime Architecture](https://img.shields.io/badge/Architecture-Unified%20SingleProcess%205.9.5-orange.svg)](ARCHITECTURE.md)
[![Offline First](https://img.shields.io/badge/100%25-Offline--First-success.svg)](README.md)

**SIRIUS‑LOCAL‑AI** is an advanced, enterprise-grade, **100% offline-only artificial intelligence runtime and symbolic reasoning framework** designed for absolute speed, diacritic-safe linguistic accuracy, architectural stability, modular intelligence, deep explainability (XAI), interactive Human-in-the-Loop (HitL) control, and full autonomous local execution without external cloud dependencies or third-party API latency.

---

## 🔍 SEO Meta & Core Search Keywords
* **Primary Keywords:** Offline AI runtime, local LLM orchestrator, symbolic artificial intelligence, dual-language knowledge graph, knowledge graph merge engine, autonomous AI agent, Python offline AI framework, privacy-first AI engine, local vectorless reasoning, XAI hierarchical proof trees.
* **Architecture Tag:** Unified Single-Process Orchestrator (`sirius_orchestrator.py` on Port 8080 with embedded TerminalAssistant + TimeCore).
* **Security Protocol:** COLNÍK Guard (0.0s hard block), Token Guard, SafeRollback crash resilience (`safe_rollback.py`), Professor Validator verification (`professor_validator.py`), and Human-in-the-Loop Safe Trash.
* **Author & Maintainer:** Richard Pizem (Lead Architect & Solo Maintainer, Banská Bystrica, Slovakia).

---

## 🚀 Key Features & Architectural Highlights (v5.9.5)

### 1. Unified Single-Process Orchestration
Driven natively by `sirius_orchestrator.py` executing on local port 8080:
- Centralized deterministic execution pipeline eliminating external file-locking contention and race conditions.
- Integrated high-performance IPC bridge and event loop.
- Real-time synchronization with AUTONOMY-6.x and the 4-Panel UI Suite (`Duplicates`, `Triage`, `Navigation`, `Terminal` with automatic `currentModule = "none"` state clearance).

### 2. Dual-Language Isolated Knowledge Graph Architecture
- Physical and logical separation between Slovak (`autosave_kg.json`) and English (`autosave_kg_en.json`) knowledge bases.
- Native lossless entity merging (`kg merge <src> into <tgt>`) preserving all attributes, relations, and alias pointers in memory.
- Ontological & taxonomical category deduction (`KG_VERIFY`) with zero proposal recurrence on confirmed concepts and inferred sub-taxa.
- Non-destructive reverse location reasoning (`_execute_reverse_location_query`) with anti-flora classification guards.

### 3. Advanced Security & Crash Resilience (COLNÍK Guard & SafeRollback)
- **Token Guard:** Entry-level character sequence sanitization rejecting malicious symbol injections (`@#$%^&*`) instantly.
- **SafeRollback:** Granular module-level state backups (`shutil.copytree`) and instant restorations (`shutil.rmtree`) protecting configuration and database integrity.
- **Professor Validator:** Strict cognitive decision verification matrix (`PASS / WARN / REJECT`) evaluating mutations before disk commit.
- **COLNÍK Guard:** 0.0s hard blocking of destructive shell commands (`format`, `diskpart`, `rmdir /s`, `drop database`).
- **Human-in-the-Loop Safe Trash:** Intercepting file deletions and routing them into quarantine awaiting manual review via `GET /trash`.

### 4. Symbolic Reasoning & Deep Explainability (XAI)
- Deterministic multi-hop inference, property inheritance (`DedicsnostVlastnostiRule`), transitive relations (`TranzitivneRelacieRule`), and orbital reasoning (`MultiHopOrbitInferenceRule`).
- `KG_EXPLAIN` and `KG_EXPLAIN_DEEP` generating multi-layer hierarchical proof trees (ASCII & HTML) for complete auditability.

---

## 📌 Table of Contents & Navigation Map
- [Architecture Overview](ARCHITECTURE.md)
- [Module Map](MODULE_MAP.md)
- [Coding Styleguide](STYLEGUIDE.md)
- [Testing Guide](TESTING_GUIDE.md)
- [Performance Optimization Guide](PERFORMANCE_GUIDE.md)
- [Release Notes](RELEASE_NOTES.md)
- [Roadmap & Version Plan](ROADMAP.md)
- [Security Family & Identity Engine](SECURITY_FAMILY.md)
- [Automatic Input Triage Engine (AITE)](AITE.md)
- [ENVOY Tutorial & Triage Protocol](ENVOY_TUTORIAL.md)
- [Contributing Guidelines](CONTRIBUTING.md)
- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Future Vision](FUTURE_VISION.md)
- [Password Vault 5.0 Reference](PASSWORD_VAULT.md)

---

## 📁 Project Structure (v5.9.5)

```text
src/
├── commands/               # Natural language routing and command execution
├── context/                # Semantic context and state engine
├── core/                   # SafeRollback backup and state protection (safe_rollback.py)
├── professor/              # Professor Validator cognitive verification (professor_validator.py)
├── envoy/                  # ENVOY execution, normalizer, and quarantine layers
├── filesystem/             # Safe file operations and HitL Safe Trash pipeline
├── knowledge_packs/        # Dual-language knowledge stores (autosave_kg.json / autosave_kg_en.json)
├── runtime/                # Runtime Core 5.9.5 and InputParser5
├── orchestrator/           # Unified Single-Process Orchestrator (sirius_orchestrator.py on Port 8080)
├── panel_api/              # Interactive PanelAPI loops ([ÁNO/NIE] / [YES/NO])
├── supervision/            # TimeCore temporal tracking & Guard resource monitoring
├── colnik/                 # COLNIK-6.x customs validation, COLNÍK Guard & triage queue
├── autonomy/               # AUTONOMY 6.x decision engine, Guard supervision & Triage Mode
├── security_family/        # Identity Engine 3.1, time-limits v3, schoolwork engine
├── self_repair/            # Self-Repair Layer 5.8 integrity scanning
├── triage/                 # Automatic Input Triage Engine (AITE 5.9.5)
├── ui/                     # 4-Panel UI dashboard (index.html)
├── workflow/               # Workflow Engine 5.9.5
├── autosave_kg.json        # Isolated Slovak Knowledge Graph Base
├── autosave_kg_en.json     # Isolated English Knowledge Graph Base
└── sirius.py               # Main runtime entry point

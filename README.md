# SIRIUS‑LOCAL‑AI: Next-Generation Offline AI Runtime & Unified Architecture (v5.9.5)

[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/Python-3.10%2B-green.svg)](https://www.python.org/)
[![Runtime Architecture](https://img.shields.io/badge/Architecture-Unified%20SingleProcess%205.9.5-orange.svg)](ARCHITECTURE.md)
[![Status: IN DEVELOPMENT](https://img.shields.io/badge/Status-IN%20DEVELOPMENT-red.svg)](README.md)
[![Offline First](https://img.shields.io/badge/100%25-Offline--First-success.svg)](README.md)

> ⚠️ **WARNING:** This project is currently under active development and integration (**WORK IN PROGRESS / NOT FINISHED**). The system is actively undergoing security hardening with COLNÍK Guard and SafeRollback validation. Use with awareness of ongoing development cycles!

**SIRIUS‑LOCAL‑AI** is an advanced, enterprise-grade, **100% offline-only artificial intelligence runtime and symbolic reasoning framework** designed for absolute speed, diacritic-safe linguistic accuracy, architectural stability, modular intelligence, deep explainability (XAI), interactive Human-in-the-Loop (HitL) control, and full autonomous local execution without external cloud dependencies or third-party API latency.

![SIRIUS LOCAL FUTURISTICKY OBR](SIRIUS%20LOCAL%20FUTURISTICKY%20OBR.png)

![Architecture Diagram](diagram%20(6).png)

---

## ⚡ Quickstart & Installation (ZIP Release)

Follow these steps to set up and run the runtime directly from a release package without requiring Git tooling:

### 1. Download & Extract
1. Navigate to the [Releases](https://github.com/richardpizem/SIRIUS-LOCAL-AI/releases) page.
2. Under the latest build (`v5.9.5`), download the source archive: **`Source code (zip)`**.
3. Extract the ZIP archive into your local workspace directory (e.g., `C:\SIRIUS-LOCAL-AI` or `~/SIRIUS-LOCAL-AI`).

### 2. Environment Setup
Ensure you have **Python 3.10+** installed. Open your terminal in the extracted root directory:

*Windows (PowerShell / Command Prompt):*
```powershell
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
Linux / macOS (Bash):
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
3. Launch Orchestrator
Start the unified runtime and IPC bridge on local port 8080:
python src/sirius_orchestrator.py --port 8080
Once initialized, open your browser and access the interactive 4-Panel UI Suite at http://127.0.0.1:8080.
🔍 SEO Meta & Core Search Keywords
Primary Keywords: Offline AI runtime, local LLM orchestrator, symbolic artificial intelligence, dual-language knowledge graph, knowledge graph merge engine, autonomous AI agent, Python offline AI framework, privacy-first AI engine, local vectorless reasoning, XAI hierarchical proof trees.

Architecture Tag: Unified Single-Process Orchestrator (sirius_orchestrator.py on Port 8080 with embedded TerminalAssistant + TimeCore).

Security Protocol: COLNÍK Guard (0.0s hard block), Token Guard, SafeRollback crash resilience (safe_rollback.py), Professor Validator verification (professor_validator.py), and Human-in-the-Loop Safe Trash.

Author & Maintainer: Richard Pizem (Lead Architect & Solo Maintainer, Banská Bystrica, Slovakia).

🚀 Key Features & Architectural Highlights (v5.9.5)
1. Unified Single-Process Orchestration
Driven natively by sirius_orchestrator.py executing on local port 8080:

Centralized deterministic execution pipeline eliminating external file-locking contention and race conditions.

Integrated high-performance IPC bridge and event loop.

Real-time synchronization with AUTONOMY-6.x and the 4-Panel UI Suite (Duplicates, Triage, Navigation, Terminal with automatic currentModule = "none" state clearance).

2. Dual-Language Isolated Knowledge Graph Architecture
Physical and logical separation between Slovak (autosave_kg.json) and English (autosave_kg_en.json) knowledge bases.

Native lossless entity merging (kg merge <src> into <tgt>) preserving all attributes, relations, and alias pointers in memory.

Ontological & taxonomical category deduction (KG_VERIFY) with zero proposal recurrence on confirmed concepts and inferred sub-taxa.

Non-destructive reverse location reasoning (_execute_reverse_location_query) with anti-flora classification guards.

3. Advanced Security & Crash Resilience (COLNÍK Guard & SafeRollback)
Token Guard: Entry-level character sequence sanitization rejecting malicious symbol injections (@#\$%^&*) instantly.

SafeRollback: Granular module-level state backups (shutil.copytree) and instant restorations (shutil.rmtree) protecting configuration and database integrity.

Professor Validator: Strict cognitive decision verification matrix (PASS / WARN / REJECT) evaluating mutations before disk commit.

COLNÍK Guard: 0.0s hard blocking of destructive shell commands (format, diskpart, rmdir /s, drop database).

Human-in-the-Loop Safe Trash: Intercepting file deletions and routing them into quarantine awaiting manual review via GET /trash.

4. Symbolic Reasoning & Deep Explainability (XAI)
Deterministic multi-hop inference, property inheritance (DedicsnostVlastnostiRule), transitive relations (TranzitivneRelacieRule), and orbital reasoning (MultiHopOrbitInferenceRule).

KG_EXPLAIN and KG_EXPLAIN_DEEP generating multi-layer hierarchical proof trees (ASCII & HTML) for complete auditability.

📌 Table of Contents & Navigation Map
Quickstart & Installation

Architecture Overview

Module Map

Coding Styleguide

Testing Guide

Performance Optimization Guide

Release Notes

Roadmap & Version Plan

Security Family & Identity Engine

Automatic Input Triage Engine (AITE)

ENVOY Tutorial & Triage Protocol

Contributing Guidelines

Code of Conduct

Future Vision

Password Vault 5.0 Reference

📁 Project Structure (v5.9.5)
Plaintext
src/
|-- commands/             # Natural language routing and command execution
|-- context/              # Semantic context and state engine
|-- core/                 # SafeRollback backup and state protection (safe_rollback.py)
|-- professor/            # Professor Validator cognitive verification (professor_validator.py)
|-- envoy/                # ENVOY execution, normalizer, and quarantine layers
|-- filesystem/           # Safe file operations and HitL Safe Trash pipeline
|-- knowledge_packs/      # Dual-language knowledge stores (autosave_kg.json / autosave_kg_en.json)
|-- runtime/              # Runtime Core 5.9.5 and InputParser5
|-- orchestrator/         # Unified Single-Process Orchestrator (sirius_orchestrator.py on Port 8080)
|-- panel_api/            # Interactive PanelAPI loops ([ÁNO/NIE] / [YES/NO])
|-- supervision/          # TimeCore temporal tracking & Guard resource monitoring
|-- colnik/               # COLNIK-6.x customs validation, COLNÍK Guard & triage queue
|-- autonomy/             # AUTONOMY 6.x decision engine, Guard supervision & Triage Mode
|-- security_family/      # Identity Engine 3.1, time-limits v3, schoolwork engine
|-- self_repair/          # Self-Repair Layer 5.8 integrity scanning
|-- triage/               # Automatic Input Triage Engine (AITE 5.9.5)
|-- ui/                   # 4-Panel UI dashboard (index.html)
|-- workflow/             # Workflow Engine 5.9.5
|-- autosave_kg.json      # Isolated Slovak Knowledge Graph Base
|-- autosave_kg_en.json   # Isolated English Knowledge Graph Base
`-- sirius.py             # Main runtime entry point
⚙️ Performance & Optimization Guarantees
Zero External API Latency: 100% offline local execution.

Instant Memory Resolution: O(1) hash-indexed dual-language graph lookups.

Lightweight Asynchronous UI: Non-blocking 4-Panel dashboard on port 8080.

Strict Bounded Inference: Cycle-safe reasoning preventing runaway recursion.

🧩 License & Copyright
The project is open-source and licensed under the MIT License. See the LICENSE file for details.

✨ Author & Lead Architect
Richard Pizem

Lead Architect & Solo Maintainer

SIRIUS‑LOCAL‑AI (Banská Bystrica, Slovakia)

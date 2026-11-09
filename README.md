# 🚀 SIRIUS‑LOCAL‑AI: Next-Generation Offline AI Runtime & Unified Architecture (v6.0.1)

[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/Python-3.10%2B-green.svg)](https://www.python.org/)
[![Runtime Architecture](https://img.shields.io/badge/Architecture-Unified%20SingleProcess%206.0.1-orange.svg)](ARCHITECTURE.md)
[![Status: IN DEVELOPMENT](https://img.shields.io/badge/Status-IN%20DEVELOPMENT-red.svg)](README.md)
[![Offline First](https://img.shields.io/badge/100%25-Offline--First-success.svg)](README.md)

> ⚠️ **WARNING:** This project is currently under active development and integration (**WORK IN PROGRESS / NOT FINISHED**). The system is actively undergoing security hardening with COLNÍK Guard and SafeRollback validation. Use with awareness of ongoing development cycles!

**SIRIUS‑LOCAL‑AI** is an advanced, enterprise-grade, **100% offline-only artificial intelligence runtime and symbolic reasoning framework** designed for absolute speed, diacritic-safe linguistic accuracy, architectural stability, modular intelligence, deep explainability (XAI), interactive Human-in-the-Loop (HitL) control, and full autonomous local execution without external cloud dependencies or third-party API latency.

![SIRIUS LOCAL FUTURISTICKY OBR](SIRIUS%20LOCAL%20FUTURISTICKY%20OBR.png)

![Architecture Diagram](diagram%20(6).png)

---

## ⚠️ Windows Startup Notice / Upozornenie pri spustení vo Windowse

- **EN** — Extract the entire ZIP before running `SiriusOrchestrator.exe`. The executable in this release is unsigned. Depending on your Windows security settings, Windows may display a warning or block it from starting. If Windows blocks SIRIUS, please open a GitHub issue with your Windows version, the ZIP filename, and the exact error message.
- **SK** — Pred spustením `SiriusOrchestrator.exe` rozbaľte celý ZIP. Spustiteľný súbor v tomto vydaní nemá digitálny podpis. Podľa nastavení zabezpečenia môže Windows zobraziť upozornenie alebo zablokovať spustenie. Ak Windows zablokuje SIRIUS, založte prosím GitHub issue a uveďte verziu Windowsu, názov ZIP-u a presnú chybovú hlášku.

---

## ⚡ Quickstart & Installation (ZIP Release)

Follow these steps to set up and run the runtime directly from a release package without requiring Git tooling:

### 1. Download & Extract
1. Navigate to the [Releases](https://github.com/richardpizem/SIRIUS-LOCAL-AI/releases) page.
2. Under the latest build (`v6.0.1`), download the source archive: **`Source code (zip)`**.
3. Extract the ZIP archive into your local workspace directory (e.g., `C:\SIRIUS-LOCAL-AI` or `~/SIRIUS-LOCAL-AI`).

### 2. Environment Setup
Ensure you have **Python 3.10+** installed. Open your terminal in the extracted root directory:

*Windows (PowerShell / Command Prompt):*
    python -m venv venv
    .\venv\Scripts\activate
    pip install -r requirements.txt

*Linux / macOS (Bash):*
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

### 3. Launch Orchestrator
Start the unified runtime and IPC bridge on local port `8080`:

    python src/sirius_orchestrator.py --port 8080

Once initialized, open your browser and access the interactive 4-Panel UI Suite at `http://127.0.0.1:8080`.

---

## 🔍 SEO Meta & Core Search Keywords

- **Primary Keywords:** Offline AI runtime, local LLM orchestrator, symbolic artificial intelligence, dual-language knowledge graph, knowledge graph merge engine, autonomous AI agent, Python offline AI framework, privacy-first AI engine, local vectorless reasoning, XAI hierarchical proof trees.
- **Architecture Tag:** Unified Single-Process Orchestrator (`sirius_orchestrator.py` on Port 8080 with embedded TerminalAssistant + TimeCore).
- **Security Protocol:** COLNÍK Guard (0.0s hard block), Token Guard, SafeRollback crash resilience (`safe_rollback.py`), Professor Validator verification (`professor_validator.py`), and Human-in-the-Loop Safe Trash.
- **Author & Maintainer:** Richard Pizem (Lead Architect & Solo Maintainer, Banská Bystrica, Slovakia).

---

## 🚀 Key Features & Architectural Highlights (v6.0.1)

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

## 📋 What We Changed & Improved

| Area | What We Did | Verified Results |
| :--- | :--- | :--- |
| **Windows EXE & Desktop Startup** | Integrated automatic UI launch, file handling, controlled shutdown, and Knowledge Graph autosave. | `.exe` opened the panel without manual CMD startup. Offline queries (e.g., "Čo je Slnko?") responded successfully. |
| **EXE Content & Data Paths** | Unified working paths for IPC, Trash, and helper KG under `SIRIUS_DATA`. | Verified Runtime 5.x, Autonomy, Colník, Executor, and ENVOY modules inside the package. |
| **Slovak, English & Diacritics** | Verified separated SK/EN graphs and improved diacritics-insensitive search lookup. | Both queries like "CO JE MACKA DOMACA?" and "WHAT IS A ROUTER?" resolved correctly from the local graph. |
| **ENVOY & Permissions** | Fixed policy loading (`policies_envoy.json`) and verified user-consent workflows. | Loaded 5 rules successfully; external web queries correctly triggered explicit consent prompts. |
| **Autonomy → Colník → Executor** | Separated proposal generation from execution and added an optional `--autonomy` scanning mode. | Successfully detected file conflicts (`FILE_CONFLICT`) and processed safe `MOVE` operations via UI approval. |
| **Trash & Recovery** | Added token validation, path checks, SHA-256 verification, and cross-volume file recovery. | Blocked unauthorized requests (HTTP 403) and successfully handled file restore/deletion workflows. |
| **Terminal & Navigation** | Tested basic system commands and panel navigation features. | Command `mem` correctly outputted process stats; system modules opened smoothly. |

---

## 🔍 Filtered & Excluded Behaviors

- **Action Safety:** Autonomy proposals no longer trigger automatic file movements without validation. Trash operations require proper security tokens and pre-execution file integrity checks.
- **IPC Deduplication:** The IPC queue filters out duplicate proposal identifiers, leaving existing pending tasks untouched during empty cycles.

---

## 📌 Table of Contents & Navigation Map

- [Quickstart & Installation](#-quickstart--installation-zip-release)
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

## 📁 Project Structure (v6.0.1)

src/
|-- commands/              # Natural language routing and command execution
|-- context/               # Semantic context and state engine
|-- core/                  # SafeRollback backup and state protection (safe_rollback.py)
|-- professor/             # Professor Validator cognitive verification (professor_validator.py)
|-- envoy/                 # ENVOY execution, normalizer, and quarantine layers
|-- filesystem/            # Safe file operations and HitL Safe Trash pipeline
|-- knowledge_packs/       # Dual-language knowledge stores (autosave_kg.json / autosave_kg_en.json)
|-- runtime/               # Runtime Core 6.0.1 and InputParser5
|-- orchestrator/          # Unified Single-Process Orchestrator (sirius_orchestrator.py on Port 8080)
|-- panel_api/             # Interactive PanelAPI loops ([ÁNO/NIE] / [YES/NO])
|-- supervision/           # TimeCore temporal tracking & Guard resource monitoring
|-- colnik/                # COLNIK-6.x customs validation, COLNÍK Guard & triage queue
|-- autonomy/              # AUTONOMY 6.x decision engine, Guard supervision & Triage Mode
|-- security_family/       # Identity Engine 3.1, time-limits v3, schoolwork engine
|-- self_repair/           # Self-Repair Layer 5.8 integrity scanning
|-- triage/                # Automatic Input Triage Engine (AITE 6.0.1)
|-- ui/                    # 4-Panel UI dashboard (index.html)
|-- workflow/              # Workflow Engine 6.0.1
|-- autosave_kg.json       # Isolated Slovak Knowledge Graph Base
|-- autosave_kg_en.json    # Isolated English Knowledge Graph Base
`-- sirius.py              # Main runtime entry point

---

## ⚙️ Performance & Optimization Guarantees

- **Zero External API Latency:** 100% offline local execution.
- **Instant Memory Resolution:** O(1) hash-indexed dual-language graph lookups.
- **Lightweight Asynchronous UI:** Non-blocking 4-Panel dashboard on port 8080.
- **Strict Bounded Inference:** Cycle-safe reasoning preventing runaway recursion.

---

## 🧩 License & Copyright

The project is open-source and licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## ✨ Author & Lead Architect

**Richard Pizem**  
Lead Architect & Solo Maintainer  
*SIRIUS‑LOCAL‑AI (Banská Bystrica, Slovakia)*

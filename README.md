# 🚀 SIRIUS‑LOCAL‑AI (v6.0.1)

> ⚠️ **WARNING:** This release is a Windows Preview intended for testing. Use with awareness of ongoing development cycles!

SIRIUS LOCAL AI is an offline-first symbolic AI system with separate Slovak and English knowledge graphs. The Windows Preview includes a desktop interface for local knowledge queries, terminal monitoring, and folder navigation. Optional web lookups through ENVOY require user approval.

## Development Status

SIRIUS LOCAL AI BETA will remain at v6.0.1 for an extended period while development focuses on SIRIUS LOCAL AI GAMA. The v6.0.1 Windows Preview remains available for download and testing.

A future milestone is to connect SIRIUS LOCAL AI BETA and SIRIUS LOCAL AI GAMA through ENVOY.

## ⚠️ Windows Startup Notice / Upozornenie pri spustení vo Windowse

* **EN** — Extract the entire ZIP before running `SiriusOrchestrator.exe`. The executable in this release is unsigned. Depending on your Windows security settings, Windows may display a warning or block it from starting. If Windows blocks SIRIUS, please open a GitHub issue with your Windows version, the ZIP filename, and the exact error message.

* **SK** — Pred spustením `SiriusOrchestrator.exe` rozbaľte celý ZIP. Spustiteľný súbor v tomto vydaní nemá digitálny podpis. Podľa nastavení zabezpečenia môže Windows zobraziť upozornenie alebo zablokovať spustenie. Ak Windows zablokuje SIRIUS, založte prosím GitHub issue a uveďte verziu Windowsu, názov ZIP-u a presnú chybovú hlášku.

## ⚡ Quickstart: Windows Preview (Recommended)

To run the pre-compiled standalone version directly on Windows without installing Python or Git:

1. **Download:** Navigate to the [SIRIUS LOCAL AI v6.0.1](https://github.com/richardpizem-ctrl/SIRIUS-LOCAL-AI-BETA/releases/tag/v6.0.1) page and download **`SIRIUS-KG-ALIAS-Windows-x64-REVIEW.zip`**.

2. **Extract:** Extract the entire ZIP archive to your desired location (e.g., `C:\SIRIUS_ARCHIVE`).

3. **Launch:** Open the extracted folder and run **`SiriusOrchestrator.exe`**. The desktop interface will open automatically.

## 💻 Developer Setup: Build from Source

If you prefer to run or contribute directly from the source code repository:

### 1. Clone & Extract Source

Download the source code ZIP from the [SIRIUS LOCAL AI v6.0.1](https://github.com/richardpizem-ctrl/SIRIUS-LOCAL-AI-BETA/releases/tag/v6.0.1) page or clone the repository, then open your terminal in the root directory.

### 2. Environment Setup

Ensure you have **Python 3.10+** installed:

*Windows (PowerShell / Command Prompt):*
python -m venv venv
.\\venv\\Scripts\\activate
pip install -r requirements.txt

*Linux / macOS (Bash):*
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

### 3. Launch Orchestrator

Start the unified runtime and IPC bridge from the root directory:

```
python sirius_orchestrator.py

```

Once initialized, access the interactive 4-Panel UI Suite at `http://127.0.0.1:8080`.

## 🚀 Key Features & Architectural Highlights (v6.0.1)

* **Unified Single-Process Orchestration:** Powered by `sirius_orchestrator.py` on local port 8080 with embedded TerminalAssistant and TimeCore.

* **Dual-Language Isolated Knowledge Graphs:** Separate physical and logical knowledge bases for Slovak (`autosave_kg.json`) and English (`autosave_kg_en.json`).

* **Human-in-the-Loop Controls & Preview Scope:** The downloadable Windows Preview uses `dist_KG_ALIAS` (featuring local knowledge queries, terminal monitoring, and folder browsing). *Note: Advanced Trash token validation and file integrity safeguards were tested separately in `dist_V6_CHECK`.*

## 📋 What We Changed & Improved

| Area | What We Did | Verified Results (Build / Test Context) | 
| ----- | ----- | ----- | 
| **Windows EXE & Desktop Startup** | Integrated automatic UI launch, file handling, controlled shutdown, and Knowledge Graph autosave. | **dist_KG_ALIAS / dist_V6_CHECK:** `.exe` opened the panel without manual CMD startup. Offline queries (e.g., "Čo je Slnko?") and bilingual graph saves completed successfully. | 
| **EXE Content & Data Paths** | Unified working paths for IPC, Trash, and helper KG under `SIRIUS_DATA`. | **dist_V6_CHECK:** Verified Runtime 5.x, Autonomy, Colník, Executor, and ENVOY modules inside the package. | 
| **Slovak, English & Diacritics** | Verified separated SK/EN graphs and improved diacritics-insensitive search lookup. | **dist_KG_ALIAS:** Queries like "CO JE MACKA DOMACA?" and "WHAT IS A ROUTER?" resolved correctly from the local graph. | 
| **ENVOY & Permissions** | Fixed policy loading (`policies_envoy.json`) and verified user-consent workflows. | **dist_ENVOY_POLICY:** Loaded 5 rules successfully; external web queries correctly triggered explicit consent prompts. | 
| **Autonomy → Colník → Executor** | Separated proposal generation from execution and added an optional `--autonomy` scanning mode. | **dist_AUTONOMY_NORMAL / dist_MOVE_UI:** Successfully detected file conflicts (`FILE_CONFLICT`) and processed safe `MOVE` operations via UI approval. | 
| **Trash & Recovery** | Added token validation, path checks, SHA-256 verification, and cross-volume file recovery. | **dist_V6_CHECK:** Blocked unauthorized requests (HTTP 403) and handled file delete/restore workflows. Cross-volume recovery was verified via a *simulated test from source* (`winerror 17`). | 
| **Terminal & Navigation** | Tested basic system commands and panel navigation features. | **dist_KG_ALIAS (Desktop run):** Command `mem` correctly outputted process stats; system modules (Duplicates, Triage, Trash) opened smoothly. | 

## 🔍 Filtered & Excluded Behaviors

* **Action Safety:** Autonomy proposals no longer trigger automatic file movements without validation. Trash operations (tested in `dist_V6_CHECK`) require proper security tokens and pre-execution file integrity checks; the downloadable Windows Preview (`dist_KG_ALIAS`) excludes these newer Trash safeguards.

* **IPC Deduplication:** The IPC queue filters out duplicate proposal identifiers, leaving existing pending tasks untouched during empty cycles.

## 📌 Table of Contents & Navigation Map

* [Quickstart & Installation](#-quickstart-windows-preview-recommended)

* [Architecture Overview](#-architecture-overview-logical-module-mapping)

* [Coding Styleguide](STYLEGUIDE.md)

* [Testing Guide](TESTING_GUIDE.md)

* [Performance Design](#-performance-design)

* [Release Notes](RELEASE_NOTES.md)

* [Security Family & Identity Engine](SECURITY_FAMILY.md)

* [Contributing Guidelines](CONTRIBUTING.md)

## 📁 Architecture Overview (Logical Module Mapping)

*Note: This section outlines the logical module organization and high-level architecture of the runtime components.*

src/
|-- commands/             # Natural language routing and command execution
|-- context/              # Semantic context and state engine
|-- core/                 # SafeRollback backup and state protection (safe_rollback.py)
|-- professor/            # Professor Validator cognitive verification (professor_validator.py)
|-- envoy/                # ENVOY execution, normalizer, and quarantine layers
|-- filesystem/           # Safe file operations and HitL Safe Trash pipeline
|-- knowledge_packs/      # Dual-language knowledge stores (autosave_kg.json / autosave_kg_en.json)
|-- runtime/              # Runtime Core 5.x and InputParser5
|-- orchestrator/         # Unified Single-Process Orchestrator (sirius_orchestrator.py on Port 8080)
|-- panel_api/            # Interactive PanelAPI loops (\[ÁNO/NIE\] / \[YES/NO\])
|-- supervision/          # TimeCore temporal tracking & Guard resource monitoring
|-- colnik/               # COLNIK-6.x customs validation, COLNÍK Guard & triage queue
|-- autonomy/             # AUTONOMY 6.x decision engine, Guard supervision & Triage Mode
|-- security_family/      # Identity Engine 3.1, time-limits v3, schoolwork engine
|-- self_repair/          # Self-Repair Layer 5.8 integrity scanning
|-- triage/               # Automatic Input Triage Engine (AITE 6.0.1)
|-- ui/                   # 4-Panel UI dashboard (index.html)
|-- workflow/             # Workflow Engine 6.0.1
|-- autosave_kg.json        # Isolated Slovak Knowledge Graph Base
|-- autosave_kg_en.json     # Isolated English Knowledge Graph Base
\`-- sirius.py             # Main runtime entry point

## ⚙️ Performance Design

* **Zero External API Latency:** 100% offline local execution (with optional user-approved ENVOY web lookups).

* **Lightweight Asynchronous UI:** Non-blocking 4-Panel dashboard on port 8080.

* **Strict Bounded Inference:** Cycle-safe reasoning preventing runaway recursion.

## 🧩 License & Copyright

The project is open-source and licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## ✨ Author & Lead Architect

**Richard Pizem**

Lead Architect & Solo Maintainer

*SIRIUS‑LOCAL‑AI (Banská Bystrica, Slovakia)*

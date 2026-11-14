🚀 SIRIUS‑LOCAL‑AI (v6.1.0) — Offline Symbolic AI & Clinical Knowledge Engine
> ⚠️ **WARNING:** This release is a Windows Preview intended for testing and evaluation. Use with awareness of ongoing development cycles!
<p align="center">
  <b>SIRIUS LOCAL AI</b> is an advanced offline-first symbolic AI system featuring isolated Slovak and English knowledge graphs, autonomous cognitive reasoning, and specialized clinical sub-modules. Designed for sovereign local execution with zero external cloud dependencies.
</p>
---
🔍 SEO Metadata & Keywords
Primary Keywords: SIRIUS Local AI, offline symbolic AI, knowledge graph, Python AI runtime, Colník Guard, Delta-Medic, Professor reasoning engine, Windows orchestrator, secure local AI, offline medical triage.
Geographic & Project Context: Banská Bystrica, Slovakia | Lead Architect: Richard Pizem.
---
📈 Development Status & Roadmap
SIRIUS LOCAL AI BETA will remain at v6.1.0 for an extended period while active development focuses on SIRIUS LOCAL AI GAMA.
The v6.1.0 Windows Preview remains fully available for download, deployment, and offline testing.
A future milestone is to bridge and connect SIRIUS LOCAL AI BETA and SIRIUS LOCAL AI GAMA through the secure ENVOY execution layer.
---
🧠 Deep-Dive: How the Core Modules Work
1. 🩺 SIRIUS DELTA-MEDIC v1.3.2 Module
The DELTA-MEDIC sub-module is a specialized clinical knowledge and triage engine integrated directly into the offline web UI suite.
Dual Independent Knowledge Graphs: Operates on isolated local databases (`autosave_kg_delta.json` for Slovak medical protocols and `autosave_kg_en_delta.json` for English technical terminology).
Strict Parentheses Enforcement: In the English graph, the Colník Guard validation layer mandates that every technical term strictly includes its Slovak translation in parentheses (e.g., Acute Myocardial Infarction (Akútny infarkt myokardu)) to guarantee 100% bilingual clarity.
Multi-Factor Triage & Simulation: Evaluates severity scores ($1-10$), matches clinical symptoms, and traces relational node dependencies to recommend immediate emergency protocols or routine care pathways.
Secure JSON Import/Sanitization: Features robust pre-import validation that filters schema irregularities, escapes inputs against XSS, and prevents malformed data from disrupting local searches.
2. 🧠 Professor Cognitive Reasoning Engine
The Professor engine (`professor_validator.py`) is the autonomous background reasoning core of SIRIUS.
Idle Batch Processing: While SIRIUS is idle, Professor actively scans both the Slovak and English knowledge graphs in optimized batches.
Symbolic Synthesis: Its inaugural operational rule automatically synthesizes structured explanations (such as detailed analyses regarding biological categories or environmental graphs) directly from explicit graph relationships.
Fact Append & Safe Writes: Automatically appends and saves supporting backing facts alongside the generated narrative. All write operations and graph mutations are rigorously tested and verified on isolated memory copies before committing to storage.
---
🏗️ Architecture & Component Diagram
```text
================================================================================
                    SIRIUS LOCAL AI v6.1.0 — ARCHITECTURE SUITE
================================================================================

  [ User / Desktop EXE ] ---> (SiriusOrchestrator.exe / Port 8080)
                                      |
         +----------------------------+----------------------------+
         |                                                         |
         v                                                         v
  [ 4-Panel UI Suite ]                                    [ Python Runtime 5.x/6.x ]
  - Terminal & Monitoring                                 - Universal InputParser5
  - Knowledge Graphs (SK/EN)                              - Workflow Engine 6.1.0
  - DELTA-MEDIC Clinical UI                               - Self-Repair Layer 5.8
         |                                                         |
         +----------------------------+----------------------------+
                                      |
                                      v
                        [ Security & Governance Layer ]
                        - COLNÍK-6.x Customs & Triage
                        - Colník Guard Schema Validator
                        - IdentityEngine 3.1 & ENVOY Quarantine
                                      |
                                      v
                        [ Autonomous Reasoning Cores ]
                        - Professor Cognitive Validator
                        - Rule Reasoning Engine (RRE)
                        - Isolated Knowledge Graphs (.json)
================================================================================
```
---
⚠️ Windows Startup Notice / Upozornenie pri spustení vo Windowse
EN — Extract the entire ZIP before running `SiriusOrchestrator.exe`. The executable in this release is unsigned. Depending on your Windows security settings, Windows may display a warning or block it from starting. If Windows blocks SIRIUS, please open a GitHub issue with your Windows version, the ZIP filename, and the exact error message.
SK — Pred spustením `SiriusOrchestrator.exe` rozbaľte celý ZIP. Spustiteľný súbor v tomto vydaní nemá digitálny podpis. Podľa nastavení zabezpečenia môže Windows zobraziť upozornenie alebo zablokovať spustenie. Ak Windows zablokuje SIRIUS, založte prosím GitHub issue a uveďte verziu Windowsu, názov ZIP-u a presnú chybovú hlášku.
---
⚡ Quickstart: Windows Preview (Recommended)
To run the pre-compiled standalone version directly on Windows without installing Python or Git:
Download: Navigate to the SIRIUS LOCAL AI v6.1.0 page and download `SIRIUS-KG-ALIAS-Windows-x64-REVIEW.zip`.
Extract: Extract the entire ZIP archive to your desired location (e.g., `C:\SIRIUS_ARCHIVE`).
Launch: Open the extracted folder and run `SiriusOrchestrator.exe`. The desktop interface will open automatically.
---
💻 Developer Setup: Build from Source
If you prefer to run or contribute directly from the source code repository:
1. Clone & Extract Source
Download the source code ZIP from the SIRIUS LOCAL AI v6.1.0 page or clone the repository, then open your terminal in the root directory.
2. Environment Setup
Ensure you have Python 3.10+ installed:
Windows (PowerShell / Command Prompt):
```powershell
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```
Linux / macOS (Bash):
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
3. Launch Orchestrator
Start the unified runtime and IPC bridge from the root directory:
```bash
python sirius_orchestrator.py
```
Once initialized, access the interactive 4-Panel UI Suite at `http://127.0.0.1:8080`.
---
🚀 Key Features & Architectural Highlights (v6.1.0)
Unified Single-Process Orchestration: Powered by `sirius_orchestrator.py` on local port 8080 with embedded TerminalAssistant and TimeCore.
Dual-Language Isolated Knowledge Graphs: Separate physical and logical knowledge bases for Slovak (`autosave_kg.json` / `autosave_kg_delta.json`) and English (`autosave_kg_en.json` / `autosave_kg_en_delta.json`).
Specialized DELTA-MEDIC Sub-Module: Built-in clinical protocol manager and multi-factor triage simulator for emergency and routine medical workflows.
Human-in-the-Loop Controls & Preview Scope: The downloadable Windows Preview uses `dist_KG_ALIAS` (featuring local knowledge queries, terminal monitoring, and folder browsing).
---
📋 What We Changed & Improved in v6.1.0
Area	What We Did	Verified Results (Build / Test Context)
Windows EXE & Desktop Startup	Integrated automatic UI launch, file handling, controlled shutdown, and Knowledge Graph autosave.	dist_KG_ALIAS: `.exe` opened panel without manual CMD startup. Offline queries and bilingual graph saves completed successfully.
DELTA-MEDIC v1.3.2 Integration	Added pre-filled clinical diagnostic trees, strict schema validation, and isolated local storage keys.	UI Panel Test: Successfully tested search, filtering, JSON import sanitization, and triage scoring.
Professor Cognitive Engine	Enabled idle batch scanning of graphs with automated relational explanation synthesis and safe memory writes.	Core Test: Verified rule inference and backing fact generation on isolated graph copies.
Slovak, English & Diacritics	Verified separated SK/EN graphs and improved diacritics-insensitive search lookup.	dist_KG_ALIAS: Queries resolved correctly from local symbolic databases.
ENVOY & Permissions	Fixed policy loading (`policies_envoy.json`) and verified user-consent workflows.	dist_ENVOY_POLICY: Loaded 5 rules successfully; external web queries triggered explicit consent prompts.
---
📁 Architecture Overview (Logical Module Mapping)
```text
src/
|-- commands/              # Natural language routing and command execution
|-- context/               # Semantic context and state engine
|-- core/                  # SafeRollback backup and state protection (safe_rollback.py)
|-- professor/             # Professor Validator cognitive verification (professor_validator.py)
|-- envoy/                 # ENVOY execution, normalizer, and quarantine layers
|-- filesystem/            # Safe file operations and HitL Safe Trash pipeline
|-- knowledge_packs/       # Dual-language knowledge stores (autosave_kg.json / autosave_kg_en.json)
|-- runtime/               # Runtime Core 5.x and InputParser5
|-- orchestrator/          # Unified Single-Process Orchestrator (sirius_orchestrator.py on Port 8080)
|-- panel_api/             # Interactive PanelAPI loops
|-- supervision/           # TimeCore temporal tracking & Guard resource monitoring
|-- colnik/                # COLNIK-6.x customs validation, COLNÍK Guard & triage queue
|-- autonomy/              # AUTONOMY 6.x decision engine, Guard supervision & Triage Mode
|-- security_family/       # Identity Engine 3.1, time-limits v3, schoolwork engine
|-- self_repair/           # Self-Repair Layer 5.8 integrity scanning
|-- triage/                # Automatic Input Triage Engine & DELTA-MEDIC clinical module
|-- ui/                    # 4-Panel UI dashboard (index.html & sirius_delta_medic.html)
|-- workflow/              # Workflow Engine 6.1.0
|-- autosave_kg.json       # Isolated Slovak Knowledge Graph Base
|-- autosave_kg_en.json    # Isolated English Knowledge Graph Base
\`-- sirius.py              # Main runtime entry point
```
---
⚙️ Performance Design
Zero External API Latency: 100% offline local execution (with optional user-approved ENVOY web lookups).
Lightweight Asynchronous UI: Non-blocking 4-Panel dashboard on port 8080.
Strict Bounded Inference: Cycle-safe reasoning preventing runaway recursion.
---
🧩 License & Copyright
The project is open-source and licensed under the MIT License. See the LICENSE file for details.
---
✨ Author & Lead Architect
Richard Pizem  
Lead Architect & Solo Maintainer  
SIRIUS‑LOCAL‑AI (Banská Bystrica, Slovakia)

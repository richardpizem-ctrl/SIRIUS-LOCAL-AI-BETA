# 📦 Installation Guide – SIRIUS LOCAL AI (v4.3.0)

SIRIUS LOCAL AI is a fully local, modular AI runtime built on the **Intelligent Runtime 4.x architecture**.  
The system is currently distributed as clean Python source code, intended for developers, testers, and advanced users.

A packaged installer will be introduced in a future release.

All processing is fully local; **no data ever leaves your PC**.

---

# ⚠️ System Notes (v4.3.0)

SIRIUS LOCAL AI interacts with Windows 11 system APIs through the **WIN‑CAP 4.x** capability layer, including:

- filesystem operations  
- window management  
- application control  
- accessibility interfaces  
- developer automation  
- plugin‑driven system actions  
- **Security Family 4.0** — identity engine 2.0, time‑limits v2, stranger‑mode, schoolwork engine  
- **AITE 4.0** — semantic triage, OCR, subject detection  
- **Reasoning Engine 4.x** — structured offline reasoning  
- **Self‑Repair Layer** — integrity checks and safe fallback states  
- **UI Automation Engine 4.3** — semantic UI parsing, workflow fallback, OS‑level routing  

Windows Defender or SmartScreen may classify the runtime as an “Unknown App”.  
Antivirus tools may generate false positives during development.

All modules operate offline with strict safety boundaries, deterministic behavior, and identity‑aware protections.

---

# 🔧 How to Run (Developer Mode)

### 1. Install **Python 3.10+**
SIRIUS requires a modern Python environment with stable async and event‑loop behavior.

### 2. Clone the repository
git clone https://github.com/richardpizem-ctrl/SIRIUS-LOCAL-AI-BETA 
### 3. Open the project in VS Code or any terminal

### 4. Run the main entrypoint
python sirius.py 
### 5. Optional: run individual modules for testing  
(runtime, plugins, GUI, workflows, triage, security, self‑repair, UI automation)

Developer mode provides full access to:

- Runtime Core 4.x  
- Plugin System 4.x  
- Workflow Engine 4.x  
- Reasoning Engine 4.x  
- GUI 4.x  
- AITE 4.0  
- WIN‑CAP 4.x  
- **Security Family 4.0 (identity engine 2.0, time‑limits v2, schoolwork engine, stranger‑mode)**  
- **Self‑Repair & Health‑Check Layer**  
- **Knowledge Packs 4.x**  
- **ENVOY 4.0 (optional safe retrieval layer)**  
- **UI Automation Engine 4.3 (NEW)**  

---

# 🛠️ Future Installation System (Planned)

## v4.1.0 – Basic Packaging
- simple startup executable  
- bundled Python environment  
- plugin auto‑loader  
- Security Family pre‑startup checks  
- Self‑Repair pre‑launch validation  

---

## v4.3.0 – UI Automation Integration (Delivered)
Although not part of the installer, v4.3.0 introduced:

- UIParser 4.3  
- UIWorkflow 4.3  
- UIActions 4.3  
- WinCapabilities 4.3  
- deterministic UI automation pipeline  

This replaces the originally planned v4.2.0 release.

---

## v5.0.0 – Intelligent Runtime Installer
- performance‑optimized packaging  
- optional UI/animation bundles  
- tray/voice integration  
- semantic triage extensions  
- deeper identity learning  
- pack‑aware installation logic  

---

## v6.0.0 – Self‑Repair Integrated Installer
The installation system will integrate fully with the diagnostic layer:

- integrity checks before startup  
- detection of corrupted configs or missing files  
- automatic safe repairs (cache reset, index rebuild, default config restore)  
- pre‑launch validation  
- user‑approved patch suggestions  
- ENVOY‑assisted safe updates (optional)  

This ensures long‑term stability even in packaged builds.

---

# 📌 Status (v4.3.0)

Installation system: **Not yet implemented**  
Packaging: **Planned for v4.1.0+**  
Runtime: **Stable (4.3.0)**  
Plugins: **Stable (4.x)**  
Architecture: **Stable (4.x)**  
Security Family: **Fully integrated (identity engine 2.0, time‑limits v2, schoolwork engine, stranger‑mode)**  
AITE: **Upgraded to v4.0.0 with semantic triage + OCR**  
WIN‑CAP: **Upgraded to v4.x**  
Self‑Repair Layer: **Stable**  
Knowledge Packs: **Semantic pack system**  
ENVOY: **Optional safe retrieval layer**  
UI Automation Engine: **New in v4.3.0 (complete semantic UI automation pipeline)**  

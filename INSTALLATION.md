# 📦 Installation Guide – SIRIUS LOCAL AI (v4.4.0 PRO)

SIRIUS LOCAL AI is a fully local, modular AI runtime built on the **Runtime 4.4.0 PRO architecture**.  
The system is distributed as clean Python source code, intended for developers, testers, and advanced users.

A packaged installer will be introduced in a future release.

All processing is fully local; **no data ever leaves your PC**.

---

# ⚠️ System Notes (v4.4.0 PRO)

SIRIUS LOCAL AI interacts with Windows 10/11 system APIs through the **WIN‑CAP 4.x** capability layer, including:

- filesystem operations  
- window management  
- application control  
- accessibility interfaces  
- plugin‑driven system actions  
- developer automation  
- **Security Family 4.x** — identity engine, time‑limits, stranger‑mode, schoolwork engine  
- **AITE 4.x** — semantic triage, OCR, subject detection  
- **Reasoning Engine 4.x** — structured offline reasoning  
- **Self‑Repair Layer 4.x** — integrity checks and safe fallback states  
- **UI Automation Engine 4.3** — semantic UI parsing, workflow fallback, OS‑level routing  
- **Runtime 4.4.0 PRO Stack** — deterministic, sandboxed, Phase‑5‑ready execution  

Windows Defender or SmartScreen may classify the runtime as an “Unknown App”.  
Antivirus tools may generate false positives during development.

All modules operate offline with strict safety boundaries, deterministic behavior, and identity‑aware protections.

---

# 🔧 How to Run (Developer Mode)

### 1. Install **Python 3.10 or 3.11**
Python 3.12 is **not supported** due to library incompatibilities.

### 2. Install required Python packages
pip install watchdog psutil dearpygui pyaudio speechrecognition pyttsx3 colorama 
### 3. Clone the repository
git clone https://github.com/richardpizem-ctrl/SIRIUS-LOCAL-AI-BETA 
### 4. Open the project in VS Code or any terminal

### 5. Run the main entrypoint
python sirius.py 
### 6. Optional: run individual modules for testing  
(runtime, plugins, GUI, workflows, triage, security, self‑repair, UI automation)

Developer mode provides full access to:

- **Runtime Core 4.4.0 PRO**  
- **Plugin System 4.4**  
- **Workflow Engine 4.4**  
- **Reasoning Engine 4.x**  
- **GUI 4.4**  
- **Tray 4.4**  
- **Voice 4.4**  
- **Hotword 4.4**  
- **AI Loop 4.4**  
- **SystemHealthEngine 4.4**  
- **TaskManagerEngine 4.4**  
- **ServiceManager 4.4**  
- **SystemAgent 4.4**  
- **AITE 4.x**  
- **WIN‑CAP 4.x**  
- **Security Family 4.x**  
- **Self‑Repair & Health‑Check Layer 4.x**  
- **Knowledge Packs 4.x**  
- **UI Automation Engine 4.3**  

---

# 🛠️ Future Installation System (Planned)

## v4.5.0 – System Intelligence Expansion
- Driver Manager Engine 4.5  
- Education Engine 4.5  
- ENVOY Bridge Layer 2.0  
- deeper integration with Runtime 4.4  

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

# 📌 Status (v4.4.0 PRO)

Installation system: **Not yet implemented**  
Packaging: **Planned for v4.5.0+**  
Runtime: **Stable (4.4.0 PRO)**  
Plugins: **Stable (4.4)**  
Architecture: **Stable (4.4)**  
Security Family: **Fully integrated (identity engine, time‑limits, stranger‑mode, schoolwork engine)**  
AITE: **Upgraded to v4.x with semantic triage + OCR**  
WIN‑CAP: **Upgraded to 4.x**  
Self‑Repair Layer: **Stable**  
Knowledge Packs: **Semantic pack system**  
UI Automation Engine: **Stable (4.3)**  
ENVOY: **Base layer (Bridge Layer 2.0 coming in 4.5)**  

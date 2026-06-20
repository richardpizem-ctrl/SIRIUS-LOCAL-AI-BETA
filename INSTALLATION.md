# 📦 Installation Guide – SIRIUS LOCAL AI (v5.3.0)

SIRIUS LOCAL AI is a fully local, modular AI runtime built on the **Unified Runtime 5.3 architecture**, featuring:

- AITE 5.3 (multimodal semantic triage)  
- Workflow Engine 5.3  
- Reasoning Engine 5.0  
- Knowledge Graph 5.x  
- ENVOY Execution + Permission Layers 5  
- System Agent 5  
- Security Family 5.x  
- Self‑Repair Layer 5.x  
- Deterministic UI Automation Engine 5.0  

The system is distributed as clean Python source code, intended for developers, testers, and advanced users.

A packaged installer (`.EXE`) is introduced in **5.x** and expanded in **5.3+**.

All processing is fully local; **no data ever leaves your PC**.

---

# ⚠️ System Notes (v5.3.0)

SIRIUS LOCAL AI interacts with Windows 11 system APIs through the **WIN‑CAP 5.x** capability layer, including:

- filesystem operations  
- window management  
- application control  
- accessibility interfaces  
- plugin‑driven system actions  
- developer automation  
- **Security Family 5.x** — identity engine, time‑limits, stranger‑mode, schoolwork engine  
- **Reasoning Engine 5.0** — deterministic KG‑based reasoning  
- **Workflow Engine 5.3** — deterministic routing  
- **System Agent 5** — identity‑aware OS validation  
- **HealthMonitor5** — degraded‑mode detection  
- **ErrorHandler5** — safe execution wrapper  
- **SystemHooks5** — runtime event hooks  
- **Knowledge Graph Runtime 1.x** — offline entity‑relation reasoning  
- **ENVOY Execution + Permission Layers 5** — permission‑based online fetch (optional)  

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
---

# ⚠️ Important Note — SIRIUS runs through CLI

SIRIUS LOCAL AI is executed **via the command line (CLI)**.  
The runtime does not start automatically through a graphical launcher unless the optional UI module is enabled.

Running through CLI ensures:

- correct initialization of Runtime 5.3  
- proper loading of the Knowledge Graph  
- activation of System Agent 5  
- deterministic workflow routing  
- correct plugin and capability loading  
- safe ENVOY initialization  
- correct Self‑Repair Layer activation  

Using the CLI is the **official and recommended method** for all developers and testers.

---

### 6. Optional: run individual modules for testing  
(runtime, plugins, GUI, workflows, KG, security, system agent, UI automation)

Developer mode provides full access to:

- **Runtime Core 5.3**  
- **Workflow Engine 5.3**  
- **Reasoning Engine 5.0**  
- **Knowledge Graph Runtime 1.x**  
- **System Agent 5**  
- **HealthMonitor5**  
- **ErrorHandler5**  
- **SystemHooks5**  
- **Plugin System 5.x**  
- **Security Family 5.x**  
- **ENVOY Execution + Permission Layers 5**  
- **UI Automation Engine 5.0**  

---

# 🛠️ Future Installation System

## ⭐ v5.3.0 – Intelligent Runtime Installer (STABLE)
- performance‑optimized packaging  
- optional UI/animation bundles  
- tray/voice integration  
- semantic triage extensions  
- identity‑aware installation logic  
- KG‑aware initialization  
- ENVOY permission setup  
- **stable `.EXE` installer for SIRIUS LOCAL AI**  

---

## ⭐ v5.4.0 – Self‑Repair Layer Integration
- repair sandbox  
- module integrity scanning  
- safe fallback states  
- degraded → repaired transitions  
- repair‑aware startup validation  

---

## ⭐ v6.0.0 – Self‑Repair Integrated Installer
The installation system will integrate fully with the diagnostic layer:

- integrity checks before startup  
- detection of corrupted configs or missing files  
- automatic safe repairs (cache reset, index rebuild, default config restore)  
- pre‑launch validation  
- user‑approved patch suggestions  
- ENVOY‑assisted safe updates (optional)  

This ensures long‑term stability even in packaged builds.

---

# 📌 Status (v5.3.0)

Installation system: **Stable (5.3.0)**  
Packaging: **Stable**  
Runtime: **Stable (5.3.0)**  
Plugins: **Stable (5.x)**  
Architecture: **Unified Runtime 5.x**  
Security Family: **Integrated (identity engine, time‑limits, stranger‑mode, schoolwork engine)**  
Reasoning Engine: **Stable (5.0)**  
Workflow Engine: **Stable (5.3)**  
System Agent: **Stable (5)**  
Knowledge Graph: **Runtime 1.x**  
UI Automation Engine: **Stable (5.0)**  
ENVOY: **Execution + Permission Layers 5**  
Self‑Repair: **Layer 5.x active**  

# 📦 Installation Guide – SIRIUS LOCAL AI (v5.0.0)

SIRIUS LOCAL AI is a fully local, modular AI runtime built on the **Runtime 5.0.0 architecture**, featuring the first generation of **Offline Knowledge Graph Reasoning**.

The system is distributed as clean Python source code, intended for developers, testers, and advanced users.

A packaged installer (`.EXE`) is introduced in **version 5.0.0** and expanded in **5.1+**.

All processing is fully local; **no data ever leaves your PC**.

---

# ⚠️ System Notes (v5.0.0)

SIRIUS LOCAL AI interacts with Windows 11 system APIs through the **WIN‑CAP 5.x** capability layer, including:

- filesystem operations  
- window management  
- application control  
- accessibility interfaces  
- plugin‑driven system actions  
- developer automation  
- **Security Family 5.0** — identity engine, time‑limits, stranger‑mode, schoolwork engine  
- **Reasoning Engine 5.0** — deterministic KG‑based reasoning  
- **Workflow Engine 5.0** — KG‑aware routing  
- **System Agent 5.0** — identity‑aware OS validation  
- **HealthMonitor5** — degraded‑mode detection  
- **ErrorHandler5** — safe execution wrapper  
- **SystemHooks5** — runtime event hooks  
- **Knowledge Graph Runtime 1.0** — offline entity‑relation reasoning  
- **Envoy Bridge Layer 1.0** — permission‑based online fetch (optional)  

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
(runtime, plugins, GUI, workflows, KG, security, system agent, UI automation)

Developer mode provides full access to:

- **Runtime Core 5.0.0**  
- **Workflow Engine 5.0**  
- **Reasoning Engine 5.0**  
- **Knowledge Graph Runtime 1.0**  
- **System Agent 5.0**  
- **HealthMonitor5**  
- **ErrorHandler5**  
- **SystemHooks5**  
- **Plugin System 5.x**  
- **Security Family 5.0**  
- **Envoy Bridge Layer 1.0**  
- **UI Automation Engine 4.5 (temporary until 5.x)**  

---

# 🛠️ Future Installation System

## ⭐ v5.0.0 – Intelligent Runtime Installer (FIRST .EXE PACKAGE)
- performance‑optimized packaging  
- optional UI/animation bundles  
- tray/voice integration  
- semantic triage extensions  
- identity‑aware installation logic  
- KG‑aware initialization  
- **first official `.EXE` installer for SIRIUS LOCAL AI**  

---

## ⭐ v5.1.0 – Self‑Repair Layer 1.0 Integration
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

# 📌 Status (v5.0.0)

Installation system: **In development (first .EXE in 5.0.0)**  
Packaging: **In progress**  
Runtime: **Stable (5.0.0)**  
Plugins: **Stable (5.x)**  
Architecture: **Stable (5.x)**  
Security Family: **Integrated (identity engine, time‑limits, stranger‑mode, schoolwork engine)**  
Reasoning Engine: **Upgraded to 5.0 (KG‑based)**  
Workflow Engine: **Upgraded to 5.0 (KG‑aware)**  
System Agent: **Upgraded to 5.0**  
Knowledge Graph: **Runtime 1.0**  
UI Automation Engine: **Stable (4.5 → 5.x planned)**  
ENVOY: **Bridge Layer 1.0 (full fetch in 5.1)**  

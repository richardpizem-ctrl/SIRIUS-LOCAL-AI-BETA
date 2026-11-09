# 📥 INSTALLATION GUIDE — SIRIUS LOCAL AI (v6.0.1 UNIFIED)
**Status:** ✔ Production-Enhanced  
**Version:** 6.0.1  
**Component:** Installation & Deployment  
**Role:** Step-by-step local deployment guide for setting up SIRIUS LOCAL AI (v6.0.1) on Windows 11 with single-process orchestration on port 8080, dual-language graph isolation, SafeRollback crash resilience, Professor Validator middleware, and COLNÍK Guard security.

---

## 🎯 1. Overview & System Requirements  
SIRIUS Local AI is an offline-first, modular symbolic AI runtime (with optional user-approved ENVOY web lookups). It requires **no active cloud connectivity during core execution**, no external API keys, and operates entirely on local hardware.

### **System Requirements**
- **Operating System:** Windows 11 (tested and optimized) or compatible local environment  
- **Python Version:** Python 3.10 or higher  
- **Port Allocation:** Port `8080` (reserved for the single-process HTTP/IPC orchestrator daemon)  
- **Storage:** ~50 MB local disk space for core modules, dual-language knowledge graphs (`autosave_kg.json`, `autosave_kg_en.json`), and quarantine storage  

---

## ⚙️ 2. Step-by-Step Installation Instructions

### **Step 1: Clone or Download the Repository**  
Obtain the latest SIRIUS Local AI release package (`SIRIUS-KG-ALIAS-Windows-x64-REVIEW.zip`) or clone the repository directly from GitHub:
```cmd
git clone https://github.com/richardpizem-ctrl/SIRIUS-LOCAL-AI-BETA.git
cd SIRIUS-LOCAL-AI-BETA
```

### **Step 2: Verify Python Environment**  
Ensure Python is installed and accessible in your system PATH:
```cmd
python --version
```

### **Step 3: Review Directory Structure & Core Modules**  
Ensure the root directory contains the updated v6.0.1 modules:
- `sirius_orchestrator.py` (Central orchestrator and IPC daemon on port 8080)  
- `core/safe_rollback.py` (SafeRollback backup and restore module)  
- `professor/professor_validator.py` (Professor Validator decision middleware)  
- `autosave_kg.json` (Slovak knowledge graph store)  
- `autosave_kg_en.json` (English knowledge graph store)  
- `ui/index.html` (4-Panel UI Suite dashboard)  

---

## 🚀 3. Launching the Runtime

To start the complete SIRIUS Local AI ecosystem (v6.0.1) via the unified single-process orchestrator, execute:
```cmd
python sirius_orchestrator.py
```

This command initializes:
- The single-process HTTP/IPC daemon bound to port 8080  
- Embedded TerminalAssistant and TimeCore heartbeat telemetry  
- Dual-language isolated knowledge stores (`autosave_kg.json` & `autosave_kg_en.json`)  
- Token Guard input sanitization and COLNÍK Guard shell security (0.0s hard blocks)  
- SafeRollback backup supervision (`safe_rollback.py`)  
- Professor Validator cognitive verification matrix (`PASS / WARN / REJECT`)  
- Human-in-the-Loop Safe Trash quarantine pipeline (`GET /trash`, tested in `dist_V6_CHECK`)  
- The 4-Panel UI Suite dashboard (`Duplicates`, `Triage`, `Navigation`, `Terminal`)  

---

## 🛡️ 4. Verification & Testing

Once launched, verify system operation:
1. Open your web browser and navigate to: `http://localhost:8080`  
2. Confirm that the 4-Panel UI Suite loads successfully and displays active system telemetry.  
3. Test terminal input clearance to ensure automatic state reset (`currentModule = "none"`).  
4. Verify dual-language knowledge graph isolation by toggling between SK and EN modes.  

---

## 📂 Related Files & Documentation
- Architecture  
- Module Map  
- Code of Conduct  
- Contributing  
- Security Protocol  

# 🏗 Architecture – SIRIUS LOCAL AI (v4.0.0 → v4.1.0 EXPANDED)

<p align="center">
  <img src="https://img.shields.io/badge/version-4.1.0-purple">
  <img src="https://img.shields.io/badge/license-MIT-green">
  <img src="https://img.shields.io/badge/platform-Windows%2011-blue">
  <img src="https://img.shields.io/badge/runtime-Intelligent%204.0-orange">
  <img src="https://img.shields.io/badge/local%20AI-100%25-blueviolet">
</p>

SIRIUS LOCAL AI v4.1.0 expands the Intelligent Runtime 4.0 architecture with a **new System Intelligence Layer**, enabling deep PC‑level diagnostics, optimization, driver management, service control, safe system actions, and human‑friendly education.

This update introduces:

- **System Health Engine 4.1**
- **Driver Manager Engine 4.1**
- **Task Manager Engine 4.1**
- **Service Manager Engine 4.1**
- **Education Engine 4.1**
- **VYSLANEC 4.1 (Bridge Layer 2.0)**
- **Password Vault 4.0 (Secure Identity‑Aware Credential Storage)** ← *NEW MODULE*

All system‑level actions remain **fully local**, **identity‑aware**, and **safely routed** through VYSLANEC.

---

# 🛡 Stability Notice (v4.1.0)

The new System Intelligence Layer guarantees:

- safe system operations  
- identity‑aware permissions  
- no direct kernel access  
- no hidden automation  
- reversible actions  
- transparent explanations  
- strict FAMILY‑safe behavior  
- deterministic, predictable execution  

This version elevates SIRIUS from a semantic runtime to a **PC‑aware intelligent assistant**.

---

# 🧩 Architectural Principles (v4.1.0)

- strict modular separation  
- deterministic behavior  
- identity‑aware access control  
- FAMILY‑safe operation  
- SCHOOLWORK always allowed  
- no direct network communication  
- no direct system access (VYSLANEC required)  
- reversible, predictable actions  
- semantic understanding of system state  
- friendly education for every system action  
- capability‑based access to Windows functions  

---

# 🧱 Core Layers (v4.1.0)

## 1. Runtime Core 4.0
Central orchestrator.

Responsibilities:
- module lifecycle  
- workflow dispatch  
- plugin loading  
- capability enforcement  
- identity integration  
- self‑repair integration  

---

## 2. Natural Language Router 4.0
Semantic command routing.

---

## 3. Filesystem Agent 4.0
Deterministic FS operations.

---

## 4. Context Memory Engine 4.0
Workflow context.

---

## 5. Workflow Engine 4.0
Deterministic workflow logic.

---

## 6. GUI Layer 4.0
Modular UI.

---

## 7. AITE 4.0
Semantic triage.

---

## 8. WIN‑CAP 4.0
Safe Windows capability layer.

---

# 🆕 SYSTEM INTELLIGENCE LAYER (v4.1.0)

A brand‑new architectural layer that gives SIRIUS **awareness of the PC**, the ability to **diagnose**, **optimize**, and **repair**, while maintaining strict safety.

---

# 🔥 1. System Health Engine 4.1
(… unchanged …)

---

# 🔥 2. Driver Manager Engine 4.1
(… unchanged …)

---

# 🔥 3. Task Manager Engine 4.1
(… unchanged …)

---

# 🔥 4. Service Manager Engine 4.1
(… unchanged …)

---

# 🔥 5. Education Engine 4.1
(… unchanged …)

---

# 🔥 6. VYSLANEC 4.1 (Bridge Layer 2.0)
(… unchanged …)

---

# 🔐 Password Vault 4.0 (Secure Credential Module)

A fully local, encrypted, identity‑aware password storage system integrated into the SIRIUS Security Family.

### Responsibilities:
- AES‑256‑GCM encrypted credential storage  
- PBKDF2‑HMAC‑SHA256 master key derivation  
- offline, file‑based vault container  
- OWNER‑only write access  
- FAMILY read‑only access  
- STRANGER blocked  
- deterministic API for workflows  
- safe routing through Runtime Core  

### Architecture:
- **vault_api.py** → public interface  
- **vault_core.py** → logic layer  
- **vault_storage.py** → encrypted JSON container  
- **vault_crypto.py** → AES‑256‑GCM + PBKDF2  
- **NL Router block** → natural language commands  
- **RuntimeManager tasks** → workflow integration  

### Guarantees:
- 100% offline  
- no telemetry  
- no cloud sync  
- identity‑aware access  
- deterministic behavior  
- tamper‑resistant encrypted container  

---

# 🖼 Architecture Diagram (v4.1.0 Placeholder)

<p align="center">
  <img src="docs/architecture_diagram_v4_1_placeholder.png" width="600">
</p>

---

# 🔌 Module Interconnections (v4.1.0)

User Input  
↓  
AITE 4.0 → FS‑AGENT 4.0 → CME‑MEM 4.0  
↓  
Workflow Engine 4.0  
↓  
Runtime Core 4.0  
↓  
**System Intelligence Layer 4.1**  
↓  
**Password Vault 4.0 (identity‑aware secure storage)**  
↓  
**VYSLANEC 4.1**  
↓  
Windows 11 (safe, controlled)

---

# 📌 Document Status

Current version: **4.1.0 (Expanded)**  
Architecture is fully defined and includes the new Password Vault 4.0 module.

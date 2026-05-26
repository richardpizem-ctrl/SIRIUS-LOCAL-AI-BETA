# SIRIUS‑LOCAL‑AI  
**A fully modular, offline‑only AI runtime with intelligent reasoning, self‑repair, semantic triage, deterministic UI automation, and a next‑generation capability architecture.**

SIRIUS‑LOCAL‑AI is a next‑generation local AI framework designed for **speed, stability, modularity, semantic intelligence, and full offline autonomy**.

Version **4.0.0** introduced the Intelligent Runtime 2.0, Reasoning Engine 4.0, AITE 4.0, Security Family 4.0, Schoolwork Engine 4.0, Self‑Repair Layer, Knowledge Packs 4.0, and the ENVOY safe‑retrieval system.

Version **4.3.0** delivered the **Semantic UI Automation Engine**, completing the originally planned 4.2.0 release and expanding the runtime with UIParser 4.3, UIWorkflow 4.3, UIActions 4.3, and WinCapabilities 4.3.

Version **4.4.0 PRO** upgraded the entire runtime into a **deterministic, system‑intelligent, safety‑hardened architecture**, including AITE 4.4, Reasoning Engine 4.4, Workflow Engine 4.4, Knowledge Packs 4.4, System Agent 4.2, and UI Automation Engine 4.4.

Version **4.5.0 PRO** completes the PRO‑tier upgrade with **unified deterministic routing**, **System Agent 4.5**, **AITE 4.5**, **UI Automation Engine 4.5**, **Knowledge Packs 4.5**, **Security Family 4.5**, and a fully stabilized **System Intelligence Layer 4.5**.

The entire system runs **100% locally**, without external dependencies or cloud services.

---

## 📌 Table of Contents
- [Architecture](ARCHITECTURE.md)
- [Module Map](MODULE_MAP.md)
- [Styleguide](STYLEGUIDE.md)
- [Testing Guide](TESTING_GUIDE.md)
- [Performance Guide](PERFORMANCE_GUIDE.md)
- [Release Notes](RELEASE_NOTES.md)
- [Roadmap](ROADMAP.md)
- [Security Family](SECURITY_FAMILY.md)
- [AITE 4.5](AITE.md)
- [ENVOY 4.0](ENVOY_TUTORIAL.md)
- [Future Vision](FUTURE_VISION.md)
- [Password Vault 4.1](PASSWORD_VAULT.md)

---

## 🚀 Key Features (v4.5.0 PRO)

### **Intelligent Runtime 4.x**
A fully upgraded runtime with:
- deterministic execution  
- semantic routing  
- identity‑aware logic  
- self‑repair integration  
- capability isolation  
- safe fallback states  
- UI automation integration (v4.5.0)  
- hardened System Agent 4.5 validation  

---

### **Modular Architecture (v4.x)**
Each module is isolated and follows strict boundaries:

- `commands/` – NL routing and command logic  
- `context/` – semantic context engine  
- `filesystem/` – safe file operations  
- `runtime/` – Runtime Core 4.x  
- `triage/` – AITE 4.5 (semantic triage)  
- `ui/` – GUI logic  
- `ui_components/` – graphical elements  
- `ui_components/animations/` – animation engine  
- `workflow/` – Workflow Engine 4.x  
- `plugins/` – Plugin System 4.x  
- `security_family/` – Identity Engine 2.1, time‑limits v2, schoolwork engine  
- `self_repair/` – Self‑Repair & Health‑Check Layer  
- `knowledge_packs/` – Knowledge Packs 4.x  
- `envoy/` – ENVOY 4.0 safe retrieval layer  
- `ui_automation/` – **UI Automation Engine 4.5**  
- `system_agent/` – System Agent 4.5 (safe action execution)  

The system is designed to be extended **without modifying the core**.

---

### **Plugin System 4.x**
Plugins can define:

- NL commands  
- AI tasks  
- workflows  
- reasoning hooks  
- GUI elements  
- pack‑aware logic  

All official plugins are fully prepared for v4.x.

---

### **Automatic Input Triage Engine (AITE 4.5)**
AITE analyzes inputs, classifies them, and routes them to the correct modules.

It ensures:

- semantic input understanding  
- OCR extraction  
- subject detection  
- difficulty scoring  
- identity‑aware routing  
- deterministic behavior  
- **Schoolwork Engine 4.5 — academic tasks always bypass FAMILY restrictions**  
- **integration with SECURITY FAMILY 4.5**  
- **integration with Reasoning Engine 4.5**  

---

### **Reasoning Engine 4.x**
A structured reasoning layer:

- step‑by‑step reasoning  
- academic explanations  
- code analysis  
- semantic breakdown  
- pack‑aware reasoning  
- deterministic logic  

---

### **Self‑Repair & Health‑Check Layer**
Ensures long‑term stability:

- integrity checks  
- corruption detection  
- safe automatic repairs  
- fallback states  
- dependency validation  
- system‑wide health reporting  

---

### **Knowledge Packs 4.x**
Offline knowledge expansions:

- household  
- cooking  
- school subjects  
- device diagnostics  
- safety  
- troubleshooting  
- definitions & facts  

All packs are semantic and reasoning‑ready.

---

### **SIRIUS ENVOY 4.0 – Safe Online Retrieval**
Optional isolated agent for safe external lookups:

- outbound‑only  
- quarantine sandbox  
- scraper layer  
- validator & policy filter  
- safe payload delivery  

ENVOY never sends local data outward.

---

### **Workflow Engine 4.x**
Manages:

- multi‑step processes  
- semantic transitions  
- plugin workflows  
- safe command execution  
- deterministic state changes  
- SCHOOLWORK workflow prioritization  

---

### **PC Automation Runtime 4.x**
Developer‑level offline automation:

- filesystem automation  
- editor integration  
- code workflows  
- structured command parsing  
- command routing  

---

### **UI Automation Engine 4.5 (UPDATED)**
A major capability expanded in v4.5.0:

- improved fuzzy UI parsing  
- safer semantic UI actions  
- deterministic fallback logic  
- OS‑level routing  
- sandbox‑protected execution  
- WinCapabilities 4.5 integration  
- System Agent 4.5 validation for all UI actions  

This engine replaces the originally planned v4.2.0 release.

---

## 📁 Project Structure (v4.5.0)
src/
├── commands/  
├── context/  
├── envoy/  
├── filesystem/  
├── knowledge_packs/  
├── runtime/  
├── security_family/  
├── self_repair/  
├── triage/  
├── ui/  
├── ui_components/  
│    └── animations/  
├── ui_automation/  
├── system_agent/  
├── workflow/  
├── plugins/  
└── sirius.py  

Each directory has a clear responsibility and is described in **MODULE_MAP.md**.

---

## 🧪 Testing
The project includes a complete testing plan:

- functional tests  
- semantic routing tests  
- real‑time tests  
- UI tests  
- workflow sequence tests  
- plugin integration tests  
- SECURITY FAMILY identity tests  
- SCHOOLWORK ENGINE tests  
- self‑repair integrity tests  
- UI Automation Engine 4.5 tests  
- System Agent 4.5 validation tests  

Details are in **TESTING_GUIDE.md**.

---

## ⚙️ Performance
The system is optimized for:

- low latency  
- long‑term stability  
- predictable processing  
- minimal thread blocking  
- efficient event routing  
- deterministic reasoning  

More in **PERFORMANCE_GUIDE.md**.

---

## 🗓️ Release Plan

### **v4.0.0 – Intelligent Runtime 2.0 (Stable)**  
### **v4.3.0 – Semantic UI Automation Engine**  
### **v4.4.0 – PRO Runtime Expansion**  
### **v4.5.0 – Unified PRO Runtime (Current)**  
- AITE 4.5  
- Reasoning Engine 4.5  
- Workflow Engine 4.5  
- Knowledge Packs 4.5  
- UI Automation Engine 4.5  
- System Agent 4.5  
- deterministic system‑level intelligence  

---

## 🧩 License
The project is open‑source and available to the community.  
The license is provided in **LICENSE**.

---

## ✨ Author
**Richard Pizem**  
Lead architect & solo maintainer  
SIRIUS‑LOCAL‑AI

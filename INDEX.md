# SIRIUS‑LOCAL‑AI  
**A fully modular, offline‑only AI runtime with intelligent reasoning, self‑repair, and a next‑generation capability architecture.**

SIRIUS‑LOCAL‑AI is a next‑generation local AI framework designed for **speed, stability, modularity, semantic intelligence, and full offline autonomy**.  
Version **4.0.0** introduces the Intelligent Runtime 2.0, Reasoning Engine 4.0, AITE 4.0, Security Family 4.0, Schoolwork Engine 4.0, Self‑Repair Layer, Knowledge Packs 4.0, and the ENVOY safe‑retrieval system.

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
- [AITE 4.0](AITE.md)
- [ENVOY 4.0](ENVOY_TUTORIAL.md)
- [Future Vision](FUTURE_VISION.md)

---

## 🚀 Key Features (v4.0.0)

### **Intelligent Runtime 4.0**
A fully upgraded runtime with:
- deterministic execution  
- semantic routing  
- identity‑aware logic  
- self‑repair integration  
- capability isolation  
- safe fallback states  

---

### **Modular Architecture (v4.0.0)**
Each module is isolated and follows strict boundaries:

- `commands/` – NL routing and command logic  
- `context/` – semantic context engine  
- `filesystem/` – safe file operations  
- `runtime/` – Runtime Core 4.0  
- `triage/` – AITE 4.0 (semantic triage)  
- `ui/` – GUI logic  
- `ui_components/` – graphical elements  
- `ui_components/animations/` – animation engine  
- `workflow/` – Workflow Engine 4.0  
- `plugins/` – Plugin System 4.0  
- `security_family/` – Identity Engine 2.0, time‑limits v2, schoolwork engine  
- `self_repair/` – Self‑Repair & Health‑Check Layer  
- `knowledge_packs/` – Knowledge Packs 4.0  
- `envoy/` – ENVOY 4.0 safe retrieval layer  

The system is designed to be extended **without modifying the core**.

---

### **Plugin System 4.0**
Plugins can define:

- NL commands  
- AI tasks  
- workflows  
- reasoning hooks  
- GUI elements  
- pack‑aware logic  

All official plugins are fully prepared for v4.0.0.

---

### **Automatic Input Triage Engine (AITE 4.0)**
AITE analyzes inputs, classifies them, and routes them to the correct modules.

It ensures:

- semantic input understanding  
- OCR extraction  
- subject detection  
- difficulty scoring  
- identity‑aware routing  
- deterministic behavior  
- **Schoolwork Engine 4.0 — academic tasks always bypass FAMILY restrictions**  
- **integration with SECURITY FAMILY 4.0**  
- **integration with Reasoning Engine 4.0**  

---

### **Reasoning Engine 4.0**
A new structured reasoning layer:

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

### **Knowledge Packs 4.0**
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

### **Workflow Engine 4.0**
Manages:

- multi‑step processes  
- semantic transitions  
- plugin workflows  
- safe command execution  
- deterministic state changes  
- SCHOOLWORK workflow prioritization  

---

### **PC Automation Runtime 4.0**
Developer‑level offline automation:

- filesystem automation  
- editor integration  
- code workflows  
- structured command parsing  
- command routing  

---

## 📁 Project Structure (v4.0.0)
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

### **v4.0.0 – Intelligent Runtime 2.0 (Current Stable Release)**
- Runtime 4.0  
- Plugin System 4.0  
- Workflow Engine 4.0  
- Reasoning Engine 4.0  
- GUI 4.0  
- AITE 4.0  
- WIN‑CAP 4.0  
- **SECURITY FAMILY 4.0 – identity engine 2.0**  
- **time‑limits v2**  
- **Schoolwork Engine 4.0**  
- **Self‑Repair Layer**  
- **Knowledge Packs 4.0**  
- **ENVOY 4.0**  
- expanded household modules  

---

## 🧩 License
The project is open‑source and available to the community.  
The license is provided in **LICENSE**.

---

## ✨ Author
**Richard Pizem**  
Lead architect & solo maintainer  
SIRIUS‑LOCAL‑AI

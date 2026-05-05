# SIRIUS‑LOCAL‑AI  
**A fully modular, offline AI runtime with a stable architecture, plugin ecosystem, and real‑time processing.**

SIRIUS‑LOCAL‑AI is a next‑generation local AI framework designed for **speed, stability, modularity, and full offline autonomy**.  
Version **3.0.0** introduces the Intelligent Runtime, SECURITY FAMILY, Schoolwork Priority Mode, and expanded triage and workflow intelligence.

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

---

## 🚀 Key Features

### **Modular Architecture (v3.0.0)**
Each module is isolated and follows strict boundaries:

- `commands/` – NL routing and command logic  
- `context/` – context memory engine  
- `filesystem/` – safe file operations  
- `runtime/` – Runtime Core 3.0  
- `triage/` – AITE 3.0  
- `ui/` – GUI logic  
- `ui_components/` – graphical elements  
- `workflow/` – Workflow Engine 3.0  
- `plugins/` – Plugin System 3.0  
- `security_family/` – **NEW (v3.0.0): behavior‑based identity, family safety, time‑limits, schoolwork priority**

The system is designed to be extended **without modifying the core**.

---

### **Plugin System 3.0**
Plugins can define:

- NL commands  
- AI tasks  
- workflows  
- AI loop rules  
- GUI elements  

All official plugins are fully prepared for v3.0.0.

---

### **Automatic Input Triage Engine (AITE 3.0)**
AITE analyzes inputs, classifies them, and routes them to the correct modules.

It ensures:

- correct input type detection  
- safe routing  
- deterministic behavior  
- zero conflicts between modules  
- **Schoolwork Priority Mode — academic tasks always bypass FAMILY restrictions**  
- **integration with SECURITY FAMILY identity rules**

---

### **Real‑Time Processing**
The system includes a custom real‑time engine with:

- a stable event loop  
- optimized processing  
- low latency  
- predictable performance  

---

### **GUI Layer 3.0**
The UI is built on modular components:

- `ui/` – UI logic  
- `ui_components/` – graphical elements  
- `ui_components/animations/` – animations (ready for v3.0.0)  

---

### **Workflow Engine 3.0**
The workflow layer manages:

- multi‑step processes  
- safe command execution  
- plugin workflows  
- predictable state transitions  
- UI feedback  
- SCHOOLWORK workflow prioritization  

---

## 📁 Project Structure (v3.0.0)
```
src/
├── commands/
├── context/
├── email/
├── filesystem/
├── runtime/
├── triage/
├── ui/
├── ui_components/
│    └── animations/
├── workflow/
├── plugins/
├── security_family/   ← NEW (v3.0.0)
└── sirius.py
```

Each directory has a clear responsibility and is described in **MODULE_MAP.md**.

---

## 🧪 Testing
The project includes a complete testing plan:

- manual tests  
- Git Bash tests  
- real‑time tests  
- UI tests  
- workflow sequence tests  
- plugin integration tests  
- SECURITY FAMILY identity tests  
- SCHOOLWORK PRIORITY MODE tests  

Details are in **TESTING_GUIDE.md**.

---

## ⚙️ Performance
The system is optimized for:

- low latency  
- long‑term stability  
- predictable processing  
- minimal thread blocking  
- efficient event routing  

More in **PERFORMANCE_GUIDE.md**.

---

## 🗓️ Release Plan

### **v3.0.0 – Intelligent Runtime (Current Stable Release)**
- Runtime 3.0  
- Plugin System 3.0  
- Workflow Engine 3.0  
- AI Loop 3.0  
- GUI 3.0  
- AITE 3.0  
- WIN‑CAP 3.0  
- **SECURITY FAMILY – behavior‑based identity & family safety layer**  
- **time‑based limits for children**  
- **Schoolwork Priority Mode (schoolwork always allowed)**  
- expanded household modules (HOME_ASSISTANT, COOKING_ADVISOR, SCHOOL_HELPER, DEVICE_DIAGNOSTICS)

### **v4.0.0 – Self‑Repair & Health‑Check Layer**
- integrity checks  
- safe automatic repairs  
- patch suggestions  
- system‑wide health reporting  

---

## 🧩 License
The project is open‑source and available to the community.  
The license is provided in **LICENSE**.

---

## ✨ Author
**Richard Pizem**  
Visionary architect & solo maintainer  
SIRIUS‑LOCAL‑AI

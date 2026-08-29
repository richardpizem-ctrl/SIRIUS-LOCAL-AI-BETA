# 🧠 REASONING ENGINE 5.x — Deterministic Multi‑Hop Inference Core  
**Status:** ✔ Active  
**Version:** 5.x  
**SIRIUS Local AI Version:** 5.7.0  
**Component:** ReasoningEngine5  
**Role:** Deterministic symbolic reasoning engine performing multi-hop inference, rule evaluation, and KG-driven logic

---

## 🎯 Purpose  
ReasoningEngine5 is the core inference module of SIRIUS Local AI.  
It evaluates rules, performs multi-hop reasoning, validates hypotheses, and generates structured explanations based on the Knowledge Graph (KG ENGINE).

The engine is fully deterministic, transparent, and designed for enterprise-grade explainability.

---

## 🧩 Architecture Overview  
**KG ENGINE → ReasoningEngine5 → AUTONOMY → COLNÍK → EXECUTE**

### Core Responsibilities  
- Evaluate inference rules  
- Perform multi-hop reasoning  
- Auto-detect hypotheses  
- Validate semantic relations  
- Generate structured WHY reasoning  
- Provide transparent explainability  
- Integrate with autonomy workflow  

### Key Files  
- `runtime5/ReasoningEngine5.py`  
- `KG/kg_engine.py`  
- `KG/kg_store/`  
- `IPC_DATA/proposals.json`  
- `IPC_DATA/responses.json`  

---

## 🔍 Reasoning Pipeline  

### **1 — Hypothesis Detection**  
If no hypothesis is provided, the engine auto-detects the most relevant semantic relation using KG metadata.

### **2 — Rule Evaluation**  
The engine loads and evaluates all active inference rules, including:  
- OrbitTypeInferenceRule  
- AutoTypeInferenceRule  
- MultiHopOrbitInferenceRule  
- DedicsnostVlastnostiRule  
- TranzitivneRelacieRule  

Each rule is deterministic and produces structured evidence.

### **3 — Multi-Hop Reasoning**  
The engine explores multi-hop paths across the KG:  
- direct relations  
- transitive chains  
- inherited properties  
- orbit-based semantic jumps  
- multi-layer explainability  

Depth is capped to prevent runaway inference.

### **4 — WHY Reasoning**  
Generates a structured explanation:  
- hypothesis  
- evidence  
- confidence  
- multi-hop chain  
- semantic justification  

WHY reasoning is used by AUTONOMY for decision-making.

### **5 — Workflow Integration**  
Results are passed to:  
- AUTONOMY (decision layer)  
- COLNÍK (routing layer)  
- EXECUTE (action layer)  
- UI PANEL (developer diagnostics)

---

## 🧱 Inference Rules  

### **OrbitTypeInferenceRule**  
Determines semantic orbit relationships between entities.

### **AutoTypeInferenceRule**  
Automatically infers entity types based on KG metadata.

### **MultiHopOrbitInferenceRule**  
Performs multi-hop orbit-based reasoning.

### **DedicsnostVlastnostiRule**  
Handles inheritance of properties across entity hierarchies.

### **TranzitivneRelacieRule**  
Evaluates transitive relations such as `A is B` and `B is C`.

---

## 🔐 Safety Rules  
- ❌ No destructive KG operations  
- 🔒 Deterministic rule evaluation  
- ⚠ Multi-hop depth limits  
- 🛡 No modification of autonomy logic  
- 🧠 Transparent explainability required for all outputs  

---

## 📊 Module Status  
- ✔ Fully implemented  
- ✔ Multi-hop inference verified  
- ✔ WHY reasoning functional  
- ✔ Rule evaluation stable  
- ✔ KG integration confirmed  
- ✔ AUTONOMY workflow connected  
- ✔ Developer diagnostics active  

---

## 🏁 Summary  
ReasoningEngine5 is the deterministic inference core of SIRIUS Local AI (v5.7.0).  
It performs multi-hop reasoning, evaluates rules, and generates transparent WHY explanations used throughout the autonomy workflow.  
The engine is stable, production-ready, and fully integrated with KG ENGINE, AUTONOMY, COLNÍK, EXECUTE, and the UI PANEL.


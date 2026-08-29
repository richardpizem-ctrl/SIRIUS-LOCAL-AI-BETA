# 🔐 SECURITY FAMILY 5.x — Identity Engine 3.1 & Unified Permission Framework  
**Status:** ✔ Active  
**Version:** 5.x (Updated for 5.7.0 UNIFIED)  
**Component:** Security Family  
**Role:** Identity enforcement, permission gating, safety modes, autonomy‑aware and COLNIK‑validated security logic

---

## 🎯 Purpose  
Security Family 5.x is the unified identity and permission enforcement layer of SIRIUS Local AI.  
It ensures that every workflow, automation request, KG mutation, reasoning step, and OS‑level action is validated through identity rules, explainability, COLNIK‑6.x, and AUTONOMY‑6.x.

Security Family protects the workstation from unsafe operations, unauthorized changes, and identity‑restricted actions.

---

## 🧩 Architecture Overview  
**Identity Engine → Security Family → System Agent → AUTONOMY → COLNIK → EXECUTE**

### Core Responsibilities  
- enforce identity modes  
- validate permissions  
- block unauthorized actions  
- integrate explainability  
- provide autonomy‑aware gating  
- validate KG mutations  
- protect UI automation  
- unify PC/Mobile identity logic  

### Key Files  
- `security_family/security_family.py`  
- `security_family/identity_modes.json`  
- `security_family/permissions.json`  
- `IPC_DATA/security_events.json`  

---

## 🔍 Identity Modes  

### **FAMILY Mode**  
Full trusted mode.  
Allows safe workflows, UI automation, KG operations, and system actions.

### **STRANGER Mode**  
Restricted mode.  
Blocks sensitive workflows, KG mutations, OS‑level actions, and UI automation.

### **SCHOOLWORK Mode (Bypass)**  
Special mode for school tasks.  
Allows safe KG operations and reasoning, blocks OS automation.

### **ENVOY 5 Permission Layer**  
Controls external fetch permissions and identity‑restricted operations.

---

## 🔍 Permission Pipeline  

### **1 — Identity Validation**  
Security Family checks:  
- user identity  
- active mode  
- permission level  
- ENVOY restrictions  
- SCHOOLWORK bypass  

If identity validation fails, the action is blocked.

---

### **2 — Explainability Enforcement**  
Every identity decision generates:  
- KG_EXPLAIN  
- KG_EXPLAIN_DEEP  
- identity reasoning  
- permission justification  
- autonomy reasoning  

Explainability is mandatory for all identity‑restricted operations.

---

### **3 — COLNIK‑Validated Security**  
All allow/deny decisions are validated through COLNIK‑6.x:  
- enterprise‑grade safety  
- deterministic routing  
- reversible action checks  
- threat classification  
- explainability logs  

Security Family never allows unsafe identity transitions.

---

### **4 — AUTONOMY‑Aware Gating**  
AUTONOMY‑6.x receives proposals for:  
- identity‑restricted workflows  
- unsafe KG mutations  
- risky OS‑level actions  
- UI automation attempts  

AUTONOMY confirms or denies transitions.

---

### **5 — KG Mutation Protection**  
Security Family validates:  
- entity creation  
- relation creation  
- relation deletion  
- KG imports  
- KG exports  

Unsafe or identity‑restricted KG mutations are blocked.

---

### **6 — UI Automation Protection**  
Security Family blocks:  
- unverified UI actions  
- unsafe automation  
- identity‑restricted UI sequences  
- privilege‑escalation UI operations  

All UI actions require identity validation.

---

## 🧱 Protection Layers  

### **Identity Layer**  
- FAMILY / STRANGER / SCHOOLWORK modes  
- constant‑time identity validation  
- ENVOY 5 permission enforcement  

### **KG Layer**  
- KG mutation validation  
- KG explainability  
- multi‑hop identity reasoning  

### **Automation Layer**  
- UI automation gating  
- OS‑level action validation  
- reversible action enforcement  

### **Autonomy Layer**  
- supervised gating  
- proposal/confirmation logic  
- fallback routing  

---

## 🔐 Safety Rules  
- ❌ No unsafe identity transitions  
- 🔒 COLNIK validation required  
- 🛡 AUTONOMY confirmation required  
- ⚠ Explainability required  
- 🧠 KG‑aware identity reasoning  
- 🔁 Reversible actions enforced  
- 📉 Threat detection always active  

---

## 📊 Module Status  
- ✔ Fully implemented  
- ✔ identity modes stable  
- ✔ permission logic hardened  
- ✔ KG mutation protection active  
- ✔ UI automation protection integrated  
- ✔ COLNIK validation functional  
- ✔ AUTONOMY gating active  
- ✔ PC/Mobile identity logic unified  

---

## 🏁 Summary  
Security Family 5.x is the unified identity and permission enforcement layer of SIRIUS Local AI.  
It validates every workflow, KG mutation, reasoning step, and OS‑level action through identity rules, explainability, COLNIK‑6.x, and AUTONOMY‑6.x.

It ensures that SIRIUS operates Windows 11 **safely, intelligently, identity‑aware, autonomy‑aware, and fully explainably**.


# 🚀 SIRIUS LOCAL AI — Runtime 5.x  
### Next‑Generation Local AI Runtime for Windows 11  
### Offline Knowledge Graph Reasoning • Deterministic OS Automation • Envoy Online Fetch Module

<p align="center">
  <img src="https://img.shields.io/badge/version-5.x-blue">
  <img src="https://img.shields.io/badge/license-MIT-green">
  <img src="https://img.shields.io/badge/platform-Windows%2011-blue">
  <img src="https://img.shields.io/badge/runtime-Intelligent%20Runtime%205.x-purple">
  <img src="https://img.shields.io/badge/local%20AI-100%25-blueviolet">
</p>

---

# 🧠 What’s New in SIRIUS Runtime 5.x  
SIRIUS 5.x represents the **biggest leap in the history of the project**:

### ⭐ 1. Offline Knowledge Graph Reasoning (KG‑Reasoning 1.0)
- reasoning over a local knowledge graph  
- contextual links between entities  
- deterministic inference paths  
- faster responses without models  

### ⭐ 2. Envoy Module 1.0 — Secure Online Fetch (Permission‑Based)
- optional online fetch  
- ASK → FETCH → QUARANTINE → DELIVER  
- works for both PC and mobile  
- identity‑aware security model  
- no automatic requests  

### ⭐ 3. Runtime 5.x Architecture
- new layers for the Knowledge Graph  
- redesigned Reasoning Engine 5.0  
- Workflow Engine 5.0 with KG‑routing  
- System Agent 5.0 with extended rules  

### ⭐ 4. Mobile Sync 2.0
- PC ↔ Mobile SIRIUS communication  
- Envoy fetch on both sides  
- secure LAN Sync protocol  

---

# 🧩 Architecture Diagram (Runtime 5.x)
┌───────────────────────────────┐  
│      Knowledge Graph 5.x      │  
│  (entities, relations, facts) │  
└───────────────┬──────────────┘  
                │  
┌───────────────▼──────────────┐  
│       Reasoning Engine 5.0    │  
│            PRO Layer          │  
└───────────────┬──────────────┘  
                │  
┌───────────────▼──────────────┐  
│       Workflow Engine 5.0     │  
│ KG‑aware routing • deterministic │  
└───────────────┬──────────────┘  
                │  
┌───────────────▼──────────────┐  
│        System Agent 5.0       │  
│ identity rules • OS validation │  
└───────────────┬──────────────┘  
                │  
┌───────────────▼──────────────┐  
│    UI Automation Engine 5.0   │  
│ Win32/UIA/WinRT • deterministic │  
└───────────────────────────────┘  

---

# 🛰 Envoy Module 1.0 — Secure Online Information Fetcher  
**Status:** Plánovaný cieľ pre verziu 5.x  
**Cieľ:** Poskytnúť voliteľný, povolením riadený prístup k online informáciám pri zachovaní 100 % offline architektúry.

Envoy je **riadený externý agent**, ktorý môže vykonať **jednu izolovanú online požiadavku**, ale **len po výslovnom súhlase používateľa**.  
Offline režim zostáva **predvolený**, nedotknutý a plne deterministický.

---

## 🔐 Envoy Security Flow (ASK → FETCH → QUARANTINE → DELIVER)

```
User Request
      ↓
ASK — explicit permission required
      ↓
FETCH — one isolated online request
      ↓
QUARANTINE — sanitize, validate, strip unsafe content
      ↓
DELIVER — safe data passed to Reasoning Engine
```

### Kľúčové princípy Envoy 1.0
- **Nikdy nebeží automaticky**
- **Vždy žiada o povolenie (ASK)**
- **Jednoúčelové, izolované fetch operácie**
- **Všetky dáta prechádzajú karanténou**
- **System Agent overuje celý proces**
- **Offline režim je predvolený a nedotknutý**
- **Rešpektuje identitu používateľa (OWNER / FAMILY / STRANGER)**

---

## 🔁 PC ↔ Mobile Envoy Support (Runtime 5.x)
- PC môže fetchovať pre mobil  
- Mobil môže fetchovať pre PC  
- Oba Envoy moduly používajú rovnaký bezpečnostný tok  
- LAN Sync 2.0 prenáša len **karantenizované dáta**  
- System Agent 5.0 validuje každú fázu  

---

## 🧠 Integrácia Envoy do Runtime 5.x

### **Reasoning Engine 5.0**
- prijíma len karantenizované dáta  
- žiadne nevalidované informácie sa nedostanú do inference pipeline  

### **Workflow Engine 5.0**
- Envoy fetch je len jeden z krokov workflow  
- KG‑routing rozhoduje, či je fetch vôbec potrebný  

### **System Agent 5.0**
- kontroluje identitu  
- kontroluje povolenia  
- kontroluje bezpečnostné pravidlá  
- blokuje neautorizované fetch operácie  

---

## 🛡 Prečo Envoy neporušuje offline architektúru
- Envoy **nie je internetový modul**  
- Envoy **nie je prehliadač**  
- Envoy **nie je AI model**  
- Envoy **nie je automatický fetcher**

Envoy je **riadený, jednorazový, povolením chránený agent**, ktorý:

- nikdy nebeží bez súhlasu  
- nikdy neukladá dáta  
- nikdy neobchádza karanténu  
- nikdy neovplyvňuje offline deterministiku  

---

# 🧠 Offline Knowledge Graph Reasoning (KG‑Reasoning 1.0)

### What it brings:
- reasoning without models  
- instant responses  
- zero latency  
- zero hallucination risk  
- deterministic inference paths  

### Examples:
- “Who is the parent of this entity?”  
- “What concepts are related?”  
- “What is the shortest relation between A and B?”  

---

# 🔁 Workflow Engine 5.0  
- KG‑aware routing  
- multi‑stage deterministic workflows  
- identity‑aware gating  
- Envoy integration  

---

# 🛡 System Agent 5.0  
- extended identity rules  
- OWNER / FAMILY / STRANGER 2.0  
- OS action validation  
- reversibility 3.0  
- Envoy security policies  

---

# 🖱 UI Automation Engine 5.0  
- faster UIA/Win32/WinRT routing  
- KG‑enhanced UI matching  
- deterministic fallbacks  
- System Agent validation  

---

# 📦 Knowledge Packs 5.x  
- KG‑ready structure  
- integrity validation 2.0  
- faster lookups  
- expanded school, home, diagnostic packs  

---

# 🌍 Mobile Sync 2.0  
- PC ↔ Mobile SIRIUS communication  
- Envoy fetch on both sides  
- secure LAN protocol  
- identity‑aware synchronization  

---

# 📘 Installation (Runtime 5.x)
*(empty — will be filled after 5.0.0 release)*

---

# 📄 License  
MIT License.

---

# 🤝 Contributions  
Pull requests are welcome.

---

# 🧭 Roadmap (5.x → 6.x)
- **5.0.0** — Knowledge Graph Reasoning  
- **5.1.0** — Envoy 1.1 + Mobile Sync 2.1  
- **5.2.0** — KG‑Enhanced UI Automation  
- **6.0.0** — Self‑Repair Layer 2.0  

---

# 📦 Installer Note  
Installers for SIRIUS Runtime 5.x will be released **in parallel with the final GAMA 5.x versions**.  
They will include the final module structure, stable API layers, System Agent 5.0, Envoy 1.0, UI Automation Engine 5.0, and Knowledge Graph Runtime 1.0.  
They will be published **immediately after the last GAMA milestone is completed** to ensure 100% compatibility.

---

# 🏁 End of README_v5.md

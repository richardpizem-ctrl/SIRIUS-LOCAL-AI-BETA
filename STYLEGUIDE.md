# 12. NEW IN VERSION 4.5.0 PRO — System‑Intelligent Styleguide Expansion

Version **4.5.0 PRO** rozširuje pôvodný STYLEGUIDE o nové pravidlá pre:

- System Intelligence Layer 4.5  
- System Agent 4.5  
- UI Automation Engine 4.5  
- Security Family 4.5  
- Workflow Engine 4.5  
- Knowledge Packs 4.5  

Všetky staršie pravidlá ostávajú platné.  
4.5.0 PRO iba dopĺňa nové povinné normy pre deterministickú, systémovo‑inteligentnú architektúru.

---

# 12.1 Core Principles (Expanded for 4.5.0 PRO)

### NEW (4.5.0 PRO)
- všetky systémové akcie musia byť **prediktívne validované**  
- System Intelligence Layer musí byť konzultovaný pred OS‑úrovňovými workflowmi  
- identity‑aware logika musí byť **konzistentná naprieč všetkými modulmi**  
- žiadne workflow nesmie bežať v **rizikovom OS stave**  
- všetky moduly musia podporovať **deterministické fallbacky 2.0**  
- reasoning musí byť **bounded, cacheovaný a pack‑aware 3.0**  
- UI Automation musí používať **fuzzy matching 4.5**  
- System Agent 4.5 je **jediný validátor OS akcií**  

---

# 12.2 Naming Conventions (Expanded for 4.5.0 PRO)

### NEW Reserved Names (4.5.0 PRO)
- `SystemIntelligenceLayer`  
- `PredictiveSafetyEngine`  
- `OSHealthMonitor`  
- `RiskAnalyzer`  
- `IdentityGatekeeperV2`  
- `DeterministicFallbackEngineV2`  

Tieto názvy sú **rezervované** a nesmú byť použité na iné účely.

---

# 12.3 File & Folder Structure (Expanded for 4.5.0 PRO)

### NEW Folders (4.5.0 PRO)
/system_intelligence  
/system_intelligence/diagnostics  
/system_intelligence/predictive  
/system_intelligence/risk_models  
/system_agent_v2  
/ui_automation/fallback_v2  
/security_family_v2  

### NEW Rules (4.5.0 PRO)
- System Intelligence Layer musí byť izolovaný od UI Automation  
- System Agent 4.5 musí byť jediný modul s právom validovať OS akcie  
- Workflow Engine 4.5 musí konzultovať OS stav pred vykonaním workflowu  
- žiadny modul nesmie obchádzať System Intelligence Layer pri OS‑úrovňových rozhodnutiach  

---

# 12.4 Function Length (Expanded for 4.5.0 PRO)

### NEW (4.5.0 PRO)
OS‑úrovňové funkcie musia byť rozdelené na:

- `precheck_identity()`  
- `precheck_system_state()` ← NEW  
- `precheck_risk_level()` ← NEW  
- `execute_action()`  
- `postcheck_reversibility()`  
- `postcheck_system_integrity()` ← NEW  

Maximálna dĺžka OS‑úrovňovej funkcie: **45 riadkov**.

---

# 12.5 Comments (Expanded for 4.5.0 PRO)

### NEW (4.5.0 PRO)
Komentáre musia obsahovať:

- prediktívne bezpečnostné dôvody  
- OS‑stavové podmienky  
- rizikové faktory  
- identity‑aware rozhodnutia  
- fallback 2.0 logiku  
- prečo bol workflow zastavený alebo presmerovaný  

---

# 12.6 Error Messages (Expanded for 4.5.0 PRO)

### NEW (4.5.0 PRO)
- `"OS action blocked – unsafe system state detected."`  
- `"Operation rejected – predictive risk level too high."`  
- `"System Agent 4.5: identity validation failed."`  
- `"Workflow halted – system integrity not guaranteed."`  
- `"UI action denied – fallback 2.0 engaged."`  

---

# 12.7 Security Rules in Code (Expanded for 4.5.0 PRO)

### NEW (4.5.0 PRO)
- všetky OS akcie musia prejsť cez `SystemAgentV2`  
- System Intelligence Layer musí byť konzultovaný pred workflow spustením  
- žiadne workflow nesmie bežať v rizikovom OS stave  
- žiadne priame Win32/UIA/WinRT volania  
- žiadne implicitné OS zmeny  
- žiadne persistentné hooky  
- žiadne background OS manipulácie  
- žiadne obchádzanie identity‑aware logiky  

---

# 12.8 Testing Requirements (Expanded for 4.5.0 PRO)

### NEW (4.5.0 PRO)
System Intelligence Layer testy musia obsahovať:

- OS health detection tests  
- risk prediction tests  
- unsafe state prevention tests  
- workflow blocking tests  
- fallback 2.0 tests  
- System Agent 4.5 integration tests  

UI Automation 4.5 testy musia obsahovať:

- fuzzy matching 4.5 tests  
- deterministic fallback 2.0 tests  
- identity‑aware UI action tests  
- WinCapabilities 4.5 routing tests  

---

# 12.9 Logging Rules (Expanded for 4.5.0 PRO)

### NEW (4.5.0 PRO)
System Intelligence Layer logging:

- nikdy neukladať OS handles  
- nikdy neukladať citlivé systémové cesty  
- logovať iba semantické akcie  
- logovať OS stav ako kategóriu (SAFE / WARNING / RISK)  
- logovať prediktívne rizikové faktory  
- logovať fallback 2.0 aktiváciu  

---

# 12.10 Module Boundaries (Expanded for 4.5.0 PRO)

### NEW (4.5.0 PRO)
- **System Agent 4.5 je jediný validátor OS akcií**  
- **System Intelligence Layer 4.5 je jediný modul, ktorý môže hodnotiť OS stav**  
- **UI Automation Engine 4.5 musí používať fallback 2.0**  
- **Workflow Engine 4.5 nesmie spustiť workflow v rizikovom OS stave**  
- **Security Family 4.5 musí byť konzultovaná pred každou OS akciou**  

---

# Document Status (Updated)

**Version:** 3.0.0 (Expanded to include 4.2.0, 4.3.0, 4.4.0 PRO, and **4.5.0 PRO**)  
This styleguide now includes all deterministic, OS‑aware, system‑intelligent rules introduced in Runtime 4.5.0 PRO.

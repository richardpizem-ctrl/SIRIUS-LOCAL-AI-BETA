# 🎛 UI PANEL 6.x — 4-Panel Futuristic Neon Web Suite (Port 8080)
**Status:** ✔ Stabilizované a aktívne integrované (Active & Stabilized)  
**Version:** 6.x (Stabilized for 5.9.0 UNIFIED)  
**SIRIUS Local AI Version:** 5.9.0 UNIFIED  
**Component:** 4-Panel UI Suite & Terminal Decoupling Controller  
**Role:** Unified browser-based interface running natively on local port 8080 under single-process orchestrator supervision with automated terminal state decoupling (`currentModule = "none"`)

---

## 🎯 Purpose  
UI PANEL 6.x je moderné webové rozhranie s futuristickou neónovou estetikou, slúžiace ako primárna interakčná a riadiaca vrstva pre runtime **SIRIUS Local AI v5.9.0**.  
Beží natívne ako jednoprocesový démon priamo cez `sirius_orchestrator.py` na lokálnom porte **8080**, čím definitívne eliminuje kolízie soketov a zámky súborov na disku.

Rozhranie implementuje plne oddelenú architektúru štyroch špecializovaných panelov (**Duplicates**, **Triage**, **Navigation**, **Terminal**) a zavádza kľúčový bezpečnostný mechanizmus **Terminal State Decoupling**: pri vymazaní vstupu alebo prerušení príkazu sa kontext terminálu automaticky resetuje na `currentModule = "none"`, čo natrvalo zabraňuje tomu, aby bežné konverzačné dopyty alebo entity prepadávali do systémového shellu operačného systému Windows 11.

---

## 🧩 Architecture Overview  
**Browser Console (Port 8080) → Terminal Decoupling Guard (`currentModule = "none"`) → sirius_orchestrator.py → PanelAPI [ÁNO/NIE] → RuntimeCore 5.9.0 → InputParser5 → Multi-Alias KG (`autosave_kg.json`) → COLNIK-6.x / AUTONOMY 6.x → EXECUTE 6.x**

### Core Responsibilities  
- natívna obsluha rozhrania cez lokálny HTTP/WebSocket server na porte 8080 v rámci jedného procesu  
- okamžitý reset modulu (`currentModule = "none"`) pri zmazaní vstupu, garantujúci izoláciu od hostiteľského OS shellu  
- vizuálna kontrola a správa karanténneho radu v priečinku `COLNIK-6.x/triage`  
- neinvazívne zobrazovanie duplicitných súborov so striktným vynútením politiky `REPORT_ONLY`  
- asynchrónne zobrazovanie hardvérovej telemetrie (vyťaženie CPU, RAM, Disk pod 1 % réžie cez Guard)  
- riadenie interaktívnych schvaľovacích slučiek `PanelAPI` (`[ÁNO/NIE]`) s garanciou nulovej rekurencie návrhov pre už potvrdené entity  
- plynulé prepínanie medzi používateľským (User) a vývojárskym (Developer) zobrazením  

### Key Files & Endpoints  
- `ui_suite_8080/index.html` (hlavný dashboard)  
- `ui_suite_8080/neon_theme.css` (futuristický neónový vizuál)  
- `ui_suite_8080/app.js` (riadenie stavu modulov a WebSocket most)  
- `ui_suite_8080/terminal_decoupling_guard.js` (uvoľňovanie kontextu na `none`)  
- `ORCHESTRATOR/sirius_orchestrator.py` (démon na porte 8080)  
- `PANEL_API/panel_api.py` (obsluha promptov `[ÁNO/NIE]`)  
- `http://127.0.0.1:8080` (lokálny prístupový bod)  

---

## 🖥 4-Panel Suite Layout (Port 8080)  

### **1. Duplicates Panel (Správa duplicít)**  
- prehľadná vizuálna inventúra duplicitných súborov na lokálnom úložisku  
- striktné bezpečnostné pravidlo: **iba REPORT_ONLY** (žiadne automatické mazanie bez explicitného autorizovaného potvrdenia)  
- priamy odkaz na metriky diskového priestoru dodávané modulom Guard  

### **2. Triage Panel (Karanténny rad COLNIK-6.x/triage)**  
- živý inšpekčný panel pre zachytené, neoverené alebo neznáme vstupy  
- správa normalizovaných dát z ENVOY 5 s kontrolou doménového štítu (`NonBioDomainShield`)  
- tlačidlá pre manuálne uvoľnenie (Release) alebo bezpečné vymazanie (Discard) karanténneho payloadu  

### **3. Navigation Panel (Navigácia a stav subsystémov)**  
- deterministické prepínanie medzi vetvami: Runtime Core, Multi-Alias KG, Envoy Researcher, Security Vault a Autonomy  
- živé neónové indikátory zdravia:  
  - **Orchestrator:** port 8080 aktívny  
  - **Knowledge Graph:** `autosave_kg.json` synchronizovaný (Dual-Key persistence)  
  - **COLNIK-6.x Gate:** Standard & High-Performance IPC pripravené  
  - **Guard Telemetry:** CPU, RAM, Disk v norme  
  - **TimeCore:** heartbeat stabilný  

### **4. Terminal Panel (Izolovaná príkazová konzola)**  
- interaktívny neónový terminál s automatickou izoláciou shellu:  
  - ak používateľ vymaže vstupný riadok (Backspace/Clear) alebo dokončí dopyt, skript okamžite odošle signál `currentModule = "none"`  
  - zabraňuje nechcenému spusteniu textových dotazov ako systémových príkazov vo Windows PowerShell/CMD  
  - plná podpora viacslovných fráz (`InputParser5`) a zobrazenie odvodzovacích stromov (`KG_EXPLAIN_DEEP`)  

---

## 🔀 Prevádzkové režimy (Modes)  

### **User Mode (Bežný používateľ)**  
- čisté, vysoko kontrastné neónové zobrazenie  
- zamerané na dialóg, overovanie faktov, školské dopyty (garantovaný `SCHOOLWORK` bypass) a prehliadanie znalostí  
- interaktívne potvrdzovanie nových entít cez dialóg `PanelAPI` (`[ÁNO/NIE]`)  
- úplne skryté systémové a rizikové OS operácie  

### **Developer Mode (Vývojár a audit)**  
- podrobné trasovanie procesov orchestrátora a pamäťového IPC  
- vizualizácia hierarchických dôkazových stromov (ASCII + HTML proof trees)  
- ladenie multi-aliasov v Knowledge Graph (`kg add alias`, `kg debug stats`, `kg release`)  
- priamy prístup k telemetrii Guard a detailom rozhodnutí COLNIK-6.x (ALLOW / DENY / TRIAGE)  
- monitorovanie karanténneho priečinka `COLNIK-6.x/triage`  

---

## 🎨 Design & Security Principles  
- **Futuristic Neon Aesthetic:** ergonomický tmavý podklad s neónovými akcentmi a vysokým kontrastom pre dlhodobú prácu  
- **Terminal State Decoupling:** nulová šanca na prenos konverzačných vstupov do hostiteľského operačného systému  
- **Single-Process Sovereignty:** celý server aj rozhranie sú spravované v rámci jediného procesu `sirius_orchestrator.py`  
- **Zero Recurrence Assurance:** po schválení entity v paneli sa už nikdy nezobrazí opakovaný dotaz na učenie  
- **Strict Non-Destructive Defaults:** panely nepovoľujú deštruktívne zápisy na disk bez viacúrovňového overenia  

---

## 📊 Module Status (v5.9.0)  
- ✔ **Plne stabilizované a funkčné (Production-Ready)**  
- ✔ Architektúra 4 panelov (`Duplicates`, `Triage`, `Navigation`, `Terminal`) implementovaná  
- ✔ Bezpečnostný reset `currentModule = "none"` aktívny a otestovaný  
- ✔ Integrované na lokálny port 8080 pod jedným procesom `sirius_orchestrator.py`  
- ✔ Živé prepojenie s `PanelAPI` (`[ÁNO/NIE]`) a zobrazenie odvodzovacích stromov XAI  
- ✔ Vizuálna integrácia karantény `COLNIK-6.x/triage` dokončená  
- ✔ Telemetria Guard (CPU, RAM, Disk) aktívna s réžiou < 1 %  

---

## 🏁 Summary  
UI PANEL 6.x v architektúre **SIRIUS Local AI v5.9.0 UNIFIED** predstavuje plne dokončený, bezpečný a vizuálne prepracovaný 4-panelový webový dashboard dostupný na adrese `http://127.0.0.1:8080`.  
Zabezpečuje absolútne oddelenie používateľského vstupu od systémového shellu, vizualizuje stav znalostného grafu a karantény a poskytuje používateľovi aj vývojárovi dokonalú kontrolu nad autonómnym behom systému — **deterministicky, bezpečne, vysvetliteľne a 100 % offline**.

# 🎛 UI PANEL 6.x — 4-Panel Futuristic Neon Web Suite (Port 8080)
**Status:** ✔ Active & Stabilized  
**Version:** 6.x (Stabilized for 5.9.5 UNIFIED)  
**SIRIUS Local AI Version:** 5.9.5 UNIFIED  
**Author / Architecture:** Richard Pizem  
**Component:** 4-Panel UI Suite, Terminal Decoupling Controller, COLNÍK Guard Shell Filter, Professor Validator Middleware & Safe Trash Bridge  
**Role:** Unified browser-based interface running natively on local port 8080 under single-process orchestrator supervision with embedded TerminalAssistant, TimeCore latency profiling, COLNÍK Guard (0.0s hard blocks), Professor Middleware quality gating (PASS / WARN / REJECT), HitL Safe Trash management, and automated terminal state decoupling (`currentModule = "none"`)

---

## 🎯 Purpose  
UI PANEL 6.x is a modern web interface with a futuristic neon aesthetic, serving as the primary interaction and presentation layer for the **SIRIUS Local AI v5.9.5** runtime, architected by Richard Pizem.  
It runs natively as a single-process daemon directly through `sirius_orchestrator.py` on local port **8080** with embedded `TerminalAssistant` and `TimeCore`, permanently eliminating socket collisions and disk-level file locking contention.

The interface implements a fully decoupled architecture across four specialized panels (**Duplicates**, **Triage**, **Navigation**, **Terminal**), integrates entry-level **Token Guard** filtering (`@#$%^&*` drop), pre-processing spellcheck (`spellcheck_engine.py`), greedy trailing punctuation stripping (`.rstrip("?")`), supports confirmation state latching across conversation turns, enforces **COLNÍK Guard** shell protection (0.0s hard blocks on destructive commands like `format` and `diskpart`), and manages the **Human-in-the-Loop Safe UI Trash** pipeline (`GET /trash`).

Výstup do UI je striktne podriadený vrstve **Professor Middleware Layer** (`Professor Validator`): Runtime Core môže v Znalostnom Grafe nájsť čokoľvek, ale Professor rozhodne (cez stavy **PASS / WARN / REJECT**), či a v akej forme sa výstup používateľovi vôbec zobrazí. Zároveň interface vynucuje kľúčový mechanizmus **Terminal State Decoupling**: vymazanie vstupného poľa alebo zrušenie príkazu okamžite resetuje kontext terminálu na `currentModule = "none"`, čím permanentne bráni úniku konverzačných dotazov do hostiteľského shellu Windows 11.

---

## 🧩 Architecture Overview  
[ UŽÍVATEĽ / UI PANEL (Port 8080) ]  
          │ (Zadanie dopytu / Príkaz)  
          ▼  
Token Guard (@#$%^&* drop) → spellcheck_engine.py (Korekcia preklepov a diakritiky)  
          ▼  
sirius_orchestrator.py (Port 8080 s TerminalAssistant + TimeCore)  
          ▼  
COLNÍK Guard (0.0s Hard Block) → Terminal Decoupling Guard (currentModule = "none")  
          ▼  
RuntimeCore 5.9.5 (Vyhľadávanie v autosave_kg.json / autosave_kg_en.json)  
          │ (Surová odpoveď / Dáta z grafu)  
          ▼  
┌────────────────────────────────────────────────────────┐  
│                PROFESSOR MIDDLEWARE LAYER              │  
│                                                        │  
│   1. Professor Cleaner / grammar_engine.py             │  
│   2. Professor Validator (PASS / WARN / REJECT)        │  
│   3. Professor Summarizer / professor_miner.py         │  
└────────────────────────────────────────────────────────┘  
          │ (Filtrovaná, obohatená a validovaná odpoveď)  
          ▼  
PanelAPI [ÁNO/NIE] / [YES/NO] → COLNIK-6.x / AUTONOMY 6.x → HitL Safe Trash (GET /trash)  
          ▼  
[ UI PANEL (V2) — Vykreslenie výsledku používateľovi ]  

---

### Core Responsibilities  
- hostovať webové rozhranie lokálne cez HTTP/WebSocket na porte 8080 v rámci jedného procesu s TerminalAssistant a TimeCore  
- zahodiť škodlivé vstupné tokeny (@#$%^&*) okamžite na vstupe cez Token Guard a normalizovať text cez spellcheck_engine  
- sprostredkovať výstup až po overení cez **Professor Validator** (prepustenie pri PASS, vizuálny príznak pri WARN, zablokovanie výstupu pri REJECT)  
- vykonať okamžitý reset modulu (currentModule = "none") pri vymazaní vstupu na zaistenie úplnej izolácie od shellu OS  
- smerovať terminálové príkazy cez COLNÍK Guard: 0.0s okamžité blokovanie zakázaných príkazov (format, diskpart, rmdir /s, del /f /s /q c:, drop database)  
- spravovať Human-in-the-Loop Safe UI Trash: zachytávať priame mazanie súborov z disku a presúvať ich do karantény pre manuálnu kontrolu (GET /trash)  
- poskytovať vizuálnu kontrolu a správu karanténneho radu v COLNIK-6.x/triage a dohliadať na strop posuvného okna karantény (100 súborov v COLNIK-6.x/envoy/quarantine/)  
- zabezpečovať neinvazívny audit duplicitných súborov s prísnym uplatňovaním politiky REPORT_ONLY  
- vykresľovať telemetriu hardvéru a profilovanie latencie príkazov asynchrónne (Guard CPU, RAM, Disk zaťaženie pod 1 %, TimeCore cycle_delta())  
- riadiť interaktívne potvrdzovacie slučky cez PanelAPI ([ÁNO/NIE] / [YES/NO]) s potvrdeným stavom latchingu a nulovou redundanciou návrhov  
- umožňovať plynulé prepínanie medzi používateľským a vývojárskym režimom naprieč izolovanými jazykovými partíciami grafu (SK / EN)  

### Key Files & Endpoints  
- ui_suite_8080/index.html (hlavný dashboard)  
- ui_suite_8080/neon_theme.css (futuristický neónový vizuál)  
- ui_suite_8080/app.js (manažment stavov modulov a WebSocket most)  
- ui_suite_8080/terminal_decoupling_guard.js (uvoľnenie kontextu na "none")  
- orchestrator/terminal_assistant.py (gatekeeper shell príkazov a profilovač latencie)  
- colnik_6_x/colnik_guard.py (klasifikačná matica príkazov)  
- runtime5/token_guard.py (filter symbolových injekcií)  
- runtime5/spellcheck_engine.py (predspracovanie diakritiky a preklepov)  
- runtime5/professor_validator.py (kvalitatívna brána PASS / WARN / REJECT)  
- runtime5/grammar_engine.py (Professor Cleaner & extrakcia trojíc)  
- runtime5/professor_miner.py (Professor Summarizer)  
- filesystem/safe_trash_quarantine.py (správca karantény vymazaných súborov)  
- runtime5/envoy_quarantine_5.py (rotátor posuvného okna karantény na 100 súborov)  
- ORCHESTRATOR/sirius_orchestrator.py (jednoprocesový démon na porte 8080)  
- PANEL_API/panel_api.py (spracovanie výziev [ÁNO/NIE] / [YES/NO])  
- http://127.0.0.1:8080 (lokálny endpoint)  
- GET /trash (rozhranie pre kontrolu a bezpečné vysypanie koša)  

---

## 🎓 Professor Middleware Layer (Kvalitatívna kontrola výstupu)

Medzi Runtime Core a UI Panelom stojí validačná vrstva **Professor**, ktorá garantuje, že do používateľského rozhrania sa nedostanú chybné, protirečivé alebo neúplné fakty:

1. **Professor Cleaner (`grammar_engine.py`):**  
   - Normalizuje vyťažené relácie a trojice, čistí stop-slová a izoluje zvratné zámená (*sa/si*).  
   - Filtruje jednopísmenové spojky pre SK a neurčité členy pre EN bez poškodenia zmyslu viacslovných objektov.

2. **Professor Validator (Rozhodovacia logika):**  
   - **PASS (Vysoká kvalita faktov):** Fakty sú konzistentné, overené a kompletné. Odpoveď je okamžite uvoľnená do UI.  
   - **WARN (Použiteľné, ale neisté):** Fakty spĺňajú základné kritériá, ale majú nižšiu mieru istoty. Odpoveď je odoslaná s vizuálnym neónovým príznakom neistoty.  
   - **REJECT (Neúplné, poškodené alebo protirečivé):** Odpoveď sa vôbec nezostaví ani nezobrazí. UI dostane štruktúrovanú správu o zamietnutí:
     ```json
     {
       "status": "REJECT",
       "reason": "INCOMPLETE_FACTS"
     }
     ```
     *(Alternatívne dôvody: `"LOW_CONFIDENCE"`, `"CONTRADICTION"`)*

3. **Professor Summarizer (`professor_miner.py`):**  
   - Zabezpečuje syntézu viacerých faktických uzlov do stručného a prehľadného výstupu pre UI.

---

## 🖥 4-Panel Suite Layout (Port 8080)  

### 1. Duplicates Panel (Manažment duplicitných súborov & Safe Trash)  
- vizuálny prehľad duplicitných súborov nájdených na lokálnom disku  
- prísne uplatňovanie pravidla REPORT_ONLY (žiadne automatické mazanie bez zásahu používateľa)  
- integrácia Human-in-the-Loop Safe Trash: súbory smerujú do karantény a vyžadujú manuálne schválenie cez `GET /trash`  
- priame prepojenie na Guard metriky diskového úložiska  

### 2. Triage Panel (Karanténny rad COLNIK-6.x/triage & Sledovanie posuvného okna)  
- sledovanie zachytených, neoverených alebo poškodených dát v reálnom čase  
- monitorovanie limitu posuvného okna (striktne maximálne 100 JSON záznamov v `COLNIK-6.x/envoy/quarantine/`)  
- kontrola normalizovaných dát z ENVOY 5 cez Non-Bio Domain Shield (`NonBioDomainShield`)  
- explicitné tlačidlá na manuálne uvoľnenie (Release) alebo bezpečné vyradenie (Discard) karanténnych objektov  

### 3. Navigation Panel (Navigácia, Zdravie subsystémov & Duálny KG)  
- deterministické prepínanie vetiev: Runtime Core, Duálny KG (`autosave_kg.json` & `autosave_kg_en.json`), Envoy Researcher, Bezpečnostný Vault a Autonómia  
- dynamické prepínanie jazykového kontextu (SK / EN) do izolovaných grafov  
- stavové indikátory neónového rozhrania:  
  - Orchestrator: port 8080 aktívny s TerminalAssistant & TimeCore  
  - Knowledge Graph: duálna partícia synchronizovaná (Lossless `kg merge` a `KG_VERIFY` aktívne)  
  - Professor Validator: stav filtrovania a priepustnosti (PASS / WARN / REJECT)  
  - COLNÍK Guard: ochrana príkazov shellu aktívna (0.0s blokovanie)  
  - COLNIK-6.x Gate: štandardný aj IPC režim v prevádzke  
  - Guard Telemetria: vyťaženie CPU, RAM a disku v norme (< 1 % réžia)  
  - TimeCore: stabilný pulz `cycle_delta()` a profilovač latencie  

### 4. Terminal Panel (Izolovaná príkazová konzola & COLNÍK Guard)  
- interaktívny neónový terminál s automatickým oddelením stavu (Decoupling):  
  - vymazanie vstupu (Backspace/Clear) okamžite nastaví `currentModule = "none"`  
  - zabraňuje tomu, aby bežné konverzačné otázky unikli ako príkazy do systémového shellu Windows (PowerShell/CMD)  
  - Token Guard na vstupe zahadzuje reťazce s nepovolenými znakmi (`@#$%^&*`)  
  - orezávanie otáznikov (`.rstrip("?")`) zabezpečuje čisté hľadanie v entitách  
  - COLNÍK Guard v čase 0.0s zastavuje deštruktívne príkazy (`format`, `diskpart`, `rmdir /s`, `del /f /s /q c:`, `drop database`)  
  - viacstupňový dekodér výstupu (UTF-8 -> CP1250 -> CP852) garantuje nepoškodenú diakritiku  
  - podpora viacslovných fráz cez InputParser5 a zobrazenie stromov odvodenia (`KG_EXPLAIN_DEEP`)  

---

## 🔀 Operating Modes  

### User Mode (Bežná prevádzka)  
- čisté neónové rozhranie zamerané na dialóg, overovanie faktov, školské úlohy (SCHOOLWORK bypass) a skúmanie znalostného grafu  
- všetky výstupy sú overené validačnou vrstvou Professor  
- interaktívne potvrdzovanie nových entít cez PanelAPI (`[ÁNO/NIE]` / `[YES/NO]`) s latchingom stavu  
- systémové administrátorské príkazy a shell sú úplne skryté a zablokované  

### Developer Mode (Inžiniersky a auditný režim)  
- podrobný tracing orchestrátora, profilovanie latencie TimeCore (`cycle_delta()`) a zber IPC kanálov  
- správa natívneho zlučovania entít (`kg merge <src> into <tgt>`) a taxonomickej dedukcie (`KG_VERIFY`)  
- zobrazenie stromov dôkazov (ASCII a HTML proof trees) z `KG_EXPLAIN_DEEP`  
- diagnostika vrstvy Professor Validator: detailné dôvody pre REJECT a WARN stavy  
- nástroje na správu aliasov (`kg add alias`, `kg merge`, `kg reverse location`, `kg debug stats`, `kg release`)  
- priamy prístup k hardvérovej telemetrii Guard a colným verdiktom COLNIK-6.x (ALLOW / DENY / TRIAGE)  
- živá kontrola karantény `COLNIK-6.x/triage` a Safe UI Trash (`GET /trash`)  

---

## 🎨 Design & Security Principles  
- **Futuristic Neon Aesthetic:** ergonomické tmavé pozadie kombinované s vysoko kontrastnými prvkami pre dlhodobú prácu  
- **Professor Quality Gating:** Runtime Core síce vyhľadá dáta, ale Professor Middleware autoritatívne určí, či sa fakt smie zobraziť používateľovi  
- **Terminal State Decoupling:** nulová šanca na únik konverzačného textu do shellu operačného systému (`currentModule = "none"`)  
- **COLNÍK Guard Interception:** okamžité zastavenie zakázaných shell príkazov v 0.0s  
- **Human-in-the-Loop Safe Trash:** blokovanie trvalého mazania; presun do karantény s manuálnou kontrolou cez `GET /trash`  
- **Token Guard Entry Sanitization:** okamžité zahadzovanie injekčných sekvencií (`@#$%^&*`) na prahu UI  
- **Confirmation State Latching:** udržanie ID čakajúceho návrhu v pamäti naprieč krokmi dialógu  
- **Dual-Language Sovereignty:** prísne oddelené slovenské a anglické databázy bez miešania faktov  
- **Single-Process Sovereignty:** orchestrátor, UI server, TerminalAssistant aj TimeCore bežia v jedinom procese `sirius_orchestrator.py`  
- **Zero Recurrence Assurance:** potvrdené fakty a odvodené taxonómie sa už nikdy znova nepýtajú používateľa na potvrdenie  
- **Strict Non-Destructive Defaults:** predvolený bezpečný režim REPORT_ONLY pre prácu so súbormi  

---

## 📊 Module Status (v5.9.5)  
- ✔ Plne stabilizované a pripravené na produkciu  
- ✔ Autor architektúry: Richard Pizem  
- ✔ 4-panelové rozhranie (Duplicates, Triage, Navigation, Terminal) nasadené  
- ✔ Bezpečnostný reset `currentModule = "none"` aktívny  
- ✔ Jednoprocesový beh na porte 8080 (`sirius_orchestrator.py` s TerminalAssistant a TimeCore)  
- ✔ Professor Middleware Layer integrovaná (Cleaner, Validator PASS/WARN/REJECT, Summarizer)  
- ✔ COLNÍK Guard 0.0s blokovanie deštruktívnych príkazov overené  
- ✔ Human-in-the-Loop Safe UI Trash funkčný (`GET /trash`)  
- ✔ Token Guard a orezávanie otáznikov (`.rstrip("?")`) aktívne  
- ✔ Posuvné okno karantény (strop 100 súborov) aktívne  
- ✔ PanelAPI potvrdzovacie slučky (`[ÁNO/NIE]` / `[YES/NO]`) s latchingom stavu funkčné  
- ✔ Duálna vizualizácia grafu overená (`autosave_kg.json` a `autosave_kg_en.json`)  
- ✔ Vizuálna integrácia karanténneho radu `COLNIK-6.x/triage` dokončená  
- ✔ Guard telemetria hardvéru (CPU, RAM, Disk) v prevádzke s réžiou < 1 %  

---

## 🏁 Summary  
UI PANEL 6.x v rámci architektúry **SIRIUS Local AI v5.9.5 UNIFIED**, navrhnutej Richardom Pizemom, predstavuje ucelené, bezpečné a neónovo ladené webové rozhranie na adrese `http://127.0.0.1:8080`.  
Garantuje úplné oddelenie používateľského vstupu od hostiteľského shellu, blokuje deštruktívne príkazy v 0.0s cez COLNÍK Guard, presmerováva mazanie súborov do Safe Trash karantény, udržiava strop karantény na 100 súboroch a **cez validačnú vrstvu Professor prísne kontroluje kvalitu a konzistenciu každého jedného zobrazeného faktu** — **deterministicky, bezpečne, vysvetliteľne a 100 % offline**.

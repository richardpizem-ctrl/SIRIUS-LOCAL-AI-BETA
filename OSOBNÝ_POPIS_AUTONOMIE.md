AUTONÓMIA – 6 PILIEROV SIRIUS 6.x
1️⃣ Autonómia poznania PC
Autonómia musí dokonale poznať prostredie, v ktorom pracuje.
Musí vedieť identifikovať:

hardvér (CPU, RAM, GPU, disky)

softvér (OS, služby, procesy)

priečinky a ich štruktúru

konfigurácie SIRIUS-u

KG stav

ENVOY stav

SelfRepair stav

Autonómia bez znalosti prostredia je slepá.
Toto je základ všetkého.

2️⃣ Autonómia detekcie nebezpečných a poškodených súborov
Autonómia musí vedieť:

čítať obsah súborov

zisťovať poškodenie

zisťovať nebezpečný obsah

zisťovať duplicity

zisťovať konflikty

zisťovať neúplné alebo chybné súbory

nahlásiť incident

navrhnúť riešenie

Autonómia nikdy nesmie sama konať.
Len hlási a navrhuje.

3️⃣ Autonómia navigácie používateľa po PC
Autonómia musí vedieť otvoriť:

Centrum pripomienok (CTRL+F)

Správcu úloh (CTRL+SHIFT+ESC)

Prieskumník (WIN+E)

Nastavenia (WIN+I)

Ovládací panel (control.exe)

Sieťové pripojenia (ncpa.cpl)

Správu diskov (diskmgmt.msc)

Správcu zariadení (devmgmt.msc)

Ale vždy len:

Autonómia → návrh úlohy → COLNÍK → Workflow → OS

Autonómia nevykoná nič sama.

4️⃣ Autonómia TRIAZ priečinkov (A → B podľa typu)
Autonómia musí vedieť:

identifikovať typ priečinka

zistiť, či je na správnom mieste

navrhnúť presun

presun vykonať až po COLNÍKOVI

aktualizovať registry SIRIUS-u

Príklady:

SIRIUS-LOCAL-AI-BETA → presun do hlavného pracovného priečinka

KG backups → presun do /backups

runtime moduly → presun do /runtime

Autonómia len navrhne, používateľ rozhodne.

5️⃣ Autonómia TRIAZ duplicít (čítanie – porovnanie – presun – rozhodnutie)
Autonómia musí vedieť:

nájsť duplicitu

prečítať obsah súborov

porovnať obsah

zistiť identitu alebo podobnosť

navrhnúť presun duplicity do UI koša

zobraziť duplicitu v UI paneli

počkať na rozhodnutie používateľa

Používateľ rozhodne:

Vymazať

Ponechať

Autonómia nikdy sama nevymaže.

6️⃣ Autonómia terminálu a kódovania
Autonómia musí vedieť:

otvoriť terminál v správnom priečinku

pripraviť príkazy

pomôcť pri kódovaní

pomôcť pri testovaní

pomôcť pri ladení

generovať alternatívny kód

porovnávať verzie kódu

navrhovať optimalizácie

Ale:

Príkaz sa môže spustiť až po schválení používateľom.
Autonómia → návrh úlohy → COLNÍK → Workflow → OS

Autonómia nikdy nesmie sama spustiť príkaz.

ZÁKLADNÝ ZÁKON AUTONÓMIE SIRIUS 6.x
Autonómia nikdy nekoná sama.
Autonómia len predostrie všetko pred nos používateľovi.
Používateľ rozhoduje.
COLNÍK povoľuje.
Workflow vykoná.

Toto je pevná súčasť architektúry SIRIUS 6.x.
AUTONOMY/
│
├── core/                       ← mozog autonómie
│   ├── monitor.py              ← pozorovanie PC / SIRIUS
│   ├── analyzer.py             ← analýza monitorovaných dát
│   ├── proposer.py             ← tvorba návrhov
│   └── json_format.py          ← jednotný Request/Response formát
│
├── modules/                    ← schopnosti autonómie
│   ├── navigation.py
│   ├── triage_folders.py
│   ├── triage_duplicates.py
│   ├── terminal_assistant.py
│   └── detection.py
│
├── ipc/                        ← hranica medzi procesmi
│   ├── send_to_colnik.py
│   └── receive_responses.py
│
└── autonomy.py                 ← hlavný vstupný bod              AUTONOMY PROCESS
                    │
                    ▼
              monitor.py
                    │
                    ▼
             analyzer.py
                    │
                    ▼
             proposer.py
                    │
                    ▼
             json_format.py
                    │
                    ▼
          send_to_colnik.py
                    │
                    ▼
             ┌────────────┐
             │  COLNÍK    │
             └─────┬──────┘
                   │
          ALLOW / DENY /
       REQUIRE_CONFIRMATION
                   │
                   ▼
       receive_responses.py
                   │
                   ▼
              AUTONOMY A modules/ nesmie obchádzať ipc/.

Napríklad navigation.py nemá robiť:

navigation.py → OS

ale:

navigation.py
      ↓
návrh
      ↓
proposer.py
      ↓
JSON
      ↓
COLNÍK
      ↓
Workflow
      ↓
OS

To isté pre duplicity, priečinky aj terminál.

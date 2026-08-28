# COLNÍK 6.x – PROTOKOLY

## REQUEST PROTOCOL (COLNÍK 6.x)

Každá požiadavka do COLNÍKA musí mať presne tieto polia:

{
    "request_id": "<unique-id>",
    "origin": "<USER | SYSTEM | AUTONOMY | PLUGIN>",
    "action": "<READ | WRITE | MOVE | DELETE | EXECUTE | SYSTEM_CHANGE | NAVIGATE>",
    "target": "<resource>",

    "execute_type": null | "<SYSTEM_APP | USER_APP | SHELL | MMC | CONTROL_PANEL | UNKNOWN>",

    "payload": {
        "destination": "<optional>",
        "file_hash": "<optional sha256|md5>",
        "ttl": "<optional seconds>"
    },

    "priority": "<LOW | NORMAL | HIGH | CRITICAL>",
    "requires_confirmation": "<true | false>",
    "timestamp": "<ISO-8601>"
}

### Popis polí

- request_id – unikátna identifikácia požiadavky  
- origin – kto požiadavku vytvoril (USER, SYSTEM, AUTONOMY, PLUGIN)  
- action – typ akcie (READ, WRITE, MOVE, DELETE, EXECUTE, SYSTEM_CHANGE, NAVIGATE)  
- target – objekt, súbor, priečinok, entita  
- execute_type –  
  - **pri EXECUTE povinné**  
  - **pri ostatných akciách musí byť null alebo sa neuvádza**  
- payload.destination – cieľový priečinok/súbor (pri MOVE, WRITE)  
- payload.file_hash – hash súboru (MD5/SHA256), používa sa pri rizikových akciách  
- payload.ttl – Time To Live v sekundách, používa sa pri akciách, ktoré môžu vyžadovať potvrdenie  
- priority – LOW / NORMAL / HIGH / CRITICAL  
- requires_confirmation – požiadavka od odosielateľa, nie rozhodnutie COLNÍKA  
- timestamp – čas vytvorenia požiadavky (ISO-8601)

### Pravidlá

A. Každá požiadavka musí byť kompletná.  
B. Autonómia nesmie posielať EXECUTE, DELETE, SYSTEM_CHANGE bez requires_confirmation = true.  
C. USER požiadavky majú vždy priority = HIGH.  
D. SYSTEM požiadavky môžu mať CRITICAL.  
E. AUTONOMY požiadavky sú vždy NORMAL alebo LOW.  
F. PLUGIN požiadavky sú vždy NORMAL.  
G. requires_confirmation je iba návrh – COLNÍK má posledné slovo.  
H. Pri DELETE, kritických WRITE a citlivých MOVE musí byť payload.file_hash vyplnený.  
I. Pri akciách, ktoré môžu vyžadovať potvrdenie (DELETE, EXECUTE, SYSTEM_CHANGE, rizikový MOVE, kritický WRITE), musí byť payload.ttl vyplnený už v requeste.  
J. Po vypršaní ttl požiadavka automaticky expiruje na DENY s dôvodom "EXPIRED".

### Príklad validnej požiadavky

{
    "request_id": "REQ-2026-08-05-001",
    "origin": "AUTONOMY",
    "action": "MOVE",
    "target": "C:/Users/richa/Documents/duplicate_file.txt",

    "execute_type": null,

    "payload": {
        "destination": "C:/Users/richa/RecycleBin/",
        "file_hash": "sha256:9F2A1C3B...",
        "ttl": 300
    },

    "priority": "LOW",
    "requires_confirmation": true,
    "timestamp": "2026-08-05T04:16:00Z"
}

---

## DECISION PROTOCOL (COLNÍK 6.x)

COLNÍK musí na každý request vrátiť presne jednu z troch možností:

1. ALLOW  
2. DENY  
3. REQUIRE_CONFIRMATION  

Formát odpovede:

{
    "request_id": "<same-as-in-request>",
    "decision": "<ALLOW | DENY | REQUIRE_CONFIRMATION>",
    "reason": "<text>",
    "timestamp": "<ISO-8601>"
}

### Popis

- decision – výsledok rozhodnutia COLNÍKA  
- reason – stručné vysvetlenie (napr. "DELETE requires confirmation", "AUTONOMY cannot EXECUTE", "Permission denied", "HASH_MISMATCH", "EXPIRED")  
- timestamp – čas rozhodnutia (ISO-8601)

### Pravidlá

A. ALLOW sa používa pri bezpečných alebo štandardných akciách.  
B. DENY sa používa pri zakázaných akciách alebo nevalidných requestoch.  
C. REQUIRE_CONFIRMATION sa používa pri rizikových akciách (DELETE, EXECUTE, SYSTEM_CHANGE, rizikové MOVE, kritické WRITE).  
D. COLNÍK má vždy posledné slovo – autonómia nemôže obísť rozhodnutie.  
E. Každá odpoveď musí obsahovať request_id.  
F. Ak TTL vyprší, COLNÍK vráti DENY s reason = "EXPIRED".  
G. Ak file_hash nesedí, COLNÍK vráti DENY s reason = "HASH_MISMATCH".

### Príklad

{
    "request_id": "REQ-2026-08-05-001",
    "decision": "REQUIRE_CONFIRMATION",
    "reason": "MOVE to RecycleBin requires user confirmation",
    "timestamp": "2026-08-05T04:20:00Z"
}

---

## ORIGIN PROTOCOL (COLNÍK 6.x)

Origin určuje, kto vytvoril požiadavku:

- USER       – príkaz od používateľa  
- SYSTEM     – interný systémový proces (SelfRepair, HealthMonitor)  
- AUTONOMY   – autonómny proces SIRIUS 6.x  
- PLUGIN     – externý modul  

### Pravidlá

A. USER má najvyššiu dôveryhodnosť zdroja požiadavky (nie automaticky najvyššiu priority hodnotu).  
B. SYSTEM môže mať CRITICAL priority.  
C. AUTONOMY má vždy NORMAL alebo LOW priority.  
D. PLUGIN má vždy NORMAL priority.  
E. Origin je informácia pre rozhodovanie, nie automatické povolenie.

---

## ACTION PROTOCOL (COLNÍK 6.x)

Typy akcií:

- READ           – čítanie dát, štandardne ALLOW  
- WRITE          – zápis dát, stredné riziko  
- MOVE           – presun súborov/priečinkov  
- DELETE         – mazanie, vysoké riziko  
- EXECUTE        – spúšťanie kódu, vysoké riziko  
- SYSTEM_CHANGE  – zmena systémových nastavení, kritické  
- NAVIGATE       – navigácia v systéme, štandardne ALLOW  

### Pravidlá

A. DELETE, EXECUTE, SYSTEM_CHANGE vždy vyžadujú potvrdenie.  
B. READ môže byť ALLOW, DENY alebo REQUIRE_CONFIRMATION podľa cieľa.  
C. MOVE môže byť bezpečné alebo rizikové podľa cieľa (pri citlivých cieľoch sa vyžaduje file_hash + ttl).  
D. NAVIGATE môže byť ALLOW alebo REQUIRE_CONFIRMATION podľa kontextu.

---

## CONFIRMATION PROTOCOL (COLNÍK 6.x)

COLNÍK rozhoduje, či akcia potrebuje potvrdenie:

- READ             → štandardne ALLOW  
- WRITE            → podľa kontextu  
- MOVE             → podľa cieľa  
- DELETE           → REQUIRE_CONFIRMATION  
- EXECUTE          → REQUIRE_CONFIRMATION  
- SYSTEM_CHANGE    → REQUIRE_CONFIRMATION  
- NAVIGATE         → štandardne ALLOW  

### Pravidlá

A. Autonómia môže navrhnúť requires_confirmation = true.  
B. COLNÍK má posledné slovo.  
C. USER môže potvrdiť akciu, autonómia nie.  
D. Po vypršaní payload.ttl sa požiadavka automaticky zamietne (DENY, reason = "EXPIRED").

---

## RESPONSE PROTOCOL (COLNÍK 6.x)

Formát odpovede:

{
    "request_id": "<same-as-request>",
    "decision": "<ALLOW | DENY | REQUIRE_CONFIRMATION>",
    "reason": "<text>",
    "timestamp": "<ISO-8601>"
}

### Pravidlá

A. Každá odpoveď musí byť štandardizovaná.  
B. Aj pri DENY musí byť reason vyplnený.  
C. Autonómia musí vedieť presne, prečo bola akcia zamietnutá (HASH_MISMATCH, EXPIRED, INVALID_TTL, INVALID_HASH, atď.).  
D. timestamp je povinný a musí byť v ISO-8601 formáte.  
E. request_id musí byť rovnaký ako v pôvodnom requeste.

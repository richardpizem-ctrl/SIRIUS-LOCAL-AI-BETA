# WORKFLOW ENGINE – TESTOVACIA VERZIA
# Test REQUIRE_CONFIRMATION + potvrdenie YES/NO

import time
import sys
import os

# 🔥 PRIDANIE CESTY K AUTONOMY MODULOM
sys.path.append(os.path.join(os.getcwd(), "AUTONOMY"))

from autonomy_test_input import snapshot
from autonomy import Autonomy

autonomy = Autonomy()

print("\n=== SIRIUS 6.x — TESTOVACÍ REŽIM AUTONÓMIE (YES/NO CONFIRMATION TEST) ===\n")

waiting_for_confirmation = False
stored_proposal = None

while True:
    # 1️⃣ Získaj snapshot (simulovaný rast CPU)
    system_snapshot = snapshot()

    # 2️⃣ Autonómia spracuje snapshot
    result = autonomy.cycle()

    # 3️⃣ TESTOVACÍ nebezpečný návrh
    proposals = [{
        "proposal_id": "exec-test",
        "action": "EXECUTE",
        "target": "explorer.exe",
        "payload": {},
        "priority": "HIGH"
    }]

    print("[AUTONOMY] Proposals (TEST):")
    print(proposals)
    print()

    # 4️⃣ Ak čakáme na potvrdenie, nepúšťame nový návrh
    if waiting_for_confirmation:
        print("[COLNÍK] Response: REQUIRE_CONFIRMATION (už čakáme)")
        print()

        print("[WORKFLOW] Čaká sa na tvoje potvrdenie (YES/NO).")
        print()

        user_input = input("Potvrď akciu (YES/NO): ").strip().upper()

        if user_input == "YES":
            print("\n[WORKFLOW] Potvrdené — vykonávam akciu.")
            print({
                "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ"),
                "status": "EXECUTED",
                "action": stored_proposal["action"],
                "target": stored_proposal["target"],
                "message": "Akcia bola vykonaná po potvrdení."
            })
            print()
            waiting_for_confirmation = False
            stored_proposal = None

        elif user_input == "NO":
            print("\n[WORKFLOW] Zamietnuté — akcia NEBUDE vykonaná.")
            print({
                "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ"),
                "status": "CANCELLED",
                "action": stored_proposal["action"],
                "target": stored_proposal["target"],
                "message": "Akcia bola zrušená používateľom."
            })
            print()
            waiting_for_confirmation = False
            stored_proposal = None

        else:
            print("\n[WORKFLOW] Neplatný vstup — stále čakám na potvrdenie.")
            print()
        continue

    # 5️⃣ COLNÍK — REQUIRE_CONFIRMATION
    print("[COLNÍK] Response:")
    print({
        "status": "REQUIRE_CONFIRMATION",
        "reason": "dangerous_action",
        "proposal": proposals[0]
    })
    print()

    # 6️⃣ WORKFLOW — čaká na potvrdenie
    print("[WORKFLOW] Result:")
    print({
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "status": "WAITING_CONFIRMATION",
        "action": proposals[0]["action"],
        "target": proposals[0]["target"],
        "message": "Workflow NEVYKONAL akciu — čaká sa na potvrdenie."
    })
    print()

    waiting_for_confirmation = True
    stored_proposal = proposals[0]

    print("=== CYCLE COMPLETE ===\n")

    time.sleep(1)

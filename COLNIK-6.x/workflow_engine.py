import time
import json
import os
import sys
from pathlib import Path

# ============================================================
# PATH FIX
# ============================================================

BASE_DIR = Path(__file__).resolve().parent
AUTONOMY_DIR = BASE_DIR / "AUTONOMY"
COLNIK_DIR = BASE_DIR / "COLNIK_SIMULATOR"

sys.path.append(str(AUTONOMY_DIR))
sys.path.append(str(COLNIK_DIR))

# ============================================================
# IMPORTY – OPRAVENÉ
# ============================================================

from AUTONOMY.autonomy import Autonomy
from colnik_simulator import ColnikSimulator

# ============================================================
# SIRIUS 6.x — ŽIVÝ WORKFLOW S CONFIRMATION LOGIKOU
# ============================================================

autonomy = Autonomy()
colnik = ColnikSimulator()

print("\n=== SIRIUS 6.x — JEDNO OKNO (REAL WORKFLOW + CONFIRMATION) ===\n")

# 🔥 DOPLNENÉ PODĽA TESTOV
waiting_for_confirmation = False
stored_proposal = None

while True:

    # ========================================================
    # AUTONÓMIA
    # ========================================================

    result = autonomy.cycle()
    proposals = result.get("proposals", [])

    print("\n[AUTONOMY] Proposals:")
    print(json.dumps(proposals, indent=4))

    if waiting_for_confirmation:
        print("\n[COLNÍK] Response: REQUIRE_CONFIRMATION (už čakáme)")
        print("\n[WORKFLOW] Čaká sa na tvoje potvrdenie (YES/NO).\n")

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

            # 🔥 Reset
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

            # 🔥 Reset
            waiting_for_confirmation = False
            stored_proposal = None

        else:
            print("\n[WORKFLOW] Neplatný vstup — stále čakám na potvrdenie.\n")

        continue

    if not proposals:
        print("\n[WORKFLOW] Žiadny návrh.")
        print("\n=== CYCLE COMPLETE ===\n")
        time.sleep(1)
        continue

    # ========================================================
    # COLNÍK — vyhodnotenie prvého návrhu
    # ========================================================

    proposal = proposals[0]
    colnik_response = colnik.evaluate(proposal)

    print("\n[COLNÍK] Response:")
    print(json.dumps(colnik_response, indent=4))

    status = colnik_response.get("status", "UNKNOWN")
    action = proposal.get("action")
    target = proposal.get("target")

    # ========================================================
    # REQUIRE_CONFIRMATION — presne ako v testoch
    # ========================================================

    if status == "REQUIRE_CONFIRMATION":
        print("\n[WORKFLOW] Result:")
        print({
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "status": "WAITING_CONFIRMATION",
            "action": action,
            "target": target,
            "message": "Workflow NEVYKONAL akciu — čaká sa na potvrdenie."
        })
        print()

        waiting_for_confirmation = True
        stored_proposal = proposal

        print("=== CYCLE COMPLETE ===\n")
        time.sleep(1)
        continue

    # ========================================================
    # DENY — akcia sa nevykoná
    # ========================================================

    if status == "DENY":
        print("\n[WORKFLOW] Result:")
        print({
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "status": "DENY",
            "action": action,
            "target": target,
            "message": "COLNÍK zamietol akciu."
        })
        print("\n=== CYCLE COMPLETE ===\n")
        time.sleep(1)
        continue

    # ========================================================
    # ALLOW — akcia sa vykoná okamžite
    # ========================================================

    if status == "ALLOW":
        print("\n[WORKFLOW] Result:")
        print({
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "status": "EXECUTED",
            "action": action,
            "target": target,
            "message": "Akcia bola vykonaná (ALLOW)."
        })
        print("\n=== CYCLE COMPLETE ===\n")
        time.sleep(1)
        continue

    # ========================================================
    # UNKNOWN — fallback
    # ========================================================

    print("\n[WORKFLOW] Result:")
    print({
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "status": "UNKNOWN",
        "action": action,
        "target": target,
        "message": "Neznámy stav — akcia nebola vykonaná."
    })
    print("\n=== CYCLE COMPLETE ===\n")

    time.sleep(1)

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
TERMINAL_DIR = BASE_DIR / "terminal_assistant"
WORKFLOW_DIR = BASE_DIR / "workflow"
TIMECORE_DIR = BASE_DIR / "timecore"

sys.path.append(str(AUTONOMY_DIR))
sys.path.append(str(COLNIK_DIR))
sys.path.append(str(TERMINAL_DIR))
sys.path.append(str(WORKFLOW_DIR))
sys.path.append(str(TIMECORE_DIR))

# ============================================================
# IMPORTY
# ============================================================

from AUTONOMY.autonomy import Autonomy
from colnik_simulator import ColnikSimulator

from terminal_assistant.terminal_assistant import TerminalAssistant
from terminal_assistant.terminal_assistant_rules import TERMINAL_ASSISTANT_RULES

# WORKFLOW ENGINE – správny import (bez circular import)
from workflow.workflow_engine import execute_action

# TIMECORE – PILIER 0
from timecore import TimeCore

# ============================================================
# INICIALIZÁCIA MODULOV
# ============================================================

autonomy = Autonomy()
colnik = ColnikSimulator()
terminal = TerminalAssistant()

timecore = TimeCore()
timecore.runtime_start()

print("\n=== SIRIUS 6.x — WORKFLOW RUNTIME (AUTONOMY + COLNÍK + ENVOY) ===\n")

waiting_for_confirmation = False
stored_proposal = None

# ============================================================
# HLAVNÝ CYKLUS
# ============================================================

while True:

    timecore.cycle_start()   # <<< PRIDANÉ

    # ========================================================
    # AUTONÓMIA
    # ========================================================

    result = autonomy.cycle()
    proposals = result.get("proposals", [])

    print("\n[AUTONOMY] Proposals:")
    print(json.dumps(proposals, indent=4))

    # ========================================================
    # TERMINAL ASSISTANT — kontrola príkazov
    # ========================================================

    if proposals:
        proposal = proposals[0]
        command = proposal.get("command")

        if command:
            allowed = TERMINAL_ASSISTANT_RULES["allowed"]
            forbidden = TERMINAL_ASSISTANT_RULES["forbidden"]

            if command in forbidden:
                terminal.last_command = command
                print("\n[TERMINAL] Forbidden command detected:", command)
                print({
                    "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ"),
                    "status": "DENY",
                    "command": command,
                    "message": "Terminal command is forbidden."
                })
                print("\n=== CYCLE COMPLETE ===\n")

                timecore.cycle_end()   # <<< PRIDANÉ
                time.sleep(1)
                continue

            if command not in allowed:
                print("\n[TERMINAL] Unknown command:", command)
                print({
                    "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ"),
                    "status": "DENY",
                    "command": command,
                    "message": "Unknown terminal command."
                })
                print("\n=== CYCLE COMPLETE ===\n")

                timecore.cycle_end()   # <<< PRIDANÉ
                time.sleep(1)
                continue

            terminal.last_command = command
            print("\n[TERMINAL] Command accepted:", command)

    # ========================================================
    # REQUIRE_CONFIRMATION — čakáme na potvrdenie
    # ========================================================

    if waiting_for_confirmation:
        print("\n[COLNÍK] Response: REQUIRE_CONFIRMATION (už čakáme)")
        print("\n[WORKFLOW] Čaká sa na tvoje potvrdenie (YES/NO).\n")

        user_input = input("Potvrď akciu (YES/NO): ").strip().upper()

        if user_input == "YES":
            print("\n[WORKFLOW] Potvrdené — vykonávam akciu.")

            execute_action(
                stored_proposal["action"],
                stored_proposal["target"]
            )

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
            print("\n[WORKFLOW] Neplatný vstup — stále čakám na potvrdenie.\n")

        timecore.cycle_end()   # <<< PRIDANÉ
        continue

    # ========================================================
    # Žiadny návrh
    # ========================================================

    if not proposals:
        print("\n[WORKFLOW] Žiadny návrh.")
        print("\n=== CYCLE COMPLETE ===\n")

        timecore.cycle_end()   # <<< PRIDANÉ
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
    # REQUIRE_CONFIRMATION
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

        timecore.cycle_end()   # <<< PRIDANÉ
        time.sleep(1)
        continue

    # ========================================================
    # DENY
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

        timecore.cycle_end()   # <<< PRIDANÉ
        time.sleep(1)
        continue

    # ========================================================
    # ALLOW
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

        execute_action(action, target)

        print("\n=== CYCLE COMPLETE ===\n")

        timecore.cycle_end()   # <<< PRIDANÉ
        time.sleep(1)
        continue

    # ========================================================
    # UNKNOWN
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

    timecore.cycle_end()   # <<< PRIDANÉ
    time.sleep(1)

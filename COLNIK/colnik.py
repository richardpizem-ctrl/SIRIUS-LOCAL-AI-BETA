# COLNIK 6.x – skutočný manager
# Číta AUTONOMY proposals.json, validuje, rozhodne, zapíše responses.json
# + PREPOJENIE NA EXECUTE MODUL

import json
import os
import time
import subprocess
import sys

# === KOREKTNÉ CESTY NA ROOT COLNIK-6.x ===
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# C:\SIRIUS_ARCHIVE\COLNIK-6.x

# aby vedel nájsť validator.py, decision_engine.py atď.
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

from validator import validate_request
from decision_engine import decide

IPC_DIR = os.path.join(BASE_DIR, "IPC_DATA")
IPC_PROPOSALS = os.path.join(IPC_DIR, "proposals.json")
IPC_RESPONSES = os.path.join(IPC_DIR, "responses.json")
IPC_CONFIRM = os.path.join(IPC_DIR, "confirm.json")

EXECUTE_PATH = os.path.join(BASE_DIR, "EXECUTE", "executor.py")


def load_proposals():
    if not os.path.exists(IPC_PROPOSALS):
        print(f"[COLNÍK] proposals.json neexistuje: {IPC_PROPOSALS}")
        return []

    try:
        with open(IPC_PROPOSALS, "r", encoding="utf-8") as f:
            data = json.load(f)

        # AUTONOMY používa "proposals"
        proposals = data.get("proposals", [])

        print(f"[COLNÍK] Načítaných návrhov: {len(proposals)}")
        return proposals

    except Exception as e:
        print("[COLNÍK] ERROR pri čítaní proposals.json:", e)
        return []


def save_responses(responses):
    os.makedirs(IPC_DIR, exist_ok=True)
    payload = {"responses": responses}

    try:
        with open(IPC_RESPONSES, "w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False, indent=2)
        print(f"[COLNÍK] responses.json uložený → {IPC_RESPONSES}")
    except Exception as e:
        print("[COLNÍK] ERROR pri zápise responses.json:", e)


def check_confirm():
    if not os.path.exists(IPC_CONFIRM):
        return None

    try:
        with open(IPC_CONFIRM, "r", encoding="utf-8") as f:
            data = json.load(f)
    except:
        return None

    if not data:
        return None

    if data.get("confirm") is True:
        return data.get("request_id")

    return None


def process_proposal(proposal):
    errors = validate_request(proposal)

    if errors:
        decision = {
            "request_id": proposal.get("request_id", "AUTO"),
            "decision": "DENY",
            "reason": f"Invalid request: {errors}",
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ")
        }
    else:
        decision = decide(proposal)

    action = proposal.get("action")
    params = proposal.get("payload", {})

    response = {
        "request_id": proposal.get("request_id"),
        "decision": decision.get("decision"),
        "reason": decision.get("reason"),
        "action": action,
        "params": params,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ")
    }

    return response


def cycle():
    proposals = load_proposals()

    confirm_id = check_confirm()
    if confirm_id:
        print(f"[COLNÍK] Potvrdenie prijaté pre {confirm_id}")

        proposals = [p for p in proposals if p.get("request_id") != confirm_id]

        print(f"[COLNÍK] Vykonávam SYSTEM_CHANGE pre {confirm_id}")

        try:
            os.remove(IPC_CONFIRM)
        except:
            pass

        responses = [{
            "request_id": confirm_id,
            "decision": "ALLOW",
            "reason": "Confirmed and executed",
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ")
        }]

        save_responses(responses)
        print("[COLNÍK] Cycle complete.")
        return

    if not proposals:
        print("[COLNÍK] Žiadne návrhy.")
        return

    responses = []

    for p in proposals:
        resp = process_proposal(p)
        responses.append(resp)

    save_responses(responses)

    # PREPOJENIE COLNÍK → EXECUTE
    try:
        print(f"[COLNÍK] Spúšťam EXECUTE modul: {EXECUTE_PATH}")
        subprocess.run(["python", EXECUTE_PATH], check=True)
        print("[COLNÍK] EXECUTE modul úspešne dokončený.")
    except Exception as e:
        print(f"[COLNÍK] CHYBA pri spúšťaní EXECUTE: {e}")

    # 🔥 ODPORÚČANÁ OPRAVA — VYMAZAŤ proposals.json PO SPRACOVANÍ
    try:
        os.remove(IPC_PROPOSALS)
        print("[COLNÍK] proposals.json vymazaný po spracovaní.")
    except Exception as e:
        print(f"[COLNÍK] ERROR pri mazaní proposals.json: {e}")

    print("[COLNÍK] Cycle complete.")


if __name__ == "__main__":
    print("\n=== COLNÍK 6.x — IPC MANAGER (AUTONOMY → COLNÍK → EXECUTE → AUTONOMY) ===\n")
    while True:
        cycle()
        time.sleep(1)

# COLNIK 6.x – IPC MANAGER (AUTONOMY → IPC_DATA\proposals.json → COLNÍK → EXECUTE → AUTONOMY)

import json
import os
import time
import subprocess

from validator import validate_request
from decision_engine import decide

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

IPC_DIR = os.path.join(PROJECT_ROOT, "IPC_DATA")
IPC_PROPOSALS = os.path.join(IPC_DIR, "proposals.json")
IPC_RESPONSES_IPC = os.path.join(IPC_DIR, "responses.json")
IPC_CONFIRM = os.path.join(IPC_DIR, "confirm.json")

os.makedirs(IPC_DIR, exist_ok=True)


def load_proposals():
    if not os.path.exists(IPC_PROPOSALS):
        print("[COLNÍK] proposals.json neexistuje:", IPC_PROPOSALS)
        return []

    try:
        with open(IPC_PROPOSALS, "r", encoding="utf-8") as f:
            data = json.load(f)
        proposals = data.get("REQUESTS", [])
        print(f"[COLNÍK] Načítaných návrhov: {len(proposals)}")
        return proposals
    except Exception as e:
        print("[COLNÍK] ERROR pri čítaní proposals.json:", e)
        return []


def save_responses(responses):
    payload = {"responses": responses}
    try:
        with open(IPC_RESPONSES_IPC, "w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False, indent=2)
        print("[COLNÍK] responses.json uložený →", IPC_RESPONSES_IPC)
    except Exception as e:
        print("[COLNÍK] ERROR pri zápise responses.json:", e)


def check_confirm():
    if not os.path.exists(IPC_CONFIRM):
        return None

    try:
        with open(IPC_CONFIRM, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception:
        return None

    if not data:
        return None

    if data.get("confirm") is True:
        return data.get("request_id")

    return None


def process_proposal(proposal):
    errors = validate_request(proposal)
    if errors:
        print(f"[COLNÍK] VALIDATION WARN for {proposal.get('request_id')}: {errors}")

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


def cycle_once():
    proposals = load_proposals()

    if not proposals:
        print("[COLNÍK] Žiadne návrhy.")
        return

    responses = []

    for p in proposals:
        resp = process_proposal(p)
        responses.append(resp)

    confirm_id = check_confirm()
    if confirm_id:
        print(f"[COLNÍK] Potvrdenie prijaté pre {confirm_id}")
        for r in responses:
            if r.get("request_id") == confirm_id:
                r["decision"] = "ALLOW"
                r["reason"] = "Confirmed and executed"
                print(f"[COLNÍK] Vykonávam SYSTEM_CHANGE pre {confirm_id}")
                break
        try:
            os.remove(IPC_CONFIRM)
        except Exception:
            pass

    save_responses(responses)

    # Spustenie EXECUTE po uložení responses.json
    try:
        execute_path = os.path.join(PROJECT_ROOT, "EXECUTE", "executor.py")
        print(f"[COLNÍK] Spúšťam EXECUTE modul: {execute_path}")
        subprocess.run(["python", execute_path], check=True)
        print("[COLNÍK] EXECUTE modul úspešne dokončený.")
    except Exception as e:
        print(f"[COLNÍK] CHYBA pri spúšťaní EXECUTE: {e}")

    # proposals.json po spracovaní zmažeme, responses.json necháme pre AUTONOMY/KG UPDATE
    try:
        os.remove(IPC_PROPOSALS)
        print("[COLNÍK] proposals.json vymazaný po spracovaní.")
    except Exception:
        pass

    print("[COLNÍK] Cycle complete.")


if __name__ == "__main__":
    print("\n=== COLNÍK 6.x — IPC MANAGER (AUTONOMY → COLNÍK → EXECUTE → AUTONOMY) ===\n")
    while True:
        cycle_once()
        time.sleep(1)

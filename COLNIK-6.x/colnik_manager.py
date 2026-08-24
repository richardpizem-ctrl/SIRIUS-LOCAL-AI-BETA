# COLNIK 6.x – skutočný manager
# Číta AUTONOMY proposals.json, validuje, rozhodne, zapíše responses.json

import json
import os
import time

from validator import validate_request
from decision_engine import decide
import response_builder

IPC_DIR = r".\IPC_DATA"
IPC_PROPOSALS = os.path.join(IPC_DIR, "proposals.json")
IPC_RESPONSES = os.path.join(IPC_DIR, "responses.json")
IPC_CONFIRM = os.path.join(IPC_DIR, "confirm.json")


# === LOAD PROPOSALS ===
def load_proposals():
    if not os.path.exists(IPC_PROPOSALS):
        print("[COLNÍK] proposals.json neexistuje.")
        return []

    try:
        with open(IPC_PROPOSALS, "r", encoding="utf-8") as f:
            data = json.load(f)
        proposals = data.get("proposals", [])
        print(f"[COLNÍK] Načítaných návrhov: {len(proposals)}")
        return proposals
    except Exception as e:
        print("[COLNÍK] ERROR pri čítaní proposals.json:", e)
        return []


# === SAVE RESPONSES ===
def save_responses(responses):
    os.makedirs(IPC_DIR, exist_ok=True)
    payload = {"responses": responses}

    try:
        with open(IPC_RESPONSES, "w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False, indent=2)
        print("[COLNÍK] responses.json uložený.")
    except Exception as e:
        print("[COLNÍK] ERROR pri zápise responses.json:", e)


# === CHECK CONFIRMATION ===
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


# === PROCESS PROPOSAL ===
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

    response = response_builder.build_response(decision)
    return response


# === MAIN CYCLE ===
def cycle():
    proposals = load_proposals()

    # === CHECK CONFIRMATION FIRST ===
    confirm_id = check_confirm()
    if confirm_id:
        print(f"[COLNÍK] Potvrdenie prijaté pre {confirm_id}")

        # odstránime potvrdený request
        proposals = [p for p in proposals if p.get("request_id") != confirm_id]

        # vykonáme SYSTEM_CHANGE (placeholder)
        print(f"[COLNÍK] Vykonávam SYSTEM_CHANGE pre {confirm_id}")

        # vymažeme confirm.json
        try:
            os.remove(IPC_CONFIRM)
        except:
            pass

        # zapíšeme ALLOW odpoveď
        responses = [{
            "request_id": confirm_id,
            "decision": "ALLOW",
            "reason": "Confirmed and executed",
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ")
        }]

        save_responses(responses)
        print("[COLNÍK] Cycle complete.")
        print("PROPOSALS:", json.dumps(proposals, indent=2))
        print("RESPONSES:", json.dumps(responses, indent=2))
        return

    # === NORMAL PROCESSING ===
    if not proposals:
        print("[COLNÍK] Žiadne návrhy.")
        return

    responses = []

    for p in proposals:
        resp = process_proposal(p)
        responses.append(resp)

    save_responses(responses)

    print("[COLNÍK] Cycle complete.")
    print("PROPOSALS:", json.dumps(proposals, indent=2))
    print("RESPONSES:", json.dumps(responses, indent=2))


# === MAIN LOOP ===
if __name__ == "__main__":
    print("\n=== COLNÍK 6.x — IPC MANAGER (AUTONOMY → COLNÍK → RESPONSES) ===\n")
    while True:
        cycle()
        time.sleep(1)

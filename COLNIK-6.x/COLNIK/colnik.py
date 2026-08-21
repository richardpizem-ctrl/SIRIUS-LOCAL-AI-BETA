import json
import os
from datetime import datetime

# === TIMECORE – PILIER 0 ===
from timecore import TimeCore

from config import PROPOSALS_PATH, RESPONSES_PATH, LOG_PATH


def log(message):
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now().isoformat()}] {message}\n")
    print(message)


def load_proposals():
    if not os.path.exists(PROPOSALS_PATH):
        return []

    try:
        with open(PROPOSALS_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data.get("proposals", [])
    except Exception as e:
        log(f"ERROR: {e}")
        return []


def process_proposal(p, timecore):
    # TIMECORE – začiatok spracovania jedného návrhu
    timecore.cycle_start()

    action = p.get("action", "UNKNOWN")
    target = p.get("target", {})
    reason = p.get("reason", "no_reason")

    log(f"PROPOSAL: action={action}, target={target}, reason={reason}")

    response = {
        "proposal_id": p.get("id"),
        "decision": "ALLOW",
        "executed": False,
        "note": "Primitívny COLNÍK: akcia NEVYKONANÁ.",
        "cycle_time": timecore.cycle_delta()  # meranie trvania spracovania
    }

    # TIMECORE – koniec spracovania návrhu
    timecore.cycle_end()

    return response


def save_responses(responses):
    os.makedirs(os.path.dirname(RESPONSES_PATH), exist_ok=True)
    with open(RESPONSES_PATH, "w", encoding="utf-8") as f:
        json.dump({
            "timestamp": datetime.now().isoformat(),
            "responses": responses
        }, f, ensure_ascii=False, indent=2)


def main():
    # TIMECORE – inicializácia
    timecore = TimeCore()
    timecore.runtime_start()

    log("COLNÍK 6.x – štart")

    proposals = load_proposals()
    if not proposals:
        log("Žiadne návrhy od autonómie.")
        save_responses([])
        timecore.runtime_end()
        return

    responses = []
    for p in proposals:
        responses.append(process_proposal(p, timecore))

    save_responses(responses)
    log("COLNÍK 6.x – koniec")

    # TIMECORE – koniec runtime
    timecore.runtime_end()


if __name__ == "__main__":
    main()

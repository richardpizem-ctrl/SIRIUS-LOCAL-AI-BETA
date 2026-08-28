# executor.py – hlavný vykonávací modul EXECUTE

import json
import os
import time

from executor_actions import execute_action
from executor_rules import is_action_safe
from executor_log import info, warning, error, executed

# COLNÍK ukladá responses.json do IPC_DATA:
# C:\SIRIUS_ARCHIVE\COLNIK-6.x\IPC_DATA\responses.json

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
RESPONSES_PATH = os.path.join(BASE_DIR, "IPC_DATA", "responses.json")

# spätná väzba pre AUTONOMY → KG UPDATE
FEEDBACK_PATH = os.path.join(BASE_DIR, "IPC_DATA", "execute_feedback.json")


def load_responses():
    """Načíta responses.json vytvorený Colníkom."""
    if not os.path.exists(RESPONSES_PATH):
        error(f"responses.json neexistuje: {RESPONSES_PATH}")
        return None

    try:
        with open(RESPONSES_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
            info("responses.json načítaný")
            return data.get("responses", [])
    except Exception as e:
        error(f"Chyba pri čítaní responses.json: {e}")
        return None


def save_feedback(feedback):
    """Zapíše výsledky EXECUTE späť do AUTONOMY."""
    payload = {"execute_results": feedback}

    try:
        with open(FEEDBACK_PATH, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2)
        info("execute_feedback.json uložený.")
    except Exception as e:
        error(f"Chyba pri zápise execute_feedback.json: {e}")


def process_responses():
    """Spracuje všetky akcie v responses.json."""
    responses = load_responses()
    if not responses:
        warning("Žiadne dáta na spracovanie")
        return

    feedback = []

    for item in responses:
        action = item.get("action")
        params = item.get("params", {})
        req_id = item.get("request_id")

        if not action:
            warning("Položka nemá definovanú akciu – preskakujem")
            continue

        # Bezpečnostné pravidlá
        if not is_action_safe(action):
            warning(f"Akcia zamietnutá bezpečnostnými pravidlami: {action}")
            continue

        # Vykonanie akcie
        result = execute_action(action, params)
        executed(action, result)

        feedback.append({
            "request_id": req_id,
            "action": action,
            "result": result,
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ")
        })

    save_feedback(feedback)


if __name__ == "__main__":
    process_responses()

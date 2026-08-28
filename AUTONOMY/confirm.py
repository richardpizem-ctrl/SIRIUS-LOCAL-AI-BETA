import json
import os

IPC_RESPONSES = r"C:\SIRIUS_ARCHIVE\COLNIK-6.x\IPC_DATA\responses.json"
IPC_CONFIRM = r"C:\SIRIUS_ARCHIVE\COLNIK-6.x\IPC_DATA\confirm.json"

def check_confirmation():
    if not os.path.exists(IPC_RESPONSES):
        return None

    try:
        with open(IPC_RESPONSES, "r", encoding="utf-8") as f:
            data = json.load(f)
    except:
        return None

    if not data:
        return None

    last = data[-1]

    if last.get("decision") == "REQUIRE_CONFIRMATION":
        return last.get("request_id")

    return None


def send_confirmation(request_id):
    payload = {
        "request_id": request_id,
        "confirm": True
    }

    with open(IPC_CONFIRM, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)

    print(f"[CONFIRM] Request {request_id} potvrdený.")

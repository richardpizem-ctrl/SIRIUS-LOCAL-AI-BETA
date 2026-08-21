# COLNIK 6.x - response_builder.py
# Vytvára štandardizovanú odpoveď podľa protokolu

import time

def build_response(decision_obj):
    return {
        "request_id": decision_obj.get("request_id"),
        "decision": decision_obj.get("decision"),
        "reason": decision_obj.get("reason"),
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ")
    }

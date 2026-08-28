# decision_engine.py – rozhodovanie ALLOW / REQUIRE_CONFIRMATION / DENY

def decide(req):
    action = req.get("action")
    payload = req.get("payload", {})
    category = payload.get("category")
    requires_confirmation = req.get("requires_confirmation", False)

    # SYSTEM_CHANGE – citlivé veci
    if action == "SYSTEM_CHANGE":
        return {
            "decision": "REQUIRE_CONFIRMATION",
            "reason": "SYSTEM_CHANGE requires confirmation"
        }

    # DUPLICITY – CRITICAL / SAFE / EMPTY
    if category == "CRITICAL":
        return {
            "decision": "REQUIRE_CONFIRMATION",
            "reason": "Critical duplicate – manual confirmation required"
        }

    if category == "SAFE":
        return {
            "decision": "ALLOW",
            "reason": "Safe duplicate – report only"
        }

    if category == "EMPTY":
        return {
            "decision": "ALLOW",
            "reason": "Empty files – archive allowed"
        }

    # NAVIGÁCIA
    if action == "NAVIGATE":
        return {
            "decision": "ALLOW",
            "reason": "Navigation allowed"
        }

    # MOVE, DELETE, EXECUTE – default
    if action in ["MOVE", "DELETE", "EXECUTE", "READ", "WRITE"]:
        if requires_confirmation:
            return {
                "decision": "REQUIRE_CONFIRMATION",
                "reason": "Action flagged as requiring confirmation"
            }
        return {
            "decision": "ALLOW",
            "reason": "Action allowed"
        }

    # fallback
    return {
        "decision": "DENY",
        "reason": f"Unknown or unsupported action: {action}"
    }

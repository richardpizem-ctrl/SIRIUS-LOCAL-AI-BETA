# COLNIK 6.x - validator.py
# Kontrola formátu requestu podľa protokolového kontraktu

VALID_ORIGINS = ["USER", "SYSTEM", "AUTONOMY", "PLUGIN"]
VALID_ACTIONS = ["READ", "WRITE", "MOVE", "DELETE", "EXECUTE", "SYSTEM_CHANGE", "NAVIGATE"]
VALID_PRIORITIES = ["LOW", "NORMAL", "HIGH", "CRITICAL"]
VALID_EXECUTE_TYPES = ["SYSTEM_APP", "USER_APP", "SHELL", "MMC", "CONTROL_PANEL", "UNKNOWN"]

# Akcie, ktoré vyžadujú file_hash
HASH_REQUIRED_ACTIONS = ["DELETE", "WRITE", "MOVE"]

# Akcie, ktoré vyžadujú TTL pri REQUIRE_CONFIRMATION
TTL_REQUIRED_ACTIONS = ["DELETE", "EXECUTE", "SYSTEM_CHANGE", "WRITE", "MOVE"]


def validate_request(req):
    errors = []

    # Povinné polia
    required_fields = [
        "request_id",
        "origin",
        "action",
        "target",
        "priority",
        "requires_confirmation",
        "timestamp"
    ]

    for field in required_fields:
        if field not in req:
            errors.append(f"Missing field: {field}")

    # Kontrola origin
    if "origin" in req and req["origin"] not in VALID_ORIGINS:
        errors.append("Invalid origin")

    # Kontrola action
    if "action" in req and req["action"] not in VALID_ACTIONS:
        errors.append("Invalid action")

    # Kontrola priority
    if "priority" in req and req["priority"] not in VALID_PRIORITIES:
        errors.append("Invalid priority")

    # Payload musí byť objekt alebo None
    if "payload" in req and req["payload"] is not None and not isinstance(req["payload"], dict):
        errors.append("Payload must be an object")

    payload = req.get("payload", {})

    # Kontrola execute_type pri EXECUTE
    if req.get("action") == "EXECUTE":
        if "execute_type" not in req:
            errors.append("Missing field: execute_type")
        elif req["execute_type"] not in VALID_EXECUTE_TYPES:
            errors.append("Invalid execute_type")

    # Kontrola file_hash pri rizikových akciách
    if req.get("action") in HASH_REQUIRED_ACTIONS:
        # DELETE vždy vyžaduje hash
        # WRITE vyžaduje hash pri kritických súboroch (COLNÍK rozhodne neskôr)
        # MOVE vyžaduje hash pri citlivých cieľoch (COLNÍK rozhodne neskôr)
        if payload is None or "file_hash" not in payload or not payload["file_hash"]:
            errors.append("Missing or invalid file_hash for this action")

    # Kontrola TTL pri akciách, ktoré môžu ísť do REQUIRE_CONFIRMATION
    if req.get("requires_confirmation") is True:
        if req.get("action") in TTL_REQUIRED_ACTIONS:
            if payload is None or "ttl" not in payload:
                errors.append("Missing TTL for confirmation-required action")
            else:
                # TTL musí byť číslo > 0
                ttl = payload["ttl"]
                if not isinstance(ttl, int) or ttl <= 0:
                    errors.append("TTL must be a positive integer")

    return errors

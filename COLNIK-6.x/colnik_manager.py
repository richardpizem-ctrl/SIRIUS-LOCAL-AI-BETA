# COLNIK 6.x - colnik_manager.py
# Prepojenie autonómie s COLNÍKOM (validácia → rozhodnutie → odpoveď)
# + Integrácia NAVIGATION modulu

import validator
import decision_engine
import response_builder

# NAVIGATION
from navigation.navigation import Navigation
from navigation.navigation_rules import NAVIGATION_RULES

VALID_EXECUTE_TYPES = ["SYSTEM_APP", "USER_APP", "SHELL", "MMC", "CONTROL_PANEL", "UNKNOWN"]


def process_request(req):
    # 1. VALIDÁCIA REQUESTU
    errors = validator.validate_request(req)

    # Extra kontrola pre EXECUTE
    if req.get("action") == "EXECUTE":
        execute_type = req.get("execute_type")
        if execute_type is None:
            errors.append("Missing execute_type")
        elif execute_type not in VALID_EXECUTE_TYPES:
            errors.append("Invalid execute_type")

    # Ak validácia zlyhala → DENY
    if errors:
        return {
            "request_id": req.get("request_id", "UNKNOWN"),
            "decision": "DENY",
            "reason": f"Invalid request: {errors}",
            "timestamp": "AUTO"
        }

    # 2. ROZHODOVACÍ ENGINE (TTL, HASH, rizikové akcie)
    decision = decision_engine.decide(req)

    # 3. ŠTANDARDIZOVANÁ ODPOVEĎ
    response = response_builder.build_response(decision)

    return response


# ============================
# NAVIGATION API PRE COLNÍK
# ============================

navigation = Navigation()


def set_navigation_step(step_name: str):
    """Externé nastavenie kroku pre COLNÍK Navigation."""
    return navigation.set_step(step_name)


def get_allowed_next_steps(current_step: str):
    """Vráti povolené ďalšie kroky podľa NAVIGATION_RULES."""
    return NAVIGATION_RULES.get(current_step, [])

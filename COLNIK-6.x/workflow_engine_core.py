# SIRIUS COLNIK-6.x — Workflow Engine (CORE ONLY)
# This file contains ONLY the WorkflowEngine class without runtime loop.

class WorkflowEngine:
    def __init__(self):
        pass

    def run(self, request):
        action = request.get("action")
        execute_type = request.get("execute_type", None)

        # READ → ALLOW
        if action == "READ":
            return {"status": "ALLOW", "request": request}

        # DELETE → REQUIRE_CONFIRMATION
        if action == "DELETE":
            return {"status": "REQUIRE_CONFIRMATION", "request": request}

        # EXECUTE USER_APP → REQUIRE_CONFIRMATION
        if action == "EXECUTE" and execute_type == "USER_APP":
            return {"status": "REQUIRE_CONFIRMATION", "request": request}

        # EXECUTE SYSTEM → DENY
        if action == "EXECUTE" and execute_type == "SYSTEM":
            return {"status": "DENY", "request": request}

        # Default
        return {"status": "UNKNOWN", "request": request}

# SIRIUS COLNIK-6.x — Workflow Engine (CORE ONLY)
# This file contains ONLY the WorkflowEngine class without runtime loop.

# 🔥 OPRAVENÝ IMPORT — FUNGUJE PRI SPÚŠŤANÍ workflow_engine.py
import AUTONOMY.autonomy as autonomy_module

class WorkflowEngine:
    def __init__(self):
        # 🔥 vytvorenie autonómie cez modul
        self.autonomy = autonomy_module.Autonomy()

    def run(self, request):
        action = request.get("action")
        execute_type = request.get("execute_type", None)

        # ============================
        # READ → ALLOW
        # ============================
        if action == "READ":
            return {
                "status": "ALLOW",
                "action": action,
                "execute_type": execute_type,
                "request": request
            }

        # ============================
        # DELETE → REQUIRE_CONFIRMATION
        # ============================
        if action == "DELETE":
            return {
                "status": "REQUIRE_CONFIRMATION",
                "action": action,
                "execute_type": execute_type,
                "request": request
            }

        # ============================
        # EXECUTE USER_APP → REQUIRE_CONFIRMATION
        # ============================
        if action == "EXECUTE" and execute_type == "USER_APP":
            return {
                "status": "REQUIRE_CONFIRMATION",
                "action": action,
                "execute_type": execute_type,
                "request": request
            }

        # ============================
        # EXECUTE SYSTEM → DENY
        # ============================
        if action == "EXECUTE" and execute_type == "SYSTEM":
            return {
                "status": "DENY",
                "action": action,
                "execute_type": execute_type,
                "request": request
            }

        # ============================
        # UNKNOWN → DEFAULT
        # ============================
        return {
            "status": "UNKNOWN",
            "action": action,
            "execute_type": execute_type,
            "request": request
        }

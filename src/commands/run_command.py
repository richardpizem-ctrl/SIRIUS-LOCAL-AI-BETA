from commands.base_command import BaseCommand


class RunCommand(BaseCommand):
    """
    RunCommand 4.3
    Central execution of actions, AI tasks, and NL commands.

    Improvements in 4.3:
    - unified metadata contract
    - deterministic behavior for Runtime4
    - safe error handling (via BaseCommand.run)
    - consistent return structure
    - NL Router 4.x friendly
    - Self‑Repair 4.4 compatible
    """

    # ---------------------------------------------------------
    # METADATA (v4.3)
    # ---------------------------------------------------------
    name = "run"
    description = "Runs an AI task, NL command, or system action."
    category = "system"

    required_identity = "FAMILY"   # anyone may run commands, AccessControl decides
    risk_level = 0.1
    capabilities = ["command_exec"]

    keywords = ["run", "execute", "do", "perform"]
    examples = ["run move_text_files", "run system info"]

    # ---------------------------------------------------------
    # INIT
    # ---------------------------------------------------------
    def __init__(self, runtime=None, router=None, registry=None):
        self.runtime = runtime
        self.router = router
        self.registry = registry

    # ---------------------------------------------------------
    # EXECUTION (v4.3)
    # ---------------------------------------------------------
    def execute(self, *args, **kwargs):
        """
        Runs an AI task, NL command, or command from registry.
        """
        if not args:
            return {"status": "error", "message": "No action provided."}

        action = args[0]

        # -----------------------------------------------------
        # 1) Try command registry (highest priority)
        # -----------------------------------------------------
        if self.registry:
            cmd_cls = self.registry.get(action)
            if cmd_cls:
                try:
                    # Instantiate command with remaining args
                    cmd_instance = cmd_cls(*args[1:], **kwargs)
                    result = cmd_instance.run()
                    return {
                        "status": "command",
                        "command": action,
                        "result": result
                    }
                except Exception as e:
                    return {
                        "status": "error",
                        "message": f"Command '{action}' failed.",
                        "exception": str(e)
                    }

        # -----------------------------------------------------
        # 2) Try AI task
        # -----------------------------------------------------
        if self.runtime:
            result = self.runtime.handle_ai_task(action, {})
            if result is not None:
                return {
                    "status": "ai_task",
                    "task": action,
                    "result": result
                }

        # -----------------------------------------------------
        # 3) Try NL Router
        # -----------------------------------------------------
        if self.router:
            result = self.router.route(action)
            return {
                "status": "nl_router",
                "input": action,
                "result": result
            }

        # -----------------------------------------------------
        # 4) Fallback
        # -----------------------------------------------------
        return {
            "status": "fallback",
            "message": f"Running action: {action}"
        }

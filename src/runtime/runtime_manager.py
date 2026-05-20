import logging
import time
from typing import Dict, Any

from security_family.password_vault.vault_api import (
    save_password,
    retrieve_password
)

log = logging.getLogger(__name__)


class RuntimeManager:
    """
    RuntimeManager 4.4
    -------------------
    - Plugin loader (deterministic pipeline)
    - NL Router integrácia
    - AI Task handler (vrátane Password Vault)
    - Workflow engine integrácia
    - Security Family enforcement (4.4-ready)
    - Deterministic startup pipeline
    - Telemetry + degraded mode
    - Self‑Repair safe-mode
    - Stabilný, štruktúrovaný návratový model
    """

    def __init__(self):
        self.logger = logging.getLogger("RuntimeManager")
        self.plugins = None
        self.nl = None
        self.agent = None
        self.workflow = None
        self.ai_loop = None
        self.ui = None
        self.security = None
        self.engine = None

        self.safe_mode = False
        self.degraded_mode = False

    # --------------------------------------------------------
    # INITIALIZATION PIPELINE 4.4
    # --------------------------------------------------------
    def initialize(self) -> Dict[str, Any]:
        start_time = time.time()
        errors: list[str] = []
        warnings: list[str] = []

        self.logger.info("RuntimeManager 4.4 – initialization started")

        # SAFE MODE (Self‑Repair)
        if self.safe_mode:
            return {
                "status": "safe_mode",
                "message": "RuntimeManager started in safe-mode.",
                "duration": time.time() - start_time,
            }

        # ----------------------------------------------------
        # 1) Load plugins
        # ----------------------------------------------------
        try:
            plugin_result = self.plugins.load_all(self)
        except Exception as exc:
            msg = f"Plugin loading failed: {exc}"
            self.logger.error(msg)
            errors.append(msg)
            plugin_result = {
                "status": "error",
                "exception": str(exc),
                "instances": []
            }

        if plugin_result.get("degraded_mode"):
            self.degraded_mode = True
            errors.extend(plugin_result.get("errors", []))

        plugin_instances = list(getattr(self.plugins, "instances", {}).values())

        # ----------------------------------------------------
        # 2) Register NL commands
        # ----------------------------------------------------
        for plugin in plugin_instances:
            try:
                for key, fn in plugin.nl_commands().items():
                    self.nl.register(key, fn)
            except Exception as exc:
                msg = f"Failed to register NL commands for plugin {plugin}: {exc}"
                self.logger.error(msg)
                errors.append(msg)

        # ----------------------------------------------------
        # 3) Register AI tasks
        # ----------------------------------------------------
        for plugin in plugin_instances:
            try:
                for key, fn in plugin.ai_tasks().items():
                    self.agent.register_task(key, fn)
            except Exception as exc:
                msg = f"Failed to register AI tasks for plugin {plugin}: {exc}"
                self.logger.error(msg)
                errors.append(msg)

        # ----------------------------------------------------
        # 4) Register workflows
        # ----------------------------------------------------
        for plugin in plugin_instances:
            try:
                for wf in plugin.workflows():
                    self.workflow.register(wf)
            except Exception as exc:
                msg = f"Failed to register workflows for plugin {plugin}: {exc}"
                self.logger.error(msg)
                errors.append(msg)

        # ----------------------------------------------------
        # 5) Register AI loop rules
        # ----------------------------------------------------
        for plugin in plugin_instances:
            try:
                for rule in plugin.ai_loop_rules():
                    self.ai_loop.register(rule)
            except Exception as exc:
                msg = f"Failed to register AI loop rules for plugin {plugin}: {exc}"
                self.logger.error(msg)
                errors.append(msg)

        # ----------------------------------------------------
        # 6) Register GUI elements
        # ----------------------------------------------------
        for plugin in plugin_instances:
            try:
                for element in plugin.gui_elements():
                    self.ui.register(element)
            except Exception as exc:
                msg = f"Failed to register GUI elements for plugin {plugin}: {exc}"
                self.logger.error(msg)
                errors.append(msg)

        # ----------------------------------------------------
        # 7) Security Family validation
        # ----------------------------------------------------
        for plugin in plugin_instances:
            try:
                self.security.validate_plugin(plugin)
            except Exception as exc:
                msg = f"Security validation failed for plugin {plugin}: {exc}"
                self.logger.error(msg)
                errors.append(msg)

        # ----------------------------------------------------
        # 8) Initialize modules (RuntimeEngine modules)
        # ----------------------------------------------------
        for name, module in self.engine.modules.items():
            instance = module.get("instance")
            try:
                if hasattr(instance, "initialize"):
                    res = instance.initialize()
                    if isinstance(res, dict) and res.get("status") == "error":
                        msg = f"Module '{name}' initialization reported error: {res}"
                        self.logger.error(msg)
                        errors.append(msg)
            except Exception as exc:
                msg = f"Module initialization failed for '{name}': {exc}"
                self.logger.error(msg)
                errors.append(msg)

        duration = time.time() - start_time
        self.logger.info("RuntimeManager 4.4 – initialization complete")

        degraded = bool(errors)
        self.degraded_mode = self.degraded_mode or degraded

        return {
            "status": "degraded" if degraded else "success",
            "errors": errors,
            "warnings": warnings,
            "plugins": plugin_result,
            "duration": duration,
            "degraded_mode": self.degraded_mode,
        }

    # --------------------------------------------------------
    # NATURAL LANGUAGE HANDLER
    # --------------------------------------------------------
    def handle_nl(self, text: str) -> Dict[str, Any]:
        return self.nl.handle(text)

    # --------------------------------------------------------
    # AI TASK HANDLER (PASSWORD VAULT + FALLBACK)
    # --------------------------------------------------------
    def handle_ai_task(self, goal: str, args: Dict[str, Any]) -> Dict[str, Any]:
        # PASSWORD VAULT – SAVE
        if goal == "password.save":
            domain = args.get("domain")
            username = args.get("username", "default")
            password = args.get("password")

            if not domain or not password:
                return {"status": "error", "message": "Missing domain or password"}

            save_password(domain, username, password)
            return {"status": "ok", "message": f"Password saved for {domain}"}

        # PASSWORD VAULT – RETRIEVE
        if goal == "password.retrieve":
            domain = args.get("domain")
            username = args.get("username", "default")

            if not domain:
                return {"status": "error", "message": "Missing domain"}

            entry = retrieve_password(domain, username)
            if entry:
                return {
                    "status": "ok",
                    "domain": domain,
                    "username": username,
                    "password": entry["password"]
                }
            else:
                return {"status": "not_found", "message": f"No password for {domain}"}

        # PASSWORD VAULT – AUTOFILL
        if goal == "password.autofill":
            domain = args.get("domain")
            username = args.get("username", "default")

            entry = retrieve_password(domain, username)
            if not entry:
                return {"status": "not_found", "message": f"No password for {domain}"}

            return {
                "status": "ok",
                "message": f"Password for {domain} prepared for autofill"
            }

        # FALLBACK TO AGENT TASKS
        try:
            return self.agent.run_task(goal, args)
        except Exception as exc:
            self.logger.error(f"AI task handler error for goal '{goal}': {exc}")
            return {"status": "error", "message": str(exc)}

    # --------------------------------------------------------
    # CONTEXT
    # --------------------------------------------------------
    def get_ai_context(self) -> Dict[str, Any]:
        return self.agent.get_context()

    # --------------------------------------------------------
    # ENGINE CONTROL
    # --------------------------------------------------------
    def start(self) -> Dict[str, Any]:
        res = self.engine.start()
        return res if isinstance(res, dict) else {"status": "success"}

    def stop(self) -> Dict[str, Any]:
        res = self.engine.stop()
        return res if isinstance(res, dict) else {"status": "success"}

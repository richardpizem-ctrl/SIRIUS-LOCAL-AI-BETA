import logging
from typing import Dict, Any

from security_family.password_vault.vault_api import (
    save_password,
    retrieve_password
)

log = logging.getLogger(__name__)


class RuntimeManager:
    """
    RuntimeManager 4.0
    - Plugin loader
    - NL Router
    - AI Task handler
    - Workflow engine
    - Security Family enforcement
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

    # --------------------------------------------------------
    # INITIALIZATION PIPELINE
    # --------------------------------------------------------
    def initialize(self):
        """
        RuntimeManager 4.0 initialization pipeline
        """

        self.logger.info("RuntimeManager 4.0 – initialization started")

        # 1) Load plugins
        self.plugins.load_all(self)
        plugin_instances = list(self.plugins.instances.values())

        # 2) Register NL commands
        for plugin in plugin_instances:
            try:
                for key, fn in plugin.nl_commands().items():
                    self.nl.register(key, fn)
                    self.logger.info(f"NL command registered: {key}")
            except Exception as exc:
                self.logger.error(f"Failed to register NL commands for plugin {plugin}: {exc}")

        # 3) Register AI tasks
        for plugin in plugin_instances:
            try:
                for key, fn in plugin.ai_tasks().items():
                    self.agent.register_task(key, fn)
                    self.logger.info(f"AI task registered: {key}")
            except Exception as exc:
                self.logger.error(f"Failed to register AI tasks for plugin {plugin}: {exc}")

        # 4) Register workflows
        for plugin in plugin_instances:
            try:
                for wf in plugin.workflows():
                    self.workflow.register(wf)
                    self.logger.info(f"Workflow registered: {wf.get('name')}")
            except Exception as exc:
                self.logger.error(f"Failed to register workflows for plugin {plugin}: {exc}")

        # 5) Register AI loop rules
        for plugin in plugin_instances:
            try:
                for rule in plugin.ai_loop_rules():
                    self.ai_loop.register(rule)
                    self.logger.info(f"AI loop rule registered: {rule.get('name')}")
            except Exception as exc:
                self.logger.error(f"Failed to register AI loop rules for plugin {plugin}: {exc}")

        # 6) Register GUI elements
        for plugin in plugin_instances:
            try:
                for element in plugin.gui_elements():
                    self.ui.register(element)
                    self.logger.info(f"GUI element registered: {element.get('label')}")
            except Exception as exc:
                self.logger.error(f"Failed to register GUI elements for plugin {plugin}: {exc}")

        # 7) Security Family validation
        for plugin in plugin_instances:
            try:
                self.security.validate_plugin(plugin)
            except Exception as exc:
                self.logger.error(f"Security validation failed for plugin {plugin}: {exc}")

        # 8) Initialize modules
        for module in self.engine.modules.values():
            try:
                module["instance"].initialize()
            except Exception as exc:
                self.logger.error(f"Module initialization failed: {exc}")

        self.logger.info("RuntimeManager 4.0 – initialization complete")

    # --------------------------------------------------------
    # NATURAL LANGUAGE HANDLER
    # --------------------------------------------------------
    def handle_nl(self, text: str) -> Dict[str, Any]:
        return self.nl.handle(text)

    # --------------------------------------------------------
    # AI TASK HANDLER (THIS IS WHERE PASSWORD VAULT GOES)
    # --------------------------------------------------------
    def handle_ai_task(self, goal: str, args: Dict[str, Any]) -> Dict[str, Any]:
        """
        AI Task Dispatcher 4.0
        """

        # ----------------------------------------------------
        # PASSWORD VAULT – SAVE
        # ----------------------------------------------------
        if goal == "password.save":
            domain = args.get("domain")
            username = args.get("username", "default")
            password = args.get("password")

            if not domain or not password:
                return {"status": "error", "message": "Missing domain or password"}

            save_password(domain, username, password)
            return {"status": "ok", "message": f"Password saved for {domain}"}

        # ----------------------------------------------------
        # PASSWORD VAULT – RETRIEVE
        # ----------------------------------------------------
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

        # ----------------------------------------------------
        # PASSWORD VAULT – AUTOFILL (PC)
        # ----------------------------------------------------
        if goal == "password.autofill":
            domain = args.get("domain")
            username = args.get("username", "default")

            entry = retrieve_password(domain, username)
            if not entry:
                return {"status": "not_found", "message": f"No password for {domain}"}

            # TODO: Windows UI Automation autofill
            return {
                "status": "ok",
                "message": f"Password for {domain} prepared for autofill"
            }

        # ----------------------------------------------------
        # FALLBACK TO AGENT TASKS
        # ----------------------------------------------------
        try:
            return self.agent.run_task(goal, args)
        except Exception as exc:
            return {"status": "error", "message": str(exc)}

    # --------------------------------------------------------
    # CONTEXT
    # --------------------------------------------------------
    def get_ai_context(self) -> Dict[str, Any]:
        return self.agent.get_context()

    # --------------------------------------------------------
    # ENGINE CONTROL
    # --------------------------------------------------------
    def start(self):
        self.engine.start()

    def stop(self):
        self.engine.stop()

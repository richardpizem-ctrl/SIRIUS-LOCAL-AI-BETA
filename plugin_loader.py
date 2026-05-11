import os
import importlib
import json


# ============================================================
# PLUGIN LOADER (v4.0.0)
# ============================================================
class PluginLoader:
    """
    SIRIUS LOCAL AI — Plugin Loader (v4.0.0)

    Responsibilities:
    - Load plugins from /plugins directory
    - Validate manifest.json
    - Dynamically import plugin modules
    - Register NL commands, AI tasks, workflows, rules, GUI elements
    - Unified logging through RuntimeManager
    """

    def __init__(self, runtime_manager):
        self.rm = runtime_manager
        self.plugins = {}
        self.plugin_dir = "plugins"

        self.rm.logger.info("PluginLoader initialized (v4.0.0)")

    # --------------------------------------------------------
    # MAIN LOADER (v4)
    # --------------------------------------------------------
    def load_plugins(self):
        """Load all plugins from /plugins directory."""
        if not os.path.exists(self.plugin_dir):
            self.rm.logger.warning("No plugins/ directory found — skipping.")
            return

        for folder in os.listdir(self.plugin_dir):
            path = os.path.join(self.plugin_dir, folder)

            if not os.path.isdir(path):
                continue

            manifest_path = os.path.join(path, "manifest.json")
            plugin_path = os.path.join(path, "plugin.py")

            if not os.path.exists(manifest_path) or not os.path.exists(plugin_path):
                self.rm.logger.error(f"Plugin '{folder}' missing manifest or plugin.py")
                continue

            try:
                manifest = self._load_manifest(manifest_path)
                module = self._load_module(folder)

                if not hasattr(module, "Plugin"):
                    self.rm.logger.error(f"Plugin '{folder}' missing Plugin class")
                    continue

                plugin_instance = module.Plugin(self.rm)
                self.plugins[folder] = plugin_instance

                self._register_plugin(plugin_instance, manifest)

                self.rm.logger.info(f"Loaded plugin: {manifest.get('name')}")

            except Exception as e:
                self.rm.logger.error(f"Error loading plugin '{folder}': {e}")

    # --------------------------------------------------------
    # MANIFEST LOADING (v4)
    # --------------------------------------------------------
    def _load_manifest(self, path):
        """Load and parse manifest.json."""
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            self.rm.logger.error(f"Manifest load error: {e}")
            return {}

    # --------------------------------------------------------
    # DYNAMIC MODULE IMPORT (v4)
    # --------------------------------------------------------
    def _load_module(self, folder):
        """Import plugin module dynamically."""
        module_name = f"plugins.{folder}.plugin"
        return importlib.import_module(module_name)

    # --------------------------------------------------------
    # PLUGIN REGISTRATION (v4)
    # --------------------------------------------------------
    def _register_plugin(self, plugin, manifest):
        """Register plugin capabilities into RuntimeManager."""

        # NL commands
        if hasattr(plugin, "nl_commands"):
            for cmd, fn in plugin.nl_commands().items():
                self.rm.register_nl_command(cmd, fn)

        # AI tasks
        if hasattr(plugin, "ai_tasks"):
            for task, fn in plugin.ai_tasks().items():
                self.rm.register_ai_task(task, fn)

        # Workflows
        if hasattr(plugin, "workflows"):
            for wf in plugin.workflows():
                self.rm.register_workflow(wf)

        # AI Loop rules
        if hasattr(plugin, "ai_loop_rules"):
            for rule in plugin.ai_loop_rules():
                self.rm.register_ai_loop_rule(rule)

        # GUI elements
        if hasattr(plugin, "gui_elements"):
            for element in plugin.gui_elements():
                self.rm.register_gui_element(element)

        self.rm.logger.info(
            f"Plugin '{manifest.get('name')}' successfully registered."
        )

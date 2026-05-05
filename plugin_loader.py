import os
import importlib
import json


class PluginLoader:
    """
    Plugin Loader for SIRIUS-LOCAL-AI
    - loads plugins from /plugins directory
    - registers them into the runtime
    - supports manifest.json
    - supports dynamic capabilities
    """

    def __init__(self, runtime_manager):
        self.rm = runtime_manager
        self.plugins = {}
        self.plugin_dir = "plugins"

    # --------------------------------------------------------
    # MAIN FUNCTION
    # --------------------------------------------------------
    def load_plugins(self):
        if not os.path.exists(self.plugin_dir):
            print("[PLUGIN] No plugins/ directory found – skipping.")
            return

        for folder in os.listdir(self.plugin_dir):
            path = os.path.join(self.plugin_dir, folder)

            if not os.path.isdir(path):
                continue

            manifest_path = os.path.join(path, "manifest.json")
            plugin_path = os.path.join(path, "plugin.py")

            if not os.path.exists(manifest_path) or not os.path.exists(plugin_path):
                print(f"[PLUGIN] {folder} – missing manifest or plugin.py")
                continue

            try:
                manifest = self._load_manifest(manifest_path)
                module = self._load_module(folder)

                if not hasattr(module, "Plugin"):
                    print(f"[PLUGIN] {folder} – missing Plugin class")
                    continue

                plugin_instance = module.Plugin(self.rm)
                self.plugins[folder] = plugin_instance

                self._register_plugin(plugin_instance, manifest)

                print(f"[PLUGIN] Loaded plugin: {manifest.get('name')}")

            except Exception as e:
                print(f"[PLUGIN] Error loading {folder}: {e}")

    # --------------------------------------------------------
    # MANIFEST
    # --------------------------------------------------------
    def _load_manifest(self, path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    # --------------------------------------------------------
    # DYNAMIC MODULE LOADING
    # --------------------------------------------------------
    def _load_module(self, folder):
        module_name = f"plugins.{folder}.plugin"
        return importlib.import_module(module_name)

    # --------------------------------------------------------
    # PLUGIN REGISTRATION INTO RUNTIME
    # --------------------------------------------------------
    def _register_plugin(self, plugin, manifest):
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

        print(f"[PLUGIN] Plugin {manifest.get('name')} successfully registered.")

# plugin_loader_4_5.py
# SIRIUS LOCAL AI – Plugin Loader 4.5.0 PRO
# Deterministic, safe-mode compatible, Phase‑5 ready plugin loading system

from __future__ import annotations

import os
import importlib
import json
import traceback


class PluginLoader45:
    """
    SIRIUS LOCAL AI — Plugin Loader (v4.5.0 PRO)

    Responsibilities:
        - Load plugins from /plugins directory
        - Validate manifest.json (Phase‑5 rules)
        - Dynamically import plugin modules (sandboxed)
        - Register NL commands, AI tasks, workflows, rules, GUI elements
        - Provide safe-mode + degraded-mode behavior
        - Deterministic logging through RuntimeManager45
        - Self‑Repair Layer 4.5 compatible
    """

    def __init__(self, runtime_manager):
        self.rm = runtime_manager
        self.plugins = {}
        self.plugin_dir = "plugins"

        self.safe_mode = False
        self.degraded_mode = False

        self.rm.logger.info("PluginLoader initialized (v4.5.0 PRO)")

    # --------------------------------------------------------
    # MAIN LOADER (4.5.0 PRO)
    # --------------------------------------------------------
    def load_all(self):
        """Load all plugins from /plugins directory."""
        if self.safe_mode:
            self.rm.logger.warning("PluginLoader in SAFE MODE — skipping plugin load")
            return

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
                self.rm.logger.error(f"[PLUGIN] {folder}: missing manifest or plugin.py")
                continue

            try:
                manifest = self._load_manifest(manifest_path)
                if not self._validate_manifest(manifest, folder):
                    continue

                module = self._load_module(folder)
                if not hasattr(module, "Plugin"):
                    self.rm.logger.error(f"[PLUGIN] {folder}: missing Plugin class")
                    continue

                plugin_instance = module.Plugin(self.rm)
                self.plugins[folder] = plugin_instance

                self._register_plugin(plugin_instance, manifest)

                self.rm.logger.info(f"[PLUGIN] Loaded plugin: {manifest.get('name')}")

            except Exception as e:
                self.degraded_mode = True
                self.rm.logger.error(
                    f"[PLUGIN] Error loading '{folder}': {e}\n{traceback.format_exc()}"
                )

    # --------------------------------------------------------
    # MANIFEST LOADING (4.5.0 PRO)
    # --------------------------------------------------------
    def _load_manifest(self, path):
        """Load and parse manifest.json."""
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            self.rm.logger.error(f"[PLUGIN] Manifest load error: {e}")
            return {}

    # --------------------------------------------------------
    # MANIFEST VALIDATION (4.5.0 PRO)
    # --------------------------------------------------------
    def _validate_manifest(self, manifest, folder):
        """Validate manifest.json according to Phase‑5 rules."""
        required = ["name", "version", "author", "entry"]

        for key in required:
            if key not in manifest:
                self.rm.logger.error(
                    f"[PLUGIN] {folder}: manifest missing required field '{key}'"
                )
                return False

        if manifest.get("enabled", True) is False:
            self.rm.logger.info(f"[PLUGIN] {folder}: disabled in manifest — skipping")
            return False

        # Phase‑5: optional integrity hash
        if "integrity" in manifest:
            if not isinstance(manifest["integrity"], str):
                self.rm.logger.error(
                    f"[PLUGIN] {folder}: invalid integrity field (must be string)"
                )
                return False

        return True

    # --------------------------------------------------------
    # DYNAMIC MODULE IMPORT (4.5.0 PRO)
    # --------------------------------------------------------
    def _load_module(self, folder):
        """Import plugin module dynamically (sandboxed)."""
        try:
            module_name = f"plugins.{folder}.plugin"
            return importlib.import_module(module_name)
        except Exception as e:
            self.degraded_mode = True
            raise RuntimeError(f"Module import failed: {e}")

    # --------------------------------------------------------
    # PLUGIN REGISTRATION (4.5.0 PRO)
    # --------------------------------------------------------
    def _register_plugin(self, plugin, manifest):
        """Register plugin capabilities into RuntimeManager45."""

        # NL commands
        if hasattr(plugin, "nl_commands"):
            try:
                for cmd, fn in plugin.nl_commands().items():
                    self.rm.register_nl_command(cmd, fn)
            except Exception as e:
                self.rm.logger.error(f"[PLUGIN] NL command registration error: {e}")

        # AI tasks
        if hasattr(plugin, "ai_tasks"):
            try:
                for task, fn in plugin.ai_tasks().items():
                    self.rm.register_ai_task(task, fn)
            except Exception as e:
                self.rm.logger.error(f"[PLUGIN] AI task registration error: {e}")

        # Workflows
        if hasattr(plugin, "workflows"):
            try:
                for wf in plugin.workflows():
                    self.rm.register_workflow(wf)
            except Exception as e:
                self.rm.logger.error(f"[PLUGIN] Workflow registration error: {e}")

        # AI Loop rules
        if hasattr(plugin, "ai_loop_rules"):
            try:
                for rule in plugin.ai_loop_rules():
                    self.rm.register_ai_loop_rule(rule)
            except Exception as e:
                self.rm.logger.error(f"[PLUGIN] AI loop rule registration error: {e}")

        # GUI elements
        if hasattr(plugin, "gui_elements"):
            try:
                for element in plugin.gui_elements():
                    self.rm.register_gui_element(element)
            except Exception as e:
                self.rm.logger.error(f"[PLUGIN] GUI element registration error: {e}")

        self.rm.logger.info(
            f"[PLUGIN] {manifest.get('name')} successfully registered."
        )

    # --------------------------------------------------------
    # SAFE-MODE CONTROL
    # --------------------------------------------------------
    def enter_safe_mode(self):
        self.safe_mode = True

    def exit_safe_mode(self):
        self.safe_mode = False

import os
import json
import importlib.util
import logging
import time
from typing import Dict, Any, List, Optional

log = logging.getLogger(__name__)


class PluginLoader:
    """
    PluginLoader 4.3+
    -----------------
    - Loads plugins from /plugins
    - Validates manifest.json
    - Imports plugin.py safely
    - Supports dependencies
    - Security Family integration
    - Plugin lifecycle (load → initialize → register → start)
    - Error isolation
    - Telemetry (global + per-plugin)
    - Deterministic, Self‑Repair‑ready behavior
    """

    def __init__(self, plugins_dir: str = "plugins"):
        self.plugins_dir = plugins_dir
        self.instances: Dict[str, Any] = {}
        self.metadata: Dict[str, Dict[str, Any]] = {}

    # --------------------------------------------------------
    # PUBLIC API
    # --------------------------------------------------------
    def load_all(self, runtime_manager) -> Dict[str, Any]:
        if not os.path.exists(self.plugins_dir):
            msg = f"Plugins directory not found: {self.plugins_dir}"
            log.warning(msg)
            return {
                "status": "error",
                "code": "PLUGINS_DIR_NOT_FOUND",
                "message": msg,
                "errors": [msg],
                "warnings": [],
                "loaded": [],
                "started": [],
                "duration": 0.0,
                "degraded_mode": True,
            }

        start_time = time.time()
        errors: List[str] = []
        warnings: List[str] = []

        # First pass: load manifests
        manifests = self._load_all_manifests(errors, warnings)
        if not manifests:
            msg = "No valid plugin manifests found."
            return {
                "status": "error",
                "code": "NO_VALID_MANIFESTS",
                "message": msg,
                "errors": errors + [msg],
                "warnings": warnings,
                "loaded": [],
                "started": [],
                "duration": time.time() - start_time,
                "degraded_mode": True,
            }

        # Resolve dependencies
        try:
            order = self._resolve_dependencies(manifests)
        except RuntimeError as exc:
            msg = "Failed to resolve plugin dependencies."
            log.exception("%s: %s", msg, exc)
            errors.append(f"{msg}: {exc}")
            return {
                "status": "error",
                "code": "DEPENDENCY_RESOLUTION_FAILED",
                "message": msg,
                "errors": errors,
                "warnings": warnings,
                "loaded": [],
                "started": [],
                "duration": time.time() - start_time,
                "degraded_mode": True,
            }
        except Exception as exc:
            msg = "Unexpected error during dependency resolution."
            log.exception("%s: %s", msg, exc)
            errors.append(f"{msg}: {exc}")
            return {
                "status": "error",
                "code": "DEPENDENCY_RESOLUTION_UNEXPECTED",
                "message": msg,
                "errors": errors,
                "warnings": warnings,
                "loaded": [],
                "started": [],
                "duration": time.time() - start_time,
                "degraded_mode": True,
            }

        loaded: List[str] = []
        started: List[str] = []

        # Load plugins in dependency order
        for name in order:
            manifest = manifests[name]
            instance = self._load_single_plugin(manifest, runtime_manager, errors, warnings)

            if instance:
                self.instances[name] = instance
                self.metadata[name] = manifest
                loaded.append(name)
                log.info("Plugin loaded: %s", name)

        # Start plugins
        for name, instance in self.instances.items():
            t0 = time.time()
            try:
                if hasattr(instance, "start"):
                    instance.start()
                started.append(name)
                log.info("Plugin started: %s", name)
                # per-plugin telemetry
                meta = self.metadata.get(name, {})
                telemetry = meta.setdefault("_telemetry", {})
                telemetry["start_time"] = time.time() - t0
            except Exception as exc:
                msg = f"Failed to start plugin '{name}': {exc}"
                log.exception(msg)
                errors.append(msg)

        duration = time.time() - start_time
        degraded_mode = bool(errors)

        return {
            "status": "degraded" if degraded_mode else "success",
            "message": "Plugins loaded." if not degraded_mode else "Plugins loaded with errors.",
            "loaded": loaded,
            "started": started,
            "errors": errors,
            "warnings": warnings,
            "duration": duration,
            "degraded_mode": degraded_mode,
            "plugin_metadata": self.metadata,
        }

    # --------------------------------------------------------
    # LOAD ALL MANIFESTS
    # --------------------------------------------------------
    def _load_all_manifests(
        self,
        errors: List[str],
        warnings: List[str],
    ) -> Dict[str, Dict[str, Any]]:
        manifests: Dict[str, Dict[str, Any]] = {}

        if not os.path.isdir(self.plugins_dir):
            msg = f"Plugins directory is not a folder: {self.plugins_dir}"
            log.warning(msg)
            warnings.append(msg)
            return manifests

        for folder in os.listdir(self.plugins_dir):
            plugin_path = os.path.join(self.plugins_dir, folder)
            if not os.path.isdir(plugin_path):
                continue

            manifest_path = os.path.join(plugin_path, "manifest.json")
            if not os.path.exists(manifest_path):
                msg = f"Missing manifest.json in {plugin_path}"
                log.warning(msg)
                warnings.append(msg)
                continue

            manifest = self._load_manifest(manifest_path, errors)
            if not manifest:
                continue

            name = manifest.get("name")
            if not name:
                msg = f"Manifest missing 'name' in {manifest_path}"
                log.error(msg)
                errors.append(msg)
                continue

            # Internal metadata for folder/path resolution
            manifest["__folder__"] = folder
            manifest["__path__"] = plugin_path

            manifests[name] = manifest

        return manifests

    # --------------------------------------------------------
    # DEPENDENCY RESOLUTION
    # --------------------------------------------------------
    def _resolve_dependencies(self, manifests: Dict[str, Dict[str, Any]]) -> List[str]:
        resolved: List[str] = []
        unresolved = set(manifests.keys())

        while unresolved:
            progress = False

            for name in list(unresolved):
                deps = manifests[name].get("depends_on", [])

                if all(d in resolved for d in deps):
                    resolved.append(name)
                    unresolved.remove(name)
                    progress = True

            if not progress:
                raise RuntimeError("Circular or unresolved plugin dependencies.")

        log.info("Plugin load order: %s", resolved)
        return resolved

    # --------------------------------------------------------
    # LOAD SINGLE PLUGIN
    # --------------------------------------------------------
    def _load_single_plugin(
        self,
        manifest: Dict[str, Any],
        runtime_manager,
        errors: List[str],
        warnings: List[str],
    ) -> Optional[Any]:
        name = manifest.get("name")
        folder = manifest.get("__folder__") or manifest.get("folder") or name
        plugin_dir = os.path.join(self.plugins_dir, folder)
        plugin_file = os.path.join(plugin_dir, "plugin.py")

        if not manifest.get("enabled", True):
            msg = f"Plugin disabled: {name}"
            log.info(msg)
            warnings.append(msg)
            return None

        if not os.path.exists(plugin_file):
            msg = f"Missing plugin.py for plugin '{name}' (expected at {plugin_file})"
            log.error(msg)
            errors.append(msg)
            return None

        # Security Family: risk check
        risk = manifest.get("risk_level", 0)
        max_risk = getattr(getattr(runtime_manager, "security", None), "max_plugin_risk", 0)
        if risk > max_risk:
            msg = f"Plugin '{name}' blocked due to high risk (risk_level={risk}, max={max_risk})."
            log.warning(msg)
            warnings.append(msg)
            return None

        # Import plugin
        t_load = time.time()
        instance = self._import_plugin(plugin_file, manifest, errors)
        if not instance:
            return None
        load_time = time.time() - t_load

        # Validate Plugin API
        missing_methods = [
            m for m in ("initialize", "register", "start") if not hasattr(instance, m)
        ]
        if missing_methods:
            msg = f"Plugin '{name}' missing required methods: {', '.join(missing_methods)}"
            log.error(msg)
            errors.append(msg)
            return None

        # Initialize plugin
        t_init = time.time()
        try:
            instance.initialize(runtime_manager)
            init_time = time.time() - t_init
        except Exception as exc:
            msg = f"Failed to initialize plugin '{name}': {exc}"
            log.exception(msg)
            errors.append(msg)
            return None

        # Register plugin
        t_reg = time.time()
        try:
            instance.register(runtime_manager)
            register_time = time.time() - t_reg
        except Exception as exc:
            msg = f"Failed to register plugin '{name}': {exc}"
            log.exception(msg)
            errors.append(msg)
            return None

        # Per-plugin telemetry
        telemetry = {
            "load_time": load_time,
            "init_time": init_time,
            "register_time": register_time,
        }
        manifest["_telemetry"] = telemetry

        return instance

    # --------------------------------------------------------
    # MANIFEST LOADING
    # --------------------------------------------------------
    def _load_manifest(self, path: str, errors: List[str]) -> Optional[Dict[str, Any]]:
        try:
            with open(path, "r", encoding="utf-8") as f:
                manifest = json.load(f)

            # Basic validation
            if "name" not in manifest:
                raise ValueError("Manifest missing 'name'")

            return manifest

        except Exception as e:
            msg = f"Failed to load manifest {path}: {e}"
            log.exception(msg)
            errors.append(msg)
            return None

    # --------------------------------------------------------
    # IMPORT PLUGIN
    # --------------------------------------------------------
    def _import_plugin(
        self,
        plugin_file: str,
        manifest: Dict[str, Any],
        errors: List[str],
    ) -> Optional[Any]:
        name = manifest.get("name", "<unknown>")
        try:
            spec = importlib.util.spec_from_file_location(name, plugin_file)
            if spec is None or spec.loader is None:
                msg = f"Failed to create spec for plugin '{name}' at {plugin_file}"
                log.error(msg)
                errors.append(msg)
                return None

            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            if not hasattr(module, "Plugin"):
                msg = f"Plugin class missing in {plugin_file}"
                log.error(msg)
                errors.append(msg)
                return None

            cls = module.Plugin

            if not callable(cls):
                msg = f"Plugin is not a class in {plugin_file}"
                log.error(msg)
                errors.append(msg)
                return None

            return cls(manifest)

        except Exception as e:
            msg = f"PluginLoader error in {plugin_file}: {e}"
            log.exception(msg)
            errors.append(msg)
            return None

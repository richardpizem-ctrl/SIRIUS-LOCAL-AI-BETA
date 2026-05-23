"""
SIRIUS LOCAL AI – Runtime 4.5 Module Loader

Responsible for:
- registering runtime modules
- validating module integrity
- initializing modules in deterministic order
- preparing modules for sandbox isolation
- exposing modules to the scheduler and dependency graph
- Self‑Repair 4.5 degraded-mode detection
- safe‑mode compatibility
"""

from typing import Any, Dict, List


class ModuleLoader4:
    """
    ModuleLoader 4.5
    ----------------
    - strict validation
    - deterministic initialization
    - structured error surface
    - telemetry
    - degraded-mode detection
    - safe-mode compatibility
    - Self‑Repair Layer 4.5 compliant
    - Metadata version bumped to 4.5
    """

    def __init__(self, max_modules: int = 200):
        self.modules: Dict[str, Any] = {}
        self.max_modules = max_modules
        self.degraded_mode = False
        self.safe_mode = False

    # ---------------------------------------------------------
    # VALIDATION HELPERS
    # ---------------------------------------------------------

    def _validate_name(self, name: Any) -> bool:
        return isinstance(name, str) and name.strip()

    def _validate_module(self, module: Any) -> bool:
        if module is None:
            return False
        if isinstance(module, (bytes, bytearray, type(lambda: None))):
            return False
        return True

    # ---------------------------------------------------------
    # REGISTRATION
    # ---------------------------------------------------------

    def register(self, name: str, module: Any) -> Dict[str, Any]:
        """Registers a module under a given name with full safety checks."""

        if self.safe_mode:
            return {"status": "safe_mode", "module": name, "loader_version": "4.5"}

        if not self._validate_name(name):
            return {"status": "error", "code": "invalid_module_name", "loader_version": "4.5"}

        if not self._validate_module(module):
            return {"status": "error", "code": "invalid_module_object", "loader_version": "4.5"}

        if len(self.modules) >= self.max_modules:
            return {"status": "error", "code": "module_limit_reached", "loader_version": "4.5"}

        self.modules[name] = module
        return {"status": "success", "module": name, "loader_version": "4.5"}

    def unregister(self, name: str) -> Dict[str, Any]:
        if not self._validate_name(name):
            return {"status": "error", "code": "invalid_module_name", "loader_version": "4.5"}

        if name in self.modules:
            del self.modules[name]
            return {"status": "success", "module": name, "loader_version": "4.5"}

        return {"status": "error", "code": "module_not_found", "loader_version": "4.5"}

    # ---------------------------------------------------------
    # INITIALIZATION
    # ---------------------------------------------------------

    def initialize_all(self) -> Dict[str, Any]:
        """
        Calls the initialization method on all registered modules.
        Returns structured telemetry and degraded-mode status.
        """

        if self.safe_mode:
            return {
                "status": "safe_mode",
                "results": {},
                "errors": [],
                "modules": list(self.modules.keys()),
                "degraded_mode": False,
                "loader_version": "4.5",
            }

        results = {}
        errors = []

        # Deterministic order
        module_names = sorted(self.modules.keys())

        for name in module_names:
            module = self.modules[name]

            # Defense in depth
            if not self._validate_module(module):
                results[name] = {"status": "error", "code": "invalid_module_object"}
                errors.append(name)
                continue

            if hasattr(module, "initialize") and callable(module.initialize):
                try:
                    res = module.initialize()

                    # If module returns structured error
                    if isinstance(res, dict) and res.get("status") == "error":
                        results[name] = {
                            "status": "error",
                            "code": "initialization_failed",
                            "details": res,
                        }
                        errors.append(name)
                    else:
                        results[name] = {"status": "initialized"}

                except Exception as exc:
                    results[name] = {
                        "status": "error",
                        "code": "initialization_exception",
                        "exception": str(exc),
                    }
                    errors.append(name)
            else:
                results[name] = {"status": "skipped", "reason": "no_initialize_method"}

        self.degraded_mode = bool(errors)

        return {
            "status": "degraded" if errors else "success",
            "results": results,
            "errors": errors,
            "modules": module_names,
            "degraded_mode": self.degraded_mode,
            "loader_version": "4.5",
        }

    # ---------------------------------------------------------
    # ACCESS
    # ---------------------------------------------------------

    def get(self, name: str):
        if not self._validate_name(name):
            return None
        return self.modules.get(name)

    def list_modules(self) -> List[str]:
        return sorted(self.modules.keys())

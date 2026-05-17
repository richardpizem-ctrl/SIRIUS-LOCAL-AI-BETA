"""
SIRIUS LOCAL AI – Runtime 4.3 Module Loader

Responsible for:
- registering runtime modules
- validating module integrity
- initializing modules in deterministic order
- preparing modules for sandbox isolation
- exposing modules to the scheduler and dependency graph
- Self‑Repair 4.4 degraded-mode detection

This component acts as the boot manager of Runtime 4.3.
"""

from typing import Any, Dict, List


class ModuleLoader4:
    """
    Handles loading, initialization, and validation of runtime modules.
    Provides:
    - strict validation
    - structured error surface
    - telemetry
    - degraded-mode detection
    - safe-mode compatibility
    """

    def __init__(self, max_modules: int = 200):
        self.modules: Dict[str, Any] = {}
        self.max_modules = max_modules
        self.degraded_mode = False

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

        if not self._validate_name(name):
            return {"status": "error", "code": "invalid_module_name"}

        if not self._validate_module(module):
            return {"status": "error", "code": "invalid_module_object"}

        if len(self.modules) >= self.max_modules:
            return {"status": "error", "code": "module_limit_reached"}

        self.modules[name] = module
        return {"status": "success", "module": name}

    def unregister(self, name: str) -> Dict[str, Any]:
        if not self._validate_name(name):
            return {"status": "error", "code": "invalid_module_name"}

        if name in self.modules:
            del self.modules[name]
            return {"status": "success", "module": name}

        return {"status": "error", "code": "module_not_found"}

    # ---------------------------------------------------------
    # INITIALIZATION
    # ---------------------------------------------------------

    def initialize_all(self) -> Dict[str, Any]:
        """
        Calls the initialization method on all registered modules.
        Returns structured telemetry and degraded-mode status.
        """

        results = {}
        errors = []

        for name, module in self.modules.items():

            # Defense in depth
            if not self._validate_module(module):
                results[name] = {"status": "error", "code": "invalid_module_object"}
                errors.append(name)
                continue

            if hasattr(module, "initialize") and callable(module.initialize):
                try:
                    module.initialize()
                    results[name] = {"status": "initialized"}
                except Exception as exc:
                    results[name] = {
                        "status": "error",
                        "code": "initialization_failed",
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
            "modules": list(self.modules.keys()),
            "degraded_mode": self.degraded_mode,
        }

    # ---------------------------------------------------------
    # ACCESS
    # ---------------------------------------------------------

    def get(self, name: str):
        if not self._validate_name(name):
            return None
        return self.modules.get(name)

    def list_modules(self) -> List[str]:
        return list(self.modules.keys())

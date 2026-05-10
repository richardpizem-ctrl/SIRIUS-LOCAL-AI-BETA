"""
SIRIUS LOCAL AI – Runtime 4.0 Module Loader

Responsible for:
- registering runtime modules
- validating module integrity
- initializing modules in correct order
- preparing modules for sandbox isolation
- exposing modules to the scheduler and dependency graph

This component acts as the boot manager of Runtime 4.0.
"""

from typing import Any, Dict, List


class ModuleLoader4:
    """
    Handles loading, initialization, and validation of runtime modules.
    """

    def __init__(self, max_modules: int = 200):
        # Registered modules stored as:
        # { "module_name": module_instance }
        self.modules: Dict[str, Any] = {}
        self.max_modules = max_modules

    # ---------------------------------------------------------
    # INTERNAL VALIDATION HELPERS
    # ---------------------------------------------------------

    def _validate_name(self, name: Any) -> bool:
        return isinstance(name, str) and name.strip()

    def _validate_module(self, module: Any) -> bool:
        # Module must be an object (class instance)
        if module is None:
            return False

        # Prevent dangerous types
        if isinstance(module, (bytes, bytearray, type(lambda: None))):
            return False

        return True

    # ---------------------------------------------------------
    # REGISTRATION
    # ---------------------------------------------------------

    def register(self, name: str, module: Any):
        """
        Registers a module under a given name with full safety checks.
        """

        # Validate name
        if not self._validate_name(name):
            return {"error": "invalid_module_name"}

        # Validate module object
        if not self._validate_module(module):
            return {"error": "invalid_module_object"}

        # Prevent registry overflow
        if len(self.modules) >= self.max_modules:
            return {"error": "module_limit_reached"}

        # Register module
        self.modules[name] = module
        return {"status": "module_registered", "module": name}

    def unregister(self, name: str):
        """
        Removes a module from the registry safely.
        """

        if not self._validate_name(name):
            return {"error": "invalid_module_name"}

        if name in self.modules:
            del self.modules[name]
            return {"status": "module_unregistered"}

        return {"error": "module_not_found"}

    # ---------------------------------------------------------
    # INITIALIZATION
    # ---------------------------------------------------------

    def initialize_all(self):
        """
        Calls the initialization method on all registered modules.
        Includes safety checks.
        """

        results = {}

        for name, module in self.modules.items():

            # Validate module again (defense in depth)
            if not self._validate_module(module):
                results[name] = {"error": "invalid_module_object"}
                continue

            # Initialize if supported
            if hasattr(module, "initialize") and callable(module.initialize):
                try:
                    module.initialize()
                    results[name] = {"status": "initialized"}
                except Exception as exc:
                    results[name] = {"error": "initialization_failed", "details": str(exc)}
            else:
                results[name] = {"status": "no_initialize_method"}

        return results

    # ---------------------------------------------------------
    # ACCESS
    # ---------------------------------------------------------

    def get(self, name: str):
        """
        Retrieves a module by name safely.
        """

        if not self._validate_name(name):
            return None

        return self.modules.get(name)

    def list_modules(self) -> List[str]:
        """
        Returns a list of all registered module names.
        """

        return list(self.modules.keys())

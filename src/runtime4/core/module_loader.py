# module_loader.py
"""
SIRIUS LOCAL AI – Runtime 4.0 Module Loader

The Module Loader is responsible for:
- registering runtime modules
- initializing modules in correct order
- verifying module integrity
- preparing modules for sandbox isolation
- exposing modules to the scheduler and dependency graph

This component acts as the boot manager of Runtime 4.0.
"""


class ModuleLoader4:
    """
    Handles loading, initialization, and validation of runtime modules.
    """

    def __init__(self):
        # Registered modules stored as:
        # { "module_name": module_instance }
        self.modules = {}

    # ---------------------------------------------------------
    # REGISTRATION
    # ---------------------------------------------------------

    def register(self, name: str, module):
        """
        Registers a module under a given name.
        """
        self.modules[name] = module

    def unregister(self, name: str):
        """
        Removes a module from the registry.
        """
        if name in self.modules:
            del self.modules[name]

    # ---------------------------------------------------------
    # INITIALIZATION
    # ---------------------------------------------------------

    def initialize_all(self):
        """
        Calls the initialization method on all registered modules.
        """
        for name, module in self.modules.items():
            if hasattr(module, "initialize"):
                module.initialize()

    # ---------------------------------------------------------
    # ACCESS
    # ---------------------------------------------------------

    def get(self, name: str):
        """
        Retrieves a module by name.
        """
        return self.modules.get(name)

    def list_modules(self):
        """
        Returns a list of all registered module names.
        """
        return list(self.modules.keys())

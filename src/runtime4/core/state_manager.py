# state_manager.py
"""
SIRIUS LOCAL AI – Runtime 4.0 State Manager

The State Manager is responsible for:
- storing runtime state
- managing safe-mode flags
- persisting session context
- providing state access to all subsystems
- ensuring deterministic and recoverable execution

This is the central state container for Runtime 4.0.
"""


class StateManager4:
    """
    Handles global and module-specific runtime state.
    """

    def __init__(self):
        # Global runtime flags
        self.flags = {
            "safe_mode": False,
            "schoolwork_priority": True,
            "diagnostics_enabled": True
        }

        # Persistent runtime state
        self.global_state = {}

        # Module-specific state:
        # { "module_name": { ... } }
        self.module_state = {}

    # ---------------------------------------------------------
    # FLAG MANAGEMENT
    # ---------------------------------------------------------

    def set_flag(self, name: str, value: bool):
        """Sets a runtime flag."""
        self.flags[name] = value

    def get_flag(self, name: str) -> bool:
        """Retrieves a runtime flag."""
        return self.flags.get(name, False)

    # ---------------------------------------------------------
    # GLOBAL STATE
    # ---------------------------------------------------------

    def set_global(self, key: str, value):
        """Stores a global state value."""
        self.global_state[key] = value

    def get_global(self, key: str):
        """Retrieves a global state value."""
        return self.global_state.get(key)

    # ---------------------------------------------------------
    # MODULE STATE
    # ---------------------------------------------------------

    def set_module_state(self, module_name: str, key: str, value):
        """Stores state for a specific module."""
        if module_name not in self.module_state:
            self.module_state[module_name] = {}
        self.module_state[module_name][key] = value

    def get_module_state(self, module_name: str, key: str):
        """Retrieves state for a specific module."""
        if module_name not in self.module_state:
            return None
        return self.module_state[module_name].get(key)

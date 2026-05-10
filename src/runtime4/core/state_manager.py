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

from typing import Any, Dict


class StateManager4:
    """
    Handles global and module-specific runtime state.
    """

    def __init__(self):
        # Global runtime flags
        self.flags: Dict[str, bool] = {
            "safe_mode": False,
            "schoolwork_priority": True,
            "diagnostics_enabled": True
        }

        # Persistent runtime state
        self.global_state: Dict[str, Any] = {}

        # Module-specific state:
        # { "module_name": { ... } }
        self.module_state: Dict[str, Dict[str, Any]] = {}

    # ---------------------------------------------------------
    # INTERNAL VALIDATION HELPERS
    # ---------------------------------------------------------

    def _validate_flag_name(self, name: str) -> bool:
        return isinstance(name, str) and name.strip()

    def _validate_module_name(self, name: str) -> bool:
        return isinstance(name, str) and name.strip()

    def _validate_key(self, key: str) -> bool:
        return isinstance(key, str) and key.strip()

    # ---------------------------------------------------------
    # FLAG MANAGEMENT
    # ---------------------------------------------------------

    def set_flag(self, name: str, value: bool):
        """Sets a runtime flag with safety checks."""

        if not self._validate_flag_name(name):
            return {"error": "invalid_flag_name"}

        if not isinstance(value, bool):
            return {"error": "invalid_flag_value"}

        self.flags[name] = value
        return {"status": "flag_set"}

    def get_flag(self, name: str) -> Any:
        """Retrieves a runtime flag safely."""
        if not self._validate_flag_name(name):
            return None
        return self.flags.get(name, None)

    # ---------------------------------------------------------
    # GLOBAL STATE
    # ---------------------------------------------------------

    def set_global(self, key: str, value: Any):
        """Stores a global state value with safety checks."""

        if not self._validate_key(key):
            return {"error": "invalid_global_key"}

        # Prevent storing dangerous types
        if isinstance(value, (bytes, bytearray, type(lambda: None))):
            return {"error": "unsafe_value_type"}

        self.global_state[key] = value
        return {"status": "global_state_set"}

    def get_global(self, key: str):
        """Retrieves a global state value safely."""
        if not self._validate_key(key):
            return None
        return self.global_state.get(key)

    # ---------------------------------------------------------
    # MODULE STATE
    # ---------------------------------------------------------

    def set_module_state(self, module_name: str, key: str, value: Any):
        """Stores state for a specific module with safety checks."""

        if not self._validate_module_name(module_name):
            return {"error": "invalid_module_name"}

        if not self._validate_key(key):
            return {"error": "invalid_state_key"}

        # Prevent storing dangerous types
        if isinstance(value, (bytes, bytearray, type(lambda: None))):
            return {"error": "unsafe_value_type"}

        if module_name not in self.module_state:
            self.module_state[module_name] = {}

        self.module_state[module_name][key] = value
        return {"status": "module_state_set"}

    def get_module_state(self, module_name: str, key: str):
        """Retrieves state for a specific module safely."""

        if not self._validate_module_name(module_name):
            return None

        if not self._validate_key(key):
            return None

        module = self.module_state.get(module_name)
        if not module:
            return None

        return module.get(key)

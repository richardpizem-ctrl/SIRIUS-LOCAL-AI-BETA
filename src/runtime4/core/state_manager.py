"""
SIRIUS LOCAL AI – Runtime 4.4 State Manager

Responsible for:
- storing runtime state
- managing safe-mode flags
- persisting session context
- providing state access to all subsystems
- ensuring deterministic and recoverable execution
- degraded‑mode detection
- Self‑Repair 4.4 diagnostics

This is the central state container for Runtime 4.4.
"""

from typing import Any, Dict, Optional


class StateManager4:
    """
    Handles global and module-specific runtime state.
    Provides:
    - strict validation
    - structured error surface
    - safe-mode compatibility
    - degraded-mode detection
    - Self‑Repair snapshot support
    - deterministic, audit‑friendly behavior
    """

    def __init__(self):
        # Global runtime flags
        self.flags: Dict[str, bool] = {
            "safe_mode": False,
            "schoolwork_priority": True,
            "diagnostics_enabled": True,
        }

        # Persistent runtime state
        self.global_state: Dict[str, Any] = {}

        # Module-specific state:
        # { "module_name": { ... } }
        self.module_state: Dict[str, Dict[str, Any]] = {}

        self.degraded_mode = False

    # ---------------------------------------------------------
    # VALIDATION HELPERS
    # ---------------------------------------------------------

    def _validate_flag_name(self, name: str) -> bool:
        return isinstance(name, str) and name.strip()

    def _validate_module_name(self, name: str) -> bool:
        return isinstance(name, str) and name.strip()

    def _validate_key(self, key: str) -> bool:
        return isinstance(key, str) and key.strip()

    def _validate_value(self, value: Any) -> bool:
        # Prevent storing dangerous types
        return not isinstance(value, (bytes, bytearray, type(lambda: None)))

    # ---------------------------------------------------------
    # FLAG MANAGEMENT
    # ---------------------------------------------------------

    def set_flag(self, name: str, value: bool) -> Dict[str, Any]:
        if not self._validate_flag_name(name):
            return {"status": "error", "code": "invalid_flag_name"}

        if not isinstance(value, bool):
            return {"status": "error", "code": "invalid_flag_value"}

        self.flags[name] = value
        return {"status": "success", "flag": name, "value": value}

    def get_flag(self, name: str) -> Optional[bool]:
        if not self._validate_flag_name(name):
            return None
        return self.flags.get(name)

    # ---------------------------------------------------------
    # GLOBAL STATE
    # ---------------------------------------------------------

    def set_global(self, key: str, value: Any) -> Dict[str, Any]:
        if not self._validate_key(key):
            return {"status": "error", "code": "invalid_global_key"}

        if not self._validate_value(value):
            return {"status": "error", "code": "unsafe_value_type"}

        try:
            self.global_state[key] = value
            return {"status": "success", "key": key}
        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "global_state_set_failed",
                "exception": str(exc),
            }

    def get_global(self, key: str) -> Any:
        if not self._validate_key(key):
            return None
        return self.global_state.get(key)

    # ---------------------------------------------------------
    # MODULE STATE
    # ---------------------------------------------------------

    def set_module_state(
        self,
        module_name: str,
        key: str,
        value: Any,
    ) -> Dict[str, Any]:
        if not self._validate_module_name(module_name):
            return {"status": "error", "code": "invalid_module_name"}

        if not self._validate_key(key):
            return {"status": "error", "code": "invalid_state_key"}

        if not self._validate_value(value):
            return {"status": "error", "code": "unsafe_value_type"}

        try:
            if module_name not in self.module_state:
                self.module_state[module_name] = {}

            self.module_state[module_name][key] = value
            return {"status": "success", "module": module_name, "key": key}

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "module_state_set_failed",
                "exception": str(exc),
            }

    def get_module_state(self, module_name: str, key: str) -> Any:
        if not self._validate_module_name(module_name):
            return None
        if not self._validate_key(key):
            return None

        module = self.module_state.get(module_name)
        if not module:
            return None

        return module.get(key)

    # ---------------------------------------------------------
    # SNAPSHOT (Self‑Repair 4.4)
    # ---------------------------------------------------------

    def snapshot(self) -> Dict[str, Any]:
        """
        Returns a safe snapshot of all runtime state.
        Used by RuntimeEngine 4.4 and Self‑Repair 4.4.
        """

        try:
            return {
                "status": "success",
                "flags": dict(self.flags),
                "global_state": dict(self.global_state),
                "module_state": {k: dict(v) for k, v in self.module_state.items()},
                "degraded_mode": self.degraded_mode,
            }
        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "snapshot_failed",
                "exception": str(exc),
            }

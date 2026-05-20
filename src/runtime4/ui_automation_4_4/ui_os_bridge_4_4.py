"""
SIRIUS LOCAL AI – UI Automation OS Bridge 4.4.0 (PRO)

Deterministic OS‑level bridge for UI Automation Engine 4.4.

Responsibilities:
- Win32 / UIA / WinRT abstraction (via capability adapter)
- Safe window enumeration
- Safe UI element querying
- Safe action dispatching (sandbox‑routed)
- Deterministic, offline‑safe behavior

Security Notes:
- Only static imports allowed.
- No dynamic loading, no eval, no reflection.
- All OS calls must go through verified capability wrappers.
- Fully compatible with Security Family 4.4.
"""

from typing import Optional, Dict, Any


class UIOSBridge44:
    """
    Deterministic OS‑level UI bridge for Runtime 4.4 (PRO).
    """

    REQUIRED_CAPABILITY_METHODS = {"initialize", "get_windows", "find_element"}
    REQUIRED_SANDBOX_METHODS = {"initialize", "execute_ui_action"}

    def __init__(self, capability_adapter=None, sandbox=None):
        self.capability_adapter = capability_adapter
        self.sandbox = sandbox

        self.initialized: bool = False
        self.safe_mode: bool = False
        self.degraded_mode: bool = False

    # ---------------------------------------------------------------------
    # INITIALIZATION
    # ---------------------------------------------------------------------
    def initialize(self) -> Dict[str, Any]:
        if self.initialized:
            return {"status": "already_initialized"}

        # Validate capability adapter
        if not self.capability_adapter:
            self.degraded_mode = True
            return {"status": "error", "code": "no_capability_adapter"}

        for method in self.REQUIRED_CAPABILITY_METHODS:
            if not hasattr(self.capability_adapter, method):
                self.degraded_mode = True
                return {
                    "status": "error",
                    "code": "invalid_capability_adapter_interface",
                    "missing": method,
                }

        # Validate sandbox
        if not self.sandbox:
            self.degraded_mode = True
            return {"status": "error", "code": "no_sandbox"}

        for method in self.REQUIRED_SANDBOX_METHODS:
            if not hasattr(self.sandbox, method):
                self.degraded_mode = True
                return {
                    "status": "error",
                    "code": "invalid_sandbox_interface",
                    "missing": method,
                }

        try:
            cap_res = self.capability_adapter.initialize()
            if cap_res.get("status") not in ("initialized", "already_initialized"):
                self.degraded_mode = True
                return {
                    "status": "error",
                    "code": "capability_init_failed",
                    "details": cap_res,
                }

            sb_res = self.sandbox.initialize()
            if sb_res.get("status") not in ("initialized", "already_initialized"):
                self.degraded_mode = True
                return {
                    "status": "error",
                    "code": "sandbox_init_failed",
                    "details": sb_res,
                }

            self.initialized = True
            return {"status": "initialized"}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "code": "exception", "exception": str(exc)}

    # ---------------------------------------------------------------------
    # WINDOW ENUMERATION (SAFE)
    # ---------------------------------------------------------------------
    def list_windows(self) -> Dict[str, Any]:
        if self.safe_mode:
            return {
                "status": "safe_mode",
                "windows": [],
                "degraded_mode": self.degraded_mode,
            }

        if not self.initialized:
            init = self.initialize()
            if init.get("status") not in ("initialized", "already_initialized"):
                return {
                    "status": "error",
                    "code": "bridge_not_initialized",
                    "details": init,
                }

        try:
            windows = self.capability_adapter.get_windows()
            return {
                "status": "ok",
                "windows": windows,
                "degraded_mode": self.degraded_mode,
            }
        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "code": "exception", "exception": str(exc)}

    # ---------------------------------------------------------------------
    # UIA ELEMENT QUERY (SAFE)
    # ---------------------------------------------------------------------
    def query_element(self, query: Dict[str, Any]) -> Dict[str, Any]:
        if self.safe_mode:
            return {
                "status": "safe_mode",
                "element": None,
                "degraded_mode": self.degraded_mode,
            }

        if not isinstance(query, dict):
            return {"status": "error", "code": "invalid_query"}

        if not self.initialized:
            init = self.initialize()
            if init.get("status") not in ("initialized", "already_initialized"):
                return {
                    "status": "error",
                    "code": "bridge_not_initialized",
                    "details": init,
                }

        try:
            result = self.capability_adapter.find_element(query)
            return {
                "status": "ok",
                "element": result,
                "degraded_mode": self.degraded_mode,
            }
        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "code": "exception", "exception": str(exc)}

    # ---------------------------------------------------------------------
    # SAFE ACTION DISPATCH (SANDBOX‑ROUTED)
    # ---------------------------------------------------------------------
    def dispatch_action(
        self,
        element_ref: Dict[str, Any],
        action: str,
        payload: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        if self.safe_mode:
            return {
                "status": "safe_mode",
                "action": action,
                "element": element_ref,
                "degraded_mode": self.degraded_mode,
            }

        if not isinstance(element_ref, dict) or not isinstance(action, str):
            return {"status": "error", "code": "invalid_arguments"}

        if not self.initialized:
            init = self.initialize()
            if init.get("status") not in ("initialized", "already_initialized"):
                return {
                    "status": "error",
                    "code": "bridge_not_initialized",
                    "details": init,
                }

        try:
            result = self.sandbox.execute_ui_action(
                element_ref=element_ref,
                action=action,
                payload=payload or {},
            )
            return {
                "status": "ok",
                "result": result,
                "degraded_mode": self.degraded_mode,
            }
        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "exception",
                "exception": str(exc),
            }

"""
SIRIUS LOCAL AI – Home Device Diagnostics 4.5.0

Účel:
- deterministická diagnostika domácich zariadení
- 100 % offline, žiadne AI heuristiky, žiadne dynamické importy
- integrácia s:
    - Household Device Registry 4.5
    - Household State Manager 4.5
    - Event Bus 4.5

Security Family 4.5:
- žiadne nebezpečné typy
- deterministické správanie
- Self‑Repair 4.5 ready
"""

from typing import Dict, Any, List, Optional


class HomeDeviceDiagnostics45:
    """
    Deterministic diagnostics modul pre domácnosť 4.5.
    """

    def __init__(self, device_registry=None, state_manager=None, event_bus=None):
        self.initialized = False
        self.degraded_mode = False
        self.safe_mode = False

        self.device_registry = device_registry
        self.state_manager = state_manager
        self.event_bus = event_bus

        self.valid_types = ["light", "socket", "sensor", "door", "appliance"]

    # ---------------------------------------------------------
    # INTERNAL VALIDATION
    # ---------------------------------------------------------
    def _validate_str(self, value: Any) -> bool:
        return isinstance(value, str) and value.strip()

    # ---------------------------------------------------------
    # INITIALIZATION
    # ---------------------------------------------------------
    def initialize(self) -> Dict[str, Any]:
        if self.initialized:
            return {"status": "already_initialized", "version": "4.5"}

        try:
            modules = [self.device_registry, self.state_manager, self.event_bus]
            for m in modules:
                if m:
                    res = m.initialize()
                    if isinstance(res, dict) and res.get("status") == "error":
                        self.degraded_mode = True
                        return {
                            "status": "error",
                            "code": "module_init_failed",
                            "version": "4.5",
                        }

            self.initialized = True
            return {"status": "initialized", "version": "4.5"}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "exception": str(exc), "version": "4.5"}

    # ---------------------------------------------------------
    # RUN FULL DIAGNOSTICS
    # ---------------------------------------------------------
    def run_diagnostics(self) -> Dict[str, Any]:
        if self.safe_mode:
            return {
                "status": "safe_mode",
                "message": "Diagnostics disabled in safe-mode.",
                "version": "4.5",
            }

        try:
            devices = self.device_registry.list_devices().get("devices", [])
            results = []

            for dev in devices:
                results.append(self._diagnose_device(dev))

            return {
                "status": "ok",
                "devices_checked": len(devices),
                "results": results,
                "version": "4.5",
            }

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "diagnostics_failed",
                "exception": str(exc),
                "version": "4.5",
            }

    # ---------------------------------------------------------
    # DIAGNOSE SINGLE DEVICE
    # ---------------------------------------------------------
    def _diagnose_device(self, device: Dict[str, Any]) -> Dict[str, Any]:
        device_id = device.get("id")
        device_type = device.get("type")
        room = device.get("room")

        result = {
            "device_id": device_id,
            "type": device_type,
            "room": room,
            "issues": [],
        }

        # 1. Validate ID
        if not self._validate_str(device_id):
            result["issues"].append("invalid_device_id")
            return result

        # 2. Unknown type
        if device_type not in self.valid_types:
            result["issues"].append("unknown_device_type")

        # 3. Get state
        state = self.state_manager.get_state(device_id)
        if state.get("status") != "ok":
            result["issues"].append("state_unavailable")
            return result

        value = state.get("value")

        # 4. Type-specific checks
        if device_type == "light":
            if value not in ["on", "off"]:
                result["issues"].append("invalid_light_state")

        elif device_type == "socket":
            if value not in ["on", "off"]:
                result["issues"].append("invalid_socket_state")

        elif device_type == "sensor":
            if not isinstance(value, dict):
                result["issues"].append("invalid_sensor_payload")

        elif device_type == "door":
            if value not in ["open", "closed"]:
                result["issues"].append("invalid_door_state")

        elif device_type == "appliance":
            if not isinstance(value, dict):
                result["issues"].append("invalid_appliance_state")

        # 5. Non-responsive simulation
        if value in (None, "unknown"):
            result["issues"].append("device_not_responding")

        # Emit event if issues found
        if result["issues"] and self.event_bus:
            try:
                self.event_bus.emit("device_issue_detected", result)
            except Exception:
                self.degraded_mode = True

        return result

    # ---------------------------------------------------------
    # DIAGNOSE ONE DEVICE BY ID
    # ---------------------------------------------------------
    def diagnose(self, device_id: str) -> Dict[str, Any]:
        if not self._validate_str(device_id):
            return {"status": "error", "code": "invalid_device_id", "version": "4.5"}

        device = self.device_registry.get_device(device_id)
        if device.get("status") != "ok":
            return {"status": "error", "code": "device_not_found", "version": "4.5"}

        try:
            return {
                "status": "ok",
                "result": self._diagnose_device(device["device"]),
                "version": "4.5",
            }
        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "diagnose_failed",
                "exception": str(exc),
                "version": "4.5",
            }

    # ---------------------------------------------------------
    # STATUS
    # ---------------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "status": "ok",
            "initialized": self.initialized,
            "safe_mode": self.safe_mode,
            "degraded_mode": self.degraded_mode,
            "version": "4.5",
        }

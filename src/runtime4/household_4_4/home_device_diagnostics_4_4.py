# household_4_4/home_device_diagnostics_4_4.py
"""
SIRIUS LOCAL AI – Home Device Diagnostics 4.4.0

Účel:
- diagnostika domácich zariadení (svetlá, zásuvky, senzory, dvere, spotrebiče)
- 100 % offline, deterministické
- žiadne AI heuristiky, žiadne dynamické importy
- integrácia s:
    - Household Device Registry 4.4
    - Household State Manager 4.4
    - Event Bus 4.4

Diagnostika je čistá logika:
- chýbajúce zariadenie
- neznámy typ
- neplatný stav
- konfliktný stav
- zariadenie nereaguje (simulované)
"""

from typing import Dict, Any, List, Optional


class HomeDeviceDiagnostics44:
    """
    Deterministic diagnostics modul pre domácnosť.
    """

    def __init__(self, device_registry=None, state_manager=None, event_bus=None):
        self.initialized = False
        self.degraded_mode = False

        self.device_registry = device_registry
        self.state_manager = state_manager
        self.event_bus = event_bus

    # ------------------------------------------------------------------
    # INITIALIZATION
    # ------------------------------------------------------------------
    def initialize(self) -> Dict[str, Any]:
        if self.initialized:
            return {"status": "already_initialized"}

        try:
            if self.device_registry:
                self.device_registry.initialize()
            if self.state_manager:
                self.state_manager.initialize()
            if self.event_bus:
                self.event_bus.initialize()

            self.initialized = True
            return {"status": "initialized"}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "exception": str(exc)}

    # ------------------------------------------------------------------
    # RUN FULL DIAGNOSTICS
    # ------------------------------------------------------------------
    def run_diagnostics(self) -> Dict[str, Any]:
        """
        Spustí kompletnú diagnostiku všetkých zariadení.
        """

        try:
            devices = self.device_registry.list_devices().get("devices", [])
            results = []

            for dev in devices:
                results.append(self._diagnose_device(dev))

            return {
                "status": "ok",
                "devices_checked": len(devices),
                "results": results,
            }

        except Exception as exc:
            return {"status": "error", "exception": str(exc)}

    # ------------------------------------------------------------------
    # DIAGNOSE SINGLE DEVICE
    # ------------------------------------------------------------------
    def _diagnose_device(self, device: Dict[str, Any]) -> Dict[str, Any]:
        device_id = device.get("id")
        device_type = device.get("type")
        room = device.get("room")

        state = self.state_manager.get_state(device_id)

        result = {
            "device_id": device_id,
            "type": device_type,
            "room": room,
            "issues": [],
        }

        # 1. Unknown type
        if device_type not in ["light", "socket", "sensor", "door", "appliance"]:
            result["issues"].append("unknown_device_type")

        # 2. Missing state
        if state.get("status") != "ok":
            result["issues"].append("state_unavailable")
            return result

        value = state.get("value")

        # 3. Type-specific checks
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

        # 4. Simulated "non-responsive" check
        if value == "unknown" or value is None:
            result["issues"].append("device_not_responding")

        # Emit event if issues found
        if result["issues"] and self.event_bus:
            self.event_bus.emit("device_issue_detected", result)

        return result

    # ------------------------------------------------------------------
    # DIAGNOSE ONE DEVICE BY ID
    # ------------------------------------------------------------------
    def diagnose(self, device_id: str) -> Dict[str, Any]:
        device = self.device_registry.get_device(device_id)
        if device.get("status") != "ok":
            return {"status": "error", "reason": "device_not_found"}

        return {
            "status": "ok",
            "result": self._diagnose_device(device["device"]),
        }

    # ------------------------------------------------------------------
    # STATUS
    # ------------------------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "status": "ok",
            "initialized": self.initialized,
            "degraded_mode": self.degraded_mode,
        }

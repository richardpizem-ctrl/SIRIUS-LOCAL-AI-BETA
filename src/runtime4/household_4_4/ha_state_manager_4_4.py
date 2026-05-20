"""
SIRIUS LOCAL AI – Household State Manager 4.4.0

Účel:
- drží aktuálne stavy všetkých zariadení v domácnosti
- poskytuje API na čítanie a zmenu stavu
- podporuje hromadné operácie (napr. vypnúť všetky svetlá v miestnosti)
- 100 % offline, deterministické
- žiadne AI heuristiky, žiadne dynamické importy

Security Family 4.4:
- žiadne nebezpečné typy
- deterministické správanie
- Self‑Repair 4.4 ready
"""

from typing import Dict, Any, List, Optional


class HouseholdStateManager44:
    """
    Deterministic state manager pre domácnosť.
    """

    def __init__(self, device_registry=None, event_bus=None):
        self.initialized = False
        self.degraded_mode = False
        self.safe_mode = False

        self.device_registry = device_registry
        self.event_bus = event_bus

        # device_id → value
        self.states: Dict[str, Any] = {}

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
            return {"status": "already_initialized"}

        try:
            if self.device_registry:
                res = self.device_registry.initialize()
                if isinstance(res, dict) and res.get("status") == "error":
                    self.degraded_mode = True
                    return {"status": "error", "code": "device_registry_init_failed"}

            if self.event_bus:
                res = self.event_bus.initialize()
                if isinstance(res, dict) and res.get("status") == "error":
                    self.degraded_mode = True
                    return {"status": "error", "code": "event_bus_init_failed"}

            # Inicializácia stavov pre všetky zariadenia
            devices = self.device_registry.list_devices().get("devices", [])
            for d in devices:
                device_id = d.get("id")
                device_type = d.get("type")

                if not self._validate_str(device_id):
                    continue

                self.states[device_id] = self._default_state_for_type(device_type)

            self.initialized = True
            return {"status": "initialized", "degraded_mode": self.degraded_mode}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "exception": str(exc)}

    # ---------------------------------------------------------
    # DEFAULT STATE
    # ---------------------------------------------------------
    def _default_state_for_type(self, device_type: str):
        if device_type == "light":
            return "off"
        if device_type == "socket":
            return "off"
        if device_type == "door":
            return "closed"
        if device_type == "sensor":
            return {}
        if device_type == "appliance":
            return {"status": "off"}
        return None

    # ---------------------------------------------------------
    # GET STATE
    # ---------------------------------------------------------
    def get_state(self, device_id: str) -> Dict[str, Any]:
        if not self._validate_str(device_id):
            return {"status": "error", "code": "invalid_device_id"}

        if device_id not in self.states:
            return {"status": "error", "code": "device_not_found"}

        return {"status": "ok", "value": self.states[device_id]}

    # ---------------------------------------------------------
    # SET STATE (single device)
    # ---------------------------------------------------------
    def set_state(self, device_id: str, action: str, value: Any = None) -> Dict[str, Any]:
        if not self._validate_str(device_id):
            return {"status": "error", "code": "invalid_device_id"}

        if device_id not in self.states:
            return {"status": "error", "code": "device_not_found"}

        if not self._validate_str(action):
            return {"status": "error", "code": "invalid_action"}

        current = self.states[device_id]

        try:
            # Jednoduché deterministické mapovanie akcií
            if action in ["on", "off", "open", "close"]:
                self.states[device_id] = action
            elif action == "set":
                self.states[device_id] = value
            else:
                return {"status": "error", "code": "invalid_action"}

            # Event
            if self.event_bus:
                self.event_bus.emit("device_state_changed", {
                    "device_id": device_id,
                    "old": current,
                    "new": self.states[device_id],
                })

            return {"status": "ok", "new_state": self.states[device_id]}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "code": "state_update_failed", "exception": str(exc)}

    # ---------------------------------------------------------
    # SET STATE FOR ROOM (bulk)
    # ---------------------------------------------------------
    def set_state_for_room(self, room: str, action: str, value: Any = None) -> Dict[str, Any]:
        if not self._validate_str(room):
            return {"status": "error", "code": "invalid_room"}

        if not self.device_registry:
            return {"status": "error", "code": "no_device_registry"}

        try:
            devices = self.device_registry.list_devices_in_room(room).get("devices", [])
            results = []

            for d in devices:
                res = self.set_state(d["id"], action, value)
                results.append({"device_id": d["id"], "result": res})

            return {
                "status": "ok",
                "room": room,
                "affected_devices": len(devices),
                "results": results,
            }

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "code": "bulk_update_failed", "exception": str(exc)}

    # ---------------------------------------------------------
    # UPDATE SENSOR VALUE
    # ---------------------------------------------------------
    def update_sensor(self, device_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        if not self._validate_str(device_id):
            return {"status": "error", "code": "invalid_device_id"}

        if device_id not in self.states:
            return {"status": "error", "code": "device_not_found"}

        if not isinstance(self.states[device_id], dict):
            return {"status": "error", "code": "not_a_sensor"}

        if not isinstance(payload, dict):
            return {"status": "error", "code": "invalid_sensor_payload"}

        try:
            old = self.states[device_id]
            self.states[device_id] = payload

            if self.event_bus:
                self.event_bus.emit("sensor_updated", {
                    "device_id": device_id,
                    "old": old,
                    "new": payload,
                })

            return {"status": "ok"}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "code": "sensor_update_failed", "exception": str(exc)}

    # ---------------------------------------------------------
    # STATUS
    # ---------------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "status": "ok",
            "initialized": self.initialized,
            "safe_mode": self.safe_mode,
            "degraded_mode": self.degraded_mode,
            "tracked_devices": len(self.states),
        }

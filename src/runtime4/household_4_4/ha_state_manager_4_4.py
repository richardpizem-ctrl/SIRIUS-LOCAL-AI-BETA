# household_4_4/ha_state_manager_4_4.py
"""
SIRIUS LOCAL AI – Household State Manager 4.4.0

Účel:
- drží aktuálne stavy všetkých zariadení v domácnosti
- poskytuje API na čítanie a zmenu stavu
- podporuje hromadné operácie (napr. vypnúť všetky svetlá v miestnosti)
- 100 % offline, deterministické
- žiadne AI heuristiky, žiadne dynamické importy

Stav zariadenia:
{
    "device_id": "dev_001",
    "value": "on" | "off" | "open" | "closed" | dict (senzory, spotrebiče)
}
"""

from typing import Dict, Any, List, Optional


class HouseholdStateManager44:
    """
    Deterministic state manager pre domácnosť.
    """

    def __init__(self, device_registry=None, event_bus=None):
        self.initialized = False
        self.degraded_mode = False

        self.device_registry = device_registry
        self.event_bus = event_bus

        # device_id → value
        self.states: Dict[str, Any] = {}

    # ------------------------------------------------------------------
    # INITIALIZATION
    # ------------------------------------------------------------------
    def initialize(self) -> Dict[str, Any]:
        if self.initialized:
            return {"status": "already_initialized"}

        try:
            if self.device_registry:
                self.device_registry.initialize()
            if self.event_bus:
                self.event_bus.initialize()

            # Inicializácia stavov pre všetky zariadenia
            devices = self.device_registry.list_devices().get("devices", [])
            for d in devices:
                self.states[d["id"]] = self._default_state_for_type(d["type"])

            self.initialized = True
            return {"status": "initialized"}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "exception": str(exc)}

    # ------------------------------------------------------------------
    # DEFAULT STATE
    # ------------------------------------------------------------------
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

    # ------------------------------------------------------------------
    # GET STATE
    # ------------------------------------------------------------------
    def get_state(self, device_id: str) -> Dict[str, Any]:
        if device_id not in self.states:
            return {"status": "error", "reason": "device_not_found"}

        return {"status": "ok", "value": self.states[device_id]}

    # ------------------------------------------------------------------
    # SET STATE (single device)
    # ------------------------------------------------------------------
    def set_state(self, device_id: str, action: str, value: Any = None) -> Dict[str, Any]:
        if device_id not in self.states:
            return {"status": "error", "reason": "device_not_found"}

        current = self.states[device_id]

        # Jednoduché deterministické mapovanie akcií
        if action in ["on", "off", "open", "close"]:
            self.states[device_id] = action
        elif action == "set":
            self.states[device_id] = value
        else:
            return {"status": "error", "reason": "invalid_action"}

        # Event
        if self.event_bus:
            self.event_bus.emit("device_state_changed", {
                "device_id": device_id,
                "old": current,
                "new": self.states[device_id],
            })

        return {"status": "ok", "new_state": self.states[device_id]}

    # ------------------------------------------------------------------
    # SET STATE FOR ROOM (bulk)
    # ------------------------------------------------------------------
    def set_state_for_room(self, room: str, action: str, value: Any = None) -> Dict[str, Any]:
        if not self.device_registry:
            return {"status": "error", "reason": "no_device_registry"}

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

    # ------------------------------------------------------------------
    # UPDATE SENSOR VALUE
    # ------------------------------------------------------------------
    def update_sensor(self, device_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        if device_id not in self.states:
            return {"status": "error", "reason": "device_not_found"}

        if not isinstance(self.states[device_id], dict):
            return {"status": "error", "reason": "not_a_sensor"}

        old = self.states[device_id]
        self.states[device_id] = payload

        if self.event_bus:
            self.event_bus.emit("sensor_updated", {
                "device_id": device_id,
                "old": old,
                "new": payload,
            })

        return {"status": "ok"}

    # ------------------------------------------------------------------
    # STATUS
    # ------------------------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "status": "ok",
            "initialized": self.initialized,
            "degraded_mode": self.degraded_mode,
            "tracked_devices": len(self.states),
        }

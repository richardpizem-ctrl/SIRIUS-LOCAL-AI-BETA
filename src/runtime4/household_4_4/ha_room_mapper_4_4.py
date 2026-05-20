"""
SIRIUS LOCAL AI – Household Room Mapper 4.4.0

Účel:
- mapuje zariadenia do miestností
- poskytuje rýchle dotazy typu:
    - "aké zariadenia sú v kuchyni?"
    - "vypni všetky svetlá v obývačke"
- 100 % offline, deterministické
- žiadne AI heuristiky, žiadne dynamické importy

Interná štruktúra:
room_map = {
    "kitchen": ["dev_001", "dev_002"],
    "living_room": ["dev_010"]
}

Security Family 4.4:
- žiadne nebezpečné typy
- deterministické správanie
- Self‑Repair 4.4 ready
"""

from typing import Dict, Any, List, Optional


class HouseholdRoomMapper44:
    """
    Deterministic room mapper pre domácnosť.
    """

    def __init__(self, device_registry=None):
        self.initialized = False
        self.degraded_mode = False
        self.safe_mode = False

        self.device_registry = device_registry

        # room → [device_ids]
        self.room_map: Dict[str, List[str]] = {}

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
                init = self.device_registry.initialize()
                if isinstance(init, dict) and init.get("status") == "error":
                    self.degraded_mode = True
                    return {"status": "error", "code": "device_registry_init_failed"}

            # Rebuild map from registry
            rebuild = self.rebuild()
            if rebuild.get("status") != "ok":
                self.degraded_mode = True
                return {"status": "error", "code": "rebuild_failed"}

            self.initialized = True
            return {"status": "initialized", "degraded_mode": self.degraded_mode}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "exception": str(exc)}

    # ---------------------------------------------------------
    # REGISTER DEVICE → UPDATE MAP
    # ---------------------------------------------------------
    def add_device_to_room(self, device_id: str, room: str) -> Dict[str, Any]:
        if self.safe_mode:
            return {"status": "safe_mode", "message": "Room mapper disabled in safe-mode."}

        if not self._validate_str(device_id):
            return {"status": "error", "code": "invalid_device_id"}

        if not self._validate_str(room):
            return {"status": "error", "code": "invalid_room"}

        try:
            if room not in self.room_map:
                self.room_map[room] = []

            if device_id not in self.room_map[room]:
                self.room_map[room].append(device_id)

            return {"status": "ok"}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "code": "add_device_failed", "exception": str(exc)}

    # ---------------------------------------------------------
    # REMOVE DEVICE
    # ---------------------------------------------------------
    def remove_device(self, device_id: str) -> Dict[str, Any]:
        if not self._validate_str(device_id):
            return {"status": "error", "code": "invalid_device_id"}

        try:
            for room, devices in self.room_map.items():
                if device_id in devices:
                    devices.remove(device_id)
                    return {"status": "ok"}

            return {"status": "error", "code": "device_not_found"}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "code": "remove_device_failed", "exception": str(exc)}

    # ---------------------------------------------------------
    # GET DEVICES IN ROOM
    # ---------------------------------------------------------
    def devices_in_room(self, room: str) -> Dict[str, Any]:
        if not self._validate_str(room):
            return {"status": "error", "code": "invalid_room"}

        try:
            devices = self.room_map.get(room, [])
            return {"status": "ok", "room": room, "devices": list(devices)}
        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "code": "query_failed", "exception": str(exc)}

    # ---------------------------------------------------------
    # LIST ROOMS
    # ---------------------------------------------------------
    def list_rooms(self) -> Dict[str, Any]:
        try:
            return {"status": "ok", "rooms": list(self.room_map.keys())}
        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "code": "list_rooms_failed", "exception": str(exc)}

    # ---------------------------------------------------------
    # REBUILD MAP
    # ---------------------------------------------------------
    def rebuild(self) -> Dict[str, Any]:
        if not self.device_registry:
            return {"status": "error", "code": "no_device_registry"}

        try:
            self.room_map = {}

            devices = self.device_registry.list_devices().get("devices", [])
            for d in devices:
                room = d.get("room")
                if not room:
                    continue
                if room not in self.room_map:
                    self.room_map[room] = []
                self.room_map[room].append(d["id"])

            return {"status": "ok"}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "code": "rebuild_failed", "exception": str(exc)}

    # ---------------------------------------------------------
    # STATUS
    # ---------------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "status": "ok",
            "initialized": self.initialized,
            "safe_mode": self.safe_mode,
            "degraded_mode": self.degraded_mode,
            "rooms_count": len(self.room_map),
        }

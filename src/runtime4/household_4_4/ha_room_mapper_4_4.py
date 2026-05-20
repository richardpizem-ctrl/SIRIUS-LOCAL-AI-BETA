# household_4_4/ha_room_mapper_4_4.py
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
"""

from typing import Dict, Any, List, Optional


class HouseholdRoomMapper44:
    """
    Deterministic room mapper pre domácnosť.
    """

    def __init__(self, device_registry=None):
        self.initialized = False
        self.degraded_mode = False

        self.device_registry = device_registry

        # room → [device_ids]
        self.room_map: Dict[str, List[str]] = {}

    # ------------------------------------------------------------------
    # INITIALIZATION
    # ------------------------------------------------------------------
    def initialize(self) -> Dict[str, Any]:
        if self.initialized:
            return {"status": "already_initialized"}

        try:
            if self.device_registry:
                self.device_registry.initialize()

            # Načítanie existujúcich zariadení
            devices = self.device_registry.list_devices().get("devices", [])
            for d in devices:
                room = d.get("room")
                if not room:
                    continue
                if room not in self.room_map:
                    self.room_map[room] = []
                self.room_map[room].append(d["id"])

            self.initialized = True
            return {"status": "initialized"}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "exception": str(exc)}

    # ------------------------------------------------------------------
    # REGISTER DEVICE → UPDATE MAP
    # ------------------------------------------------------------------
    def add_device_to_room(self, device_id: str, room: str) -> Dict[str, Any]:
        if room not in self.room_map:
            self.room_map[room] = []

        if device_id not in self.room_map[room]:
            self.room_map[room].append(device_id)

        return {"status": "ok"}

    # ------------------------------------------------------------------
    # REMOVE DEVICE
    # ------------------------------------------------------------------
    def remove_device(self, device_id: str) -> Dict[str, Any]:
        for room, devices in self.room_map.items():
            if device_id in devices:
                devices.remove(device_id)
                return {"status": "ok"}

        return {"status": "error", "reason": "device_not_found"}

    # ------------------------------------------------------------------
    # GET DEVICES IN ROOM
    # ------------------------------------------------------------------
    def devices_in_room(self, room: str) -> Dict[str, Any]:
        devices = self.room_map.get(room, [])
        return {"status": "ok", "room": room, "devices": list(devices)}

    # ------------------------------------------------------------------
    # GET ROOMS
    # ------------------------------------------------------------------
    def list_rooms(self) -> Dict[str, Any]:
        return {"status": "ok", "rooms": list(self.room_map.keys())}

    # ------------------------------------------------------------------
    # REBUILD MAP (napr. po zmene registrácie)
    # ------------------------------------------------------------------
    def rebuild(self) -> Dict[str, Any]:
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

    # ------------------------------------------------------------------
    # STATUS
    # ------------------------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "status": "ok",
            "initialized": self.initialized,
            "degraded_mode": self.degraded_mode,
            "rooms_count": len(self.room_map),
        }

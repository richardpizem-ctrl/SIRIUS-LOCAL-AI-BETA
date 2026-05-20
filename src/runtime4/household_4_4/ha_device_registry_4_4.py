# household_4_4/ha_device_registry_4_4.py
"""
SIRIUS LOCAL AI – Household Device Registry 4.4.0

Účel:
- eviduje všetky zariadenia v domácnosti
- poskytuje API na registráciu, získanie, zoznam a odstránenie zariadení
- 100 % offline, deterministické
- žiadne AI heuristiky, žiadne dynamické importy

Zariadenie má formát:
{
    "id": "dev_001",
    "name": "Kitchen Light",
    "type": "light",
    "room": "kitchen",
    "capabilities": ["on", "off"]
}
"""

from typing import Dict, Any, List, Optional


class HouseholdDeviceRegistry44:
    """
    Deterministic registry domácich zariadení.
    """

    def __init__(self):
        self.initialized = False
        self.degraded_mode = False

        # Zoznam zariadení
        self.devices: List[Dict[str, Any]] = []

    # ------------------------------------------------------------------
    # INITIALIZATION
    # ------------------------------------------------------------------
    def initialize(self) -> Dict[str, Any]:
        if self.initialized:
            return {"status": "already_initialized"}

        try:
            self.initialized = True
            return {"status": "initialized"}
        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "exception": str(exc)}

    # ------------------------------------------------------------------
    # REGISTER DEVICE
    # ------------------------------------------------------------------
    def register_device(
        self,
        device_id: str,
        name: str,
        device_type: str,
        room: Optional[str] = None,
        capabilities: Optional[List[str]] = None,
    ) -> Dict[str, Any]:

        # Kontrola duplicity
        for d in self.devices:
            if d["id"] == device_id:
                return {"status": "error", "reason": "device_id_exists"}

        device = {
            "id": device_id,
            "name": name,
            "type": device_type,
            "room": room,
            "capabilities": capabilities or [],
        }

        self.devices.append(device)

        return {"status": "ok", "device": device}

    # ------------------------------------------------------------------
    # GET DEVICE
    # ------------------------------------------------------------------
    def get_device(self, device_id: str) -> Dict[str, Any]:
        for d in self.devices:
            if d["id"] == device_id:
                return {"status": "ok", "device": d}

        return {"status": "error", "reason": "device_not_found"}

    # ------------------------------------------------------------------
    # LIST DEVICES
    # ------------------------------------------------------------------
    def list_devices(self) -> Dict[str, Any]:
        return {"status": "ok", "devices": list(self.devices)}

    # ------------------------------------------------------------------
    # LIST DEVICES BY ROOM
    # ------------------------------------------------------------------
    def list_devices_in_room(self, room: str) -> Dict[str, Any]:
        result = [d for d in self.devices if d.get("room") == room]
        return {"status": "ok", "devices": result}

    # ------------------------------------------------------------------
    # DELETE DEVICE
    # ------------------------------------------------------------------
    def delete_device(self, device_id: str) -> Dict[str, Any]:
        for d in self.devices:
            if d["id"] == device_id:
                self.devices.remove(d)
                return {"status": "ok"}

        return {"status": "error", "reason": "device_not_found"}

    # ------------------------------------------------------------------
    # STATUS
    # ------------------------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "status": "ok",
            "initialized": self.initialized,
            "degraded_mode": self.degraded_mode,
            "devices_count": len(self.devices),
        }

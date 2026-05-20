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

Security Family 4.4:
- žiadne nebezpečné typy
- deterministické správanie
- Self‑Repair 4.4 ready
"""

from typing import Dict, Any, List, Optional


class HouseholdDeviceRegistry44:
    """
    Deterministic registry domácich zariadení.
    """

    def __init__(self):
        self.initialized = False
        self.degraded_mode = False
        self.safe_mode = False

        self.devices: List[Dict[str, Any]] = []

    # ---------------------------------------------------------
    # INTERNAL VALIDATION
    # ---------------------------------------------------------
    def _validate_str(self, value: Any) -> bool:
        return isinstance(value, str) and value.strip()

    def _validate_list(self, value: Any) -> bool:
        return isinstance(value, list)

    def _validate_capabilities(self, caps: Any) -> bool:
        if not isinstance(caps, list):
            return False
        for c in caps:
            if not isinstance(c, str) or not c.strip():
                return False
        return True

    # ---------------------------------------------------------
    # INITIALIZATION
    # ---------------------------------------------------------
    def initialize(self) -> Dict[str, Any]:
        if self.initialized:
            return {"status": "already_initialized"}

        try:
            self.devices = []
            self.initialized = True
            return {"status": "initialized"}
        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "exception": str(exc)}

    # ---------------------------------------------------------
    # REGISTER DEVICE
    # ---------------------------------------------------------
    def register_device(
        self,
        device_id: str,
        name: str,
        device_type: str,
        room: Optional[str] = None,
        capabilities: Optional[List[str]] = None,
    ) -> Dict[str, Any]:

        if self.safe_mode:
            return {"status": "safe_mode", "message": "Device registry disabled in safe-mode."}

        # VALIDATION
        if not self._validate_str(device_id):
            return {"status": "error", "code": "invalid_device_id"}

        if not self._validate_str(name):
            return {"status": "error", "code": "invalid_device_name"}

        if not self._validate_str(device_type):
            return {"status": "error", "code": "invalid_device_type"}

        if room is not None and not self._validate_str(room):
            return {"status": "error", "code": "invalid_room"}

        if capabilities is not None and not self._validate_capabilities(capabilities):
            return {"status": "error", "code": "invalid_capabilities"}

        # DUPLICITY CHECK
        for d in self.devices:
            if d["id"] == device_id:
                return {"status": "error", "code": "device_id_exists"}

        try:
            device = {
                "id": device_id,
                "name": name,
                "type": device_type,
                "room": room,
                "capabilities": capabilities or [],
            }

            self.devices.append(device)

            return {"status": "ok", "device": device}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "code": "device_register_failed", "exception": str(exc)}

    # ---------------------------------------------------------
    # GET DEVICE
    # ---------------------------------------------------------
    def get_device(self, device_id: str) -> Dict[str, Any]:
        if not self._validate_str(device_id):
            return {"status": "error", "code": "invalid_device_id"}

        for d in self.devices:
            if d["id"] == device_id:
                return {"status": "ok", "device": d}

        return {"status": "error", "code": "device_not_found"}

    # ---------------------------------------------------------
    # LIST DEVICES
    # ---------------------------------------------------------
    def list_devices(self) -> Dict[str, Any]:
        return {"status": "ok", "devices": list(self.devices)}

    # ---------------------------------------------------------
    # LIST DEVICES BY ROOM
    # ---------------------------------------------------------
    def list_devices_in_room(self, room: str) -> Dict[str, Any]:
        if not self._validate_str(room):
            return {"status": "error", "code": "invalid_room"}

        result = [d for d in self.devices if d.get("room") == room]
        return {"status": "ok", "devices": result}

    # ---------------------------------------------------------
    # DELETE DEVICE
    # ---------------------------------------------------------
    def delete_device(self, device_id: str) -> Dict[str, Any]:
        if not self._validate_str(device_id):
            return {"status": "error", "code": "invalid_device_id"}

        try:
            for d in self.devices:
                if d["id"] == device_id:
                    self.devices.remove(d)
                    return {"status": "ok"}

            return {"status": "error", "code": "device_not_found"}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "code": "device_delete_failed", "exception": str(exc)}

    # ---------------------------------------------------------
    # STATUS
    # ---------------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "status": "ok",
            "initialized": self.initialized,
            "safe_mode": self.safe_mode,
            "degraded_mode": self.degraded_mode,
            "devices_count": len(self.devices),
        }

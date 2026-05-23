"""
SIRIUS LOCAL AI – Home Energy Monitor 4.5.0

Účel:
- deterministické sledovanie spotreby energie v domácnosti
- 100 % offline, žiadne AI heuristiky, žiadne dynamické importy

Security Family 4.5:
- žiadne nebezpečné typy
- deterministické správanie
- Self‑Repair 4.5 ready
"""

from typing import Dict, Any, Optional, List


class HomeEnergyMonitor45:
    """
    Deterministic energy monitor pre domácnosť 4.5.
    """

    def __init__(self, device_registry=None, state_manager=None, event_bus=None):
        self.initialized = False
        self.degraded_mode = False
        self.safe_mode = False

        self.device_registry = device_registry
        self.state_manager = state_manager
        self.event_bus = event_bus

        # device_id → profil
        self.profiles: Dict[str, Dict[str, Any]] = {}

        self.default_wattage = 5.0

    # ---------------------------------------------------------
    # INTERNAL VALIDATION
    # ---------------------------------------------------------
    def _validate_str(self, value: Any) -> bool:
        return isinstance(value, str) and value.strip()

    def _validate_float(self, value: Any) -> bool:
        return isinstance(value, (int, float))

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

            # Inicializácia profilov
            devices = self.device_registry.list_devices().get("devices", [])
            for d in devices:
                dev_id = d.get("id")
                if not self._validate_str(dev_id):
                    continue

                if dev_id not in self.profiles:
                    self.profiles[dev_id] = {
                        "device_id": dev_id,
                        "wattage": self.default_wattage,
                        "energy_kwh": 0.0,
                    }

            self.initialized = True
            return {"status": "initialized", "version": "4.5"}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "exception": str(exc), "version": "4.5"}

    # ---------------------------------------------------------
    # SET WATTAGE
    # ---------------------------------------------------------
    def set_wattage(self, device_id: str, wattage: float) -> Dict[str, Any]:
        if self.safe_mode:
            return {
                "status": "safe_mode",
                "message": "Energy monitor disabled in safe-mode.",
                "version": "4.5",
            }

        if not self._validate_str(device_id):
            return {"status": "error", "code": "invalid_device_id", "version": "4.5"}

        if not self._validate_float(wattage) or wattage < 0:
            return {"status": "error", "code": "invalid_wattage", "version": "4.5"}

        try:
            if device_id not in self.profiles:
                self.profiles[device_id] = {
                    "device_id": device_id,
                    "wattage": wattage,
                    "energy_kwh": 0.0,
                }
            else:
                self.profiles[device_id]["wattage"] = wattage

            return {"status": "ok", "profile": dict(self.profiles[device_id]), "version": "4.5"}

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "wattage_set_failed",
                "exception": str(exc),
                "version": "4.5",
            }

    # ---------------------------------------------------------
    # TICK – UPDATE ENERGY
    # ---------------------------------------------------------
    def tick(self, hours: float) -> Dict[str, Any]:
        if self.safe_mode:
            return {
                "status": "safe_mode",
                "message": "Energy monitor disabled in safe-mode.",
                "version": "4.5",
            }

        if not self._validate_float(hours) or hours <= 0:
            return {"status": "error", "code": "invalid_hours", "version": "4.5"}

        if not self.state_manager:
            return {"status": "error", "code": "no_state_manager", "version": "4.5"}

        updated: List[Dict[str, Any]] = []

        try:
            for device_id, profile in self.profiles.items():
                state = self.state_manager.get_state(device_id)
                if state.get("status") != "ok":
                    continue

                value = state.get("value")
                active = value in ("on", "open")

                if active:
                    delta = profile["wattage"] * hours / 1000.0
                    profile["energy_kwh"] += delta

                    updated.append({
                        "device_id": device_id,
                        "delta_kwh": delta,
                        "total_kwh": profile["energy_kwh"],
                    })

            if self.event_bus and updated:
                try:
                    self.event_bus.emit("energy_tick_applied", {"updated": updated})
                except Exception:
                    self.degraded_mode = True

            return {"status": "ok", "updated": updated, "version": "4.5"}

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "tick_failed",
                "exception": str(exc),
                "version": "4.5",
            }

    # ---------------------------------------------------------
    # GET DEVICE ENERGY
    # ---------------------------------------------------------
    def get_device_energy(self, device_id: str) -> Dict[str, Any]:
        if not self._validate_str(device_id):
            return {"status": "error", "code": "invalid_device_id", "version": "4.5"}

        profile = self.profiles.get(device_id)
        if not profile:
            return {"status": "error", "code": "device_not_tracked", "version": "4.5"}

        return {"status": "ok", "profile": dict(profile), "version": "4.5"}

    # ---------------------------------------------------------
    # GET TOTAL ENERGY
    # ---------------------------------------------------------
    def get_total_energy(self) -> Dict[str, Any]:
        try:
            total = sum(p["energy_kwh"] for p in self.profiles.values())
            return {"status": "ok", "total_kwh": total, "version": "4.5"}
        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "total_energy_failed",
                "exception": str(exc),
                "version": "4.5",
            }

    # ---------------------------------------------------------
    # RESET ENERGY
    # ---------------------------------------------------------
    def reset_energy(self, device_id: Optional[str] = None) -> Dict[str, Any]:
        if self.safe_mode:
            return {
                "status": "safe_mode",
                "message": "Energy monitor disabled in safe-mode.",
                "version": "4.5",
            }

        try:
            if device_id is None:
                for p in self.profiles.values():
                    p["energy_kwh"] = 0.0
                return {"status": "ok", "version": "4.5"}

            if not self._validate_str(device_id):
                return {"status": "error", "code": "invalid_device_id", "version": "4.5"}

            if device_id not in self.profiles:
                return {"status": "error", "code": "device_not_tracked", "version": "4.5"}

            self.profiles[device_id]["energy_kwh"] = 0.0
            return {"status": "ok", "version": "4.5"}

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "reset_failed",
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
            "tracked_devices": len(self.profiles),
            "version": "4.5",
        }

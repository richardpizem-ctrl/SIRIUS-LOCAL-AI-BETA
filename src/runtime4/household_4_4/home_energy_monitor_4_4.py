# household_4_4/home_energy_monitor_4_4.py
"""
SIRIUS LOCAL AI – Home Energy Monitor 4.4.0

Účel:
- jednoduché, deterministické sledovanie spotreby energie v domácnosti
- 100 % offline, žiadne AI heuristiky, žiadne dynamické importy

Model:
- každé zariadenie môže mať definovaný "wattage" (W)
- pri zapnutí/vypnutí sa aktualizuje odhad spotreby
- modul nepočíta reálny čas – pracuje s explicitnými tick/interval volaniami

Device energy profile:
{
    "device_id": "dev_001",
    "wattage": 10.0,          # W
    "energy_kwh": 0.05        # kumulatívne kWh
}
"""

from typing import Dict, Any, Optional, List


class HomeEnergyMonitor44:
    """
    Deterministic energy monitor pre domácnosť.
    """

    def __init__(self, device_registry=None, state_manager=None, event_bus=None):
        self.initialized = False
        self.degraded_mode = False

        self.device_registry = device_registry
        self.state_manager = state_manager
        self.event_bus = event_bus

        # device_id → profil
        self.profiles: Dict[str, Dict[str, Any]] = {}

        # defaultný wattage, ak nie je definovaný
        self.default_wattage = 5.0

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

            # Inicializácia profilov pre všetky zariadenia
            devices = self.device_registry.list_devices().get("devices", [])
            for d in devices:
                dev_id = d["id"]
                if dev_id not in self.profiles:
                    self.profiles[dev_id] = {
                        "device_id": dev_id,
                        "wattage": self.default_wattage,
                        "energy_kwh": 0.0,
                    }

            self.initialized = True
            return {"status": "initialized"}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "exception": str(exc)}

    # ------------------------------------------------------------------
    # SET WATTAGE
    # ------------------------------------------------------------------
    def set_wattage(self, device_id: str, wattage: float) -> Dict[str, Any]:
        if device_id not in self.profiles:
            self.profiles[device_id] = {
                "device_id": device_id,
                "wattage": wattage,
                "energy_kwh": 0.0,
            }
        else:
            self.profiles[device_id]["wattage"] = wattage

        return {"status": "ok", "profile": self.profiles[device_id]}

    # ------------------------------------------------------------------
    # TICK – UPDATE ENERGY
    # ------------------------------------------------------------------
    def tick(self, hours: float) -> Dict[str, Any]:
        """
        Deterministický update spotreby.
        Predpoklad:
        - zariadenia so stavom "on" alebo "open" berieme ako aktívne
        - ostatné ignorujeme
        """

        if not self.state_manager:
            return {"status": "error", "reason": "no_state_manager"}

        updated: List[Dict[str, Any]] = []

        for device_id, profile in self.profiles.items():
            state = self.state_manager.get_state(device_id)
            if state.get("status") != "ok":
                continue

            value = state.get("value")
            active = value in ("on", "open")

            if active:
                # P = W, E = P * t (kWh) → W * h / 1000
                delta = profile["wattage"] * hours / 1000.0
                profile["energy_kwh"] += delta
                updated.append({
                    "device_id": device_id,
                    "delta_kwh": delta,
                    "total_kwh": profile["energy_kwh"],
                })

        if self.event_bus and updated:
            self.event_bus.emit("energy_tick_applied", {"updated": updated})

        return {"status": "ok", "updated": updated}

    # ------------------------------------------------------------------
    # GET DEVICE ENERGY
    # ------------------------------------------------------------------
    def get_device_energy(self, device_id: str) -> Dict[str, Any]:
        profile = self.profiles.get(device_id)
        if not profile:
            return {"status": "error", "reason": "device_not_tracked"}

        return {"status": "ok", "profile": dict(profile)}

    # ------------------------------------------------------------------
    # GET TOTAL ENERGY
    # ------------------------------------------------------------------
    def get_total_energy(self) -> Dict[str, Any]:
        total = sum(p["energy_kwh"] for p in self.profiles.values())
        return {"status": "ok", "total_kwh": total}

    # ------------------------------------------------------------------
    # RESET ENERGY
    # ------------------------------------------------------------------
    def reset_energy(self, device_id: Optional[str] = None) -> Dict[str, Any]:
        if device_id is None:
            for p in self.profiles.values():
                p["energy_kwh"] = 0.0
            return {"status": "ok"}

        if device_id not in self.profiles:
            return {"status": "error", "reason": "device_not_tracked"}

        self.profiles[device_id]["energy_kwh"] = 0.0
        return {"status": "ok"}

    # ------------------------------------------------------------------
    # STATUS
    # ------------------------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "status": "ok",
            "initialized": self.initialized,
            "degraded_mode": self.degraded_mode,
            "tracked_devices": len(self.profiles),
        }

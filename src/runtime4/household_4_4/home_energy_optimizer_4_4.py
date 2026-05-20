# household_4_4/home_energy_optimizer_4_4.py
"""
SIRIUS LOCAL AI – Home Energy Optimizer 4.4.0

Účel:
- nadstavba nad HomeEnergyMonitor44 + StateManager
- hľadá jednoduché, deterministické úspory:
    - identifikácia najväčších žrútov energie
    - návrh vypnutia neaktívnych / zbytočných zariadení
- 100 % offline, žiadne AI heuristiky, žiadne dynamické importy

Poznámka:
- modul NERIADI čas, pracuje len s aktuálnym stavom a kumulatívnou spotrebou
"""

from typing import Dict, Any, List, Optional


class HomeEnergyOptimizer44:
    """
    Deterministic energy optimizer pre domácnosť.
    """

    def __init__(self, energy_monitor=None, state_manager=None, event_bus=None):
        self.initialized = False
        self.degraded_mode = False

        self.energy_monitor = energy_monitor
        self.state_manager = state_manager
        self.event_bus = event_bus

        # prah pre "vysokú spotrebu" v kWh
        self.high_usage_threshold_kwh = 1.0

    # ------------------------------------------------------------------
    # INITIALIZATION
    # ------------------------------------------------------------------
    def initialize(self) -> Dict[str, Any]:
        if self.initialized:
            return {"status": "already_initialized"}

        try:
            if self.energy_monitor:
                self.energy_monitor.initialize()
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
    # ANALYZE – FIND HIGH USAGE DEVICES
    # ------------------------------------------------------------------
    def analyze_high_usage(self) -> Dict[str, Any]:
        """
        Nájde zariadenia s vysokou kumulatívnou spotrebou.
        """

        if not self.energy_monitor:
            return {"status": "error", "reason": "no_energy_monitor"}

        high: List[Dict[str, Any]] = []

        # energy_monitor.profiles: device_id → profil
        for device_id, profile in self.energy_monitor.profiles.items():
            energy = profile.get("energy_kwh", 0.0)
            if energy >= self.high_usage_threshold_kwh:
                high.append({
                    "device_id": device_id,
                    "energy_kwh": energy,
                    "wattage": profile.get("wattage"),
                })

        high.sort(key=lambda x: x["energy_kwh"], reverse=True)

        return {"status": "ok", "high_usage_devices": high}

    # ------------------------------------------------------------------
    # SUGGEST SHUTDOWN – DEVICES ON & HIGH USAGE
    # ------------------------------------------------------------------
    def suggest_shutdown(self) -> Dict[str, Any]:
        """
        Navrhne vypnutie zariadení, ktoré:
        - sú aktuálne zapnuté
        - majú vysokú kumulatívnu spotrebu
        """

        if not self.state_manager or not self.energy_monitor:
            return {"status": "error", "reason": "missing_dependencies"}

        suggestions: List[Dict[str, Any]] = []

        for device_id, profile in self.energy_monitor.profiles.items():
            energy = profile.get("energy_kwh", 0.0)
            if energy < self.high_usage_threshold_kwh:
                continue

            st = self.state_manager.get_state(device_id)
            if st.get("status") != "ok":
                continue

            value = st.get("value")
            if value not in ("on", "open"):
                continue

            suggestions.append({
                "device_id": device_id,
                "current_state": value,
                "energy_kwh": energy,
                "wattage": profile.get("wattage"),
            })

        suggestions.sort(key=lambda x: x["energy_kwh"], reverse=True)

        return {"status": "ok", "suggestions": suggestions}

    # ------------------------------------------------------------------
    # APPLY SHUTDOWN SUGGESTIONS
    # ------------------------------------------------------------------
    def apply_shutdown(self, max_devices: Optional[int] = None) -> Dict[str, Any]:
        """
        Aplikuje návrhy na vypnutie – deterministicky, bez heuristiky.
        max_devices:
            - None → všetky
            - N → len prvých N podľa spotreby
        """

        if not self.state_manager or not self.energy_monitor:
            return {"status": "error", "reason": "missing_dependencies"}

        sug_res = self.suggest_shutdown()
        if sug_res.get("status") != "ok":
            return sug_res

        suggestions = sug_res.get("suggestions", [])
        if max_devices is not None:
            suggestions = suggestions[:max_devices]

        results: List[Dict[str, Any]] = []

        for s in suggestions:
            dev_id = s["device_id"]
            res = self.state_manager.set_state(dev_id, "off", None)
            results.append({
                "device_id": dev_id,
                "result": res,
            })

        if self.event_bus and results:
            self.event_bus.emit("energy_optimization_applied", {
                "results": results,
            })

        return {"status": "ok", "applied": results}

    # ------------------------------------------------------------------
    # SET THRESHOLD
    # ------------------------------------------------------------------
    def set_high_usage_threshold(self, kwh: float) -> Dict[str, Any]:
        self.high_usage_threshold_kwh = float(kwh)
        return {"status": "ok", "threshold_kwh": self.high_usage_threshold_kwh}

    # ------------------------------------------------------------------
    # STATUS
    # ------------------------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "status": "ok",
            "initialized": self.initialized,
            "degraded_mode": self.degraded_mode,
            "high_usage_threshold_kwh": self.high_usage_threshold_kwh,
        }

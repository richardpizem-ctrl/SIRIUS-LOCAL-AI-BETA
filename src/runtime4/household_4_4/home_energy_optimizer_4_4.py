"""
SIRIUS LOCAL AI – Home Energy Optimizer 4.5.0

Účel:
- deterministická nadstavba nad HomeEnergyMonitor45 + StateManager45
- hľadá jednoduché úspory energie bez AI heuristík
- 100 % offline, deterministické

Security Family 4.5:
- žiadne nebezpečné typy
- deterministické správanie
- Self‑Repair 4.5 ready
"""

from typing import Dict, Any, List, Optional


class HomeEnergyOptimizer45:
    """
    Deterministic energy optimizer pre domácnosť 4.5.
    """

    def __init__(self, energy_monitor=None, state_manager=None, event_bus=None):
        self.initialized = False
        self.degraded_mode = False
        self.safe_mode = False

        self.energy_monitor = energy_monitor
        self.state_manager = state_manager
        self.event_bus = event_bus

        # prah pre "vysokú spotrebu" v kWh
        self.high_usage_threshold_kwh = 1.0

    # ---------------------------------------------------------
    # INTERNAL VALIDATION
    # ---------------------------------------------------------
    def _validate_float(self, value: Any) -> bool:
        return isinstance(value, (int, float))

    def _validate_str(self, value: Any) -> bool:
        return isinstance(value, str) and value.strip()

    # ---------------------------------------------------------
    # INITIALIZATION
    # ---------------------------------------------------------
    def initialize(self) -> Dict[str, Any]:
        if self.initialized:
            return {"status": "already_initialized", "version": "4.5"}

        try:
            modules = [self.energy_monitor, self.state_manager, self.event_bus]
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

            self.initialized = True
            return {"status": "initialized", "version": "4.5"}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "exception": str(exc), "version": "4.5"}

    # ---------------------------------------------------------
    # ANALYZE – FIND HIGH USAGE DEVICES
    # ---------------------------------------------------------
    def analyze_high_usage(self) -> Dict[str, Any]:
        if self.safe_mode:
            return {
                "status": "safe_mode",
                "message": "Optimizer disabled in safe-mode.",
                "version": "4.5",
            }

        if not self.energy_monitor:
            return {"status": "error", "code": "no_energy_monitor", "version": "4.5"}

        try:
            high: List[Dict[str, Any]] = []

            for device_id, profile in self.energy_monitor.profiles.items():
                energy = profile.get("energy_kwh", 0.0)
                if energy >= self.high_usage_threshold_kwh:
                    high.append({
                        "device_id": device_id,
                        "energy_kwh": energy,
                        "wattage": profile.get("wattage"),
                    })

            high.sort(key=lambda x: x["energy_kwh"], reverse=True)

            return {"status": "ok", "high_usage_devices": high, "version": "4.5"}

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "analyze_failed",
                "exception": str(exc),
                "version": "4.5",
            }

    # ---------------------------------------------------------
    # SUGGEST SHUTDOWN
    # ---------------------------------------------------------
    def suggest_shutdown(self) -> Dict[str, Any]:
        if self.safe_mode:
            return {
                "status": "safe_mode",
                "message": "Optimizer disabled in safe-mode.",
                "version": "4.5",
            }

        if not self.state_manager or not self.energy_monitor:
            return {"status": "error", "code": "missing_dependencies", "version": "4.5"}

        try:
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

            return {"status": "ok", "suggestions": suggestions, "version": "4.5"}

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "suggest_failed",
                "exception": str(exc),
                "version": "4.5",
            }

    # ---------------------------------------------------------
    # APPLY SHUTDOWN SUGGESTIONS
    # ---------------------------------------------------------
    def apply_shutdown(self, max_devices: Optional[int] = None) -> Dict[str, Any]:
        if self.safe_mode:
            return {
                "status": "safe_mode",
                "message": "Optimizer disabled in safe-mode.",
                "version": "4.5",
            }

        if not self.state_manager or not self.energy_monitor:
            return {"status": "error", "code": "missing_dependencies", "version": "4.5"}

        try:
            sug_res = self.suggest_shutdown()
            if sug_res.get("status") != "ok":
                return sug_res

            suggestions = sug_res.get("suggestions", [])
            if max_devices is not None:
                if not isinstance(max_devices, int) or max_devices < 0:
                    return {"status": "error", "code": "invalid_max_devices", "version": "4.5"}
                suggestions = suggestions[:max_devices]

            results: List[Dict[str, Any]] = []

            for s in suggestions:
                dev_id = s["device_id"]
                res = self.state_manager.set_state(dev_id, "off", None)
                results.append({"device_id": dev_id, "result": res})

            if self.event_bus and results:
                try:
                    self.event_bus.emit("energy_optimization_applied", {"results": results})
                except Exception:
                    self.degraded_mode = True

            return {"status": "ok", "applied": results, "version": "4.5"}

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "apply_failed",
                "exception": str(exc),
                "version": "4.5",
            }

    # ---------------------------------------------------------
    # SET THRESHOLD
    # ---------------------------------------------------------
    def set_high_usage_threshold(self, kwh: float) -> Dict[str, Any]:
        if not self._validate_float(kwh) or kwh < 0:
            return {"status": "error", "code": "invalid_threshold", "version": "4.5"}

        try:
            self.high_usage_threshold_kwh = float(kwh)
            return {"status": "ok", "threshold_kwh": self.high_usage_threshold_kwh, "version": "4.5"}
        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "threshold_set_failed",
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
            "high_usage_threshold_kwh": self.high_usage_threshold_kwh,
            "version": "4.5",
        }

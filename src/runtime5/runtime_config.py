"""
SIRIUS Runtime 5.1.0
Runtime Config 5.1

Účel:
- poskytovať jednotnú konfiguráciu pre RuntimeCore, WorkflowEngine5,
  HealthMonitor5, SystemAgent5 a Self‑Repair Layer 1.0
- umožniť jednoduché DI (dependency injection) a override hodnot
"""

from typing import Dict, Any


class RuntimeConfig:
    """
    RuntimeConfig – centrálna konfigurácia Runtime5.

    Konfigurácia je dict-like objekt:
        - podporuje get()
        - podporuje override cez update()
        - obsahuje default hodnoty pre celý runtime
    """

    def __init__(self, overrides: Dict[str, Any] | None = None):
        # DEFAULT KONFIGURÁCIA RUNTIME 5.1
        self._config: Dict[str, Any] = {
            # Self‑Repair Layer
            "repair_on_degraded": True,
            "repair_auto_trigger": True,
            "repair_max_attempts": 3,

            # Workflow Engine
            "workflow_max_steps": 100,
            "workflow_safe_mode": False,

            # Health Monitor
            "health_strict_mode": False,

            # System Agent
            "security_log_level": "INFO",
            "isolation_enforce": True,

            # Runtime
            "runtime_cycle_interval_ms": 250,
            "runtime_safe_exceptions": True,
        }

        # Aplikovať override hodnoty
        if overrides:
            self._config.update(overrides)

    # ---------------------------------------------------------
    # PUBLIC API
    # ---------------------------------------------------------

    def get(self, key: str, default=None):
        return self._config.get(key, default)

    def set(self, key: str, value: Any) -> None:
        self._config[key] = value

    def update(self, values: Dict[str, Any]) -> None:
        self._config.update(values)

    def as_dict(self) -> Dict[str, Any]:
        """Vráti celú konfiguráciu ako dict."""
        return dict(self._config)

    # pekná reprezentácia pre debug
    def __repr__(self) -> str:
        return f"RuntimeConfig({self._config})"

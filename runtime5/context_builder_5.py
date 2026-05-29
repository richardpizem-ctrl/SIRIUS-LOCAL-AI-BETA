# runtime5/context_builder_5.py

from typing import Dict, Any

from runtime5.logging_5 import log5
from runtime5.error_handler_5 import ErrorHandler5
from runtime5.health_monitor_5 import HealthMonitor5
from runtime5.system_hooks_5 import SystemHooks5


class ContextBuilder5:
    """
    Context Builder 5.x

    Responsibilities:
    - normalize raw text input
    - extract entity candidate
    - prepare structured context for ReasoningEngine5
    - diagnostics + degraded mode awareness
    - Self‑Repair Layer compatibility
    """

    def __init__(self):
        log5("[ContextBuilder5] Initialized context builder 5.x")

    # --------------------------------------------------------
    # PUBLIC API
    # --------------------------------------------------------
    def build(self, text: str) -> Dict[str, Any]:
        """
        Build normalized context from raw text.
        Returns:
        {
            "raw": original text,
            "entity": extracted entity,
            "clean": normalized text,
            "degraded": bool
        }
        """

        def _exec():
            raw = text or ""
            clean = raw.strip()

            log5(f"[ContextBuilder5] Building context for: {clean!r}")

            # Extract entity candidate
            # Simple deterministic rule:
            # - if input contains ":", take right side
            # - else use whole text
            if ":" in clean:
                entity = clean.split(":", 1)[1].strip()
            else:
                entity = clean

            # If entity is empty, fallback to raw
            if not entity:
                entity = clean

            ctx = {
                "raw": raw,
                "clean": clean,
                "entity": entity,
                "degraded": HealthMonitor5.is_degraded()
            }

            log5(f"[ContextBuilder5] Context built: {ctx}")
            HealthMonitor5.record_success()
            return ctx

        return ErrorHandler5.safe_execute(
            _exec,
            context={"input": text},
            fallback={
                "raw": text,
                "clean": text.strip() if text else "",
                "entity": text.strip() if text else "",
                "degraded": HealthMonitor5.is_degraded(),
                "error": "ContextBuilder5 failed."
            }
        )

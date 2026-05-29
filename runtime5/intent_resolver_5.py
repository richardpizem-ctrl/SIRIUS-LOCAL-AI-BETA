# runtime5/intent_resolver_5.py

from typing import Any

from runtime5.logging_5 import log5
from runtime5.error_handler_5 import ErrorHandler5
from runtime5.health_monitor_5 import HealthMonitor5
from runtime5.system_hooks_5 import SystemHooks5


class IntentResolver5:
    """
    Intent Resolver 5.x

    Lightweight, deterministic intent resolver for Runtime 5.x.
    Responsibilities:
    - normalize raw text input
    - map text → high‑level intent label
    - provide diagnostics + degraded mode awareness
    - be fully safe (ErrorHandler5 wrapped)
    """

    def __init__(self):
        log5("[IntentResolver5] Initialized intent resolver 5.x")

    # --------------------------------------------------------
    # PUBLIC API
    # --------------------------------------------------------
    def resolve(self, text: str) -> Any:
        """
        Resolve raw input text into a high‑level intent label.

        Returns:
        - string intent label (e.g. 'KG_REASONING', 'ENVOY', 'SYSTEM_AGENT', 'WORKFLOW_CONTINUE')
        """
        def _exec():
            raw = text or ""
            s = raw.strip()
            lower = s.lower()

            log5(f"[IntentResolver5] Resolving intent for input: {s!r}")

            if not s:
                intent = "EMPTY"
            elif lower.startswith("kg:") or lower.startswith("kg "):
                intent = "KG_REASONING"
            elif lower.startswith("envoy:") or lower.startswith("envoy ") \
                    or lower.startswith("http://") or lower.startswith("https://"):
                intent = "ENVOY"
            elif lower.startswith("sys:") or lower.startswith("sys ") or lower.startswith("system "):
                intent = "SYSTEM_AGENT"
            else:
                intent = "WORKFLOW_CONTINUE"

            log5(f"[IntentResolver5] Resolved intent: {intent}")
            HealthMonitor5.record_success()
            return intent

        return ErrorHandler5.safe_execute(
            _exec,
            context={"input": text},
            fallback="WORKFLOW_CONTINUE"
        )

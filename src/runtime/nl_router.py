import logging
import time
import re
from typing import Dict, Any, Callable

log = logging.getLogger(__name__)


class NaturalLanguageRouter:
    """
    NL Router 4.4
    ----------------
    - Plugin dynamic NL commands (regex + parameters)
    - Security Family enforcement (identity, capabilities, risk)
    - Telemetry (duration, matched_command, source)
    - Deterministic structured returns
    - Rule-based commands (Password Vault 4.x)
    - AITE fallback
    - SiriusAgent interpret fallback
    - Self‑Repair Layer 4.4 ready (safe-mode, degraded mode)
    - Stable error model for Runtime4.4
    """

    def __init__(self, runtime_manager):
        self.rm = runtime_manager
        self.agent = runtime_manager.agent
        self.dynamic_commands: Dict[str, Callable[[str, Any], Any]] = {}
        self.safe_mode = False
        self.degraded_mode = False

    # --------------------------------------------------------
    # REGISTER PLUGIN COMMAND
    # --------------------------------------------------------
    def register(self, phrase: str, fn: Callable[[str, Any], Any]):
        """
        Register NL command from plugin.
        Supports regex patterns.
        """
        key = phrase.lower()
        self.dynamic_commands[key] = fn
        log.info("NL Router registered plugin command: '%s'", phrase)

        return {
            "status": "success",
            "command": key
        }

    # --------------------------------------------------------
    # MAIN HANDLER
    # --------------------------------------------------------
    def handle(self, text: str) -> Dict[str, Any]:
        t0 = time.time()
        original_text = text
        text = text.lower().strip()
        log.info("NL Router received: %s", text)

        # SAFE MODE (Self‑Repair)
        if self.safe_mode:
            return {
                "status": "safe_mode",
                "message": "NL Router is running in safe-mode.",
                "duration": time.time() - t0,
            }

        # ----------------------------------------------------
        # 1) Plugin NL commands (regex match)
        # ----------------------------------------------------
        for pattern, fn in self.dynamic_commands.items():
            if re.search(pattern, text):
                try:
                    # Security Family enforcement
                    if not self._security_check(fn):
                        return {
                            "status": "blocked",
                            "source": "security",
                            "command": pattern,
                            "message": "Command blocked by Security Family.",
                            "duration": time.time() - t0,
                        }

                    result = fn(original_text, self.rm)
                    return {
                        "status": "plugin",
                        "command": pattern,
                        "result": result,
                        "duration": time.time() - t0,
                    }
                except Exception as e:
                    self.degraded_mode = True
                    log.exception("NL Router plugin error (%s): %s", pattern, e)
                    return {
                        "status": "error",
                        "source": "plugin",
                        "command": pattern,
                        "exception": str(e),
                        "duration": time.time() - t0,
                    }

        # ----------------------------------------------------
        # 2) Rule-based NL commands
        # ----------------------------------------------------
        rb = self._handle_rule_based(text)
        if rb is not None:
            return {
                "status": "rule_based",
                "result": rb,
                "duration": time.time() - t0,
            }

        # ----------------------------------------------------
        # 3) AITE fallback
        # ----------------------------------------------------
        try:
            aite_result = self.rm.aite.process(original_text)
            if aite_result is not None:
                return {
                    "status": "aite",
                    "result": aite_result,
                    "duration": time.time() - t0,
                }
        except Exception as e:
            log.exception("AITE error: %s", e)

        # ----------------------------------------------------
        # 4) SiriusAgent interpret fallback
        # ----------------------------------------------------
        try:
            agent_result = self.agent.run_task("interpret", {"text": original_text})
            if agent_result is not None:
                return {
                    "status": "agent",
                    "result": agent_result,
                    "duration": time.time() - t0,
                }
        except Exception as e:
            log.exception("Agent interpret error: %s", e)

        # ----------------------------------------------------
        # 5) Final fallback
        # ----------------------------------------------------
        return {
            "status": "error",
            "source": "router",
            "message": "I do not understand the command.",
            "duration": time.time() - t0,
        }

    # --------------------------------------------------------
    # SECURITY FAMILY CHECK
    # --------------------------------------------------------
    def _security_check(self, fn: Callable) -> bool:
        """
        Placeholder for Security Family 4.4:
        - identity check
        - capability check
        - risk check
        """
        # TODO: integrate with runtime_manager.security
        return True

    # --------------------------------------------------------
    # RULE-BASED COMMANDS (PASSWORD VAULT 4.x)
    # --------------------------------------------------------
    def _handle_rule_based(self, text: str):
        # sem môžeš doplniť svoje existujúce pravidlá (Password Vault 4.x, atď.)
        # ak nič nematchne, vráť None
        return None

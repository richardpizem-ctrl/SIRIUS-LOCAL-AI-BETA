"""
SIRIUS LOCAL AI – Household Command Parser 4.4.0

Účel:
- deterministické rozpoznávanie domácich príkazov
- žiadne AI, žiadne heuristiky, žiadne dynamické importy
- čisté patterny a pravidlá

Podporované intent typy:
1. device_control
2. routine_trigger
3. task_create

Príklady:
- "zapni svetlo v kuchyni"
- "vypni všetky svetlá v obývačke"
- "spusti rutinu good night"
- "pridaj úlohu vyniesť smeti v kuchyni"

Security Family 4.4:
- žiadne nebezpečné typy
- žiadne dynamické operácie
- deterministické spracovanie
"""

from typing import Dict, Any, Optional


class HouseholdCommandParser44:
    """
    Deterministic parser domácich príkazov.
    Fully offline‑safe, deterministic, Security Family 4.4 compliant.
    """

    def __init__(self):
        self.initialized = False
        self.degraded_mode = False
        self.safe_mode = False

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
    # MAIN PARSE
    # ------------------------------------------------------------------
    def parse(self, command: str) -> Dict[str, Any]:
        # SAFE MODE
        if self.safe_mode:
            return {
                "status": "safe_mode",
                "message": "Command parsing disabled in safe-mode.",
                "degraded_mode": self.degraded_mode,
            }

        # VALIDATION
        if not isinstance(command, str):
            return {"status": "error", "code": "invalid_command_type"}

        cmd = command.lower().strip()
        if not cmd:
            return {"status": "error", "code": "empty_command"}

        # DEVICE CONTROL
        dc = self._parse_device_control(cmd)
        if dc:
            return {
                "status": "ok",
                "intent": "device_control",
                "payload": dc,
                "degraded_mode": self.degraded_mode,
            }

        # ROUTINE TRIGGER
        rt = self._parse_routine_trigger(cmd)
        if rt:
            return {
                "status": "ok",
                "intent": "routine_trigger",
                "payload": rt,
                "degraded_mode": self.degraded_mode,
            }

        # TASK CREATE
        tc = self._parse_task_create(cmd)
        if tc:
            return {
                "status": "ok",
                "intent": "task_create",
                "payload": tc,
                "degraded_mode": self.degraded_mode,
            }

        return {
            "status": "error",
            "code": "unrecognized_command",
            "degraded_mode": self.degraded_mode,
        }

    # ------------------------------------------------------------------
    # DEVICE CONTROL PARSER
    # ------------------------------------------------------------------
    def _parse_device_control(self, cmd: str) -> Optional[Dict[str, Any]]:
        actions = {
            "zapni": "on",
            "vypni": "off",
            "otvor": "open",
            "zavri": "close",
            "zatvor": "close",
            "nastav": "set",
        }

        action = None
        for k, v in actions.items():
            if cmd.startswith(k + " "):
                action = v
                break

        if not action:
            return None

        # ROOM TARGET
        if " v " in cmd:
            parts = cmd.split(" v ")
            room = parts[-1].strip()
            if room:
                return {
                    "action": action,
                    "target_type": "room",
                    "room": room,
                }

        # DEVICE TARGET
        if " zariadenie " in cmd:
            parts = cmd.split(" zariadenie ")
            device_id = parts[-1].strip()
            if device_id:
                return {
                    "action": action,
                    "target_type": "device",
                    "device_id": device_id,
                }

        return None

    # ------------------------------------------------------------------
    # ROUTINE TRIGGER PARSER
    # ------------------------------------------------------------------
    def _parse_routine_trigger(self, cmd: str) -> Optional[Dict[str, Any]]:
        if cmd.startswith("spusti rutinu "):
            name = cmd.replace("spusti rutinu ", "").strip()
            return {"routine_name": name} if name else None

        if cmd.startswith("spusti scénu "):
            name = cmd.replace("spusti scénu ", "").strip()
            return {"routine_name": name} if name else None

        return None

    # ------------------------------------------------------------------
    # TASK CREATE PARSER
    # ------------------------------------------------------------------
    def _parse_task_create(self, cmd: str) -> Optional[Dict[str, Any]]:
        if not cmd.startswith("pridaj úlohu "):
            return None

        text = cmd.replace("pridaj úlohu ", "").strip()
        if not text:
            return None

        if " v " in text:
            parts = text.split(" v ")
            name = parts[0].strip()
            room = parts[1].strip()
            if name:
                return {
                    "name": name,
                    "category": "general",
                    "room": room or None,
                }

        return {
            "name": text,
            "category": "general",
            "room": None,
        }

    # ------------------------------------------------------------------
    # STATUS
    # ------------------------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "status": "ok",
            "initialized": self.initialized,
            "safe_mode": self.safe_mode,
            "degraded_mode": self.degraded_mode,
        }

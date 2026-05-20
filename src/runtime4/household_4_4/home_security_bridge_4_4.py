# household_4_4/home_security_bridge_4_4.py
"""
SIRIUS LOCAL AI – Home Security Bridge 4.4.0

Účel:
- deterministický most medzi Household Automation 4.4 a bezpečnostnými režimami
- prepína domáce správanie podľa security módu:
    - HOME
    - AWAY
    - NIGHT
    - VACATION
    - SCHOOL_MODE
    - STRANGER_MODE
- 100 % offline, žiadne AI heuristiky, žiadne dynamické importy

Príklady:
- pri AWAY:
    - vypnúť svetlá
    - zamknúť dvere (ak sú mapované ako zariadenia)
- pri NIGHT:
    - vypnúť väčšinu svetiel, nechať chodbu
- pri STRANGER_MODE:
    - sprísniť safety guard (napr. len OWNER/FAMILY)
"""

from typing import Dict, Any, List, Optional


class HomeSecurityBridge44:
    """
    Deterministic security bridge pre domácnosť.
    """

    def __init__(self, state_manager=None, safety_guard=None, event_bus=None):
        self.initialized = False
        self.degraded_mode = False

        self.state_manager = state_manager
        self.safety_guard = safety_guard
        self.event_bus = event_bus

        # aktuálny security mód
        self.current_mode: str = "HOME"

        # jednoduché mapovanie módov na akcie
        self.mode_actions = {
            "HOME": [],
            "AWAY": [
                {"type": "room", "room": "all", "action": "off"},
            ],
            "NIGHT": [
                {"type": "room", "room": "living_room", "action": "off"},
                {"type": "room", "room": "kitchen", "action": "off"},
            ],
            "VACATION": [
                {"type": "room", "room": "all", "action": "off"},
            ],
            "SCHOOL_MODE": [],
            "STRANGER_MODE": [],
        }

    # ------------------------------------------------------------------
    # INITIALIZATION
    # ------------------------------------------------------------------
    def initialize(self) -> Dict[str, Any]:
        if self.initialized:
            return {"status": "already_initialized"}

        try:
            if self.state_manager:
                self.state_manager.initialize()
            if self.safety_guard:
                self.safety_guard.initialize()
            if self.event_bus:
                self.event_bus.initialize()

            self.initialized = True
            return {"status": "initialized"}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "exception": str(exc)}

    # ------------------------------------------------------------------
    # SET SECURITY MODE
    # ------------------------------------------------------------------
    def set_mode(self, mode: str) -> Dict[str, Any]:
        mode = mode.upper().strip()
        if mode not in self.mode_actions:
            return {"status": "error", "reason": "unknown_mode"}

        old_mode = self.current_mode
        self.current_mode = mode

        # aplikuj akcie módu
        actions = self.mode_actions.get(mode, [])
        results: List[Dict[str, Any]] = []

        if self.state_manager:
            for act in actions:
                t = act.get("type")
                action = act.get("action")
                value = act.get("value")

                if t == "room":
                    room = act.get("room")
                    if room == "all":
                        # špeciálny prípad – všetky miestnosti
                        # tu predpokladáme, že state_manager vie pracovať s "all"
                        res = self.state_manager.set_state_for_room("all", action, value)
                        results.append(res)
                    else:
                        res = self.state_manager.set_state_for_room(room, action, value)
                        results.append(res)

        if self.event_bus:
            self.event_bus.emit("security_mode_changed", {
                "old_mode": old_mode,
                "new_mode": mode,
                "results": results,
            })

        return {"status": "ok", "mode": mode, "results": results}

    # ------------------------------------------------------------------
    # GET CURRENT MODE
    # ------------------------------------------------------------------
    def get_mode(self) -> Dict[str, Any]:
        return {"status": "ok", "mode": self.current_mode}

    # ------------------------------------------------------------------
    # CHECK COMMAND AGAINST SECURITY MODE
    # ------------------------------------------------------------------
    def check_command(self, command: str, identity: str) -> Dict[str, Any]:
        """
        Voliteľná vrstva nad safety guardom – môže sprísniť pravidlá
        podľa aktuálneho security módu.
        """

        # najprv klasický safety guard
        if self.safety_guard:
            base = self.safety_guard.check_command(command, identity)
            if base.get("status") == "blocked":
                return base

        # dodatočné obmedzenia podľa módu
        mode = self.current_mode

        if mode == "STRANGER_MODE":
            # v tomto móde blokujeme všetko okrem OWNER
            if identity.upper().strip() != "OWNER":
                return {
                    "status": "blocked",
                    "reason": "stranger_mode_restriction",
                    "mode": mode,
                }

        if mode == "VACATION":
            # počas dovolenky blokujeme "otvor", "open", "unlock"
            lowered = command.lower()
            risky = ["otvor", "open", "unlock", "odomkni"]
            if any(w in lowered for w in risky):
                return {
                    "status": "blocked",
                    "reason": "vacation_mode_restriction",
                    "mode": mode,
                }

        return {"status": "ok", "mode": mode}

    # ------------------------------------------------------------------
    # STATUS
    # ------------------------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "status": "ok",
            "initialized": self.initialized,
            "degraded_mode": self.degraded_mode,
            "current_mode": self.current_mode,
        }

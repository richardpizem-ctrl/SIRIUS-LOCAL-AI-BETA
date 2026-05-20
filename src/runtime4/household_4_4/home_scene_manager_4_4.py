# household_4_4/home_scene_manager_4_4.py
"""
SIRIUS LOCAL AI – Home Scene Manager 4.4.0

Účel:
- správa domácich scén (preddefinované kombinácie akcií)
- scéna = skupina deterministických krokov (žiadne AI)
- 100 % offline, žiadne heuristiky, žiadne dynamické importy

Príklady scén:
- "movie_night":
    - stlmiť svetlá v obývačke
    - vypnúť kuchyňu
    - zapnúť TV zásuvku

- "good_morning":
    - zapnúť svetlá v kuchyni
    - otvoriť žalúzie
    - zapnúť kávovar

Scéna:
{
    "name": "movie_night",
    "actions": [
        {"type": "room", "room": "living_room", "action": "set", "value": "dim"},
        {"type": "room", "room": "kitchen", "action": "off"},
        {"type": "device", "device_id": "socket_tv", "action": "on"}
    ]
}
"""

from typing import Dict, Any, List, Optional


class HomeSceneManager44:
    """
    Deterministic scene manager pre domácnosť.
    """

    def __init__(self, state_manager=None, event_bus=None):
        self.initialized = False
        self.degraded_mode = False

        self.state_manager = state_manager
        self.event_bus = event_bus

        # Názov scény → definícia
        self.scenes: Dict[str, Dict[str, Any]] = {}

    # ------------------------------------------------------------------
    # INITIALIZATION
    # ------------------------------------------------------------------
    def initialize(self) -> Dict[str, Any]:
        if self.initialized:
            return {"status": "already_initialized"}

        try:
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
    # REGISTER SCENE
    # ------------------------------------------------------------------
    def register_scene(self, scene: Dict[str, Any]) -> Dict[str, Any]:
        name = scene.get("name")
        if not name:
            return {"status": "error", "reason": "missing_name"}

        if name in self.scenes:
            return {"status": "error", "reason": "scene_exists"}

        self.scenes[name] = scene
        return {"status": "ok"}

    # ------------------------------------------------------------------
    # LIST SCENES
    # ------------------------------------------------------------------
    def list_scenes(self) -> Dict[str, Any]:
        return {"status": "ok", "scenes": list(self.scenes.keys())}

    # ------------------------------------------------------------------
    # RUN SCENE
    # ------------------------------------------------------------------
    def run_scene(self, name: str) -> Dict[str, Any]:
        if name not in self.scenes:
            return {"status": "error", "reason": "scene_not_found"}

        scene = self.scenes[name]
        actions = scene.get("actions", [])
        results: List[Dict[str, Any]] = []

        if not self.state_manager:
            return {"status": "error", "reason": "no_state_manager"}

        for act in actions:
            t = act.get("type")
            action = act.get("action")
            value = act.get("value")

            if t == "room":
                room = act.get("room")
                if not room:
                    results.append({"status": "error", "reason": "missing_room"})
                    continue
                res = self.state_manager.set_state_for_room(room, action, value)
                results.append(res)

            elif t == "device":
                device_id = act.get("device_id")
                if not device_id:
                    results.append({"status": "error", "reason": "missing_device_id"})
                    continue
                res = self.state_manager.set_state(device_id, action, value)
                results.append(res)

            else:
                results.append({"status": "error", "reason": "invalid_action_type"})

        if self.event_bus:
            self.event_bus.emit("scene_executed", {
                "scene_name": name,
                "results": results,
            })

        return {"status": "ok", "results": results}

    # ------------------------------------------------------------------
    # DELETE SCENE
    # ------------------------------------------------------------------
    def delete_scene(self, name: str) -> Dict[str, Any]:
        if name not in self.scenes:
            return {"status": "error", "reason": "scene_not_found"}

        del self.scenes[name]
        return {"status": "ok"}

    # ------------------------------------------------------------------
    # STATUS
    # ------------------------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "status": "ok",
            "initialized": self.initialized,
            "degraded_mode": self.degraded_mode,
            "scenes_count": len(self.scenes),
        }

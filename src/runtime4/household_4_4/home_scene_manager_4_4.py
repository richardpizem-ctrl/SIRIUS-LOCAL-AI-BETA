"""
SIRIUS LOCAL AI – Home Scene Manager 4.5.0 (PRO)

Purpose:
- deterministic management of home scenes
- no AI heuristics, no dynamic imports
- 100% offline

Security Family 4.5:
- deterministic behavior
- safe‑mode compatible
- Self‑Repair 4.5 ready
"""

from typing import Dict, Any, List, Optional


class HomeSceneManager45:
    """
    Deterministic scene manager for household automation 4.5.
    """

    def __init__(self, state_manager=None, event_bus=None):
        self.initialized = False
        self.degraded_mode = False
        self.safe_mode = False

        self.state_manager = state_manager
        self.event_bus = event_bus

        # Scene name → definition
        self.scenes: Dict[str, Dict[str, Any]] = {}

    # ---------------------------------------------------------
    # INTERNAL VALIDATION
    # ---------------------------------------------------------
    def _validate_str(self, value: Any) -> bool:
        return isinstance(value, str) and value.strip()

    def _validate_actions(self, actions: Any) -> bool:
        if not isinstance(actions, list):
            return False
        for a in actions:
            if not isinstance(a, dict):
                return False
            if not self._validate_str(a.get("type")):
                return False
            if not self._validate_str(a.get("action")):
                return False
        return True

    # ---------------------------------------------------------
    # INITIALIZATION
    # ---------------------------------------------------------
    def initialize(self) -> Dict[str, Any]:
        if self.initialized:
            return {"status": "already_initialized", "version": "4.5"}

        try:
            modules = [self.state_manager, self.event_bus]
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
            return {
                "status": "error",
                "exception": str(exc),
                "version": "4.5",
            }

    # ---------------------------------------------------------
    # REGISTER SCENE
    # ---------------------------------------------------------
    def register_scene(self, scene: Dict[str, Any]) -> Dict[str, Any]:
        if self.safe_mode:
            return {
                "status": "safe_mode",
                "message": "Scene manager disabled in safe-mode.",
                "version": "4.5",
            }

        name = scene.get("name")
        actions = scene.get("actions")

        if not self._validate_str(name):
            return {"status": "error", "code": "invalid_name", "version": "4.5"}

        if name in self.scenes:
            return {"status": "error", "code": "scene_exists", "version": "4.5"}

        if not self._validate_actions(actions):
            return {"status": "error", "code": "invalid_actions", "version": "4.5"}

        try:
            self.scenes[name] = scene

            if self.event_bus:
                try:
                    self.event_bus.emit("scene_registered", {"scene": scene})
                except Exception:
                    self.degraded_mode = True

            return {"status": "ok", "version": "4.5"}

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "register_failed",
                "exception": str(exc),
                "version": "4.5",
            }

    # ---------------------------------------------------------
    # LIST SCENES
    # ---------------------------------------------------------
    def list_scenes(self) -> Dict[str, Any]:
        try:
            return {
                "status": "ok",
                "scenes": list(self.scenes.keys()),
                "version": "4.5",
            }
        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "list_failed",
                "exception": str(exc),
                "version": "4.5",
            }

    # ---------------------------------------------------------
    # RUN SCENE
    # ---------------------------------------------------------
    def run_scene(self, name: str) -> Dict[str, Any]:
        if not self._validate_str(name):
            return {"status": "error", "code": "invalid_name", "version": "4.5"}

        if name not in self.scenes:
            return {"status": "error", "code": "scene_not_found", "version": "4.5"}

        if not self.state_manager:
            return {"status": "error", "code": "no_state_manager", "version": "4.5"}

        try:
            scene = self.scenes[name]
            actions = scene.get("actions", [])
            results: List[Dict[str, Any]] = []

            for act in actions:
                t = act.get("type")
                action = act.get("action")
                value = act.get("value")

                if t == "room":
                    room = act.get("room")
                    if not self._validate_str(room):
                        results.append({"status": "error", "code": "invalid_room"})
                        continue
                    res = self.state_manager.set_state_for_room(room, action, value)
                    results.append(res)

                elif t == "device":
                    device_id = act.get("device_id")
                    if not self._validate_str(device_id):
                        results.append({"status": "error", "code": "invalid_device_id"})
                        continue
                    res = self.state_manager.set_state(device_id, action, value)
                    results.append(res)

                else:
                    results.append({"status": "error", "code": "invalid_action_type"})

            if self.event_bus:
                try:
                    self.event_bus.emit("scene_executed", {
                        "scene_name": name,
                        "results": results,
                    })
                except Exception:
                    self.degraded_mode = True

            return {"status": "ok", "results": results, "version": "4.5"}

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "run_failed",
                "exception": str(exc),
                "version": "4.5",
            }

    # ---------------------------------------------------------
    # DELETE SCENE
    # ---------------------------------------------------------
    def delete_scene(self, name: str) -> Dict[str, Any]:
        if not self._validate_str(name):
            return {"status": "error", "code": "invalid_name", "version": "4.5"}

        if name not in self.scenes:
            return {"status": "error", "code": "scene_not_found", "version": "4.5"}

        try:
            del self.scenes[name]
            return {"status": "ok", "version": "4.5"}

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "delete_failed",
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
            "scenes_count": len(self.scenes),
            "version": "4.5",
        }

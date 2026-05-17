import threading
import time
import logging

log = logging.getLogger(__name__)


class AILoop:
    """
    AI Loop 4.3
    --------------------
    Features:
    - Interval rules
    - Event rules (triggered externally)
    - Autonomous scheduler
    - Overlap protection
    - Rule pausing / resuming / unregistering
    - Telemetry (last_run, error_count, running state)
    - Deterministic Runtime4 behavior
    - Self‑Repair 4.4 compatible
    """

    def __init__(self, runtime_manager):
        self.rm = runtime_manager
        self.rules = {}
        self.running = False
        self.thread = None

    # --------------------------------------------------------
    # RULE REGISTRATION
    # --------------------------------------------------------
    def register(self, rule: dict):
        rule = dict(rule)

        name = rule.get("name", f"rule_{len(self.rules)}")
        rule["name"] = name

        rule.setdefault("trigger", "interval")
        rule.setdefault("params", {})
        rule.setdefault("interval", 60)
        rule.setdefault("enabled", True)
        rule.setdefault("running", False)
        rule.setdefault("last_run", 0)
        rule.setdefault("error_count", 0)

        # Minimum interval protection
        if rule["trigger"] == "interval":
            rule["interval"] = max(1, rule["interval"])

        self.rules[name] = rule
        log.info("AI LOOP: Registered rule '%s'", name)

        return {
            "status": "success",
            "rule": name,
            "data": rule
        }

    # --------------------------------------------------------
    # RULE CONTROL
    # --------------------------------------------------------
    def unregister(self, name: str):
        if name in self.rules:
            del self.rules[name]
            log.info("AI LOOP: Unregistered rule '%s'", name)
            return {"status": "success", "rule": name}

        return {"status": "error", "rule": name, "message": "Rule not found"}

    def pause(self, name: str):
        if name in self.rules:
            self.rules[name]["enabled"] = False
            log.info("AI LOOP: Paused rule '%s'", name)
            return {"status": "success", "rule": name}

        return {"status": "error", "rule": name, "message": "Rule not found"}

    def resume(self, name: str):
        if name in self.rules:
            self.rules[name]["enabled"] = True
            log.info("AI LOOP: Resumed rule '%s'", name)
            return {"status": "success", "rule": name}

        return {"status": "error", "rule": name, "message": "Rule not found"}

    # --------------------------------------------------------
    # START / STOP LOOP
    # --------------------------------------------------------
    def start(self):
        if self.running:
            return {"status": "error", "message": "Already running"}

        self.running = True
        self.thread = threading.Thread(target=self._loop, daemon=True)
        self.thread.start()

        log.info("AI LOOP: Started")
        return {"status": "success"}

    def stop(self):
        self.running = False

        if self.thread:
            self.thread.join(timeout=2)

        log.info("AI LOOP: Stopped")
        return {"status": "success"}

    # --------------------------------------------------------
    # MAIN LOOP
    # --------------------------------------------------------
    def _loop(self):
        while self.running:
            now = time.time()

            for name, rule in list(self.rules.items()):
                if not rule["enabled"]:
                    continue

                if rule["trigger"] == "interval":
                    if now - rule["last_run"] >= rule["interval"]:
                        self._execute_rule(rule)

                # Event triggers handled externally via runtime_manager.emit_event()

            time.sleep(0.5)

    # --------------------------------------------------------
    # RULE EXECUTION
    # --------------------------------------------------------
    def _execute_rule(self, rule: dict):
        name = rule["name"]

        # Prevent overlapping execution
        if rule["running"]:
            log.warning("AI LOOP: Skipping rule '%s' (still running)", name)
            return

        rule["running"] = True
        rule["last_run"] = time.time()

        try:
            self.rm.handle_ai_task(rule["action"], rule["params"])
            log.info("AI LOOP: Executed rule '%s'", name)

        except Exception as exc:
            rule["error_count"] += 1
            log.exception("AI LOOP ERROR (%s): %s", name, exc)

        finally:
            rule["running"] = False

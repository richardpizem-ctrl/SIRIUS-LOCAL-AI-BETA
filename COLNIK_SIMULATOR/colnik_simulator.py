# COLNIK SIMULATOR 6.x – VERZIA S REQUIRE_CONFIRMATION + TIMECORE
# Bezpečný, kompatibilný, aktivuje YES/NO vo workflow_engine.py

import json
import time
import uuid
from datetime import datetime
from timecore import TimeCore   # <<< TIMECORE

# ============================================================
# Pomocné funkcie
# ============================================================

def load_proposal(path="colnik_in.json"):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return None


def save_response(response, path="colnik_out.json"):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(response, f, indent=4)


def log_event(message, path="colnik_log.txt"):
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now().isoformat()}] {message}\n")


# ============================================================
# COLNÍK ROZHODOVACIA LOGIKA
# ============================================================

class ColnikSimulator:

    def __init__(self):
        self.last_actions = {}

        # TIMECORE – PILIER 0
        self.timecore = TimeCore()
        self.timecore.runtime_start()

    # TTL kontrola
    def check_ttl(self, proposal):
        ttl = proposal.get("ttl", None)
        timestamp = proposal.get("timestamp", None)

        if ttl is None or timestamp is None:
            return True

        try:
            proposal_time = time.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ")
            proposal_epoch = time.mktime(proposal_time)
            now = time.time()

            if now - proposal_epoch > ttl:
                return False
        except:
            return True

        return True

    # Detekcia opakovania
    def detect_repetition(self, proposal):
        action = proposal.get("action")
        target = proposal.get("target")

        key = f"{action}:{target}"

        if key in self.last_actions:
            last_time = self.last_actions[key]
            if time.time() - last_time < 10:
                return True

        self.last_actions[key] = time.time()
        return False

    # ============================================================
    # HLAVNÁ ROZHODOVACIA FUNKCIA
    # ============================================================

    def evaluate(self, proposal):
        # TIMECORE – začiatok hodnotenia
        self.timecore.cycle_start()

        if proposal is None:
            self.timecore.cycle_end()
            return {
                "status": "NO_PROPOSAL",
                "message": "Autonómia neposlala žiadny návrh.",
                "cycle_time": self.timecore.cycle_delta()
            }

        action = proposal.get("action")
        target = proposal.get("target", "")
        priority = proposal.get("priority", "NORMAL")

        # TTL
        if not self.check_ttl(proposal):
            log_event("TTL EXPIRED – návrh zamietnutý")
            self.timecore.cycle_end()
            return {
                "status": "DENY",
                "reason": "TTL_EXPIRED",
                "proposal": proposal,
                "cycle_time": self.timecore.cycle_delta()
            }

        # Opakovanie
        if self.detect_repetition(proposal):
            log_event("REPETITION DETECTED – návrh zamietnutý")
            self.timecore.cycle_end()
            return {
                "status": "DENY",
                "reason": "REPETITION",
                "proposal": proposal,
                "cycle_time": self.timecore.cycle_delta()
            }

        # ============================================================
        # DANGEROUS ACTION → REQUIRE_CONFIRMATION
        # ============================================================

        # EXECUTE taskkill
        if action == "EXECUTE" and "taskkill" in target.lower():
            log_event("DANGEROUS_ACTION – vyžaduje potvrdenie")
            self.timecore.cycle_end()
            return {
                "status": "REQUIRE_CONFIRMATION",
                "proposal": proposal,
                "cycle_time": self.timecore.cycle_delta()
            }

        # DELETE systémových súborov
        if action == "DELETE" and "C:\\" in target:
            log_event("DANGEROUS_ACTION – vyžaduje potvrdenie")
            self.timecore.cycle_end()
            return {
                "status": "REQUIRE_CONFIRMATION",
                "proposal": proposal,
                "cycle_time": self.timecore.cycle_delta()
            }

        # MOVE systémových súborov
        if action == "MOVE" and "C:\\" in target:
            log_event("DANGEROUS_ACTION – vyžaduje potvrdenie")
            self.timecore.cycle_end()
            return {
                "status": "REQUIRE_CONFIRMATION",
                "proposal": proposal,
                "cycle_time": self.timecore.cycle_delta()
            }

        # ============================================================
        # SAFE ACTIONS → ALLOW
        # ============================================================

        safe_actions = [
            "OPTIMIZE_CPU",
            "OPTIMIZE_RAM",
            "CLEAN_DISK",
            "TRIAZ_FOLDER",
            "DUPLICATE_FOUND",
            "NAVIGATION_TOOL_MISSING",
            "TERMINAL_TOOL_MISSING"
        ]

        if action in safe_actions:
            log_event(f"ALLOW – bezpečná akcia: {action}")
            self.timecore.cycle_end()
            return {
                "status": "ALLOW",
                "proposal": proposal,
                "cycle_time": self.timecore.cycle_delta()
            }

        # ============================================================
        # RISKY ACTIONS → DENY
        # ============================================================

        risky_actions = ["DELETE", "WRITE", "MOVE", "EXECUTE"]

        if action in risky_actions:
            log_event(f"DENY – riziková akcia: {action}")
            self.timecore.cycle_end()
            return {
                "status": "DENY",
                "reason": "RISKY_ACTION",
                "proposal": proposal,
                "cycle_time": self.timecore.cycle_delta()
            }

        # ============================================================
        # DEFAULT → ALLOW
        # ============================================================

        log_event(f"ALLOW – default pre akciu: {action}")
        self.timecore.cycle_end()
        return {
            "status": "ALLOW",
            "proposal": proposal,
            "cycle_time": self.timecore.cycle_delta()
        }


# ============================================================
# Spúšťací bod simulátora
# ============================================================

def run_simulator():
    colnik = ColnikSimulator()

    proposal = load_proposal("colnik_in.json")
    response = colnik.evaluate(proposal)

    save_response(response, "colnik_out.json")

    print("COLNÍK SIMULÁTOR – HOTOVO")
    print(json.dumps(response, indent=4))


if __name__ == "__main__":
    run_simulator()

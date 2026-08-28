# ============================================================
# WORKFLOW ENGINE — SIRIUS 6.x (SUPER-FINAL)
# ============================================================

import os
import time
import subprocess
from datetime import datetime

# ============================================================
# TIMECORE — PILIER 0
# ============================================================

from timecore import TimeCore
timecore = TimeCore()

# ============================================================
# ENVOY MODULY
# ============================================================

from envoy.envoy_manager import EnvoyManager
from envoy.envoy_rules import EnvoyRules
from envoy.envoy_storage import EnvoyStorage
from envoy.envoy_log import EnvoyLog

# ============================================================
# KG CORE
# ============================================================

from kg.kg_core import KGCore
kg = KGCore()

# ============================================================
# TERMINAL ASSISTANT (PILIER 6)
# ============================================================

from terminal_assistant.terminal_assistant import TerminalAssistant
terminal_assistant = TerminalAssistant()

# ============================================================
# ENVOY INICIALIZÁCIA
# ============================================================

envoy_manager = EnvoyManager()
envoy_rules = EnvoyRules()
envoy_storage = EnvoyStorage()
envoy_log = EnvoyLog()


# ============================================================
# LOGOVACIA FUNKCIA COLNÍKA
# ============================================================

def colnik_log(message: str):
    """Zapisuje udalosti do colnik_log.txt."""
    log_path = "colnik_log.txt"
    timestamp = datetime.now().isoformat()
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {message}\n")


# ============================================================
# TERMINAL — RUN_COMMAND (PILIER 6)
# ============================================================

def workflow_run_command(command: str, payload: dict):
    """
    Vykonanie terminálového príkazu — iba ak je bezpečný alebo potvrdený.
    """

    timecore.cycle_start()

    category = payload.get("category", "UNKNOWN")
    requires_confirmation = payload.get("requires_confirmation", True)

    # ------------------------------------------------------------
    # 1. Zakázané príkazy → DENY
    # ------------------------------------------------------------
    if category == "FORBIDDEN":
        colnik_log(f"DENY – zakázaný príkaz: {command}")
        timecore.cycle_end()
        return {
            "status": "DENY",
            "message": f"Zakázaný príkaz: {command}",
            "cycle_time": timecore.cycle_delta()
        }

    # ------------------------------------------------------------
    # 2. Príkazy vyžadujúce potvrdenie → REQUIRE_CONFIRMATION
    # ------------------------------------------------------------
    if requires_confirmation:
        colnik_log("REQUIRE_CONFIRMATION – návrh čaká na potvrdenie")
        timecore.cycle_end()
        return {
            "status": "REQUIRE_CONFIRMATION",
            "message": "Príkaz vyžaduje potvrdenie.",
            "cycle_time": timecore.cycle_delta()
        }

    # ------------------------------------------------------------
    # 3. Bezpečné príkazy → ALLOW + vykonanie
    # ------------------------------------------------------------
    try:
        subprocess.Popen(command, shell=True)
        colnik_log(f"ALLOW – bezpečná akcia: RUN_COMMAND ({command})")

        # KG zápis
        event_id = f"terminal_run_{time.time()}"
        kg.add_entity(event_id, {
            "type": "workflow_event",
            "action": "RUN_COMMAND",
            "command": command,
            "category": category,
            "timestamp": datetime.now().isoformat(),
            "cycle_time": timecore.cycle_delta()
        })
        kg.add_relation("workflow_engine", "executed", event_id)

        timecore.cycle_end()

        return {
            "status": "OK",
            "message": f"Príkaz vykonaný: {command}",
            "cycle_time": timecore.cycle_delta()
        }

    except Exception as e:
        colnik_log(f"ERROR – príkaz zlyhal: {command}")
        timecore.cycle_end()
        return {
            "status": "ERROR",
            "message": f"Chyba pri vykonávaní príkazu: {e}",
            "cycle_time": timecore.cycle_delta()
        }


# ============================================================
# KARANTÉNA — WORKFLOW AKCIA
# ============================================================

def workflow_quarantine(target_path: str):
    """Presun súboru do ENVOY karantény."""

    timecore.cycle_start()

    if not os.path.exists(target_path):
        timecore.cycle_end()
        return {
            "status": "ERROR",
            "message": f"Súbor neexistuje: {target_path}"
        }

    rule_result = envoy_rules.evaluate_file(target_path)
    status = rule_result.get("status", "UNKNOWN")
    reason = rule_result.get("reason", "Bez dôvodu")

    if status == "SAFE":
        timecore.cycle_end()
        return {
            "status": "SAFE",
            "message": "Súbor je bezpečný."
        }

    file_name = os.path.basename(target_path)
    envoy_log.log_rule(file_name, reason)

    store_result = envoy_storage.store(target_path, reason)

    if store_result["status"] != "OK":
        timecore.cycle_end()
        return {
            "status": "ERROR",
            "message": store_result.get("message", "Neznáma chyba.")
        }

    envoy_log.log_quarantine(store_result["file"], reason)

    event_id = f"workflow_quarantine_{time.time()}"

    kg.add_entity(event_id, {
        "type": "workflow_event",
        "action": "QUARANTINE",
        "file_name": store_result["file"],
        "original_path": target_path,
        "quarantine_path": store_result["quarantine_path"],
        "reason": reason,
        "timestamp": datetime.now().isoformat(),
        "cycle_time": timecore.cycle_delta()
    })

    kg.add_relation("workflow_engine", "executed", event_id)

    timecore.cycle_end()

    return {
        "status": "QUARANTINED",
        "file": store_result["file"],
        "quarantine_path": store_result["quarantine_path"],
        "reason": reason,
        "cycle_time": timecore.cycle_delta()
    }


# ============================================================
# NAVIGÁCIA — WORKFLOW AKCIA
# ============================================================

def _safe_start_target(target: str) -> dict:
    try:
        if target.startswith("ms-settings:"):
            subprocess.Popen(["start", "", target], shell=True)
        elif target.lower().endswith((".msc", ".cpl", ".exe")):
            subprocess.Popen(["start", "", target], shell=True)
        else:
            if os.path.exists(target):
                os.startfile(target)
            else:
                return {"status": "ERROR", "message": f"Neznámy cieľ: {target}"}

        return {"status": "OK", "message": f"Navigácia spustená: {target}"}

    except Exception as e:
        return {"status": "ERROR", "message": f"Chyba pri navigácii: {e}"}


def workflow_navigate(target: str, payload: dict | None = None):
    timecore.cycle_start()

    nav_result = _safe_start_target(target)
    status = nav_result["status"]
    message = nav_result["message"]

    event_id = f"workflow_navigate_{time.time()}"

    kg.add_entity(event_id, {
        "type": "workflow_event",
        "action": "NAVIGATE",
        "target": target,
        "payload": payload or {},
        "status": status,
        "message": message,
        "timestamp": datetime.now().isoformat(),
        "cycle_time": timecore.cycle_delta()
    })

    kg.add_relation("workflow_engine", "executed", event_id)

    timecore.cycle_end()

    return {
        "status": status,
        "target": target,
        "message": message,
        "cycle_time": timecore.cycle_delta()
    }


# ============================================================
# DISPATCHER — HLAVNÝ VSTUP PRE MAIN.PY
# ============================================================

def execute_action(action: str, target: str, payload: dict | None = None):
    """Dispatcher workflow akcií."""

    if action == "QUARANTINE":
        return workflow_quarantine(target)

    if action == "NAVIGATE":
        return workflow_navigate(target, payload)

    if action == "RUN_COMMAND":
        return workflow_run_command(target, payload or {})

    if action == "FORBID_COMMAND":
        colnik_log(f"DENY – zakázaný príkaz: {target}")
        return {
            "status": "DENY",
            "message": f"Zakázaný príkaz: {target}"
        }

    return {
        "status": "UNKNOWN_ACTION",
        "action": action,
        "target": target,
        "message": "Neznáma workflow akcia."
    }

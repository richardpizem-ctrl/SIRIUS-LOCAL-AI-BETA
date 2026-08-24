# ============================================================
# WORKFLOW ENGINE — SIRIUS 6.x
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
# ENVOY INICIALIZÁCIA
# ============================================================

envoy_manager = EnvoyManager()
envoy_rules = EnvoyRules()
envoy_storage = EnvoyStorage()
envoy_log = EnvoyLog()


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

    # 1. Vyhodnotenie pravidiel
    rule_result = envoy_rules.evaluate_file(target_path)
    status = rule_result.get("status", "UNKNOWN")
    reason = rule_result.get("reason", "Bez dôvodu")

    if status == "SAFE":
        timecore.cycle_end()
        return {
            "status": "SAFE",
            "message": "Súbor je bezpečný."
        }

    # 2. Log pravidla
    file_name = os.path.basename(target_path)
    envoy_log.log_rule(file_name, reason)

    # 3. Presun do karantény
    store_result = envoy_storage.store(target_path, reason)

    if store_result["status"] != "OK":
        timecore.cycle_end()
        return {
            "status": "ERROR",
            "message": store_result.get("message", "Neznáma chyba.")
        }

    # 4. Log karantény
    envoy_log.log_quarantine(store_result["file"], reason)

    # 5. KG zápis
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
# NAVIGÁCIA — WORKFLOW AKCIA (OPTIMALIZOVANÁ)
# ============================================================

def _safe_start_target(target: str) -> dict:
    """
    Optimalizovaná navigácia:
    - podporuje explorer.exe, control.exe, *.msc, *.cpl, ms-settings:
    - univerzálne spúšťanie cez Windows shell
    """

    try:
        # ms-settings: → shell príkaz
        if target.startswith("ms-settings:"):
            subprocess.Popen(["start", "", target], shell=True)

        # .msc / .cpl / .exe → shell start
        elif target.lower().endswith((".msc", ".cpl", ".exe")):
            subprocess.Popen(["start", "", target], shell=True)

        else:
            # fallback: ak je to cesta
            if os.path.exists(target):
                os.startfile(target)
            else:
                return {
                    "status": "ERROR",
                    "message": f"Neznámy alebo neexistujúci cieľ navigácie: {target}"
                }

        return {
            "status": "OK",
            "message": f"Navigácia spustená: {target}"
        }

    except Exception as e:
        return {
            "status": "ERROR",
            "message": f"Chyba pri navigácii: {e}"
        }


def workflow_navigate(target: str, payload: dict | None = None):
    """Workflow akcia NAVIGATE — otvorenie systémových nástrojov / aplikácií."""

    timecore.cycle_start()

    # 1. Spustenie navigácie
    nav_result = _safe_start_target(target)
    status = nav_result["status"]
    message = nav_result["message"]

    # 2. KG zápis
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

    return {
        "status": "UNKNOWN_ACTION",
        "action": action,
        "target": target,
        "message": "Neznáma workflow akcia."
    }

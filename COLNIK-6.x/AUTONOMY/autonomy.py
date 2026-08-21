import time
import importlib.util
import sys
import os
import json

# === FIX PYTHON PATH (DÔLEŽITÉ!) ===
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(BASE_DIR)

# === KG MODULE ===
from kg.kg_core import KGCore
kg = KGCore()

# === TIMECORE – PILIER 0 ===
from timecore import TimeCore

# === CONFIRMATION HANDLER ===
IPC_RESPONSES = r"C:\SIRIUS_ARCHIVE\COLNIK-6.x\IPC_DATA\responses.json"
IPC_CONFIRM = r"C:\SIRIUS_ARCHIVE\COLNIK-6.x\IPC_DATA\confirm.json"

def check_confirmation():
    if not os.path.exists(IPC_RESPONSES):
        return None
    try:
        with open(IPC_RESPONSES, "r", encoding="utf-8") as f:
            data = json.load(f)
    except:
        return None

    if isinstance(data, dict):
        responses = data.get("responses", [])
    elif isinstance(data, list):
        responses = data
    else:
        return None

    if not responses:
        return None

    last = responses[-1]
    if last.get("decision") == "REQUIRE_CONFIRMATION":
        return last.get("request_id")
    return None


def send_confirmation(request_id):
    payload = {
        "request_id": request_id,
        "confirm": True
    }
    with open(IPC_CONFIRM, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)
    print(f"[CONFIRM] Request {request_id} potvrdený.")


# === LOAD MONITOR (SAFE IMPORT) ===
monitor_path = os.path.join(os.path.dirname(__file__), "..", "monitor.py")
monitor_path = os.path.abspath(monitor_path)

spec = importlib.util.spec_from_file_location("sirius_monitor_real", monitor_path)
monitor = importlib.util.module_from_spec(spec)

try:
    spec.loader.exec_module(monitor)
except Exception as e:
    print("[MONITOR] ERROR PRI NAČÍTANÍ:", e)
    raise

SystemMonitor = monitor.SystemMonitor

from analyzer import analyze
from proposer import generate_proposals

# === IPC ===
from send_to_colnik import IPCSender
from receive_responses import IPCReceiver

# === MODULES ===
from modules.navigation import Navigation
from modules.triage_folders import TriageFolders
from modules.terminal_assistant import TerminalAssistant

# === AUTONOMY GUARD ===
from guard.guard_monitor import GuardMonitor
from guard.guard_analyzer import GuardAnalyzer
from guard.guard_rules import GuardRules
from guard.guard_alerts import GuardAlerts

# === SYSTEM INFO ===
from core.system_info.system_info_main import collect_system_info

# === DETECTION MODULE (PILIER 2) ===
from modules.detection import Detection
detector = Detection()

# === COLNÍK POVOLENÉ AKCIE ===
VALID_ACTIONS = [
    "READ", "WRITE", "MOVE", "DELETE", "EXECUTE",
    "SYSTEM_CHANGE", "NAVIGATE"
]

# === COLNÍK POVOLENÉ PRIORITY ===
VALID_PRIORITIES = ["LOW", "NORMAL", "HIGH", "CRITICAL"]

# === MAPOVANIE AUTONÓMNYCH AKCIÍ NA COLNÍK ===
ACTION_MAP = {
    "OPTIMIZE_CPU": "SYSTEM_CHANGE",
    "OPTIMIZE_RAM": "SYSTEM_CHANGE",
    "CLEAN_DISK": "SYSTEM_CHANGE",
    "REPORT_CORRUPTED_FILE": "SYSTEM_CHANGE",
    "REPORT_DANGEROUS_FILE": "SYSTEM_CHANGE",
    "DELETE_EMPTY_FOLDER": "DELETE",
    "DELETE_DUPLICATE": "DELETE",
    "MOVE_TO_ARCHIVE": "MOVE",
    "REORGANIZE_FOLDER": "MOVE",
    "KILL": "EXECUTE",
    "QUARANTINE": "SYSTEM_CHANGE",
    "OPEN": "NAVIGATE"
}


def proposal_to_request(p):
    original_action = p.get("action")
    action = ACTION_MAP.get(original_action, original_action)

    if action not in VALID_ACTIONS:
        return None

    priority = p.get("priority", "NORMAL")
    if priority not in VALID_PRIORITIES:
        priority = "NORMAL"

    payload = p.get("payload", {}) or {}
    payload["subaction"] = original_action

    return {
        "request_id": p.get("proposal_id", "AUTO"),
        "origin": "AUTONOMY",
        "action": action,
        "target": p.get("target", "SYSTEM"),
        "priority": priority,
        "requires_confirmation": False,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "payload": payload
    }


class Autonomy:

    def __init__(self):
        self.monitor = SystemMonitor()

        self.nav = Navigation()
        self.triage_folders = TriageFolders()
        self.term = TerminalAssistant()

        self.sender = IPCSender()
        self.receiver = IPCReceiver()

        self.guard_monitor = GuardMonitor()
        self.guard_analyzer = GuardAnalyzer()
        self.guard_rules = GuardRules()
        self.guard_alerts = GuardAlerts()

        self.safe_processes = set()
        self.hard_stop_required = False

        self.timecore = TimeCore()
        self.timecore.runtime_start()

    def generate_real_proposals(self, analysis):
        proposals = []

        cpu_trend = analysis["trends"]["cpu"]
        ram_trend = analysis["trends"]["ram"]
        disk_trend = analysis["trends"]["disk"]

        cpu_val = analysis["system"]["cpu"]
        ram_val = analysis["system"]["ram"]
        disk_val = analysis["system"]["disk"]

        if cpu_trend == "rising" and cpu_val > 80:
            proposals.append({
                "proposal_id": "cpu-optimize",
                "action": "OPTIMIZE_CPU",
                "target": "SYSTEM",
                "payload": {"cpu": cpu_val},
                "priority": "HIGH"
            })

        if ram_trend == "rising" and ram_val > 80:
            proposals.append({
                "proposal_id": "ram-optimize",
                "action": "OPTIMIZE_RAM",
                "target": "SYSTEM",
                "payload": {"ram": ram_val},
                "priority": "NORMAL"
            })

        if disk_trend == "rising" and disk_val > 5_000_000:
            proposals.append({
                "proposal_id": "disk-clean",
                "action": "CLEAN_DISK",
                "target": "SYSTEM",
                "payload": {"disk": disk_val},
                "priority": "HIGH"
            })

        return proposals

    def cycle(self):
        self.timecore.cycle_start()
        print("[AUTONOMY] CYCLE START")

        # === SAFE MONITOR SNAPSHOT ===
        try:
            system_snapshot = self.monitor.snapshot()
        except Exception as e:
            print("[MONITOR] ERROR:", e)
            system_snapshot = {
                "system": {"cpu": 0, "ram": 0, "disk": 0},
                "processes": [],
                "issues": []
            }

        system_info = collect_system_info()

        sirius_info = system_info.get("sirius", {})
        modules = sirius_info.get("modules", {})
        configs = sirius_info.get("configs", {})

        modules["kg"] = True
        configs["kg_autosave"] = True

        kg_size = len(getattr(kg, "entities", {}))
        sirius_info["kg_size"] = kg_size
        sirius_info["status"] = "ok"

        sirius_info["modules"] = modules
        sirius_info["configs"] = configs
        system_info["sirius"] = sirius_info

        folders = system_snapshot.get("folders", {})
        if isinstance(folders, dict):
            folders["root"] = r"C:\SIRIUS_ARCHIVE\COLNIK-6.x"
            system_snapshot["folders"] = folders

        analysis = analyze(system_snapshot)
        analysis["system_info"] = system_info

        print("DEBUG ANALYSIS:", analysis)

        proposals = []
        proposals.extend(self.generate_real_proposals(analysis))
        proposals.extend(generate_proposals(analysis))

        # === TRIAGE FOLDERS ===
        root_folder = r"C:\SIRIUS_ARCHIVE\COLNIK-6.x"
        proposals.extend(self.triage_folders.propose_triage(root_folder))

        # === NAVIGATION PROPOSALS ===
        try:
            nav_props = self.nav.propose_navigation()
            if nav_props:
                proposals.extend(nav_props)
        except Exception as e:
            print("[NAVIGATION] ERROR:", e)

        # === SAFE PROCESS PRIORITY FIX ===
        safe = self.safe_processes
        adjusted = []
        for p in proposals:
            target = p.get("target")
            action = p.get("action")
            priority = p.get("priority", "NORMAL")

            if action == "KILL" and target in safe and priority == "CRITICAL":
                print(f"[AUTONOMY] SAFE proces {target} – znižujem prioritu.")
                p["priority"] = "NORMAL"

            adjusted.append(p)

        proposals = adjusted

        priority_order = {"CRITICAL": 4, "HIGH": 3, "NORMAL": 2, "LOW": 1}
        proposals.sort(key=lambda x: priority_order.get(x.get("priority", "NORMAL"), 1), reverse=True)

        guard_snapshot = self.guard_monitor.observe({
            "proposals": proposals,
            "responses": [],
            "trends": analysis["trends"],
            "system": analysis["system"],
            "system_info": system_info
        })

        guard_problems = self.guard_analyzer.analyze(guard_snapshot)
        guard_validation = self.guard_rules.validate(guard_problems)

        print("[GUARD] Problems:", guard_problems)
        print("[GUARD] Validation:", guard_validation)
        print("[GUARD] Analysis issues:", analysis.get("issues", []))

        guard_result = self.guard_alerts.handle(guard_validation)
        print("[AUTONOMY] GUARD RESULT:", guard_result)

        if guard_result == "STOP":
            print("[AUTONOMY] STOP — GUARD BLOCKED EXECUTION")
            print("[AUTONOMY] DETAIL PROBLÉMU:")
            print("  - issues:", analysis.get("issues", []))
            print("  - guard_problems:", guard_problems)
            print("  - guard_validation:", guard_validation)
            print("  - proposals:", proposals)

            danger_targets = [p.get("target") for p in proposals if p.get("action") == "KILL"]
            safe = self.safe_processes

            if any(t in safe for t in danger_targets):
                print("[AUTONOMY] SAFE problém — autonómia pokračuje.")
                self.hard_stop_required = False
                self.timecore.cycle_end()
                print(f"[TIMECORE] Autonomy cycle: {self.timecore.cycle_delta()} sec")
                return {
                    "status": "OK",
                    "snapshot": system_snapshot,
                    "analysis": analysis,
                    "proposals": proposals,
                    "responses": []
                }

            self.hard_stop_required = True
            self.timecore.cycle_end()
            print(f"[TIMECORE] Autonomy cycle: {self.timecore.cycle_delta()} sec")
            return {
                "status": "STOP",
                "snapshot": system_snapshot,
                "analysis": analysis,
                "proposals": proposals,
                "responses": []
            }

        requests = []
        for p in proposals:
            req = proposal_to_request(p)
            if req:
                requests.append(req)

                kg.add_entity(req["request_id"], {
                    "action": req["action"],
                    "target": req["target"],
                    "priority": req["priority"]
                })
                kg.add_relation(req["request_id"], "targets", req["target"])

        self.sender.send(requests)
        responses = self.receiver.receive()

        confirm_id = check_confirmation()
        if confirm_id:
            send_confirmation(confirm_id)

        print("=== AUTONOMY 6.x CYCLE ===")
        print("PROPOSALS:", proposals)
        print("REQUESTS:", requests)
        print("RESPONSES:", responses)
        print("==========================")

        self.timecore.cycle_end()
        print(f"[TIMECORE] Autonomy cycle: {self.timecore.cycle_delta()} sec")

        return {
            "status": "OK",
            "snapshot": system_snapshot,
            "analysis": analysis,
            "proposals": proposals,
            "responses": responses
        }


if __name__ == "__main__":
    auto = Autonomy()

    while True:
        result = auto.cycle()

        if isinstance(result, dict) and result.get("status") == "STOP" and auto.hard_stop_required:
            print("[MAIN] AUTONÓMIA ZASTAVENÁ — ČLOVEK MUSÍ OPRAVIŤ PROBLÉM")
            print("[MAIN] DETAIL PROBLÉMU PRE ČLOVEKA:")
            print("  - issues:", result.get("analysis", {}).get("issues", []))
            print("  - proposals:", result.get("proposals", []))
            print("  - snapshot.system:", result.get("snapshot", {}).get("system", {}))
            break

        if isinstance(result, dict) and result.get("status") == "STOP":
            print("[MAIN] Autonómia zastavená – vykonávam opravu problému...")

            analysis = result.get("analysis", {})
            issues = analysis.get("issues", [])

            suspicious_processes = [
                i for i in issues
                if i.get("type") == "process_danger" and i.get("process")
            ]

            for proc in suspicious_processes:
                pname = proc.get("process")
                print(f"[MAIN] Pokus o kill podozrivého procesu: {pname}")
                try:
                    os.system(f"taskkill /IM {pname} /F")
                    print(f"[MAIN] taskkill /IM {pname} /F vykonaný.")
                except Exception as e:
                    print(f"[MAIN] Kill procesu {pname} zlyhal: {e}")

                print(f"[MAIN] Proces {pname} sa nedá odstrániť – označujem ako SAFE.")
                auto.safe_processes.add(pname)

            auto.guard_analyzer.proposal_history = {}
            auto.guard_analyzer.target_history = {}
            auto.guard_analyzer.subaction_history = {}
            print("[MAIN] GuardAnalyzer história resetovaná – autonómia môže pokračovať.")

            auto.timecore.pause_start()
            time.sleep(1)
            auto.timecore.pause_end()
            print(f"[TIMECORE] Pause: {auto.timecore.pause_duration()} sec")
            continue

        auto.timecore.pause_start()
        time.sleep(1)
        auto.timecore.pause_end()
        print(f"[TIMECORE] Pause: {auto.timecore.pause_duration()} sec")

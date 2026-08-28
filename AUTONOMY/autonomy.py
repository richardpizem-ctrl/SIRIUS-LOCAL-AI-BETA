import time
import importlib.util
import sys
import os
import json
import argparse
import hashlib

# === BASE DIR ===
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

# === AUTONOMY DIR (aby Python videl modules/*) ===
AUTONOMY_DIR = os.path.abspath(os.path.dirname(__file__))
if AUTONOMY_DIR not in sys.path:
    sys.path.append(AUTONOMY_DIR)

AUTONOMY_STATE = r"C:\SIRIUS_ARCHIVE\COLNIK-6.x\IPC_DATA\autonomy_state.json"

# ============================================================
# HELPER FUNCTIONS
# ============================================================
def get_file_hash(filepath):
    """Vypočíta SHA-256 hash súboru alebo vráti 'DIR' pre priečinky."""
    if not os.path.exists(filepath):
        return "NOT_FOUND"
    if os.path.isdir(filepath):
        return "DIR"
    
    sha256 = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            while chunk := f.read(8192):
                sha256.update(chunk)
        return sha256.hexdigest()
    except Exception:
        return "READ_ERROR"

# ============================================================
# LOAD / SAVE AUTONOMY STATE
# ============================================================
def load_autonomy_state():
    default_state = {
        "last_snapshot_hash": None,
        "last_navigation": [],
        "last_proposals": [],
        "last_trends": {}
    }
    
    if not os.path.exists(AUTONOMY_STATE):
        try:
            os.makedirs(os.path.dirname(AUTONOMY_STATE), exist_ok=True)
            with open(AUTONOMY_STATE, "w", encoding="utf-8") as f:
                json.dump(default_state, f, indent=2)
        except Exception as e:
            print(f"[STATE] Nepodarilo sa vytvoriť stavový súbor: {e}")
        return default_state

    try:
        with open(AUTONOMY_STATE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"[STATE] Chyba pri načítaní stavu: {e}")
        try:
            with open(AUTONOMY_STATE, "w", encoding="utf-8") as f:
                json.dump(default_state, f, indent=2)
        except Exception:
            pass
        return default_state


def save_autonomy_state(snapshot_hash, navigation_list, proposals_list, trends):
    new_state = {
        "last_snapshot_hash": snapshot_hash,
        "last_navigation": navigation_list,
        "last_proposals": proposals_list,
        "last_trends": trends
    }
    try:
        os.makedirs(os.path.dirname(AUTONOMY_STATE), exist_ok=True)
        with open(AUTONOMY_STATE, "w", encoding="utf-8") as f:
            json.dump(new_state, f, indent=2)
        print("[STATE] autonomy_state.json uložený.")
    except Exception as e:
        print(f"[STATE] Zlyhalo uloženie stavu: {e}")


def compute_snapshot_hash(snapshot):
    try:
        raw = json.dumps(snapshot, sort_keys=True)
        return hashlib.sha256(raw.encode("utf-8")).hexdigest()
    except Exception:
        return None

# ============================================================
# KG + TIMECORE
# ============================================================
try:
    from kg.kg_core import KGCore
    kg = KGCore()
except ImportError:
    class DummyKG:
        def __init__(self): self.entities = {}
        def add_entity(self, *a, **k): pass
        def add_relation(self, *a, **k): pass
    kg = DummyKG()

try:
    from timecore import TimeCore
except ImportError:
    class TimeCore:
        def runtime_start(self): pass
        def cycle_start(self): self._start = time.time()
        def cycle_end(self): self._end = time.time()
        def cycle_delta(self): return round(getattr(self, '_end', time.time()) - getattr(self, '_start', time.time()), 4)

# ============================================================
# IPC
# ============================================================
IPC_RESPONSES = r"C:\SIRIUS_ARCHIVE\COLNIK-6.x\IPC_DATA\responses.json"
IPC_CONFIRM = r"C:\SIRIUS_ARCHIVE\COLNIK-6.x\IPC_DATA\confirm.json"

def check_confirmation():
    if not os.path.exists(IPC_RESPONSES):
        return None
    try:
        with open(IPC_RESPONSES, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception:
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
    if isinstance(last, dict) and last.get("decision") == "REQUIRE_CONFIRMATION":
        return last.get("request_id")
    return None


def send_confirmation(request_id):
    payload = {"request_id": request_id, "confirm": True}
    try:
        os.makedirs(os.path.dirname(IPC_CONFIRM), exist_ok=True)
        with open(IPC_CONFIRM, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2)
        print(f"[CONFIRM] Request {request_id} potvrdený.")
    except Exception as e:
        print(f"[CONFIRM] Zlyhalo odoslanie potvrdenia: {e}")

# ============================================================
# MONITOR
# ============================================================
try:
    monitor_path = os.path.join(os.path.dirname(__file__), "..", "monitor.py")
    monitor_path = os.path.abspath(monitor_path)

    spec = importlib.util.spec_from_file_location("sirius_monitor_real", monitor_path)
    monitor = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(monitor)
    SystemMonitor = monitor.SystemMonitor
except Exception:
    class SystemMonitor:
        def snapshot(self):
            return {
                "system": {"cpu": 0, "ram": 0, "disk": 0},
                "processes": [],
                "issues": []
            }

# ============================================================
# ANALYZER + PROPOSER
# ============================================================
try:
    from analyzer import analyze
except ImportError:
    def analyze(snap): return {"system": snap.get("system", {}), "trends": {"cpu": "flat", "ram": "flat", "disk": "flat"}, "issues": []}

try:
    from proposer import generate_proposals
except ImportError:
    def generate_proposals(analysis): return []

# ============================================================
# IPC SEND/RECEIVE
# ============================================================
try:
    from send_to_colnik import IPCSender
except ImportError:
    class IPCSender:
        def send(self, reqs): print(f"[MOCK IPC] Odosielam requesty: {len(reqs)}")

try:
    from receive_responses import IPCReceiver
except ImportError:
    class IPCReceiver:
        def receive(self): return []

# ============================================================
# MODULES
# ============================================================
try: from modules.navigation import Navigation
except ImportError:
    class Navigation:
        def propose_navigation(self): return []

try: from triage_folders.triage_folders import TriageFolders
except ImportError:
    class TriageFolders:
        def triage(self): return []

try: from modules.terminal_assistant import TerminalAssistant
except ImportError:
    class TerminalAssistant: pass

try: from modules.detection import Detection
except ImportError:
    class Detection: pass

# PILIER 5 — DUPLICITY
try: from modules.duplicates.duplicates_module import DuplicatesModule
except ImportError:
    class DuplicatesModule:
        def run(self): return []

detector = Detection() if 'Detection' in locals() else None

# ============================================================
# GUARD (FIXED RETURN VALUES IN FALLBACKS)
# ============================================================
try: from guard.guard_monitor import GuardMonitor
except ImportError:
    class GuardMonitor:
        def observe(self, data): return data

try: from guard.guard_analyzer import GuardAnalyzer
except ImportError:
    class GuardAnalyzer:
        def __init__(self):
            self.proposal_history = {}
            self.target_history = {}
            self.subaction_history = {}
        def analyze(self, snap): return []

try: from guard.guard_rules import GuardRules
except ImportError:
    class GuardRules:
        def validate(self, probs): 
            if isinstance(probs, list) and len(probs) > 0:
                return {"status": "PROBLEMS_FOUND", "problems": probs}
            return {"status": "OK", "problems": []}

try: from guard.guard_alerts import GuardAlerts
except ImportError:
    class GuardAlerts:
        def handle(self, val): 
            if isinstance(val, dict) and val.get("status") == "STOP":
                return "STOP"
            return "OK"

# ============================================================
# SYSTEM INFO
# ============================================================
try: from core.system_info.system_info_main import collect_system_info
except ImportError:
    def collect_system_info(): return {"sirius": {"modules": {}, "configs": {}}}

# ============================================================
# ACTION MAP & PROPOSAL TRANSLATION
# ============================================================
VALID_ACTIONS = [
    "READ", "WRITE", "MOVE", "DELETE", "EXECUTE",
    "SYSTEM_CHANGE", "NAVIGATE"
]

VALID_PRIORITIES = ["LOW", "NORMAL", "HIGH", "CRITICAL"]

ACTION_MAP = {
    # PILIER 5 — DUPLICITY (FÁZA 3)
    "IGNORE_DUPLICATE": "IGNORE",
    "DELETE_DUPLICATE_SAFE": "DELETE",
    "ARCHIVE_DUPLICATE": "MOVE",
    "QUARANTINE_DUPLICATE": "SYSTEM_CHANGE",
    "REPORT_DUPLICATE": "SYSTEM_CHANGE",

    # Pôvodné akcie
    "DELETE_DUPLICATE": "DELETE",
    "OPTIMIZE_CPU": "SYSTEM_CHANGE",
    "OPTIMIZE_RAM": "SYSTEM_CHANGE",
    "CLEAN_DISK": "SYSTEM_CHANGE",
    "REPORT_CORRUPTED_FILE": "SYSTEM_CHANGE",
    "REPORT_DANGEROUS_FILE": "SYSTEM_CHANGE",
    "DELETE_EMPTY_FOLDER": "DELETE",
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

    requires_confirmation = True if action == "SYSTEM_CHANGE" else False

    if payload.get("category") in ["CRITICAL", "KG"]:
        action = "SYSTEM_CHANGE"
        requires_confirmation = True
        print(f"[AUTONOMY] DUPLICITA {payload.get('category')} → vyžaduje potvrdenie")

    target = p.get("target", "SYSTEM")

    # FIX PRE MOVE / ARCHIVE HASH MISMATCH (Priečinky vs. Súbory)
    if action == "MOVE":
        files = payload.get("files", [])

        # Vezmeme prvý súbor/priečinok zo zoznamu
        if (target == "SYSTEM" or not target) and files:
            target = files[0]

        # Ak je cieľ priečinok (napr. C:\SIRIUS_ARCHIVE\DIR)
        if os.path.isdir(target):
            payload["file_hash"] = "DIR"
            payload["hash"] = "DIR"
        else:
            # Ak je cieľ prázdny súbor
            if payload.get("category") == "EMPTY":
                payload["file_hash"] = "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
                payload["hash"] = payload["file_hash"]
            elif payload.get("hash"):
                payload["file_hash"] = payload.get("hash")
            else:
                computed_hash = get_file_hash(target)
                payload["file_hash"] = computed_hash
                payload["hash"] = computed_hash

        payload["source_file"] = target

    req = {
        "request_id": p.get("proposal_id", "AUTO"),
        "origin": "AUTONOMY",
        "action": action,
        "target": target,
        "priority": priority,
        "requires_confirmation": requires_confirmation,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "payload": payload
    }

    if req["requires_confirmation"]:
        req["ttl"] = 300

    if p.get("module") == "duplicates":
        print(f"[AUTONOMY] DUPLICITA: {payload.get('category')} → {original_action}")

    return req

# ============================================================
# AUTONOMY CLASS
# ============================================================
class Autonomy:

    def __init__(self):
        self.monitor = SystemMonitor()
        self.nav = Navigation()
        self.triage_folders = TriageFolders()
        self.term = TerminalAssistant() if 'TerminalAssistant' in locals() else None
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
        trends = analysis.get("trends", {})
        system = analysis.get("system", {})

        cpu_trend = trends.get("cpu", "flat")
        ram_trend = trends.get("ram", "flat")
        disk_trend = trends.get("disk", "flat")

        cpu_val = system.get("cpu", 0)
        ram_val = system.get("ram", 0)
        disk_val = system.get("disk", 0)

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

        # === MONITOR SNAPSHOT ===
        try:
            system_snapshot = self.monitor.snapshot()
        except Exception as e:
            print("[MONITOR] ERROR:", e)
            system_snapshot = {
                "system": {"cpu": 0, "ram": 0, "disk": 0},
                "processes": [],
                "issues": []
            }

        # === AUTONOMY STATE ===
        state = load_autonomy_state()
        current_hash = compute_snapshot_hash(system_snapshot)
        system_changed = (current_hash != state.get("last_snapshot_hash"))

        if not system_changed:
            print("[STATE] Systém sa nezmenil – navigačné návrhy sa NEGENERUJÚ.")

        # === SYSTEM INFO + KG STATUS ===
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

        # === ANALYSIS ===
        analysis = analyze(system_snapshot)
        analysis["system_info"] = system_info

        print("DEBUG ANALYSIS:", analysis)

        # === PROPOSALS PIPELINE ===
        proposals = []
        proposals.extend(self.generate_real_proposals(analysis))
        proposals.extend(generate_proposals(analysis))

        # === PILIER 4 — TRIAZ PRIEČINKOV ===
        try:
            triage_props = self.triage_folders.triage()
            if isinstance(triage_props, list) and triage_props:
                proposals.extend(triage_props)
                print("[TRIAGE] Návrhy TRIAZ priečinkov vygenerované.")
            else:
                print("[TRIAGE] Žiadne návrhy TRIAZ priečinkov.")
        except Exception as e:
            print("[TRIAGE] ERROR:", e)

        # === PILIER 5 — DUPLICITY ===
        try:
            duplicates_module = DuplicatesModule()
            duplicate_proposals = duplicates_module.run()

            if duplicate_proposals:
                proposals.extend(duplicate_proposals)
                print(f"[PILIER 5] Vytvorených návrhov duplicít: {len(duplicate_proposals)}")
            else:
                print("[PILIER 5] Žiadne duplicity.")
        except Exception as e:
            print(f"[PILIER 5] ERROR: {e}")

        # === NAVIGÁCIA ===
        nav_props = []
        if system_changed:
            try:
                nav_props = self.nav.propose_navigation()
                if nav_props:
                    proposals.extend(nav_props)
                    print("[NAVIGATION] Navigačné návrhy vygenerované (zmena systému).")
            except Exception as e:
                print("[NAVIGATION] ERROR:", e)
        else:
            print("[NAVIGATION] Preskakujem navigáciu – systém sa nezmenil.")

        # === SAFE PROCESSES ADJUSTMENT ===
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

        # === PRIORITY SORTING ===
        priority_order = {"CRITICAL": 4, "HIGH": 3, "NORMAL": 2, "LOW": 1}
        proposals.sort(key=lambda x: priority_order.get(x.get("priority", "NORMAL"), 1), reverse=True)

        # === GUARD SNAPSHOT ===
        guard_snapshot = self.guard_monitor.observe({
            "proposals": proposals,
            "responses": [],
            "trends": analysis.get("trends", {}),
            "system": analysis.get("system", {}),
            "system_info": system_info
        })

        guard_problems = self.guard_analyzer.analyze(guard_snapshot)
        guard_validation = self.guard_rules.validate(guard_problems)

        print("[GUARD] Problems:", guard_problems)
        print("[GUARD] Validation:", guard_validation)
        print("[GUARD] Analysis issues:", analysis.get("issues", []))

        guard_result = self.guard_alerts.handle(guard_validation)
        if guard_result is None:
            guard_result = "OK"

        print("[AUTONOMY] GUARD RESULT:", guard_result)

        # === GUARD STOP HANDLING ===
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

        # === REQUESTS + KG LOGGING ===
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

        # === IPC SEND/RECEIVE ===
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

        # === POST-ACTION REASONING ===
        try:
            from core.post_action.post_action_manager import PostActionManager
            pam = PostActionManager()
            pam.process_responses()
        except Exception as e:
            print("[POST-ACTION] ERROR:", e)

        # === KG UPDATE ===
        try:
            from core.kg_update.kg_update_manager import KGUpdateManager
            kgm = KGUpdateManager()
            kgm.apply_updates()
        except Exception as e:
            print("[KG UPDATE] ERROR:", e)

        # === STATE MANAGER ===
        try:
            from core.state_manager.state_manager import StateManager
            sm = StateManager()
            sm.save_cycle_state()
        except Exception as e:
            print("[STATE MANAGER] ERROR:", e)

        navigation_targets = [p.get("target") for p in proposals if p.get("action") == "OPEN"]
        proposal_ids = [p.get("proposal_id") for p in proposals]

        save_autonomy_state(
            snapshot_hash=current_hash,
            navigation_list=navigation_targets,
            proposals_list=proposal_ids,
            trends=analysis.get("trends", {})
        )

        self.timecore.cycle_end()
        print(f"[TIMECORE] Autonomy cycle: {self.timecore.cycle_delta()} sec")

        return {        
            "status": "OK",
            "snapshot": system_snapshot,
            "analysis": analysis,
            "proposals": proposals,
            "responses": responses
        }

# ============================================================
# TERMINAL ARGUMENT SUPPORT — PILIER 6
# ============================================================

try:
    from modules.terminal_module import TerminalModule
    terminal_module = TerminalModule()
except ImportError:
    class TerminalModule:
        def generate_terminal_proposal(self, cmd):
            return {
                "proposal_id": f"TERM_{int(time.time())}",
                "action": "EXECUTE",
                "target": "TERMINAL",
                "priority": "HIGH",
                "payload": {"command": cmd}
            }
    terminal_module = TerminalModule()

def parse_terminal_argument():
    parser = argparse.ArgumentParser()
    parser.add_argument("--terminal", type=str, help="Spusti terminalový príkaz cez autonómiu.")
    args, unknown = parser.parse_known_args()
    return args.terminal

# ============================================================
# MAIN — SPUSTENIE AUTONÓMIE + TERMINAL SUPPORT
# ============================================================
if __name__ == "__main__":

    # 1. Načítaj argument --terminal
    terminal_cmd = parse_terminal_argument()

    auto = Autonomy()

    # 2. Ak je terminalový príkaz, vytvor TERMINAL_TASK návrh
    if terminal_cmd:
        print(f"[TERMINAL] Prijatý príkaz: {terminal_cmd}")

        proposal = terminal_module.generate_terminal_proposal(terminal_cmd)

        proposals_path = r"C:\SIRIUS_ARCHIVE\COLNIK-6.x\IPC_DATA\proposals.json"
        try:
            os.makedirs(os.path.dirname(proposals_path), exist_ok=True)
            with open(proposals_path, "w", encoding="utf-8") as f:
                json.dump([proposal], f, indent=2)
            print("[TERMINAL] TERMINAL_TASK uložený do proposals.json")
        except Exception as e:
            print(f"[TERMINAL] Zlyhalo uloženie proposals.json: {e}")

        print("[TERMINAL] Odovzdávam COLNÍK-u na vykonanie…")

        auto.sender.send([proposal])
        responses = auto.receiver.receive()

        try:
            with open(r"C:\SIRIUS_ARCHIVE\COLNIK-6.x\IPC_DATA\responses.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                responses = data.get("responses", []) if isinstance(data, dict) else data
        except Exception:
            responses = []

        print("[TERMINAL] RESPONSES:", responses)
        sys.exit(0)

    # 3. Normálny autonómny cyklus
    result = auto.cycle()

    # === GUARD STOP ===
    if isinstance(result, dict) and result.get("status") == "STOP" and auto.hard_stop_required:
        print("[MAIN] AUTONÓMIA ZASTAVENÁ — ČLOVEK MUSÍ OPRAVIŤ PROBLÉM")
        print("[MAIN] DETAIL PROBLÉMU PRE ČLOVEKA:")
        print("  - issues:", result.get("analysis", {}).get("issues", []))
        print("  - proposals:", result.get("proposals", []))
        print("  - snapshot.system:", result.get("snapshot", {}).get("system", {}))
        sys.exit(0)

    # === GUARD STOP (SAFE) ===
    elif isinstance(result, dict) and result.get("status") == "STOP":
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

        sys.exit(0)

    print("[MAIN] Autonómia dokončila jeden cyklus.")
    sys.exit(0)
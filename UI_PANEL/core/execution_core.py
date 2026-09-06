import json
import os
import time
from typing import Any, Dict, List

# Dispatcher import
from dispatcher import Dispatcher

# Panel imports
from duplicates_panel import DuplicatesPanel
from triage_panel import TriagePanel
from navigation_panel import NavigationPanel
from terminal_panel import TerminalPanel  # ← PRIDANÉ

# Absolútna cesta na responses.json z COLNÍKA
RESPONSES_PATH = r"C:\SIRIUS_ARCHIVE\COLNIK-6.x\IPC_DATA\responses.json"

class ExecutionCore:
    """
    UI PANEL – EXECUTION CORE
    - Načíta responses.json
    - Zobrazí návrhy/requests
    - Čaká na potvrdenie používateľa
    - Vykoná akciu cez správny panel
    - Zapíše výsledok do logu (lokálne)
    """

    def __init__(self, responses_path: str = RESPONSES_PATH) -> None:
        self.responses_path = responses_path
        self.requests: List[Dict[str, Any]] = []
        self.dispatcher = Dispatcher()

        # Inicializácia panelov
        self.duplicates_panel = DuplicatesPanel()
        self.triage_panel = TriagePanel()
        self.navigation_panel = NavigationPanel()
        self.terminal_panel = TerminalPanel()  # ← PRIDANÉ

    def load_responses(self) -> None:
        """Načíta responses.json z COLNÍKA."""
        if not os.path.exists(self.responses_path):
            print(f"[EXECUTION_CORE] responses.json neexistuje: {self.responses_path}")
            self.requests = []
            return

        try:
            with open(self.responses_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            print(f"[EXECUTION_CORE] Chyba pri čítaní responses.json: {e}")
            self.requests = []
            return

        if isinstance(data, dict) and "REQUESTS" in data:
            self.requests = data["REQUESTS"]
        elif isinstance(data, list):
            self.requests = data
        else:
            print("[EXECUTION_CORE] Neznáma štruktúra responses.json")
            self.requests = []

        print(f"[EXECUTION_CORE] Načítaných requests: {len(self.requests)}")

    def list_requests(self) -> None:
        """Vypíše všetky requests v jednoduchom texte (do konzoly)."""
        if not self.requests:
            print("[EXECUTION_CORE] Žiadne requests na spracovanie.")
            return

        print("\n=== UI PANEL – PENDING REQUESTS ===")
        for idx, req in enumerate(self.requests, start=1):
            rid = req.get("request_id", "UNKNOWN_ID")
            origin = req.get("origin", "UNKNOWN_ORIGIN")
            action = req.get("action", "UNKNOWN_ACTION")
            target = req.get("target", "UNKNOWN_TARGET")
            priority = req.get("priority", "UNKNOWN_PRIORITY")
            requires_confirmation = req.get("requires_confirmation", False)

            print(f"{idx}. [{rid}]")
            print(f"   Origin:   {origin}")
            print(f"   Action:   {action}")
            print(f"   Target:   {target}")
            print(f"   Priority: {priority}")
            print(f"   Confirm:  {requires_confirmation}")
            print("")

    def confirm_and_execute(self) -> None:
        """Interaktívny loop."""
        if not self.requests:
            print("[EXECUTION_CORE] Žiadne requests na spracovanie.")
            return

        while True:
            self.list_requests()
            choice = input("[EXECUTION_CORE] Zadaj číslo requestu na vykonanie (ENTER = koniec): ").strip()
            if choice == "":
                print("[EXECUTION_CORE] Končím execution loop.")
                break

            try:
                idx = int(choice) - 1
            except ValueError:
                print("[EXECUTION_CORE] Neplatný vstup.")
                continue

            if idx < 0 or idx >= len(self.requests):
                print("[EXECUTION_CORE] Index mimo rozsahu.")
                continue

            req = self.requests[idx]
            requires_confirmation = req.get("requires_confirmation", False)

            print("\n=== DETAIL REQUESTU ===")
            print(json.dumps(req, indent=2, ensure_ascii=False))
            print("")

            if requires_confirmation:
                confirm = input("[EXECUTION_CORE] Potvrdiť vykonanie? (yes/no): ").strip().lower()
                if confirm not in ("yes", "y"):
                    print("[EXECUTION_CORE] Vykonanie zrušené používateľom.")
                    continue

            self.execute_request(req)

    def execute_request(self, req: Dict[str, Any]) -> Dict[str, Any]:
        """Vykoná request cez správny panel a vráti výsledok."""
        rid = req.get("request_id", "UNKNOWN_ID")
        action = req.get("action", "UNKNOWN_ACTION")
        target = req.get("target", "UNKNOWN_TARGET")
        payload = req.get("payload", {})

        print(f"[EXECUTION_CORE] Vykonávam request: {rid}")
        print(f"  Action: {action}")
        print(f"  Target: {target}")
        print(f"  Payload: {payload}")

        # DISPATCHER
        module = self.dispatcher.dispatch(req)
        print(f"[EXECUTION_CORE] Dispatcher vybral modul: {module}")

        # ROUTING DO PANELU
        if module == "duplicates":
            result = self.duplicates_panel.handle(req)

        elif module == "triage":
            result = self.triage_panel.handle(req)

        elif module == "navigation":
            result = self.navigation_panel.handle(req)

        elif module == "terminal":
            result = self.terminal_panel.handle(req)

        else:
            print(f"[EXECUTION_CORE] Modul '{module}' zatiaľ nie je implementovaný.")
            result = {
                "request_id": rid,
                "success": False,
                "module": module,
                "action": action,
                "target": target
            }

        # Log výsledku
        self.log_result(result, success=result.get("success", False))

        # 🔥 DÔLEŽITÉ: VRÁTIŤ VÝSLEDOK DO UI / CALLERA
        return result

    def log_result(self, result: Dict[str, Any], success: bool) -> None:
        """Zapíše výsledok vykonania do lokálneho logu UI PANELU."""
        log_path = os.path.join(os.path.dirname(__file__), "ui_panel_log.json")
        entry = {
            "request_id": result.get("request_id", "UNKNOWN_ID"),
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "success": success,
            "module": result.get("module", "unknown"),
            "action": result.get("action", "UNKNOWN_ACTION"),
            "target": result.get("target", "UNKNOWN_TARGET"),
        }

        try:
            if os.path.exists(log_path):
                with open(log_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                if not isinstance(data, list):
                    data = []
            else:
                data = []

            data.append(entry)

            with open(log_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)

            print(f"[EXECUTION_CORE] Výsledok requestu uložený do {log_path}")

        except Exception as e:
            print(f"[EXECUTION_CORE] Chyba pri zápise logu: {e}")


def main() -> None:
    core = ExecutionCore()
    core.load_responses()
    core.confirm_and_execute()


if __name__ == "__main__":
    main()

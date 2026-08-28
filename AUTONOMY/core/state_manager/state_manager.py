import os
import json

AUTONOMY_STATE = r"C:\SIRIUS_ARCHIVE\COLNIK-6.x\IPC_DATA\autonomy_state.json"
STATE_LOG = r"C:\SIRIUS_ARCHIVE\COLNIK-6.x\IPC_DATA\state_manager_log.json"


class StateManager:

    def __init__(self):
        pass

    def _load_state(self):
        if not os.path.exists(AUTONOMY_STATE):
            return {}

        try:
            with open(AUTONOMY_STATE, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return {}

    def _save_state(self, state):
        try:
            with open(AUTONOMY_STATE, "w", encoding="utf-8") as f:
                json.dump(state, f, indent=2)
            print("[STATE MANAGER] autonomy_state.json uložený.")
        except Exception as e:
            print("[STATE MANAGER] ERROR pri ukladaní stavu:", e)

    def _save_log(self, log):
        try:
            with open(STATE_LOG, "w", encoding="utf-8") as f:
                json.dump(log, f, indent=2)
        except Exception as e:
            print("[STATE MANAGER] ERROR pri ukladaní logu:", e)

    def save_cycle_state(self):
        print("[STATE MANAGER] Ukladám stav autonómie...")

        state = self._load_state()

        log_entry = {
            "last_snapshot_hash": state.get("last_snapshot_hash"),
            "last_navigation": state.get("last_navigation", []),
            "last_proposals": state.get("last_proposals", []),
            "last_trends": state.get("last_trends", {})
        }

        self._save_log(log_entry)
        print("[STATE MANAGER] Log uložený.")

        self._save_state(state)
        print("[STATE MANAGER] Stav autonómie uložený.")

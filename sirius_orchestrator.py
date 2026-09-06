import sys
import time
import traceback
import json

# ============================================================
# FIXED PATHS — JEDINÁ SPRÁVNA VERZIA
# ============================================================

sys.path.append("C:/SIRIUS_ARCHIVE/SIRIUS-LOCAL-AI-5.6.2/COLNIK-6.x")
sys.path.append("C:/SIRIUS_ARCHIVE/SIRIUS-LOCAL-AI-5.6.2/COLNIK-6.x/COLNIK")
sys.path.append("C:/SIRIUS_ARCHIVE/SIRIUS-LOCAL-AI-5.6.2/COLNIK-6.x/AUTONOMY")
sys.path.append("C:/SIRIUS_ARCHIVE/SIRIUS-LOCAL-AI-5.6.2/COLNIK-6.x/EXECUTE")
sys.path.append("C:/SIRIUS_ARCHIVE/SIRIUS-LOCAL-AI-5.6.2/UI_PANEL/core")

from runtime5.runtime_core_5 import RuntimeCore
from colnik_manager import Colnik
from autonomy import Autonomy, proposal_to_request
from executor import Executor
from panel_api import PanelAPI


class SiriusOrchestrator:

    def __init__(self):
        print("[ORCH] Initializing Sirius Orchestrator 6.x")

        self.runtime = RuntimeCore()
        self.colnik = Colnik()
        self.autonomy = Autonomy()
        self.executor = Executor()
        self.ui = PanelAPI()

        self.state = {
            "last_input": None,
            "last_runtime_output": None,
            "last_autonomy_output": None,
            "last_colnik_output": None,
            "last_executor_output": None
        }

        print("[ORCH] Initialization complete.")

    def run(self):
        print("[ORCH] Starting main loop...")

        while True:
            try:
                user_input = self.ui.get_user_input()

                if not user_input:
                    time.sleep(0.1)
                    continue

                self.state["last_input"] = user_input

                # PRIAME JSON REQUESTY
                if user_input.strip().startswith("{"):
                    try:
                        req = json.loads(user_input)
                        colnik_out = self.colnik.process(req)
                        exec_out = self.executor.execute(colnik_out)
                        self.ui.update(exec_out)
                        continue
                    except Exception as e:
                        self.ui.show_error(f"JSON ERROR: {e}")
                        continue

                # STEP 1 — RUNTIME
                runtime_out = self.runtime.process({"input": user_input})
                self.state["last_runtime_output"] = runtime_out

                # STEP 2 — AUTONOMY
                autonomy_out = self.autonomy.cycle()
                self.state["last_autonomy_output"] = autonomy_out

                # STEP 3 — PROPOSALS → REQUESTS
                proposals = autonomy_out.get("proposals", [])

                if not proposals:
                    print("[ORCH] Autonómia nevytvorila žiadne PROPOSALS.")
                    self.ui.update({"status": "SKIPPED", "reason": "No proposals"})
                    continue

                requests = []
                for p in proposals:
                    req = proposal_to_request(p)
                    if req:
                        requests.append(req)

                if not requests:
                    print("[ORCH] Žiadne validné REQUESTS po preklade z proposals.")
                    self.ui.update({"status": "SKIPPED", "reason": "No valid requests"})
                    continue

                # STEP 4 — COLNÍK + EXECUTOR
                for req in requests:
                    colnik_out = self.colnik.process(req)
                    exec_out = self.executor.execute(colnik_out)
                    self.ui.update(exec_out)

            except KeyboardInterrupt:
                print("[ORCH] Shutdown requested.")
                break

            except Exception as e:
                print("[ORCH] ERROR:", e)
                traceback.print_exc()
                self.ui.show_error(str(e))

        print("[ORCH] Main loop terminated.")


if __name__ == "__main__":
    SiriusOrchestrator().run()

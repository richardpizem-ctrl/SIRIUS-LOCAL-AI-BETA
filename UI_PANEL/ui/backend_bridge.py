import json
import sys
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

# ============================================
#  PRIDÁME CESTY K core/ AJ panels/
# ============================================

CURRENT_DIR = os.path.dirname(__file__)                 # ...\UI_PANEL\ui
UIPANEL_DIR = os.path.dirname(CURRENT_DIR)              # ...\UI_PANEL
CORE_DIR = os.path.join(UIPANEL_DIR, "core")            # ...\UI_PANEL\core
PANELS_DIR = os.path.join(UIPANEL_DIR, "panels")        # ...\UI_PANEL\panels

sys.path.append(CORE_DIR)
sys.path.append(PANELS_DIR)

from execution_core import ExecutionCore

core = ExecutionCore()

# ============================================
#  GLOBAL SERVER INSTANCE (pre shutdown)
# ============================================
httpd = None


class BridgeHandler(BaseHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    # ============================================
    #  SHUTDOWN ENDPOINT
    # ============================================
    def do_GET(self):
        global httpd

        if self.path == "/shutdown":
            self._set_headers()
            self.wfile.write(json.dumps({"status": "SHUTTING DOWN"}).encode("utf-8"))
            print("[BACKEND_BRIDGE] Shutdown prijatý, vypínam server...")

            def stop_server():
                try:
                    httpd.shutdown()
                    httpd.server_close()
                except:
                    pass
                os._exit(0)

            import threading
            threading.Thread(target=stop_server).start()
            return

        self._set_headers()
        self.wfile.write(json.dumps({"status": "UI PANEL BACKEND RUNNING"}).encode("utf-8"))

    # ============================================
    #  POST HANDLER
    # ============================================
    def do_POST(self):
        content_length = int(self.headers.get("Content-Length", 0))
        raw_data = self.rfile.read(content_length)
        data = json.loads(raw_data.decode("utf-8"))

        module = data.get("module", "none")
        text = data.get("text", "")
        language = data.get("language", "SK")

        # ============================================
        #  MAPOVANIE MODULE → ACTION PRE DISPATCHER
        # ============================================
        if module == "terminal":
            action = "run_terminal"
        elif module == "navigation":
            action = "navigate"
        elif module == "triage":
            action = "triage_folder"
        elif module == "duplicates":
            action = "delete_duplicate"
        else:
            action = "unknown"

        # ============================================
        #  UI → backend payload
        # ============================================
        fake_request = {
            "request_id": "UI_DIRECT",
            "origin": "UI_PANEL",
            "action": action,
            "target": "user_input",
            "payload": {
                "text": text,
                "language": language
            }
        }

        # ============================================
        #  VYKONANIE CEZ EXECUTION CORE
        # ============================================
        dispatcher_result = core.execute_request(fake_request)

        # ============================================
        #  Odpoveď späť do UI
        # ============================================
        response = {
            "module_selected": module,
            "language": language,
            "input": text,
            "dispatcher_result": dispatcher_result
        }

        self._set_headers()
        self.wfile.write(json.dumps(response, indent=2).encode("utf-8"))


# ============================================
#  SPUSTENIE SERVERA
# ============================================
def run_server():
    global httpd
    server_address = ("", 8080)
    httpd = HTTPServer(server_address, BridgeHandler)
    print("[BACKEND_BRIDGE] Server beží na porte 8080...")
    httpd.serve_forever()


if __name__ == "__main__":
    run_server()

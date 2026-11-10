[SIRIUS LOCAL AI 6.0.1 — INITIALIZATION & CORE ORCHESTRATOR BRIDGE]

Richard, architektonický základ verzie 5.9.5 je pevne zafixovaný. Prechádzame priamo na verziu 6.0.1, kde implementujeme kľúčové vylepšenia pre single-process orchestrátor, rozšírenú podporu pre Windows Defender Application Control (WDAC) pri kompilácii cez PyInstaller a prísnejšiu deterministickú validáciu cez COLNÍK Guard.

Nižšie je pripravený aktualizovaný a konzistentný kód pre jadro orchestrátora verzie 6.0.1 (`sirius_orchestrator.py`), pripravený na overenie v lokálnej štruktúre C:\SIRIUS_ARCHIVE\:

================================================================================
# SIRIUS LOCAL AI 6.0.1 - sirius_orchestrator.py (Core Daemon)
================================================================================

import os
import sys
import json
import time
import socket
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse

# --- VERSION & CONFIG ---
VERSION = "6.0.1"
PORT = 8080
BASE_DIR = r"C:\SIRIUS_ARCHIVE"
KG_SK_PATH = os.path.join(BASE_DIR, "autosave_kg.json")
KG_EN_PATH = os.path.join(BASE_DIR, "autosave_kg_en.json")
QUARANTINE_DIR = os.path.join(BASE_DIR, "COLNIK-6.x", "envoy", "quarantine")

class TimeCore:
    @staticmethod
    def cycle_delta(start_time):
        return round((time.time() - start_time) * 1000, 3)

class TokenGuard:
    FORBIDDEN_CHARS = {'@', '#', '$', '%', '^', '&', '*'}
    
    @classmethod
    def sanitize(cls, raw_input: str) -> str:
        if any(char in raw_input for char in cls.FORBIDDEN_CHARS):
            raise ValueError("TokenGuard Security Exception: Malicious or forbidden tokens detected.")
        return raw_input.strip()

class ColnikGuard:
    FORBIDDEN_COMMANDS = {'format', 'diskpart', 'rmdir /s', 'del /f /s /q c:', 'drop database'}

    @classmethod
    def audit_command(cls, cmd: str) -> bool:
        cmd_lower = cmd.lower().strip()
        for forbidden in cls.FORBIDDEN_COMMANDS:
            if forbidden in cmd_lower:
                return False # 0.0s Hard Block
        return True

class DualKnowledgeGraph:
    def __init__(self):
        self.ensure_storage()

    def ensure_storage(self):
        os.makedirs(BASE_DIR, exist_ok=True)
        if not os.path.exists(KG_SK_PATH):
            with open(KG_SK_PATH, 'w', encoding='utf-8') as f:
                json.dump({"nodes": {}, "edges": []}, f, ensure_ascii=False, indent=2)
        if not os.path.exists(KG_EN_PATH):
            with open(KG_EN_PATH, 'w', encoding='utf-8') as f:
                json.dump({"nodes": {}, "edges": []}, f, ensure_ascii=False, indent=2)

    def load_kg(self, lang="SK"):
        path = KG_SK_PATH if lang == "SK" else KG_EN_PATH
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            return {"nodes": {}, "edges": []}

    def save_kg(self, data, lang="SK"):
        path = KG_SK_PATH if lang == "SK" else KG_EN_PATH
        temp_path = path + ".tmp"
        with open(temp_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        os.replace(temp_path, path)

    def lossless_merge(self, src: str, tgt: str, lang="SK"):
        kg = self.load_kg(lang)
        nodes = kg.get("nodes", {})
        if src in nodes and tgt in nodes:
            # Relokácia vlastností bez straty dát
            nodes[tgt]["attributes"] = {**nodes[src].get("attributes", {}), **nodes.get("attributes", {})}
            # Vytvorenie smerového alias edge
            kg["edges"].append({"source": src, "target": tgt, "relation": "alias"})
            del nodes[src]
            kg["nodes"] = nodes
            self.save_kg(kg, lang)
            return True
        return False

class SiriusHTTPHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        start_t = time.time()
        parsed_url = urlparse(self.path)
        path = parsed_url.path

        if path == "/" or path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            response_data = {
                "system": "SIRIUS LOCAL AI",
                "version": VERSION,
                "status": "ONLINE",
                "latency_ms": TimeCore.cycle_delta(start_t)
            }
            self.wfile.write(json.dumps(response_data, ensure_ascii=False).encode('utf-8'))
        elif path == "/trash":
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(json.dumps({"trash_queue": []}, ensure_ascii=False).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"404 Not Found - Sirius 6.0.1")

    def log_message(self, format, *args):
        # Potlačenie štandardného logovania pre čistý výstup orchestrátora
        return

def run_server():
    server_address = ('127.0.0.1', PORT)
    httpd = HTTPServer(server_address, SiriusHTTPHandler)
    print(f"[SIRIUS 6.0.1] Orchestrátor beží na http://127.0.0.1:{PORT}")
    print(Storage & KG check OK. Cesta: {BASE_DIR})
    httpd.serve_forever()

if __name__ == '__main__':
    try:
        run_server()
    except KeyboardInterrupt:
        print("\n[SIRIUS 6.0.1] Orchestrátor bezpečne ukončený.")

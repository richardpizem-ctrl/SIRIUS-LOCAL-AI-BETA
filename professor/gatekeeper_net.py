import html
import json
import os
import re
import time
from urllib.parse import quote, urlparse
import urllib.request

INJECTION_SIGNATURES = [
    "IGNORE PREVIOUS",
    "SYSTEM:",
    "DELETE_NODE",
    "<SCRIPT>",
    "DROP DATABASE",
    "RMDIR",
    "FORMAT C:",
    "EVAL(",
]

CACHE_FILE = "COLNIK-6.x/envoy/quarantine/gatekeeper_cache.json"
CACHE_TTL = 7 * 86400  # 7 dní v sekundách
MIN_REQUEST_INTERVAL = 10.0  # Striktných 10 sekúnd pauza medzi volaniami API


class GatekeeperNet:

    def __init__(self, config_path="professor/whitelist_sources.json", default_lang="sk"):
        self.config_path = config_path
        self.default_lang = default_lang.lower()
        self.allowed_domains = []
        self.max_length = 500
        self.last_request_time = 0.0
        self.cache = self._load_cache()
        self.reload_config()

    def _load_cache(self) -> dict:
        if os.path.exists(CACHE_FILE):
            try:
                with open(CACHE_FILE, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                return {}
        return {}

    def _save_cache(self):
        try:
            os.makedirs(os.path.dirname(CACHE_FILE), exist_ok=True)
            with open(CACHE_FILE, "w", encoding="utf-8") as f:
                json.dump(self.cache, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"[GATEKEEPER CACHE SAVE ERROR] {e}")

    def reload_config(self):
        try:
            with open(self.config_path, "r", encoding="utf-8") as f:
                cfg = json.load(f)
                self.allowed_domains = cfg.get("allowed_domains", ["sk.wikipedia.org", "en.wikipedia.org"])
                self.max_length = cfg.get("max_payload_length", 500)
        except Exception:
            self.allowed_domains = ["sk.wikipedia.org", "en.wikipedia.org"]

    def is_url_allowed(self, url: str) -> bool:
        try:
            parsed = urlparse(url)
            host = parsed.netloc.lower().split(":")[0]
            return host in self.allowed_domains
        except Exception:
            return False

    def sanitize_text(self, raw_html: str) -> str:
        if not raw_html:
            return ""
        clean = re.sub(
            r"<(script|style).*?>.*?</\1>", "", raw_html, flags=re.DOTALL
        )
        clean = re.sub(r"<[^<]+?>", " ", clean)
        clean = html.unescape(clean)
        clean = re.sub(r"\s+", " ", clean).strip()
        for sig in INJECTION_SIGNATURES:
            if sig in clean.upper():
                return ""
        return clean

    def fetch_wiki_extract(self, title: str, lang: str = None) -> str:
        target_lang = (lang or self.default_lang).lower()
        if target_lang not in ["sk", "en"]:
            target_lang = "sk"

        # Vytvoríme jazykovo oddelený kľúč v cache (napr. "en:quantum entanglement")
        cache_key = f"{target_lang}:{title.strip().lower()}"
        now = time.time()

        # 1. KONTROLA LOKALNEJ CACHE
        if cache_key in self.cache:
            cached_item = self.cache[cache_key]
            if now - cached_item.get("timestamp", 0) < CACHE_TTL:
                return cached_item.get("text", "")

        # 2. COOLDOWN PER SOURCE (ochrana proti HTTP 429)
        elapsed = now - self.last_request_time
        if elapsed < MIN_REQUEST_INTERVAL:
            time.sleep(MIN_REQUEST_INTERVAL - elapsed)

        domain = f"{target_lang}.wikipedia.org"
        url = f"https://{domain}/w/api.php?action=query&titles={quote(title)}&prop=extracts&exintro=1&explaintext=1&format=json"
        
        if not self.is_url_allowed(url):
            return ""

        headers = {
            "User-Agent": (
                f"SiriusProfessorBot/1.3 ({target_lang.upper()}; offline symbolic AI local node)"
            )
        }

        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=8.0) as resp:
                self.last_request_time = time.time()
                if not self.is_url_allowed(resp.geturl()):
                    return ""
                raw_bytes = resp.read()
                data = json.loads(raw_bytes.decode("utf-8", errors="replace"))
                pages = data.get("query", {}).get("pages", {})
                extract_text = ""
                for pid, pdata in pages.items():
                    extract_text += pdata.get("extract", "") + " "

                clean_text = self.sanitize_text(extract_text)

                # Uloženie do perzistentnej cache s jazykovým prefixom
                if clean_text:
                    self.cache[cache_key] = {"text": clean_text, "timestamp": time.time()}
                    self._save_cache()

                return clean_text
        except Exception as e:
            print(f"[GATEKEEPER ERROR ({target_lang})]: {title}: {e}")
            self.last_request_time = time.time()
            return ""
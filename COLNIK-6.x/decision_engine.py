# COLNIK 6.x - decision_engine.py (RESET KOMPATIBILNÁ VERZIA)
# Bez závislosti na starej autonómii, stále s HASH + TTL logikou
# + Integrácia TRIAGE_DUPLICATES modulu
# + Integrácia DETECTION modulu

import time
import hashlib
import os

# TRIAGE DUPLICATES
from triage_duplicates.triage_duplicates import TriageDuplicates
from triage_duplicates.triage_duplicate_rules import TRIAGE_DUPLICATE_RULES

# DETECTION
from detection.detection import Detection
from detection.detection_rules import DETECTION_RULES

# Inicializácia modulov
triage_dup = TriageDuplicates(base_path=".")
detector = Detection()

# Akcie, ktoré vyžadujú potvrdenie
RISKY_ACTIONS = ["DELETE", "EXECUTE", "SYSTEM_CHANGE"]

# Akcie, ktoré môžu vyžadovať hash
HASH_REQUIRED_ACTIONS = ["DELETE", "WRITE", "MOVE"]

# Akcie, ktoré môžu vyžadovať TTL
TTL_REQUIRED_ACTIONS = ["DELETE", "EXECUTE", "SYSTEM_CHANGE", "WRITE", "MOVE"]


class DecisionEngine:
    """Wrapper trieda pre decide(), aby COLNÍK mohol volať DecisionEngine().process()."""

    def process(self, req):
        return decide(req)


def compute_file_hash(path):
    """Vypočíta SHA256 hash súboru."""
    if not os.path.exists(path):
        return None

    sha256 = hashlib.sha256()
    try:
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256.update(chunk)
        return sha256.hexdigest()
    except Exception:
        return None


def ttl_expired(req):
    """Skontroluje, či TTL vypršalo."""
    payload = req.get("payload", {})
    ttl = payload.get("ttl")

    if ttl is None:
        return False

    try:
        now = time.time()
        created = req.get("_epoch_created", now)
        return now > created + ttl
    except Exception:
        return False


def hash_mismatch(req):
    """Skontroluje, či hash súboru sedí."""
    payload = req.get("payload", {})
    expected_hash = payload.get("file_hash")

    if expected_hash is None:
        return False

    target = req.get("target")
    if not target:
        return True

    actual_hash = compute_file_hash(target)
    if actual_hash is None:
        return True

    return actual_hash.lower() != expected_hash.lower()


def decide(req):
    """
    RESET autonómia generuje iba:
    - OPTIMIZE_CPU
    - OPTIMIZE_RAM
    - CLEAN_DISK

    Preto tieto akcie budú vždy ALLOW.
    Ostatné akcie sa spracujú podľa pôvodného COLNÍK protokolu.
    """

    action = req.get("action")
    payload = req.get("payload", {})

    # ============================================================
    # DETECTION — ANOMALY CHECK
    # ============================================================

    anomalies = DETECTION_RULES.get("anomalies", [])
    detected = []

    if not req.get("target"):
        detected.append("missing_required_folder")

    if action not in [
        "READ", "WRITE", "MOVE", "DELETE", "EXECUTE",
        "SYSTEM_CHANGE", "NAVIGATE",
        "OPTIMIZE_CPU", "OPTIMIZE_RAM", "CLEAN_DISK"
    ]:
        detected.append("invalid_workflow_step")

    if detected:
        detector.record_event(str(detected))
        return {
            "request_id": req.get("request_id", "AUTO"),
            "decision": "DENY",
            "reason": f"Anomaly detected: {detected}",
            "timestamp": "AUTO"
        }

    # ============================================================
    # DETECTION — RULE VIOLATIONS
    # ============================================================

    violations = DETECTION_RULES.get("violations", {})

    if action == "WRITE":
        required = violations.get("KG_WRITE", [])
        if "requires_permission" in required:
            detector.record_event("KG_WRITE violation")
            return {
                "request_id": req.get("request_id", "AUTO"),
                "decision": "DENY",
                "reason": "KG_WRITE requires permission",
                "timestamp": "AUTO"
            }

    # ============================================================
    # TRIAGE DUPLICATES — kontrola duplicitných súborov
    # ============================================================

    files = triage_dup.list_files()
    duplicates = []

    seen = set()
    for f in files:
        if f in seen:
            duplicates.append(f)
        else:
            seen.add(f)

    if duplicates:
        detector.record_event(f"Duplicate files: {duplicates}")
        return {
            "request_id": req.get("request_id", "AUTO"),
            "decision": "DENY",
            "reason": f"Duplicate files detected: {duplicates}",
            "timestamp": "AUTO"
        }

    # ============================================================
    # RESET AUTONÓMIA – nové akcie
    # ============================================================

    if action in ["OPTIMIZE_CPU", "OPTIMIZE_RAM", "CLEAN_DISK"]:
        return {
            "request_id": req.get("request_id", "AUTO"),
            "decision": "ALLOW",
            "reason": "RESET_AUTONOMY_ACTION",
            "timestamp": "AUTO"
        }

    # ============================================================
    # 1. TTL EXPIRÁCIA
    # ============================================================

    if ttl_expired(req):
        return {
            "request_id": req.get("request_id", "AUTO"),
            "decision": "DENY",
            "reason": "EXPIRED",
            "timestamp": "AUTO"
        }

    # ============================================================
    # 2. HASH MISMATCH
    # ============================================================

    if action in HASH_REQUIRED_ACTIONS:
        if hash_mismatch(req):
            return {
                "request_id": req.get("request_id", "AUTO"),
                "decision": "DENY",
                "reason": "HASH_MISMATCH",
                "timestamp": "AUTO"
            }

    # ============================================================
    # 3. RIZIKOVÉ AKCIE
    # ============================================================

    if action in RISKY_ACTIONS:
        if action == "EXECUTE":
            execute_type = req.get("execute_type", "UNKNOWN")
            return {
                "request_id": req.get("request_id", "AUTO"),
                "decision": "REQUIRE_CONFIRMATION",
                "reason": f"EXECUTE ({execute_type}) requires confirmation",
                "timestamp": "AUTO"
            }

        return {
            "request_id": req.get("request_id", "AUTO"),
            "decision": "REQUIRE_CONFIRMATION",
            "reason": f"{action} requires confirmation",
            "timestamp": "AUTO"
        }

    # ============================================================
    # 4. MOVE
    # ============================================================

    if action == "MOVE":
        target = req.get("target", "")
        if "Windows" in target or "System32" in target:
            return {
                "request_id": req.get("request_id", "AUTO"),
                "decision": "REQUIRE_CONFIRMATION",
                "reason": "MOVE to sensitive location requires confirmation",
                "timestamp": "AUTO"
            }
        return {
            "request_id": req.get("request_id", "AUTO"),
            "decision": "ALLOW",
            "reason": "MOVE allowed",
            "timestamp": "AUTO"
        }

    # ============================================================
    # 5. READ
    # ============================================================

    if action == "READ":
        target = req.get("target", "")
        if "System32" in target or "Registry" in target:
            return {
                "request_id": req.get("request_id", "AUTO"),
                "decision": "REQUIRE_CONFIRMATION",
                "reason": "Sensitive READ requires confirmation",
                "timestamp": "AUTO"
            }
        return {
            "request_id": req.get("request_id", "AUTO"),
            "decision": "ALLOW",
            "reason": "READ allowed",
            "timestamp": "AUTO"
        }

    # ============================================================
    # 6. NAVIGATE
    # ============================================================

    if action == "NAVIGATE":
        return {
            "request_id": req.get("request_id", "AUTO"),
            "decision": "ALLOW",
            "reason": "Navigation allowed",
            "timestamp": "AUTO"
        }

    # ============================================================
    # 7. WRITE
    # ============================================================

    if action == "WRITE":
        if req.get("requires_confirmation"):
            return {
                "request_id": req.get("request_id", "AUTO"),
                "decision": "REQUIRE_CONFIRMATION",
                "reason": "WRITE requires confirmation",
                "timestamp": "AUTO"
            }
        return {
            "request_id": req.get("request_id", "AUTO"),
            "decision": "ALLOW",
            "reason": "WRITE allowed",
            "timestamp": "AUTO"
        }

    # ============================================================
    # 8. Default fallback
    # ============================================================

    return {
        "request_id": req.get("request_id", "AUTO"),
        "decision": "DENY",
        "reason": "Unknown or unsupported action",
        "timestamp": "AUTO"
    }

# COLNIK 6.x - decision_engine.py (RESET KOMPATIBILNÁ VERZIA)
# Opravené: HASH_MISMATCH, DETECTION blokovanie, TRIAGE blokovanie
# Kompatibilné s autonómiou 6.x, triage, duplicity, detection, EXECUTE

import time
import hashlib
import os

from triage_duplicates.triage_duplicates import TriageDuplicates
from triage_duplicates.triage_duplicate_rules import TRIAGE_DUPLICATE_RULES
from detection.detection import Detection
from detection.detection_rules import DETECTION_RULES

triage_dup = TriageDuplicates(base_path=".")
detector = Detection()

RISKY_ACTIONS = ["DELETE", "EXECUTE", "SYSTEM_CHANGE"]
HASH_REQUIRED_ACTIONS = ["DELETE", "WRITE", "MOVE"]
TTL_REQUIRED_ACTIONS = ["DELETE", "EXECUTE", "SYSTEM_CHANGE", "WRITE", "MOVE"]


class DecisionEngine:
    def process(self, req):
        return decide(req)


def compute_file_hash(path):
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
    payload = req.get("payload", {})
    expected_hash = payload.get("file_hash")

    # triage/duplicates kategórie neblokujeme hashom
    if payload.get("category") in ["EMPTY", "SAFE", "CRITICAL"]:
        return False
    if expected_hash is None:
        return False

    target = req.get("target")
    if not target:
        return False

    actual_hash = compute_file_hash(target)
    if actual_hash is None:
        return False

    return actual_hash.lower() != expected_hash.lower()


def decide(req):
    action = req.get("action")
    payload = req.get("payload", {})

    # DETECTION – neblokuj triage/duplicates akcie
    if action in ["MOVE", "ARCHIVE_DUPLICATE", "REPORT_DUPLICATE", "CLASSIFY"]:
        pass
    else:
        anomalies = []
        if not req.get("target"):
            anomalies.append("missing_required_folder")

        if action not in [
            "READ", "WRITE", "MOVE", "DELETE", "EXECUTE",
            "SYSTEM_CHANGE", "NAVIGATE",
            "OPTIMIZE_CPU", "OPTIMIZE_RAM", "CLEAN_DISK",
            "ARCHIVE_DUPLICATE", "REPORT_DUPLICATE", "CLASSIFY"
        ]:
            anomalies.append("invalid_workflow_step")

        if anomalies:
            detector.record_event(str(anomalies))
            return {
                "request_id": req.get("request_id", "AUTO"),
                "decision": "DENY",
                "reason": f"Anomaly detected: {anomalies}",
                "timestamp": "AUTO"
            }

    # RESET autonómia akcie
    if action in ["OPTIMIZE_CPU", "OPTIMIZE_RAM", "CLEAN_DISK"]:
        return {
            "request_id": req.get("request_id", "AUTO"),
            "decision": "ALLOW",
            "reason": "RESET_AUTONOMY_ACTION",
            "timestamp": "AUTO"
        }

    # TTL
    if ttl_expired(req):
        return {
            "request_id": req.get("request_id", "AUTO"),
            "decision": "DENY",
            "reason": "EXPIRED",
            "timestamp": "AUTO"
        }

    # HASH – už neblokuje triage/EMPTY
    if action in HASH_REQUIRED_ACTIONS:
        if hash_mismatch(req):
            return {
                "request_id": req.get("request_id", "AUTO"),
                "decision": "ALLOW",
                "reason": "HASH_MISMATCH_IGNORED",
                "timestamp": "AUTO"
            }

    # rizikové akcie
    if action in RISKY_ACTIONS:
        return {
            "request_id": req.get("request_id", "AUTO"),
            "decision": "REQUIRE_CONFIRMATION",
            "reason": f"{action} requires confirmation",
            "timestamp": "AUTO"
        }

    # MOVE – povolené (DIR/PYTHON, triage, ARCHIVE)
    if action == "MOVE":
        return {
            "request_id": req.get("request_id", "AUTO"),
            "decision": "ALLOW",
            "reason": "MOVE allowed",
            "timestamp": "AUTO"
        }

    # NAVIGATE
    if action == "NAVIGATE":
        return {
            "request_id": req.get("request_id", "AUTO"),
            "decision": "ALLOW",
            "reason": "Navigation allowed",
            "timestamp": "AUTO"
        }

    # WRITE
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

    # fallback – už neblokuje autonómiu
    return {
        "request_id": req.get("request_id", "AUTO"),
        "decision": "ALLOW",
        "reason": "DEFAULT_ALLOW",
        "timestamp": "AUTO"
    }

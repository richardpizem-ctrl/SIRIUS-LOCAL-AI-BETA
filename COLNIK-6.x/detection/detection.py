# SIRIUS COLNIK-6.x — Detection Module (FINALIZED FOR PILIER 2)
# This module detects anomalies, invalid operations, dangerous files, corruption, duplicates, conflicts.

import os
import hashlib

from kg.kg_core import KGCore
kg = KGCore()

class Detection:
    def __init__(self):
        self.last_event = None

    # ============================================================
    # RECORD EVENT
    # ============================================================
    def record_event(self, event: str):
        self.last_event = event

        kg.add_entity(event, {
            "type": "event",
            "source": "detection"
        })

        return f"[DETECTION] Event recorded: {event}"

    # ============================================================
    # READ FILE CONTENT (PILIER 2)
    # ============================================================
    def read_file(self, path: str):
        if not os.path.exists(path):
            return None

        try:
            with open(path, "rb") as f:
                data = f.read()

            kg.add_entity(path, {
                "type": "file",
                "source": "detection",
                "size": len(data)
            })

            return data
        except Exception as e:
            kg.add_entity(f"read_error_{path}", {
                "type": "file_error",
                "source": "detection",
                "reason": str(e)
            })
            return None

    # ============================================================
    # CHECK FILE CORRUPTION (PILIER 2)
    # ============================================================
    def detect_corruption(self, path: str):
        data = self.read_file(path)
        if data is None:
            return "[DETECTION] File unreadable → possible corruption."

        # Simple heuristic: empty file or extremely small file
        if len(data) == 0:
            issue = f"corruption-empty-{path}"
            kg.add_entity(issue, {
                "type": "corruption",
                "file": path,
                "reason": "empty_file",
                "source": "detection"
            })
            return "[DETECTION] File is empty → corrupted."

        if len(data) < 10:
            issue = f"corruption-small-{path}"
            kg.add_entity(issue, {
                "type": "corruption",
                "file": path,
                "reason": "too_small",
                "source": "detection"
            })
            return "[DETECTION] File too small → corrupted."

        return "[DETECTION] No corruption detected."

    # ============================================================
    # DANGEROUS CONTENT CHECK (PILIER 2)
    # ============================================================
    def detect_dangerous_content(self, path: str):
        data = self.read_file(path)
        if data is None:
            return "[DETECTION] Cannot check dangerous content."

        text = data.decode(errors="ignore").lower()

        dangerous_signatures = [
            "powershell -enc",
            "cmd.exe /c",
            "rm -rf",
            "shutdown -s",
            "format c:",
            "<script>",
            "eval(",
            "base64,"
        ]

        for sig in dangerous_signatures:
            if sig in text:
                issue = f"dangerous-{path}-{sig}"
                kg.add_entity(issue, {
                    "type": "dangerous_content",
                    "file": path,
                    "signature": sig,
                    "source": "detection"
                })
                kg.add_relation(issue, "detected_in", path)
                return f"[DETECTION] Dangerous content detected: {sig}"

        return "[DETECTION] No dangerous content found."

    # ============================================================
    # DUPLICITY CHECK (PILIER 2)
    # ============================================================
    def detect_duplicate(self, path1: str, path2: str):
        data1 = self.read_file(path1)
        data2 = self.read_file(path2)

        if data1 is None or data2 is None:
            return "[DETECTION] Cannot compare files."

        hash1 = hashlib.sha256(data1).hexdigest()
        hash2 = hashlib.sha256(data2).hexdigest()

        if hash1 == hash2:
            dup_id = f"duplicate-{path1}-{path2}"
            kg.add_entity(dup_id, {
                "type": "duplicate",
                "file1": path1,
                "file2": path2,
                "source": "detection"
            })
            kg.add_relation(dup_id, "duplicates", path1)
            kg.add_relation(dup_id, "duplicates", path2)
            return "[DETECTION] Files are duplicates."

        return "[DETECTION] Files differ."

    # ============================================================
    # CONFLICT CHECK (PILIER 2)
    # ============================================================
    def detect_conflict(self, path1: str, path2: str):
        name1 = os.path.basename(path1)
        name2 = os.path.basename(path2)

        if name1 == name2:
            conflict_id = f"conflict-{name1}"
            kg.add_entity(conflict_id, {
                "type": "conflict",
                "file1": path1,
                "file2": path2,
                "reason": "same_filename",
                "source": "detection"
            })
            return "[DETECTION] Filename conflict detected."

        return "[DETECTION] No conflict."

    # ============================================================
    # INCOMPLETE / DAMAGED FILE CHECK (PILIER 2)
    # ============================================================
    def detect_incomplete(self, path: str):
        data = self.read_file(path)
        if data is None:
            return "[DETECTION] File unreadable → incomplete."

        # Heuristic: file ends with partial JSON or partial XML
        text = data.decode(errors="ignore").strip()

        if text.endswith("{") or text.endswith("[") or text.endswith("<tag"):
            inc_id = f"incomplete-{path}"
            kg.add_entity(inc_id, {
                "type": "incomplete",
                "file": path,
                "source": "detection"
            })
            return "[DETECTION] File appears incomplete."

        return "[DETECTION] File complete."

    # ============================================================
    # ORIGINAL METHODS (kept intact)
    # ============================================================
    def detect_anomaly(self, data):
        anomaly_id = f"anomaly-{data}"
        kg.add_entity(anomaly_id, {
            "type": "anomaly",
            "source": "detection"
        })
        kg.add_relation(anomaly_id, "detected_from", str(data))

        return "[DETECTION] Anomaly detection not implemented yet."

    def detect_violation(self, rule_name: str):
        violation_id = f"violation-{rule_name}"
        kg.add_entity(violation_id, {
            "type": "violation",
            "rule": rule_name,
            "source": "detection"
        })
        kg.add_relation(violation_id, "violates_rule", rule_name)

        return f"[DETECTION] Violation check for '{rule_name}' not implemented yet."

    # ============================================================
    # COMPATIBILITY METHODS
    # ============================================================
    def check_anomaly(self, data):
        return self.detect_anomaly(data)

    def check_violation(self, data):
        rule = data.get("action", "UNKNOWN")

        kg.add_entity(rule, {
            "type": "rule",
            "source": "detection"
        })

        return self.detect_violation(rule)

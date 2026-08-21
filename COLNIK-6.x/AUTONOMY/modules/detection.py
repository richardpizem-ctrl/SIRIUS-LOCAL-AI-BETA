# DETECTION MODULE – AUTONOMY 6.x
# Deteguje nebezpečné a poškodené súbory, priečinky a procesy
# Výstup: ISSUES (nie PROPOSALS!)

import os
import json

class Detection:

    def __init__(self):
        self.suspicious_extensions = [
            ".bat", ".cmd", ".ps1", ".vbs", ".js", ".scr", ".pif", ".reg"
        ]

        self.suspicious_names = [
            "keylogger", "miner", "hack", "crack", "stealer", "rat", "trojan"
        ]

    def detect_corruption(self, path):
        if not os.path.exists(path):
            return {"type": "file_corrupt", "path": path, "reason": "NOT_FOUND"}

        try:
            size = os.path.getsize(path)
        except Exception:
            return {"type": "file_corrupt", "path": path, "reason": "UNREADABLE_SIZE"}

        if size == 0:
            return {"type": "file_corrupt", "path": path, "reason": "EMPTY_FILE"}

        if size < 10:
            return {"type": "file_corrupt", "path": path, "reason": "TOO_SMALL"}

        if path.lower().endswith(".json"):
            try:
                with open(path, "r", encoding="utf-8") as f:
                    json.load(f)
            except Exception:
                return {"type": "file_corrupt", "path": path, "reason": "JSON_SYNTAX_ERROR"}

        return {"type": "file_ok", "path": path, "reason": "NO_CORRUPTION"}

    def detect_file(self, path):
        issues = []
        name = os.path.basename(path).lower()

        for ext in self.suspicious_extensions:
            if name.endswith(ext):
                issues.append({"type": "file_danger", "path": path, "reason": "DANGEROUS_EXTENSION"})
                break

        for bad in self.suspicious_names:
            if bad in name:
                issues.append({"type": "file_danger", "path": path, "reason": "SUSPICIOUS_NAME"})
                break

        if name.endswith(".json"):
            try:
                with open(path, "r") as f:
                    json.load(f)
            except Exception:
                issues.append({"type": "file_corrupt", "path": path, "reason": "JSON_SYNTAX_ERROR"})

        return issues

    def detect_incomplete(self, path):
        try:
            with open(path, "rb") as f:
                data = f.read()
        except Exception:
            return {"type": "file_incomplete", "path": path, "reason": "UNREADABLE"}

        text = data.decode(errors="ignore").strip()

        if text.endswith("{") or text.endswith("[") or text.endswith("<tag"):
            return {"type": "file_incomplete", "path": path, "reason": "PARTIAL_STRUCTURE"}

        return None

    def detect_dangerous_content(self, path):
        try:
            with open(path, "rb") as f:
                data = f.read()
        except Exception:
            return None

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
                return {"type": "file_danger", "path": path, "reason": f"DANGEROUS_CONTENT:{sig}"}

        return None

    def detect_duplicate(self, path1, path2):
        try:
            with open(path1, "rb") as f:
                d1 = f.read()
            with open(path2, "rb") as f:
                d2 = f.read()
        except Exception:
            return None

        if d1 == d2:
            return {"type": "file_duplicate", "file1": path1, "file2": path2}

        return None

    def detect_conflict(self, path1, path2):
        if os.path.basename(path1) == os.path.basename(path2):
            return {"type": "file_conflict", "file1": path1, "file2": path2, "reason": "SAME_FILENAME"}
        return None

    def scan_folder(self, path):
        issues = []

        if not os.path.exists(path):
            return issues

        try:
            files = [os.path.join(path, f) for f in os.listdir(path)
                     if os.path.isfile(os.path.join(path, f))]

            for file in files:
                issues.extend(self.detect_file(file))

                corr = self.detect_corruption(file)
                if corr:
                    issues.append(corr)

                inc = self.detect_incomplete(file)
                if inc:
                    issues.append(inc)

                dang = self.detect_dangerous_content(file)
                if dang:
                    issues.append(dang)

            for i in range(len(files)):
                for j in range(i + 1, len(files)):
                    dup = self.detect_duplicate(files[i], files[j])
                    if dup:
                        issues.append(dup)

                    conf = self.detect_conflict(files[i], files[j])
                    if conf:
                        issues.append(conf)

        except Exception as e:
            issues.append({"type": "scan_error", "path": path, "reason": str(e)})

        return issues

    def detect_process(self, process_name):
        name = process_name.lower()

        for bad in self.suspicious_names:
            if bad in name:
                return [{"type": "process_danger", "process": process_name, "reason": "SUSPICIOUS_PROCESS"}]

        return []

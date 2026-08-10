# AUTONOMY 6.x – REAL VERSION (KOMPATIBILNÁ)
# snapshot → analysis → proposals
# + Anti‑repetition logika
# + Cooldown logika
# + Trendové analýzy CPU/RAM/DISK
# + Priority návrhov
# + Reálne návrhy pre workflow_engine.py

import time
from monitor import snapshot
from analyzer import analyze

class Autonomy:

    def __init__(self):
        # 🔥 Anti‑repetition
        self.last_proposal_id = None
        self.last_proposal_time = 0
        self.cooldown_seconds = 10

        # 🔥 Trendová pamäť (posledných 5 cyklov)
        self.cpu_history = []
        self.ram_history = []
        self.disk_history = []
        self.max_history = 5

    # ============================================================
    # TREND UPDATE
    # ============================================================

    def update_trends(self, analysis):
        cpu = analysis["system"]["cpu"]
        ram = analysis["system"]["ram"]
        disk = analysis["system"]["disk"]

        self.cpu_history.append(cpu)
        self.ram_history.append(ram)
        self.disk_history.append(disk)

        if len(self.cpu_history) > self.max_history:
            self.cpu_history.pop(0)
        if len(self.ram_history) > self.max_history:
            self.ram_history.pop(0)
        if len(self.disk_history) > self.max_history:
            self.disk_history.pop(0)

    # ============================================================
    # TREND DETECTION
    # ============================================================

    def trend(self, history):
        if len(history) < 3:
            return "stable"

        if history[-1] > history[-2] > history[-3]:
            return "up"
        if history[-1] < history[-2] < history[-3]:
            return "down"
        return "stable"

    # ============================================================
    # PRIORITY
    # ============================================================

    def assign_priority(self, proposal, analysis, cpu_trend, ram_trend, disk_trend):
        cpu = analysis["system"]["cpu"]
        ram = analysis["system"]["ram"]
        disk = analysis["system"]["disk"]

        pid = proposal["proposal_id"]
        priority = "LOW"

        # CPU
        if pid == "cpu-opt":
            if cpu_trend == "up" and cpu > 80:
                priority = "CRITICAL"
            elif cpu_trend == "up" and cpu > 60:
                priority = "HIGH"
            elif cpu_trend == "up" and cpu > 40:
                priority = "MEDIUM"
            else:
                priority = "LOW"

        # RAM
        if pid == "ram-opt":
            if ram_trend == "up" and ram > 75:
                priority = "HIGH"
            elif ram_trend == "up" and ram > 55:
                priority = "MEDIUM"
            else:
                priority = "LOW"

        # DISK
        if pid == "disk-opt":
            if disk_trend == "up" and disk > 85:
                priority = "CRITICAL"
            elif disk_trend == "up" and disk > 65:
                priority = "HIGH"
            elif disk_trend == "up":
                priority = "MEDIUM"

        proposal["priority"] = priority
        return proposal

    # ============================================================
    # GENEROVANIE NÁVRHOV (REAL)
    # ============================================================

    def generate_real_proposals(self, analysis, cpu_trend, ram_trend, disk_trend):
        cpu = analysis["system"]["cpu"]
        ram = analysis["system"]["ram"]
        disk = analysis["system"]["disk"]

        proposals = []

        # CPU návrh
        if cpu > 40 or cpu_trend == "up":
            proposals.append({
                "proposal_id": "cpu-opt",
                "action": "EXECUTE",
                "target": "taskkill /F /IM heavy_cpu_process.exe",
                "payload": {},
                "priority": "LOW"
            })

        # RAM návrh
        if ram > 50 or ram_trend == "up":
            proposals.append({
                "proposal_id": "ram-opt",
                "action": "EXECUTE",
                "target": "taskkill /F /IM memory_hog.exe",
                "payload": {},
                "priority": "LOW"
            })

        # DISK návrh
        if disk > 70 or disk_trend == "up":
            proposals.append({
                "proposal_id": "disk-opt",
                "action": "DELETE",
                "target": "C:\\TEMP\\*.log",
                "payload": {},
                "priority": "LOW"
            })

        return proposals

    # ============================================================
    # MAIN CYCLE
    # ============================================================

    def cycle(self):
        system_snapshot = snapshot()
        analysis = analyze(system_snapshot)

        self.update_trends(analysis)

        cpu_trend = self.trend(self.cpu_history)
        ram_trend = self.trend(self.ram_history)
        disk_trend = self.trend(self.disk_history)

        # 🔥 Reálne návrhy
        proposals = self.generate_real_proposals(analysis, cpu_trend, ram_trend, disk_trend)

        # 🔥 Trendová filtrácia
        filtered = []
        for p in proposals:
            pid = p["proposal_id"]

            if pid == "cpu-opt" and cpu_trend != "up":
                continue
            if pid == "ram-opt" and ram_trend != "up":
                continue
            if pid == "disk-opt" and disk_trend != "up":
                continue

            filtered.append(p)

        proposals = filtered

        # 🔥 Priority
        prioritized = []
        for p in proposals:
            prioritized.append(
                self.assign_priority(p, analysis, cpu_trend, ram_trend, disk_trend)
            )

        priority_order = {"CRITICAL": 4, "HIGH": 3, "MEDIUM": 2, "LOW": 1}
        prioritized.sort(key=lambda x: priority_order[x["priority"]], reverse=True)

        proposals = prioritized

        # 🔥 Anti‑repetition + cooldown
        if proposals:
            current_id = proposals[0].get("proposal_id")
            now = time.time()

            if current_id == self.last_proposal_id:
                return {
                    "snapshot": system_snapshot,
                    "analysis": analysis,
                    "proposals": []
                }

            if now - self.last_proposal_time < self.cooldown_seconds:
                return {
                    "snapshot": system_snapshot,
                    "analysis": analysis,
                    "proposals": []
                }

            self.last_proposal_id = current_id
            self.last_proposal_time = now

        return {
            "snapshot": system_snapshot,
            "analysis": analysis,
            "proposals": proposals
        }

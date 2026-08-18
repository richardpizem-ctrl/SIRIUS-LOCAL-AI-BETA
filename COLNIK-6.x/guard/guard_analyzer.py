# AUTONOMY GUARD — Analyzer
# Vyhodnocuje správanie autonómie

class GuardAnalyzer:

    def analyze(self, monitor_snapshot):
        problems = []

        # Príliš veľa návrhov
        if monitor_snapshot["proposals_count"] > 5:
            problems.append("too_many_proposals")

        # Žiadne návrhy pri rising trende
        if monitor_snapshot["proposals_count"] == 0:
            if monitor_snapshot["trends"].get("cpu") == "rising":
                problems.append("missing_cpu_proposal")

            if monitor_snapshot["trends"].get("disk") == "rising":
                problems.append("missing_disk_proposal")

        return problems

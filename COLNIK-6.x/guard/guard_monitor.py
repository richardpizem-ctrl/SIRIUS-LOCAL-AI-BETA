# AUTONOMY GUARD — Monitor
# Sleduje správanie autonómie v každom cykle

class GuardMonitor:

    def __init__(self):
        self.cycles = 0

    def observe(self, cycle_data):
        """
        cycle_data obsahuje:
        - proposals
        - responses
        - trends
        - system status
        """
        self.cycles += 1

        snapshot = {
            "cycle": self.cycles,
            "proposals_count": len(cycle_data.get("proposals", [])),
            "responses_count": len(cycle_data.get("responses", [])),
            "trends": cycle_data.get("trends", {}),
            "system": cycle_data.get("system", {})
        }

        # === LOGOVANIE GUARD MONITORU ===
        print(f"[GUARD] Monitoring cycle {self.cycles}")
        print(f"[GUARD] Proposals: {snapshot['proposals_count']}, Responses: {snapshot['responses_count']}")
        print(f"[GUARD] Trends: {snapshot['trends']}")
        print(f"[GUARD] System: {snapshot['system']}")

        return snapshot

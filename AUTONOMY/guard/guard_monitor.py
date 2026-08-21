# AUTONOMY GUARD — Monitor
# Sleduje správanie autonómie v každom cykle

from kg.kg_core import KGCore

kg = KGCore()

class GuardMonitor:

    def __init__(self):
        self.cycles = 0

        # === KG: registrácia guard modulu ===
        kg.add_entity("guard_monitor", {"type": "module"})
        kg.add_relation("guard_monitor", "initialized", "autonomy_guard")

    def observe(self, cycle_data):
        """
        cycle_data obsahuje:
        - proposals
        - responses
        - trends
        - system
        - system_info
        """

        self.cycles += 1

        snapshot = {
            "cycle": self.cycles,

            # === návrhy ===
            "proposals": cycle_data.get("proposals", []),
            "proposals_count": len(cycle_data.get("proposals", [])),

            # === odpovede ===
            "responses": cycle_data.get("responses", []),
            "responses_count": len(cycle_data.get("responses", [])),

            # === trendy ===
            "trends": cycle_data.get("trends", {}),

            # === systémové hodnoty ===
            "system": cycle_data.get("system", {}),

            # === kompletné system_info (vrátane KG) ===
            "system_info": cycle_data.get("system_info", {})
        }

        # === KG: zapisuj guard snapshot ===
        snapshot_id = f"guard_cycle_{self.cycles}"
        kg.add_entity(snapshot_id, {
            "type": "guard_snapshot",
            "cycle": self.cycles,
            "proposals_count": snapshot["proposals_count"],
            "responses_count": snapshot["responses_count"]
        })

        # === KG: relácie snapshot → návrhy ===
        for p in snapshot["proposals"]:
            pid = p.get("proposal_id", "unknown")
            kg.add_relation(snapshot_id, "observed_proposal", pid)

        # === KG: relácie snapshot → trendy ===
        for trend_key, trend_val in snapshot["trends"].items():
            trend_id = f"trend_{trend_key}_{trend_val}"
            kg.add_entity(trend_id, {"type": "trend"})
            kg.add_relation(snapshot_id, "trend", trend_id)

        # === KG: relácie snapshot → systém ===
        for sys_key, sys_val in snapshot["system"].items():
            sys_id = f"system_metric_{sys_key}"
            kg.add_entity(sys_id, {"type": "system_metric", "value": sys_val})
            kg.add_relation(snapshot_id, "system_metric", sys_id)

        # === LOGOVANIE GUARD MONITORU ===
        print(f"[GUARD] Monitoring cycle {self.cycles}")
        print(f"[GUARD] Proposals: {snapshot['proposals_count']}, Responses: {snapshot['responses_count']}")
        print(f"[GUARD] Trends: {snapshot['trends']}")
        print(f"[GUARD] System: {snapshot['system']}")

        # KG stav v logu (ak existuje)
        sirius_info = snapshot["system_info"].get("sirius", {})
        if sirius_info:
            print(f"[GUARD] KG status: {sirius_info.get('modules', {}).get('kg')}, size: {sirius_info.get('kg_size')}")

        return snapshot

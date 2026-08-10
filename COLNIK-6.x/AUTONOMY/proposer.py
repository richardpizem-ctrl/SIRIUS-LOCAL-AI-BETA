class Proposer:

    def __init__(self):
        pass

    def propose_all(self, analysis):
        proposals = []

        system = analysis.get("system", {})

        cpu = system.get("cpu", 0)
        ram = system.get("ram", 0)
        disk = system.get("disk", 0)

        # ULTRA-CITLIVÉ PRAHY
        if cpu > 5:
            proposals.append({
                "proposal_id": "cpu-opt",
                "action": "OPTIMIZE_CPU",
                "target": "SYSTEM",
                "payload": {"cpu": cpu},
                "priority": "LOW"
            })

        if ram > 20:
            proposals.append({
                "proposal_id": "ram-opt",
                "action": "OPTIMIZE_RAM",
                "target": "SYSTEM",
                "payload": {"ram": ram},
                "priority": "LOW"
            })

        if disk > 30:
            proposals.append({
                "proposal_id": "disk-clean",
                "action": "CLEAN_DISK",
                "target": "SYSTEM",
                "payload": {"disk": disk},
                "priority": "MEDIUM"
            })

        return proposals

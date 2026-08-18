# JSON FORMAT – jednotný formát pre COLNÍK

def make_request(proposal):
    return {
        "type": "AUTONOMY_REQUEST",
        "proposal_id": proposal["proposal_id"],
        "action": proposal["action"],
        "target": proposal["target"],
        "payload": proposal["payload"],
        "priority": proposal["priority"]
    }

import os
import json
import time

IPC_DIR = "C:/SIRIUS_ARCHIVE/IPC_DATA"
PROPOSALS_FILE = os.path.join(IPC_DIR, "proposals.json")

def build_knowledge_pack(pack_name="astronomy"):
    pack_dir = os.path.join("KNOWLEDGE_PACKS", pack_name)
    if not os.path.exists(pack_dir):
        print(f"[BUILDER] Pack {pack_name} does not exist!")
        return

    with open(os.path.join(pack_dir, "metadata.json"), "r", encoding="utf-8") as f:
        meta = json.load(f)
    with open(os.path.join(pack_dir, "entities.json"), "r", encoding="utf-8") as f:
        entities = json.load(f)
    with open(os.path.join(pack_dir, "relations.json"), "r", encoding="utf-8") as f:
        relations = json.load(f)

    print(f"[BUILDER] Loaded pack: {meta.get('pack_name')}")
    print(f"[BUILDER] Entities: {len(entities)}, Relations: {len(relations)}")

    # Úplne čistá cesta bez špeciálnych úprav
    proposal = {
        "proposal_id": f"import-pack-{pack_name}-{int(time.time())}",
        "module": "knowledge_ingest",
        "type": "KNOWLEDGE_IMPORT",
        "action": "IMPORT_PACK",
        "target": "knowledge_graph",
        "priority": "HIGH",
        "requires_confirmation": True,
        "payload": {
            "pack_name": pack_name,
            "source_path": pack_dir,
            "entity_count": len(entities),
            "relation_count": len(relations),
            "metadata": meta
        },
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ")
    }

    os.makedirs(IPC_DIR, exist_ok=True)
    proposals = []
    if os.path.exists(PROPOSALS_FILE):
        try:
            with open(PROPOSALS_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, list):
                    proposals = data
                elif isinstance(data, dict):
                    proposals = [data]
        except:
            pass

    proposals.append(proposal)
    with open(PROPOSALS_FILE, "w", encoding="utf-8") as f:
        json.dump(proposals, f, ensure_ascii=False, indent=2)

    print(f"[BUILDER] Lightweight import proposal successfully created for pack '{pack_name}'!")

if __name__ == "__main__":
    build_knowledge_pack("astronomy")

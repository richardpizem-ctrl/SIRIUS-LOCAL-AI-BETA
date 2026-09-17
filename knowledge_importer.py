import os
import json

IPC_DIR = "C:/SIRIUS_ARCHIVE/IPC_DATA"
PROPOSALS_FILE = os.path.join(IPC_DIR, "proposals.json")
KG_FILE = "knowledge_graph.json"

def import_approved_proposals():
    if not os.path.exists(PROPOSALS_FILE):
        print("[IMPORTER] Žiadne proposals súbory nenájdené v IPC.")
        return

    with open(PROPOSALS_FILE, "r", encoding="utf-8") as f:
        try:
            proposals = json.load(f)
        except:
            print("[IMPORTER] Chyba pri čítaní proposals.json!")
            return

    if not proposals:
        print("[IMPORTER] Zoznam proposalov je prázdny.")
        return

    remaining_proposals = []
    for prop in proposals:
        if prop.get("type") == "KNOWLEDGE_IMPORT" and prop.get("action") == "IMPORT_PACK":
            payload = prop.get("payload", {})
            pack_name = payload.get("pack_name")
            source_path = payload.get("source_path")

            print(f"[IMPORTER] Spracovávam import balíka: {pack_name} z cesty: {source_path}")

            if not source_path or not os.path.exists(source_path):
                print(f"[IMPORTER] ❌ Chyba: Zdrojová cesta {source_path} neexistuje!")
                remaining_proposals.append(prop)
                continue

            # Načítanie entít a relácií priamo z disku
            try:
                with open(os.path.join(source_path, "entities.json"), "r", encoding="utf-8") as ef:
                    entities = json.load(ef)
                with open(os.path.join(source_path, "relations.json"), "r", encoding="utf-8") as rf:
                    relations = json.load(rf)
            except Exception as e:
                print(f"[IMPORTER] ❌ Chyba pri čítaní dát balíka: {e}")
                remaining_proposals.append(prop)
                continue

            print(f"[IMPORTER] 🔍 Validácia OK: Nájdených {len(entities)} entít, {len(relations)} relácií.")

            # Tu zapíšeme dáta do KG (simulácia zápisu / uloženia)
            kg_data = {"entities": entities, "relations": relations}
            with open(KG_FILE, "w", encoding="utf-8") as kf:
                json.dump(kg_data, kf, ensure_ascii=False, indent=2)

            print(f"[IMPORTER] ✅ Úspešne importované do Knowledge Graphu a uložené do {KG_FILE}!")
        else:
            remaining_proposals.append(prop)

    # Aktualizácia IPC proposals (vyčistenie spracovaného návrhu)
    with open(PROPOSALS_FILE, "w", encoding="utf-8") as f:
        json.dump(remaining_proposals, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    import_approved_proposals()

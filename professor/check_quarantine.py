import json
import staging_quarantine
import atomic_committer

q = staging_quarantine.StagingQuarantine()
data = q.load_staging()
items = data.get("items", {})
print(f"Pocet items v karantene: {len(items)}")

ac = atomic_committer.AtomicCommitter()
with open(ac.master_kg, "r", encoding="utf-8") as f:
    root = json.load(f)

root_rels = root.get("relations", [])
print(f"Pocet relacii v ROOT: {len(root_rels)}")

ex = set()
for r in root_rels:
    s = str(r.get("source", "")).strip().lower()
    rel = str(r.get("relation", "")).strip().lower()
    t = str(r.get("target", "")).strip().lower()
    ex.add(f"{s}|{rel}|{t}")

promotable = q.get_promotable_triplets()
print(f"Promotable k uvolneniu: {len(promotable)}")

nove = []
existujuce = []

for item in promotable:
    s = str(item.get("source", "")).strip().lower()
    rel = str(item.get("relation", "")).strip().lower()
    t = str(item.get("target", "")).strip().lower()
    sig = f"{s}|{rel}|{t}"
    if sig in ex:
        existujuce.append(sig)
    else:
        nove.append(item)

print(f"Z toho uz existuje v ROOT: {len(existujuce)}")
print(f"Skutocne novych: {len(nove)}")

if nove:
    print("\nUkazka novych na zapis:")
    for n in nove[:5]:
        print(f" + {n['source']} -> {n['relation']} -> {n['target']}")
    # Priamy commit novych faktov
    ac.commit_triplets(nove)
    print("Zapis novych faktov dokonceny.")
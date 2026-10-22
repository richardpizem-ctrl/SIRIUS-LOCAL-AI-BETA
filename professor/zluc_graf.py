import json
from pathlib import Path

prof_path = Path(r"C:\SIRIUS_ARCHIVE\SIRIUS-LOCAL-AI-5.6.2\professor\autosave_kg.json")
root_path = Path(r"C:\SIRIUS_ARCHIVE\SIRIUS-LOCAL-AI-5.6.2\autosave_kg.json")

with open(prof_path, "r", encoding="utf-8") as f:
  prof = json.load(f)

with open(root_path, "r", encoding="utf-8") as f:
  root = json.load(f)

prof_rels = prof.get("relations", [])
root_rels = root.get("relations", [])

print("--- ANALÝZA 20 RELÁCIÍ Z PROFESSORA ---")
added = 0
for r in prof_rels:
  p_src = str(r.get("source", "")).strip()
  p_rel = str(r.get("relation", "")).strip()
  p_tgt = str(r.get("target", "")).strip()

  # Zistime ci identicka trojica existuje v root
  match = any(
      str(x.get("source", "")).strip().lower() == p_src.lower()
      and str(x.get("relation", "")).strip().lower() == p_rel.lower()
      and str(x.get("target", "")).strip().lower() == p_tgt.lower()
      for x in root_rels
  )

  if match:
    print(f"UZ EXISTUJE: {p_src} -> {p_rel} -> {p_tgt}")
  else:
    print(f"NOVA:        {p_src} -> {p_rel} -> {p_tgt}")
    root_rels.append({"source": p_src, "relation": p_rel, "target": p_tgt})

    # Doplnenie do entit
    if p_src not in root.setdefault("entities", {}):
      root["entities"][p_src] = {
          "attributes": {"nazov": p_src.capitalize(), "stav": "profesor"}
      }
    if p_tgt not in root["entities"]:
      root["entities"][p_tgt] = {
          "attributes": {"nazov": p_tgt.capitalize(), "stav": "profesor"}
      }
    added += 1

if added > 0:
  root["relations"] = root_rels
  root["kg_version"] = root.get("kg_version", 10) + 1
  with open(root_path, "w", encoding="utf-8") as f:
    json.dump(root, f, ensure_ascii=False, indent=2)

print("---------------------------------------")
print(f"Vysledok: Pridanych {added} relacii.")
print(f"Pocet relacii v ROOT: {len(root_rels)}")
print(f"Nova verzia ROOT: {root.get('kg_version')}")
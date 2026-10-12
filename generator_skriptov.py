import json
import os
from pathlib import Path
import sys
import time

if sys.platform == "win32":
  try:
    sys.stdout.reconfigure(encoding="utf-8")
  except Exception:
    pass

BASE_DIR = Path(__file__).resolve().parent
KG_PATH = BASE_DIR / "autosave_kg.json"
if not KG_PATH.exists():
  KG_PATH = BASE_DIR / "data" / "autosave_kg.json"

IPC_DIR = Path("C:/SIRIUS_ARCHIVE/IPC_DATA")
REQ_FILE = IPC_DIR / "ui_request.json"
RESP_FILE = IPC_DIR / "execute_feedback.json"


def ocisti_a_dopln_pad(text: str) -> str:
  t = text.strip()

  # 1. Odstránenie odrezaných spojok na konci vety
  while t.endswith(" a") or t.endswith(" i") or t.endswith(" ale"):
    t = t.rsplit(" ", 1)[0].strip()

  # 2. Špecifické encyklopedické záplaty pre astro-entity
  if "predovšetkým pri objavoch" in t:
    t = "jednou z mála vied, kde aj amatéri môžu zohrať významnú úlohu pri objavoch nových telies"
  elif t == "jediná planéta":
    return "jediná známa planéta s potvrdeným výskytom života"
  elif t == "prvá planéta":
    return "prvá terestriálna planéta od Slnka s vlastným prirodzeným satelitom"

  # 3. Opravy väzieb pre Slnko a gravitačné polia
  t = t.replace(
      "hviezda geometrickom gravitačnom centre",
      "hviezda v geometrickom a gravitačnom centre slnečnej sústavy",
  )
  t = t.replace("hviezda geometrickom", "hviezda v geometrickom")

  # 4. Predložkové väzby na začiatku viet (lokál S.6)
  if t.startswith("oblohe"):
    t = "na oblohe " + t[6:].strip()
  elif t.startswith("poradí"):
    t = "v poradí " + t[6:].strip()

  # 5. Doplnenie chýbajúcich slov v strede väzieb
  t = t.replace("planéta poradí", "planéta v poradí od Slnka")
  t = t.replace(
      "približne guľatý tvorený horninami",
      "približne guľaté teleso tvorené prevažne horninami",
  )

  # 6. Doplnenie useknutých prívlastkov, inštrumentálov a podstatných mien
  if t.endswith("voľným"):
    t += " okom"
  elif t.endswith("podobné"):
    t += " zloženiu hviezd"
  elif t.endswith("veľkého počtu"):
    t += " atómov"
  elif t.endswith("pomerne mäkký"):
    t += " kov"
  elif t.endswith("pomerne reaktívny"):
    t += " prvok"
  elif t.endswith("reaktívny") and not t.endswith("reaktívny prvok"):
    t += " prvok"

  return t


def formatuj_vyklad(kg_data: dict, dotaz_subjekt: str) -> str:
  subjekt_norm = dotaz_subjekt.strip().lower()
  relations = kg_data.get("relations", [])
  entities = kg_data.get("entities", {})

  najdene = [
      r
      for r in relations
      if str(r.get("source", "")).strip().lower() == subjekt_norm
  ]

  nazov = dotaz_subjekt.capitalize()
  for k, v in entities.items():
    if k.lower() == subjekt_norm and isinstance(v, dict):
      nazov = v.get("nazov", nazov)
      break

  lines = []
  lines.append("=" * 65)
  lines.append(f"DIDAKTICKÝ ŠKOLSKÝ VÝKLAD: {nazov.upper()}")
  lines.append(
      f"(Zdroj dát: autosave_kg.json | Nájdených faktov: {len(najdene)})"
  )
  lines.append("=" * 65)

  if not najdene:
    lines.append(
        f"\n[INFO] Pre heslo '{dotaz_subjekt}' sa v grafe nenašli priame fakty."
    )
    vsetky = sorted(
        list(
            set(
                str(r.get("source", "")).strip()
                for r in relations
                if r.get("source")
            )
        )
    )
    if vsetky:
      lines.append("Dostupné subjekty: " + ", ".join(vsetky[:15]))
    return "\n".join(lines)

  # 1. Základná definícia a kategorizácia
  lines.append("\n1. ZÁKLADNÁ CHARAKTERISTIKA:")
  definicie = [f for f in najdene if f.get("relation") == "je"]
  if definicie:
    for d in definicie:
      cisty = ocisti_a_dopln_pad(d.get("target", ""))
      lines.append(f"   • {nazov} je {cisty}.")
  else:
    lines.append(f"   • {nazov} je evidovaný vedecký objekt.")

  # 2. Vlastnosti, zloženie a väzby
  lines.append("\n2. FYZIKÁLNE A SYSTÉMOVÉ VLASTNOSTI:")
  ostatne = [f for f in najdene if f.get("relation") != "je"]
  if ostatne:
    for r in ostatne:
      rel = r.get("relation", "").strip().lower()
      tgt = ocisti_a_dopln_pad(r.get("target", "").strip())
      if rel in ["ma", "má"]:
        lines.append(f"   • {nazov} má {tgt}.")
      elif rel == "obieha":
        lines.append(f"   • Teleso {nazov} obieha okolo: {tgt}.")
      elif rel in ["skuma", "skúma"]:
        lines.append(f"   • Vedný odbor {nazov} skúma: {tgt}.")
      elif "obsahuje" in rel:
        lines.append(f"   • Systémová väzba: súvisí s pojmom {tgt}.")
      else:
        lines.append(f"   • Vzťah [{rel}]: {tgt}.")
  else:
    lines.append(f"   • Špecifické fyzikálne parametre sú v procese zberu.")

  # 3. Zhrnutie pre žiaka
  lines.append("\n3. ZHRNUTIE PRE ŽIAKA:")
  lines.append(
      f"   Zapamätaj si: {nazov} patrí medzi kľúčové vedecké entity nášho"
      " vesmíru."
  )
  if definicie:
    hlavna = ocisti_a_dopln_pad(definicie[0].get("target", ""))
    lines.append(f"   Hlavná definícia: {nazov} = {hlavna}.")
  lines.append("=" * 65 + "\n")

  return "\n".join(lines)


def run_ipc_listener():
  print("[GENERATOR IPC] Čakám na požiadavky z UI panelu...")
  while True:
    try:
      if REQ_FILE.exists():
        with open(REQ_FILE, "r", encoding="utf-8") as f:
          req = json.load(f)

        subjekt = req.get("query") or req.get("subject") or req.get("text", "")
        if subjekt:
          print(f"[GENERATOR IPC] Prijatý dopyt: '{subjekt}'")
          with open(KG_PATH, "r", encoding="utf-8", errors="ignore") as f:
            kg = json.load(f)

          odpoved = formatuj_vyklad(kg, subjekt)

          IPC_DIR.mkdir(parents=True, exist_ok=True)
          with open(RESP_FILE, "w", encoding="utf-8") as f:
            json.dump(
                {
                    "status": "success",
                    "subject": subjekt,
                    "response": odpoved,
                    "timestamp": time.time(),
                },
                f,
                ensure_ascii=False,
                indent=2,
            )

          print(f"[GENERATOR IPC] Odpoveď zapísaná do {RESP_FILE.name}")
          try:
            REQ_FILE.unlink()
          except Exception:
            pass

      time.sleep(1)
    except KeyboardInterrupt:
      print("\n[GENERATOR IPC] Ukončené.")
      break
    except Exception as e:
      print(f"[GENERATOR IPC ERROR] {e}")
      time.sleep(2)


def main():
  if not KG_PATH.exists():
    print(f"[CHYBA] Súbor {KG_PATH} neexistuje.")
    return

  if len(sys.argv) > 1 and sys.argv[1] == "--listen":
    run_ipc_listener()
  else:
    tema = sys.argv[1] if len(sys.argv) > 1 else "zem"
    with open(KG_PATH, "r", encoding="utf-8", errors="ignore") as f:
      kg = json.load(f)
    print(formatuj_vyklad(kg, tema))


if __name__ == "__main__":
  main()
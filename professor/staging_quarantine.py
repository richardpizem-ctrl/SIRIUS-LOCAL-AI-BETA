import json
import os
from pathlib import Path
import time

BASE_DIR = Path(__file__).resolve().parent.parent
QUARANTINE_FILE = str(
    BASE_DIR / "COLNIK-6.x" / "envoy" / "quarantine" / "professor_staging.json"
)


class StagingQuarantine:

  def __init__(self, filepath=QUARANTINE_FILE):
    self.filepath = filepath
    os.makedirs(os.path.dirname(self.filepath), exist_ok=True)

  def load_staging(self) -> dict:
    if not os.path.exists(self.filepath):
      return {"items": {}}
    try:
      with open(self.filepath, "r", encoding="utf-8") as f:
        return json.load(f)
    except Exception:
      return {"items": {}}

  def save_staging(self, data: dict):
    with open(self.filepath, "w", encoding="utf-8") as f:
      json.dump(data, f, indent=2, ensure_ascii=False)

  def stage_triplet(
      self, source: str, relation: str, target: str, domain: str
  ) -> bool:
    data = self.load_staging()
    key = f"{source.strip().lower()}|{relation.strip().lower()}|{target.strip().lower()}"
    now = time.time()

    # Overené domény postupujú okamžite bez čakania na 3 cykly
    is_trusted_domain = bool(domain and "wikipedia.org" in domain.lower())
    initial_status = (
        "verified_multi_source" if is_trusted_domain else "provisional"
    )

    if key not in data["items"]:
      data["items"][key] = {
          "source": source.strip().lower(),
          "relation": relation.strip().lower(),
          "target": target.strip().lower(),
          "first_seen": now,
          "cycles": 1,
          "domains": [domain] if domain else [],
          "status": initial_status,
      }
    else:
      item = data["items"][key]
      item["cycles"] += 1
      if domain and domain not in item["domains"]:
        item["domains"].append(domain)

      if is_trusted_domain or item["cycles"] >= 3 or len(item["domains"]) >= 2:
        item["status"] = "verified_multi_source"

    self.save_staging(data)
    return data["items"][key]["status"] == "verified_multi_source"

  def get_promotable_triplets(self) -> list:
    data = self.load_staging()
    promotable = []
    remaining = {}

    for key, item in data.get("items", {}).items():
      if item.get("status") == "verified_multi_source":
        promotable.append({
            "source": item["source"],
            "relation": item["relation"],
            "target": item["target"],
        })
      else:
        remaining[key] = item

    data["items"] = remaining
    self.save_staging(data)
    return promotable
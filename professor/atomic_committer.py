import json
import os
from pathlib import Path
import sys
import time

BASE_DIR = Path(__file__).resolve().parent.parent

LOCK_FILE = str(BASE_DIR / "kg_lock.lock")
DEFAULT_MASTER_KG = str(BASE_DIR / "autosave_kg.json")
DEFAULT_TMP_KG = str(BASE_DIR / "autosave_kg.tmp")


class FileLockException(Exception):
  pass


class AtomicCommitter:

  def __init__(self, lock_file=LOCK_FILE, kg_path=None, tmp_kg=None):
    self.lock_file = str(lock_file)
    
    # Ak dostane konkrétnu cestu (napr. pre anglický súbor), použije ju
    if kg_path:
      self.master_kg = str(Path(kg_path).resolve())
      self.tmp_kg = str(Path(kg_path).with_suffix(".tmp"))
    else:
      self.master_kg = DEFAULT_MASTER_KG
      self.tmp_kg = DEFAULT_TMP_KG
      
    self._lock_handle = None

  def acquire_lock(self, timeout=3.0):
    start = time.time()
    while time.time() - start < timeout:
      try:
        self._lock_handle = open(self.lock_file, "w")
        if sys.platform == "win32":
          import msvcrt
          msvcrt.locking(self._lock_handle.fileno(), msvcrt.LK_NBLCK, 1)
        else:
          import fcntl
          fcntl.flock(self._lock_handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
        return True
      except (IOError, OSError):
        time.sleep(0.05)
    raise FileLockException("kg_lock.lock nie je voľný.")

  def release_lock(self):
    if self._lock_handle:
      try:
        if sys.platform == "win32":
          import msvcrt
          msvcrt.locking(self._lock_handle.fileno(), msvcrt.LK_UNLCK, 1)
        else:
          import fcntl
          fcntl.flock(self._lock_handle, fcntl.LOCK_UN)
        self._lock_handle.close()
      except Exception:
        pass
      self._lock_handle = None
      if os.path.exists(self.lock_file):
        try:
          os.remove(self.lock_file)
        except Exception:
          pass

  def commit_triplets(self, new_triplets: list) -> bool:
    if not new_triplets:
      return True
    self.acquire_lock()
    try:
      if not os.path.exists(self.master_kg):
        base_data = {"kg_version": 1, "entities": {}, "relations": []}
      else:
        with open(self.master_kg, "r", encoding="utf-8") as f:
          base_data = json.load(f)

      if base_data.get("immutable", False):
        return False

      base_version = base_data.get("kg_version", 1)
      relations = base_data.get("relations", [])
      entities = base_data.get("entities", {})
      existing_rels = {
          f"{r.get('source')}|{r.get('relation')}|{r.get('target')}"
          for r in relations
      }
      added_count = 0

      for t in new_triplets:
        sig = f"{t['source']}|{t['relation']}|{t['target']}"
        if sig not in existing_rels:
          relations.append({
              "source": t["source"],
              "relation": t["relation"],
              "target": t["target"],
          })
          if t["source"] not in entities:
            entities[t["source"]] = {
                "attributes": {
                    "nazov": t["source"].capitalize(),
                    "stav": "obohatené_cez_profesor",
                }
            }
          if t["target"] not in entities:
            entities[t["target"]] = {
                "attributes": {
                    "nazov": t["target"].capitalize(),
                    "stav": "obohatené_cez_profesor",
                }
            }
          existing_rels.add(sig)
          added_count += 1

      if added_count == 0:
        return True

      base_data["relations"] = relations
      base_data["entities"] = entities
      base_data["kg_version"] = base_version + 1

      with open(self.tmp_kg, "w", encoding="utf-8") as f:
        json.dump(base_data, f, indent=2, ensure_ascii=False)

      with open(self.tmp_kg, "r", encoding="utf-8") as f:
        verified = json.load(f)

      if "relations" not in verified:
        raise ValueError("Validacia zlyhala!")

      os.replace(self.tmp_kg, self.master_kg)
      print(
          f"[PROFESSOR ATOMIC COMMIT] Pridaných {added_count} faktov do"
          f" {Path(self.master_kg).name}. Nová verzia: {base_data['kg_version']}"
      )
      return True
    finally:
      if os.path.exists(self.tmp_kg):
        try:
          os.remove(self.tmp_kg)
        except Exception:
          pass
      self.release_lock()
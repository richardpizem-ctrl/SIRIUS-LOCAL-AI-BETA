import json
import os

# === TIMECORE — PILIER 0 ===
from timecore import TimeCore

class KGCore:
    def __init__(self):
        self.entities = {}          # { name_lower: { "name": original, "attributes": {} } }
        self.relations = []         # [ { "source": a, "relation": r, "target": b } ]

        self.timecore = TimeCore()  # <<< INTEGRÁCIA TIMECORE
        self.timecore.runtime_start()

        self.autosave_path = os.path.join(os.path.dirname(__file__), "kg_autosave.json")
        self._load_autosave()

    # ============================================================
    # ENTITY MANAGEMENT
    # ============================================================
    def add_entity(self, name: str, attributes=None):
        """Pridá entitu do KG alebo aktualizuje existujúcu."""
        self.timecore.cycle_start()   # <<< TIMECORE

        key = name.strip().lower()
        attrs = attributes or {}

        if key not in self.entities:
            self.entities[key] = {
                "name": name,
                "attributes": {}
            }

        # aktualizácia atribútov
        self.entities[key]["attributes"].update(attrs)

        # TIMECORE — zapis do KG
        self.entities[key]["attributes"]["kg_timestamp"] = self.timecore.timestamp()
        self.entities[key]["attributes"]["kg_cycle_time"] = self.timecore.cycle_delta()

        self._autosave()
        self.timecore.cycle_end()     # <<< TIMECORE
        return self.entities[key]

    def set_attribute(self, entity: str, key: str, value):
        """Nastaví atribút entity."""
        self.timecore.cycle_start()   # <<< TIMECORE

        ekey = entity.strip().lower()
        if ekey not in self.entities:
            self.add_entity(entity)

        self.entities[ekey]["attributes"][key] = value

        # TIMECORE — zapis do KG
        self.entities[ekey]["attributes"]["kg_timestamp"] = self.timecore.timestamp()
        self.entities[ekey]["attributes"]["kg_cycle_time"] = self.timecore.cycle_delta()

        self._autosave()
        self.timecore.cycle_end()     # <<< TIMECORE
        return True

    # ============================================================
    # RELATION MANAGEMENT
    # ============================================================
    def add_relation(self, source: str, relation: str, target: str):
        """Pridá reláciu medzi entitami."""
        self.timecore.cycle_start()   # <<< TIMECORE

        s_key = source.strip().lower()
        t_key = target.strip().lower()

        # zabezpečiť existenciu entít
        if s_key not in self.entities:
            self.add_entity(source)
        if t_key not in self.entities:
            self.add_entity(target)

        rel = {
            "source": self.entities[s_key]["name"],
            "relation": relation,
            "target": self.entities[t_key]["name"],
            "kg_timestamp": self.timecore.timestamp(),
            "kg_cycle_time": self.timecore.cycle_delta()
        }

        self.relations.append(rel)
        self._autosave()

        self.timecore.cycle_end()     # <<< TIMECORE
        return rel

    # ============================================================
    # AUTOSAVE / AUTOLOAD
    # ============================================================
    def _autosave(self):
        """Uloží KG do JSON súboru."""
        data = {
            "entities": self.entities,
            "relations": self.relations,
            "timecore": {
                "last_runtime_start": self.timecore.last_runtime_start,
                "last_runtime_end": self.timecore.last_runtime_end,
                "runtime_gap": self.timecore.runtime_gap()
            }
        }
        try:
            with open(self.autosave_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"[KG AUTOSAVE ERROR] {e}")

    def _load_autosave(self):
        """Načíta KG zo súboru, ak existuje."""
        if not os.path.exists(self.autosave_path):
            return

        try:
            with open(self.autosave_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            self.entities = data.get("entities", {})
            self.relations = data.get("relations", [])

        except Exception as e:
            print(f"[KG LOAD ERROR] {e}")

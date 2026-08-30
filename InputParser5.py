import re
import shlex

try:
    from runtime5.logging_5 import log5
except ImportError:
    def log5(msg):
        print(msg)

RESERVED_WORDS = {
    "kg",
    "reason",
    "envoy",
    "system",
    "workflow",
    "runtime",
    "compare",
    "fetch",
    "why",
    "help",
    "exit",
}


class InputParser5:
    """
    SIRIUS InputParser5 – hybrid 3.0 + 4.0

    - Podporuje: KG_PATH / KG_GET / KG_VIEW / KG_RELATIONS / KG_INFER / REASON_ORBITS
    - Podporuje: kg.path / kg.get / kg.view / kg.relations / kg.infer / reason.orbits
    - Podporuje: aliasy, bodky, podčiarkovníky, camelCase
    - Automaticky rozpoznáva vzory (path, get, view, relations, infer, orbits)
    - Zachováva intent / entity / args logiku RuntimeCore 5.x + Autonómia 6.x
    """

    def __init__(self):
        log5("[InputParser5] Initialized SIRIUS unified Input Parser 5.x")

    def _normalize(self, text: str) -> str:
        if not isinstance(text, str):
            return ""
        return text.strip()

    def _tokenize(self, text: str) -> list[str]:
        if not isinstance(text, str) or not text.strip():
            return []
        try:
            return shlex.split(text.strip())
        except Exception:
            return text.strip().split()

    def _is_reserved(self, name: str) -> bool:
        if not isinstance(name, str):
            return False
        n = name.strip().lower()
        if not n or n in RESERVED_WORDS:
            return True
        if n.startswith("kg ") or n.startswith("kg.") or n.startswith("reason ") or n.startswith("reason."):
            return True
        return False

    # ---------- HELPER: NORMALIZE COMMAND NAME ----------
    def _cmd_name(self, token: str) -> str:
        """
        Normalizuje príkaz:
        - KG_PATH, kg_path, kg.path, KgPath, kgPath, KG.PATH, kg PATH -> 'kg.path'
        - KG_GET, kg_get, kg.get, KgGet, kgGet, KG.GET, kg GET -> 'kg.get'
        - KG_VIEW, kg_view, kg.view, KgView, kgView -> 'kg.view'
        - KG_RELATIONS, kg_relations, kg.relations -> 'kg.relations'
        - KG_INFER, kg_infer, kg.infer -> 'kg.infer'
        - REASON_ORBITS, reason_orbits, reason.orbits -> 'reason.orbits'
        """
        t = token.strip()
        low = t.lower()

        # remove non-alnum separators for pattern detection
        core = re.sub(r'[^a-z0-9]', '', low)

        # KG PATH / kg_path / kg.path / KgPath / kgPath / KG.PATH
        if core in ["kgpath", "path"]:
            return "kg.path"

        if core in ["kgget", "get"]:
            return "kg.get"

        if core in ["kgview", "view"]:
            return "kg.view"

        if core in ["kgrelations", "relations"]:
            return "kg.relations"

        if core in ["kginfer", "infer"]:
            return "kg.infer"

        if core in ["reasonorbits", "orbits"]:
            return "reason.orbits"

        if low in ["kg", "reason"]:
            return low

        return low

    def parse(self, raw_input: str) -> dict:
        raw_cleaned = self._normalize(raw_input)

        result = {
            "intent": "UNKNOWN",
            "entity": None,
            "args": {},
            "raw": raw_input,
            "normalized": raw_cleaned.lower(),
        }

        if not raw_cleaned:
            return result

        tokens = self._tokenize(raw_cleaned)
        if not tokens:
            return result

        raw_lower = raw_cleaned.lower()
        cmd_raw = tokens[0]
        cmd = self._cmd_name(cmd_raw)

        # ====================================================
        # 0. ZJEDNOTENÉ KG / REASON PRÍKAZY (HYBRID 3.0 + 4.0)
        # ====================================================

        # ---------- KG.PATH ----------
        if cmd == "kg.path" or (cmd == "kg" and len(tokens) > 1 and self._cmd_name(tokens[1]) == "kg.path"):
            # formáty:
            # KG_PATH src tgt
            # kg.path src tgt
            # kg path src tgt
            # path src tgt
            if cmd == "kg.path" and len(tokens) >= 3:
                src = tokens[1]
                tgt = tokens[2]
            elif cmd == "kg" and len(tokens) >= 4 and self._cmd_name(tokens[1]) == "kg.path":
                src = tokens[2]
                tgt = tokens[3]
            elif self._cmd_name(cmd_raw) == "kg.path" and len(tokens) >= 3:
                src = tokens[1]
                tgt = tokens[2]
            else:
                src = None
                tgt = None

            if src and tgt and not self._is_reserved(src) and not self._is_reserved(tgt):
                return {
                    "intent": "kg.path",
                    "entity": src,
                    "args": {"source": src, "target": tgt, "mode": "developer"},
                    "raw": raw_input,
                    "normalized": raw_lower,
                }

        # ---------- KG.GET ----------
        if cmd == "kg.get" or (cmd == "kg" and len(tokens) > 1 and self._cmd_name(tokens[1]) == "kg.get"):
            # KG_GET entity attr
            # kg.get entity attr
            # kg get entity attr
            if cmd == "kg.get" and len(tokens) >= 3:
                entity = tokens[1]
                attribute = tokens[2]
            elif cmd == "kg" and len(tokens) >= 4 and self._cmd_name(tokens[1]) == "kg.get":
                entity = tokens[2]
                attribute = tokens[3]
            else:
                entity = None
                attribute = None

            if entity and attribute and not self._is_reserved(entity):
                return {
                    "intent": "kg.get",
                    "entity": entity,
                    "args": {
                        "entity": entity,
                        "attribute": attribute,
                        "key": attribute,
                        "mode": "developer",
                    },
                    "raw": raw_input,
                    "normalized": raw_lower,
                }

        # ---------- KG.VIEW ----------
        if cmd == "kg.view" or (cmd == "kg" and len(tokens) > 1 and self._cmd_name(tokens[1]) == "kg.view"):
            # KG_VIEW entity
            # kg.view entity
            # kg view entity
            if cmd == "kg.view" and len(tokens) >= 2:
                entity = tokens[1]
            elif cmd == "kg" and len(tokens) >= 3 and self._cmd_name(tokens[1]) == "kg.view":
                entity = tokens[2]
            else:
                entity = None

            if entity and not self._is_reserved(entity):
                return {
                    "intent": "kg.view",
                    "entity": entity,
                    "args": {"entity": entity, "mode": "developer"},
                    "raw": raw_input,
                    "normalized": raw_lower,
                }

        # ---------- KG.RELATIONS ----------
        if cmd == "kg.relations" or (cmd == "kg" and len(tokens) > 1 and self._cmd_name(tokens[1]) == "kg.relations"):
            # KG_RELATIONS entity
            # kg.relations entity
            # kg relations entity
            if cmd == "kg.relations" and len(tokens) >= 2:
                entity = tokens[1]
            elif cmd == "kg" and len(tokens) >= 3 and self._cmd_name(tokens[1]) == "kg.relations":
                entity = tokens[2]
            else:
                entity = None

            if entity and not self._is_reserved(entity):
                return {
                    "intent": "kg.relations",
                    "entity": entity,
                    "args": {"entity": entity, "mode": "developer"},
                    "raw": raw_input,
                    "normalized": raw_lower,
                }

        # ---------- KG.INFER ----------
        if cmd == "kg.infer" or cmd == "infer" or (cmd == "kg" and len(tokens) > 1 and self._cmd_name(tokens[1]) == "kg.infer") \
           or cmd == "reason.infer" or (cmd == "reason" and len(tokens) > 1 and self._cmd_name(tokens[1]) == "kg.infer"):
            # KG_INFER entity
            if self._cmd_name(cmd_raw) == "kg.infer" and len(tokens) == 2:
                entity = tokens[1]
                if not self._is_reserved(entity):
                    return {
                        "intent": "kg.infer",
                        "entity": entity,
                        "args": {"entity": entity, "mode": "developer"},
                        "raw": raw_input,
                        "normalized": raw_lower,
                    }
            return {
                "intent": "kg.infer",
                "entity": None,
                "args": {"mode": "developer"},
                "raw": raw_input,
                "normalized": raw_lower,
            }

        # ---------- REASON.ORBITS ----------
        if cmd == "reason.orbits" or (cmd == "reason" and len(tokens) > 1 and self._cmd_name(tokens[1]) == "reason.orbits"):
            # REASON_ORBITS entity
            # reason.orbits entity
            # reason orbits entity
            if self._cmd_name(cmd_raw) == "reason.orbits" and len(tokens) == 2:
                entity = tokens[1]
            elif cmd == "reason" and len(tokens) >= 3 and self._cmd_name(tokens[1]) == "reason.orbits":
                entity = tokens[2]
            else:
                entity = None

            if entity and not self._is_reserved(entity):
                return {
                    "intent": "reason.orbits",
                    "entity": entity,
                    "args": {"entity": entity, "mode": "developer"},
                    "raw": raw_input,
                    "normalized": raw_lower,
                }

        # ====================================================
        # 1. STARÁ DOT LOGIKA – ZACHOVANÁ (RELATE, REMOVE_RELATION, SET, UNSET, MERGE, SEARCH, EXPLAIN…)
        # ====================================================

        # KG RELATE
        if raw_lower.startswith("kg.relate "):
            parts = raw_input.split()
            if len(parts) == 4:
                src, rel, tgt = parts[1], parts[2], parts[3]
                if not self._is_reserved(src) and not self._is_reserved(tgt):
                    return {
                        "intent": "kg.relate",
                        "entity": src,
                        "args": {
                            "source": src,
                            "relation": rel,
                            "target": tgt,
                            "mode": "developer",
                        },
                        "raw": raw_input,
                        "normalized": raw_lower,
                    }

        if raw_lower.startswith("kg relate "):
            parts = raw_input.split()
            if len(parts) == 5:
                src = parts[2]
                a = parts[3]
                b = parts[4]

                RELATION_WORDS = {
                    "je", "ma", "má", "ma_vlastnost", "patri_do", "patrí_do",
                    "obsahuje", "je_typ", "je_cast", "je_podtyp",
                    "je_instance", "je_kategoria", "je_kategória"
                }

                if a.lower() in RELATION_WORDS:
                    rel, tgt = a, b
                elif b.lower() in RELATION_WORDS:
                    rel, tgt = b, a
                else:
                    rel, tgt = a, b

                if not self._is_reserved(src) and not self._is_reserved(tgt):
                    return {
                        "intent": "kg.relate",
                        "entity": src,
                        "args": {
                            "source": src,
                            "relation": rel,
                            "target": tgt,
                            "mode": "developer",
                        },
                        "raw": raw_input,
                        "normalized": raw_lower,
                    }

        # KG REMOVE_RELATION
        if raw_lower.startswith("kg.remove_relation ") or raw_lower.startswith("kg remove_relation "):
            parts = raw_input.split()
            if len(parts) >= 4:
                src, rel, tgt = parts[1], parts[2], parts[3]
                if not self._is_reserved(src) and not self._is_reserved(tgt):
                    return {
                        "intent": "kg.remove_relation",
                        "entity": src,
                        "args": {
                            "source": src,
                            "relation": rel,
                            "target": tgt,
                            "mode": "developer",
                        },
                        "raw": raw_input,
                        "normalized": raw_lower,
                    }

        # KG EXPLAIN
        if raw_lower.startswith("kg.explain "):
            parts = raw_input.split()
            if len(parts) >= 2:
                entity = parts[1]
                if not self._is_reserved(entity):
                    return {
                        "intent": "kg.explain",
                        "entity": entity,
                        "args": {"target": entity, "mode": "developer"},
                        "raw": raw_input,
                        "normalized": raw_lower,
                    }

        if raw_lower.startswith("kg explain "):
            parts = raw_input.split()
            if len(parts) >= 3:
                entity = parts[2]
                if not self._is_reserved(entity):
                    return {
                        "intent": "kg.explain",
                        "entity": entity,
                        "args": {"target": entity, "mode": "developer"},
                        "raw": raw_input,
                        "normalized": raw_lower,
                    }

        # KG EXPLAIN_DEEP
        if raw_lower.startswith("kg.explain_deep "):
            parts = raw_input.split()
            if len(parts) >= 2:
                entity = parts[1]
                if not self._is_reserved(entity):
                    return {
                        "intent": "kg.explain_deep",
                        "entity": entity,
                        "args": {"entity": entity, "mode": "developer"},
                        "raw": raw_input,
                        "normalized": raw_lower,
                    }

        if raw_lower.startswith("kg explain_deep "):
            parts = raw_input.split()
            if len(parts) >= 3:
                entity = parts[2]
                if not self._is_reserved(entity):
                    return {
                        "intent": "kg.explain_deep",
                        "entity": entity,
                        "args": {"entity": entity, "mode": "developer"},
                        "raw": raw_input,
                        "normalized": raw_lower,
                    }

        # KG EXPLORE
        if raw_lower.startswith("kg.explore "):
            parts = raw_input.split()
            if len(parts) >= 2:
                entity = parts[1]
                if not self._is_reserved(entity):
                    return {
                        "intent": "kg.explore",
                        "entity": entity,
                        "args": {"entity": entity, "mode": "developer"},
                        "raw": raw_input,
                        "normalized": raw_lower,
                    }

        if raw_lower.startswith("kg explore "):
            parts = raw_input.split()
            if len(parts) >= 3:
                entity = parts[2]
                if not self._is_reserved(entity):
                    return {
                        "intent": "kg.explore",
                        "entity": entity,
                        "args": {"entity": entity, "mode": "developer"},
                        "raw": raw_input,
                        "normalized": raw_lower,
                    }

        # KG ATTRIBUTES
        if raw_lower.startswith("kg.attributes "):
            parts = raw_input.split()
            if len(parts) >= 2:
                entity = parts[1]
                if not self._is_reserved(entity):
                    return {
                        "intent": "kg.attributes",
                        "entity": entity,
                        "args": {"entity": entity, "mode": "developer"},
                        "raw": raw_input,
                        "normalized": raw_lower,
                    }

        if raw_lower.startswith("kg attributes "):
            parts = raw_input.split()
            if len(parts) >= 3:
                entity = parts[2]
                if not self._is_reserved(entity):
                    return {
                        "intent": "kg.attributes",
                        "entity": entity,
                        "args": {"entity": entity, "mode": "developer"},
                        "raw": raw_input,
                        "normalized": raw_lower,
                    }

        # KG ADD
        if raw_lower.startswith("kg.add "):
            parts = raw_input.split()
            if len(parts) >= 2:
                entity = parts[1]
                if not self._is_reserved(entity):
                    return {
                        "intent": "kg.add",
                        "entity": entity,
                        "args": {"entity": entity, "mode": "developer"},
                        "raw": raw_input,
                        "normalized": raw_lower,
                    }

        if raw_lower.startswith("kg add "):
            parts = raw_input.split()
            if len(parts) >= 3:
                entity = parts[2]
                if not self._is_reserved(entity):
                    return {
                        "intent": "kg.add",
                        "entity": entity,
                        "args": {"entity": entity, "mode": "developer"},
                        "raw": raw_input,
                        "normalized": raw_lower,
                    }

        # KG REMOVE
        if raw_lower.startswith("kg.remove "):
            parts = raw_input.split()
            if len(parts) >= 2:
                entity = parts[1]
                if not self._is_reserved(entity):
                    return {
                        "intent": "kg.remove",
                        "entity": entity,
                        "args": {"entity": entity, "mode": "developer"},
                        "raw": raw_input,
                        "normalized": raw_lower,
                    }

        if raw_lower.startswith("kg remove "):
            parts = raw_input.split()
            if len(parts) >= 3:
                entity = parts[2]
                if not self._is_reserved(entity):
                    return {
                        "intent": "kg.remove",
                        "entity": entity,
                        "args": {"entity": entity, "mode": "developer"},
                        "raw": raw_input,
                        "normalized": raw_lower,
                    }

        # KG DELETE
        if raw_lower.startswith("kg.delete "):
            parts = raw_input.split()
            if len(parts) == 2:
                entity = parts[1]
                if not self._is_reserved(entity):
                    return {
                        "intent": "kg.delete",
                        "entity": entity,
                        "args": {"entity": entity, "mode": "developer"},
                        "raw": raw_input,
                        "normalized": raw_lower,
                    }

        if raw_lower.startswith("kg delete "):
            parts = raw_input.split()
            if len(parts) >= 3:
                entity = parts[2]
                if not self._is_reserved(entity):
                    return {
                        "intent": "kg.delete",
                        "entity": entity,
                        "args": {"entity": entity, "mode": "developer"},
                        "raw": raw_input,
                        "normalized": raw_lower,
                    }

        # KG MERGE
        if raw_lower.startswith("kg.merge "):
            parts = raw_input.split()
            if len(parts) == 3:
                source, target = parts[1], parts[2]
                if not self._is_reserved(source) and not self._is_reserved(target):
                    return {
                        "intent": "kg.merge",
                        "entity": target,
                        "args": {"source": source, "target": target, "mode": "developer"},
                        "raw": raw_input,
                        "normalized": raw_lower,
                    }

        if raw_lower.startswith("kg merge "):
            parts = raw_input.split()
            if len(parts) == 4:
                source, target = parts[2], parts[3]
                if not self._is_reserved(source) and not self._is_reserved(target):
                    return {
                        "intent": "kg.merge",
                        "entity": target,
                        "args": {"source": source, "target": target, "mode": "developer"},
                        "raw": raw_input,
                        "normalized": raw_lower,
                    }

        # KG QUERY
        if raw_lower.startswith("kg.query "):
            parts = raw_input.split()
            if len(parts) >= 2:
                entity = parts[1]
                if not self._is_reserved(entity):
                    return {
                        "intent": "kg.query",
                        "entity": entity,
                        "args": {"entity": entity, "mode": "developer"},
                        "raw": raw_input,
                        "normalized": raw_lower,
                    }

        if raw_lower.startswith("kg query "):
            parts = raw_input.split()
            if len(parts) >= 3:
                entity = parts[2]
                if not self._is_reserved(entity):
                    return {
                        "intent": "kg.query",
                        "entity": entity,
                        "args": {"entity": entity, "mode": "developer"},
                        "raw": raw_input,
                        "normalized": raw_lower,
                    }

        # KG SET
        if raw_lower.startswith("kg set "):
            parts = raw_input.split()
            if len(parts) >= 5:
                entity = parts[2].strip('"')
                attribute = parts[3].strip('"')
                value = " ".join(parts[4:]).strip('"')
                if not self._is_reserved(entity):
                    return {
                        "intent": "kg.set",
                        "entity": entity,
                        "args": {
                            "entity": entity,
                            "attribute": attribute,
                            "value": value,
                            "mode": "developer",
                        },
                        "raw": raw_input,
                        "normalized": raw_lower,
                    }

        if raw_lower.startswith("kg.set "):
            parts = raw_input.split()
            if len(parts) >= 4:
                entity = parts[1].strip('"')
                attribute = parts[2].strip('"')
                value = " ".join(parts[3:]).strip('"')
                if not self._is_reserved(entity):
                    return {
                        "intent": "kg.set",
                        "entity": entity,
                        "args": {
                            "entity": entity,
                            "attribute": attribute,
                            "value": value,
                            "mode": "developer",
                        },
                        "raw": raw_input,
                        "normalized": raw_lower,
                    }

        # KG GET (dot variant – už pokryté vyššie, ale nechávame kvôli kompatibilite)
        if raw_lower.startswith("kg get "):
            parts = raw_input.split()
            if len(parts) >= 4:
                entity = parts[2].strip('"')
                attribute = parts[3].strip('"')
                if not self._is_reserved(entity):
                    return {
                        "intent": "kg.get",
                        "entity": entity,
                        "args": {
                            "entity": entity,
                            "attribute": attribute,
                            "key": attribute,
                            "mode": "developer",
                        },
                        "raw": raw_input,
                        "normalized": raw_lower,
                    }

        if raw_lower.startswith("kg.get "):
            parts = raw_input.split()
            if len(parts) >= 3:
                entity = parts[1].strip('"')
                attribute = parts[2].strip('"')
                if not self._is_reserved(entity):
                    return {
                        "intent": "kg.get",
                        "entity": entity,
                        "args": {
                            "entity": entity,
                            "attribute": attribute,
                            "key": attribute,
                            "mode": "developer",
                        },
                        "raw": raw_input,
                        "normalized": raw_lower,
                    }

        # KG UNSET
        if raw_lower.startswith("kg unset "):
            parts = raw_input.split()
            if len(parts) >= 4:
                entity = parts[2].strip('"')
                attribute = parts[3].strip('"')
                if not self._is_reserved(entity):
                    return {
                        "intent": "kg.unset",
                        "entity": entity,
                        "args": {
                            "entity": entity,
                            "attribute": attribute,
                            "key": attribute,
                            "mode": "developer",
                        },
                        "raw": raw_input,
                        "normalized": raw_lower,
                    }

        if raw_lower.startswith("kg.unset "):
            parts = raw_input.split()
            if len(parts) >= 3:
                entity = parts[1].strip('"')
                attribute = parts[2].strip('"'
                )
                if not self._is_reserved(entity):
                    return {
                        "intent": "kg.unset",
                        "entity": entity,
                        "args": {
                            "entity": entity,
                            "attribute": attribute,
                            "key": attribute,
                            "mode": "developer",
                        },
                        "raw": raw_input,
                        "normalized": raw_lower,
                    }

        # ====================================================
        # 2. REASON WHY (dot + natural)
        # ====================================================

        if raw_lower.startswith("reason.why ") or raw_lower.startswith("reason why ") or raw_lower.startswith("why "):
            parts = raw_input.strip().split()
            if parts[0].lower() == "why":
                if len(parts) == 2:
                    entity = parts[1]
                    if not self._is_reserved(entity):
                        return {
                            "intent": "reason.why",
                            "entity": entity,
                            "args": {"entity": entity, "hypothesis": None, "mode": "developer"},
                            "raw": raw_input,
                            "normalized": raw_lower,
                        }
                if len(parts) >= 3:
                    entity = parts[1]
                    if not self._is_reserved(entity):
                        hypothesis = " ".join(parts[1:])
                        return {
                            "intent": "reason.why",
                            "entity": entity,
                            "args": {"entity": entity, "hypothesis": hypothesis, "mode": "developer"},
                            "raw": raw_input,
                            "normalized": raw_lower,
                        }
            else:
                # reason.why / reason why
                if len(parts) == 2:
                    entity = parts[1]
                    if not self._is_reserved(entity):
                        return {
                            "intent": "reason.why",
                            "entity": entity,
                            "args": {"entity": entity, "hypothesis": None, "mode": "developer"},
                            "raw": raw_input,
                            "normalized": raw_lower,
                        }
                if len(parts) >= 4:
                    entity = parts[1] if parts[0].lower() == "reason.why" else parts[2]
                    if not self._is_reserved(entity):
                        hypothesis = " ".join(parts[1:]) if parts[0].lower() == "reason.why" else " ".join(parts[2:])
                        return {
                            "intent": "reason.why",
                            "entity": entity,
                            "args": {"entity": entity, "hypothesis": hypothesis, "mode": "developer"},
                            "raw": raw_input,
                            "normalized": raw_lower,
                        }

        # ====================================================
        # 3. NLP FALLBACKS (natural language)
        # ====================================================

        # Vzťahy / cesta medzi dvoma entitami
        match_rel = re.search(r'(?:ako súvisí|vzťah medzi|cesta z|prepojenie)\s+(.+?)\s+(?:s|a|do)\s+(.+)', raw_lower, re.IGNORECASE)
        if match_rel:
            src, tgt = match_rel.group(1).strip(), match_rel.group(2).strip()
            return {
                "intent": "kg.path",
                "entity": src,
                "args": {"source": src, "target": tgt, "mode": "natural"},
                "raw": raw_input,
                "normalized": raw_lower,
            }

        # Prečo / Why (natural)
        match_why = re.search(r'^(?:prečo|why)\s+(is|je|sa|má)?\s*(.+)', raw_lower, re.IGNORECASE)
        if match_why:
            content = match_why.group(2).strip()
            parts = content.split()
            entity = parts[0] if parts else content
            hypothesis = " ".join(parts[1:]) if len(parts) > 1 else None
            return {
                "intent": "reason.why",
                "entity": entity,
                "args": {"entity": entity, "hypothesis": hypothesis, "mode": "natural"},
                "raw": raw_input,
                "normalized": raw_lower,
            }

        # Vyhľadávanie: ukáž, hľadaj, find, show
        match_search = re.search(r'^(?:ukáž|ukaz|zoznam|hľadaj|hladaj|find|show)\s+(.+)', raw_lower, re.IGNORECASE)
        if match_search:
            target = match_search.group(1).strip()
            return {
                "intent": "kg.explore",
                "entity": target,
                "args": {"entity": target, "target": target, "mode": "natural"},
                "raw": raw_input,
                "normalized": raw_lower,
            }

        # Jednoslovný vstup = dopyt na entity
        if len(tokens) == 1 and not self._is_reserved(tokens[0]):
            entity = tokens[0]
            return {
                "intent": "kg.relations",
                "entity": entity,
                "args": {"entity": entity, "target": entity, "mode": "natural"},
                "raw": raw_input,
                "normalized": raw_lower,
            }

        # ====================================================
        # 4. FALLBACK
        # ====================================================
        return result

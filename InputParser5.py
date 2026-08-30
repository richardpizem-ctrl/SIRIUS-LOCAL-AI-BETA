from runtime5.logging_5 import log5

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
}

class InputParser5:
    """
    Input Parser 5.x – stabilná, deterministická, kompatibilná s RuntimeCore 5.x,
    KGReasoner, KG routerom a workflow registry.
    """

    def __init__(self):
        log5("[InputParser5] Initialized Input Parser 5.x")

    def _normalize(self, text: str) -> str:
        if not isinstance(text, str):
            return ""
        return text.strip().lower()

    def _tokenize(self, text: str):
        clean = text.strip()
        return clean.split()

    def _is_reserved(self, name: str) -> bool:
        if not isinstance(name, str):
            return False
        n = name.strip().lower()
        if not n:
            return False
        if n in RESERVED_WORDS:
            return True
        if n.startswith("kg ") or n.startswith("kg.") \
           or n.startswith("reason ") or n.startswith("reason."):
            return True
        return False

    def parse(self, raw_input: str) -> dict:

        if not isinstance(raw_input, str):
            return {
                "intent": "UNKNOWN",
                "entity": None,
                "args": {},
                "raw": raw_input,
                "normalized": "",
            }

        clean = self._normalize(raw_input)
        tokens = self._tokenize(raw_input)
        raw_lower = raw_input.lower()

        result = {
            "intent": "UNKNOWN",
            "entity": None,
            "args": {},
            "raw": raw_input,
            "normalized": clean,
        }

        # ====================================================
        # ⭐⭐⭐ KG RELATE (OPRAVENÉ) ⭐⭐⭐
        # ====================================================
        if raw_lower.startswith("kg.relate "):
            parts = raw_input.split()
            if len(parts) == 4:
                src = parts[1]
                rel = parts[2]
                tgt = parts[3]
                if self._is_reserved(src) or self._is_reserved(tgt):
                    return result
                return {
                    "intent": "kg.relate",
                    "entity": src,
                    "args": {
                        "source": src,
                        "relation": rel,
                        "target": tgt,
                        "mode": "developer",
                    },
                }

        if raw_lower.startswith("kg relate "):
            parts = raw_input.split()

            # Očakávané formáty:
            # kg relate <src> <rel> <tgt>
            # kg relate <src> <tgt> <rel>
            if len(parts) == 5:
                src = parts[2]
                a = parts[3]
                b = parts[4]

                RELATION_WORDS = {
                    "je", "ma", "má", "ma_vlastnost", "patri_do", "patrí_do",
                    "obsahuje", "je_typ", "je_cast", "je_podtyp",
                    "je_instance", "je_kategoria", "je_kategória"
                }

                # a = relation?
                if a.lower() in RELATION_WORDS:
                    rel = a
                    tgt = b

                # b = relation?
                elif b.lower() in RELATION_WORDS:
                    rel = b
                    tgt = a

                # fallback
                else:
                    rel = a
                    tgt = b

                if self._is_reserved(src) or self._is_reserved(tgt):
                    return result

                return {
                    "intent": "kg.relate",
                    "entity": src,
                    "args": {
                        "source": src,
                        "relation": rel,
                        "target": tgt,
                        "mode": "developer",
                    },
                }

        # ====================================================
        # ⭐⭐⭐ KG REMOVE_RELATION ⭐⭐⭐
        # ====================================================
        if clean.startswith("kg.remove_relation "):
            if len(tokens) >= 4:
                src = tokens[1]
                rel = tokens[2]
                tgt = tokens[3]
                if self._is_reserved(src) or self._is_reserved(tgt):
                    return result
                return {
                    "intent": "kg.remove_relation",
                    "entity": src,
                    "args": {
                        "source": src,
                        "relation": rel,
                        "target": tgt,
                        "mode": "developer",
                    },
                }

        if clean.startswith("kg remove_relation "):
            if len(tokens) >= 5:
                src = tokens[2]
                rel = tokens[3]
                tgt = tokens[4]
                if self._is_reserved(src) or self._is_reserved(tgt):
                    return result
                return {
                    "intent": "kg.remove_relation",
                    "entity": src,
                    "args": {
                        "source": src,
                        "relation": rel,
                        "target": tgt,
                        "mode": "developer",
                    },
                }

        # ====================================================
        # ⭐⭐⭐ KG RELATIONS ⭐⭐⭐
        # ====================================================
        if clean.startswith("kg.relations "):
            if len(tokens) >= 2:
                entity = tokens[1]
                if self._is_reserved(entity):
                    return result
                return {
                    "intent": "kg.relations",
                    "entity": entity,
                    "args": {"entity": entity, "mode": "developer"},
                }

        if clean.startswith("kg relations "):
            if len(tokens) >= 3:
                entity = tokens[2]
                if self._is_reserved(entity):
                    return result
                return {
                    "intent": "kg.relations",
                    "entity": entity,
                    "args": {"entity": entity, "mode": "developer"},
                }

        # ====================================================
        # ⭐⭐⭐ KG EXPLAIN ⭐⭐⭐
        # ====================================================
        if clean.startswith("kg.explain "):
            if len(tokens) >= 2:
                entity = tokens[1]
                if self._is_reserved(entity):
                    return result
                return {
                    "intent": "kg.explain",
                    "entity": entity,
                    "args": {"target": entity, "mode": "developer"},
                }

        if clean.startswith("kg explain "):
            if len(tokens) >= 3:
                entity = tokens[2]
                if self._is_reserved(entity):
                    return result
                return {
                    "intent": "kg.explain",
                    "entity": entity,
                    "args": {"target": entity, "mode": "developer"},
                }

        # ====================================================
        # ⭐⭐⭐ KG EXPLAIN_DEEP ⭐⭐⭐
        # ====================================================
        if clean.startswith("kg.explain_deep "):
            if len(tokens) >= 2:
                entity = tokens[1]
                if self._is_reserved(entity):
                    return result
                return {
                    "intent": "kg.explain_deep",
                    "entity": entity,
                    "args": {"entity": entity, "mode": "developer"},
                }

        if clean.startswith("kg explain_deep "):
            if len(tokens) >= 3:
                entity = tokens[2]
                if self._is_reserved(entity):
                    return result
                return {
                    "intent": "kg.explain_deep",
                    "entity": entity,
                    "args": {"entity": entity, "mode": "developer"},
                }

        # ====================================================
        # ⭐⭐⭐ KG EXPLORE ⭐⭐⭐
        # ====================================================
        if clean.startswith("kg.explore "):
            if len(tokens) >= 2:
                entity = tokens[1]
                if self._is_reserved(entity):
                    return result
                return {
                    "intent": "kg.explore",
                    "entity": entity,
                    "args": {"entity": entity, "mode": "developer"},
                }

        if clean.startswith("kg explore "):
            if len(tokens) >= 3:
                entity = tokens[2]
                if self._is_reserved(entity):
                    return result
                return {
                    "intent": "kg.explore",
                    "entity": entity,
                    "args": {"entity": entity, "mode": "developer"},
                }

        # ====================================================
        # ⭐⭐⭐ KG INFER ⭐⭐⭐
        # ====================================================
        if clean == "kg.infer":
            return {
                "intent": "kg.infer",
                "entity": None,
                "args": {"mode": "developer"},
            }

        if clean.startswith("kg infer"):
            return {
                "intent": "kg.infer",
                "entity": None,
                "args": {"mode": "developer"},
            }

        if clean == "infer":
            return {
                "intent": "kg.infer",
                "entity": None,
                "args": {"mode": "developer"},
            }

        # ====================================================
        # ⭐⭐⭐ REASON WHY ⭐⭐⭐
        # ====================================================
        if clean.startswith("reason.why "):
            parts = raw_input.strip().split()
            if len(parts) == 2:
                entity = parts[1]
                if self._is_reserved(entity):
                    return result
                return {
                    "intent": "reason.why",
                    "entity": entity,
                    "args": {"entity": entity, "hypothesis": None, "mode": "developer"},
                }
            if len(parts) >= 4:
                entity = parts[1]
                if self._is_reserved(entity):
                    return result
                hypothesis = " ".join(parts[1:])
                return {
                    "intent": "reason.why",
                    "entity": entity,
                    "args": {
                        "entity": entity,
                        "hypothesis": hypothesis,
                        "mode": "developer",
                    },
                }

        if clean.startswith("reason why "):
            parts = raw_input.strip().split()
            if len(parts) == 3:
                entity = parts[2]
                if self._is_reserved(entity):
                    return result
                return {
                    "intent": "reason.why",
                    "entity": entity,
                    "args": {"entity": entity, "hypothesis": None, "mode": "developer"},
                }
            if len(parts) >= 4:
                entity = parts[2]
                if self._is_reserved(entity):
                    return result
                hypothesis = " ".join(parts[2:])
                return {
                    "intent": "reason.why",
                    "entity": entity,
                    "args": {
                        "entity": entity,
                        "hypothesis": hypothesis,
                        "mode": "developer",
                    },
                }

        if clean.startswith("why "):
            parts = raw_input.strip().split()
            if len(parts) == 2:
                entity = parts[1]
                if self._is_reserved(entity):
                    return result
                return {
                    "intent": "reason.why",
                    "entity": entity,
                    "args": {"entity": entity, "hypothesis": None, "mode": "developer"},
                }
            if len(parts) >= 3:
                entity = parts[1]
                if self._is_reserved(entity):
                    return result
                hypothesis = " ".join(parts[1:])
                return {
                    "intent": "reason.why",
                    "entity": entity,
                    "args": {
                        "entity": entity,
                        "hypothesis": hypothesis,
                        "mode": "developer",
                    },
                }

        # ====================================================
        # ⭐⭐⭐ REASON ORBITS ⭐⭐⭐
        # ====================================================
        if clean.startswith("reason.orbits "):
            parts = raw_input.split()
            if len(parts) == 2:
                entity = parts[1]
                if self._is_reserved(entity):
                    return result
                return {
                    "intent": "reason.orbits",
                    "entity": entity,
                    "args": {
                        "entity": entity,
                        "mode": "developer",
                    },
                }

        if clean.startswith("reason orbits "):
            parts = raw_input.split()
            if len(parts) >= 3:
                entity = parts[2]
                if self._is_reserved(entity):
                    return result
                return {
                    "intent": "reason.orbits",
                    "entity": entity,
                    "args": {
                        "entity": entity,
                        "mode": "developer",
                    },
                }

        # ====================================================
        # ⭐⭐⭐ REASON INFER ⭐⭐⭐
        # ====================================================
        if clean.startswith("reason.infer"):
            return {
                "intent": "reason.infer",
                "entity": None,
                "args": {"mode": "developer"},
            }

        if clean.startswith("reason infer"):
            return {
                "intent": "reason.infer",
                "entity": None,
                "args": {"mode": "developer"},
            }

        if clean == "infer":
            return {
                "intent": "reason.infer",
                "entity": None,
                "args": {"mode": "developer"},
            }

        # ====================================================
        # ⭐⭐⭐ KG VIEW ⭐⭐⭐
        # ====================================================
        if clean.startswith("kg.view "):
            if len(tokens) >= 2:
                entity = tokens[1]
                if self._is_reserved(entity):
                    return result
                return {
                    "intent": "kg.view",
                    "entity": entity,
                    "args": {"entity": entity, "mode": "developer"},
                }

        if clean.startswith("kg view "):
            if len(tokens) >= 3:
                entity = tokens[2]
                if self._is_reserved(entity):
                    return result
                return {
                    "intent": "kg.view",
                    "entity": entity,
                    "args": {"entity": entity, "mode": "developer"},
                }

        # ====================================================
        # ⭐⭐⭐ KG PATH ⭐⭐⭐
        # ====================================================
        if clean.startswith("kg.path "):
            parts = raw_input.split()
            if len(parts) >= 3:
                src = parts[1]
                tgt = parts[2]
                if self._is_reserved(src) or self._is_reserved(tgt):
                    return result
                return {
                    "intent": "kg.path",
                    "entity": src,
                    "args": {
                        "source": src,
                        "target": tgt,
                        "mode": "developer",
                    },
                }

        if clean.startswith("kg path "):
            parts = raw_input.split()
            if len(parts) >= 4:
                src = parts[2]
                tgt = parts[-1]
                if self._is_reserved(src) or self._is_reserved(tgt):
                    return result
                return {
                    "intent": "kg.path",
                    "entity": src,
                    "args": {
                        "source": src,
                        "target": tgt,
                        "mode": "developer",
                    },
                }

        # ====================================================
        # ⭐⭐⭐ KG ATTRIBUTES ⭐⭐⭐
        # ====================================================
        if clean.startswith("kg.attributes "):
            if len(tokens) >= 2:
                entity = tokens[1]
                if self._is_reserved(entity):
                    return result
                return {
                    "intent": "kg.attributes",
                    "entity": entity,
                    "args": {"entity": entity, "mode": "developer"},
                }

        if clean.startswith("kg attributes "):
            if len(tokens) >= 3:
                entity = tokens[2]
                if self._is_reserved(entity):
                    return result
                return {
                    "intent": "kg.attributes",
                    "entity": entity,
                    "args": {"entity": entity, "mode": "developer"},
                }

        # ====================================================
        # ⭐⭐⭐ KG ADD ⭐⭐⭐
        # ====================================================
        if clean.startswith("kg.add "):
            if len(tokens) >= 2:
                entity = tokens[1]
                if self._is_reserved(entity):
                    return result
                return {
                    "intent": "kg.add",
                    "entity": entity,
                    "args": {"entity": entity, "mode": "developer"},
                }

        if clean.startswith("kg add "):
            if len(tokens) >= 3:
                entity = tokens[2]
                if self._is_reserved(entity):
                    return result
                return {
                    "intent": "kg.add",
                    "entity": entity,
                    "args": {"entity": entity, "mode": "developer"},
                }

        # ====================================================
        # ⭐⭐⭐ KG REMOVE ⭐⭐⭐
        # ====================================================
        if clean.startswith("kg.remove "):
            if len(tokens) >= 2:
                entity = tokens[1]
                if self._is_reserved(entity):
                    return result
                return {
                    "intent": "kg.remove",
                    "entity": entity,
                    "args": {"entity": entity, "mode": "developer"},
                }

        if clean.startswith("kg remove "):
            if len(tokens) >= 3:
                entity = tokens[2]
                if self._is_reserved(entity):
                    return result
                return {
                    "intent": "kg.remove",
                    "entity": entity,
                    "args": {"entity": entity, "mode": "developer"},
                }

        # ====================================================
        # ⭐⭐⭐ KG DELETE ⭐⭐⭐
        # ====================================================
        if clean.startswith("kg.delete "):
            if len(tokens) == 2:
                entity = tokens[1]
                if self._is_reserved(entity):
                    return result
                return {
                    "intent": "kg.delete",
                    "entity": entity,
                    "args": {
                        "entity": entity,
                        "mode": "developer",
                    },
                }

        if clean.startswith("kg delete "):
            if len(tokens) >= 3:
                entity = tokens[2]
                if self._is_reserved(entity):
                    return result
                return {
                    "intent": "kg.delete",
                    "entity": entity,
                    "args": {
                        "entity": entity,
                        "mode": "developer",
                    },
                }

        # ====================================================
        # ⭐⭐⭐ KG MERGE ⭐⭐⭐
        # ====================================================
        if clean.startswith("kg.merge "):
            if len(tokens) == 3:
                source = tokens[1]
                target = tokens[2]
                if self._is_reserved(source) or self._is_reserved(target):
                    return result
                return {
                    "intent": "kg.merge",
                    "entity": target,
                    "args": {
                        "source": source,
                        "target": target,
                        "mode": "developer",
                    },
                }

        if clean.startswith("kg merge "):
            if len(tokens) == 4:
                source = tokens[2]
                target = tokens[3]
                if self._is_reserved(source) or self._is_reserved(target):
                    return result
                return {
                    "intent": "kg.merge",
                    "entity": target,
                    "args": {
                        "source": source,
                        "target": target,
                        "mode": "developer",
                    },
                }

        # ====================================================
        # ⭐⭐⭐ KG QUERY ⭐⭐⭐
        # ====================================================
        if clean.startswith("kg.query "):
            if len(tokens) >= 2:
                entity = tokens[1]
                if self._is_reserved(entity):
                    return result
                return {
                    "intent": "kg.query",
                    "entity": entity,
                    "args": {
                        "entity": entity,
                        "mode": "developer",
                    },
                }

        if clean.startswith("kg query "):
            if len(tokens) >= 3:
                entity = tokens[2]
                if self._is_reserved(entity):
                    return result
                return {
                    "intent": "kg.query",
                    "entity": entity,
                    "args": {
                        "entity": entity,
                        "mode": "developer",
                    },
                }

        # ====================================================
        # ⭐⭐⭐ KG SET – podpora kg set "entity" "key" "value" ⭐⭐⭐
        # ====================================================

        # kg set "entity" "attribute" "value"
        if clean.startswith("kg set "):
            if len(tokens) >= 5:
                entity = tokens[2].strip('"')
                attribute = tokens[3].strip('"')
                value = " ".join(tokens[4:]).strip('"')
                if self._is_reserved(entity):
                    return result
                return {
                    "intent": "kg.set",
                    "entity": entity,
                    "args": {
                        "entity": entity,
                        "attribute": attribute,
                        "value": value,
                        "mode": "developer",
                    },
                }

        # kg.set "entity" "attribute" "value"
        if clean.startswith("kg.set "):
            if len(tokens) >= 4:
                entity = tokens[1].strip('"')
                attribute = tokens[2].strip('"')
                value = " ".join(tokens[3:]).strip('"')
                if self._is_reserved(entity):
                    return result
                return {
                    "intent": "kg.set",
                    "entity": entity,
                    "args": {
                        "entity": entity,
                        "attribute": attribute,
                        "value": value,
                        "mode": "developer",
                    },
                }

        # ====================================================
        # ⭐⭐⭐ KG GET – podpora kg get "entity" "attribute" ⭐⭐⭐
        # ====================================================

        # kg get "entity" "attribute"
        if clean.startswith("kg get "):
            if len(tokens) >= 4:
                entity = tokens[2].strip('"')
                attribute = tokens[3].strip('"')
                if self._is_reserved(entity):
                    return result
                return {
                    "intent": "kg.get",
                    "entity": entity,
                    "args": {
                        "entity": entity,
                        "attribute": attribute,
                        "key": attribute,
                        "mode": "developer",
                    },
                }

        # kg get entity attribute
        if clean.startswith("kg get "):
            if len(tokens) >= 3:
                entity = tokens[2]
                attribute = tokens[3]
                if self._is_reserved(entity):
                    return result
                return {
                    "intent": "kg.get",
                    "entity": entity,
                    "args": {
                        "entity": entity,
                        "attribute": attribute,
                        "key": attribute,
                        "mode": "developer",
                    },
                }

        # kg.get entity attribute
        if clean.startswith("kg.get "):
            if len(tokens) >= 3:
                entity = tokens[1].strip('"')
                attribute = tokens[2].strip('"')
                if self._is_reserved(entity):
                    return result
                return {
                    "intent": "kg.get",
                    "entity": entity,
                    "args": {
                        "entity": entity,
                        "attribute": attribute,
                        "key": attribute,
                        "mode": "developer",
                    },
                }

        # ====================================================
        # ⭐⭐⭐ KG UNSET – podpora kg unset "entity" "attribute" ⭐⭐⭐
        # ====================================================

        # kg unset "entity" "attribute"
        if clean.startswith("kg unset "):
            if len(tokens) >= 4:
                entity = tokens[2].strip('"')
                attribute = tokens[3].strip('"')
                if self._is_reserved(entity):
                    return result
                return {
                    "intent": "kg.unset",
                    "entity": entity,
                    "args": {
                        "entity": entity,
                        "attribute": attribute,
                        "key": attribute,
                        "mode": "developer",
                    },
                }

        # kg unset entity attribute
        if clean.startswith("kg unset "):
            if len(tokens) >= 3:
                entity = tokens[2]
                attribute = tokens[3]
                if self._is_reserved(entity):
                    return result
                return {
                    "intent": "kg.unset",
                    "entity": entity,
                    "args": {
                        "entity": entity,
                        "attribute": attribute,
                        "key": attribute,
                        "mode": "developer",
                    },
                }

        # kg.unset entity attribute
        if clean.startswith("kg.unset "):
            if len(tokens) >= 3:
                entity = tokens[1].strip('"')
                attribute = tokens[2].strip('"')
                if self._is_reserved(entity):
                    return result
                return {
                    "intent": "kg.unset",
                    "entity": entity,
                    "args": {
                        "entity": entity,
                        "attribute": attribute,
                        "key": attribute,
                        "mode": "developer",
                    },
                }

        # ====================================================
        # ⭐⭐⭐ KG SEARCH – podpora kg search "entity" ⭐⭐⭐
        # ====================================================

        # kg search "entity"
        if clean.startswith("kg search "):
            if len(tokens) >= 3:
                entity = tokens[2].strip('"')
                if self._is_reserved(entity):
                    return result
                return {
                    "intent": "kg.search",
                    "entity": entity,
                    "args": {
                        "entity": entity,
                        "query": entity,
                        "mode": "developer",
                    },
                }

        # kg search entity
        if clean.startswith("kg search "):
            if len(tokens) >= 3:
                entity = tokens[2]
                if self._is_reserved(entity):
                    return result
                return {
                    "intent": "kg.search",
                    "entity": entity,
                    "args": {
                        "entity": entity,
                        "query": entity,
                        "mode": "developer",
                    },
                }

        # kg.search entity
        if clean.startswith("kg.search "):
            if len(tokens) >= 2:
                entity = tokens[1].strip('"')
                if self._is_reserved(entity):
                    return result
                return {
                    "intent": "kg.search",
                    "entity": entity,
                    "args": {
                        "entity": entity,
                        "query": entity,
                        "mode": "developer",
                    },
                }

        # ====================================================
        # ⭐⭐⭐ KG RENAME – podpora kg rename "old" "new" ⭐⭐⭐
        # ====================================================

        # kg rename "old" "new"
        if clean.startswith("kg rename "):
            if len(tokens) >= 4:
                old_name = tokens[2].strip('"')
                new_name = tokens[3].strip('"')
                if self._is_reserved(old_name):
                    return result
                return {
                    "intent": "kg.rename",
                    "entity": old_name,
                    "args": {
                        "old": old_name,
                        "new": new_name,
                        "mode": "developer",
                    },
                }

        # kg rename old new
        if clean.startswith("kg rename "):
            if len(tokens) >= 3:
                old_name = tokens[2]
                new_name = tokens[3]
                if self._is_reserved(old_name):
                    return result
                return {
                    "intent": "kg.rename",
                    "entity": old_name,
                    "args": {
                        "old": old_name,
                        "new": new_name,
                        "mode": "developer",
                    },
                }

        # kg.rename old new
        if clean.startswith("kg.rename "):
            if len(tokens) >= 3:
                old_name = tokens[1].strip('"')
                new_name = tokens[2].strip('"')
                if self._is_reserved(old_name):
                    return result
                return {
                    "intent": "kg.rename",
                    "entity": old_name,
                    "args": {
                        "old": old_name,
                        "new": new_name,
                        "mode": "developer",
                    },
                }

        # ====================================================
        # ⭐⭐⭐ KG EXISTS – podpora kg exists "entity" ⭐⭐⭐
        # ====================================================

        # kg exists "entity"
        if clean.startswith("kg exists "):
            if len(tokens) >= 3:
                entity = tokens[2].strip('"')
                if self._is_reserved(entity):
                    return result
                return {
                    "intent": "kg.exists",
                    "entity": entity,
                    "args": {
                        "entity": entity,
                        "mode": "developer",
                    },
                }

        # kg exists entity
        if clean.startswith("kg exists "):
            if len(tokens) >= 3:
                entity = tokens[2]
                if self._is_reserved(entity):
                    return result
                return {
                    "intent": "kg.exists",
                    "entity": entity,
                    "args": {
                        "entity": entity,
                        "mode": "developer",
                    },
                }

        # kg.exists entity
        if clean.startswith("kg.exists "):
            if len(tokens) >= 2:
                entity = tokens[1].strip('"')
                if self._is_reserved(entity):
                    return result
                return {
                    "intent": "kg.exists",
                    "entity": entity,
                    "args": {
                        "entity": entity,
                        "mode": "developer",
                    },
                }

        # ====================================================
        # ⭐⭐⭐ KG LIST – podpora kg list / kg.list / kg list entities ⭐⭐⭐
        # ====================================================

        # kg list
        if clean == "kg list":
            return {
                "intent": "kg.list",
                "entity": None,
                "args": {
                    "mode": "developer",
                },
            }

        # kg.list
        if clean.startswith("kg.list"):
            return {
                "intent": "kg.list",
                "entity": None,
                "args": {
                    "mode": "developer",
                },
            }

        # kg list entities
        if clean.startswith("kg list entities"):
            return {
                "intent": "kg.list",
                "entity": None,
                "args": {
                    "mode": "developer",
                },
            }

        # ====================================================
        # ⭐⭐⭐ KG STATS – podpora kg stats / kg.stats ⭐⭐⭐
        # ====================================================

        # kg stats
        if clean == "kg stats":
            return {
                "intent": "kg.stats",
                "entity": None,
                "args": {
                    "mode": "developer",
                },
            }

        # kg.stats
        if clean.startswith("kg.stats"):
            return {
                "intent": "kg.stats",
                "entity": None,
                "args": {
                    "mode": "developer",
                },
            }

        # ====================================================
        # ⭐⭐⭐ NATURAL KG RELATE ⭐⭐⭐
        # ====================================================
        # Format: <source> <relation> <target>
        # Spúšťa sa len ak to NIE JE príkaz začínajúci na "kg" alebo "reason"
        if len(tokens) == 3 and not raw_lower.startswith("kg ") and not raw_lower.startswith("kg.") \
           and not raw_lower.startswith("reason ") and not raw_lower.startswith("reason."):
            src = tokens[0]
            rel = tokens[1]
            tgt = tokens[2]

            # Skip reserved words
            if self._is_reserved(src) or self._is_reserved(tgt):
                return result

            return {
                "intent": "kg.relate",
                "entity": src,
                "args": {
                    "source": src,
                    "relation": rel,
                    "target": tgt,
                    "mode": "developer",
                },
            }

        # ====================================================
        # ⭐⭐⭐ FALLBACK ⭐⭐⭐
        # ====================================================
        return result

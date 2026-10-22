"""
SIRIUS REASONING BRIDGE - DETERMINISTIC SYNTHESIZER V1.1 (BIDIRECTIONAL)
Plne offline deterministická inferencia nad autosave_kg.json.
Podpora: Outbound fakty (source), Inbound kontext (target) a tranzitívne prepojenia.
"""

import json
from pathlib import Path
from typing import List, Dict, Any, Set, Optional


class DeterministicSynthesizer:
    TEMPLATES = {
        "je": "{source} je {target}.",
        "sú": "{source} sú {target}.",
        "má": "{source} má {target}.",
        "majú": "{source} majú {target}.",
        "obsahuje": "{source} obsahuje {target}.",
        "obsahujú": "{source} obsahujú {target}.",
        "pozostáva": "{source} pozostáva z {target}.",
        "tvorí": "{source} tvorí {target}.",
        "vyžaruje": "{source} vyžaruje {target}.",
        "predstavuje": "{source} predstavuje {target}.",
    }

    def __init__(self, kg_path: Optional[str] = None):
        self.kg_path = self.resolve_kg_path(kg_path)
        self.relations: List[Dict[str, Any]] = []
        self.kg_version: int = 0
        self.load_graph()

    @staticmethod
    def resolve_kg_path(explicit_path: Optional[str] = None) -> Path:
        """Nájde hlavný autosave_kg.json bez ohľadu na pracovný adresár."""
        if explicit_path:
            p = Path(explicit_path).resolve()
            if p.exists():
                return p

        cwd_p = Path("autosave_kg.json").resolve()
        parent_p = (Path.cwd().parent / "autosave_kg.json").resolve()
        script_parent_p = (Path(__file__).resolve().parent.parent / "autosave_kg.json").resolve()
        script_dir_p = (Path(__file__).resolve().parent / "autosave_kg.json").resolve()

        candidates = [cwd_p, parent_p, script_parent_p, script_dir_p]
        for candidate in candidates:
            if candidate.exists():
                try:
                    with open(candidate, "r", encoding="utf-8") as f:
                        data = json.load(f)
                    if len(data.get("relations", [])) > 50:
                        return candidate
                except Exception:
                    continue

        for candidate in candidates:
            if candidate.exists():
                return candidate

        raise FileNotFoundError("Súbor autosave_kg.json nebol nájdený.")

    def load_graph(self) -> None:
        """Načíta zmrazený graf do pamäte RAM."""
        with open(self.kg_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.relations = data.get("relations", [])
        self.kg_version = data.get("kg_version", 0)

    def format_fact(self, source: str, relation: str, target: str) -> str:
        """Sformátuje trojicu do deterministickej vety podľa šablóny."""
        rel_clean = relation.strip().lower()
        src_clean = source.strip().capitalize()
        tgt_clean = target.strip()
        template = self.TEMPLATES.get(rel_clean, "{source} [{relation}] {target}.")
        return template.format(source=src_clean, relation=rel_clean, target=tgt_clean)

    def query_concept(self, entity: str) -> str:
        """Vytiahne podsieť k entite obojsmerne a zostaví deterministický kognitívny list."""
        q = entity.strip().lower()

        # 1. Priame fakty (Pojem ako Subjekt / Source)
        direct_outbound = [
            r for r in self.relations
            if r.get("source", "").strip().lower() == q
        ]
        direct_outbound.sort(key=lambda x: (x.get("relation", "").strip().lower(), x.get("target", "").strip().lower()))

        # 2. Kontextové fakty (Pojem ako Objekt / Target alebo podreťazec)
        inbound = [
            r for r in self.relations
            if q in r.get("target", "").strip().lower()
            and r.get("source", "").strip().lower() != q
        ]
        inbound.sort(key=lambda x: (x.get("source", "").strip().lower(), x.get("relation", "").strip().lower()))

        # Ak sa nenašiel ani ako presný source, skontrolujeme či nie je ako podreťazec v source
        if not direct_outbound and not inbound:
            fuzzy_source = [
                r for r in self.relations
                if q in r.get("source", "").strip().lower()
            ]
            if fuzzy_source:
                direct_outbound = fuzzy_source
                direct_outbound.sort(key=lambda x: (x.get("source", "").strip().lower(), x.get("relation", "").strip().lower()))

        if not direct_outbound and not inbound:
            return f"[REASONING BRIDGE] Pojem '{entity}' sa v zmrazenom grafe nenachádza."

        # 3. Tranzitívne súvislosti (1. rád z cieľov outbound faktov)
        target_words: Set[str] = set()
        for r in direct_outbound:
            for word in r.get("target", "").strip().lower().split():
                if len(word) > 3:
                    target_words.add(word)

        inferred = [
            r for r in self.relations
            if r.get("source", "").strip().lower() in target_words
            and r.get("source", "").strip().lower() != q
        ]
        inferred.sort(key=lambda x: (x.get("source", "").strip().lower(), x.get("relation", "").strip().lower()))

        # 4. Deterministická syntéza protokolu
        lines = [
            "=" * 60,
            f"SIRIUS DETERMINISTIC DEDUCTION: {entity.upper()}",
            f"Zdroj: {self.kg_path.name} (v{self.kg_version}) | Režim: Ground Truth Offline",
            "=" * 60,
        ]

        if direct_outbound:
            lines.append("\n1. PRIAME DEFINÍCIE A ZÁKLADNÉ VLASTNOSTI:")
            for f in direct_outbound:
                lines.append(f"   • {self.format_fact(f['source'], f['relation'], f['target'])}")

        if inbound:
            lines.append("\n2. KONTEXTOVÉ VÄZBY V GRAFE (VÝSKYT AKO CIEĽ/OBJEKT):")
            for f in inbound:
                lines.append(f"   • {self.format_fact(f['source'], f['relation'], f['target'])}")

        if inferred:
            lines.append("\n3. ODVODENÉ TRANZITÍVNE SÚVISLOSTI (1. RÁD):")
            for f in inferred:
                lines.append(f"   • {self.format_fact(f['source'], f['relation'], f['target'])}")

        lines.append("=" * 60)
        return "\n".join(lines)


if __name__ == "__main__":
    import sys
    test_concept = sys.argv[1] if len(sys.argv) > 1 else "anihilácia"
    bridge = DeterministicSynthesizer()
    print(f"\n[INIT] Úspešne načítaných {len(bridge.relations)} relácií (v{bridge.kg_version}) zo súboru: {bridge.kg_path}")
    print(bridge.query_concept(test_concept))
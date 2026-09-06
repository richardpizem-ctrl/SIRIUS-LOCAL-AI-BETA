class LanguageOutput:
    def build(self, normalized: str, category: str, parsed: dict) -> dict:
        """
        Výstup jazykového modulu pre autonómiu.
        Kombinuje:
        - normalizovaný text
        - kategóriu vety
        - rozparsované časti (akcia, objekt, stav, kontext)
        """

        return {
            "normalized_text": normalized,
            "category": category,
            "action": parsed.get("action"),
            "object": parsed.get("object"),
            "state": parsed.get("state"),
            "context": parsed.get("context")
        }

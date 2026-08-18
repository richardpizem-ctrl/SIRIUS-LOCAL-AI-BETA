# AUTONOMY GUARD — Rules
# Pravidlá zdravého behu autonómie

class GuardRules:

    def validate(self, problems):
        """
        Ak existuje problém, vracia STOP signál.
        """
        if not problems:
            return {"status": "OK"}

        return {
            "status": "STOP",
            "problems": problems
        }

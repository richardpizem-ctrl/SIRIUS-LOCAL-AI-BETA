# SIRIUS COLNIK-6.x — Navigation Module (PRE-FINAL)
# This module handles routing, step selection, and safe traversal inside COLNIK.

class Navigation:
    def __init__(self):
        self.current_step = None

    def set_step(self, step_name: str):
        """Set the current navigation step."""
        self.current_step = step_name
        return f"[NAVIGATION] Step set to: {step_name}"

    def next(self):
        """Placeholder for next-step logic (will be completed in final version)."""
        return "[NAVIGATION] Next step logic not implemented yet."

    def previous(self):
        """Placeholder for previous-step logic."""
        return "[NAVIGATION] Previous step logic not implemented yet."

    def get_allowed_next_steps(self, current_step: str):
        """Return allowed next steps based on NAVIGATION_RULES."""
        from navigation.navigation_rules import NAVIGATION_RULES
        return NAVIGATION_RULES.get(current_step, [])

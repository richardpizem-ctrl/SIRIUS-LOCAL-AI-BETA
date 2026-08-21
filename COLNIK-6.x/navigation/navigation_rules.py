# Navigation Rules (PRE-FINAL)
# These rules will define allowed transitions between COLNIK workflow steps.

NAVIGATION_RULES = {
    "INIT": ["ANALYZE"],
    "ANALYZE": ["VALIDATE", "REJECT"],
    "VALIDATE": ["DECIDE"],
    "DECIDE": ["WORKFLOW"],
    "WORKFLOW": ["END"]
}


"""
SIRIUS LOCAL AI – Reasoning Engine 4.5 Package (PRO)

Initializes the deterministic reasoning subsystem for Runtime 4.5.

Provides:
- ReasoningCore45
- ReasoningContextBuilder45
- ReasoningChainExecutor45
- ReasoningRuleEngine45
- ReasoningExplainer45
- ReasoningSafetyGuard45

Security Notes (Runtime 4.5 PRO):
- Only static imports allowed.
- No dynamic loading, no eval, no reflection.
- __all__ must contain only verified public symbols.
- Fully deterministic, offline, isolated.
- Compatible with Security Family 4.5 and Self‑Repair 4.5.
"""

# -------------------------------------------------------------------------
# PACKAGE METADATA
# -------------------------------------------------------------------------

REASONING_VERSION = "4.5"
SECURITY_FAMILY_COMPAT = "4.5"

# -------------------------------------------------------------------------
# STATIC IMPORTS (PRO)
# -------------------------------------------------------------------------

from .re_core_4_5 import ReasoningCore45
from .re_context_builder_4_5 import ReasoningContextBuilder45
from .re_chain_executor_4_5 import ReasoningChainExecutor45
from .re_rule_engine_4_5 import ReasoningRuleEngine45
from .re_explainer_4_5 import ReasoningExplainer45
from .re_safety_guard_4_5 import ReasoningSafetyGuard45

# -------------------------------------------------------------------------
# SAFE EXPORT LIST
# -------------------------------------------------------------------------

__all__ = [
    "ReasoningCore45",
    "ReasoningContextBuilder45",
    "ReasoningChainExecutor45",
    "ReasoningRuleEngine45",
    "ReasoningExplainer45",
    "ReasoningSafetyGuard45",
    "REASONING_VERSION",
    "SECURITY_FAMILY_COMPAT",
]

"""
SIRIUS LOCAL AI – Reasoning Engine 4.4 Package (PRO)

Initializes the deterministic reasoning subsystem for Runtime 4.4.

Provides:
- ReasoningCore44
- ReasoningContextBuilder44
- ReasoningChainExecutor44
- ReasoningRuleEngine44
- ReasoningExplainer44
- ReasoningSafetyGuard44

Security Notes (Runtime 4.4 PRO):
- Only static imports allowed.
- No dynamic loading, no eval, no reflection.
- __all__ must contain only verified public symbols.
- Fully deterministic, offline, isolated.
- Compatible with Security Family 4.4 and Self‑Repair 4.4.
"""

# -------------------------------------------------------------------------
# PACKAGE METADATA
# -------------------------------------------------------------------------

REASONING_VERSION = "4.4"
SECURITY_FAMILY_COMPAT = "4.4"

# -------------------------------------------------------------------------
# STATIC IMPORTS (PRO)
# -------------------------------------------------------------------------

from .re_core_4_4 import ReasoningCore44
from .re_context_builder_4_4 import ReasoningContextBuilder44
from .re_chain_executor_4_4 import ReasoningChainExecutor44
from .re_rule_engine_4_4 import ReasoningRuleEngine44
from .re_explainer_4_4 import ReasoningExplainer44
from .re_safety_guard_4_4 import ReasoningSafetyGuard44

# -------------------------------------------------------------------------
# SAFE EXPORT LIST
# -------------------------------------------------------------------------

__all__ = [
    "ReasoningCore44",
    "ReasoningContextBuilder44",
    "ReasoningChainExecutor44",
    "ReasoningRuleEngine44",
    "ReasoningExplainer44",
    "ReasoningSafetyGuard44",
    "REASONING_VERSION",
    "SECURITY_FAMILY_COMPAT",
]

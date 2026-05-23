"""
SIRIUS LOCAL AI – Knowledge Packs 4.5.0 (PRO)

This package contains the full Knowledge Packs subsystem for Runtime 4.5.
It provides:

- KP Core 4.5 (base logic)
- KP Loader 4.5 (deterministic loading)
- KP Registry 4.5 (pack registration)
- KP Validator 4.5 (schema + integrity checks)
- KP Query Engine 4.5 (fast offline lookup)
- KP Metadata 4.5 (versioning + descriptors)
- Domain Packs 4.5 (math, language, science, history, geography, general)

All modules inside this package are:
- deterministic
- offline
- fully isolated
- static‑import only
- free of dynamic loading, eval, reflection, or runtime mutation

Security Notes (Knowledge Packs 4.5.0):
- Only static imports allowed.
- No dynamic loading, no eval, no reflection.
- Knowledge Packs must be pure JSON or pure Python dicts.
- __all__ must contain only verified public namespaces.
- This file must not contain executable logic.
"""

# -------------------------------------------------------------------------
# PACKAGE METADATA (STATIC, IMMUTABLE)
# -------------------------------------------------------------------------

KNOWLEDGE_PACKS_VERSION_4_5 = "4.5.0"
KNOWLEDGE_PACKS_RUNTIME = "4.5"
KNOWLEDGE_PACKS_OFFLINE = True

# -------------------------------------------------------------------------
# SAFE EXPORT LIST (STRICT WHITELIST)
# -------------------------------------------------------------------------

__all__ = [
    "kp_core_4_5",
    "kp_loader_4_5",
    "kp_registry_4_5",
    "kp_validator_4_5",
    "kp_query_engine_4_5",
    "kp_metadata_4_5",
    "kp_math_pack_4_5",
    "kp_language_pack_4_5",
    "kp_science_pack_4_5",
    "kp_history_pack_4_5",
    "kp_geography_pack_4_5",
    "kp_general_pack_4_5",
    "KNOWLEDGE_PACKS_VERSION_4_5",
    "KNOWLEDGE_PACKS_RUNTIME",
    "KNOWLEDGE_PACKS_OFFLINE",
]

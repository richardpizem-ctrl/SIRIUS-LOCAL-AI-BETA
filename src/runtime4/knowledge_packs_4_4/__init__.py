knowledge_packs_4_4/__init__.py
"""
SIRIUS LOCAL AI – Knowledge Packs 4.4.0

This package contains the full Knowledge Packs subsystem for Runtime 4.4.
It provides:

- KP Core 4.4 (base logic)
- KP Loader 4.4 (deterministic loading)
- KP Registry 4.4 (pack registration)
- KP Validator 4.4 (schema + integrity checks)
- KP Query Engine 4.4 (fast offline lookup)
- KP Metadata 4.4 (versioning + descriptors)
- Domain Packs 4.4 (math, language, science, history, geography, general)

All modules inside this package are deterministic, offline, and fully isolated.

Security Notes (Knowledge Packs 4.4.0):
- Only static imports allowed.
- No dynamic loading, no eval, no reflection.
- Knowledge Packs must be pure JSON or pure Python dicts.
- __all__ must contain only verified public namespaces.
- This file must not contain executable logic.
"""

# -------------------------------------------------------------------------
# PACKAGE METADATA
# -------------------------------------------------------------------------

KNOWLEDGE_PACKS_VERSION_4_4 = "4.4.0"
KNOWLEDGE_PACKS_RUNTIME = "4.4"
KNOWLEDGE_PACKS_OFFLINE = True

# -------------------------------------------------------------------------
# SAFE EXPORT LIST
# -------------------------------------------------------------------------

__all__ = [
    "kp_core_4_4",
    "kp_loader_4_4",
    "kp_registry_4_4",
    "kp_validator_4_4",
    "kp_query_engine_4_4",
    "kp_metadata_4_4",
    "kp_math_pack_4_4",
    "kp_language_pack_4_4",
    "kp_science_pack_4_4",
    "kp_history_pack_4_4",
    "kp_geography_pack_4_4",
    "kp_general_pack_4_4",
    "KNOWLEDGE_PACKS_VERSION_4_4",
    "KNOWLEDGE_PACKS_RUNTIME",
    "KNOWLEDGE_PACKS_OFFLINE",
]

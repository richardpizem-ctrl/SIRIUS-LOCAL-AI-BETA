"""
SIRIUS LOCAL AI – Household Automation 4.5 Package

Initializes household automation subsystems:
- Core
- Device Registry
- State Manager
- Routine Engine
- Room Mapper
- Command Parser
- Safety Guard
- Event Bus
- Context Memory

All modules in this package are:
- deterministic
- offline‑safe
- Security Family 4.5 compatible
- Self‑Repair 4.5 ready
"""

# ---------------------------------------------------------
# SAFE STATIC IMPORTS
# ---------------------------------------------------------

from .ha_core_4_5 import HouseholdCore45
from .ha_device_registry_4_5 import HouseholdDeviceRegistry45
from .ha_state_manager_4_5 import HouseholdStateManager45
from .ha_routine_engine_4_5 import HouseholdRoutineEngine45
from .ha_room_mapper_4_5 import HouseholdRoomMapper45
from .ha_command_parser_4_5 import HouseholdCommandParser45
from .ha_safety_guard_4_5 import HouseholdSafetyGuard45
from .ha_event_bus_4_5 import HouseholdEventBus45
from .ha_context_memory_4_5 import HouseholdContextMemory45

# ---------------------------------------------------------
# PACKAGE METADATA
# ---------------------------------------------------------

HOUSEHOLD_VERSION_4_5 = "4.5.0"
HOUSEHOLD_SECURITY_FAMILY = "4.5"
HOUSEHOLD_SELF_REPAIR_READY = True
HOUSEHOLD_OFFLINE_DETERMINISTIC = True

# ---------------------------------------------------------
# SAFE EXPORT LIST
# ---------------------------------------------------------

__all__ = [
    "HouseholdCore45",
    "HouseholdDeviceRegistry45",
    "HouseholdStateManager45",
    "HouseholdRoutineEngine45",
    "HouseholdRoomMapper45",
    "HouseholdCommandParser45",
    "HouseholdSafetyGuard45",
    "HouseholdEventBus45",
    "HouseholdContextMemory45",
    "HOUSEHOLD_VERSION_4_5",
    "HOUSEHOLD_SECURITY_FAMILY",
    "HOUSEHOLD_SELF_REPAIR_READY",
    "HOUSEHOLD_OFFLINE_DETERMINISTIC",
]

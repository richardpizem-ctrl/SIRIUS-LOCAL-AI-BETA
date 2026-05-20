"""
SIRIUS LOCAL AI – Household Automation 4.4 Package

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
- Security Family 4.4 compatible
- Self‑Repair 4.4 ready
"""

# ---------------------------------------------------------
# SAFE STATIC IMPORTS
# ---------------------------------------------------------

from .ha_core_4_4 import HouseholdCore44
from .ha_device_registry_4_4 import HouseholdDeviceRegistry44
from .ha_state_manager_4_4 import HouseholdStateManager44
from .ha_routine_engine_4_4 import HouseholdRoutineEngine44
from .ha_room_mapper_4_4 import HouseholdRoomMapper44
from .ha_command_parser_4_4 import HouseholdCommandParser44
from .ha_safety_guard_4_4 import HouseholdSafetyGuard44
from .ha_event_bus_4_4 import HouseholdEventBus44
from .ha_context_memory_4_4 import HouseholdContextMemory44

# ---------------------------------------------------------
# PACKAGE METADATA
# ---------------------------------------------------------

HOUSEHOLD_VERSION_4_4 = "4.4.0"
HOUSEHOLD_SECURITY_FAMILY = "4.4"
HOUSEHOLD_SELF_REPAIR_READY = True
HOUSEHOLD_OFFLINE_DETERMINISTIC = True

# ---------------------------------------------------------
# SAFE EXPORT LIST
# ---------------------------------------------------------

__all__ = [
    "HouseholdCore44",
    "HouseholdDeviceRegistry44",
    "HouseholdStateManager44",
    "HouseholdRoutineEngine44",
    "HouseholdRoomMapper44",
    "HouseholdCommandParser44",
    "HouseholdSafetyGuard44",
    "HouseholdEventBus44",
    "HouseholdContextMemory44",
    "HOUSEHOLD_VERSION_4_4",
    "HOUSEHOLD_SECURITY_FAMILY",
    "HOUSEHOLD_SELF_REPAIR_READY",
    "HOUSEHOLD_OFFLINE_DETERMINISTIC",
]

# household_4_4/home_inventory_manager_4_4.py
"""
SIRIUS LOCAL AI – Home Inventory Manager 4.4.0

Účel:
- sledovanie zásob v domácnosti (potraviny, hygiena, čistiace prostriedky…)
- 100 % offline, deterministické
- žiadne AI heuristiky, žiadne dynamické importy

Položka inventára:
{
    "name": "toaletny_papier",
    "category": "hygiene",
    "quantity": 12,
    "min_quantity": 4
}
"""

from typing import Dict, Any, Optional, List


class HomeInventoryManager44:
    """
    Deterministic inventory manager pre domácnosť.
    """

    def __init__(self, event_bus=None):
        self.initialized = False
        self.degraded_mode = False

        self.event_bus = event_bus

        # name → item
        self.inventory: Dict[str, Dict[str, Any]] = {}

    # ------------------------------------------------------------------
    # INITIALIZATION
    # ------------------------------------------------------------------
    def initialize(self) -> Dict[str, Any]:
        if self.initialized:
            return {"status": "already_initialized"}

        try:
            if self.event_bus:
                self.event_bus.initialize()

            self.initialized = True
            return {"status": "initialized"}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "exception": str(exc)}

    # ------------------------------------------------------------------
    # ADD OR UPDATE ITEM
    # ------------------------------------------------------------------
    def add_item(
        self,
        name: str,
        category: str,
        quantity: int,
        min_quantity: int = 1
    ) -> Dict[str, Any]:

        item = {
            "name": name,
            "category": category,
            "quantity": quantity,
            "min_quantity": min_quantity,
        }

        self.inventory[name] = item

        if self.event_bus:
            self.event_bus.emit("inventory_item_added", {"item": item})

        return {"status": "ok", "item": item}

    # ------------------------------------------------------------------
    # REMOVE ITEM
    # ------------------------------------------------------------------
    def remove_item(self, name: str) -> Dict[str, Any]:
        if name not in self.inventory:
            return {"status": "error", "reason": "item_not_found"}

        removed = self.inventory.pop(name)

        if self.event_bus:
            self.event_bus.emit("inventory_item_removed", {"item": removed})

        return {"status": "ok"}

    # ------------------------------------------------------------------
    # UPDATE QUANTITY
    # ------------------------------------------------------------------
    def update_quantity(self, name: str, quantity: int) -> Dict[str, Any]:
        if name not in self.inventory:
            return {"status": "error", "reason": "item_not_found"}

        old = self.inventory[name]["quantity"]
        self.inventory[name]["quantity"] = quantity

        if self.event_bus:
            self.event_bus.emit("inventory_quantity_updated", {
                "name": name,
                "old": old,
                "new": quantity,
            })

        return {"status": "ok", "item": dict(self.inventory[name])}

    # ------------------------------------------------------------------
    # LIST ITEMS
    # ------------------------------------------------------------------
    def list_items(self) -> Dict[str, Any]:
        return {"status": "ok", "items": list(self.inventory.values())}

    # ------------------------------------------------------------------
    # LIST LOW-STOCK ITEMS
    # ------------------------------------------------------------------
    def list_low_stock(self) -> Dict[str, Any]:
        low = [
            item for item in self.inventory.values()
            if item["quantity"] <= item["min_quantity"]
        ]
        return {"status": "ok", "low_stock": low}

    # ------------------------------------------------------------------
    # GET ITEM
    # ------------------------------------------------------------------
    def get_item(self, name: str) -> Dict[str, Any]:
        if name not in self.inventory:
            return {"status": "error", "reason": "item_not_found"}

        return {"status": "ok", "item": dict(self.inventory[name])}

    # ------------------------------------------------------------------
    # CLEAR INVENTORY
    # ------------------------------------------------------------------
    def clear(self) -> Dict[str, Any]:
        self.inventory = {}
        return {"status": "ok"}

    # ------------------------------------------------------------------
    # STATUS
    # ------------------------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "status": "ok",
            "initialized": self.initialized,
            "degraded_mode": self.degraded_mode,
            "items_count": len(self.inventory),
        }

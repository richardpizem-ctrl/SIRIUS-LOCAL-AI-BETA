"""
SIRIUS LOCAL AI – Home Inventory Manager 4.4.0

Účel:
- deterministické sledovanie zásob v domácnosti
- 100 % offline, žiadne AI heuristiky, žiadne dynamické importy

Security Family 4.4:
- žiadne nebezpečné typy
- deterministické správanie
- Self‑Repair 4.4 ready
"""

from typing import Dict, Any, Optional, List


class HomeInventoryManager44:
    """
    Deterministic inventory manager pre domácnosť.
    """

    def __init__(self, event_bus=None):
        self.initialized = False
        self.degraded_mode = False
        self.safe_mode = False

        self.event_bus = event_bus

        # name → item
        self.inventory: Dict[str, Dict[str, Any]] = {}

    # ---------------------------------------------------------
    # INTERNAL VALIDATION
    # ---------------------------------------------------------
    def _validate_str(self, value: Any) -> bool:
        return isinstance(value, str) and value.strip()

    def _validate_int(self, value: Any) -> bool:
        return isinstance(value, int) and value >= 0

    # ---------------------------------------------------------
    # INITIALIZATION
    # ---------------------------------------------------------
    def initialize(self) -> Dict[str, Any]:
        if self.initialized:
            return {"status": "already_initialized"}

        try:
            if self.event_bus:
                res = self.event_bus.initialize()
                if isinstance(res, dict) and res.get("status") == "error":
                    self.degraded_mode = True
                    return {"status": "error", "code": "event_bus_init_failed"}

            self.initialized = True
            return {"status": "initialized"}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "exception": str(exc)}

    # ---------------------------------------------------------
    # ADD OR UPDATE ITEM
    # ---------------------------------------------------------
    def add_item(
        self,
        name: str,
        category: str,
        quantity: int,
        min_quantity: int = 1
    ) -> Dict[str, Any]:

        if self.safe_mode:
            return {"status": "safe_mode", "message": "Inventory manager disabled in safe-mode."}

        if not self._validate_str(name):
            return {"status": "error", "code": "invalid_name"}

        if not self._validate_str(category):
            return {"status": "error", "code": "invalid_category"}

        if not self._validate_int(quantity):
            return {"status": "error", "code": "invalid_quantity"}

        if not self._validate_int(min_quantity):
            return {"status": "error", "code": "invalid_min_quantity"}

        try:
            item = {
                "name": name,
                "category": category,
                "quantity": quantity,
                "min_quantity": min_quantity,
            }

            self.inventory[name] = item

            if self.event_bus:
                try:
                    self.event_bus.emit("inventory_item_added", {"item": item})
                except Exception:
                    self.degraded_mode = True

            return {"status": "ok", "item": dict(item)}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "code": "add_item_failed", "exception": str(exc)}

    # ---------------------------------------------------------
    # REMOVE ITEM
    # ---------------------------------------------------------
    def remove_item(self, name: str) -> Dict[str, Any]:
        if not self._validate_str(name):
            return {"status": "error", "code": "invalid_name"}

        if name not in self.inventory:
            return {"status": "error", "code": "item_not_found"}

        try:
            removed = self.inventory.pop(name)

            if self.event_bus:
                try:
                    self.event_bus.emit("inventory_item_removed", {"item": removed})
                except Exception:
                    self.degraded_mode = True

            return {"status": "ok"}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "code": "remove_item_failed", "exception": str(exc)}

    # ---------------------------------------------------------
    # UPDATE QUANTITY
    # ---------------------------------------------------------
    def update_quantity(self, name: str, quantity: int) -> Dict[str, Any]:
        if not self._validate_str(name):
            return {"status": "error", "code": "invalid_name"}

        if not self._validate_int(quantity):
            return {"status": "error", "code": "invalid_quantity"}

        if name not in self.inventory:
            return {"status": "error", "code": "item_not_found"}

        try:
            old = self.inventory[name]["quantity"]
            self.inventory[name]["quantity"] = quantity

            if self.event_bus:
                try:
                    self.event_bus.emit("inventory_quantity_updated", {
                        "name": name,
                        "old": old,
                        "new": quantity,
                    })
                except Exception:
                    self.degraded_mode = True

            return {"status": "ok", "item": dict(self.inventory[name])}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "code": "update_quantity_failed", "exception": str(exc)}

    # ---------------------------------------------------------
    # LIST ITEMS
    # ---------------------------------------------------------
    def list_items(self) -> Dict[str, Any]:
        try:
            return {"status": "ok", "items": list(self.inventory.values())}
        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "code": "list_failed", "exception": str(exc)}

    # ---------------------------------------------------------
    # LIST LOW-STOCK ITEMS
    # ---------------------------------------------------------
    def list_low_stock(self) -> Dict[str, Any]:
        try:
            low = [
                item for item in self.inventory.values()
                if item["quantity"] <= item["min_quantity"]
            ]
            return {"status": "ok", "low_stock": low}
        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "code": "low_stock_failed", "exception": str(exc)}

    # ---------------------------------------------------------
    # GET ITEM
    # ---------------------------------------------------------
    def get_item(self, name: str) -> Dict[str, Any]:
        if not self._validate_str(name):
            return {"status": "error", "code": "invalid_name"}

        if name not in self.inventory:
            return {"status": "error", "code": "item_not_found"}

        try:
            return {"status": "ok", "item": dict(self.inventory[name])}
        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "code": "get_item_failed", "exception": str(exc)}

    # ---------------------------------------------------------
    # CLEAR INVENTORY
    # ---------------------------------------------------------
    def clear(self) -> Dict[str, Any]:
        if self.safe_mode:
            return {"status": "safe_mode", "message": "Inventory manager disabled in safe-mode."}

        try:
            self.inventory = {}
            return {"status": "ok"}
        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "code": "clear_failed", "exception": str(exc)}

    # ---------------------------------------------------------
    # STATUS
    # ---------------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "status": "ok",
            "initialized": self.initialized,
            "safe_mode": self.safe_mode,
            "degraded_mode": self.degraded_mode,
            "items_count": len(self.inventory),
        }

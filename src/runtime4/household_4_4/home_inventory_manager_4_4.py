"""
SIRIUS LOCAL AI – Home Inventory Manager 4.5.0

Purpose:
- deterministic household inventory tracking
- 100% offline, no AI heuristics, no dynamic imports

Security Family 4.5:
- no dangerous types
- deterministic behavior
- Self‑Repair 4.5 ready
"""

from typing import Dict, Any, Optional, List


class HomeInventoryManager45:
    """
    Deterministic household inventory manager 4.5.
    """

    def __init__(self, event_bus=None):
        self.initialized = False
        self.degraded_mode = False
        self.safe_mode = False

        self.event_bus = event_bus

        # name → item structure
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
            return {"status": "already_initialized", "version": "4.5"}

        try:
            if self.event_bus:
                res = self.event_bus.initialize()
                if isinstance(res, dict) and res.get("status") == "error":
                    self.degraded_mode = True
                    return {
                        "status": "error",
                        "code": "event_bus_init_failed",
                        "version": "4.5",
                    }

            self.initialized = True
            return {"status": "initialized", "version": "4.5"}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "exception": str(exc), "version": "4.5"}

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
            return {
                "status": "safe_mode",
                "message": "Inventory manager disabled in safe-mode.",
                "version": "4.5",
            }

        if not self._validate_str(name):
            return {"status": "error", "code": "invalid_name", "version": "4.5"}

        if not self._validate_str(category):
            return {"status": "error", "code": "invalid_category", "version": "4.5"}

        if not self._validate_int(quantity):
            return {"status": "error", "code": "invalid_quantity", "version": "4.5"}

        if not self._validate_int(min_quantity):
            return {"status": "error", "code": "invalid_min_quantity", "version": "4.5"}

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

            return {"status": "ok", "item": dict(item), "version": "4.5"}

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "add_item_failed",
                "exception": str(exc),
                "version": "4.5",
            }

    # ---------------------------------------------------------
    # REMOVE ITEM
    # ---------------------------------------------------------
    def remove_item(self, name: str) -> Dict[str, Any]:
        if not self._validate_str(name):
            return {"status": "error", "code": "invalid_name", "version": "4.5"}

        if name not in self.inventory:
            return {"status": "error", "code": "item_not_found", "version": "4.5"}

        try:
            removed = self.inventory.pop(name)

            if self.event_bus:
                try:
                    self.event_bus.emit("inventory_item_removed", {"item": removed})
                except Exception:
                    self.degraded_mode = True

            return {"status": "ok", "version": "4.5"}

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "remove_item_failed",
                "exception": str(exc),
                "version": "4.5",
            }

    # ---------------------------------------------------------
    # UPDATE QUANTITY
    # ---------------------------------------------------------
    def update_quantity(self, name: str, quantity: int) -> Dict[str, Any]:
        if not self._validate_str(name):
            return {"status": "error", "code": "invalid_name", "version": "4.5"}

        if not self._validate_int(quantity):
            return {"status": "error", "code": "invalid_quantity", "version": "4.5"}

        if name not in self.inventory:
            return {"status": "error", "code": "item_not_found", "version": "4.5"}

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

            return {"status": "ok", "item": dict(self.inventory[name]), "version": "4.5"}

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "update_quantity_failed",
                "exception": str(exc),
                "version": "4.5",
            }

    # ---------------------------------------------------------
    # LIST ITEMS
    # ---------------------------------------------------------
    def list_items(self) -> Dict[str, Any]:
        try:
            return {"status": "ok", "items": list(self.inventory.values()), "version": "4.5"}
        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "list_failed",
                "exception": str(exc),
                "version": "4.5",
            }

    # ---------------------------------------------------------
    # LIST LOW-STOCK ITEMS
    # ---------------------------------------------------------
    def list_low_stock(self) -> Dict[str, Any]:
        try:
            low = [
                item for item in self.inventory.values()
                if item["quantity"] <= item["min_quantity"]
            ]
            return {"status": "ok", "low_stock": low, "version": "4.5"}
        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "low_stock_failed",
                "exception": str(exc),
                "version": "4.5",
            }

    # ---------------------------------------------------------
    # GET ITEM
    # ---------------------------------------------------------
    def get_item(self, name: str) -> Dict[str, Any]:
        if not self._validate_str(name):
            return {"status": "error", "code": "invalid_name", "version": "4.5"}

        if name not in self.inventory:
            return {"status": "error", "code": "item_not_found", "version": "4.5"}

        try:
            return {"status": "ok", "item": dict(self.inventory[name]), "version": "4.5"}
        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "get_item_failed",
                "exception": str(exc),
                "version": "4.5",
            }

    # ---------------------------------------------------------
    # CLEAR INVENTORY
    # ---------------------------------------------------------
    def clear(self) -> Dict[str, Any]:
        if self.safe_mode:
            return {
                "status": "safe_mode",
                "message": "Inventory manager disabled in safe-mode.",
                "version": "4.5",
            }

        try:
            self.inventory = {}
            return {"status": "ok", "version": "4.5"}
        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "clear_failed",
                "exception": str(exc),
                "version": "4.5",
            }

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
            "version": "4.5",
        }

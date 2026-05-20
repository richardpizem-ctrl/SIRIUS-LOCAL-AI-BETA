# reasoning_4_4/reasoning_symbolic_solver_4_4.py
"""
SIRIUS LOCAL AI – Reasoning Symbolic Solver 4.4.0

Deterministic, offline‑safe symbolic solver for Reasoning Engine 4.4.

Features:
- Simple symbolic expressions (variables, numbers, +, -, *, /, ^, parentheses)
- Deterministic parsing (no eval, no dynamic imports, no reflection)
- Expression tree representation
- Substitution of variables
- Numeric evaluation with environment
- Basic simplifications (constant folding, neutral elements)

Security Notes:
- No eval, no exec, no dynamic imports.
- Only operates on in‑memory strings, numbers, and dicts.
- Fully offline, deterministic, isolated.
"""

from __future__ import annotations
from typing import Any, Dict, Union, List, Optional


Number = Union[int, float]


class SymbolicNode44:
    """
    Base class for all symbolic expression nodes.
    """

    def evaluate(self, env: Dict[str, Number]) -> Number:
        raise NotImplementedError

    def substitute(self, mapping: Dict[str, "SymbolicNode44"]) -> "SymbolicNode44":
        raise NotImplementedError

    def simplify(self) -> "SymbolicNode44":
        return self


class ConstNode44(SymbolicNode44):
    def __init__(self, value: Number):
        self.value = value

    def evaluate(self, env: Dict[str, Number]) -> Number:
        return self.value

    def substitute(self, mapping: Dict[str, "SymbolicNode44"]) -> "SymbolicNode44":
        return self

    def simplify(self) -> "SymbolicNode44":
        return self

    def __repr__(self) -> str:
        return f"Const({self.value})"


class VarNode44(SymbolicNode44):
    def __init__(self, name: str):
        self.name = name

    def evaluate(self, env: Dict[str, Number]) -> Number:
        if self.name not in env:
            raise KeyError(f"Variable '{self.name}' not found in environment")
        return env[self.name]

    def substitute(self, mapping: Dict[str, "SymbolicNode44"]) -> "SymbolicNode44":
        return mapping.get(self.name, self)

    def __repr__(self) -> str:
        return f"Var({self.name})"


class BinOpNode44(SymbolicNode44):
    def __init__(self, op: str, left: SymbolicNode44, right: SymbolicNode44):
        self.op = op
        self.left = left
        self.right = right

    def evaluate(self, env: Dict[str, Number]) -> Number:
        lv = self.left.evaluate(env)
        rv = self.right.evaluate(env)

        if self.op == "+":
            return lv + rv
        if self.op == "-":
            return lv - rv
        if self.op == "*":
            return lv * rv
        if self.op == "/":
            return lv / rv
        if self.op == "^":
            return lv ** rv

        raise ValueError(f"Unsupported operator: {self.op}")

    def substitute(self, mapping: Dict[str, SymbolicNode44]) -> "SymbolicNode44":
        return BinOpNode44(
            self.op,
            self.left.substitute(mapping),
            self.right.substitute(mapping),
        )

    def simplify(self) -> "SymbolicNode44":
        left_s = self.left.simplify()
        right_s = self.right.simplify()

        # Constant folding
        if isinstance(left_s, ConstNode44) and isinstance(right_s, ConstNode44):
            env: Dict[str, Number] = {}
            return ConstNode44(self.evaluate(env))

        # Neutral elements
        if self.op == "+":
            if isinstance(left_s, ConstNode44) and left_s.value == 0:
                return right_s
            if isinstance(right_s, ConstNode44) and right_s.value == 0:
                return left_s

        if self.op == "*":
            if isinstance(left_s, ConstNode44):
                if left_s.value == 0:
                    return ConstNode44(0)
                if left_s.value == 1:
                    return right_s
            if isinstance(right_s, ConstNode44):
                if right_s.value == 0:
                    return ConstNode44(0)
                if right_s.value == 1:
                    return left_s

        return BinOpNode44(self.op, left_s, right_s)

    def __repr__(self) -> str:
        return f"BinOp({self.op}, {self.left}, {self.right})"


class SymbolicParser44:
    """
    Deterministic parser for simple symbolic expressions.

    Grammar (informal):
        expr   := term (('+' | '-') term)*
        term   := factor (('*' | '/') factor)*
        factor := primary ('^' factor)?
        primary:= NUMBER | IDENT | '(' expr ')'
    """

    def __init__(self, text: str):
        self.text = text
        self.pos = 0
        self.length = len(text)

    # ------------- low-level helpers -------------

    def _peek(self) -> Optional[str]:
        if self.pos >= self.length:
            return None
        return self.text[self.pos]

    def _consume(self) -> Optional[str]:
        ch = self._peek()
        if ch is not None:
            self.pos += 1
        return ch

    def _skip_ws(self) -> None:
        while self._peek() is not None and self._peek().isspace():
            self._consume()

    # ------------- token readers -------------

    def _read_number(self) -> ConstNode44:
        start = self.pos
        dot_seen = False

        while True:
            ch = self._peek()
            if ch is None:
                break
            if ch.isdigit():
                self._consume()
            elif ch == "." and not dot_seen:
                dot_seen = True
                self._consume()
            else:
                break

        num_str = self.text[start:self.pos]
        if not num_str:
            raise ValueError("Expected number")

        if "." in num_str:
            return ConstNode44(float(num_str))
        return ConstNode44(int(num_str))

    def _read_ident(self) -> VarNode44:
        start = self.pos
        ch = self._peek()
        if ch is None or not (ch.isalpha() or ch == "_"):
            raise ValueError("Expected identifier")

        self._consume()
        while True:
            ch = self._peek()
            if ch is None:
                break
            if ch.isalnum() or ch == "_":
                self._consume()
            else:
                break

        name = self.text[start:self.pos]
        return VarNode44(name)

    # ------------- grammar rules -------------

    def parse(self) -> SymbolicNode44:
        node = self._parse_expr()
        self._skip_ws()
        if self._peek() is not None:
            raise ValueError(f"Unexpected character at position {self.pos}: {self._peek()}")
        return node

    def _parse_expr(self) -> SymbolicNode44:
        node = self._parse_term()
        while True:
            self._skip_ws()
            ch = self._peek()
            if ch in ("+", "-"):
                op = self._consume()
                right = self._parse_term()
                node = BinOpNode44(op, node, right)
            else:
                break
        return node

    def _parse_term(self) -> SymbolicNode44:
        node = self._parse_factor()
        while True:
            self._skip_ws()
            ch = self._peek()
            if ch in ("*", "/"):
                op = self._consume()
                right = self._parse_factor()
                node = BinOpNode44(op, node, right)
            else:
                break
        return node

    def _parse_factor(self) -> SymbolicNode44:
        node = self._parse_primary()
        self._skip_ws()
        ch = self._peek()
        if ch == "^":
            self._consume()
            right = self._parse_factor()
            node = BinOpNode44("^", node, right)
        return node

    def _parse_primary(self) -> SymbolicNode44:
        self._skip_ws()
        ch = self._peek()

        if ch is None:
            raise ValueError("Unexpected end of input")

        if ch.isdigit():
            return self._read_number()

        if ch.isalpha() or ch == "_":
            return self._read_ident()

        if ch == "(":
            self._consume()
            node = self._parse_expr()
            self._skip_ws()
            if self._peek() != ")":
                raise ValueError("Expected ')'")
            self._consume()
            return node

        if ch == "+":
            self._consume()
            return self._parse_primary()

        if ch == "-":
            self._consume()
            zero = ConstNode44(0)
            return BinOpNode44("-", zero, self._parse_primary())

        raise ValueError(f"Unexpected character: {ch}")


class ReasoningSymbolicSolver44:
    """
    High-level interface for symbolic solving in Reasoning Engine 4.4.
    """

    def __init__(self):
        self.initialized = False
        self.degraded_mode = False

    # ------------------------------------------------------------------
    # INITIALIZATION
    # ------------------------------------------------------------------
    def initialize(self) -> Dict[str, Any]:
        if self.initialized:
            return {"status": "already_initialized"}

        try:
            self.initialized = True
            return {"status": "initialized"}
        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "exception": str(exc)}

    # ------------------------------------------------------------------
    # PARSE EXPRESSION
    # ------------------------------------------------------------------
    def parse(self, expr: str) -> Dict[str, Any]:
        try:
            parser = SymbolicParser44(expr)
            node = parser.parse()
            return {"status": "ok", "ast": node}
        except Exception as exc:
            return {"status": "error", "exception": str(exc)}

    # ------------------------------------------------------------------
    # EVALUATE EXPRESSION
    # ------------------------------------------------------------------
    def evaluate(self, expr: str, env: Dict[str, Number]) -> Dict[str, Any]:
        parsed = self.parse(expr)
        if parsed.get("status") != "ok":
            return parsed

        node: SymbolicNode44 = parsed["ast"]
        try:
            value = node.evaluate(env)
            return {"status": "ok", "value": value}
        except Exception as exc:
            return {"status": "error", "exception": str(exc)}

    # ------------------------------------------------------------------
    # SIMPLIFY EXPRESSION
    # ------------------------------------------------------------------
    def simplify(self, expr: str) -> Dict[str, Any]:
        parsed = self.parse(expr)
        if parsed.get("status") != "ok":
            return parsed

        node: SymbolicNode44 = parsed["ast"]
        try:
            simplified = node.simplify()
            return {"status": "ok", "ast": simplified}
        except Exception as exc:
            return {"status": "error", "exception": str(exc)}

    # ------------------------------------------------------------------
    # SUBSTITUTE VARIABLES
    # ------------------------------------------------------------------
    def substitute(
        self,
        expr: str,
        mapping: Dict[str, str],
    ) -> Dict[str, Any]:
        """
        Substitute variables in expr with other expressions (given as strings).
        """

        parsed = self.parse(expr)
        if parsed.get("status") != "ok":
            return parsed

        node: SymbolicNode44 = parsed["ast"]

        # Parse mapping expressions
        sub_map: Dict[str, SymbolicNode44] = {}
        for name, sub_expr in mapping.items():
            sub_parsed = self.parse(sub_expr)
            if sub_parsed.get("status") != "ok":
                return {
                    "status": "error",
                    "reason": "substitution_parse_failed",
                    "var": name,
                    "details": sub_parsed,
                }
            sub_map[name] = sub_parsed["ast"]

        try:
            new_node = node.substitute(sub_map)
            return {"status": "ok", "ast": new_node}
        except Exception as exc:
            return {"status": "error", "exception": str(exc)}

    # ------------------------------------------------------------------
    # STATUS
    # ------------------------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "status": "ok",
            "initialized": self.initialized,
            "degraded_mode": self.degraded_mode,
        }

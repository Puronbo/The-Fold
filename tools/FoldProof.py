"""FoldProof: a tiny, auditable equality checker and Fold-state model.

This is an experimental companion to the Lean development, not a Lean
replacement and not a proof of the soundness of arbitrary mathematics.

The equality kernel accepts expressions in the commutative polynomial
language Z[x_1, ..., x_n] (integer constants, variables, addition,
multiplication). It decides equality by reducing both sides to the same
canonical sparse polynomial. The checker itself does not accept callbacks,
Python eval, or user-supplied proof functions.

Run:
    python FoldProof.py

The Fold-state examples are executable model checks. They are deliberately
kept separate from the symbolic equality kernel.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Tuple, Union

Monomial = Tuple[str, ...]
Polynomial = Dict[Monomial, int]


@dataclass(frozen=True)
class Expr:
    op: str
    arg: Union[int, str, Tuple["Expr", "Expr"]]


def const(n: int) -> Expr:
    return Expr("const", n)


def var(name: str) -> Expr:
    if not name or not name.isidentifier():
        raise ValueError("variable names must be nonempty identifiers")
    return Expr("var", name)


def add(a: Expr, b: Expr) -> Expr:
    return Expr("add", (a, b))


def mul(a: Expr, b: Expr) -> Expr:
    return Expr("mul", (a, b))


def _clean(p: Polynomial) -> Polynomial:
    return {m: c for m, c in p.items() if c != 0}


def normalize(e: Expr) -> Polynomial:
    """Return the canonical sparse polynomial for an expression."""
    if e.op == "const":
        n = e.arg
        if not isinstance(n, int):
            raise TypeError("malformed integer constant")
        return {} if n == 0 else {(): n}
    if e.op == "var":
        name = e.arg
        if not isinstance(name, str):
            raise TypeError("malformed variable")
        return {(name,): 1}
    if e.op not in ("add", "mul") or not isinstance(e.arg, tuple):
        raise ValueError("unknown or malformed expression")
    a, b = e.arg
    pa, pb = normalize(a), normalize(b)
    if e.op == "add":
        out = dict(pa)
        for m, c in pb.items():
            out[m] = out.get(m, 0) + c
        return _clean(out)
    out: Polynomial = {}
    for ma, ca in pa.items():
        for mb, cb in pb.items():
            monomial = tuple(sorted(ma + mb))
            out[monomial] = out.get(monomial, 0) + ca * cb
    return _clean(out)


@dataclass(frozen=True)
class EqualityCertificate:
    left: Expr
    right: Expr


def check_equality(cert: EqualityCertificate) -> bool:
    """Check an equality in the polynomial language by canonicalization."""
    try:
        return normalize(cert.left) == normalize(cert.right)
    except (TypeError, ValueError):
        return False


@dataclass(frozen=True)
class State:
    value: int
    reference: int
    direction: int  # +1 forward, -1 backward
    history: Tuple[str, ...] = ()


def initial(reference: int) -> State:
    if reference < 0:
        raise ValueError("reference must be a natural number")
    return State(value=1, reference=reference, direction=-1)


def collapse(s: State) -> State:
    return State(0, s.reference, s.direction, s.history + ("collapse",))


def turn(s: State) -> State:
    return State(s.value, s.reference, -s.direction, s.history + ("turn",))


def move(s: State, steps: int) -> State:
    if steps < 0:
        raise ValueError("steps must be natural")
    return State(
        s.value + s.direction * steps,
        s.reference,
        s.direction,
        s.history + (f"move({steps})",),
    )


def observable(s: State) -> int:
    """The reference-free observation: only the numeric position."""
    return s.value


def run_checks() -> None:
    x, y = var("x"), var("y")
    checks = []

    checks.append(("x + 0 = x", check_equality(
        EqualityCertificate(add(x, const(0)), x))))
    checks.append(("x * 1 = x", check_equality(
        EqualityCertificate(mul(x, const(1)), x))))
    checks.append(("commutativity", check_equality(
        EqualityCertificate(add(x, y), add(y, x)))))
    checks.append(("distributivity", check_equality(
        EqualityCertificate(mul(x, add(y, const(2))),
                            add(mul(x, y), mul(const(2), x))))))
    checks.append(("reject false equality", not check_equality(
        EqualityCertificate(add(const(7), mul(const(2), const(3))),
                            const(14)))))

    a, b = initial(2), initial(4)
    ca, cb = collapse(a), collapse(b)
    checks.append(("both collapsed observations are zero",
                   observable(ca) == observable(cb) == 0))
    checks.append(("retained references distinguish states",
                   ca.reference != cb.reference and ca != cb))
    checks.append(("two turns restore direction",
                   turn(turn(a)).direction == a.direction))
    checks.append(("collapse-turn-move restores one",
                   move(turn(collapse(a)), 1).value == 1))
    checks.append(("collapse preserves reference",
                   ca.reference == a.reference))
    checks.append(("reference-free observations cannot distinguish",
                   observable(ca) == observable(cb)))

    failed = [name for name, passed in checks if not passed]
    for name, passed in checks:
        print(f"{'PASS' if passed else 'FAIL'}  {name}")
    print(f"{len(checks) - len(failed)}/{len(checks)} checks passed")
    if failed:
        raise SystemExit("failed checks: " + ", ".join(failed))


if __name__ == "__main__":
    run_checks()

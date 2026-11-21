#!/usr/bin/env python3
"""Reference experiment for UF-001. Standard library only."""
from __future__ import annotations
from collections import Counter
from dataclasses import dataclass
from math import gcd, lcm
from typing import Iterable

Signature = tuple[int, int]


@dataclass(frozen=True)
class State:
    components: tuple[Signature, ...]
    orientation: int = 0

    def __post_init__(self) -> None:
        if self.orientation not in (0, 1):
            raise ValueError("orientation must be 0 or 1")
        for d, tau in self.components:
            if d < 1 or tau not in (0, 1) or (tau and d % 2):
                raise ValueError("invalid spectral signature")


def lcm_many(xs: Iterable[int]) -> int:
    out = 1
    for x in xs:
        if x < 1:
            raise ValueError("values must be positive")
        out = lcm(out, x)
    return out


def pi(sig: Signature, r: int) -> Signature:
    d, tau = sig
    if r < 1:
        raise ValueError("exponent must be positive")
    d1 = d // gcd(d, r)
    return d1, int(bool(tau) and d1 % 2 == 0)


def power(state: State, r: int) -> State:
    return State(tuple(pi(s, r) for s in state.components), state.orientation)


def turn(state: State) -> State:
    return State(state.components, 1 - state.orientation)


def core(d: int, L: int) -> int:
    if d < 1 or L < 1:
        raise ValueError("d and L must be positive")
    while gcd(d, L) != 1:
        d //= gcd(d, L)
    return d


def invariant(state: State, exponents: Iterable[int]) -> tuple[Signature, ...]:
    rs = tuple(exponents)
    L = lcm_many(rs)
    return tuple((core(d, L), tau if L % 2 else 0)
                 for d, tau in state.components)


def steps_to_stable(d: int, E: int) -> int:
    k = 0
    while True:
        nxt = d // gcd(d, E)
        if nxt == d:
            return k
        d, k = nxt, k + 1


def terminal(state: State, exponents: Iterable[int]) -> State:
    rs = tuple(exponents)
    E = 1
    for r in rs:
        if r < 1:
            raise ValueError("exponents must be positive")
        E *= r
    out = state
    if E > 1:
        k = max((steps_to_stable(d, E) for d, _ in out.components), default=0)
        for _ in range(k):
            out = power(out, E)
    return turn(out) if out.orientation else out


def order_mod(a: int, m: int) -> int:
    if m < 2 or gcd(a, m) != 1:
        raise ValueError("a must be a unit modulo m >= 2")
    a %= m
    x, d = a, 1
    while x != 1:
        x = x * a % m
        d += 1
        if d > m:
            raise ArithmeticError("order search failed")
    return d


def residue_signature(a: int, m: int) -> Signature:
    d = order_mod(a, m)
    tau = int(d % 2 == 0 and pow(a, d // 2, m) == m - 1)
    return d, tau


def enumerate_classes(moduli: list[int], exponents: list[int]) -> dict[str, int]:
    M = lcm_many(moduli)
    states = {
        tuple(residue_signature(a, m) for m in moduli)
        for a in range(1, M) if gcd(a, M) == 1
    }
    classes = {invariant(State(s), exponents) for s in states}
    return {
        "combined_modulus": M,
        "unit_count": sum(gcd(a, M) == 1 for a in range(1, M)),
        "spectral_state_count": len(states),
        "invariant_class_count": len(classes),
    }


def verify(max_order: int = 120) -> dict[str, int]:
    invariance = terminal_checks = orientation_checks = composition = 0
    families = ([], [2], [3], [2, 5], [2, 3, 5], [6])
    for d in range(1, max_order + 1):
        taus = (0, 1) if d % 2 == 0 else (0,)
        for tau in taus:
            for eps in (0, 1):
                s = State(((d, tau),), eps)
                for rs in families:
                    inv = invariant(s, rs)
                    for r in rs:
                        assert invariant(power(s, r), rs) == inv
                        invariance += 1
                    assert invariant(turn(s), rs) == inv
                    invariance += 1
                    end = terminal(s, rs)
                    assert end.components == inv and end.orientation == 0
                    terminal_checks += 1
                    other = State(((d, tau),), 1 - eps)
                    assert terminal(other, rs) == end
                    orientation_checks += 1
                    for a in range(1, 7):
                        for b in range(1, 7):
                            assert pi(pi((d, tau), a), b) == pi((d, tau), a * b)
                            composition += 1
    sample = State(((2, 1), (4, 1), (6, 1)), 1)
    collapsed = power(sample, lcm_many(d for d, _ in sample.components))
    collapsed = turn(collapsed) if collapsed.orientation else collapsed
    assert collapsed.components == ((1, 0), (1, 0), (1, 0))
    assert collapsed.orientation == 0
    return {
        "invariance": invariance,
        "canonical_terminal": terminal_checks,
        "orientation_quotient": orientation_checks,
        "power_composition": composition,
        "all_powers_collapse": 1,
    }


def main() -> None:
    for rs in ([2], [3], [5], [6], [2, 3, 5]):
        print(f"R={rs}: {enumerate_classes([4, 5, 7], list(rs))}")
    print("bounded checks:", verify())


if __name__ == "__main__":
    main()

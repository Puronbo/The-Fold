#!/usr/bin/env python3
"""UF-002: minimum sets of reusable power-exponent types for spectral cores.

A selected exponent type may be applied repeatedly. The solver minimizes the
number or weighted cost of distinct allowed exponents, not individual
applications needed to reach the terminal prime core.
"""
from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from math import gcd, lcm
from typing import Iterable, Optional


def prime_support(n: int) -> frozenset[int]:
    if n < 1:
        raise ValueError("support is defined for positive integers")
    result: set[int] = set()
    p = 2
    while p * p <= n:
        if n % p == 0:
            result.add(p)
            while n % p == 0:
                n //= p
        p = 3 if p == 2 else p + 2
    if n > 1:
        result.add(n)
    return frozenset(result)


def valuation(n: int, p: int) -> int:
    count = 0
    while n % p == 0:
        count += 1
        n //= p
    return count


def prime_core(n: int, L: int) -> int:
    """Largest divisor of n coprime to L."""
    if n < 1 or L < 1:
        raise ValueError("n and L must be positive")
    while gcd(n, L) != 1:
        n //= gcd(n, L)
    return n


@dataclass(frozen=True)
class TargetProfile:
    keep: frozenset[int]
    erase: frozenset[int]
    per_coordinate_keep: tuple[frozenset[int], ...]
    per_coordinate_erase: tuple[frozenset[int], ...]


def derive_target_profile(original_orders: Iterable[int], target_orders: Iterable[int]) -> TargetProfile:
    originals, targets = tuple(original_orders), tuple(target_orders)
    if not originals or len(originals) != len(targets):
        raise ValueError("original and target orders must have equal nonzero length")
    keep_all: set[int] = set()
    erase_all: set[int] = set()
    keeps, erases = [], []
    for d, c in zip(originals, targets):
        if d < 1 or c < 1 or d % c:
            raise ValueError(f"target order {c} must divide original order {d}")
        sd, sc = prime_support(d), prime_support(c)
        for q in sd:
            vc, vd = valuation(c, q), valuation(d, q)
            if vc not in (0, vd):
                raise ValueError(
                    f"target {c} partially retains the {q}-primary component of {d}"
                )
        keep_j, erase_j = sc, sd - sc
        keep_all.update(keep_j)
        erase_all.update(erase_j)
        keeps.append(keep_j)
        erases.append(erase_j)
    return TargetProfile(frozenset(keep_all), frozenset(erase_all),
                         tuple(keeps), tuple(erases))


def minimum_operation_family(
    profile: TargetProfile,
    allowed_exponents: Iterable[int],
    costs: Optional[dict[int, float]] = None,
) -> Optional[tuple[int, ...]]:
    """Exact minimum-cardinality or minimum-cost safe set cover of exponent types."""
    D = tuple(sorted(profile.erase))
    K = profile.keep
    if K & profile.erase:
        return None
    if not D:
        return ()
    bit = {q: 1 << i for i, q in enumerate(D)}
    candidates: list[tuple[int, int, float]] = []
    seen: set[int] = set()
    for r in allowed_exponents:
        if r < 2 or r in seen:
            continue
        seen.add(r)
        support = prime_support(r)
        if support & K:
            continue
        mask = 0
        for q in support & profile.erase:
            mask |= bit[q]
        if not mask:
            continue
        cost = float(costs[r]) if costs is not None and r in costs else 1.0
        if cost < 0:
            raise ValueError("costs must be nonnegative")
        candidates.append((r, mask, cost))

    full = (1 << len(D)) - 1
    dp: dict[int, tuple[float, tuple[int, ...]]] = {0: (0.0, ())}
    for r, mask, cost in candidates:
        updated = dict(dp)
        for old_mask, (old_cost, old_set) in dp.items():
            new_mask = old_mask | mask
            proposed_set = old_set + (r,)
            proposed = (old_cost + cost, proposed_set)
            current = updated.get(new_mask)
            if current is None or proposed[0] < current[0] or (
                proposed[0] == current[0] and len(proposed[1]) < len(current[1])
            ):
                updated[new_mask] = proposed
        dp = updated
    return dp[full][1] if full in dp else None


def brute_force_cover(profile: TargetProfile, allowed_exponents: Iterable[int]) -> Optional[tuple[int, ...]]:
    """Small-input oracle used to validate the dynamic-programming solver."""
    if profile.keep & profile.erase:
        return None
    if not profile.erase:
        return ()
    safe = sorted({r for r in allowed_exponents
                   if r >= 2 and not (prime_support(r) & profile.keep)})
    target = set(profile.erase)
    for count in range(len(safe) + 1):
        for chosen in combinations(safe, count):
            covered: set[int] = set()
            for r in chosen:
                covered.update(prime_support(r) & target)
            if covered == target:
                return chosen
    return None




def rounds_to_stable(original_orders: Iterable[int], operations: Iterable[int]) -> int:
    """Rounds when each selected exponent type is applied once per round."""
    orders, ops = tuple(original_orders), tuple(operations)
    if any(r < 2 for r in ops):
        raise ValueError("operation exponents must be at least 2")
    rounds = 0
    for d in orders:
        for q in prime_support(d):
            rate = sum(valuation(r, q) for r in ops)
            if rate:
                rounds = max(rounds, (valuation(d, q) + rate - 1) // rate)
    return rounds


def realized_targets(original_orders: Iterable[int], operations: Iterable[int]) -> tuple[int, ...]:
    ds = tuple(original_orders)
    L = 1
    for r in operations:
        if r < 1:
            raise ValueError("operation exponents must be positive")
        L = lcm(L, r)
    return tuple(prime_core(d, L) for d in ds)


def unrestricted_minimum(profile: TargetProfile) -> tuple[int, ...]:
    """Minimum reusable exponent types with arbitrary composites: zero or one."""
    if profile.keep & profile.erase:
        raise ValueError("global keep/erase conflict")
    if not profile.erase:
        return ()
    product = 1
    for q in sorted(profile.erase):
        product *= q
    return (product,)


def verify() -> dict[str, int]:
    catalogue_checks = 0
    catalogues = (
        (2, 3, 6, 10, 15, 21, 35),
        (2, 3, 5, 7),
        (6, 10, 14, 15, 21, 35),
        (4, 9, 25, 49, 6, 10, 14),
    )
    for catalog in catalogues:
        for d in range(1, 100):
            primes = sorted(prime_support(d))
            for mask in range(1 << len(primes)):
                target = 1
                for i, q in enumerate(primes):
                    if mask & (1 << i):
                        target *= q ** valuation(d, q)
                profile = derive_target_profile((d,), (target,))
                exact = minimum_operation_family(profile, catalog)
                brute = brute_force_cover(profile, catalog)
                assert (exact is None) == (brute is None)
                if exact is not None:
                    assert len(exact) == len(brute)
                catalogue_checks += 1

    profile_checks = 0
    for d1 in range(1, 80):
        for d2 in range(1, 50):
            p1, p2 = sorted(prime_support(d1)), sorted(prime_support(d2))
            for mask1 in range(1 << len(p1)):
                c1 = 1
                for i, q in enumerate(p1):
                    if mask1 & (1 << i):
                        c1 *= q ** valuation(d1, q)
                for mask2 in range(1 << len(p2)):
                    c2 = 1
                    for i, q in enumerate(p2):
                        if mask2 & (1 << i):
                            c2 *= q ** valuation(d2, q)
                profile = derive_target_profile((d1, d2), (c1, c2))
                if profile.keep & profile.erase:
                    continue
                ops = unrestricted_minimum(profile)
                assert realized_targets((d1, d2), ops) == (c1, c2)
                profile_checks += 1

    conflict = derive_target_profile((12, 15), (4, 3))
    assert conflict.keep & conflict.erase == frozenset({3})
    assert minimum_operation_family(conflict, (2, 3, 5, 6, 10, 15)) is None

    worked = derive_target_profile((720, 98), (5, 49))
    assert minimum_operation_family(worked, (2, 3, 6, 10, 15, 21, 35)) == (6,)
    assert realized_targets((720, 98), (6,)) == (5, 49)
    assert rounds_to_stable((720, 98), (6,)) == 4
    assert rounds_to_stable((720, 98), (2, 3)) == 4
    assert minimum_operation_family(worked, (2, 3, 5, 7)) == (2, 3)

    return {
        "DP_vs_bruteforce_checks": catalogue_checks,
        "global_target_reconstruction_checks": profile_checks,
        "conflict_and_example_checks": 4,
    }


def main() -> None:
    profile = derive_target_profile((720, 98), (5, 49))
    catalogue = (2, 3, 6, 10, 15, 21, 35)
    print("keep primes:", sorted(profile.keep))
    print("erase primes:", sorted(profile.erase))
    print("catalogue minimum:", minimum_operation_family(profile, catalogue))
    print("unrestricted minimum:", unrestricted_minimum(profile))
    print("prime-only minimum:", minimum_operation_family(profile, (2, 3, 5, 7)))
    print("terminal targets after repeated exponent-6 applications:", realized_targets((720, 98), (6,)))
    conflict = derive_target_profile((12, 15), (4, 3))
    print("global conflict K intersect D:", sorted(conflict.keep & conflict.erase))
    print("bounded verification:", verify())


if __name__ == "__main__":
    main()

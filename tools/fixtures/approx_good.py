"""Fixture: exact equality and documented tolerance, no findings."""

import math
from functools import cmp_to_key


class ExactPoint:
    def __init__(self, x):
        self.x = x

    def __eq__(self, other):
        return self.x == other.x

    def __hash__(self):
        return hash(self.x)


def close(a, b):
    return math.isclose(a, b, rel_tol=1e-9, abs_tol=1e-12)


def by_exact_order(a, b):
    return (a > b) - (a < b)


ordered = sorted([1.0, 2.0], key=cmp_to_key(by_exact_order))


def canonical_key(x):
    # Rounding is a function, so the key is exact; it is a canonicalization,
    # not a tolerance.
    return round(x, 6)


class ExplicitlyUnhashable:
    """An approximate __eq__ with __hash__ = None is a deliberate non-quotient."""

    def __init__(self, x):
        self.x = x

    def __eq__(self, other):
        return abs(self.x - other.x) < 1e-9

    __hash__ = None

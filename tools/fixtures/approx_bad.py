"""Fixture: tolerance used as equality, in two places."""

import math
from functools import cmp_to_key, total_ordering


class ApproxPoint:
    def __init__(self, x):
        self.x = x

    def __eq__(self, other):
        return math.isclose(self.x, other.x, rel_tol=1e-9)

    def __hash__(self):
        return hash(round(self.x, 6))


class UnhashableApprox:
    def __init__(self, x):
        self.x = x

    def __eq__(self, other):
        return abs(self.x - other.x) < 1e-9


class AssignedHash:
    def __init__(self, x):
        self.x = x

    def __eq__(self, other):
        return math.isclose(self.x, other.x)

    __hash__ = object.__hash__


def by_tolerance(a, b):
    if math.isclose(a, b):
        return 0
    return -1 if a < b else 1


def exact_but_spelled_isclose(a, b):
    return math.isclose(a, b, rel_tol=0, abs_tol=0)


@total_ordering
class OrderedApprox:
    def __init__(self, x):
        self.x = x

    def __eq__(self, other):
        return math.isclose(self.x, other.x)

    def __lt__(self, other):
        return self.x < other.x


def exact_by_default(a, b):
    # abs_tol defaults to 0.0, so this is still ==.
    return math.isclose(a, b, rel_tol=0)


ordered = sorted([1.0, 2.0], key=cmp_to_key(by_tolerance))

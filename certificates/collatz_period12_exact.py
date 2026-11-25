#!/usr/bin/env python3
"""Exact period-12 accelerated Collatz cycle exclusion certificate."""
from math import comb

P = 12
A = 20
THREE_P = 3**P
Q = 2**A - THREE_P


def compositions(total, parts, prefix=()):
    if parts == 1:
        if total >= 1:
            yield prefix + (total,)
        return
    for first in range(1, total - parts + 2):
        yield from compositions(total - first, parts - 1, prefix + (first,))


def numerator(word):
    d = 0
    prefix_sum = 0
    for j, a in enumerate(word):
        d += 3 ** (P - 1 - j) * 2**prefix_sum
        prefix_sum += a
    return d


# Exact integer comparisons prove 19 < 12 log_2(3)
# and 12 log_2(10/3) < 21, so A=20 is forced.
assert 2**19 < THREE_P < 2**20
assert 2**20 * THREE_P < 10**12 < 2**21 * THREE_P
assert Q == 517_135

checked = 0
hits = []
for tail in compositions(A - 1, P - 1):
    word = (1,) + tail
    d = numerator(word)
    checked += 1
    if d % Q == 0:
        hits.append((word, d // Q))

assert checked == comb(18, 10) == 43_758
assert hits == []

print("period 12: checked", checked, "minimum-rotated valuation words")
print("denominator:", Q)
print("divisibility hits:", hits)
print("certificate: PASS")

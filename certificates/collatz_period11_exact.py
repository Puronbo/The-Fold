#!/usr/bin/env python3
"""Exact period-11 accelerated Collatz cycle exclusion certificate."""
from math import comb

P = 11
THREE_P = 3**P


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


# For every nontrivial cycle, 11 log_2(3) < A
# < 11 log_2(10/3), so the only integer totals are 18 and 19.
assert 3**11 < 2**18 and 2**17 < 3**11
assert 2**19 < (10 / 3) ** 11 < 2**20

checked = 0
hits = []
counts = {}
for A in (18, 19):
    q = 2**A - THREE_P
    count = 0
    for tail in compositions(A - 1, P - 1):
        word = (1,) + tail
        d = numerator(word)
        checked += 1
        count += 1
        if d % q == 0:
            hits.append((A, word, d // q))
    counts[A] = count

assert counts == {18: comb(16, 9), 19: comb(17, 9)}
assert checked == 35_750
assert hits == []

print("period 11: checked", checked, "minimum-rotated valuation words")
print("counts by total:", counts)
print("divisibility hits:", hits)
print("certificate: PASS")

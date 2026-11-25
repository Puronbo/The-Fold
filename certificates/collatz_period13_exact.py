#!/usr/bin/env python3
"""Exact period-13 accelerated Collatz cycle exclusion certificate."""
from math import comb

P = 13
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


# Exact integer comparisons force A in {21, 22}.
assert 2**20 < THREE_P < 2**21
assert 2**22 * THREE_P < 10**13 < 2**23 * THREE_P

expected = {21: comb(19, 8), 22: comb(20, 8)}
assert expected == {21: 75_582, 22: 167_960}

checked = 0
hits = []
for A in (21, 22):
    q = 2**A - THREE_P
    count = 0
    for tail in compositions(A - 1, P - 1):
        word = (1,) + tail
        d = numerator(word)
        checked += 1
        count += 1
        if d % q == 0:
            hits.append((A, word, d // q))
    assert count == expected[A]

assert checked == 243_542
assert hits == []

print("period 13: checked", checked, "minimum-rotated valuation words")
print("counts by total:", expected)
print("divisibility hits:", hits)
print("certificate: PASS")

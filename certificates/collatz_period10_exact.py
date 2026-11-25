#!/usr/bin/env python3
"""Exact certificate excluding nontrivial accelerated Collatz cycles of period 10.

Only words with a_0=1 are needed: rotate any hypothetical nontrivial
cycle to its smallest odd member, whose valuation is necessarily one.
All arithmetic in the divisibility test is integer arithmetic.
"""
from math import comb

P = 10
THREE_P = 3**P
C = THREE_P - 2**P


def compositions(total, parts, prefix=()):
    if parts == 1:
        if total >= 1:
            yield prefix + (total,)
        return
    for first in range(1, total - parts + 2):
        yield from compositions(total - first, parts - 1, prefix + (first,))


def numerator(word):
    value = 0
    prefix_sum = 0
    for j, a in enumerate(word):
        value += 3 ** (P - 1 - j) * 2**prefix_sum
        prefix_sum += a
    return value


def accelerated(n):
    value = 3 * n + 1
    while value % 2 == 0:
        value //= 2
    return value


def steps_to_one(n):
    steps = 0
    while n != 1:
        n = accelerated(n)
        steps += 1
    return steps


checked = 0
hits = []
for A in range(16, 24):
    q = 2**A - THREE_P
    for tail in compositions(A - 1, P - 1):
        word = (1,) + tail
        D = numerator(word)
        checked += 1
        if D % q == 0:
            hits.append((A, word, D // q))

assert checked == sum(comb(A - 2, 8) for A in range(16, 24))
assert checked == 495_418
assert hits == []

# For A >= 24 the universal numerator bound gives n < 57.
assert C * 2**14 < 57 * (2**24 - THREE_P)
for A in range(24, 80):
    assert C * 2 ** (A - P) < 57 * (2**A - THREE_P)

# The minimum of a nontrivial cycle would be an odd n in this range.
candidate_steps = {n: steps_to_one(n) for n in range(3, 57, 2)}
assert len(candidate_steps) == 27
assert all(steps > 0 for steps in candidate_steps.values())
assert max(candidate_steps.values()) == 41
assert candidate_steps[27] == 41

print("period 10: checked", checked, "minimum-rotated valuation words")
print("divisibility hits:", hits)
print("large-total bound: n < 57 for all A >= 24")
print("odd candidates 3..55 all reach 1; maximum steps:", max(candidate_steps.values()))
print("certificate: PASS")

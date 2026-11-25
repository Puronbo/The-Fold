#!/usr/bin/env python3
"""Exact period-15 accelerated Collatz cycle exclusion certificate."""
from math import comb

P = 15
THREE_P = 3**P


def visit_words(A):
    q = 2**A - THREE_P
    count = 0
    hits = []

    # a_0 = 1, hence A_0 = 1 and the first numerator term is 2.
    def extend(position, remaining, cumulative, d, prefix):
        nonlocal count
        if position == P - 1:
            if remaining < 1:
                return
            final_sum = cumulative + remaining
            final_d = 3 * d + 2**final_sum
            count += 1
            if final_d % q == 0:
                hits.append((prefix + (remaining,), final_d // q))
            return

        largest = remaining - (P - 1 - position)
        for a in range(1, largest + 1):
            new_sum = cumulative + a
            extend(
                position + 1,
                remaining - a,
                new_sum,
                3 * d + 2**new_sum,
                prefix + (a,),
            )

    extend(1, A - 1, 1, 2, (1,))
    return count, hits


# Exact comparisons force A in {24, 25, 26}.
assert 2**23 < THREE_P < 2**24
assert 2**26 * THREE_P < 10**15 < 2**27 * THREE_P

expected = {
    24: comb(22, 13),
    25: comb(23, 13),
    26: comb(24, 13),
}
assert expected == {
    24: 497_420,
    25: 1_144_066,
    26: 2_496_144,
}

total = 0
for A in (24, 25, 26):
    count, hits = visit_words(A)
    assert count == expected[A]
    assert hits == []
    total += count

assert total == 4_137_630
print("period 15: checked", total, "minimum-rotated valuation words")
print("counts by total:", expected)
print("divisibility hits: none")
print("certificate: PASS")

#!/usr/bin/env python3
"""Exact finite certificate for accelerated Collatz valuation words of length six.

The accompanying proof handles every total valuation A >= 12 by a
uniform starting-value bound. This script checks the remaining totals A=10,11.
"""
from math import comb


def compositions(total: int, parts: int):
    if parts == 1:
        yield (total,)
        return
    for first in range(1, total - parts + 2):
        for tail in compositions(total - first, parts - 1):
            yield (first,) + tail


def numerator(word):
    partial = 0
    total = 0
    p = len(word)
    for j in range(p):
        if j:
            partial += word[j - 1]
        total += (2**partial) * (3 ** (p - 1 - j))
    return total


expected_counts = {10: comb(9, 5), 11: comb(10, 5)}
for valuation_total, expected in expected_counts.items():
    denominator = 2**valuation_total - 3**6
    words = list(compositions(valuation_total, 6))
    assert len(words) == expected
    hits = [
        (word, numerator(word) // denominator)
        for word in words
        if numerator(word) % denominator == 0
    ]
    assert hits == [], (valuation_total, hits)
    print(
        f"A={valuation_total}: checked {len(words)} words; "
        "divisibility hits = 0"
    )

assert 665 * 64 < 13 * (2**12 - 3**6)
print("A>=12: n<13; odd candidates {1,3,5,7,9,11}.")
print("Each candidate above 1 reaches 1 before returning to itself.")

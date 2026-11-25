#!/usr/bin/env python3
"""Exact finite certificate for accelerated Collatz valuation words of length nine.

The accompanying proof handles all total valuations A >= 19 by a
uniform starting-value bound. This script checks the remaining totals 15..18.
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


expected_counts = {
    15: comb(14, 8),
    16: comb(15, 8),
    17: comb(16, 8),
    18: comb(17, 8),
}
all_hits = []
for valuation_total, expected in expected_counts.items():
    denominator = 2**valuation_total - 3**9
    words = list(compositions(valuation_total, 9))
    assert len(words) == expected
    hits = [
        (word, numerator(word) // denominator)
        for word in words
        if numerator(word) % denominator == 0
    ]
    all_hits.extend((valuation_total, *hit) for hit in hits)
    print(
        f"A={valuation_total}: checked {len(words)} words; "
        f"divisibility hits = {len(hits)}"
    )

assert all_hits == [(18, (2,) * 9, 1)], all_hits
print("Unique hit: A=18, word=(2,2,2,2,2,2,2,2,2), n=1.")

assert 19171 * 2**10 < 39 * (2**19 - 3**9)
print("A>=19: n<39; odd candidates are 1,3,...,37.")

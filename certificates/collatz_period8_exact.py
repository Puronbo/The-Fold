#!/usr/bin/env python3
"""Exact finite certificate for accelerated Collatz valuation words of length eight.

The accompanying proof handles every total valuation A >= 18 by a
uniform starting-value bound. This script checks the remaining totals 13..17.
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
    13: comb(12, 7),
    14: comb(13, 7),
    15: comb(14, 7),
    16: comb(15, 7),
    17: comb(16, 7),
}
all_hits = []
for valuation_total, expected in expected_counts.items():
    denominator = 2**valuation_total - 3**8
    words = list(compositions(valuation_total, 8))
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

assert all_hits == [(16, (2, 2, 2, 2, 2, 2, 2, 2), 1)], all_hits
print("Unique hit: A=16, word=(2,2,2,2,2,2,2,2), n=1.")

assert 6305 * 2**10 < 26 * (2**18 - 3**8)
print("A>=18: n<26; odd candidates are 1,3,5,7,9,11,13,15,17,19,21,23,25.")

#!/usr/bin/env python3
"""Exact finite certificate for accelerated Collatz valuation words of length five.

All arithmetic is integer arithmetic. The script checks the only small-total
cases A=8,9; the proof in the accompanying note handles every A>=10 by a
uniform starting-value bound.
"""

def compositions(total: int, parts: int):
    if parts == 1:
        yield (total,)
        return
    for first in range(1, total - parts + 2):
        for tail in compositions(total - first, parts - 1):
            yield (first,) + tail


def numerator(word):
    a, b, c, d, _e = word
    return (
        81
        + 27 * 2**a
        + 9 * 2 ** (a + b)
        + 3 * 2 ** (a + b + c)
        + 2 ** (a + b + c + d)
    )


expected_counts = {8: 35, 9: 70}
for total, expected in expected_counts.items():
    denominator = 2**total - 243
    words = list(compositions(total, 5))
    assert len(words) == expected
    hits = [
        (word, numerator(word) // denominator)
        for word in words
        if numerator(word) % denominator == 0
    ]
    assert not hits, (total, hits)
    print(f"A={total}: checked {len(words)} words; divisibility hits = 0")

# For A >= 10, D <= 211*2**(A-5), so n=D/(2**A-243)
# <= 211*2**(A-5)/(2**A-243) <= 6752/781 < 9.
# Since n is odd, n is 1, 3, 5, or 7. Only 1 can return
# after five accelerated steps; it has valuation 2 at every step.
assert 6752 < 9 * 781
print("A>=10: n<9; odd candidates {1,3,5,7}; only fixed point 1 cycles.")

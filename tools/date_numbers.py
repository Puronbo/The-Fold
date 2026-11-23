"""The arithmetic of the date labels.

The four formats of 2000-10-26 are the integers

    10262000   10/26/2000
    26102000   26/10/2000
    20001026   2000-10-26
    20002610   2000/26/10

This script computes, with no dependencies:

1. their factorizations and divisor counts;
2. the mod-99 residue from the even/odd digit split;
3. the block lemma: every permutation of the even-length blocks
   10 | 26 | 2000 has residue 56, while a digit swap inside a block
   does not;
4. the tau scaling when a trailing 000 is appended.

Run: python tools/date_numbers.py
"""

from itertools import permutations


def factorize(n):
    f = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            f[p] = f.get(p, 0) + 1
            n //= p
        p += 1 if p == 2 else 2
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def tau(n):
    t = 1
    for e in factorize(n).values():
        t *= e + 1
    return t


def show_factor(n):
    f = factorize(n)
    return " * ".join(f"{p}^{e}" if e > 1 else str(p) for p, e in sorted(f.items()))


def split(n, width=8):
    s = str(n).zfill(width)[::-1]
    even = sum(int(c) for i, c in enumerate(s) if i % 2 == 0)
    odd = sum(int(c) for i, c in enumerate(s) if i % 2 == 1)
    return even, odd


LABELS = [
    ("10262000", "10/26/2000"),
    ("26102000", "26/10/2000"),
    ("20001026", "2000-10-26"),
    ("20002610", "2000/26/10"),
]

if __name__ == "__main__":
    print("the four labels of 2000-10-26\n")
    print(f"{'label':>9}  {'format':>10}  {'factorization':<20} {'tau':>4} {'E':>2} {'O':>2} {'mod 99':>6}")
    for s, fmt in LABELS:
        n = int(s)
        e, o = split(n)
        print(f"{s:>9}  {fmt:>10}  {show_factor(n):<20} {tau(n):>4} {e:>2} {o:>2} {n % 99:>6}")

    print("\nthe five-digit prefixes\n")
    for s, fmt in (("10262", "10/26/2"), ("26102", "26/10/2")):
        n = int(s)
        print(f"{s:>9}  {fmt:>10}  {show_factor(n):<20} {tau(n):>4}")

    print("\nall six permutations of the even-length blocks 10 | 26 | 2000\n")
    for p in permutations(("10", "26", "2000")):
        s = "".join(p)
        print(f"  {s}  {int(s) % 99:>3}")

    print("\ndigit swaps inside a block break the residue\n")
    for s in ("10262000", "10622000", "01262000"):
        print(f"  {s}  {int(s) % 99:>3}")

    print("\nthe padding hypothesis: 2 January 2000, padded and unpadded\n")
    for s in ("02012000", "20000201", "1202000", "2000012"):
        print(f"  {s:>8}  {int(s) % 99:>3}")

    print("\ntau when 000 is appended: tau(1000*m) = (a+4)(b+4)tau(q), m = 2^a 5^b q\n")
    for m in (10262, 26102):
        a = 0
        t = m
        while t % 2 == 0:
            a += 1
            t //= 2
        b = 0
        while t % 5 == 0:
            b += 1
            t //= 5
        print(f"  m = {m}: a = {a}, b = {b}, tau(q) = {tau(t)}, tau(1000m) = "
              f"{(a + 4) * (b + 4) * tau(t)}")

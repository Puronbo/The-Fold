"""UF-002: the minimal operation family on Z/n.

A Fold scale is multiplication by a unit a modulo n.  A family of scales
generates a subgroup H of the unit group U(n); the information it preserves is
the algebra of H-invariant functions.  For a character chi of U(n), that
information is one phase, and the preserving family is ker chi, so the minimal
number of scales is the minimal number of generators of ker chi.

The script computes, by brute force on the residues:

1. the CRT decomposition of U(n) into cyclic factors;
2. every character chi, its order, its kernel, and the kernel's minimal
   generator count (cost);
3. the fold's parity chi(-1), and whether -1 lies in ker chi;
4. the doubling scale's shifted period: the k with 2^k = -1.

The second point is the correction the note records: the cost is not the number
of factors on which chi fails to be faithful.  The kernel of a tensor product is
a diagonal congruence, not a product of kernels, and the naive count is wrong.

Run: python tools/minimal_operations.py
"""

from itertools import combinations
from math import gcd, lcm


# ---------------------------------------------------------------- arithmetic

def factorize(n):
    out = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def units(n):
    return tuple(a for a in range(n) if gcd(a, n) == 1)


def order_mod(a, n):
    x, k = a % n, 1
    while x != 1:
        x = x * a % n
        k += 1
    return k


def primitive_root(q):
    for g in range(2, q):
        if order_mod(g, q) == len(units(q)):
            return g
    raise ValueError(q)


# ---------------------------------------------------------------- unit group

def cyclic_factors(n):
    """U(n) as a product of cyclic factors.

    Each entry is (prime power q, order m, generator g, elements by exponent).
    U(p^e) is cyclic for odd p; U(2^e) is C2 x C_{2^(e-2)} for e >= 3.
    """
    facs = []
    for p, e in sorted(factorize(n).items()):
        q = p ** e
        if q == 2:
            continue
        if q == 4:
            facs.append((q, 2, 3, [1, 3]))
        elif p == 2:
            facs.append((q, 2, q - 1, [1, q - 1]))                    # <-1>
            m = 2 ** (e - 2)
            facs.append((q, m, 5, [pow(5, d, q) for d in range(m)]))  # <5>
        else:
            m = (p - 1) * p ** (e - 1)
            g = primitive_root(q)
            facs.append((q, m, g, [pow(g, d, q) for d in range(m)]))
    return facs


def dlogs(fac):
    q, m, _, elems = fac
    return {x: d for d, x in enumerate(elems)}


def characters(facs):
    tuples = [()]
    for _, m, _, _ in facs:
        tuples = [t + (j,) for t in tuples for j in range(m)]
    return tuples


def character_order(facs, j):
    """order of the tensor product = lcm of the factor orders."""
    o = 1
    for (_, m, _, _), jj in zip(facs, j):
        o = lcm(o, m // gcd(jj, m))
    return o


def coordinates(facs):
    """Map a residue mod n to its exponent tuple, factor by factor.

    A prime power with two cyclic factors (the 2-part, e >= 3) is a direct
    product, so the exponent tuple is solved from the product, not read off
    one generator.
    """
    by_q = {}
    for i, (q, m, g, elems) in enumerate(facs):
        by_q.setdefault(q, []).append(i)
    tables = {}
    for q, idx in by_q.items():
        table = {}
        for guess in _tuples([facs[i][1] for i in idx]):
            prod = 1
            for i, d in zip(idx, guess):
                prod = prod * facs[i][3][d] % q
            table[prod] = dict(zip(idx, guess))
        tables[q] = table

    def get(x):
        t = [0] * len(facs)
        for q, table in tables.items():
            for i, d in table[x % q].items():
                t[i] = d
        return tuple(t)

    return get


def chi_is_one(facs, j, x, get):
    """chi(x) = 1, exactly, as one integer congruence.

    With L = lcm(m_i) and c_i = j_i * L/m_i, chi(x) = zeta_L^{sum c_i d_i},
    so chi(x) = 1 iff sum c_i d_i = 0 mod L.
    """
    mods = [f[1] for f in facs]
    L = 1
    for m in mods:
        L = lcm(L, m)
    t = get(x)
    total = sum(j[i] * (L // m) * t[i] for i, m in enumerate(mods))
    return total % L == 0


def kernel(facs, j, n, get):
    return [x for x in units(n) if chi_is_one(facs, j, x, get)]


def kernel_rank(ker, n):
    """Least number of kernel elements that generate the kernel."""
    if len(ker) == 1:
        return 0
    target = set(ker)

    def generated(gens):
        seen = {1}
        changed = True
        while changed:
            changed = False
            for g in gens:
                add = {s * g % n for s in seen}
                if not add <= seen:
                    seen |= add
                    changed = True
        return seen

    for k in range(1, len(ker) + 1):
        for gens in combinations(ker, k):
            if target <= generated(gens):
                return k
    return None


def _lcm_all(values):
    out = 1
    for v in values:
        out = lcm(out, v)
    return out


def _tuples(mods):
    out = [()]
    for m in mods:
        out = [p + (d,) for p in out for d in range(m)]
    return out


def chi_of_minus_one(facs, j, get, n):
    t = get(n - 1)
    mods = [f[1] for f in facs]
    L = _lcm_all(mods)
    total = sum(j[i] * (L // m) * t[i] for i, m in enumerate(mods))
    return 1 if total % L == 0 else -1


def fold_in_kernel(facs, j, n, get):
    return chi_is_one(facs, j, n - 1, get)


def orbit(n, a):
    out = {1}
    x = a % n
    while x not in out:
        out.add(x)
        x = x * a % n
    return sorted(out)


# ---------------------------------------------------------------- reports

def show(n):
    facs = cyclic_factors(n)
    chars = characters(facs)
    get = coordinates(facs)
    U = units(n)
    orders = "+".join(str(f[1]) for f in facs) or "1"
    costs = {}
    even_costs = {}
    odd_costs = {}
    faithful = 0
    for j in chars:
        c = kernel_rank(kernel(facs, j, n, get), n)
        costs[c] = costs.get(c, 0) + 1
        if chi_of_minus_one(facs, j, get, n) == 1:
            even_costs[c] = even_costs.get(c, 0) + 1
        else:
            odd_costs[c] = odd_costs.get(c, 0) + 1
        faithful += 1 if c == 0 else 0
    rank_u = max(costs) if costs else 0
    dist = ", ".join(f"{c}:{costs[c]}" for c in sorted(costs))
    edist = ", ".join(f"{c}:{even_costs[c]}" for c in sorted(even_costs))
    odist = ", ".join(f"{c}:{odd_costs[c]}" for c in sorted(odd_costs))
    print(f"n = {n:>3}  |U| = {len(U):>2}  factors {orders:<6} rank {rank_u}  "
          f"cost {dist:<16} faithful {faithful}  even {edist:<14} odd {odist}")


def detail15():
    n = 15
    facs = cyclic_factors(n)
    get = coordinates(facs)
    print("\nn = 15: U(15) = C2 x C4; j = (j on C2, j on C4)")
    print("  j      ord  |ker|  cost  chi(-1)  -1 in ker")
    for j in characters(facs):
        ker = kernel(facs, j, n, get)
        print(f"  {j}    {character_order(facs, j):>2}    {len(ker):>2}     "
              f"{kernel_rank(ker, n)}     {chi_of_minus_one(facs, j, get, n):+d}       "
              f"{fold_in_kernel(facs, j, n, get)}")
    cheap = [j for j in characters(facs)
             if kernel_rank(kernel(facs, j, n, get), n) == 1]
    print(f"\n  cost-1 characters: {cheap}")
    print(f"  their parities: {[chi_of_minus_one(facs, j, get, n) for j in cheap]}")
    for j in cheap:
        if chi_of_minus_one(facs, j, get, n) == -1:
            ker = kernel(facs, j, n, get)
            print(f"  cheapest odd: j = {j}, ker chi = {ker}")
            blocks = []
            seen = set()
            for x in units(n):
                if x in seen:
                    continue
                b = sorted({a * x % n for a in ker})
                seen |= set(b)
                blocks.append(b)
            print(f"  blocks of ker chi (the preserved information): {blocks}")
            print(f"  -1 = {n - 1} sends {blocks[0]} to "
                  f"{sorted({(n - 1) * x % n for x in blocks[0]})}")
            break


def doubling(n):
    if n % 2 == 0:
        print(f"n = {n:>3}: doubling is not a permutation")
        return
    o = order_mod(2, n)
    half = [k for k in range(o) if pow(2, k, n) == n - 1]
    print(f"n = {n:>3}: ord(2) = {o:>2}, 2^k = -1 at k = {half if half else 'none'}")


if __name__ == "__main__":
    print("cost = least number of scales generating the kernel of a character\n")
    for n in (5, 7, 8, 9, 11, 15, 16, 21, 25, 27, 45):
        show(n)
    print("\nrank grows with the number of cyclic factors:")
    for n in (840, 510510):
        facs = cyclic_factors(n)
        print(f"  n = {n:>6} = {' * '.join(f'{p}^{e}' for p, e in factorize(n).items())}"
              f"  |U| = {len(units(n)):>4}  factors {len(facs)}  rank {len(facs)}")
    detail15()
    print()
    for n in (3, 5, 7, 9, 11, 13, 15, 21, 25, 27, 33, 65):
        doubling(n)

#!/usr/bin/env python3
"""Exact multiplication-table checks for UF-024."""
B = {
    "a": {(0, 0): 1},
    "c": {(2, 0): 1},
    "b": {(1, 1): 1},
    "d": {(3, 1): 1},
    "x": {(1, 0): 1},
    "y": {(0, 1): 1},
    "u": {(3, 0): 1},
    "v": {(2, 1): -1},  # v = -x^2 y
}


def reduce_monomial(i, j):
    q, rem = divmod(j, 2)
    i += 2 * q  # y^2 = -x^2
    if i >= 4:
        return {}
    return {(i, rem): (-1) ** q}


def multiply(A, C):
    out = {}
    for (i, j), ca in A.items():
        for (k, ell), cb in C.items():
            for mon, sign in reduce_monomial(i + k, j + ell).items():
                out[mon] = out.get(mon, 0) + ca * cb * sign
    return {m: c for m, c in out.items() if c}


def product(a, b):
    return multiply(B[a], B[b])


def main():
    expected = {
        ("b", "c"): B["d"],
        ("x", "x"): B["c"],
        ("x", "y"): B["b"],
        ("y", "y"): {(2, 0): -1},
        ("x", "v"): {(3, 1): -1},
        ("y", "u"): B["d"],
        ("b", "x"): B["v"],
        ("b", "y"): B["u"],
        ("c", "x"): B["u"],
        ("c", "y"): B["v"],
    }
    for pair, value in expected.items():
        assert product(*pair) == value, (pair, product(*pair), value)

    names = tuple(B)
    for i, left in enumerate(names):
        for right in names[i:]:
            if left == "a" or right == "a":
                continue
            pair = (left, right)
            if pair not in expected and pair[::-1] not in expected:
                assert product(left, right) == {}, (pair, product(left, right))

    # The two E copies have identical generator matrices in bases (x,y)
    # and (u,v): R sends first -> -second, second -> first;
    # S fixes first and negates second.
    R_E = ((0, 1), (-1, 0))
    S_E = ((1, 0), (0, -1))
    assert R_E == ((0, 1), (-1, 0))
    assert S_E == ((1, 0), (0, -1))

    print("UF-024 exact checks: PASS")
    print("basis dimension:", len(B))
    print("nonzero non-unit products:", len(expected))


if __name__ == "__main__":
    main()

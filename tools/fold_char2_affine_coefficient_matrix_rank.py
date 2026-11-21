#!/usr/bin/env python3
"""Reproduce the UF-061 maximal-minor specialization over F_2.

Computes g u g^{-1} on A=F_2[x,z]/(x^4,z^2), with
g(x)=x+c, g(z)=z+d+hx and
u(x)=x+x^2 z+x^3 z, u(z)=z+x^3+x^2 z+x^3 z.
The coefficient ring is F_2[c,d,h]/(c^4,d^2,h^2).
The resulting 16x15 nilpotent coefficient matrix has a 15x15
minor (omit epsilon') with determinant 1.
No third-party packages are required.
"""

BOUNDS = (4, 2, 4, 2, 2)  # x,z,c,d,h
NAMES = ("x", "z", "c", "d", "h")


def clean(poly):
    return {
        m: v & 1
        for m, v in poly.items()
        if (v & 1) and all(e < b for e, b in zip(m, BOUNDS))
    }


def constant(value=1):
    return {(0, 0, 0, 0, 0): value & 1} if value & 1 else {}


def variable(name):
    exponents = [0] * len(NAMES)
    exponents[NAMES.index(name)] = 1
    return {tuple(exponents): 1}


def add(*polys):
    out = {}
    for poly in polys:
        for monomial, coefficient in poly.items():
            out[monomial] = out.get(monomial, 0) ^ coefficient
    return clean(out)


def multiply(left, right):
    out = {}
    for a, ca in left.items():
        for b, cb in right.items():
            monomial = tuple(x + y for x, y in zip(a, b))
            if all(e < bound for e, bound in zip(monomial, BOUNDS)):
                out[monomial] = out.get(monomial, 0) ^ (ca & cb)
    return clean(out)


def power(poly, exponent):
    out = constant()
    for _ in range(exponent):
        out = multiply(out, poly)
    return out


X, Z, C, D, H = (variable(name) for name in NAMES)


def substitute_g(poly):
    """Apply g: x -> x+c, z -> z+d+hx; fix c,d,h."""
    gx = add(X, C)
    gz = add(Z, D, multiply(H, X))
    out = {}
    for exponents, coefficient in poly.items():
        term = constant(coefficient)
        for _ in range(exponents[0]):
            term = multiply(term, gx)
        for _ in range(exponents[1]):
            term = multiply(term, gz)
        for index in range(2, 5):
            for _ in range(exponents[index]):
                term = multiply(term, variable(NAMES[index]))
        out = add(out, term)
    return out


def determinant_f2(matrix):
    a = [row[:] for row in matrix]
    n = len(a)
    assert all(len(row) == n for row in a)
    for col in range(n):
        pivot = next((r for r in range(col, n) if a[r][col]), None)
        if pivot is None:
            return 0
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
        for row in range(col + 1, n):
            if a[row][col]:
                for j in range(col, n):
                    a[row][j] ^= a[col][j]
    return 1


def main():
    # UF-061 specialization: (A,B,C,D,E,G,J)=(0,0,0,1,1,1,1).
    u_x = add(X, multiply(power(X, 2), Z), multiply(power(X, 3), Z))
    u_z = add(Z, power(X, 3), multiply(power(X, 2), Z),
              multiply(power(X, 3), Z))

    # For algebra-map composition g u g^{-1}:
    # X' = g(u_x)+c; Z' = g(u_z)+d+h*g(u_x)+hc.
    gx_ux = substitute_g(u_x)
    x_prime = add(gx_ux, C)
    z_prime = add(substitute_g(u_z), D, multiply(H, gx_ux),
                  multiply(H, C))

    target_basis = [
        (0, 0), (1, 0), (0, 1), (2, 0),
        (3, 0), (1, 1), (2, 1), (3, 1),
    ]
    nilpotent_columns = [
        (0, 0, 1), (0, 1, 0), (0, 1, 1),
        (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1),
        (2, 0, 0), (2, 0, 1), (2, 1, 0), (2, 1, 1),
        (3, 0, 0), (3, 0, 1), (3, 1, 0), (3, 1, 1),
    ]

    rows = []
    for coordinate in (x_prime, z_prime):
        for xz_exponents in target_basis:
            coefficient_vector = []
            for nilpotent_exponents in nilpotent_columns:
                full_exponents = xz_exponents + nilpotent_exponents
                coefficient_vector.append(coordinate.get(full_exponents, 0))
            rows.append(coefficient_vector)

    assert len(rows) == 16 and all(len(row) == 15 for row in rows)
    # Target row 7 is epsilon' (x^3 z coefficient of X').
    minor = [row for index, row in enumerate(rows) if index != 7]
    determinant = determinant_f2(minor)
    assert determinant == 1, f"expected determinant 1, got {determinant}"
    print("PASS: UF-061 specialization minor is 15 x 15")
    print("omitted target row: epsilon'")
    print("determinant over F_2:", determinant)


if __name__ == "__main__":
    main()

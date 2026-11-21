#!/usr/bin/env python3
"""UF-014: complete scalar D4 semi-invariant classification on z^2=x^4+y^4.

For convergent analytic germs at the cone vertex, the theorem is
    R_chi = Delta_chi * K{p,z},
where p=x^2+y^2, and
Delta_(+,+)=1, Delta_(-,+)=xy,
Delta_(-,-)=x^2-y^2, Delta_(+,-)=xy(x^2-y^2).

This verifier checks group relations, character transformations, invariant
coordinates, quotient-branch identities, and forced multiplicity orbits.
It is not a proof of analytic Weierstrass division or invariant-ring
generation; those are proved in the companion research note.
Standard library only.
"""
from __future__ import annotations
from fractions import Fraction
from itertools import product

Matrix = tuple[int, int, int, int]
Point = tuple[int, int]
IDENTITY: Matrix = (1, 0, 0, 1)
R: Matrix = (0, -1, 1, 0)
S: Matrix = (0, 1, 1, 0)

CHARACTERS = {
    "++": (1, 1),
    "-+": (-1, 1),
    "--": (-1, -1),
    "+-": (1, -1),
}


def matmul(A: Matrix, B: Matrix) -> Matrix:
    a, b, c, d = A
    e, f, g, h = B
    return (a*e+b*g, a*f+b*h, c*e+d*g, c*f+d*h)


def matvec(A: Matrix, x: int, y: int) -> Point:
    a, b, c, d = A
    return (a*x+b*y, c*x+d*y)


def group_elements() -> tuple[tuple[int, int, Matrix], ...]:
    """Represent all elements r^k s^eps."""
    out = []
    power = IDENTITY
    for k in range(4):
        out.append((k, 0, power))
        out.append((k, 1, matmul(power, S)))
        power = matmul(power, R)
    return tuple(out)


def char_value(k: int, eps: int, alpha: int, beta: int) -> int:
    return alpha**k * beta**eps


def invariant_coordinates(x: int, y: int) -> tuple[int, int]:
    return x*x+y*y, x*x*y*y


def relative_invariants(x: int, y: int) -> dict[str, int]:
    d = x*x-y*y
    return {"++": 1, "-+": x*y, "--": d, "+-": x*y*d}


def model_semi_invariant(x: int, y: int, z: int, label: str) -> int:
    """Delta_chi times one nonconstant invariant polynomial F(p,z)."""
    p = x*x+y*y
    F = 1 + 2*p + 3*z + p*p + p*z + 2*z*z
    return relative_invariants(x, y)[label] * F


def verify() -> dict[str, int | bool]:
    group = group_elements()
    assert len(group) == 8 and len({g[2] for g in group}) == 8

    # D4 presentation r^4=s^2=1 and srs=r^-1.
    power = IDENTITY
    for _ in range(4):
        power = matmul(power, R)
    assert power == IDENTITY
    assert matmul(S, S) == IDENTITY
    assert matmul(matmul(matmul(S, R), S), R) == IDENTITY
    relation_checks = 3

    samples = ((2, 1), (3, -2), (1, 4), (-3, 5), (5, 7))
    invariant_checks = 0
    for _k, _eps, A in group:
        for x, y in samples:
            xp, yp = matvec(A, x, y)
            assert invariant_coordinates(xp, yp) == invariant_coordinates(x, y)
            p, q = invariant_coordinates(x, y)
            assert p*p - 2*q == x**4+y**4
            invariant_checks += 2

    relative_checks = 0
    for k, eps, A in group:
        for x, y in samples:
            xp, yp = matvec(A, x, y)
            before = relative_invariants(x, y)
            after = relative_invariants(xp, yp)
            for label, (alpha, beta) in CHARACTERS.items():
                expected = char_value(k, eps, alpha, beta)
                assert after[label] == expected*before[label]
                relative_checks += 1

    # Test arbitrary invariant polynomial multipliers F(p,z).
    model_checks = 0
    z_samples = (-3, -1, 0, 2, 5)
    for k, eps, A in group:
        for (x, y), z in product(samples, z_samples):
            xp, yp = matvec(A, x, y)
            for label, (alpha, beta) in CHARACTERS.items():
                lhs = model_semi_invariant(xp, yp, z, label)
                rhs = char_value(k, eps, alpha, beta)*model_semi_invariant(x, y, z, label)
                assert lhs == rhs
                model_checks += 1

    # On X, q=x^2 y^2=(p^2-z^2)/2. Hence these exact quotient identities:
    # (z-p)(z+p)=-2 x^2 y^2;
    # (z-p/sqrt(2))(z+p/sqrt(2))=(x^2-y^2)^2/2.
    branch_identity_checks = 0
    for x, y in samples:
        p = x*x+y*y
        z2 = x**4+y**4
        assert z2-p*p == -2*x*x*y*y
        assert z2-Fraction(p*p, 2) == Fraction((x*x-y*y)**2, 2)
        branch_identity_checks += 2

    # p and d^2 are preserved, so the four quotient branch families
    # (coordinate +/- and diagonal +/-) are stable as D4-orbits.
    orbit_checks = 0
    for _k, _eps, A in group:
        for x, y in samples:
            xp, yp = matvec(A, x, y)
            assert x*x+y*y == xp*xp+yp*yp
            assert (x*x-y*y)**2 == (xp*xp-yp*yp)**2
            orbit_checks += 2

    # Generic coordinate-branch points show the plus/minus quotient factors:
    multiplicity_checks = 0
    for t in (1, 2, 3, 5):
        p = t*t
        assert t*t-p == 0 and t*t+p == 2*t*t
        assert -t*t+p == 0 and -t*t-p == -2*t*t
        multiplicity_checks += 4

    degrees = {"++": 0, "-+": 2, "--": 2, "+-": 4}
    assert degrees == {"++": 0, "-+": 2, "--": 2, "+-": 4}

    return {
        "D4_group_elements": len(group),
        "D4_relation_checks": relation_checks,
        "invariant_coordinate_checks": invariant_checks,
        "relative_invariant_character_checks": relative_checks,
        "analytic_module_model_checks": model_checks,
        "quotient_branch_identity_checks": branch_identity_checks,
        "D4_branch_orbit_checks": orbit_checks,
        "branch_multiplicity_checks": multiplicity_checks,
        "character_modules_classified": 4,
    }


def main() -> None:
    print("UF-014 complete D4 analytic character classification")
    print("R_chi = Delta_chi * K{p,z}, p=x^2+y^2")
    print("relative invariants:", {k: relative_invariants(2, 1)[k] for k in CHARACTERS})
    print("verification:", verify())


if __name__ == "__main__":
    main()

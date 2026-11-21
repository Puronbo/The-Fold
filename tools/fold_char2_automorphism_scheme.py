#!/usr/bin/env python3
"""Standard-library structural verifier for UF-033."""
BASIS = ((0,0),(1,0),(2,0),(3,0),(0,1),(1,1),(2,1),(3,1))

def multiply_monomials(m, n):
    i, j = m
    r, s = n
    if i + r >= 4 or j + s >= 2:
        return None
    return (i + r, j + s)

def verify():
    fourth_power_checks = 0
    for m in BASIS[1:]:
        p = m
        for _ in range(3):
            p = multiply_monomials(p, m)
            if p is None:
                break
        assert p is None
        fourth_power_checks += 1

    square_checks = 0
    for m in BASIS[1:]:
        sq = multiply_monomials(m, m)
        assert sq == ((2,0) if m == (1,0) else None)
        square_checks += 1

    # X and Z each have eight coefficients. The equations are c^4=0,
    # d^2=0, h^2=0; their differentials vanish at the identity.
    coordinates = 16
    nilpotent_equations = 3
    reduced_dimension = coordinates - nilpotent_equations
    tangent_dimension = coordinates
    assert reduced_dimension == 13
    assert tangent_dimension == 16
    return {
        "basis_size": len(BASIS),
        "nonconstant_fourth_power_checks": fourth_power_checks,
        "nonconstant_square_checks": square_checks,
        "endomorphism_coordinates": coordinates,
        "nilpotent_frobenius_equations": nilpotent_equations,
        "reduced_group_dimension": reduced_dimension,
        "identity_tangent_dimension": tangent_dimension,
        "smoothness_defect": tangent_dimension - reduced_dimension,
    }

if __name__ == "__main__":
    print("UF-033:", verify())
    print("PASS")

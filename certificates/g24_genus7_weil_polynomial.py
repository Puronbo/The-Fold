#!/usr/bin/env python3
"""Exact point counts and Weil polynomial for the genus-7 octic curve.

The affine model is the length-three Artin-Schreier-Witt tower
  u^2+u=s,
  w^2+w=u^3+u,
  v^2+v=u^7+u^4+u^3*w^2+u^3*w+u^2*w^2+u^2*w+w^3+w^2.
There is one rational point above infinity.  All arithmetic below is
exact in GF(2^m), represented by binary polynomials.
"""
from fractions import Fraction

# Irreducible binary polynomials, including their leading term.
MODULI = {
    1: 0b11, 2: 0b111, 3: 0b1011, 4: 0b10011, 5: 0b100101,
    6: 0b1000011, 7: 0b10000011, 8: 0x11D, 9: 0x211, 10: 0x409,
}


def mul_factory(m):
    q, mod = 1 << m, MODULI[m]

    def mul(a, b):
        out = 0
        while b:
            if b & 1:
                out ^= a
            b >>= 1
            a <<= 1
            if a & q:
                a ^= mod
        return out

    return mul


def point_count(m):
    q = 1 << m
    mul = mul_factory(m)
    square = [mul(x, x) for x in range(q)]
    # Roots[z^2+z = c].  Each nonempty fiber has exactly two elements.
    roots = {}
    for z in range(q):
        roots.setdefault(square[z] ^ z, []).append(z)

    affine = 0
    for u in range(q):
        u2 = square[u]
        u3 = mul(u2, u)
        u4 = square[u2]
        u7 = mul(mul(u4, u2), u)
        for w in roots.get(u3 ^ u, ()):
            w2 = square[w]
            rhs_v = (
                u7 ^ u4 ^ mul(u3, w2) ^ mul(u3, w)
                ^ mul(u2, w2) ^ mul(u2, w) ^ mul(w2, w) ^ w2
            )
            affine += len(roots.get(rhs_v, ()))
    return affine + 1  # unique totally ramified point above infinity


def main():
    counts = {m: point_count(m) for m in range(1, 11)}
    expected = {1: 9, 2: 9, 3: 9, 4: 9, 5: 49,
                6: 105, 7: 121, 8: 177, 9: 513, 10: 1009}
    assert counts == expected, (counts, expected)

    genus = 7
    power_sums = {m: (1 << m) + 1 - counts[m] for m in range(1, genus + 1)}
    # Newton identities: P(T)=sum c_k T^k, c_0=1.
    c = [Fraction(1)]
    for k in range(1, genus + 1):
        c_k = -sum(c[k-i] * power_sums[i] for i in range(1, k+1)) / k
        assert c_k.denominator == 1
        c.append(c_k)

    # Weil functional equation supplies the remaining coefficients.
    coeff = [0] * (2 * genus + 1)
    for k in range(genus + 1):
        coeff[k] = int(c[k])
    for k in range(genus):
        coeff[2*genus-k] = (2 ** (genus-k)) * coeff[k]

    expected_coeff = [1, 6, 20, 48, 90, 140, 196, 272,
                      392, 560, 720, 768, 640, 384, 128]
    assert coeff == expected_coeff, (coeff, expected_coeff)

    # Independent checks: point counts beyond genus agree with the
    # power sums predicted by the completed Weil polynomial.
    predicted = dict(power_sums)
    for m in range(genus + 1, 11):
        p_m = -sum(coeff[k] * predicted[m-k]
                   for k in range(1, m)) - m * coeff[m]
        predicted[m] = p_m
        assert (1 << m) + 1 - p_m == counts[m]

    print("m : #C(F_{2^m})")
    for m, n in counts.items():
        print(f"{m:2d}: {n}")
    print("Weil polynomial coefficients, low degree first:")
    print(coeff)


if __name__ == "__main__":
    main()

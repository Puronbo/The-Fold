# G-EP8 — exact polynomial factorization over prime fields

## Result

The spectral engine now factors every nonzero polynomial over a prime field into monic irreducibles with multiplicities. The implementation uses only the Python standard library and exact arithmetic.

For a characteristic polynomial, the automatic fingerprint now includes a complete factorization over F_p. Factors are reported in ascending degree order, with descending coefficient arrays and positive multiplicities. Because characteristic polynomials are monic, no leading-unit entry is expected in this use case.

## Algorithm

1. **Squarefree decomposition.** Compute the formal derivative and polynomial gcds over F_p. Separate squarefree layers by multiplicity. When the derivative vanishes in characteristic p, extract the p-th root (all nonzero exponents are divisible by p) and multiply the recovered multiplicities by p. This handles inseparable repeated powers such as (x²+x+1)² over F_2.
2. **Berlekamp factorization.** For a squarefree monic polynomial f of degree n, form the matrix of the Frobenius map Q: g ↦ g^p mod f on the basis 1,x,…,x^(n−1). The nullspace of Q−I is the Berlekamp algebra. Its basis elements, combined with gcd splits against g−a for a in F_p, separate f into irreducible factors.
3. **Verification by reconstruction.** The factor list should multiply back to the monic input polynomial, with each factor raised to its reported multiplicity. Tests cover irreducible and split quadratics, repeated linear factors, and a repeated irreducible factor in characteristic two.

All polynomial coefficient arithmetic is reduced modulo p. No floating-point arithmetic or external symbolic algebra dependency is used.

## Scope

This milestone completes factorization over the base prime field. It does not yet adjoin roots of irreducible factors of degree greater than one. Such roots live in finite extensions F_(p^d). The next milestone should implement quotient-field arithmetic, irreducibility validation, and matrix/Jordan computations over those extensions.

## Complexity

Berlekamp's method is deterministic, but this straightforward implementation is intended as a transparent reference algorithm for modest polynomial degrees. It is not optimized for very large matrices or degrees. The characteristic-polynomial determinant stage remains exponential in matrix dimension; polynomial factorization is a separate stage.

## Tests and status

The added tests exercise:
- x²+1 irreducible over F_3;
- x²+1 split over F_5;
- (x+1)² over F_2;
- (x²+x+1)² over F_2;
- automatic spectral output carrying the full base-field factorization.

The tests are authored and committed, but the repository test suite and CI have not been run in this environment. The algorithm and implementation should be treated as a committed research implementation pending execution of those tests and independent property-based reconstruction checks.

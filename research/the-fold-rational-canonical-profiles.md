# G-EP21 — rational canonical profiles from primary kernel growth

For a linear operator A over F_p, its characteristic polynomial alone does not determine its similarity class. The rational canonical form is determined by a divisibility chain of invariant factors, equivalently by the elementary divisors (f^e) for monic irreducible polynomials f.

For each irreducible factor f of the characteristic polynomial, consider the F_p-linear operator f(A). If d=deg(f), then
[
\dim_{F_p}\ker(f(A)^k)/d
]
is the sum of min(k,e) over the elementary-divisor exponents e belonging to f. Consequently the first differences count primary blocks of size at least k, and second differences recover the exact multiplicity of each exponent.

The implementation computes f(A) by exact matrix-polynomial evaluation, obtains ranks over F_p, and divides nullities by deg(f). It then sorts each irreducible's elementary-divisor exponents and right-aligns them. Multiplying corresponding powers of the irreducible factors produces the invariant factors (d_1|d_2|\cdots|d_r).

## Implementation

- `tools/rational_canonical.py`: `rational_canonical_profile(matrix, p)`.
- `tests/test_rational_canonical.py`: identity, irreducible cyclic companion, mixed nilpotent blocks, similarity, and invalid-input tests.

The output includes the characteristic polynomial, primary nullity sequences, elementary-divisor exponents, and invariant factors. It reports a complete similarity-class descriptor for the supplied matrix over the supplied prime field.

## Scope and limitations

This is an exact finite-field classification, not a real/complex numerical canonical-form routine. It uses dense matrix arithmetic and modular rank; computational cost grows quickly with dimension and primary exponents. The result is prime-dependent: the same integer matrix can have different rational canonical forms after reduction modulo different primes.

A canonical-form fingerprint is mathematically complete for similarity over the stated finite field. It does not by itself imply that two neural-network layers are functionally interchangeable: their input/output coordinate roles, surrounding layers, nonlinearities, quantization, and execution context still matter.

# G-EP7 — exact characteristic polynomials and automatic base-field spectra

## Result

For an integer matrix A and prime p, the engine now computes
χ_A(x)=det(xI−A) in F_p[x] without division, scans every λ in F_p, and constructs the Jordan profile for each root.

The returned coefficient list is in descending degree order. Each base-field root is accompanied by its algebraic multiplicity, recovered by repeated synthetic division, and its Jordan profile from G-EP5/G-EP6.

## Why the determinant algorithm matters

The implementation uses a subset dynamic program for the Leibniz determinant. At row k, a state indexed by a k-element set of columns stores the signed polynomial sum over assignments of the first k rows to those columns. Appending column j contributes the entry xδ_kj−a_kj, with sign determined by the number of previously selected columns larger than j.

This computes the determinant in F_p[x] using only addition and multiplication. It avoids division by k, so it remains valid when the characteristic divides the matrix dimension — a case where a naive Faddeev–LeVerrier implementation can fail.

The cost is exponential in matrix dimension. This is an exact reference implementation for small matrices, not a large-scale characteristic-polynomial algorithm.

## Automatic scan

The CLI exposes this mode with `--auto`, for example:

~~~sh
python tools/spectral_fingerprint.py --prime 2 --matrix-json '[[0,1],[1,0]]' --auto
~~~

The previous `--eigenvalues` mode remains available for explicitly supplied roots. The two modes are mutually exclusive.

For each of the p field elements, the implementation computes the multiplicity of x−λ in the characteristic polynomial. For every root it invokes the existing exact kernel-growth routine to recover the Jordan block sizes.

The output explicitly marks irreducible_factorization_complete as false. A scan of F_p finds all base-field eigenvalues, but it does not factor the remaining polynomial into irreducibles of degree greater than one and does not construct splitting fields.

## Checks and examples

- For the quarter-turn matrix [[0,1],[1,0]] over F_2, the characteristic polynomial is x²+1=(x+1)². The scan finds λ=1 with algebraic multiplicity 2, and the Jordan engine finds one block of size 2.
- For [[0,2],[1,0]] over F_3, the characteristic polynomial is x²+1, irreducible over F_3. The base-field scan correctly returns no eigenvalues.

The determinant recurrence was independently cross-checked by evaluating its output at every field element and comparing with a permutation-expansion determinant for 6,800 random matrix/field evaluations (dimensions 1–4, primes 2, 3, 5, and 7). This is an independent algorithm check, not a claim that the repository's unittest suite or CI has run.

## Boundary and next layer

G-EP7 is complete for exact characteristic polynomials and eigenvalues in the base prime field. It is not a full finite-field spectral factorization.

G-EP8 should add polynomial factorization over F_p, ideally with an optional, isolated backend first, then exact finite-extension arithmetic and root/Jordan profiles over F_{p^d}. It must preserve the distinction between base-field eigenvalues and eigenvalues that exist only in an extension.

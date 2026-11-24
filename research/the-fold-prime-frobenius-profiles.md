# G-EP17 — prime-indexed Frobenius-orbit spectral profiles

## Definition

For an integer matrix (A) and a prime (p), factor its characteristic polynomial over (mathbb F_p):
[
\chi_{A,p}(x)=\prod_i q_i(x)^{e_i},
]
where the (q_i) are distinct monic irreducibles. Each (q_i) of degree (d_i) represents a Frobenius orbit of (d_i) conjugate eigenvalues. G-EP17 records, for each prime:

- modular rank of (A);
- characteristic polynomial;
- irreducible orbit classes (polynomial, degree, multiplicity);
- orbit-degree histogram, weighted by the number of represented roots including algebraic multiplicity.

The histogram satisfies the exact dimension check
[
\sum_d d\,N_d=\dim A,
]
where (N_d) is the total represented-root count contributed by degree-(d) factors. Jordan fingerprints remain available from G-EP10 but are not collapsed into the orbit histogram.

## Controlled same-rank example

Take
[
I_2=\begin{pmatrix}1&0\\0&1\end{pmatrix},\qquad
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
]
Both have rank two modulo every prime. Their characteristic polynomials are ((x-1)^2) and (x^2+1), respectively. The latter is irreducible over (mathbb F_3) and (mathbb F_7), but splits over (mathbb F_5). Thus:

| Prime | Identity orbit histogram | Quarter-turn orbit histogram |
|---|---:|---:|
| 3 | degree 1: 2 roots | degree 2: 2 conjugate roots |
| 5 | degree 1: 2 roots | degree 1: 2 roots |
| 7 | degree 1: 2 roots | degree 2: 2 conjugate roots |

This proves that the orbit profile can distinguish some equal-rank matrices, and that the distinction can depend on the prime. It does not prove that this signature is useful for neural-network analysis.

## Implementation

`tools/prime_spectral_profile.py` exposes `prime_spectral_profile(matrix, primes)` and `compare_prime_profiles(matrices, primes)`. It reuses the exact characteristic-polynomial factorization and extension-profile routines from G-EP7–G-EP10. The comparison reports rank equality separately from Frobenius-profile equality.

Run:
```bash
python -m unittest tests.test_prime_spectral_profile -v
```

## Limits and next experiment

These profiles are exact invariants of the reduced matrix over each selected prime. They are not invariants of arbitrary real-valued model weights: quantization, scale, and prime can change them. Equal characteristic factorization does not determine Jordan structure for general matrices; use the separate Jordan profiles. No trained checkpoint or predictive benchmark is involved here.

A useful empirical follow-up is to compare the profile against rank-only and ordinary real/complex spectral summaries on actual checkpoints, and test whether it adds stable information after controlling for quantization scale and prime choice.

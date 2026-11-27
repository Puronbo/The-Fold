# Unified prime memory field: path, arithmetic, and alignment

**Status:** finite-data computational representation. The three layers are deliberately separate; this construction does not assert a new law of prime distribution.

## 1. Geometric path

For prime index n, embed the index on the chosen spiral

\[
z_n=n e^{in\omega}=n\cos(n\omega)+i\,n\sin(n\omega).
\]

The implementation records index, prime label, radius, angle, and Cartesian coordinates. This is an index-based visualization; the prime value labels the point but does not determine its radius.

## 2. Arithmetic path and afterimage

The arithmetic layer reuses the prime-sensitive path record h_n=(n,p_n,g_n,(p_n mod m_j)_j,sigma_A(p_n)), where g_n is the difference from the previous supplied prime and sigma_A is optional and matrix-dependent. Its feature afterimage uses the exact rational update

\[
M_n^{arith}=\lambda M_{n-1}^{arith}+\phi(h_n).
\]

This layer retains the supplied ordered records separately from its generally lossy feature summary.

## 3. Alignment field

For each pair of indices i<j, the geometric recurrence predicate requires both angular and relative radial proximity. Arithmetic recurrence predicates are evaluated independently: gap, selected residues, and optional complete spectral profiles.

The alignment field records pair events where geometric recurrence co-occurs with at least one arithmetic recurrence. It also retains separate channels for each type of co-occurrence. If e_k^(c) in {0,1} is the event indicator for channel c, the pair-ordered alignment afterimage is

\[
M_k^{(c)}=\lambda M_{k-1}^{(c)}+e_k^{(c)},\qquad M_0^{(c)}=0,
\]

where k enumerates index pairs in lexicographic order. Thus this memory fades across pair events, not across prime-index steps. Raw channel totals and fading memory are both returned because they answer different questions.

## Executable interface

`tools/prime_memory_field.py` exposes `prime_memory_field`. It composes the geometric embedding, the arithmetic afterimage, the pairwise recurrence comparison, and the cyclic-shift alignment control. All decay updates use rational fractions. Geometric coordinates and angular distances are floating-point quantities because they depend on trigonometric functions.

The output is separated into `geometry`, `arithmetic`, `alignment`, and `controls`. No combined scalar score is defined: adding geometric distances, prime gaps, residue matches, and spectral features would require an explicit normalization and weighting convention.

## Example interpretation

With supplied primes 3,5,7,11, omega=0, moduli 2,3, angular tolerance zero, radial tolerance one, and gap tolerance zero, all six pairs pass the geometric criterion. Only one pair has equal supplied-entry gaps (the two gaps of size 2), and only one pair has equal residues modulo both 2 and 3 (labels 5 and 11). These are two distinct alignment events. Under lambda=1/2, the gap-alignment event is followed by two nonmatching pair events, leaving alignment memory 1/4.

This example is a deterministic check of definitions and ordering, not evidence that the prime sequence has a hidden spiral law.

## Limits and controls

The cyclic-shift control rotates arithmetic records against fixed geometric indices. It is a finite alignment diagnostic, not an independent randomization test or p-value. The spectral channel is conditional on the supplied matrix and on complete finite-field factorization profiles. The model does not establish periodicity, predict primes, prove the prime number theorem or the Riemann hypothesis, or show that a chosen spiral encoding is intrinsic.

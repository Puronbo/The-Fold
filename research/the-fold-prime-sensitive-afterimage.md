# Prime-sensitive afterimage: gaps, residues, and spectral memory

**Status:** exact finite computation under explicit inputs. This is a memory representation and an analysis tool, not a claimed law of prime distribution.

## Path record

Given a strictly increasing list of primes \(p_1,\ldots,p_N\), residue moduli \(m_1,\ldots,m_k\), and optionally a square integer matrix \(A\), the path record at index \(n\) is

\[
h_n=\left(n,p_n,\ p_n-p_{n-1},\
(p_n\bmod m_j)_{j=1}^k,\ \sigma_A(p_n)\right).
\]

The first gap is null. The residue signature is explicit and depends on the selected moduli. The optional spectral fingerprint \(\sigma_A(p_n)\) is the existing exact finite-field Frobenius profile of \(A\) reduced modulo \(p_n\). It depends on the matrix and reduction convention; it is not an intrinsic attribute of the prime.

## Exact afterimage update

Each record emits integer-valued feature channels \(\phi(h_n)\). For a rational decay factor \(0\le\lambda\le1\), update

\[
M_n=\lambda M_{n-1}+\phi(h_n),\qquad M_0=0.
\]

Equivalently,

\[
M_N=\sum_{n=1}^N\lambda^{N-n}\phi(h_n).
\]

The implementation uses Python Fraction, so the reported numerator/denominator pairs are exact. At \(\lambda=0\), only the latest record remains; at \(\lambda=1\), all feature emissions accumulate without fading. Intermediate values give exponentially fading memory.

The ordered path is lossless for the listed fields. The afterimage is generally lossy: different histories can produce the same aggregate feature vector. It must not be mistaken for a reversible encoding of the path.

## Executable interface

The module tools/prime_memory_afterimage.py exposes prime_sensitive_memory_path. It validates primality, strict ordering, distinct moduli, and the decay range. With a matrix, it calls prime_spectral_profile once per listed prime and records modular rank, Frobenius orbit-degree histogram, and completeness flags.

Example:

\[
(p_n)=(2,3,5,7),\quad (m_j)=(2,3,5),\quad\lambda=\frac12.
\]

The gap channel is emitted as \(1,2,2\), giving

\[
M_{\rm gap}=\frac12\left(\frac12(1)+2\right)+2
=\frac{13}{4}.
\]

This is an exact check of the memory recurrence, not a statistical statement about primes.

## Reading the three layers

- **Arithmetic path:** ordered prime values, gaps, and modular residues.
- **Spectral path:** matrix-dependent finite-field profiles indexed by the same primes.
- **Afterimage:** rationally weighted aggregate of the chosen feature channels.

This creates a testable question: do patterns in a chosen spiral embedding also appear in gap, residue, or spectral channels? Compare against alternative radial/angular encodings and explicit baselines. A visual alignment alone is not evidence of an arithmetic law; any claimed regularity needs a defined statistic, controls, and reproducible tests.

## Limits

The code checks only the finite prime list supplied by the caller; it does not generate an unbounded prime sequence. It does not prove periodicity, predict future primes, or establish a relation between prime gaps and matrix spectra. Spectral channels are properties of the selected matrix after reduction modulo each prime. The afterimage is a chosen feature summary whose interpretation depends on the selected channels and decay factor.

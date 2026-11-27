# Stable prime recurrence: persistence beyond first return

**Status:** finite-sample operational definition layered on the proposed prime-spiral encoding. Stability is not asserted to be intrinsic to primes.

## Consecutive-return criterion

A first return detects one later match. To require persistence, fix a channel c, anchor index i, and integer q >= 2. A stable return is the first j for which q consecutive later indices match:

\[
E_c(i,j-q+1)=E_c(i,j-q+2)=\cdots=E_c(i,j)=1.
\]

A nonmatching intervening index resets the run. Both first-return and stable-arrival indices are retained.

## Stable-event memory

Let s_j^(c) count stable-return events arriving at index j. The afterimage is

\[
Q_j^{(c)}=\lambda Q_{j-1}^{(c)}+s_j^{(c)},\qquad Q_0^{(c)}=0.
\]

The clock advances once per later prime index. Rational decay is accumulated exactly. Raw event tables remain available because the fading summary is lossy.

## Executable interface

The module tools/prime_recurrence_stability.py exposes prime_recurrence_stability. It supports geometric, gap, residue, optional matrix-relative spectral, and geometric-arithmetic alignment channels. required_consecutive defaults to two and must be at least two.

## Limits

A run of q consecutive matches in a finite sample establishes only that this operational criterion was met in that sample. It does not prove eventual recurrence, periodicity, predict primes, or establish a new prime-distribution theorem. Results depend on the selected spiral, tolerances, residue moduli, optional matrix, and finite sample.

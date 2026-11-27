# Prime recurrence chronology: first return and arrival order

**Status:** finite-data extension of the proposed prime spiral representation. It adds a discrete event clock; it does not claim that primes have an intrinsic spiral trajectory.

## First return

For each recurrence channel c and anchor index i, define

\[
\tau_c(i)=\min\{j>i:E_c(i,j)=1\},
\]

when the set is nonempty. Here E_c is the declared Boolean recurrence predicate: geometric, gap, residue, spectral, or a named geometric-arithmetic alignment. If no later index matches, no first-return event is emitted.

The latency is \(\ell_c(i)=\tau_c(i)-i\). This is an index latency, not elapsed physical time.

## Event clock

Events are ordered by arrival index j, not by lexicographic pair enumeration. All first-return events with the same arrival index share one event-clock bucket. This preserves simultaneity in the discrete index clock.

Let e_j^(c) be the number of anchors whose first return in channel c arrives at index j. The chronological afterimage is

\[
R_j^{(c)}=\lambda R_{j-1}^{(c)}+e_j^{(c)},\qquad R_0^{(c)}=0.
\]

Unlike pair-event memory, the clock advances once per prime index, even if many pairs are tested at that index. Decay is exact rational arithmetic for lambda in Q intersect [0,1].

## Executable interface

The module tools/prime_recurrence_chronology.py exposes prime_recurrence_chronology. It returns per-anchor first returns, simultaneous arrival buckets, the index-clock memory trace, and final channel memories. It delegates pair predicates to the existing recurrence comparison module.

## Interpretation and limits

The first-return map depends on the chosen spiral angle, tolerances, residue moduli, supplied prime sample, and optional matrix. It is not a prime period, a prediction of the next prime, or evidence for an infinite recurrence theorem. A missing return in a finite sample means only that no match was observed within that sample.

The chronological memory retains arrival order and multiplicity but is generally lossy. Keep the raw first-return table if exact reconstruction is required.

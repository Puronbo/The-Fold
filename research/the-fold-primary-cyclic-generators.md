# G-EP44 — bounded elementary-divisor cyclic generators

## Construction

For a primary operator with irreducible factor (f) and elementary-divisor
exponents (e_1\ge\cdots\ge e_r), a cyclic generator (v_i) must satisfy
(f(A)^{e_i}v_i=0) and, when (e_i>1),
(f(A)^{e_i-1}v_i\ne0). Its Krylov orbit has the expected dimension
(e_i\deg f).

The implementation enumerates vectors over the finite field, tests these
annihilator conditions, and accepts an orbit only when it increases the
previously assembled span by its full expected dimension. If all requested
summands are found, the concatenated columns form an invertible basis.

## Limits

The search is exhaustive only up to `max_candidates`. A budget exhaustion
or a failed greedy choice is reported as incomplete, not as nonexistence.
This is a constructive bounded search, not a polynomial-time algorithm.
The current routine works within a single primary component; a subsequent
integration step must verify the resulting companion-block coordinates and
combine component bases into a whole-operator similarity witness.

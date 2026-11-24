# Collatz and the failure of fixed congruence quotients

## Result

Let (C:\mathbb N_{>0}\to\mathbb N_{>0}) be the Collatz map
\[
C(n)=\begin{cases}
n/2,&2\mid n,\\
3n+1,&2\nmid n.
\end{cases}
\]

For every integer (m>1), there is **no** function
\[
\overline C:\mathbb Z/m\mathbb Z\to\mathbb Z/m\mathbb Z
\]
such that
\[
\overline C([n]_m)=[C(n)]_m
\qquad(n\ge1).
\]
Equivalently, congruence modulo (m) is not a forward congruence for the Collatz map.

### Proof for even moduli

Take (n=m) and (n'=2m). Both are even and congruent modulo (m). But
\[
C(m)=m/2\not\equiv0\pmod m,
\qquad C(2m)=m\equiv0\pmod m.
\]
Thus congruent inputs can have noncongruent outputs.

### Proof for odd moduli

Take (n=2m) and (n'=3m). They are congruent modulo (m). Since (m) is odd, (2m) is even and (3m) is odd. Hence
\[
C(2m)=m\equiv0\pmod m,
\qquad C(3m)=9m+1\equiv1\pmod m.
\]
Again congruent inputs have noncongruent outputs.

The two cases exhaust all (m>1). \(\square\)

## Fold interpretation

The orbit-quotient theorem applies to a specified equivalence relation, but a quotient supports an induced deterministic operation only if the original operation respects that equivalence. The calculation above proves that the residue equivalence (n\sim_m n'\iff n\equiv n'\pmod m) fails this compatibility condition for every nontrivial modulus.

This is not a proof for or against the Collatz conjecture. It is a no-go result for one tempting finite-state reduction.

## What a viable finite model must retain

Any finite abstraction intended to model Collatz transitions must retain more than one fixed residue class. At minimum, it must address:

1. **Branch information:** parity must be determined by the state.
2. **Division information:** on the even branch, computing (n/2\pmod m) requires information about (n\pmod{2m}), not merely (n\pmod m).
3. **Scale/valuation information:** repeated divisions by two can require an unbounded amount of 2-adic information. A fixed finite residue state cannot record all such valuations exactly.
4. **A sound abstraction relation:** if several integers are merged into one abstract state, every possible concrete successor must be represented by the abstract transition. Otherwise a finite cycle in the abstraction need not correspond to a Collatz cycle.

A natural next object is therefore a branch-labelled, valuation-aware transition system, possibly over bounded 2-adic precision with an explicit “precision loss” transition. Such a system may be useful for finite verification, but a proof of global termination would require a well-founded ranking or another global argument that survives the abstraction.

## Status

- Non-descent to every fixed congruence quotient (\mathbb Z/m\mathbb Z), (m>1): **proved**.
- Non-representation by one affine homothety: **proved** in `research/the-fold-problem-applications.md`.
- A useful complete finite quotient for the full Collatz dynamics: **open**.
- Collatz conjecture: **not solved**.

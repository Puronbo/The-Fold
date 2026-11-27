# The zero-residual question: what could NP = 0 mean?

## The proposed equivalence

The research prompt is

\[
\boxed{P\ne NP\iff NP=0.}
\]

In standard complexity theory, NP is a class of decision languages, not a number. Therefore NP = 0 is not currently a well-typed mathematical statement. A zero convention must identify a numerical or set-valued object before the equivalence can be evaluated.

Earlier work in The Fold defines the usual classes and the verifier projection/solver section picture. It contains no previously established definition of NP = 0. This note does not silently retrofit one.

## 1. The canonical residual

Since \(P\subseteq NP\), define the residual class

\[
\mathcal R_{NP\mid P}:=NP\setminus P.
\]

Its elements are precisely the languages that have polynomial-time nondeterministic verification but no polynomial-time deterministic decider.

Then the exact set-theoretic statements are

\[
\boxed{P=NP\iff \mathcal R_{NP\mid P}=\varnothing}
\]

and

\[
\boxed{P\ne NP\iff \mathcal R_{NP\mid P}\ne\varnothing.}
\]

Thus, if zero means that the residual is empty, the direction is the opposite of the proposed one:

\[
\mathcal R_{NP\mid P}=0
\quad\Longleftrightarrow\quad P=NP,
\]

where zero is being used as a name for the empty set. If the residual is nonempty, that is the separation statement.

This is a characterization, not a proof that the residual is empty or nonempty.

## 2. A zero-valued indicator with a precise meaning

Define the collapse indicator

\[
C_{P,NP}:=
\begin{cases}
0,&\mathcal R_{NP\mid P}=\varnothing,\\
1,&\mathcal R_{NP\mid P}\ne\varnothing.
\end{cases}
\]

Then

\[
C_{P,NP}=0\iff P=NP,
\qquad
C_{P,NP}=1\iff P\ne NP.
\]

This makes a rigorous zero-valued object, but it does not make the standard class NP equal to zero. It is a Boolean indicator whose value is exactly the question's answer. Computing it is as hard as resolving P versus NP.

A notation such as NP-zero could be introduced for this indicator, but it must not be confused with the standard class NP.

## 3. Why a naive complexity gap is not enough

A proposed numerical gap must be invariant under reasonable machine/encoding changes and must have a proven relationship to polynomial-time decidability.

For example, comparing raw deterministic and nondeterministic running times,

\[
T_D(L,n)-T_N(L,n),
\]

does not give a canonical class invariant: machine models, simulation overheads, encodings, and the choice of algorithms affect the values. Moreover, a positive difference at finite input sizes says nothing about whether the deterministic complexity is polynomial.

Likewise, an exponent difference between two polynomial upper bounds cannot certify separation. Both sides can be polynomial while their exponents differ. A superpolynomial deterministic lower bound for some NP language would be needed to prove a genuine separation.

A valid gap proposal therefore needs:
1. a precise machine model and input encoding;
2. a minimization over all admissible algorithms, not one chosen implementation;
3. a robust asymptotic definition;
4. a theorem that zero/nonzero corresponds to membership in P;
5. a proof that the proposed quantity can be established without assuming the desired separation.

No such nontrivial gap is supplied here.

## 4. Connection to the verifier projection

For a language \(L\in NP\), let \(R(x,w)\) be its polynomial-time verifier relation. The instance is accepted when the witness fiber is nonempty:

\[
x\in L\iff \exists w\;R(x,w).
\]

A polynomial-time solver is a polynomial-time section selecting a valid witness on every accepted instance. Therefore P = NP is equivalent to the statement that every polynomially verifiable language admits such a polynomial-time witness-selection procedure (with the usual decision/witness formulation).

The residual \(NP\setminus P\) is nonempty exactly when at least one such decision problem has no polynomial-time deterministic decider. This is a statement about the class of problems, not a numerical value of NP itself.

## 5. Lean formalization

The dependency-free Lean module Fold/Complexity/ZeroResidual.lean formalizes the abstract set-theoretic part using predicates over a type of languages:

- NPResidual PClass NPClass L means that L is in NP and not in P;
- ResidualZero means that this residual has no members;
- class_eq_iff_residual_zero proves equality iff the residual is empty;
- class_ne_iff_residual_nonempty proves inequality iff a residual witness exists;
- CollapseBit is a 0/1 indicator, with zero exactly for collapse and one exactly for separation.

The file assumes P is contained in NP, as standard. It does not define concrete Turing machines, prove a lower bound, or decide which branch is true. The theorem is an exact logical characterization, not a resolution of the open problem.

## 6. Current verdict

The proposed equation is not valid with standard meanings of the symbols. The mathematically precise alternatives are

\[
\boxed{P\ne NP\iff NP\setminus P\ne\varnothing}
\]

and, for the defined indicator,

\[
\boxed{P\ne NP\iff C_{P,NP}=1.}
\]

If the intended zero is the vanishing of the NP-over-P residual, then it characterizes P = NP, not P != NP.

The next substantive breakthrough would not be a new name for the residual. It would be a proved lower bound showing that at least one language in NP lies outside P, or a polynomial-time section construction for every NP verifier.

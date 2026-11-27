# Stage 23 — Relationships between affine transformations

## Scope

Given a finite, caller-supplied collection of scalar affine self-maps, compare every unordered pair using exact rational arithmetic. Discover commutation, order dependence, and equality of fixed-point sets.

## Composition and commutation

For
\[
f(x)=ax+b,\qquad g(x)=cx+d,
\]
we obtain
\[
(f\circ g)(x)=acx+ad+b,
\]
\[
(g\circ f)(x)=acx+cb+d.
\]
The slopes agree automatically. Therefore
\[
f\circ g=g\circ f
\iff ad+b=cb+d
\iff (a-1)d=(c-1)b.
\]
The implementation stores the exact intercept difference
\[
\kappa=(ad+b)-(cb+d).
\]
Thus κ=0 precisely when the pair commutes.

The module also compares fixed-point sets. An affine map has all real points fixed when it is the identity, no fixed points when it is a nonzero translation, and one fixed point (b/(1-a)) when (a\ne1). The comparison distinguishes these three cases.

## Proposition

Two affine maps with the same unique fixed point commute.

**Proof.** Suppose (a\ne1), (c\ne1), and both fixed points equal (p). Then (b=(1-a)p) and (d=(1-c)p). Hence
\[
(a-1)d=(a-1)(1-c)p=(c-1)(1-a)p=(c-1)b.
\]
By the commutation criterion, the maps commute. □

## API

- `compose_affine(outer, inner)`: exact ordered composition.
- `analyze_affine_pair`: pairwise commutation, commutator offset, fixed-set relation, and both compositions.
- `discover_affine_relationships`: exhaustive pairwise analysis of a finite declared collection.

## Limits

This is not unrestricted relation discovery. It analyzes only scalar affine maps, only pairs in the supplied finite collection, and only the declared relationship predicates. It does not infer causal relationships, discover arbitrary algebraic structures, or establish general intelligence. A finite collection's pairwise pattern is not a universal theorem about transformations outside that collection.

# Stage 25 — Finite symmetry discovery through group actions

## Model

A finite state set is (X=(x_0,\ldots,x_{n-1})). Each supplied transformation is a permutation (\sigma:X\to X), encoded by an index tuple where entry (i) gives the destination index of (x_i).

The engine requires the supplied permutations to contain the identity and be closed under composition. Since permutations are bijections and the collection is finite, these conditions imply inverses; associativity is inherited from function composition.

## Orbits and stabilizers

The orbit of a state (x) is
\[
G\cdot x=\{g(x):g\in G\}.
\]
Its stabilizer is
\[
G_x=\{g\in G:g(x)=x\}.
\]
Orbits partition the state set. Stabilizers identify transformations that leave a selected state unchanged.

## Structure preservation

An optional binary relation (R\subseteq X\times X) is checked against every transformation. A transformation preserves (R) when
\[
(x,y)\in R\implies(g(x),g(y))\in R.
\]
For a bijection on a finite set, this inclusion implies equality of the image relation with (R). This supports finite graph-like structures, adjacency relations, and other binary relational structures.

## Proposition: orbit partition

The orbits of a group action partition (X).

**Proof.** Every (x\in X) lies in its own orbit because the identity belongs to (G). If (y\in G\cdot x), then (y=g(x)) for some (g\in G). Since (g^{-1}\in G), (x=g^{-1}(y)), so (G\cdot x=G\cdot y). Thus intersecting orbits are equal, and the orbits partition (X). \(\square\)

## Limits

This is a finite, explicitly supplied permutation-group action. It does not infer state encodings or transformations from raw observations, discover arbitrary symmetries in continuous spaces, or establish physical symmetry without a justified state representation and action. Relation preservation is checked only for the supplied binary relation.

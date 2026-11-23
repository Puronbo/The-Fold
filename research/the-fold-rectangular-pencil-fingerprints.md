# G-EP23 — rectangular matrix-pencil fingerprints

A rectangular matrix is a linear map between two different vector spaces. It should not be padded into a square matrix merely to apply a square-operator invariant. For one map over a field, rank classifies it up to independent invertible changes of input and output coordinates. A pair of same-shaped maps contains more relational information.

Let Q,K: V -> W be represented by m x n matrices over F_p. Consider the matrix pencil

\[
P(a,b)=aQ+bK,\qquad [a:b]\in\mathbb P^1(\mathbb F_p).
\]

The projective rank profile records the rank of every nonzero coefficient pair up to scalar. The implementation uses the canonical representatives (1,t), t in F_p, followed by (0,1), so there are exactly p+1 entries.

## Shared-coordinate invariance

Under a common change of coordinates in the codomain and domain,

\[
Q'=SQT^{-1},\qquad K'=SKT^{-1},
\]

where S is in GL_m(F_p) and T is in GL_n(F_p), every pencil member satisfies

\[
aQ'+bK'=S(aQ+bK)T^{-1}.
\]

Multiplication by invertible matrices preserves rank. Thus the entire projective rank profile is invariant. The horizontal concatenation rank of [Q K] and vertical stack rank of [Q;K] are invariant under the corresponding block-diagonal coordinate changes as well.

This is **shared strict equivalence**, not arbitrary independent basis changes for Q and K. The distinction matters for attention: the Q/K coordinated transformation previously studied for Q^T K is a different action and should not be silently identified with this pencil equivalence.

## A small separating example

Over F_2, take Q=I_2. Compare K_1=I_2 with the coordinate-swap matrix K_2=[[0,1],[1,0]]. In both pairs, Q and K individually have rank two. But the projective pencil rank profiles are:

- (Q,K_1): ranks 2,0,2 at (1,0),(1,1),(0,1);
- (Q,K_2): ranks 2,1,2 at those same points.

The paired maps therefore carry information that the two individual ranks miss.

## Implementation and limits

- tools/rectangular_pencil.py: rectangular_pencil_fingerprint(Q, K, p).
- tests/test_rectangular_pencil.py: separation at equal individual ranks, shared-coordinate invariance, genuinely rectangular dimensions, and invalid inputs.
- Uses exact modular Gaussian elimination from the existing spectral engine.
- Computes individual ranks, horizontal/vertical joint ranks, all p+1 projective pencil ranks, and their distribution.
- Does not pad rectangular matrices.
- The rank profile is an invariant, not a complete classification of matrix pencils. More refined classification requires singular blocks and minimal indices, among other structure.

## Neural-network relevance

This offers a low-cost exact diagnostic for paired rectangular projections when a common input/output coordinate action is justified. It can be applied to exported, quantized matrices, but remains prime- and scale-dependent because the real-valued weights are first quantized. A match does not imply matching attention outputs, model behavior, or semantic content. The current result is a mathematical and software capability, not evidence of predictive value on trained transformers.

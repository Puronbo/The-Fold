# Stage 14 — exact compositional relational concepts

## Goal

Stage 13 proposed proportional, inverse, and affine relations independently. Stage 14 composes supported relations into chains while preserving exact arithmetic, provenance, and the domain restrictions of every intermediate step.

## Representation

Represent each relation as a fractional-linear map

\[
f(x)=\frac{ax+b}{cx+d},
\qquad
M_f=\begin{pmatrix}a&b\\c&d\end{pmatrix}.
\]

The Stage 13 families embed as proportional \(ax\), affine \(ax+b\), and inverse \(k/x\). For \(f\) followed by \(g\),

\[
M_{g\circ f}=M_gM_f.
\]

All coefficients are exact Fraction values. Matrices are canonicalized up to nonzero scalar multiplication by setting the first nonzero coefficient to one. Singular nonzero matrices are allowed because constant maps can arise; the all-zero matrix is rejected.

## Domain preservation

The composed matrix alone is insufficient: algebraic cancellation can erase a factor even though an intermediate step was undefined. For example, inverse followed by inverse simplifies to the identity formula, but the original chain remains undefined at zero.

The implementation carries excluded inputs separately. It also pulls an outer map's pole back through the inner map and excludes the corresponding input.

## Evidence and status

Only Stage 13 hypotheses supported on every supplied observation can be converted into maps. Refuted hypotheses are rejected. Composition is an exact algebraic consequence of the supplied parameters, not new empirical evidence.

The API retains the relation-family provenance path. It does not infer missing links, select a best network, infer causality, or extrapolate as a validated physical law. A composed prediction still needs independent endpoint observations for empirical validation.

## Verification

Run:

    python -m unittest agi.test_concept_learner agi.test_concept_proposer agi.test_relation_discovery agi.test_relation_composition -v

Tests cover affine composition, proportional-after-affine composition, inverse-domain exclusions, pulled-back poles, refuted source hypotheses, exact fractions, and constant maps.

## Limits and next step

This is a closed algebraic family of scalar fractional-linear relations, not arbitrary symbolic program composition. It has no units or semantic types, noisy fitting, multivariate relations, uncertainty propagation, automatic graph search, causal identification, or active experiment design. The next extension is to validate composed paths against independent intermediate and endpoint observations and compare competing paths without collapsing distinct semantics.

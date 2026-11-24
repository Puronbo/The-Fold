# G-EP23 — Rectangular matrix-pencil fingerprints

## Purpose

Earlier transformer diagnostics treated rectangular projections as individual maps and reported their modular ranks. A pair of equal-shaped rectangular maps contains relational information that individual ranks discard. This milestone records that information without padding either map into a square matrix.

## Definition

Let (Q,K\in M_{m,n}(\mathbb F_p)). Regard them as a matrix pencil
\[
P(a,b)=aQ+bK,\qquad [a:b]\in\mathbb P^1(\mathbb F_p).
\]
The projective rank profile is the list of ranks of (P(a,b)), one for each projective coefficient class. The implementation uses the representatives ((1,t)) for every (t\in\mathbb F_p), together with ((0,1)).

It also records the ranks of (Q), (K), the horizontal concatenation ([Q\ K]), and the vertical stack \(\begin{bmatrix}Q\\K\end{bmatrix}\).

## Invariance

For invertible (S\in GL_m(\mathbb F_p)) and (T\in GL_n(\mathbb F_p)), apply the same coordinate changes to both maps:
\[
Q'=SQT^{-1},\qquad K'=SKT^{-1}.
\]
Then
\[
aQ'+bK'=S(aQ+bK)T^{-1},
\]
so every pencil rank is preserved. The horizontal concatenation and vertical stack ranks are preserved as well, by corresponding block-diagonal invertible transformations.

This is the standard strict-equivalence setting for a matrix pencil. The invariants are not a complete classification of pencils. Crucially, they do not survive arbitrary *independent* basis changes for Q and K; the common-coordinate assumption is part of the mathematical meaning.

## Why it may matter for transformer projections

For equal-shaped query/key projections, this offers a relational diagnostic beyond comparing each projection's rank separately. It does not assume the matrices are square, and it does not fabricate square operators through padding. Whether shared strict equivalence is the right symmetry for a particular architecture is an open modeling question: query and key channels may have different operational roles, and the actual attention mechanism also depends on activations, scaling, masks, softmax, and value/output paths.

The implementation operates on already-quantized entries in a chosen prime field. Changing the quantization scale or prime can change the result. A matching profile is not evidence of equal attention functions, semantic similarity, or improved model quality.

## Implementation

- `tools/rectangular_pair.py`: exact modular ranks and projective pencil profile.
- `tests/test_rectangular_pair.py`: rectangular dimensions, same individual ranks but different pencil profiles, shared-basis invariance, and validation.

Run the full suite with:

```bash
python -m unittest discover -s tests -v
```

This is an algebraic inspection tool, not a trained-model result. No trained checkpoint has been evaluated in this milestone.

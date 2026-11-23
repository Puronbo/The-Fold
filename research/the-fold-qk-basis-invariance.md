# G-EP20 — a basis-invariance test for Q/K interaction

Let Q,K be integer matrices of shape d_o x d_i and let B be a unimodular integer d_i x d_i matrix. Define
[
Q'=QB,\qquad K'=KB^{-T}.
]
Then
[
Q'^TK'=B^TQ^TKB^{-T}.
]
Since (B^T) is invertible, this is a similarity transformation of the input-space interaction (Q^TK). Its characteristic polynomial, rank, and complete finite-field factor/Frobenius profile are preserved modulo every prime.

This is deliberately narrower than claiming that every basis transformation of a real neural network preserves its attention computation. It is an algebraic coordinated transformation of the two projection matrices, and only the specified product is guaranteed to be similar. The separate Q and K ranks are preserved by invertible right multiplication, but their individual characteristic polynomials need not be.

## Implementation

`tools/qk_basis_change.py` accepts Q, K, B, and the exact integer inverse transpose B^(-T). It verifies both inverse identities over the integers, so the transformation is unimodular and invertible modulo every prime. It then computes before/after Q^T K profiles and Q/K modular ranks.

## Test fixture

A nontrivial integer shear with determinant one is tested over F_2, F_3, F_5, and F_7. The test confirms exact equality of the full input-space interaction profiles and preservation of individual projection ranks. Invalid inverse data and incompatible dimensions are rejected.

Run:
```bash
python -m unittest tests.test_qk_basis_change -v
```

## Interpretation

G-EP20 establishes a real invariance of the chosen relational matrix under a precisely specified gauge-like coordinate change. It does not show that this invariant predicts model behavior, nor that it is invariant under independent changes to Q or K. In particular, the output-space product QK^T and the individual projection spectra are not covered by this similarity guarantee.

The next research step should construct perturbations that preserve Q and K ranks while changing Q^T K, and coordinated perturbations that preserve Q^T K exactly. This will test how much information the relational profile retains beyond the individual projection ranks.

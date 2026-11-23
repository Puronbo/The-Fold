# G-EP30 — Strict-equivalence certificate verifier

For a pencil (P(t)=Q+tK), strict equivalence over (mathbb F_p) means that there are constant invertible matrices (S,T) such that

[
Q'=SQT,qquad K'=SKT.
]

This is deliberately different from polynomial unimodular equivalence of (Q+tK), which permits (U(t),V(t)) with polynomial entries. G-EP28–29 concern the latter.

The new API `strict_pencil_equivalence_audit(q,k,p,q_target,k_target,left_transform,right_transform)` verifies a supplied pair of constant witnesses. It checks dimensions, computes both determinants over (mathbb F_p), and verifies the two coefficient identities independently. A certificate is accepted only if both transforms are invertible and both identities hold.

The verifier does not find (S,T), does not construct a Kronecker form, and does not infer strict equivalence from matching Smith data. It is a reliable verification boundary for future constructive algorithms.

Tests cover a right singular block (L_2), a nontrivial constant basis change, singular candidate transforms, altered targets, and shape/type validation.

# G-EP31 — Bounded constructive recovery of a single singular block

G-EP31 moves beyond witness verification in one tightly delimited case. For an (e\times(e+1)) pencil, the canonical right singular block is

[
L_e(t)=Q+tK,\qquad Q=[I_e\ 0],\quad K=[0\ I_e].
]

The transposed block is the canonical left singular block.

`recover_single_singular_block_equivalence` enumerates (GL_m(\mathbb F_p)\times GL_n(\mathbb F_p)) and searches for constant invertible (S,T) such that (SQT=Q_0) and (SKT=K_0). A found witness is immediately passed to the independent G-EP30 verifier. The API reports the exact search-space size, tested pair count, and whether the search was exhaustive.

This is constructive but intentionally small-scale: the search is exponential/factorial in dimensions and is capped by `max_pairs`. It supports only a single right or left singular block, not a mixed pencil, multiple singular blocks, or a regular part. A budget refusal is explicitly not a negative classification result.

This gives us a tested end-to-end path from an input pencil to an explicit strict-equivalence certificate for the one-block case, without pretending to solve general Kronecker canonical decomposition.

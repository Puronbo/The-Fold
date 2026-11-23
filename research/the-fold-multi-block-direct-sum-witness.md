# G-EP58: Exact multi-block direct-sum witness verification

G-EP57 verified a supplied two-block rectangular direct-sum witness. G-EP58
extends the same certificate boundary to an ordered list of two or more
rectangular diagonal blocks.

For Q,K in F_p^(m x n), supplied S in GL_m(F_p), T in GL_n(F_p), and block
shapes (r_i,c_i), the verifier requires sum(r_i)=m and sum(c_i)=n. It computes
SQT and SKT, partitions both using cumulative row and column cuts, and checks
that every off-diagonal block vanishes in both coefficients. The diagonal
blocks may be rectangular.

## Scope and limitations

- This verifies supplied transforms and block shapes; it does not discover them.
- It does not prove uniqueness, indecomposability, or regularity of any block.
- It does not replace G-EP49/50's structured or exhaustive witness discovery.
- A failed check invalidates the supplied witness, not every possible split.

Tests cover a scrambled three-block rectangular witness, coupling in both
coefficients, singular transforms, composite moduli, and invalid partitions.


## G-EP59 integration

Successful results from `recover_mixed_kronecker_pencil` now include an ordered `canonical_block_shapes` list and `multi_block_direct_sum_audit`. The order matches canonical target assembly: right singular blocks, left singular blocks, then the regular canonical blocks. The multi-block verifier independently checks the recovered constant transforms against every cross-block cut in both coefficient matrices. The existing whole-target strict-equivalence audit remains in place, so callers receive both an overall equality certificate and a block-structure certificate. This adds no new search capability and leaves incomplete-profile, structured-budget, and exhaustive-search semantics unchanged.

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

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


## G-EP90: Rectangular multi-block basis-invariance controls

The multi-block verifier is now exercised on a generated-style partition that
contains both a zero-row block and a zero-column block while keeping positive
total row and column dimensions. Over each of F₂, F₃, F₅, and F₇, independent
invertible unitriangular left and right basis changes scramble both pencil
coefficients. The supplied inverse basis changes recover the exact block
diagonal pair, including its empty-width/empty-height diagonal pieces, and the
verifier must accept the witness with the original ordered block shapes.

This is finite regression coverage for the stated rectangular edge case and
constant strict-equivalence convention. It does not imply decomposition
discovery, uniqueness, or a universal invariance theorem beyond the algebraic
identities checked by the verifier.


## G-EP91: Adversarial basis-invariance witness checks

The generated rectangular basis-scrambled fixture from G-EP90 is now tested
against individual off-diagonal mutations. Each representable directed
off-diagonal block is injected separately into Q and K over F₂, F₃, F₅, and
F₇; additional cases mutate both coefficients at once. The audit must identify
which coefficient contains coupling and reject the combined witness.

The tests also perturb the supplied left and right transforms while keeping
them invertible, and separately supply singular square transforms. These are
well-formed but mathematically false witnesses and must produce a negative
audit rather than a caller-input exception. By contrast, ragged or
dimension-incompatible transforms and boolean/floating-point entries are
malformed inputs and must raise ValueError. A failed witness invalidates only
that supplied witness; it does not prove that no alternative decomposition
exists. The cases are finite regression coverage, not a universal theorem.


## G-EP92: Stability under equivalent representations

Regression controls now check equivalent presentations of the same
multi-block direct sum over F₂, F₃, F₅, and F₇. Adding integer multiples of
the modulus to source entries leaves the normalized transformed matrices
unchanged. Independently selected invertible left/right basis scramblings
remain accepted, as do reciprocal nonzero scalar rescalings
(S -> cS, T -> c⁻¹T), which preserve both transformed coefficients exactly.
A simultaneous permutation of the row and column coordinate intervals and
their ordered rectangular block shapes also remains a valid direct-sum
witness.

These tests establish representation stability for the finite fixtures only.
They do not establish uniqueness of a block partition or witness, nor do they
turn failure of one supplied witness into a no-decomposition result.

# G-EP56: Exact feasibility certificates for minimal-chain annihilator complements

G-EP55 computed bases for two simultaneous annihilator spaces and greedily
attempted to extend the fixed minimal-chain bases. This milestone makes the
success/failure criterion explicit and returns exact rank certificates.

## Exact criterion

Let (C_D) be the span of the fixed right-chain domain vectors and (A_D)
the common kernel of the left-chain constraints
(S_{chain}Qv=0) and (S_{chain}Kv=0). A domain complement selected inside
(A_D) exists exactly when

[
dim(C_D+A_D)=n.
]

The implementation computes a basis of (A_D) by exact row reduction over
(mathbb F_p), then reports the rank of the concatenated spanning families
for (C_D) and (A_D). The codomain condition is dual: if (C_C) is the
fixed left-chain covector span and (A_C) is the common annihilator of
(QT_{chain}) and (KT_{chain}), a codomain completion exists exactly when
(dim(C_C+A_C)=m).

These tests are necessary and sufficient for basis completion **inside the
specified annihilator spaces**. Since each candidate list spans its entire
annihilator space, greedy independent extension is complete: enumerating
additional field-linear combinations cannot increase the span and is
unnecessary.

## Output

The G-EP55 result now includes `feasibility_certificate` with each combined
span rank, ambient dimension, deficiency, and Boolean feasibility flag.
A positive certificate permits basis construction, after which the routine
still verifies invertibility, both transformed coefficient identities, and
zero cross-coupling blocks by exact arithmetic.

A positive rank deficiency proves that no complement exists within that
particular fixed-chain annihilator space. It does **not** prove that the
pencil has no other direct-sum splitting, nor does it rule out a different
strict-equivalence construction that does not obey these annihilator
constraints. It also makes no claim that the residual block is regular.

## Validation

Tests check the full-rank zero-chain case and verify that the mixed fixture's
completion flag agrees exactly with both rank certificates. Any reported
failure must have a positive deficiency on at least one side.

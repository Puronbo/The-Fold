# G-EP5 — Jordan fingerprints from kernel growth

## Status

**Theorem / algorithm.** This note gives an exact way to recover the Jordan block sizes of a finite-dimensional linear operator from kernel dimensions. It extends the spectral fingerprint beyond cyclotomic companion matrices. It does not assert that every Fold operator has been constructed or computed.

## 1. Kernel-growth theorem

Let V be a finite-dimensional vector space over a field K, let A:V→V be linear, and suppose the characteristic polynomial of A splits over K. Fix an eigenvalue λ. Put

[
K_r(\lambda)=\dim_K\ker(A-\lambda I)^r,\qquad K_0(\lambda)=0.
]

Let b_r(λ) be the number of Jordan blocks for λ whose size is at least r, and let c_r(λ) be the number whose size is exactly r. Then

[
K_r-K_{r-1}=b_r,
qquad
c_r=b_r-b_{r+1}
=2K_r-K_{r-1}-K_{r+1}.
]

In particular, K_1 is the geometric multiplicity, while the eventual stable value of K_r is the algebraic multiplicity of λ.

### Proof

On a Jordan block J_s(λ), the operator A−λI restricts to the nilpotent Jordan block N_s. The kernel of N_s^r has dimension min(r,s): each application of N_s shifts one position along the Jordan chain, and precisely min(r,s) basis vectors are killed by the r-th power.

The Jordan decomposition is a direct sum, so dimensions add:
[
K_r(\lambda)=\sum_{s\ge1}c_s(\lambda)\min(r,s).
]
Taking the first difference gives
[
K_r-K_{r-1}=\sum_{s\ge r}c_s=b_r,
]
and taking the next difference gives
[
b_r-b_{r+1}=c_r.
]
For r large enough, min(r,s)=s for every block, hence K_r=Σ_s s c_s, the total algebraic multiplicity. Also K_1=Σ_s c_s, the number of blocks, which is the geometric multiplicity. ∎

The same formulas apply when K is not algebraically closed, provided λ∈K and the λ-primary component is considered; the Jordan-block statement is over a splitting field. For a complete profile over K, factorization data must also be retained.

## 2. Shape constraints and stopping rule

The increments
[
b_r=K_r-K_{r-1}
]
are nonnegative integers and are nonincreasing:
[
b_1\ge b_2\ge b_3\ge\cdots\ge0.
]
Equivalently, the kernel-growth sequence is increasing and discretely concave. A violation is an implementation error or inconsistent input.

The sequence stabilizes once r reaches the largest Jordan block size for λ. In an n-dimensional space it must stabilize by r≤n. Thus at most n successive nullity computations are required, and in practice computation stops as soon as K_r=K_{r-1}; all later increments are zero.

## 3. Worked example

Suppose the λ-primary Jordan block sizes are 3, 2, and 1. Then
[
(K_0,K_1,K_2,K_3,K_4)=(0,3,5,6,6).
]
The first differences are
[
(b_1,b_2,b_3,b_4)=(3,2,1,0),
]
so there are 3 blocks of size at least 1, 2 of size at least 2, and 1 of size at least 3. The second differences give
[
(c_1,c_2,c_3)=(1,1,1).
]
The recovered partition is therefore 3+2+1. Its algebraic multiplicity is 6 and its geometric multiplicity is 3.

## 4. A finite-field spectral fingerprint

For an integer matrix A and prime p, define its p-profile by retaining:

1. the factorization of the characteristic polynomial of A modulo p;
2. for each irreducible factor, its degree and multiplicity;
3. for each eigenvalue λ in the chosen splitting field, the kernel-growth sequence K_r(λ), or equivalently the Jordan-block partition.

The characteristic polynomial alone supplies algebraic multiplicities and irreducible factorization, but not the Jordan partition. Kernel growth supplies the missing information.

For an eigenvalue not in F_p, compute after passing to a finite extension in which the relevant irreducible factor splits. If an irreducible factor has degree d over F_p, its roots lie in F_{p^d}; a common splitting field for all factors can be taken with degree the least common multiple of their degrees. The profile should record the base field and extension degree so that eigenvalues and multiplicities are not confused across fields.

For the cyclotomic companion C_m, G-EP4 already gives the partition directly: if m=p^a n with p∤n and a≥1, then the reduced characteristic polynomial is Φ_n^{φ(p^a)}, and cyclicity gives one Jordan block of size φ(p^a) for each distinct residual root. G-EP5 provides a general matrix method that can verify this result without relying on the companion-specific shortcut.

## 5. Algorithm

Given A over F_p (or a finite extension):

1. Factor χ_A(x) over the base field.
2. Choose a splitting extension for the factor(s) whose roots are to be profiled.
3. For each eigenvalue λ, compute the nullities K_r = nullity((A−λI)^r), beginning with K_0=0.
4. Form b_r=K_r−K_{r−1}; check b_r≥b_{r+1}≥0.
5. Recover c_r=b_r−b_{r+1}; discard trailing zeros.
6. Stop when K_r=K_{r−1}.

A numerically stable floating-point tolerance is not appropriate for these exact finite-field ranks: rank and nullity must be computed with exact field arithmetic. For large sparse matrices, sparse elimination or Krylov-style methods may reduce cost, but their output must still be certified over the stated field.

## 6. Relevance to reusable AI and scientific software

This is a small, backend-independent linear-algebra primitive. An implementation can expose a function of the form

`jordan_profile(A, field, eigenvalue_or_factor)`

returning the field, characteristic factor, nullity sequence, and block partition. It can sit behind an existing AI or scientific-computing stack without changing its neural-network architecture: use it as a diagnostic for finite-field state-transition operators, exact modular test matrices, or algebraic components of a model. It is not itself a transformer improvement, and no speedup or learning benefit follows from the theorem alone.

The separation of concerns is deliberate:

- model/framework layer: supplies the matrix or operator;
- exact algebra layer: performs factorization and rank/nullity over the declared field;
- fingerprint layer: serializes the invariant profile;
- comparison layer: compares profiles only when base fields and extension conventions match.

A future adapter could translate a supported framework tensor into an exact modular matrix, but quantized floating-point weights are not automatically elements of a finite field. The conversion rule must be explicit and mathematically meaningful.

## 7. Formalization and tests

A Lean formalization should first prove the nilpotent Jordan-block identity
`finrank (ker N^r) = min(r,s)`
for a standard nilpotent Jordan block, then lift by direct sums and derive the difference formulas. This is a target, not a claim that the repository's current Lean build contains the theorem.

Minimum computational tests:

- a single block of sizes 1, 2, and 3;
- direct sums with repeated block sizes;
- a diagonalizable matrix (all blocks size 1);
- a non-split characteristic polynomial, profiled only after a declared splitting extension;
- the ramified cyclotomic companion cases already recorded in G-EP4.

## 8. Boundary of the result

The theorem is standard Jordan theory expressed as an invariant-recovery algorithm. Its contribution to this research sequence is the reusable interface: factorization describes which eigenvalues occur, while kernel growth describes the nilpotent structure attached to each eigenvalue. Together they form a complete Jordan fingerprint over a splitting field.

It does not infer a neural network's behavior from its spectrum, establish stability or generalization, or prove that two operators with the same fingerprint are similar unless the full eigenvalue-labelled Jordan data over the same field are identical. With that full data, Jordan canonical form does give similarity over the splitting field.

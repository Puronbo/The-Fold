# Equivariant learning and exact symbolic verification for the Fold section-change action

## Purpose

This note defines a machine-learning research track built around the characteristic-two coefficient-section action. The goal is not to replace proof with prediction. It is to let statistical models propose compact transformation laws, rank candidate identities, and discover useful invariant features, while an exact algebraic backend decides which claims are true.

The verified local setting is
\[
E=F(t),\qquad F=\mathbb F_2(S),\qquad t^2=S,
\]
\[
L=E((p)),\qquad M=L\,d\log t\oplus L\,d\log p,\qquad
R=B^1+(\Phi-1)M.
\]
Finite section changes \(t\mapsto t(1+p^rv)\), \(v=e+ft\), preserve \(R\) by Cartier naturality (G-4ch) and have the exact ambient pullback formula (G-4ci).

## 1. Verified algebraic supervision

For a negative odd source layer, write its quotient coordinate as \((x,y)\in F^2\), represented by \((A,B)=(x,ty)\). For a negative even source layer, write \(d\in F\), represented by \((A,B)=(0,td)\).

For an isolated parameter \(v=e+ft\) at depth \(r\), the first nonzero graded corrections are
\[
\delta^{odd}_{r,v}(x,y)=
\begin{cases}
fx+ey\in F,&r\text{ odd},\\
(0,fx+ey)\in F^2,&r\text{ even},
\end{cases}
\]
and
\[
\delta^{even}_{r,v}(d)=
\begin{cases}
(0,ed)\in F^2,&r\text{ odd},\\
ed\in F,&r\text{ even}.
\end{cases}
\]
The even-depth odd-source formula includes the \(fx\) contribution from the first logarithmic coefficient. This corrects the earlier G-4ca expression.

The leading Lie bracket and ordered composition cross term are
\[
[X_v,X_u]=X_{t(e_vf_u+e_uf_v)},
\]
\[
w_{r+s}^{\mathrm{mixed}}=e_u v
\]
for the composition order used in G-4cc. The reversal difference is \(t(e_uf_v+e_vf_u)\).

The second isolated diagonal is also available:
\[
D_v=S(e^2+Sf^2)\partial_S,
\]
\[
N_{odd}(x,y)=
(Sf^2x+D_vx,\ e^2y+D_vy),\qquad
N_{even}(d)=e^2d+D_vd.
\]
These are verified low-order targets. The complete higher-order quotient matrices are not known.

## 2. Exact data generator

The companion script \`tools/section_change_equivariance_data.py\` uses the polynomial subring \(\mathbb F_2[S]\subset F\). It encodes a polynomial as an integer bitmask: bit \(i\) is the coefficient of \(S^i\). Addition is XOR and multiplication is carry-free polynomial convolution.

It emits JSONL examples for:
- odd-layer and even-layer first-order transitions;
- leading Lie brackets;
- ordered mixed composition coefficients.

The script's self-test recomputes the quotient projections from the raw coefficient pairs and checks the nonzero-parameter detection probes. Example:
\`\`\`bash
python tools/section_change_equivariance_data.py --self-test --count 1000 --max-degree 4 > section_change_train.jsonl
\`\`\`

This data covers a polynomial coefficient subring, not all rational functions in \(F\). Generalization to rational coefficients is a separate evaluation. No neural network has yet been trained; the script is an exact oracle/data foundation, not a claim of learned performance.

## 3. Proposed hybrid model

A suitable architecture has four explicitly typed stages.

1. **Symbolic coefficient encoder.** Encode a rational function by a normalized numerator/denominator polynomial pair or a sparse expression tree. Keep the filtration depth and odd/even quotient type as type information rather than flattening them into undifferentiated features.
2. **Equivariant transformation layer.** Apply section changes through exact pullback/reduction. For learned approximations, enforce the intertwining condition
   \[
   \mathcal E(\sigma\cdot q)=\rho(\sigma)\mathcal E(q)
   \]
   on intermediate features. Do not approximate the group law by unconstrained augmentation.
3. **Invariant readout.** Build candidate scalar features \(I(q)\) satisfying
   \[
   I(\sigma\cdot q)=I(q).
   \]
   Their existence and completeness are open invariant-theory questions; the model may propose generators, but symbolic orbit tests must verify them.
4. **Exact verifier.** Recheck proposed transition formulas, bracket identities, cocycles, and invariant identities using exact \(\mathbb F_2[S]\) or rational-function arithmetic. A high model score is never itself a proof certificate.

## 4. Training tasks and leakage-resistant evaluation

The first benchmark should use the exact generator for three supervised tasks:

- predict the graded transition from \((r\bmod 2,e,f,x,y)\);
- predict the bracket parameter from two section parameters;
- predict the ordered composition cross term and its reversal defect.

Use structured holdouts, not only random train/test splits:
- hold out higher polynomial degrees in \(S\);
- hold out depths not seen during training;
- hold out compositions of three or more section changes;
- test equivalent symbolic presentations of the same rational function;
- include zero, dependent, and independent parameter pairs to test kernel and centralizer detection.

A second benchmark can begin only after the exact finite-pullback reducer computes certified quotient labels beyond the first two diagonals. It can then ask the learner to discover the \(p^3,p^4,\ldots\) extension maps and composition cocycles. Until then, those targets remain unlabelled.

## 5. Adjacent mathematical problems

### Gauge geometry

A coefficient section is a choice of local frame. Section changes are gauge transformations; quotient classes and their associated graded are intrinsic, while an explicit direct-sum splitting is frame-dependent. This is directly analogous to gauge-equivariant learning, where internal features transform covariantly and observables may be invariant.

### Invariant theory

Compute the invariant algebra of the quotient action and classify equivariant maps between the alternating \(F^2\) and \(F\) graded pieces. The zero group center and trivial action kernel do not imply that the quotient has no fixed vectors or no invariant functions.

### Filtered extensions and group cohomology

The first-order arrows and the p-squared composition identities are extension data for a filtered representation. The cross terms \(M_uL_v\) and \(L_uM_v\) are the first concrete cocycle-like terms. A formal cohomology classification should follow only after the coefficient modules and the full filtered group action are specified.

### Deformation theory

Independent higher-depth parameters are new deformation directions; lower-depth parameters force part of their composite corrections. The exact obstruction to extending a truncated action from depth \(n\) to \(n+1\) is a natural next symbolic-learning target.

## 6. Research references

- Gerken et al., [Geometric Deep Learning and Equivariant Neural Networks](https://doi.org/10.1007/s10462-023-10502-7), a survey of group- and gauge-equivariant architectures.
- Blum-Smith and Villar, [Machine Learning and Invariant Theory](https://doi.org/10.1090/noti2760), on invariant-theoretic structure in machine learning.
- Winter et al., [Unsupervised Learning of Group Invariant and Equivariant Representations](https://papers.neurips.cc/paper_files/paper/2022/hash/cf3d7d8e79703fe947deffb587a83639-Abstract-Conference.html), separating invariant content from a group-action component.
- Shalyt, Elimelech, and Kaminer, [ASyMOB: Algebraic Symbolic Mathematical Operations Benchmark](https://proceedings.mlr.press/v306/shalyt26a.html), which motivates equivalence-preserving perturbation and robustness tests for symbolic reasoning.

## Status

- **Proved / algebraically checked:** first-order graded transitions (with the even-depth correction), leading bracket/composition term, and isolated second diagonal.
- **Implemented and self-tested:** standard-library GF(2)[S] data generator.
- **Not yet done:** train a neural model; compute the invariant ring; classify equivariant maps; obtain exact higher-order quotient matrices and labels.


## 7. Fixed vectors versus invariant functions

G-4cm proves that the common fixed-vector subspace of the quotient representation is exactly the zero-exponent layer \(Q_0\). This is a statement about invariant **vectors**, not invariant linear functionals. A linear readout \(\ell:Q\to k\) is invariant precisely when it annihilates the span of all differences \(gq-q\); equivalently, it belongs to the dual of the coinvariant quotient
\[
Q_{\mathcal G}=Q/\langle gq-q:g\in\mathcal G,\ q\in Q\rangle.
\]
The fixed-vector theorem does not determine this coinvariant quotient, so it does not yet show that invariant linear readouts factor through \(Q_0\). Nonlinear invariant functions are a further, separate question.

This gives a useful machine-learning diagnostic:
- the fixed-vector subspace is \(Q_0\), but linear invariant readouts must be computed from the coinvariants \(Q_{\mathcal G}\), not inferred from fixed vectors;
- nonlinear invariant candidates must be tested on full group orbits;
- an equivariant latent representation must retain the negative filtered components, since those components transform nontrivially even though each associated-graded layer is unchanged on its diagonal.

The distinction prevents the model from collapsing all negative layers merely because their associated-graded action is the identity.


## 8. Important representation-theoretic distinction

For a possibly non-semisimple representation, fixed vectors and invariant linear functionals are different objects:
\[
Q^{\mathcal G}=\{q:gq=q\ \forall g\},\qquad
(Q^*)^{\mathcal G}\simeq (Q_{\mathcal G})^*.
\]
The first is known from G-4cm. The second requires an independent computation of coinvariants. The exact data pipeline must keep both targets separate; otherwise a learner may be trained toward an incorrect invariant readout.


## 9. Cartier-aware coinvariant features

G-4co gives a mathematically useful intermediate target. At the first arrow level, all negative even layers and the second coordinate of negative odd layers are in the generated difference image. The corrected second diagonal removes \(SF^2\) from the first coordinate of each odd negative layer. The resulting two-diagonal residual is
\[
F/SF^2\simeq\Omega_F^1/dF,\qquad [x]\mapsto (x/S)dS.
\]
This is an approximation to the full coinvariant quotient, not its final answer; higher Frobenius/divided-power terms and the zero-mode boundary may impose more relations.

The exact encoder should therefore perform the p-basis decomposition
\[
x=a^2+Sb^2
\]
and retain the \(a\)- and \(b\)-channels separately. The Cartier operator provides the natural quotient map on differentials: exact forms are its kernel, and logarithmic forms are Cartier-stable. See the [function-field Cartier reference](https://sporadic.stanford.edu/reference/function_fields/sage/rings/function_field/differential.html).

### New certified tasks

The data generator now includes:
- p-basis decomposition and derivative extraction;
- the corrected second odd-layer diagonal;
- the second even-layer diagonal;
- verification that the first coordinate of the odd second diagonal lies in \(SF^2\), and that this image is attained exactly on polynomial coefficients.

Run:
\`\`\`bash
python tools/section_change_equivariance_data.py --self-test --count 1000 --max-degree 5 > section_change_train.jsonl
\`\`\`

A run with these settings passed all self-tests and generated 5,000 JSONL examples. This is a reproducible exact dataset generator over \(\mathbb F_2[S]\), not evidence of neural generalization to \(\mathbb F_2(S)\).

### Learning the unresolved tower

A useful next model predicts the first nonzero Frobenius-scaled diagonal for inputs in \(F^{2^h}\). The scaling section \(t\mapsto t(1+p)\) changes \(S\) by \(S\mapsto S(1+p^2)\), so a \(2^h\)-th power has its first possible coefficient at depth \(2^{h+1}\). The target coefficient is \((Sa')^{2^h}\) when the input is \(a^{2^h}\).

This creates a controlled extrapolation benchmark over the Frobenius level h. Train on small h, hold out larger h, and require the exact verifier to check the predicted exponent and coefficient. The goal is to discover the full coinvariant/Frobenius tower without treating guessed higher-order formulas as proof.

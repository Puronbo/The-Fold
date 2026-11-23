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
python tools/section_change_equivariance_data.py --self-test --count 1000 --max-degree 5 > section_change_train.jsonl
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

The current generator emits eight rows per sample iteration plus one rational challenge, hence 8,001 rows for count 1,000. I independently checked the polynomial tower decomposition exhaustively for all bitmasks below 2^12 and the Hasse/Frobenius first-coefficient identity for all masks below 2^10 and Frobenius levels h≤6. These are component-level checks; the full updated script has not yet been run as a repository CI job. The symbolic rational witness is a separate exact challenge, not a polynomial training example.

### Learning the unresolved tower

A useful next model predicts the first nonzero Frobenius-scaled diagonal for inputs in \(F^{2^h}\). The scaling section \(t\mapsto t(1+p)\) changes \(S\) by \(S\mapsto S(1+p^2)\), so a \(2^h\)-th power has its first possible coefficient at depth \(2^{h+1}\). The target coefficient is \((Sa')^{2^h}\) when the input is \(a^{2^h}\).

This creates a controlled extrapolation benchmark over the Frobenius level h. Train on small h, hold out larger h, and require the exact verifier to check the predicted exponent and coefficient. The goal is to discover the full coinvariant/Frobenius tower without treating guessed higher-order formulas as proof.


## 10. Rational-function Cartier features and residue targets

The polynomial-only benchmark is insufficient for the stable scaling problem: nontrivial periodic simple-pole classes require rational denominators. A second exact encoder now works directly in \(F=\mathbb F_2(S)\), representing a rational function as a normalized numerator/denominator pair of GF(2)[S] bitmasks.

For the p-basis decomposition
\[
f=a_0^2+Sa_1^2,
\]
the even-component root \(C_0(f)=a_0\) is computed without adjoining square roots by multiplying \(f=N/D\) by \(D^2\) and splitting \(ND=A^2+SB^2\):
\[
C_0(f)=A/D,\qquad C_1(f)=B/D.
\]
The exact check identity is
\[
C_0(f)^2=f+Sf'.
\]

The pure-scaling tower is the direct limit of \(C_0\), equivalently \(F/\bigcup_n\ker C_0^n\). Its stable quotient has the explicit residue-field decomposition
\[
\mathbb F_2\oplus\bigoplus_{Q\ne S}\mathbb F_2[S]/(Q),
\]
over monic irreducibles Q. Each \(Q\ne S\) simple-pole coefficient block is acted on invertibly; higher Q-poles contract to simple poles. The S-pole block is nilpotent and polynomial terms reduce to constants.

The companion script tools/cartier_stable_part.py:
- performs exact rational arithmetic over GF(2)(S);
- computes \(C_0,C_1\), derivatives, and iterates;
- enumerates irreducible Q of bounded degree;
- checks invertibility on each simple-pole coefficient space for Q≠S;
- checks pole-order contraction and the identity \(C_0(f)^2=f+Sf'\);
- emits rational-function orbit examples for learning.

Independent core checks passed for all 14 monic irreducibles of degree at most five and pole orders through eight. These tests confirm the p-basis identity, simple-pole ranks, and pole-order bounds. They are exact algebra checks; no neural training or generalization claim is made.

### New learning benchmark: residue recovery

Train a model to predict:
1. the next \(C_0\)-iterate of a rational function;
2. whether a simple-pole block is stable or nilpotent;
3. the residue-field coordinate \(P(\alpha)/(\alpha Q'(\alpha))\) for a simple pole \(P/Q\);
4. the eventual simple-pole representative after repeated p-basis reduction.

Use irreducible polynomials of unseen degrees as a structural holdout. Also hold out pole orders and rational numerators/denominators, so the model cannot solve the task by memorizing polynomial bit patterns. An exact GF(2)[S] verifier remains authoritative.

The remaining mathematical question is whether general section changes act trivially on this residue module. Until that is proved or disproved, these are the exact invariants of the pure-scaling subgroup, not certified invariants of the full section-change group.


## 11. Stable Cartier modules: rational-function data

The exact learning benchmark now includes rational functions, not only polynomial coefficients. This is necessary because the stable scaling quotient contains simple-pole classes at every monic irreducible \(Q\ne S\); a polynomial-only dataset misses them.

A rational function is encoded as a reduced bitmask pair \(N/D\). The p-basis root operator is computed by
\[
ND=A^2+SB^2,\qquad C_0(N/D)=A/D,\quad C_1(N/D)=B/D.
\]
The verifier checks
\[
C_0(f)^2=f+Sf'.
\]
The stable quotient for the pure scaling subgroup is
\[
\mathbb F_2\oplus\bigoplus_{Q\ne S}\mathbb F_2[S]/(Q).
\]
A simple pole \(P/Q\) is a stable coordinate, and \(C_0\) acts on its residue coefficient by the invertible semilinear map
\[
\bar P\longmapsto
\sqrt{\bar S\,\overline{Q'}\,\bar P}.
\]
Higher-order poles contract to simple poles; the distinguished S-pole block is nilpotent.

The exact rational verifier is tools/cartier_stable_part.py. Its test design checks all irreducible polynomials up to a selected degree, the ranks of the simple-pole maps, and the reduction of pole order under \(C_0\).

### Revised benchmark protocol

Use three distinct holdouts:
- unseen irreducible polynomials Q (new closed points);
- unseen pole orders (higher-order-to-simple-pole reduction);
- unseen rational numerators/denominators (avoid memorizing coefficient patterns).

The full section-change coinvariant is now computed in G-4ct. The correct target is the Frobenius-normalized orbit sum across exponents \(-q,-2q,-4q,\ldots\), not a residue at one exponent. The exact rational residue generator covers each finite residue field; add orbit-stage sequences and adjacent \((\alpha,\alpha^2)\) relation pairs to train the normalized sum.


## 12. Learning the finite section-change Cartier tower

The exact finite pullback has now been reduced to a rational one-variable coefficient problem. For \(s=t(1+p^r(e+ft))\), q=p^{2r}, u=e²+Sf², and an odd residual input \(a²\),
\[
A'_0=a(S(1+qu))²\frac{1+qe²}{1+qu}.
\]
The first two corrections are exact:
\[
\Delta_1=Sf²a²\in\ker C_0,\qquad
C_0²(\Delta_2)=0.
\]
A higher-order bound \(C_0^{v_2(m)+1}(\Delta_m)=0\) is a conjectural pattern from bounded exact tests, not a theorem.

The companion script tools/section_change_cartier_stability.py uses exact rational-function arithmetic from cartier_stable_part.py, expands the pullback to a chosen q-order, verifies the first two identities, and stress-tests the proposed higher-order torsion bound. It also emits rational input/target-orbit examples. The exact algebraic identities are the certified labels; higher-order vanishing is explicitly tagged as exploratory.

A productive model task is to predict the C0-torsion depth of each coefficient \(\Delta_m\), then extrapolate to unseen rational denominators and larger m. A verifier should reject any prediction that fails exact rational arithmetic. The model is being used as a conjecture generator, not as a proof engine.

### Residue-coordinate supervision

G-4cq identifies the pure-scaling stable module with residue fields \(\kappa_Q\) at finite closed points. Ohi's Cartier-compatible residue theory gives a possible invariant target under changes of local parameters. The next dataset should pair:
- a rational coefficient and its simple-pole residue coordinate;
- its finite section-change pullback;
- the difference of the resulting residue coordinates;
- the applicable Cartier filtration depth and valuation bound.

This benchmark must distinguish the pure-scaling residue module (proved) from the still-open full section-group coinvariant. No full-group invariant label should be included before that bridge is proved.


## 13. Use the Cartier-stable differential module as the canonical latent space

G-4ct gives an exact intertwining map
\[
\Theta(x)=\frac{x}{S}dS,\qquad C\Theta=\Theta C_0,
\]
and identifies the pure-scaling stable quotient with
\[
\Omega_F^1/B_\infty.
\]
The finite closed-point coordinates are residue fields \(\kappa_Q\), plus the constant block at \(S=0\).

This suggests replacing raw coefficient vectors by a residue-aware latent representation:
- decompose a rational coefficient into its partial-fraction blocks;
- apply Cartier until each nonstable higher-pole block contracts or vanishes;
- encode each stable simple-pole block by its residue-field coordinate;
- retain the distinguished \(S=0\) block separately.

This representation is canonical for the pure-scaling subgroup. It becomes a canonical feature space for the full section-change group only after the open G-4cr/G-4cs residue-invariance problem is settled. The learning system must preserve this distinction.


## 14. Latest rational pullback stress test

The exact finite-section test harness was run with:
- 50 rational inputs \(a,e,f\in\mathbb F_2(S)\);
- irreducible denominator factors of degree at most 4;
- pullback expansion through \(q^{13}\);
- all 650 nonconstant coefficients checked against the proposed \(C_0^{v_2(m)+1}\)-torsion bound.

All 650 coefficient checks passed. A separate generated sample of 100 rational inputs produced 900 coefficient targets with observed Cartier-torsion indices 1, 2, 3, and 4. This is bounded computational evidence only; it does not prove the all-orders pattern or identify the full section-group coinvariant.

G-4ct now identifies the stable target exactly as \(\Omega_F^1/B_\infty\). For the model, this suggests a two-stage encoder: first map a rational coefficient into the Cartier-stable differential module, then express the stable component through its closed-point residue coordinates. The full section group is not yet certified to act trivially on that module.


## 15. Hasse–Taylor learning targets

G-4cu gives a closed coefficient formula for the finite-section pullback. If \(a^{[i]}\) are Hasse derivatives and \(B_N(a)=\sum_{i=0}^N S^ia^{[i]}\), then
\[
\Delta_m=\mathbf1_{2\mid m}S^mu^m(a^{[m/2]})²+
Sf²u^{m-1}B_{\lfloor(m-1)/2\rfloor}(a)².
\]
For odd m, \(\Delta_m\in SF²\) and is killed by one \(C_0\). Also \(2^k\mid n\) implies \(B_{n-1}(a)\in F^{2^k}\). These are exact algebraic labels for all rational-function inputs.

The rational harness now verifies:
- the Hasse–Taylor coefficient identities through the selected q-order;
- one-step Cartier vanishing for every odd coefficient;
- the Frobenius-power property of \(B_{n-1}\);
- the previously conjectural higher-order torsion bound as a separate exploratory check.

A useful learning task is to predict the Hasse-power level \(v_2(n)\) from the truncated Taylor-sum construction, then predict the even coefficient's Cartier root
\[
C_0(\Delta_{2n})=S^nu^na^{[n]}+Sf^2u^{n-1}B_{n-1}.
\]
The exact verifier can check these outputs symbolically. The remaining even-coefficient cancellation and the full-group residue invariance remain open; the model should help find the needed identity but cannot substitute for its proof.


## 16. Hasse–Taylor constraints as symbolic supervision

G-4cu proves two new exact targets for rational-function learning:
- every odd q-coefficient \(\Delta_m\) of the section pullback lies in \(SF²=\ker C_0\);
- if \(2^k\mid n\), the truncated Hasse sum \(B_{n-1}(a)=\sum_{i<n}S^ia^{[i]}\) is a \(2^k\)-th power.

For even \(m=2n\), the first Cartier root is
\[
C_0(\Delta_{2n})=S^nu^na^{[n]}+Sf²u^{n-1}B_{n-1}(a).
\]
This is a useful exact target for the next model, but the cancellation that would prove the full even-coefficient torsion bound is still open.

The rational verifier now checks the odd-coefficient and Hasse-power statements as theorem tests, separately from the conjectural even-coefficient bound. Training examples should label these three categories separately:
1. proved odd-coefficient exactness;
2. proved Hasse-sum Frobenius level;
3. exploratory high-order even torsion.

This prevents the model from treating the conjecture as a theorem merely because the bounded stress tests have not falsified it.


## 10. Residue-aware stable features

G-4cp identifies the pure-scaling coinvariant of each negative odd layer with the stable Cartier-residue module
\[
\mathcal R_C=
\Omega_F^1\Big/\bigcup_{n\ge1}\ker C^n
\simeq
\bigoplus_{Q\ {\rm monic\ irreducible}}
\mathbb F_{2^{\deg Q}}.
\]
A rational coefficient \(x\in F\) is encoded by the residues of
\[
\omega_x=(x/S)dS
\]
at the finite closed points Q. The residue at infinity is determined by the trace sum. This feature map is invariant under the pure-scaling coinvariant relations. Whether the full t-dependent section-change group preserves all these residue coordinates is an open exact test; do not yet treat \(\mathcal R_C\) as the certified full-group invariant space.

### Important coverage limitation

The current exact generator uses polynomial coefficients in \(\mathbb F_2[S]\). For polynomial x, \(\omega_x=(x/S)dS\) has finite poles only at Q=S, so the stable residue feature seen by this dataset is at most the single residue at S. It does not sample the residue-field coordinates at irreducible denominators \(Q\ne S\).

To train models that learn the full residue module, extend the coefficient encoder to normalized rational functions \(N(S)/D(S)\), factor D into monic irreducibles, and represent each residue in the finite field \(\mathbb F_2[S]/(Q)\). A useful exact generating family is
\[
\omega_{Q,\alpha}=\alpha(S)\frac{Q'(S)}{Q(S)}\,dS,
\qquad \alpha\bmod Q\in\mathbb F_2[S]/(Q),
\]
which has prescribed residue \(\bar\alpha\) at Q and a trace-determined residue at infinity.

### Frobenius-depth task

For \(x=a^{2^h}\), the first pure-scaling correction occurs at p-depth \(2^{h+1}r\), with coefficient \((S e^2a')^{2^h}\). The data generator now emits this target and checks it against the exact Hasse coefficient of \(x(S/(1+q))\), \(q=p^{2r}\), using Lucas' theorem for binomial coefficients. This makes the model's extrapolation task explicit: infer the first nonzero depth from the Frobenius depth h, then predict the coefficient. The test suite verifies the formula over \(\mathbb F_2[S]\), while rational-denominator residue learning remains future work.


## 11. Full-group residue invariants and rational-function data

G-4cq proves that the full finite section-change group preserves the stable Cartier-residue coordinates, including for rational parameters with poles at closed points. The proof localizes at each irreducible Q, extends the substitution to the two-dimensional local field \(k_Q((z))((p))\), and applies invariance of the top residue under continuous automorphisms.

G-4cr computes the associated-graded coinvariants:
\[
\operatorname{gr}_n(Q_{\mathcal G})\simeq
\begin{cases}
\mathcal R=\bigoplus_{Q\ {\rm monic\ irreducible}}k_Q,&n<0\text{ odd},\\
0,&n<0\text{ even},\\
F/(\wp(F)+SF^2),&n=0,\\
0,&n>0.
\end{cases}
\]
G-4ct upgrades these graded targets to the full canonical coinvariant. The invariant readout uses Frobenius-normalized sums over each exponent-doubling orbit, together with the zero-mode \(F/\wp(F)\) coordinate. There is no remaining algebraic filtered-extension cocycle to learn in the coinvariant itself; higher coordinate changes can still be studied on the original quotient before taking coinvariants.

### Rational coefficient encoder

The new exact generator tools/residue_feature_data.py creates rational functions
\[
x=\frac{S\alpha Q'}{Q}
\]
for a monic irreducible Q and a residue \(\alpha\in k_Q\). Then
\[
\frac{x}{S}dS=\alpha\frac{Q'}{Q}dS
\]
has residue \(\alpha\) at Q, and the residue at infinity is the field trace \(\operatorname{Tr}_{k_Q/\mathbb F_2}(\alpha)\). The generator stores numerator and denominator polynomials, the irreducible, the finite residue, and the trace coordinate. It uses integer bitmasks for GF(2)[S] and finite-field arithmetic modulo Q; it has no floating point or external package dependency.

Example:
\`\`\`bash
python tools/residue_feature_data.py --self-test --max-degree 5 --samples-per-point 8 > residue_train.jsonl
\`\`\`

This fills the main gap in the earlier polynomial-only dataset: it samples residue coordinates at irreducible denominators Q other than S. The tests should hold out entire irreducibles and residue-field degrees, not just random alpha values at Q already seen in training.

### Learning tasks after G-4cr

1. Predict finite-place residue vectors from normalized rational numerator/denominator input.
2. Predict the trace-determined infinity residue from the finite residue data.
3. Verify invariance of the residue vector under random full section changes with rational e,f, using the exact local two-dimensional residue check.
4. Learn the extension cocycles between surviving odd layers while preserving the known graded coinvariant readout.

The exact target is now a structured family of finite fields \(k_Q\), not a generic latent vector. This should make the feature space more interpretable and the generalization tests more stringent.


## 12. Full-group graded coinvariants and rational residue learning

G-4cq uses two-dimensional local residue invariance to prove that the entire finite section-change group preserves every stable Cartier-residue coordinate, even when the parameters e,f have poles at the closed point. G-4cr then computes the associated-graded coinvariants:
- each negative odd layer contributes \(\mathcal R=\bigoplus_Q k_Q\);
- negative even layers and negative odd second coordinates contribute zero;
- the zero layer contributes only \(F/(\wp(F)+SF^2)\);
- positive layers vanish.

G-4ct resolves the extension between the surviving graded pieces: the Frobenius-normalized orbit-residue map gives a canonical full algebraic coinvariant splitting. Higher filtered extension data for the original quotient representation (before taking coinvariants) remain a separate open learning target.

### Rational residue generator

The new standard-library script tools/residue_feature_data.py emits rational coefficients
\[
x=\frac{S\alpha Q'}{Q}
\]
and their exact finite-residue targets
\[
\operatorname{res}_Q((x/S)dS)=\alpha\pmod Q.
\]
It stores the finite-field residue in the polynomial basis of \(k_Q\), the trace-determined infinity residue, and a coprime numerator/denominator encoding. Its irreducibility test is Rabin's exact GF(2) test; all polynomial and finite-field operations use integer bitmasks.

Run:
\`\`\`bash
python tools/residue_feature_data.py --self-test --max-degree 5 --samples-per-point 8 > residue_train.jsonl
\`\`\`

An independent arithmetic check verified 14 monic irreducibles through degree five, all 52 basis residue elements across those fields, coprime rational encodings, and trace linearity. This checks the construction algebraically; it is not a neural training run.

### Updated machine-learning agenda

The immediate supervised tasks are now:
1. rational numerator/denominator to finite residue vector;
2. finite residue vector to the infinity trace;
3. exact invariance checks under rational full section changes;
4. learning the unresolved filtered extension cocycles while keeping the graded residue features fixed.

Hold out entire irreducible polynomials and residue-field degrees to test generalization beyond memorized denominators. The old polynomial-only dataset remains useful for the Cartier/Frobenius tower, but it is not enough to learn the complete finite-place residue module.


## 13. Canonical orbit-residue coordinates for all invariant linear readouts

G-4ct upgrades the graded result to the full algebraic coinvariant. For a negative exponent-doubling orbit rooted at \(-q\), q positive odd, the correct invariant is not a residue at a single exponent. It is the Frobenius-normalized orbit sum
\[
\mathfrak r_{q,Q}
=\sum_{j\ge0}\operatorname{Frob}_{k_Q}^{-j}
\operatorname{res}_Q\left(\frac{a_{-2^j q}}S\,dS\right),
\]
where \(A_n=a_n+t b_n\) is the first logarithmic coefficient at exponent n. This telescopes under \((\Phi-1)\), and it is invariant under the full section-change group by the exact coefficient-curve pullback and two-dimensional residue invariance.

The complete algebraic coinvariant is canonically
\[
Q_{\mathcal G}\simeq
F/\wp(F)\oplus
\bigoplus_{q>0\ {\rm odd}}\bigoplus_{Q\ {\rm monic\ irreducible}} k_Q.
\]
The zero summand is identified with \(F/\wp(F)\) by the p-basis map \(a=u^2+Sv^2\mapsto u\). Thus the filtered extension is no longer open: the orbit-residue map supplies a canonical splitting, not merely a noncanonical vector-space decomposition.

An invariant linear readout is any \(\mathbb F_2\)-linear functional on this direct sum. Each finite residue coordinate has the trace-dual form
\[
x\longmapsto \operatorname{Tr}_{k_Q/\mathbb F_2}(c_{q,Q}x),
\qquad c_{q,Q}\in k_Q.
\]
Because the source is an algebraic direct sum, an arbitrary algebraic linear functional may select coefficients on infinitely many coordinates; continuous/readout restrictions would impose a separate finiteness or decay condition.

### Orbit-aware data task

A residue example must now carry its exponent-orbit root q and stage j. If \(\alpha_j\in k_Q\) is the finite residue at exponent \(-2^j q\), the invariant target is
\[
\sum_j \operatorname{Frob}^{-j}(\alpha_j).
\]
Training examples should include:
- single-stage inputs;
- relation pairs \((\alpha_j,\alpha_j^2)\) at adjacent stages, whose normalized sum is zero;
- random finite orbit sequences with known normalized sum;
- full section-change perturbations whose orbit-residue target must remain fixed.

This prevents the model from confusing coefficientwise residues with the actual invariant of the Cartier quotient.


## 14. Orbit-residue sequence benchmark

The rational residue generator now emits sequences on an exponent-doubling orbit. A sample contains the odd root q, irreducible Q, finite-field residues \(\alpha_j\) at exponents \(-2^j q\), and the exact target
\[
\sum_j\operatorname{Frob}_{k_Q}^{-j}(\alpha_j).
\]
This is the canonical invariant in G-4ct. Adjacent pairs \((\alpha,\alpha^2)\) at stages j and j+1 have normalized sum zero; they are the exact training examples for the \((\Phi-1)\)-relation.

Generate rational coefficient samples and orbit sequences together:
\`\`\`bash
python tools/residue_feature_data.py --self-test --max-degree 5 --samples-per-point 8 --orbit-samples 8 --max-orbit-stages 6 > residue_orbit_train.jsonl
\`\`\`

Independent exact finite-field checks covered 1,056 adjacent-stage relation pairs over all 14 irreducibles of degree at most five. This validates the Frobenius normalization identity, not a trained model's performance.

### Final invariant-readout target

The full algebraic linear-invariant space is now dual to
\[
F/\wp(F)\oplus
\bigoplus_{q>0\ {\rm odd}}\bigoplus_{Q\ {\rm monic\ irreducible}}k_Q.
\]
For each finite residue coordinate, use the trace-pairing readout \(x\mapsto\operatorname{Tr}_{k_Q/\mathbb F_2}(c_{q,Q}x)\). The zero-mode \(F/\wp(F)\) factor uses its explicit Artin–Schreier basis. The model should predict the normalized orbit sums, not raw per-exponent residues.


## 15. Finite basis and dual-readout benchmark

The new script tools/coinvariant_basis_data.py enumerates an exact finite window in the canonical coinvariant:
\[
F/\wp(F)\oplus\bigoplus_{q>0\ {\rm odd}}\bigoplus_Q k_Q.
\]

For the zero Artin–Schreier factor it emits the standard basis elements
\[
1,\qquad S^n\ (n>0\text{ odd}),\qquad
S^j/Q^d\ (Q\text{ monic irreducible},\ d>0\text{ odd},\ 0\le j<\deg Q),
\]
with a height cutoff. For each residue block it emits the polynomial basis
\(1,\bar S,\ldots,\bar S^{m-1}\) of \(k_Q\), for each odd root q in a bounded range.

It also computes a trace-dual basis \(c_i\in k_Q\) satisfying
\[
\operatorname{Tr}_{k_Q/\mathbb F_2}(c_i\bar S^j)=\delta_{ij}.
\]
Thus every finite residue coordinate has an explicit dual invariant linear readout. The script computes this by exact Gaussian elimination on the trace Gram matrix; it verifies nondegeneracy and all duality identities.

Example finite benchmark:
\`\`\`bash
python tools/coinvariant_basis_data.py --self-test --height 5 --q-max 7 --degree-max 4 > coinvariant_basis.jsonl
\`\`\`
The cutoff has 60 zero-mode basis elements and 88 residue basis elements, for a total of 148 exact basis coordinates. The residue count is
\[
4\cdot\sum_{\deg Q\le4}\deg Q
=4(2+2+6+12)=88.
\]
The zero-mode count is 60: one constant, three positive odd powers through height five, six classes at the two linear places with three allowed odd denominator powers, two classes at the irreducible quadratic, six at the two cubics, twelve at the three quartics, and thirty at the six quintics.

The complete algebraic dual of the infinite direct sum is a product of coordinate duals. This finite benchmark supplies finite trace-dual readouts only; it does not impose a continuity condition on arbitrary algebraic functionals.


## 16. Exact GF(2) system-identification learner

The new script tools/train_orbit_residue_gf2.py learns the orbit-residue readout from examples rather than hard-coding its Frobenius matrices.

For a fixed irreducible Q of degree d and an orbit with L stages, encode the stage residues as a \(dL\)-bit input vector and the normalized orbit residue as a d-bit output. The target map is \(\mathbb F_2\)-linear. The trainer:
1. draws random orbit sequences and their exact normalized residue targets;
2. solves for each output bit's linear functional by Gaussian elimination over \(\mathbb F_2\);
3. requires full feature rank \(dL\), so the learned map is uniquely determined;
4. evaluates on independent held-out sequences;
5. verifies the learned map on every coordinate basis vector.

This is an exact symbolic system-identification baseline, not a floating-point neural-network run. It is useful as a ground-truth benchmark for later neural models.

Run:
\`\`\`bash
python tools/train_orbit_residue_gf2.py --self-test --max-degree 5 --stages 5 --train-multiplier 12 --test-count 1000
\`\`\`

An independent implementation of the same GF(2) learner recovered the exact map for all eight monic irreducibles of degree at most four, with three orbit stages, full input rank, 128 held-out sequences per field, and exact coordinate-basis checks. The committed script's self-test covers the same construction; no claim of neural generalization is made.

The next model comparison is now well-defined: the exact GF(2) learner is the oracle baseline; a neural network must match it on held-out sequences and then generalize across unseen irreducibles or larger residue degrees.


## 10. Pure-scaling tower: polynomial versus rational generalization

For the pure scaling section change \(t\mapsto t(1+p)\), the exact coefficient substitution is \(S\mapsto S/(1+p^2)\). On an odd-layer input \(a^{2^h}\), the first nonzero quotient correction occurs at offset \(2^{h+1}\), with coefficient
\[
(Sa')^{2^h}\in I_h:=S^{2^h}F^{2^{h+1}}.
\]
The successive targets are \(SF^2,S^2F^4,S^4F^8,\ldots\). The finite p-basis decomposition is exact:
\[
F=\left(\bigoplus_{h<N}I_h\right)\oplus F^{2^N}.
\]

This creates a crucial train/test distinction.

- On \(\mathbb F_2[S]\), every nonconstant monomial belongs to one \(I_h\); the quotient by the displayed tower is only \(\mathbb F_2\).
- On the full rational field \(F=\mathbb F_2(S)\), the Cartier-nonnilpotent part is nonzero. The rational coefficient \(x=S/(S+1)\) gives \((x/S)dS=d\log(S+1)\), a nonexact Cartier-fixed form.

Therefore a polynomial-only learner can incorrectly infer that the residual is one-dimensional. The benchmark must include rational denominators and Cartier-fixed logarithmic examples. A rational-function encoder should normalize numerator/denominator pairs and preserve irreducible factor and valuation data.

The tower quotient for the pure-scaling diagonal family is
\[
(\Omega_F^1/dF)/\bigcup_{h\ge1}\ker C^h.
\]
This is not yet the full coinvariant quotient for the entire section-change group. The model should predict candidate additional relations but the exact verifier must preserve this distinction.

### Benchmark extension

The generator now emits:
- Frobenius-level scaling examples for \(h=0,\ldots,4\);
- exact polynomial tower decompositions, with each monomial assigned to \(h=v_2(n)\);
- a rational Cartier-fixed challenge with \(x=S/(S+1)\) and differential \(d\log(S+1)\).

The polynomial decomposition self-test exhaustively checked all bitmasks below \(2^{12}\) in a separate verification run. The rational challenge is a symbolic witness; it is not represented as a polynomial training example.


**Correction to generator status:** the earlier 5,000-row run refers to the previous five-task generator. The current nine-task version has component-level algebraic checks documented above; do not describe the full current script as having passed an end-to-end run until that run is actually performed.

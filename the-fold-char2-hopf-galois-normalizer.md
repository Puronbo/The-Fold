# Hopf–Galois verification and translation normalizer (G-1/G-2)

## 1. The characteristic-two Hopf algebra

Let k be a field of characteristic two and
\[
A=k[x,z]/(x^4,z^2).
\]
Use the basis
\[
\mathcal B=(1,x,x^2,x^3,z,xz,x^2z,x^3z).
\]
Declare x,z primitive:
\[
\Delta(x)=x\otimes1+1\otimes x,\qquad
\Delta(z)=z\otimes1+1\otimes z,
\]
with \(\varepsilon(x)=\varepsilon(z)=0\) and \(S(x)=x,\ S(z)=z\).
The algebra map Delta respects the relations:
\[
\Delta(x)^4=x^4\otimes1+1\otimes x^4=0,\quad
\Delta(z)^2=z^2\otimes1+1\otimes z^2=0.
\]
Coassociativity and the counit identities hold on the generators, hence on all of A. The antipode identities hold on the generators and extend multiplicatively (A is commutative). Thus A is a commutative Hopf algebra, with group scheme
\[
G=\alpha_4\times\alpha_2,\qquad \operatorname{rank}(G)=8.
\]

## 2. Exact Hopf–Galois canonical map

Take H=A and the regular coaction rho=Delta. The coinvariants are k. The canonical map is
\[
\beta:A\otimes_k A\to A\otimes_k H,\qquad
a\otimes b\mapsto(a\otimes1)\Delta(b).
\]
For every Hopf algebra, its inverse is
\[
\gamma(a\otimes h)=\sum aS(h_{(1)})\otimes h_{(2)}.
\]
Indeed, the two composites reduce respectively to
\[
\sum aS(h_{(1)})h_{(2)}\otimes h_{(3)}=a\otimes h,
\quad
\sum ab_{(1)}S(b_{(2)})\otimes b_{(3)}=a\otimes b.
\]
Thus beta is an isomorphism. Since A is faithfully flat over k, Spec(A)=G is a G-torsor over Spec(k), in fact the trivial torsor with its identity section. This is a Hopf–Galois object, not a nontrivial field extension.

The independent verifier tools/fold_char2_hopf_galois.py constructs the 64-by-64 matrix of beta over F_2 in the monomial tensor basis and checks rank 64. This is a finite-field certificate in the chosen basis; the antipode identity above proves the result over every characteristic-two field.

## 3. Translation subgroup: centralizer and normalizer

For a k-algebra R, translations t_(u,v), with u^4=v^2=0, act by
\[
x\mapsto x+u,\qquad z\mapsto z+v.
\]
They form a closed subgroup scheme G in the automorphism group scheme of the underlying finite affine scheme Spec(A).

### Theorem 3.1 (centralizer)

The scheme-theoretic centralizer of G in Aut(Spec(A)) is exactly G.

**Proof.** Functorially over every characteristic-two k-algebra R, let f commute with every translation L_t. Then f composed with L_t equals L_t composed with f. Evaluating at the identity e gives f(t)=t+f(e). Thus f is translation by f(e) in G(R). Conversely, translations commute because G is commutative. The equality is functorial in R, so it identifies the centralizer group functor with G. QED.

### Theorem 3.2 (normalizer)

The scheme-theoretic normalizer is
\[
N_{\operatorname{Aut}(\operatorname{Spec}A)}(G)
\cong G\rtimes\operatorname{Aut}_{\mathrm{grp}}(G).
\]

**Proof.** If f normalizes translations, conjugation induces a group-scheme automorphism phi of G, and
\[
f\circ L_t=L_{\phi(t)}\circ f.
\]
Evaluating at e gives f(t)=phi(t)+f(e). Hence f is a translation followed by a group-scheme automorphism. Conversely, every such affine group-scheme automorphism normalizes translations. The decomposition is split by the subgroup fixing e. QED.

This identifies the normalizer in the full automorphism scheme of the underlying finite affine scheme. It does not assert that the entire Fold automorphism group is this semidirect product.

## 4. Explicit automorphism group scheme of alpha_4 x alpha_2

The primitive elements of A_R=A tensor_k R are exactly
\[
P(A_R)=Rx\oplus Rx^2\oplus Rz.
\]
A Hopf endomorphism must therefore have
\[
x\mapsto ax+bx^2+cz,\qquad
z\mapsto dx+ex^2+fz.
\]
The first image automatically has fourth power zero. The second has square d^2 x^2, so z^2=0 is preserved exactly when d^2=0. The induced map on the cotangent space m/m^2 has matrix
\[
\begin{pmatrix}a&c\\d&f\end{pmatrix}.
\]
It is invertible exactly when af-cd is a unit. Since d^2=0, this is equivalent to a,f being units. An endomorphism of this finite local algebra with invertible cotangent map is an automorphism, by Nakayama applied to the maximal-ideal filtration.

Consequently
\[
\operatorname{Aut}_{\mathrm{grp}}(G)
=\operatorname{Spec}
k[a,a^{-1},f,f^{-1},b,c,d,e]/(d^2).
\]
Its reduced dimension is five and its tangent dimension at the identity is six. In particular this automorphism group scheme is not smooth.

The normalizer is therefore the semidirect product of the rank-eight translation group scheme with this explicit, non-smooth group scheme. The centralizer is just the translation subgroup.

## 5. Imperfect-field torsors (G-4)

For a field k of characteristic two, the exact sequence of fppf sheaves
\[
0\to\alpha_{2^n}\to\mathbb G_a
\xrightarrow{F^n}\mathbb G_a^{(2^n)}\to0
\]
and H^1(k,G_a)=0 give
\[
H^1_{\mathrm{fppf}}(k,\alpha_{2^n})
\cong k/k^{2^n}.
\]
Thus
\[
H^1_{\mathrm{fppf}}(k,G)
\cong (k/k^4)\times(k/k^2).
\]
Over a perfect field this group is zero. Over an imperfect field it can be nonzero; the factors record independent fourth-power and square-power obstructions. This classifies torsors under the fixed group scheme G, not all Hopf structures or all algebra forms of A.

The same exact-sequence argument is standard for alpha_p torsors; see [On the Local Unipotent Fundamental Group Scheme](https://doi.org/10.4153/CMB-2010-033-x). The alpha_4 factor is the second Frobenius kernel and uses the identical argument with F squared.

## 6. Resolved and open directions

**Proved here**
- the primitive Hopf structure on A, giving G=alpha_4 x alpha_2;
- the Hopf–Galois canonical map and its explicit inverse;
- centralizer equals G;
- normalizer equals G semidirect Aut_grp(G);
- explicit presentation and non-smoothness of Aut_grp(G);
- fppf torsor classes H^1(k,G)=(k/k^4) x (k/k^2).

**Still open**
- classification of all Hopf structures on the underlying algebra, beyond the primitive/filtered class treated here;
- classification of all algebra forms and group-scheme twists, rather than torsors under fixed G;
- extension or degeneration of this Hopf structure over mixed-characteristic arithmetic bases;
- a global arithmetic object justifying automorphic representations, Hecke operators, or theta correspondences;
- UF-062: the rank-drop locus and exact orbit-image Hopf core for the separate normal-closure problem.

The characteristic-two Hopf–Galois track is a rigorous, independent branch of the Fold project. It does not resolve UF-062 and does not turn the full automorphism group into a finite Galois group.

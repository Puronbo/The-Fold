# Multiple Hopf structures on the characteristic-two Fold algebra (G-3)

Let k have characteristic two and
\[
A=k[x,z]/(x^4,z^2).
\]
The algebra A admits at least four pairwise non-isomorphic commutative finite group-scheme structures. The primitive Hopf structure is concrete but not unique.

## 1. Four product structures

Choose independently whether the x-coordinate and z-coordinate are additive or multiplicative.

For an additive coordinate u, set
\[
\Delta(u)=u\otimes1+1\otimes u,\quad \varepsilon(u)=0,\quad S(u)=u.
\]
For a multiplicative coordinate u, write t=1+u and impose \(\Delta(t)=t\otimes t\), \(\varepsilon(t)=1\), \(S(t)=t^{-1}\). In the truncated algebra this becomes
\[
\Delta(u)=u\otimes1+1\otimes u+u\otimes u,\quad
\varepsilon(u)=0,\quad S(u)=u+u^2+\cdots+u^{2^r-1}
\]
when \(u^{2^r}=0\). In particular,
\[
S(x)=x+x^2+x^3\quad (x^4=0),\qquad S(z)=z\quad (z^2=0).
\]
The four choices give
\[
\alpha_4\times\alpha_2,\quad
\mu_4\times\alpha_2,\quad
\alpha_4\times\mu_2,\quad
\mu_4\times\mu_2.
\]

Why the coordinate algebra is always A: in characteristic two,
\[
(1+x)^4-1=x^4,\qquad (1+z)^2-1=z^2.
\]
Hence
\[
k[t,s]/(t^4-1,s^2-1)
\cong k[x,z]/(x^4,z^2),\quad t=1+x,\ s=1+z.
\]
The same coordinate change works if only one factor is multiplicative. The group laws are products of the standard group schemes alpha_(2^r) and mu_(2^r), so the Hopf axioms follow from those standard group laws. All four schemes are finite, connected, commutative, and of rank eight.

## 2. The four structures are pairwise non-isomorphic

Use the restricted 2-power map on the Lie algebra. For an additive factor alpha_(2^r), its invariant derivation is partial_u, and (partial_u)^2=0. For a multiplicative factor mu_(2^r), use t=1+u; its invariant derivation is t partial_t, and in characteristic two
\[
(t\partial_t)^2=t\partial_t.
\]
Thus the rank of the image of the restricted 2-power map is respectively zero, one, or two according as the product has zero, one, or two multiplicative factors. This separates the additive-additive case, the two mixed cases as a pair, and the multiplicative-multiplicative case.

To distinguish the two mixed cases, use relative Frobenius. Its scheme-theoretic image is
\[
F(\mu_4\times\alpha_2)=\mu_2,\qquad
F(\alpha_4\times\mu_2)=\alpha_2.
\]
The group schemes mu_2 and alpha_2 are not isomorphic: their one-dimensional Lie algebras have different restricted 2-power maps (identity versus zero). Therefore the two mixed products are not isomorphic. This proves pairwise non-isomorphism of all four structures.

## 3. Canonical maps for all four structures

For each Hopf structure H on A, take the regular coaction rho=Delta. The canonical map
\[
\beta:A\otimes_k A\to A\otimes_k H,\qquad
a\otimes b\mapsto(a\otimes1)\Delta(b)
\]
has inverse
\[
\gamma(a\otimes h)=\sum aS(h_{(1)})\otimes h_{(2)}.
\]
Therefore each structure makes Spec(A) a trivial H-torsor over k and A a Hopf–Galois object. The extended verifier tools/fold_char2_hopf_structures.py constructs each canonical map over F_2 and checks all four matrices have rank 64.

## 4. Consequences and boundaries

1. The algebra structure alone does not determine a group law, even among finite connected commutative group schemes.
2. The four product structures already give a nontrivial finite sample of the Hopf-structure moduli problem.
3. The translation subgroup and its normalizer depend on which Hopf law is chosen. The G-2 normalizer theorem applies to each of the four group laws, but the explicit automorphism-group equations in the G-2 note are for the additive-additive law only.
4. This is not yet a classification of all Hopf structures on A. Non-product comultiplications and deformations/extensions remain to be studied.
5. The result is specific to characteristic two. These coordinate identifications do not produce the same Hopf algebras over Z.

## 5. Next classification tasks

- Determine whether every commutative Hopf structure on A over an algebraically closed field is isomorphic to one of the four product structures, or construct counterexamples.
- Classify non-product extensions of the rank-four and rank-two group schemes.
- Compute the automorphism group scheme and translation normalizer of the new non-product cocycle group.
- Study forms and twists over imperfect fields and mixed-characteristic bases.



## G-3c — A fifth, non-product Hopf structure

The same algebra also admits the coproduct
```
Delta(x) = x tensor 1 + 1 tensor x
Delta(z) = z tensor 1 + 1 tensor z + x^2 tensor x^2
```
with counit zero on x,z and antipode S(x)=x, S(z)=z. The coproduct is coassociative and preserves x^4=z^2=0. Its group law is
```
(x,z) + (x',z') = (x+x', z+z'+x^2 x'^2).
```

It is not isomorphic to any of the four product structures: its primitive space has dimension two (basis x,x^2), its relative-Frobenius image is alpha_2, and its restricted Lie 2-power map is zero. These invariants distinguish it respectively from alpha_4 x alpha_2, the two mu_4 products, and alpha_4 x mu_2.

The standard-library verifier tools/fold_char2_cocycle_hopf.py checks coassociativity, relations, counit, antipode, and primitive-space dimension exactly over F_2.

**Open G-3c:** compute its automorphism group scheme and translation normalizer; classify its torsors; and determine whether additional non-product Hopf structures exist.

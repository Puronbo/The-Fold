# Corrected normalizers of all four product Hopf structures (G-3b)

**Correction.** The first version incorrectly asserted that additive/multiplicative cross-homomorphisms vanish. That argument only checked geometric points. Over nonreduced coefficient algebras, infinitesimal cross-homomorphisms exist. They change the scheme-theoretic automorphism groups of the two mixed products. The calculations below replace the earlier mixed-case claims.

Let k have characteristic two and let A=k[x,z]/(x^4,z^2). For each product Hopf law G on Spec(A), translations satisfy
\[
C_{\operatorname{Aut}(\operatorname{Spec}A)}(G)=G,\qquad
N_{\operatorname{Aut}(\operatorname{Spec}A)}(G)
=G\rtimes\operatorname{Aut}_{\mathrm{grp}}(G).
\]
This functorial normalizer theorem is unchanged. The automorphism-group calculations are corrected as follows.

## 1. Additive-additive: alpha_4 x alpha_2

A group-scheme automorphism has
\[
x\mapsto ax+bx^2+cz,\qquad z\mapsto dx+ex^2+fz,
\]
with d²=0 and af-cd invertible. Equivalently a,f are units. Thus
\[
\operatorname{Aut}_{\mathrm{grp}}(\alpha_4\times\alpha_2)
=\operatorname{Spec}k[a^{\pm1},f^{\pm1},b,c,d,e]/(d^2).
\]
Reduced dimension five, tangent dimension six.

## 2. Multiplicative-additive: mu_4 x alpha_2

There is an infinitesimal cross-homomorphism alpha_2→mu_4. If z is the primitive coordinate on alpha_2 and t is the multiplicative coordinate on mu_4, its pullback is
\[
t\longmapsto1+r z,\qquad r^2=0.
\]
The reverse cross-homomorphism mu_4→alpha_2 is zero because O(mu_4) has no nonzero primitive elements.

Every automorphism is therefore described by
\[
(t,z)\longmapsto
\bigl(t^\epsilon(1+r z),\,s z\bigr),
\quad \epsilon\in(\mathbb Z/4)^\times=\{1,3\},\
s\in R^\times,\ r^2=0.
\]
For composition f_(epsilon,s,r) after f_(epsilon',s',r'), the parameters obey
\[
(\epsilon,s,r)(\epsilon',s',r')
=(\epsilon\epsilon',\,ss',\,r'+rs').
\]
Thus the automorphism group scheme has underlying scheme
\[
C_2\times\mathbb G_m\times\alpha_2.
\]
It has reduced dimension one and tangent dimension two. It is not smooth.

## 3. Additive-multiplicative: alpha_4 x mu_2

There is an infinitesimal cross-homomorphism alpha_4→mu_2. Write t=1+z for the multiplicative coordinate on mu_2. Its pullback along such a homomorphism is the group-like element
\[
t\longmapsto 1+p x+q x^2+pq x^3,\qquad p^2=q^2=0.
\]
Indeed, comparing Delta(g) with g tensor g for g=1+p x+q x²+r x³ gives r=pq and p²=q²=0. The reverse cross-homomorphism mu_2→alpha_4 is zero because O(mu_2) has no nonzero primitive elements.

The cross-homomorphism group scheme K is
\[
K=\operatorname{Spec}k[p,q]/(p^2,q^2).
\]
Its group law, induced by multiplication of group-like elements, is
\[
(p,q)(p',q')=(p+p',\,q+q'+pp').
\]
The diagonal automorphism group is Aut(alpha_4), whose elements are x↦a x+b x² with a a unit. Thus
\[
\operatorname{Aut}_{\mathrm{grp}}(\alpha_4\times\mu_2)
\cong \operatorname{Aut}(\alpha_4)\ltimes K
\]
(up to the equivalent opposite convention for the semidirect action). The scheme has reduced dimension two and tangent dimension four. It is not smooth.

For reference, composition of the alpha_4 automorphisms x↦a x+b x² and x↦a' x+b' x² has coefficients
\[
(a,b)(a',b')=(aa',\,ab'+ba'^2)
\]
in the point-map convention.

## 4. Multiplicative-multiplicative: mu_4 x mu_2

This is D(M) for M=Z/4⊕Z/2. Its automorphism group is the constant group Aut(M). The automorphisms are represented by
\[
\begin{pmatrix}a&c\\b&1\end{pmatrix},
\quad a\in\{1,3\},\ b\in\{0,1\},\ c\in\{0,2\},
\]
with the first row modulo four and second row modulo two. There are eight elements, with two elements of order four and five nonidentity involutions. Hence
\[
\operatorname{Aut}_{\mathrm{grp}}(\mu_4\times\mu_2)\cong D_8
\]
as a constant finite étale group scheme.

## 5. Corrected normalizer summary

\[
\begin{array}{c|c|c}
G & \operatorname{Aut}_{\mathrm{grp}}(G) &
(\dim_{\mathrm{red}},\dim_{\mathrm{tan}})\\
\hline
\alpha_4\times\alpha_2 &
\operatorname{Spec}k[a^{\pm1},f^{\pm1},b,c,d,e]/(d^2) &(5,6)\\
\mu_4\times\alpha_2 &
C_2\times\mathbb G_m\times\alpha_2 &(1,2)\\
\alpha_4\times\mu_2 &
\operatorname{Aut}(\alpha_4)\ltimes K &(2,4)\\
\mu_4\times\mu_2 & D_8 &(0,0)
\end{array}
\]
For each row, the translation centralizer is G and the normalizer is G semidirect the displayed automorphism group scheme.

The key lesson is scheme-theoretic: checking homomorphisms only over fields misses nilpotent cross-homomorphisms. The mixed-case automorphism group schemes are non-smooth even though their geometric-point cross-homomorphisms are trivial.

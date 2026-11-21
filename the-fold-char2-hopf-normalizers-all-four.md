# Normalizers of all four product Hopf structures (G-3b)

Let k have characteristic two and let the common underlying algebra be
\[
A=k[x,z]/(x^4,z^2).
\]
For each of the four product Hopf structures from G-3, write G for its group scheme and let G act on itself by translations.

The general translation-normalizer theorem gives
\[
C_{\operatorname{Aut}(\operatorname{Spec}A)}(G)=G,\qquad
N_{\operatorname{Aut}(\operatorname{Spec}A)}(G)
=G\rtimes\operatorname{Aut}_{\mathrm{grp}}(G).
\]
The following computes the four automorphism groups.

## 1. Additive-additive: alpha_4 x alpha_2

The primitive elements are spanned by x,x²,z. A group-scheme automorphism has
\[
x\mapsto ax+bx^2+cz,\qquad z\mapsto dx+ex^2+fz,
\]
with d²=0 and af-cd invertible. Since d is nilpotent, this is equivalent to a,f being units. Thus
\[
\operatorname{Aut}_{\mathrm{grp}}(\alpha_4\times\alpha_2)
=\operatorname{Spec}k[a^{\pm1},f^{\pm1},b,c,d,e]/(d^2).
\]
Its reduced dimension is five and tangent dimension six.

## 2. Multiplicative-additive: mu_4 x alpha_2

There are no nontrivial homomorphisms between a multiplicative-type factor mu_4 and an additive factor alpha_2. In coordinates, this follows because the additive coordinate algebra has no nontrivial group-like elements and the multiplicative coordinate algebra has no nonzero primitive elements. Therefore every automorphism is block diagonal.

Since mu_4=D(Z/4), its automorphism group is the constant group Aut(Z/4)≅C2. Since Aut(alpha_2)=G_m, we get
\[
\operatorname{Aut}_{\mathrm{grp}}(\mu_4\times\alpha_2)
\cong C_2\times\mathbb G_m.
\]
It is smooth of dimension one.

## 3. Additive-multiplicative: alpha_4 x mu_2

Again the cross-homomorphisms vanish, so automorphisms are block diagonal. The group mu_2=D(Z/2) has trivial automorphism group. The primitive elements of O(alpha_4)=k[x]/x^4 are kx⊕kx², so
\[
x\mapsto ax+bx^2,\qquad a\in R^\times,\ b\in R
\]
describes every automorphism of alpha_4. Thus
\[
\operatorname{Aut}_{\mathrm{grp}}(\alpha_4\times\mu_2)
\cong\operatorname{Aut}_{\mathrm{grp}}(\alpha_4),
\]
a smooth two-dimensional group scheme. Its multiplication in the displayed coordinates is
\[
(a,b)(a',b')=(aa',\,a'b+b'a^2).
\]

## 4. Multiplicative-multiplicative: mu_4 x mu_2

This is the diagonalizable group D(M), with M=Z/4⊕Z/2. Its group-scheme automorphism group is the constant group Aut(M). An automorphism is represented on M by
\[
\begin{pmatrix}a&c\\b&1\end{pmatrix},
\quad a\in\{1,3\},\quad b\in\{0,1\},\quad c\in\{0,2\},
\]
where the first row is read modulo four and the second modulo two. There are eight such matrices. Exactly two have order four and five nonidentity elements have order two, so this group is the dihedral group D8 of order eight. Therefore
\[
\operatorname{Aut}_{\mathrm{grp}}(\mu_4\times\mu_2)\cong D_8
\]
as a constant finite étale group scheme.

## 5. Four normalizers

Combining the four calculations with the translation-normalizer theorem:
\[
\begin{array}{c|c|c}
G & \operatorname{Aut}_{\mathrm{grp}}(G) & N(G)\\
\hline
\alpha_4\times\alpha_2 &
\operatorname{Spec}k[a^{\pm1},f^{\pm1},b,c,d,e]/(d^2) &
G\rtimes\operatorname{Aut}(G)\\
\mu_4\times\alpha_2 & C_2\times\mathbb G_m & G\rtimes(C_2\times\mathbb G_m)\\
\alpha_4\times\mu_2 & \operatorname{Aut}(\alpha_4) & G\rtimes\operatorname{Aut}(\alpha_4)\\
\mu_4\times\mu_2 & D_8 & G\rtimes D_8
\end{array}
\]
For all four, the centralizer of translations is exactly G.

These are normalizers inside the automorphism group scheme of the common underlying finite affine scheme. They are not assertions that the full automorphism group of A is exhausted by these normalizers.

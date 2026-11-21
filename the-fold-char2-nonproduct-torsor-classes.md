# Fppf torsors of the two non-product Fold Hopf structures

Let k be a field of characteristic two and A=k[x,z]/(x^4,z^2).

## Theorem 1. Cohomology of the additive Frobenius kernels

For n=1,2, the fppf exact sequence
\[
0\longrightarrow\alpha_{2^n}\longrightarrow\mathbb G_a
\xrightarrow{F^n}\mathbb G_a^{(2^n)}\longrightarrow0
\]
and the acyclicity of quasi-coherent \(\mathbb G_a\) on \(\operatorname{Spec}k\) give
\[
H^1(k,\alpha_2)=k/k^2,\qquad
H^1(k,\alpha_4)=k/k^4,
\]
and
\[
H^q(k,\alpha_2)=H^q(k,\alpha_4)=0\qquad(q\ge2).
\]
In particular, both possible obstruction groups in the extension sequences below vanish.

## Theorem 2. Torsors under \(G_C\)

Give A the Hopf law
\[
\Delta(x)=x\otimes1+1\otimes x,\qquad
\Delta(z)=z\otimes1+1\otimes z+x^2\otimes x^2.
\]
The coordinate projection \(G_C\to\alpha_4\) given by x has kernel \(\alpha_2\), with coordinate z. Thus
\[
0\longrightarrow\alpha_2\longrightarrow G_C
\longrightarrow\alpha_4\longrightarrow0
\]
is an exact sequence of commutative fppf sheaves.

The associated cohomology sequence and Theorem 1 give
\[
0\longrightarrow k/k^2
\longrightarrow H^1(k,G_C)
\longrightarrow k/k^4
\longrightarrow0.
\]
The left map is injective because \(\alpha_4(k)=0\): a field has no nonzero element whose fourth power is zero. The right map is surjective because \(H^2(k,\alpha_2)=0\).

The group \(G_C\) is killed by two: its group law is
\[
(x,z)+(x',z')=(x+x',z+z'+x^2x'^2),
\]
so doubling gives \((0,0)\). Therefore \(H^1(k,G_C)\) is an \(\mathbb F_2\)-vector space, and the short exact sequence splits noncanonically. In particular, as abstract groups,
\[
H^1(k,G_C)\cong (k/k^2)\oplus(k/k^4).
\]

## Theorem 3. Torsors under \(G_D\)

Give A the Hopf law
\[
\Delta(x)=x\otimes1+1\otimes x+z\otimes z,\qquad
\Delta(z)=z\otimes1+1\otimes z.
\]
The coordinate projection \(G_D\to\alpha_2\) given by z has kernel \(\alpha_4\), with coordinate x. Thus
\[
0\longrightarrow\alpha_4\longrightarrow G_D
\longrightarrow\alpha_2\longrightarrow0
\]
is exact.

The cohomology sequence gives
\[
0\longrightarrow k/k^4
\longrightarrow H^1(k,G_D)
\longrightarrow k/k^2
\longrightarrow0.
\]
Injectivity on the left follows from \(\alpha_2(k)=0\), and surjectivity on the right follows from \(H^2(k,\alpha_4)=0\).

The group \(G_D\) is killed by two because
\[
(x,z)+(x,z)=(z^2,0)=(0,0).
\]
Consequently the sequence splits noncanonically as an \(\mathbb F_2\)-vector-space sequence:
\[
H^1(k,G_D)\cong (k/k^4)\oplus(k/k^2)
\]
as an abstract group.

## 4. What this does and does not classify

The result determines the abstract fppf torsor-class groups for these two fixed Hopf structures over every characteristic-two field. It does not give a canonical splitting, a preferred pair of representatives for each torsor, or a classification of the Hopf structures themselves.

It is noteworthy that \(G_C\), \(G_D\), and the product \(\alpha_4\times\alpha_2\) have abstractly isomorphic fppf \(H^1\)-groups over every such field, although the underlying group schemes are pairwise non-isomorphic. Thus \(H^1(k,-)\) as an abstract group does not distinguish these Hopf structures.

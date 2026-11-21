# Fppf torsors under the non-product cocycle group (G-3e/G-4)

Let G_C be the non-product group scheme with
\[
\Delta(x)=x\otimes1+1\otimes x,\qquad
\Delta(z)=z\otimes1+1\otimes z+x^2\otimes x^2.
\]
Projection to x and inclusion of the z-axis give an exact sequence of commutative fppf sheaves
\[
0\longrightarrow\alpha_2\longrightarrow G_C
\longrightarrow\alpha_4\longrightarrow0.
\]
The group scheme is killed by 2.

## 1. Cohomology exact sequence

Over a field k of characteristic two,
\[
H^1(k,\alpha_2)=k/k^2,\qquad
H^1(k,\alpha_4)=k/k^4.
\]
Also \(H^2_{\mathrm{fppf}}(k,\alpha_2)=0\): use
\(0\to\alpha_2\to\mathbb G_a\xrightarrow{F}\mathbb G_a\to0\)
and the vanishing of positive-degree fppf cohomology of the quasi-coherent sheaf \(\mathbb G_a\) on the affine scheme Spec(k).

Since \(\alpha_4(k)=0\) for a field, the long exact sequence yields
\[
0\longrightarrow k/k^2
\longrightarrow H^1_{\mathrm{fppf}}(k,G_C)
\longrightarrow k/k^4
\longrightarrow0.
\]
Because G_C is commutative and killed by 2, its H^1 is an \(\mathbb F_2\)-vector space. The short exact sequence therefore splits noncanonically as a sequence of abstract \(\mathbb F_2\)-vector spaces. In particular, abstractly
\[
H^1_{\mathrm{fppf}}(k,G_C)\cong(k/k^2)\oplus(k/k^4),
\]
but no canonical splitting is asserted.

## 2. Explicit torsor representatives

For any \(a,b\in k\), define
\[
B_{a,b}=k[u,v]/(u^4-a,\ v^2-b).
\]
Give it the right G_C-coaction
\[
\rho(u)=u\otimes1+1\otimes x,\qquad
\rho(v)=v\otimes1+1\otimes z+u^2\otimes x^2.
\]
The relations are preserved:
\[
\rho(u)^4=a,\qquad
\rho(v)^2=b,
\]
because \(x^4=z^2=0\) and \(u^4=a\).

The canonical map
\[
\beta:B_{a,b}\otimes_kB_{a,b}\to B_{a,b}\otimes_k k[G_C]
\]
is an isomorphism. To see this, denote the two copies of the torsor coordinates by \(u_1,v_1\) and \(u_2,v_2\). Under beta,
\[
u_1\mapsto u,\quad v_1\mapsto v,\quad
u_2\mapsto u+x,\quad
v_2\mapsto v+z+u^2x^2.
\]
The inverse is given by
\[
x\mapsto u_1+u_2,\qquad
z\mapsto v_1+v_2+u_1^2(u_1+u_2)^2,
\]
together with u↦u_1 and v↦v_1. These substitutions respect the relations since \(u_1^4=u_2^4=a\) and \(v_1^2=v_2^2=b\). Thus B_{a,b} is a finite faithfully flat G_C-torsor of rank eight.

The family B_{a,b} realizes lifts of the alpha_4-torsors \(u^4=a\); varying b moves through the kernel \(H^1(k,\alpha_2)=k/k^2\). After choosing representatives of classes in k/k^4, it gives a set-theoretic parameterization of all G_C-torsor classes. The abstract group splitting remains noncanonical.

## 3. Perfect and imperfect fields

If k is perfect, k/k² and k/k⁴ vanish, so every G_C-torsor is trivial.

If k is imperfect, these quotients may be nonzero. Over k=F_2(t), for example, t is neither a square nor a fourth power, giving nontrivial classes in both ends of the exact sequence.

This computes the fppf torsor classes of the fifth, non-product Hopf structure. It does not classify all Hopf structures on A or all forms of G_C.

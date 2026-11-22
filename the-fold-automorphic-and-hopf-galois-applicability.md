# Applicability audit — automorphic methods and Galois theory for the Fold algebra

## 1. Scope of the external note

The four-page note at https://alpo.ge/remark.pdf announces a proposed proof strategy for RH and GRH. It describes a mixture of Stepanov-style determinant/multiplicity arguments, Fourier analysis and iterated Parseval, theta lifts, automorphic representations on unitary groups, GGP-type periods, relative trace formulas, arithmetic divisibility, and Iwasawa towers. It also says a Lean formalization is available in multipart archives.

This document is a research announcement and compressed roadmap, not the proof itself. The PDF does not supply enough definitions, lemmas, or formalization details to audit the RH/GRH claims. No claim about the correctness of that proposed proof is made here.

A terminology distinction matters: *automorphic* in the PDF refers to automorphic forms and representations of arithmetic groups. The Fold work studies algebra automorphisms and their group schemes. These are related broad mathematical themes, but the words do not indicate the same structure.

## 2. What transfers to the Fold project?

The most plausible points of contact are structural, not a direct import of the analytic number theory.

- **Determinants and multiplicity.** The Fold program already studies multiplication matrices, trace forms, discriminants, and determinant-open automorphism loci. Determinant identities and rank/multiplicity methods can be useful for exact algebraic calculations. This is a methodological overlap, not a transfer of the PDF's RH argument.
- **Group actions and representations.** The automorphism group scheme acts on the algebra and its tensor powers. Its representations, invariant rings, and covariants are natural objects. This is closer to algebraic representation theory than to automorphic representation theory.
- **Integral and modular structures.** The Fold algebra is defined over Z and has distinctive characteristic-two behavior. Integral lattices, reduction modulo primes, and changes in symmetry across characteristics are directly relevant. The PDF's arithmetic emphasis suggests useful questions, but its Iwasawa and theta-lift machinery needs additional arithmetic input not present in the finite algebra alone.
- **Trace and pairing structures.** The multiplication trace pairing and Frobenius pairing already studied for the Fold can be used to investigate duality, adjoints, and invariant bilinear forms. These could become representation-theoretic data for the automorphism group scheme.

There is presently no natural adelic group, Hecke algebra, automorphic representation, theta correspondence, or global period integral attached to the finite Fold algebra alone. To use those tools one would first need a meaningful arithmetic family or global object carrying such structures. Thus the PDF's main analytic/automorphic engine is not directly applicable on the current data.

## 3. Classical Galois theory: why it is not the right first language

The rank-eight Fold algebra
\[
C_{\mathbb Z}=\mathbb Z[x,y]/(x^2+y^2,x^2y^2)
\]
is not a finite étale algebra: it contains nilpotents (for example, x⁴=0). Classical finite Galois theory is built around finite separable/étale algebras and their finite étale symmetry groups. Consequently, the ordinary field-extension Galois correspondence does not directly describe this algebra.

The existing group scheme \(\operatorname{Aut}(C)\) is still meaningful and is already central to the project. The natural extensions are:

1. finite group-scheme actions and torsors;
2. Hopf algebras and Hopf–Galois extensions;
3. descent and faithfully flat cohomology;
4. group-scheme cohomology and representations;
5. arithmetic forms and twists over non-algebraically-closed base rings/fields.

These retain the symmetry/descent spirit of Galois theory without falsely treating the Fold algebra as a separable field extension.

## 4. A concrete characteristic-two Hopf–Galois structure

In characteristic two, put z=x+y. Then
\[
C_k\cong k[x,z]/(x^4,z^2).
\]
There is a natural Hopf algebra structure declaring x and z primitive:
\[
\Delta(x)=x\otimes1+1\otimes x,\qquad
\Delta(z)=z\otimes1+1\otimes z,
\]
\[
\varepsilon(x)=\varepsilon(z)=0,\qquad
S(x)=x,\quad S(z)=z.
\]
The relations are preserved because in characteristic two
\[
\Delta(x)^4=x^4\otimes1+1\otimes x^4=0,
\quad
\Delta(z)^2=z^2\otimes1+1\otimes z^2=0.
\]
Thus this is the coordinate Hopf algebra of
\[
G=\alpha_4\times\alpha_2,
\]
a finite connected commutative group scheme of rank 4·2=8.

The regular translation coaction makes A=C_k a Hopf–Galois object over k. Explicitly, with H=A and coaction rho=Delta, the canonical map
\[
\beta:A\otimes_k A\longrightarrow A\otimes_k H,
\qquad
a\otimes b\longmapsto (a\otimes1)\Delta(b)
\]
is an isomorphism; its inverse is
\[
a\otimes h\longmapsto
\sum aS(h_{(1)})\otimes h_{(2)}.
\]
The coinvariants are k. Equivalently, Spec(A) is a torsor under G over Spec(k).

This group scheme acts on itself by translations. On coordinate functions the action has the form
\[
x\longmapsto x+c,\qquad z\longmapsto z+d,
\qquad c^4=d^2=0.
\]
It therefore embeds as a rank-eight finite subgroup scheme of the already computed characteristic-two algebra automorphism group scheme. It is the h=0 translation subgroup in the ambient substitution coordinates.

This is a concrete Galois-theoretic structure on the Fold algebra, not merely an analogy.

## 5. Important limitations

- The Hopf structure above is characteristic-two-specific. The primitive formulas for x and z use the relations x⁴=z²=0 in characteristic two; they do not give an immediate Hopf structure on the original integral algebra over Z.
- The existence of this Hopf structure does not identify the full automorphism group scheme with G. The translation group scheme is only a finite subgroup of the much larger automorphism group scheme.
- Other Hopf structures may exist. Their classification is a separate problem.
- A Hopf–Galois structure over a field does not by itself produce a classical Galois extension or an automorphic representation.

## 6. Involutions and Galois modules in characteristic two

There is an important representation-theoretic caveat whenever an order-two symmetry is used over a characteristic-two base. Let (V) be a (k)-vector space, ({\rm char}(k)=2), and let (J\in\operatorname{GL}(V)) satisfy (J^2=1). Put (N=J-1). Then
[
N^2=(J-1)^2=J^2-2J+1=0.
]
Conversely, every square-zero endomorphism (N) defines an involution (J=1+N). Thus a representation of the constant group (C_2) in characteristic two is equivalently a module over
[
k[C_2]\cong k[\epsilon]/(\epsilon^2),\qquad \epsilon\mapsto J-1.
]

The canonical filtration is
[
0\subseteq\operatorname{im}(J-1)
\subseteq\ker(J-1)\subseteq V,
]
and there is an exact sequence
[
0\longrightarrow\ker(J-1)\longrightarrow V
\xrightarrow{\ J-1\ }\operatorname{im}(J-1)
\longrightarrow0.
]
The induced action of (J) is trivial on both the submodule \(\ker(J-1)\) and the quotient \(V/\ker(J-1)\). In general there is no canonical decomposition into plus and minus eigenspaces: the projectors \((1\pm J)/2\) do not exist, and \(J-1\) can be nonzero. The smallest nontrivial example is the two-dimensional module with (N(e_2)=e_1), (N(e_1)=0).

This gives a concrete characteristic-two replacement for the usual eigenspace method in any Galois or automorphism-group representation attached to the Fold algebra. One should compute the square-zero operator, its image/kernel filtration, and the associated extension class rather than assume semisimplicity. This statement concerns representations of the constant group (C_2); for a general profinite Galois group, it applies after restriction to an order-two subgroup when such a subgroup is present.

## 7. Recommended research programme

**G-1.** Verify the characteristic-two Hopf structure and the canonical Hopf–Galois map by an exact algebraic verifier.

**G-2.** Determine the normalizer and centralizer of the translation subgroup \(\alpha_4\times\alpha_2\) inside \(\operatorname{Aut}(C_k)\), and compare them with the already computed automorphism group scheme.

**G-3.** Classify Hopf algebra structures on the underlying algebra k[x,z]/(x⁴,z²), at least among those with primitive or filtered generators.

**G-4.** Study forms and twists of this Hopf algebra over imperfect fields and over arithmetic base rings, including the role of Frobenius and faithfully flat cohomology.

**G-5.** Only after identifying a meaningful arithmetic family should one revisit automorphic methods. Potential targets would be representations of a global symmetry group, Hecke operators, or theta correspondences; none is currently canonically supplied by the finite algebra.

## 8. Bottom line

The PDF's theta-lift/automorphic RH framework is not directly applicable to the Fold algebra as presently defined. Its determinant, representation, and integral-structure themes do suggest methodological parallels.

Galois theory, in its group-scheme and Hopf–Galois forms, is much more directly applicable. In characteristic two the Fold algebra itself is naturally the coordinate algebra of \(\alpha_4\times\alpha_2\), and its translation action gives an explicit rank-eight Hopf–Galois torsor structure. This is a concrete new direction worth developing independently of the PDF's RH/GRH claims.

## 7. Cohomology of an order-two Galois quotient in characteristic two

The square-zero operator above also computes the cohomology of the order-two quotient exactly. Let (L/K) be a separable quadratic Galois extension in characteristic two, let
\[
\Gamma=\operatorname{Gal}(L/K)=\langle\sigma\mid\sigma^2=1\rangle\cong C_2,
\]
and let (V) be a finite-dimensional discrete (k[Gamma])-module, where (k) has characteristic two. Put (N=\sigma-1). Then (N^2=0), and the norm operator is
\[
1+\sigma=\sigma-1=N.
\]
The standard two-periodic resolution of the trivial (k[C_2])-module therefore has every positive differential equal to (N). Consequently,
\[
H^0(C_2,V)=\ker N,\qquad
H^q(C_2,V)=\ker N/\operatorname{im}N\quad(q\ge1).
\]
In particular, all positive-degree cohomology groups are canonically the same quotient as vector spaces. If (r=\operatorname{rank}_kN) and (m=\dim_kV), then
\[
\dim_kH^q(C_2,V)=m-2r\quad(q\ge1).
\]
This follows because (\operatorname{im}N\subseteq\ker N), with dimensions (r) and (m-r), respectively. Thus the non-semisimple part of the involution is measured by (r), while the residual quotient (\ker N/\operatorname{im}N) measures the cohomology in every positive degree.

The operator also gives the complete finite-dimensional module classification. Choose a basis of \(\operatorname{im}N\), lift it to vectors \(v_i\) with \(Nv_i=u_i\), and choose a complement \(W\) of \(\operatorname{im}N\) in \(\ker N\). Then
\[
V\cong k[C_2]^r\oplus k^{m-2r},
\]
where each regular summand is a two-dimensional Jordan block and the remaining summand has trivial action. This decomposition is unique up to isomorphism, though the chosen bases and complements are not canonical. Thus the positive-degree cohomology has dimension equal to the number of trivial Jordan blocks.

There is also a direct bridge to the absolute Galois group. Write (G_K=\operatorname{Gal}(K^{\mathrm{sep}}/K)), (G_L=\operatorname{Gal}(K^{\mathrm{sep}}/L)), and assume the (G_K)-action on (V) is continuous. Inflation–restriction gives the exact segment
\[
0\to H^1(C_2,V^{G_L})
\to H^1(G_K,V)
\to H^1(G_L,V)^{C_2}
\xrightarrow{\mathrm{tr}} H^2(C_2,V^{G_L}).
\]
The end term is explicitly
\[
H^2(C_2,V^{G_L})
=\ker(N|_{V^{G_L}})/\operatorname{im}(N|_{V^{G_L}}).
\]
Hence the obstruction to descending a (G_L)-cohomology class invariant under the quotient involution is represented by this concrete square-zero quotient. This is a precise Galois-cohomological interface; it does not compute the global groups (H^1(G_K,V)) or (H^1(G_L,V)) without additional arithmetic information.

In characteristic two, every separable quadratic extension is Artin–Schreier: it can be written (L=K(\theta)) with (\theta^2-\theta=a\in K), and its nontrivial automorphism sends (\theta\mapsto\theta+1). Thus this calculation applies to the order-two quotient attached to any such extension. It does not say that an arbitrary profinite Galois representation factors through (C_2); it applies to the restriction/quotient sequence just specified.

### G-7 — Exact order-two cohomology and descent obstruction

The preceding formulas give a finite, checkable invariant for each quadratic Galois quotient: compute (N=\sigma-1) on (V^{G_L}), then compute (\ker N/\operatorname{im}N). Its dimension is (\dim V^{G_L}-2\operatorname{rank}N). This quotient is the target of the inflation–restriction transgression. For Fold representations, the next concrete task is to construct natural (G_K)-modules from the automorphism-group-scheme or Hopf–Galois data and evaluate this obstruction; no such global representation or arithmetic class is asserted here.


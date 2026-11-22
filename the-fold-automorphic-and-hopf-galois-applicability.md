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



## 8. Cyclic (2)-power Galois quotients

The order-two calculation extends to every cyclic quotient of order (q=2^n). Let (L/K) be a finite cyclic Galois extension in characteristic two, with
\[
\Gamma=\operatorname{Gal}(L/K)=\langle\sigma\rangle\cong C_q,
\]
and let (V) be a finite-dimensional (k[\Gamma]\)-module. Put (D=\sigma-1). In characteristic two,
\[
k[C_q]\cong k[D]/(D^q),\qquad
\mathsf{Norm}=1+\sigma+\cdots+\sigma^{q-1}=D^{q-1}.
\]
Indeed, writing \(\sigma=1+D\), the geometric sum is \(((1+D)^q-1)/D=D^{q-1}\), since \((1+D)^q=1+D^q\).

The standard two-periodic cyclic resolution therefore yields
\[
H^{2j+1}(C_q,V)=\ker(D^{q-1})/\operatorname{im}D,
\qquad
H^{2j+2}(C_q,V)=\ker D/\operatorname{im}(D^{q-1})
\quad(j\ge0).
\]
Write the nilpotent Jordan decomposition of (D) as a direct sum of blocks of lengths (1\le d\le q). On a block of length (d<q), (D^{q-1}=0), so each displayed quotient has dimension one. On a block of length (q), both quotients vanish: (\ker D^{q-1}=\operatorname{im}D), and (\ker D=\operatorname{im}D^{q-1}). Additivity gives the compact formula
\[
\boxed{\dim_k H^j(C_q,V)
=\#\{\text{Jordan blocks of }D\text{ with length }<q\},
\quad j\ge1.}
\]
Equivalently, positive-degree cohomology detects precisely the non-projective indecomposable summands; the length-(q) blocks are free (k[C_q])-modules and contribute no cohomology. This recovers G-7 at (q=2).

For the absolute Galois sequence (1\to G_L\to G_K\to C_q\to1), inflation–restriction gives
\[
0\to H^1(C_q,V^{G_L})\to H^1(G_K,V)
\to H^1(G_L,V)^{C_q}
\xrightarrow{\mathrm{tr}} H^2(C_q,V^{G_L}).
\]
Thus the obstruction to descending an invariant class is measured by the explicitly computable (H^2) quotient above, applied to (V^{G_L}). In characteristic two, cyclic (2)-power extensions are described by Artin–Schreier–Witt theory. This gives a family of finite quotient tests, but still does not construct a global Fold Galois module or evaluate a specific arithmetic transgression.

### G-8 — Cyclic (2)-power cohomology and projective-block detection

For a cyclic Galois quotient (C_{2^n}), the operator (D=\sigma-1) is nilpotent of order at most (2^n). The norm is (D^{2^n-1}), so positive cohomology in every degree has dimension equal to the number of Jordan blocks of length strictly less than (2^n). The maximal-length blocks are exactly the free/projective (k[C_{2^n}])-summands. This refines the quadratic G-7 criterion. The remaining Fold-specific task is to construct natural global modules and compute their Jordan block profiles and descent transgressions.
\n

### G-9 — Jordan-chain representatives for cyclic (2)-power cohomology

Let \(q=2^n\), \(k\) have characteristic two, and \(D=\sigma-1\) on a finite-dimensional \(k[C_q]\)-module \(V\). Choose a Jordan-chain decomposition into blocks \(J_d\), with basis \(e_0,\ldots,e_{d-1}\), \(De_0=0\), and \(De_j=e_{j-1}\) for \(j>0\). For a block of length \(d<q\), its contribution to \(H^1(C_q,V)=\ker D^{q-1}/\operatorname{im}D\) is represented by the top vector \(e_{d-1}\); its contribution to \(H^2(C_q,V)=\ker D/\operatorname{im}D^{q-1}\) is represented by the bottom vector \(e_0\). A length-\(q\) block contributes zero: the top vector lies in \(\operatorname{im}D\), and the bottom vector equals \(D^{q-1}e_{q-1}\), hence is a norm.

Thus, after choosing Jordan chains, the short-block top vectors form a basis of \(H^1\), and the short-block bottom vectors form a basis of \(H^2\). This is a representative-level refinement of G-8, not merely a dimension count. In a Galois extension \(1\to G_L\to G_K\to C_q\to1\), it identifies coordinates in the target \(H^2(C_q,V^{G_L})\) in which a transgression must be evaluated. It does not compute that transgression without an explicit extension, module action, and invariant cohomology class.

### G-10 — Cochain-level Hochschild–Serre transgression

For an exact sequence \(1\to N\to G\xrightarrow{\pi}Q\to1\) and a \(G\)-module \(V\), put \(W=V^N\). Let \([\alpha]\in H^1(N,V)^Q\), represented by a 1-cocycle \(\alpha:N\to V\). The transgression is computed by extending \(\alpha\) to a 1-cochain \(\beta:G\to V\) and taking its coboundary. In the standard cochain construction, invariance of \([\alpha]\) permits the extension to be chosen so that \(d\beta\) descends to a 2-cocycle on \(Q\) with values in \(W\); its class is \(d_2([\alpha])\in H^2(Q,W)\). The representative depends on choices, but the cohomology class does not. This is the explicit cochain description of the Hochschild–Serre transgression.

For \(Q=C_q\) in characteristic two, G-8 computes the target as \(\ker D/\operatorname{im}D^{q-1}\), and G-9 supplies Jordan-chain representatives for its classes. Thus an actual arithmetic computation has a finite endpoint: construct \(\alpha\), perform the cochain extension and coboundary calculation, then reduce the resulting invariant vector modulo the norm image. No Fold-specific \(N,G,V,\alpha\) has yet been constructed, so no numerical transgression is claimed.

### G-11 — Cyclic cocycle sum and the explicit obstruction vector

Let \(Q=C_q=\langle\sigma\rangle\) act on \(W\), and let \(\tau:Q\times Q\to W\) be a normalized inhomogeneous 2-cocycle. In the extension represented by \(\tau\), use the multiplication convention
\[
(w,g)(w',g')=(w+g w'+\tau(g,g'),gg').
\]
The q-th power of the lift \((0,\sigma)\) is
\[
(w_\tau,1),\qquad
w_\tau=\sum_{j=0}^{q-1}\tau(\sigma^j,\sigma).
\]
Associativity implies \(w_\tau\in W^Q\); changing the lift changes it by a norm. Under the standard cyclic identification, the class of \(\tau\) in \(H^2(C_q,W)\) is therefore represented by \(w_\tau\in W^Q/N_QW\).

In characteristic two with \(q=2^n\), the norm is \(D^{q-1}\), where \(D=\sigma-1\). Thus after constructing the G-10 quotient cocycle, sum its q consecutive values, verify \(Dw_\tau=0\), and reduce modulo \(\operatorname{im}D^{q-1}\). In a Jordan basis this reads off exactly the coefficients on bottom vectors of blocks of length less than q. This supplies a direct representative-level vanishing test for the transgression. The formula depends on the stated inhomogeneous cocycle convention; changing convention changes the displayed cocycle formula accordingly.

This is a general cyclic-cohomology computation, not yet an arithmetic evaluation for the Fold: a concrete Galois extension, coefficient module, and invariant class remain necessary.

### G-12 — Explicit cyclic quartic test extension and coefficient modules

Let \(K=\mathbb F_2(s)\) and
\[
L=K(u,w),\qquad u^2+u=s,\qquad w^2+w=u^3+u.
\]
The first equation gives \(K(u)=\mathbb F_2(u)\). The rational function \(u^3+u\) has a pole of odd order three at infinity, whereas every pole of \(r^2+r\) has even order. Thus the second Artin–Schreier equation is nontrivial and \([L:K]=4\).

The assignments
\[
\sigma(u)=u+1,\qquad \sigma(w)=w+u+1
\]
preserve the equations: \((u+1)^3+(u+1)=(u^3+u)+(u^2+u)\), and \((u+1)^2+(u+1)=u^2+u\). They satisfy \(\sigma^2(u)=u\), \(\sigma^2(w)=w+1\), so \(\sigma\) has order four and \(\operatorname{Gal}(L/K)=C_4\).

Two coefficient modules give a useful contrast. By the normal basis theorem, the additive \(K[C_4]\)-module \(L\) is regular, hence free/projective; its positive-degree group cohomology vanishes. In contrast, for the trivial module \(V=\mathbb F_2\), the operator \(D=\sigma-1\) is zero and the norm \(D^3\) is zero, so
\[
H^1(C_4,\mathbb F_2)=H^2(C_4,\mathbb F_2)=\mathbb F_2.
\]
This explicitly demonstrates why the coefficient module matters: the same concrete cyclic quartic quotient has a cohomologically invisible regular module and a nonzero trivial-coefficient obstruction target.

This example does not yet produce a nonzero Hochschild–Serre transgression. That requires a specified invariant class in \(H^1(G_L,V)^{C_4}\), not just a nonzero target group. The Artin–Schreier–Witt classification supplies the general framework for cyclic \(2^n\)-extensions; this elementary tower is a directly verified length-four test case.

### G-13 — lifting the explicit quartic example and a nonzero transgression

Let (K=\mathbb F_2(s)) and let (L/K) be the cyclic quartic extension of G-12. Artin–Schreier–Witt theory identifies cyclic extensions of degree (2^n) with classes in
\[
W_n(K)/(F-1)W_n(K),
\]
and the classification is compatible with the truncation map (W_3(K)\to W_2(K)). The latter map is surjective on Witt vectors, hence on these quotient groups: any class defining (L/K) has a length-three Witt-vector lift. This gives a character (\chi:G_K\to\mathbb Z/8\mathbb Z) whose reduction modulo four is the character defining (L/K). Since that reduction has order four, (\chi) has order eight: an order-four subgroup of \(\mathbb Z/8\mathbb Z\) reduces to the order-two subgroup modulo four. Thus there is a cyclic octic extension (M/K) with quartic subfield exactly (L).

For the finite Galois sequence
\[
1\to N=\operatorname{Gal}(M/L)\cong C_2
\to G=\operatorname{Gal}(M/K)\cong C_8
\to Q=\operatorname{Gal}(L/K)\cong C_4\to1,
\]
take the trivial module \(V=\mathbb F_2\). The nonzero class in
\(H^1(N,\mathbb F_2)=\operatorname{Hom}(C_2,\mathbb F_2)\)
is Q-invariant. The restriction map
\[
H^1(C_8,\mathbb F_2)\to H^1(C_2,\mathbb F_2)
\]
is zero: the subgroup C2 is generated by (g^4), and every homomorphism (C_8\to\mathbb F_2) sends (g^4) to zero. The five-term exact sequence therefore makes
\[
d_2:H^1(C_2,\mathbb F_2)^{C_4}\to H^2(C_4,\mathbb F_2)
\]
injective. Both sides are one-dimensional, so this transgression is an isomorphism and in particular nonzero.

This is an actual nonzero transgression for a specified finite Galois extension, not merely a nonzero obstruction target. It is a finite cyclic-group test case; it does not yet identify a Fold-specific Galois module or arithmetic class. The ASW classification and Witt truncation framework are described in the cited references.

### G-14 — explicit length-three Witt lift of the quartic field

Use standard 2-typical Witt coordinates. For length two,
\[
(F-1)(u,w)=(u^2+u,\;w^2+w+u^3+u^2).
\]
Thus the G-12 field is represented by \((s,s)\): the first equation is \(u^2+u=s\), and the second is \(w^2+w+u^3+u^2=s\), equivalent to \(w^2+w=u^3+u\).

Lift the representative to \((s,s,0)\in W_3(K)\). The third coordinate of \(F(u,w,v)-(u,w,v)\), reduced in characteristic two, is
\[
u^7+u^4+u^3w^2+u^3w+u^2w^2+u^2w+w^3+w^2+v^2+v.
\]
Therefore the explicit cyclic-octic tower is
\[
\begin{aligned}
u^2+u&=s,\\
w^2+w&=u^3+u,\\
v^2+v&=u^7+u^4+u^3w^2+u^3w+u^2w^2+u^2w+w^3+w^2.
\end{aligned}
\]
It is the ASW extension attached to \((s,s,0)\), whose reduction is the order-four class of G-12; its character has order eight, so the full extension is cyclic of degree eight and has the specified quartic subfield.

Translation by \((1,0,0)\in W_3(\mathbb F_2)\cong\mathbb Z/8\mathbb Z\) gives a generator
\[
\sigma(u)=u+1,\quad
\sigma(w)=w+u,\quad
\sigma(v)=v+u^3+uw+u.
\]
Its square sends \((u,w,v)\mapsto(u,w+1,v+w)\), and its fourth power sends \((u,w,v)\mapsto(u,w,v+1)\), confirming order eight. This makes the G-13 nonzero transgression example fully explicit at the field-equation level.

### G-15 — explicit factor set and cyclic cocycle-sum certificate

Write the quotient \(C_4=\mathbb Z/4\mathbb Z\) additively, choose a generator \(g\) of \(C_8\), and use the section \(s(i)=g^i\) for \(i=0,1,2,3\). The factor set for \(1\to\langle g^4\rangle\to C_8\to C_4\to1\) is
\[
\tau(i,j)=\left\lfloor\frac{i+j}{4}\right\rfloor\bmod2.
\]
It is normalized and satisfies the 2-cocycle identity because it is the factor set of this section. Its cyclic cocycle-sum representative is
\[
w_\tau=\sum_{j=0}^{3}\tau(j,1)=0+0+0+1=1.
\]
For trivial \(\mathbb F_2\)-coefficients, \(D=0\) and the norm \(D^3=0\), so \(H^2(C_4,\mathbb F_2)\cong\mathbb F_2\), represented by 1. Thus the G-13 transgression is exactly the nonzero G-11 cyclic obstruction class under this section convention.

### G-16 — a uniform family of nonzero transgressions

For every integer \(r\ge1\), consider
\[
1\to C_{2^r}\to C_{2^{r+2}}\to C_4\to1.
\]
With trivial \(\mathbb F_2\)-coefficients, the transgression
\[
d_2:H^1(C_{2^r},\mathbb F_2)^{C_4}\longrightarrow H^2(C_4,\mathbb F_2)
\]
is an isomorphism. Indeed, both spaces are one-dimensional. The restriction \(H^1(C_{2^{r+2}},\mathbb F_2)\to H^1(C_{2^r},\mathbb F_2)\) is zero because a generator of the kernel is the fourth power of a generator of the larger cyclic group. Five-term exactness makes \(d_2\) injective, hence bijective.

There is a uniform factor-set certificate. Let \(g\) generate \(C_{2^{r+2}}\), let \(k=g^4\) generate the kernel, and choose section \(s(i)=g^i\), \(0\le i<4\). The extension factor set with values in the kernel is
\[
\widetilde\tau(i,j)=k^{\lfloor(i+j)/4\rfloor}.
\]
Push it out along the nonzero character \(C_{2^r}\to\mathbb F_2\), which sends \(k\mapsto1\). The resulting \(\mathbb F_2\)-valued cocycle is
\[
\tau(i,j)=\lfloor(i+j)/4\rfloor\bmod2,
\qquad
\sum_{j=0}^3\tau(j,1)=1.
\]
It represents the nonzero class in \(H^2(C_4,\mathbb F_2)\), uniformly in \(r\). Thus the G-15 cocycle-sum certificate is not special to the octic case.

### G-17 — arithmetic realization of the entire G-16 family

The G-16 family is realized over the same rational function field \(K=\mathbb F_2(s)\). For every \(n\ge2\), take the length-\(n\) Witt vector
\[
\mathbf a_n=(s,s,0,\ldots,0)\in W_n(K)
\]
and solve the Artin–Schreier–Witt equation \((F-1)\mathbf y=\mathbf a_n\). The degree criterion says that a length-\(n\) Witt vector defines an extension of degree \(2^n\) whenever its first coordinate is not in \(\wp(K)=\{x^2+x:x\in K\}\). Here \(s\notin\wp(K)\), since it has a pole of odd order one at infinity, whereas a pole of \(x^2+x\) has even order. Hence \([M_n:K]=2^n\) and \(\operatorname{Gal}(M_n/K)\cong C_{2^n}\).

Truncating \(\mathbf a_n\) to length two gives \((s,s)\), exactly the G-12 quartic class. Thus the quartic field \(L\) is the specified degree-four subfield of every \(M_n\). Taking \(n=r+2\) realizes every G-16 exact sequence as a function-field Galois sequence over this one fixed \(K\).

For \(n=3\), the coordinate expansion is the explicit G-14 octic tower. For general \(n\), the Witt-vector equation is an exact finite-coordinate specification; expanded higher coordinate polynomials are not written out here. This closes the existence/arithmetic-realization gap in G-16, while leaving the Fold-specific interpretation open. The degree criterion is stated in Pop, *The Oort Conjecture on lifting covers of curves*, Fact 2.1(1), pp. 289–290.


## G-18 — arbitrary cyclic 2-power quotient transgression

Let r,m≥1 and consider the cyclic extension
\[
1\longrightarrow C_{2^r}\longrightarrow C_{2^{r+m}}\longrightarrow C_{2^m}\longrightarrow1.
\]
Give all groups the trivial coefficient module \(\mathbb F_2\). The Hochschild–Serre transgression is an isomorphism
\[
d_2:H^1(C_{2^r},\mathbb F_2)^{C_{2^m}}\xrightarrow{\sim}H^2(C_{2^m},\mathbb F_2).
\]
Indeed, both groups are one-dimensional: for a cyclic 2-group, \(H^1(-,\mathbb F_2)=H^2(-,\mathbb F_2)=\mathbb F_2\) with trivial coefficients. If g generates the middle group, the kernel is generated by \(g^{2^m}\). Every homomorphism \(C_{2^{r+m}}\to\mathbb F_2\) kills this element because \(2^m\) is even. Thus the restriction map from middle-group \(H^1\) to kernel \(H^1\) is zero. Five-term exactness makes \(d_2\) injective, hence an isomorphism.

There is an explicit factor-set certificate. Use representatives \(s(i)=g^i\), \(0\le i<2^m\), for the quotient. With kernel generator \(k=g^{2^m}\), the extension factor set is
\[
\widetilde\tau(i,j)=k^{\lfloor(i+j)/2^m\rfloor}.
\]
Push it out by the nonzero character \(C_{2^r}\to\mathbb F_2\) sending k to 1. The resulting normalized cocycle is
\[
\tau(i,j)=\lfloor(i+j)/2^m\rfloor\pmod2.
\]
Its cyclic sum is \(\sum_{j=0}^{2^m-1}\tau(j,1)=1\), since precisely the final summand wraps around. As the norm on trivial \(\mathbb F_2\)-coefficients is multiplication by \(2^m=0\), this is the nonzero class in \(H^2(C_{2^m},\mathbb F_2)\). This identifies the transgression explicitly, not just abstractly.

**Arithmetic realization over one fixed field.** Let \(K=\mathbb F_2(s)\). For every n≥1, the length-n Artin–Schreier–Witt vector \(a_n=(s,s,0,\ldots,0)\) (for n=1 use (s)) has first coordinate outside \(\wp(K)=\{x^2+x:x\in K\}\), since s has a pole of odd order one at infinity and every pole of x²+x has even order. The Artin–Schreier–Witt degree criterion therefore gives a cyclic extension \(M_n/K\) of degree \(2^n\). Take n=r+m. Its unique degree-\(2^m\) intermediate field is \(M_m\), and
\[
1\to\operatorname{Gal}(M_n/M_m)\cong C_{2^r}\to\operatorname{Gal}(M_n/K)\cong C_{2^{r+m}}\to\operatorname{Gal}(M_m/K)\cong C_{2^m}\to1
\]
realizes the group extension above. For m=2, \(M_m\) is precisely the explicit quartic field of G-12/G-14. This establishes a common arithmetic realization of the entire two-parameter family.

**Scope.** This is a theorem about finite cyclic groups and explicit Artin–Schreier–Witt extensions. It does not yet identify a Fold-derived Galois representation, Selmer class, or arithmetic transgression. That bridge remains open.

Reference for the degree criterion: the Artin–Schreier–Witt classification and criterion that the extension has degree p^n exactly when the first Witt coordinate is not in the Artin–Schreier image are stated in [Annals of Mathematics 180 (2014), Fact 2.1(1)](https://annals.math.princeton.edu/wp-content/uploads/annals-v180-n1-p06-p.pdf).

## G-19 — transgression is the pushed-out extension class

Let
\[
1\longrightarrow N\longrightarrow G\xrightarrow{\pi}Q\longrightarrow1
\]
be an extension with **abelian** kernel N. Let A be a G-module on which N acts trivially, and let \(\chi:N\to A\) be a Q-equivariant homomorphism. Then \(\chi\) defines an invariant class in \(H^1(N,A)^Q\), and the Hochschild–Serre transgression is the class of the pushout extension:
\[
\boxed{d_2([\chi])=[\chi_*G]\in H^2(Q,A).}
\]
The sign depends on the convention for the extension factor set and the inhomogeneous coboundary; it is immaterial over \(\mathbb F_2\).

**Factor-set proof.** Choose a normalized section \(s:Q\to G\), and define
\[
\omega(q_1,q_2)=s(q_1)s(q_2)s(q_1q_2)^{-1}\in N.
\]
Since N acts trivially on A, the standard cochain formula for transgression gives
\[
d_2([\chi])=[-\chi\circ\omega].
\]
But \(\chi\circ\omega\) is exactly the factor set of the pushout extension along \(\chi\). Thus its cohomology class is the pushout extension class, up to the stated sign convention. In particular, the transgression vanishes if and only if the pushout extension splits. Equivalently, the character \(\chi\) extends to a 1-cocycle (crossed homomorphism) \(G\to A\) compatible with the quotient action.

**Application to G-18.** Take
\[
N=\langle k=g^{2^m}\rangle\cong C_{2^r},\quad
G=\langle g\rangle\cong C_{2^{r+m}},\quad
Q=G/N\cong C_{2^m},
\]
and let \(A=\mathbb F_2\) with trivial action. The nonzero character \(\chi(k)=1\) is Q-invariant. For representatives \(s(i)=g^i\), \(0\le i<2^m\), the factor set is
\[
\omega(i,j)=k^{\lfloor(i+j)/2^m\rfloor}.
\]
Pushing it through \(\chi\) gives
\[
(\chi\circ\omega)(i,j)=
\left\lfloor\frac{i+j}{2^m}\right\rfloor\bmod2,
\]
the explicit G-18 cocycle. Its cyclic sum is 1, so its class is nonzero. Hence the pushout extension is nonsplit and the transgression is nonzero. This recovers the G-18 isomorphism by a direct extension-class identification, in addition to the five-term exact-sequence proof.

**Scope.** This theorem explains the group-cohomological meaning of G-18. It does not construct a Fold-derived kernel N, character \(\chi\), or Galois representation. Those remain separate open tasks.

**Reference.** A factor-set formula for transgression, \(d_2(\phi)=-\phi\circ\omega\) when N acts trivially on the coefficient module, is stated and proved as Proposition 6.1 in *The Galois action and cohomology of a relative homology group of Fermat curves*, [Journal of Algebra (2018)](https://doi.org/10.1016/j.jalgebra.2018.02.021).


## G-20 — arbitrary quotient modules: transgression is the invariant class modulo norms

Fix
\[
1\to N=\langle k\rangle\cong C_{2^r}
\to G=\langle g\rangle\cong C_{2^{r+m}}
\to Q=\langle\sigma\rangle\cong C_{2^m}\to1,
\qquad k=g^{2^m}.
\]
Let A be any (possibly nontrivial) \(\mathbb F_2[Q]\)-module, inflated to G, so N acts trivially. Put \(D=\sigma-1\) and \(q=2^m\). A homomorphism \(\chi:N\to A\) is determined by \(a=\chi(k)\); because A has exponent two, this is well-defined for every a∈A. It is Q-invariant precisely when \(Da=0\).

**Theorem.** Under the cyclic identification
\[
H^2(Q,A)=A^Q/N_QA=\ker D/\operatorname{im}(D^{q-1}),
\]
the transgression is
\[
\boxed{d_2(a)=[a].}
\]
In particular,
\[
\ker d_2=\operatorname{im}(D^{q-1})\subseteq\ker D,
\qquad
\operatorname{im}d_2=H^2(Q,A).
\]
Thus for this particular cyclic extension, the transgression from invariant kernel characters is surjective, and its kernel consists exactly of norm elements.

**Proof.** Choose section \(s(i)=g^i\), 0≤i<q. Its kernel-valued factor set is
\[
\omega(i,j)=k^{\lfloor(i+j)/q\rfloor}.
\]
Pushing out by \(\chi(k)=a\) gives the A-valued factor set
\[
\tau_a(i,j)=\left\lfloor\frac{i+j}{q}\right\rfloor a.
\]
The factor-set formula for transgression therefore identifies \(d_2(a)\) with \([\tau_a]\), up to sign (irrelevant in characteristic two). For cyclic Q, the class in H² is represented by the cyclic sum
\[
\sum_{j=0}^{q-1}\tau_a(j,1)=a.
\]
This element is invariant because Da=0, and its class is taken modulo the norm image \(N_QA=D^{q-1}A\). Hence the displayed formula and kernel/image statements follow. The cyclic cohomology quotient \(A^Q/N_QA\) follows from the standard two-periodic cyclic resolution; see Neukirch–Schmidt–Wingberg, *Cohomology of Number Fields*, §I.7 [electronic edition](https://www.mathi.uni-heidelberg.de/~schmidt/NSW2e/NSW2.3.pdf).

**Jordan interpretation.** Decompose D into nilpotent Jordan blocks of lengths d≤q. The invariant subspace \(\ker D\) has one bottom vector per block. The norm \(D^{q-1}\) maps the top vector to the bottom vector exactly on blocks of length q, and vanishes on shorter blocks. Consequently H² has one basis class per block of length <q, exactly as in G-8/G-9. The transgression sends a kernel character to its bottom-vector coordinates and discards precisely the full-length (projective) block coordinates.

**Consequences.** For trivial A=\(\mathbb F_2\), D=0 and this reduces to G-18. For a free \(\mathbb F_2[Q]\)-module, all Jordan blocks have length q, so H²=0 and every invariant kernel character is a norm; no nonzero transgression survives. For any module containing a short Jordan block, choosing its bottom vector gives a kernel character with nonzero transgression.

**Scope.** This is still an abstract finite-group construction. It gives a sharper coefficient-module criterion for a future Fold/Galois bridge, but it does not identify a coefficient module arising from the Fold.


## G-21 — explicit cyclic degree-16 Artin–Schreier–Witt tower

Let \(K=\mathbb F_2(s)\), and take the length-four Witt vector
\[
\mathbf a=(s,s,0,0)\in W_4(K).
\]
Writing \((F-1)(u,w,v,z)=\mathbf a\), the first three coordinates are the G-12/G-14 equations:
\[
\begin{aligned}
u^2+u&=s,\\
w^2+w&=u^3+u,\\
v^2+v&=u^7+u^4+u^3w^2+u^3w+u^2w^2+u^2w+w^3+w^2.
\end{aligned}
\]
The fourth coordinate, obtained from the fourth Witt ghost polynomial and reduced modulo two, is
\[
\begin{aligned}
z^2+z={}&u^{15}+u^{13}+u^{12}+u^{11}
+u^{10}w^2+u^{10}w+u^{10}\\
&+u^8w^2+u^8w+u^8
+u^7w^3+u^7w^2+u^7v^2+u^7v\\
&+u^4w^3+u^4w^2+u^4v^2+u^4v\\
&+u^3w^6+u^3w^4+u^3w^2v^2+u^3w^2v
+u^3wv^2+u^3wv\\
&+u^2w^6+u^2w^4+u^2w^2v^2+u^2w^2v
+u^2wv^2+u^2wv\\
&+w^7+w^4+w^3v^2+w^3v+w^2v^2+w^2v+v^3+v^2.
\end{aligned}
\]
There is no \(z\)-term on the right: the \(z^2+z\) is the fourth coordinate of \(F-1\).

The generator is Witt translation by \((1,0,0,0)\):
\[
\begin{aligned}
\sigma(u)&=u+1,\\
\sigma(w)&=w+u,\\
\sigma(v)&=v+u^3+uw+u,\\
\sigma(z)&=z+u^7+u^5+u^4w+u^3w+u^3v+u^3\\
&\qquad\quad+u^2w+uw^3+uwv+uv+u.
\end{aligned}
\]
In characteristic two, Witt multiplication by 2 is \(2(x_0,x_1,x_2,x_3)=(0,x_0^2,x_1^2,x_2^2)\). Hence \(2(1,0,0,0)=(0,1,0,0)\), \(4(1,0,0,0)=(0,0,1,0)\), \(8(1,0,0,0)=(0,0,0,1)\), and \(16(1,0,0,0)=0\). Thus the translation has exact order \(16\).

**Degree and tower.** The first coordinate \(s\) is not in \(\wp(K)=\{x^2+x:x\in K\}\): its pole at infinity has odd order one, while every pole of \(x^2+x\) has even order. The Artin–Schreier–Witt degree criterion therefore gives a cyclic extension \(M_4/K\) of degree \(16\). Its truncations are exactly the quartic field of G-12 and octic field of G-14. Thus the explicit arithmetic realization is now expanded through degree \(16\), rather than only specified abstractly by a length-four Witt vector.

**Derivation check.** The displayed fourth coordinate is obtained recursively from the Witt ghost polynomials
\[
w_j(X_0,\ldots,X_j)=\sum_{i=0}^j2^iX_i^{2^{j-i}},
\]
using \(F(u,w,v,z)=(u^2,w^2,v^2,z^2)\) and the Witt additive inverse, then reducing the resulting integral polynomial modulo two. The translation formulas are obtained from the same ghost-polynomial addition recursion. This records the algebraic derivation; no external computer-algebra proof certificate or Fold-specific Galois module is claimed.

**Scope.** G-21 closes the next explicit-coordinate gap in the common \(\mathbb F_2(s)\) tower. It does not create the missing Fold-derived representation or identify a Selmer class. Those remain open.

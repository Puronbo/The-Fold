# UF-026 — Complete nonlinear automorphism group of the Fold vertex algebra

## Algebra and filtration

Let k be a field of characteristic zero and
\[
C=k[x,y]/(x²+y²,x⁴).
\]
Equivalently C=k[x,y]/(x²+y²,x²y²), since y²=−x² implies x²y²=−x⁴. Its maximal ideal is m=(x,y), with m⁵=0 and Hilbert function (1,2,2,2,1).

Every k-algebra automorphism preserves m and hence induces an automorphism of m/m². The associated graded algebra gr_m(C) is C itself, so the induced degree-one map belongs to the graded linear automorphism group classified in UF-025.

## Theorem 1 — Complete kernel of the linear-part map

Let Aut₁(C) be the subgroup of automorphisms inducing the identity on m/m². Every element of Aut₁(C), and only such an element, is given by
\[
\begin{aligned}
X={}&x+\alpha x²+\beta xy+\gamma x³+\delta x²y+u x³y,\\
Y={}&y-\beta x²+\alpha xy-\delta x³+\eta x²y+v x³y,
\end{aligned}
\]
where α,β,γ,δ,η,u,v are arbitrary elements of k.

In particular, Aut₁(C) is an affine 7-dimensional unipotent algebraic group.

**Proof.** Since C has basis 1; x,y; x²,xy; x³,x²y; x³y, every possible pair with identity linear part has unique expressions
\[
X=x+\alpha x²+\beta xy+\gamma x³+\delta x²y+u x³y,
\]
\[
Y=y+A x²+B xy+C x³+D x²y+v x³y.
\]
Use y²=−x² and x⁴=0. Direct multiplication gives
\[
X²+Y²=2(\alpha-B)x³+2(\beta+A)x²y
+2(\alpha\beta+\delta+AB+C)x³y.
\]
Since char(k)=0 and x³,x²y,x³y are linearly independent, the relation X²+Y²=0 is equivalent to
B=α, A=−β, C=−δ. There are no other constraints.

Also X⁴=x⁴=0: all terms in X−x have degree at least two, and every product contributing to X⁴ beyond x⁴ has degree at least five, hence vanishes because m⁵=0. Thus the displayed assignments define an endomorphism C→C.

Their induced map on m/m² is the identity. By Nakayama's lemma, X,Y generate m; together with 1 they generate C as a k-algebra. The endomorphism is therefore surjective, and since C is finite-dimensional it is bijective. Conversely every element of Aut₁(C) has the displayed general form and must satisfy the coefficient equations just derived. ∎

The seven parameters are genuine free parameters: they are the two quadratic parameters α,β; three cubic parameters γ,δ,η; and two socle parameters u,v.

## Theorem 2 — Full automorphism group

Let G_gr denote the graded linear automorphism group from UF-025. The linear-part homomorphism gives a split exact sequence
\[
1\longrightarrow Aut_1(C)\longrightarrow Aut_k(C)
\overset{\ell}{\longrightarrow}G_{gr}\longrightarrow1.
\]
Consequently
\[
\boxed{Aut_k(C)\cong Aut_1(C)\rtimes G_{gr}.}
\]

Here G_gr consists of maps (x,y)↦tQ(x,y), with t∈k* and Q∈O(2,k) satisfying ab(a²−b²)=0 for the first row (a,b). Its orthogonal part is the dihedral group of order 16.

**Proof.** Any automorphism induces a graded automorphism on gr_m(C), which is identified with C. This induced graded automorphism is determined by its invertible degree-one linear part and lies in G_gr. Every element of G_gr is itself an actual linear automorphism of C, so the map ℓ is surjective and has a group-theoretic section. Its kernel is exactly Aut₁(C), classified in Theorem 1. A split exact sequence gives the semidirect product. ∎

The kernel is unipotent: its elements act trivially on every associated-graded piece and hence are upper triangular with diagonal entries one in a basis ordered by degree.

## Consequences

1. The full automorphism group is a positive-dimensional algebraic group of dimension 8: seven dimensions from the unipotent kernel and one from scalar dilations in the graded quotient.
2. The D4 action is not the full symmetry group. It is contained in the larger graded D16 subgroup, and the seven-parameter unipotent kernel supplies additional nonlinear automorphisms.
3. The seven-parameter family is not merely a collection of examples: it is the entire kernel of the linear-part map.
4. The automorphism group is determined by the algebra and its maximal-ideal filtration. Choosing a particular D4 subgroup still requires additional structure; the abstract algebra has a larger graded symmetry group.

## Scope

This theorem is stated in characteristic zero. The coefficient calculation uses invertibility of 2. The graded quotient and nonlinear kernel should be revisited in characteristic two, where the presentation and D4 action become modular. The theorem classifies k-algebra automorphisms of this finite local algebra; it does not classify automorphisms of the entire parameterized family R_{p,q}.

## Reproducibility

Run `python3 tools/fold_nonlinear_automorphisms.py`. The SymPy verifier expands and reduces the seven-parameter formulas and checks X²+Y²=0 and X⁴=0 identically. The proof of exhaustiveness and the Nakayama argument are given above; the script is an identity check, not a substitute for them.

## Open problem UF-026-A

Compute the group law on the seven coordinates (α,β,γ,δ,η,u,v), derive its lower central series, and determine whether it admits a useful decomposition into central and noncentral unipotent subgroups. Then study its reduction in characteristic two and compare the resulting automorphism scheme with the modular D4 action.

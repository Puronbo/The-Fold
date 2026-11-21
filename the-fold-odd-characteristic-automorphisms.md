# UF-035 — The full automorphism group in odd characteristic

## Theorem UF-035.1 — Classification over an algebraically closed odd-characteristic field

Let k be algebraically closed with char(k) not equal to 2, and let
\[
C=k[x,y]/(x^2+y^2,x^4),\qquad \mathfrak m=(x,y).
\]
Every automorphism preserves the unique maximal ideal and induces an automorphism of the associated graded algebra. The induced linear part belongs to the graded group
\[
G_{\rm gr}= (\mathbb G_m\times D_{16})/
\langle(-1,-I)\rangle,
\]
where D16 is the dihedral group of order 16 described in UF-025.

The kernel U of the linear-part map consists exactly of
\[
\begin{aligned}
X={}&x+\alpha x^2+\beta xy+\gamma x^3
       +\delta x^2y+u x^3y,\\
Y={}&y-\beta x^2+\alpha xy-\delta x^3
       +\eta x^2y+v x^3y,
\end{aligned}
\]
with seven arbitrary parameters in k. Consequently
\[
\boxed{\operatorname{Aut}_k(C)\cong U\rtimes G_{\rm gr},
\qquad \dim\operatorname{Aut}_k(C)=8.}
\]

### Proof

The algebra is local Artinian with residue field k, so every automorphism preserves \(\mathfrak m\). Its action on \(\mathfrak m/\mathfrak m^2\) determines a graded automorphism of \(\operatorname{gr}_{\mathfrak m}(C)=C\). UF-025 classifies these linear parts: after a scalar normalization they are orthogonal, and preservation of the quartic relation imposes
\[
ab(a^2-b^2)=0.
\]
Over an algebraically closed field of odd characteristic, 2 and 4 are invertible. The four projective directions selected by this equation and their orthogonal companions give precisely the finite orthogonal subgroup D16; scalar dilation supplies the one-dimensional factor.

For the kernel, write the most general identity-linear pair as
\[
X=x+\alpha x^2+\beta xy+\gamma x^3+\delta x^2y+u x^3y,
\]
\[
Y=y+A x^2+Bxy+C_3x^3+D x^2y+v x^3y.
\]
Reduction using \(y^2=-x^2\) and \(x^4=0\) gives
\[
X^2+Y^2=
2(\alpha-B)x^3+2(\beta+A)x^2y
+2(\alpha\beta+\delta+AB+C_3)x^3y.
\]
Since 2 is invertible and these three basis elements are independent, the relation is equivalent to
\[
B=\alpha,\quad A=-\beta,\quad C_3=-\delta.
\]
The relation \(X^4=0\) is automatic: every term in X beyond x has degree at least two, and all additional terms in the fourth power have degree at least five, while \(\mathfrak m^5=0\). The resulting endomorphism has identity linear part, hence is an automorphism by Nakayama's lemma and finite dimensionality. This proves that U is exactly the seven-parameter group of UF-026.

The linear-part map is split because every graded automorphism is itself an algebra automorphism. Thus the full group is the stated semidirect product. Its dimension is seven plus one.

## Theorem UF-035.2 — Smoothness in every odd characteristic

For every algebraically closed field k of odd characteristic, the full automorphism group scheme of C is smooth of dimension eight.

**Proof.** The preceding classification identifies its geometric points with an eight-dimensional algebraic group, so its underlying reduced group has dimension eight. UF-034 gives identity tangent dimension eight in every odd characteristic. Therefore the local dimension and embedding dimension at the identity agree, so the local ring is regular. Over an algebraically closed field this is smoothness at the identity; translation gives smoothness at every point. The same conclusion holds geometrically for any field of odd characteristic after algebraic closure. \(\square\)

## Characteristic comparison

- In every odd characteristic, the full automorphism group is smooth of dimension eight and has tangent dimension eight.
- In characteristic two, UF-033 gives reduced dimension 13 and tangent dimension 16, so the automorphism group scheme is non-smooth.
- Characteristic three changes the center of the seven-dimensional restricted bracket algebra from UF-030/031, but it does not change the dimension or smoothness of the full automorphism group scheme.

Thus 2 is the exceptional prime for smoothness and dimension of the full automorphism group scheme in this family. The characteristic-three effect belongs to a different, marked Lie-algebra structure.

## Scope and next problem

This classifies the geometric fibers over fields of odd characteristic. It does not yet construct or identify the schematic closure over Z of U, nor does it prove that the full automorphism group scheme is flat over Z. Those integral questions remain UF-036.

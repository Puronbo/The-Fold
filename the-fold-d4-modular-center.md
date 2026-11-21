# UF-031 — Restriction to D4 and the intrinsic characteristic-three center

## Setup

Let \(\mathfrak u\) be the seven-dimensional integral alternating Lie algebra described by UF-028 and UF-030, with coordinates \((a,b,c,d,e,u,v)\). The original signed-permutation subgroup \(D_4\) is generated inside \(D_{16}\) by \(t=r^2\) and \(s\), where \(r\) is the normalized 45-degree rotation from UF-029.

Although the individual matrix \(R\) for \(r\) contains \(1/\sqrt2\), its square is integral. Thus the restriction to this original D4 subgroup is defined over \(\mathbb Z\), and can be reduced in every characteristic.

## Theorem 1 — Integral D4 generator matrices

In the ordered coordinates \((a,b,c,d,e,u,v)\), the generators act by
\[
t=r^2:
(a,b,c,d,e,u,v)\longmapsto
(b,-a,-e,-d,-c,v,-u),
\]
and
\[
s:
(a,b,c,d,e,u,v)\longmapsto
(a,-b,c,-d,e,-u,v).
\]
They satisfy \(t^4=s^2=1\) and \(sts=t^{-1}\). These matrices have integer entries and define the same D4 action over every field.

## Theorem 2 — Characteristic-zero and odd-characteristic restriction

Over any algebraically closed field of odd characteristic, the restricted D4 module decomposes as
\[
\boxed{\mathfrak u\!\downarrow_{D_4}
\cong 2E\oplus\mathbf1\oplus\chi_{-+}\oplus\chi_{--}.}
\]
Here \(E\) is the unique two-dimensional irreducible representation of D4, with \(t\) acting as a quarter-turn and \(s\) as a reflection. The two character lines from the cubic plane \(e=c\) are:
- \(\langle(0,0,1,0,1,0,0)\rangle\), with \((t,s)=(-1,+1)\), hence \(\chi_{-+}\);
- \(\langle(0,0,0,1,0,0,0)\rangle\), with \((t,s)=(-1,-1)\), hence \(\chi_{--}\).

The line \(\chi=\langle(0,0,-1,0,1,0,0)\rangle\) from UF-029 has \((t,s)=(+1,+1)\), so it restricts to the trivial character. The quadratic plane and the socle plane each restrict to \(E\). Their reflection matrices differ by a sign, but they are equivalent: intertwining by the quarter-turn identifies them.

**Proof.** The displayed matrices preserve the indicated coordinate subspaces. The cubic three-space is the direct sum of the invariant plane \(e=c\) and the line \((-1,0,1)\); on the plane, \(t=-I\) and \(s=\operatorname{diag}(1,-1)\), giving the two stated characters. On each of the two other planes, \(t\) is a quarter-turn; the two reflection choices are conjugate by that quarter-turn. The dimensions add to seven. Since \(p\ne2\), Maschke's theorem applies. \(\square\)

The restriction is not the regular D4 representation: the regular representation has four one-dimensional characters and two copies of \(E\), whereas this module has only three one-dimensional characters. In particular, \(\chi_{+-}\) is absent.

## Theorem 3 — The characteristic-three center is intrinsically visible to D4

Let \(k\) be an algebraically closed field of odd characteristic and let \(Z(\mathfrak u_k)\) denote the center of the reduced alternating Lie algebra.

- If \(\operatorname{char}k\ne3\), then
  \[
  Z(\mathfrak u_k)=[\mathfrak u_k,\mathfrak u_k]\cong E.
  \]
- If \(\operatorname{char}k=3\), then
  \[
  Z(\mathfrak u_k)\cong E\oplus\mathbf1,
  \qquad [\mathfrak u_k,\mathfrak u_k]\cong E.
  \]
  The extra one-dimensional central summand is exactly
  \[
  \mathbf1=\langle(-1,0,1)\rangle
  \]
  in the cubic coordinates \((c,d,e)\).

**Proof.** UF-030 computes the Smith normal form of the radical map as \((1,1,1,1,3)\). Hence its kernel is zero away from characteristic three and is the line \((-1,0,1)\) in characteristic three. The commutator image remains the two-dimensional socle plane, which is \(E\) under D4. Since the extra line is fixed by both \(t\) and \(s\), the center decomposition is \(E\oplus\mathbf1\). \(\square\)

This answers the intrinsic-detection question: the characteristic-three enlargement is visible using only the original D4 action together with the Lie bracket. It is not an artifact of retaining the larger D16 group. The bracket singles out the center; the D4 action identifies its new summand as the unique trivial-character line in this module.

## What changes, and what does not

1. The D4 representation itself has the same integral matrices in every characteristic; in odd characteristic its semisimple character decomposition is unchanged.
2. The bracket radical changes at 3. The new central direction is the D4-trivial line already present as a representation summand, but it becomes central only after reduction.
3. The derived algebra remains the socle plane of dimension two.
4. This is a change in the Lie-algebra structure, not a change in the underlying D4-module.
5. Characteristic two is not covered by the semisimple decomposition above; it requires a separate modular analysis, although the integral D4 matrices themselves do reduce there.

## Reproducibility

Run `python3 tools/fold_d4_modular_center.py`.

The verifier checks the integral D4 relations, the invariant character lines and two equivalent standard planes, bracket equivariance, and the rank jump of the radical map modulo 3.

## Follow-up

**UF-031-A.** Analyze the same integral D4 module and bracket in characteristic two, where Maschke's theorem fails, and determine its indecomposable summands and center. Compare that answer with the separate characteristic-two degeneration of the original quotient map.

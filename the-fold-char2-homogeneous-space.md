# UF-038 — The homogeneous space H/U and the class-two normal closure

Work over an algebraically closed field k of characteristic two. Use the notation of UF-037:
\[
C_k=k[x,z]/(x^4,z^2),\quad z=x+y,
\]
and let \(\mathcal H\cong\mathbb A^{10}_k\) be the identity-linear automorphism group. Let U be the seven-dimensional flat subgroup and N its eight-dimensional normal closure.

## 1. Theorem UF-038.1 — N/U is the additive line

An element of N has the unique form
\[
\begin{aligned}
X={}&x+A x^2+B x^3+C xz+D x^2z+E x^3z,\\
Z={}&z+G x^3+A xz+I x^2z+J x^3z.
\end{aligned}
\]
Composition of an outer element \((A,B,C,D,E,G,I,J)\) and an inner element \((a,b,c,d,e,g,i,j)\) is
\[
\begin{aligned}
A'&=A+a,& B'&=B+b,& C'&=C+c,&D'&=D+d,\\
G'&=G+g,&I'&=I+i,\\
E'&=E+e+A^2c+Ad+Bc+Cb+Ic,\\
J'&=J+j+A^2a+Ai+Ba+Cg+Ia.
\end{aligned}
\]
In particular,
\[
\lambda:N\longrightarrow\mathbb G_a,
\qquad
\lambda(A,B,C,D,E,G,I,J)=B+G+I
\]
is a group homomorphism. It is surjective, and its kernel is exactly U, whose defining equation inside N is \(B+G+I=0\). Therefore
\[
\boxed{N/U\cong\mathbb G_a.}
\]
This also proves U is normal in N, although UF-037 shows it is not normal in all of H.

The inverse of \((A,B,C,D,E,G,I,J)\) is
\[
\begin{aligned}
A^{-1}&=A,&B^{-1}&=B,&C^{-1}&=C,&D^{-1}&=D,\\
G^{-1}&=G,&I^{-1}&=I,\\
E^{-1}&=E+A^2C+AD+IC,\\
J^{-1}&=J+A^3+BA+CG.
\end{aligned}
\]

## 2. Theorem UF-038.2 — N is two-step nilpotent

The commutator of the outer element \((A,B,C,D,E,G,I,J)\) and inner element \((a,b,c,d,e,g,i,j)\) has only its two central coordinates nonzero:
\[
\begin{aligned}
E_{[p,q]}={}&A^2c+Ad+Ca^2+Ci+Da+Ic,\\
J_{[p,q]}={}&A^2a+Aa^2+Ab+Ba+Cg+Gc.
\end{aligned}
\]
The first six coordinates vanish. The final two coordinates \((E,J)\) form a central subgroup \(\mathbb G_a^2\). The commutator map is surjective onto it: choose \(A=1,d=1\) to obtain the E direction, and \(A=1,b=1\) to obtain the J direction. If an element commutes with every element, the displayed formulas force
\[
A=B=C=D=G=I=0.
\]
Thus the center and derived subgroup coincide:
\[
\boxed{Z(N)=[N,N]\cong\mathbb G_a^2.}
\]
Consequently N has nilpotency class exactly two, and its lower central series is
\[
N=\gamma_1(N)\supset\gamma_2(N)=Z(N)\cong\mathbb G_a^2
\supset\gamma_3(N)=1.
\]

## 3. Theorem UF-038.3 — The homogeneous space H/U is affine three-space

The degree-two coefficient map from UF-037 gives
\[
q_2:\mathcal H\to\mathbb G_a^2,
\qquad
q_2(h)=(F,R),\quad R=H-A.
\]
In characteristic two, \(R=H+A\). Its kernel is N. Choose the polynomial section
\[
s(f,r):\quad x\mapsto x,\qquad z\mapsto z+f x^2+r xz.
\]
Its inverse is
\[
s(f,r)^{-1}:\quad
x\mapsto x,\quad
z\mapsto z+f x^2+r xz+fr x^3+r^2x^2z+r^3x^3z.
\]
Thus every \(h\in\mathcal H\) has a unique factorization
\[
h=s(F,R)n,\qquad n\in N.
\]
Since \(N/U\cong\mathbb G_a\), this gives a scheme isomorphism
\[
\boxed{\mathcal H/U\cong\mathbb A^2_k\times\mathbb A^1_k
\cong\mathbb A^3_k.}
\]
It is a homogeneous space, not a quotient group, because U is not normal in H.

More explicitly, in the ten coordinates of UF-037, the right-coset map is
\[
\boxed{
hU\longmapsto
\left(
F,\ H+A,\ B+G+I+F(A+C)+A(H+A)
\right).
}
\]
The first two coordinates identify the coset in \(\mathcal H/N\); the third is \(\lambda(s(F,H+A)^{-1}h)\), the coordinate on \(N/U\). In the ten coordinates of UF-037, the third coordinate is explicitly
\[
\Lambda=B+G+I+F(A+C)+A(H+A).
\]
Indeed, writing \(R=H+A\), the section inverse sends
\[
z\mapsto z+Fx^2+Rxz+FRx^3+R^2x^2z+R^3x^3z,
\]
and the resulting element \(n=s(F,R)^{-1}h\in N\) has \(\lambda(n)=\Lambda\). Thus the quotient map is
\[
h\longmapsto(F,H+A,B+G+I+F(A+C)+A(H+A)).
\]
It is polynomial and its fibers are precisely the right U-cosets.

## 4. Structural interpretation

The three-dimensional difference \(\dim H-\dim U=3\) is now fully resolved:
- Two directions, \(F\) and \(H-A\), are the coordinates of the genuine group quotient \(H/N\cong\mathbb G_a^2\).
- One direction, \(B+G+I\) after correcting by the section, is the quotient \(N/U\cong\mathbb G_a\).
- The total homogeneous space \(H/U\) is affine three-space, even though it has no natural quotient-group structure.

The subgroup chain is
\[
U\triangleleft N\triangleleft H,
\qquad
N/U\cong\mathbb G_a,
\qquad
H/N\cong\mathbb G_a^2.
\]
Here \(N\) is normal in H, while U is normal only in N.

## 5. Reproducibility

Run:
```sh
python3 tools/fold_char2_homogeneous_space.py
```
The verifier checks the N composition law, inverse, commutator, the homomorphism \(\lambda\), and the section-based quotient coordinates in the truncated polynomial ring over \(\mathbb F_2\).

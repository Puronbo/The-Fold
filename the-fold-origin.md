# Origin to Fold

## Purpose

This note rebuilds the argument from its starting objects. It does not take the later complexity-theory applications, numerical analogies, or physical interpretations as premises.

The derivation has two related but distinct constructions:

1. **Scale ledger:** an affine scaling about a chosen datum. Its zero parameter collapses all points to the datum.
2. **Fold ledger:** an involution that pairs points and fixes a crease. A reflection is the geometric model.

They are related, but they are not the same operation. In particular, a collapse is generally not invertible, while an involution is invertible.

## 0. The starting point: a datum and a distinguishable state

Let (V) be a real or complex vector space, let (P_0\in V) be a chosen datum, and let (P\in V) be a state. The displacement from the datum is

[
v=P-P_0.
]

The datum is not assumed to be absolute nothingness. It is a selected reference relative to which displacement is defined.

## 1. The scale family

For a scalar (k), define

[
g_k(P)=P_0+k(P-P_0)=P_0+kv.
]

Three parameter values establish the basic cases:

[
g_1(P)=P,\qquad
g_0(P)=P_0,qquad
g_{-1}(P)=2P_0-P.
]

- (k=1): identity; the state is unchanged.
- (k=0): collapse to the datum; every input has the same output.
- (k=-1): central reflection through the datum; the displacement changes sign.

For real (k), the map scales the displacement, with a sign reversal when (k<0). For complex (k\) acting on a complex vector space, its modulus scales and its argument rotates. This statement depends on the chosen complex structure; it is not a claim that every physical system has a complex-valued scale.

The composition law is

[
g_k\circ g_\ell=g_{k\ell}.
]

**Proof.** Applying (g_\ell) gives (P_0+\ell(P-P_0)). Applying (g_k) about the same datum gives
(P_0+k\ell(P-P_0)=g_{k\ell}(P)). (square)

The determinant statement requires a finite-dimensional vector space of dimension (n): the linear part is (kI), so its determinant is (k^n).

## 2. What collapse does and does not preserve

The map (g_0) is constant. If two distinct states (P,Q) are supplied, then

[
g_0(P)=P_0=g_0(Q).
]

Therefore (g_0) is not injective (unless the state space has only one point), and no inverse map can recover an arbitrary input from the collapsed output alone.

A retained reference can preserve a selected origin or datum. Introduce the augmented state

[
S=(x,r),\qquad F_k(x,r)=(kx,r).
]

Here (r) is explicitly retained while (x) is scaled. At (k=0), the output is ((0,r)). The recovery map

[
U(x,r)=(r,r)
]

returns the retained reference as the first coordinate. It does **not** reconstruct an arbitrary pre-collapse (x); it reconstructs the designated reference (r). If the initial normalized state is (x=r=1), this convention represents a chosen beginning (1), collapse of the first coordinate to (0), and recovery of the retained reference.

This is a proposed bookkeeping convention, not a theorem that information can be recovered after arbitrary physical destruction.

## 3. From scaling to a fold: introduce an involution

A fold in the strict mathematical sense is not the zero-scale map. It is an involution.

Let (X) be a type and (f:X\to X). The involution condition is

[
f(f(x))=x\quad\text{for every }x\in X.
]

This condition says that applying the operation twice returns the original state. It makes (f) bijective, with (f) itself as its inverse.

A concrete Euclidean example is reflection across a hyperplane. Let (n) be a unit normal and let the hyperplane pass through (P_0). Then

[
R(P)=P-2\langle P-P_0,n\rangle n.
]

The normal component changes sign and the tangential component stays fixed. Applying (R) twice restores both components, so (R^2=I).

The fixed set is the crease:

[
H=\operatorname{Fix}(R)=\{P:\langle P-P_0,n\rangle=0\}.
]

The point reflection (g_{-1}) is also an involution, but its fixed set is just the centre (P_0); it is not the same geometry as reflection across a hyperplane.

## 4. Fixed points and paired states

For any involution (f), define

[
\operatorname{Fix}(f)=\{x:f(x)=x\},
\qquad
[x]=\{x,f(x)\}.
]

Each orbit has either one element (when (x) is fixed) or two elements. The involution partitions the state space into these orbits.

This is the exact algebraic content of “two sides meet at the crease.” The phrase is geometric intuition; the theorem is the orbit-size statement.

## 5. The quotient: identifying the two sides

Define (x\sim y) when (y=x) or (y=f(x)). The involution laws make this an equivalence relation. The quotient

[
X/\sim
]

is the space of orbits. Its projection (q:X\to X/\sim) satisfies

[
q(f(x))=q(x).
]

Thus the quotient forgets which representative of a two-point orbit was selected. This is a precise sense in which the fold becomes invisible after passing to the orbit chart.

## 6. The observer or cut is extra structure

A cut is a map (p:X\to X) that retracts onto the fixed set and is constant on each fold orbit:

[
p(p(x))=p(x),\qquad f(p(x))=p(x),\qquad p(f(x))=p(x).
]

Such a map is idempotent and cannot distinguish the two members of an orbit.

Important qualification: an arbitrary involution need not come with such a cut. Existence of a cut is additional structure (for example, an appropriate geometric projection onto a reflection hyperplane). The abstract involution theorem alone does not supply an observer.

## 7. Direction and reversal

If motion is included, direction must be part of the state. For a one-dimensional model use (S=(x,r,d)), with (d\in\{-1,+1\}). A turn changes direction:

[
T(x,r,d)=(x,r,-d),\qquad T^2=I.
]

A step that does not turn preserves (d), for example (x_{m+1}=x_m+d\,\Delta) with (Delta>0). In this model, reversing direction requires a turn event. This is a rule of the proposed discrete model, not a universal theorem about all motion.

## 8. The dependency chain

[
\boxed{
\text{datum}
\to\text{displacement}
\to\text{scale family}
\to\text{collapse/identity/reflection}
\to\text{involution}
\to\text{fixed set and orbits}
\to\text{quotient}
\to\text{optional cut}
}
]

The first three stages define the scale ledger. The involution and quotient stages define the fold ledger. The cut and direction state are further structures, not consequences of collapse alone.

## 9. Status of claims

| Claim | Status |
|---|---|
| (g_k(P)=P_0+k(P-P_0)), its composition law, and the cases (k=0,1,-1) | Exact algebra |
| An involution is bijective and has orbits of size one or two | Exact theorem |
| The orbit quotient identifies each point with its fold image | Exact quotient construction |
| A cut exists for every involution | False in general; extra structure is required |
| The normalized (1\to0\to1) retained-reference story | Proposed convention |
| “The Fold” as a universal account of physical reality or intelligence | Research hypothesis, not established by these constructions |

## 10. What follows next

Only after this foundation is stable should applications be derived. The efficient order is:

1. verify every algebraic statement in Lean;
2. distinguish the affine scale map from the involutive fold in the formal API;
3. add explicit examples and counterexamples;
4. test which later applications are exact consequences, reformulations, rhymes, or false friends;
5. approach computation and learning only after their required structures are stated independently.

The governing discipline is simple: derive each layer from its stated premises, and never let a resemblance substitute for a missing proof.

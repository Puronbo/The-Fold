# A sound finite 2-adic abstraction of the Collatz map

## Purpose

The preceding note proves that no fixed congruence modulo \(m>1\) carries the Collatz map as a deterministic endomap. This note constructs the natural replacement at precision \(2^k\): an exact **set-valued abstract successor** on residue classes.

The construction is finite and sound. It also exposes a sharp limitation: the abstract graph has a self-loop at the zero residue for every precision, so no ranking function on residue states alone can strictly decrease along every abstract transition.

This is a statement about the abstraction, not about the Collatz conjecture.

## 1. Concrete map and abstraction

Let
\[
C(n)=
\begin{cases}
n/2,&n\text{ even},\\
3n+1,&n\text{ odd},
\end{cases}
\qquad n\in\mathbb N_{>0}.
\]

Fix \(k\ge1\), put \(q=2^k\), and define
\[
\alpha_k(n)=[n]_q\in\mathbb Z/q\mathbb Z.
\]
Represent each residue by its unique integer \(r\in\{0,\ldots,q-1\}\).

For a residue \(r\), define its abstract successor set
\[
T_k(r)=\{\alpha_k(C(n)):n\ge1,\ \alpha_k(n)=r\}.
\]
This is the strongest possible one-step abstract transformer for this partition: it contains exactly, not merely at least, the residues reached from concrete integers in the block \(r\).

## 2. Exact transition formula

For \(0\le r<q\),
\[
\boxed{
T_k(r)=
\begin{cases}
\{(3r+1)\bmod q\},&r\text{ odd},\\[2mm]
\{r/2,\ r/2+q/2\},&r\text{ even}.
\end{cases}}
\tag{1}
\]

### Proof

If \(r\) is odd, every positive integer congruent to \(r\pmod q\) is odd, because \(q\) is even. Write \(n=r+tq\), with \(t\) chosen so that \(n>0\). Then
\[
C(n)=3r+1+3tq\equiv3r+1\pmod q.
\]
Every concrete integer in the block therefore has the same successor residue, and the block is nonempty. This gives the odd case.

If \(r\) is even, write \(n=r+tq\). Then
\[
C(n)=n/2=r/2+t(q/2).
\]
Modulo \(q\), this is \(r/2\) when \(t\) is even and \(r/2+q/2\) when \(t\) is odd. Both parities of \(t\) occur among positive integers in the block. For \(r=0\), take positive \(t\); for \(r>0\), take nonnegative \(t\). Thus both residues occur, and there are no others. \(\square\)

## 3. Soundness and exactness

The definition immediately yields the simulation property
\[
\alpha_k(C(n))\in T_k(\alpha_k(n))
\qquad\text{for every }n\ge1.
\tag{2}
\]
More strongly, equation (1) proves that every abstract edge \(r\to s\) is witnessed by at least one positive integer \(n\) with
\[
\alpha_k(n)=r,\qquad \alpha_k(C(n))=s.
\tag{3}
\]

Thus the graph is exact for **one-step existential reachability between residue blocks**. It is not exact for arbitrary paths: witnesses for consecutive abstract edges may be different integers in the same intermediate block. An abstract path need not lift to one concrete Collatz orbit.

This distinction is essential. Soundness of each edge does not imply that every abstract cycle is a concrete cycle.

## 4. Precision loss is the even-branch fork

On the odd branch, parity is already fixed by \(r\), and the next residue at precision \(2^k\) is determined.

On the even branch, knowing \(n\bmod 2^k\) does not determine \(n/2\bmod 2^k\). One additional input bit is needed:
\[
n\bmod 2^{k+1}
\quad\Longrightarrow\quad
(n/2)\bmod 2^k.
\]
The two outputs in (1) are precisely the two possibilities for that missing bit.

Equivalently, the abstraction does not hide the loss of information inside an arbitrary error term: it represents it as a two-way transition. Increasing the output precision by one bit requires increasing the even-branch input precision by one bit. Repeated divisions therefore keep demanding new 2-adic information.

## 5. A universal abstract self-loop

For every \(k\ge1\),
\[
0\in T_k(0),
\]
because (1) gives
\[
T_k(0)=\{0,2^{k-1}\}.
\]
The edge \(0\to0\) has a concrete witness: \(n=2^{k+1}\) satisfies
\[
\alpha_k(n)=0,\qquad C(n)=2^k,\qquad \alpha_k(C(n))=0.
\]

But this witness does not say that the concrete integer is fixed; it halves from \(2^{k+1}\) to \(2^k\). The abstract state forgets that scale change.

Consequently, there is no function \(V:\mathbb Z/2^k\mathbb Z\to W\) into a strictly well-ordered set \(W\) satisfying
\[
V(s)<V(r)\qquad\text{for every abstract edge }r\to s.
\]
Indeed, applying this to the self-loop gives \(V(0)<V(0)\), a contradiction.

This rules out a particularly simple proof strategy: a strict ranking depending only on the fixed residue state. It does **not** rule out rankings that also retain scale, valuation, a bounded-but-renewable precision counter, or other history.

## 6. What a stronger abstraction must do

The obstruction identifies the missing coordinate. A useful state must distinguish not only the residue but also some measure of scale lost during division. Candidate designs include:

- a residue together with a scale band;
- a capped \(2\)-adic valuation plus an explicit overflow state;
- a tower of precisions, where an even step consumes one bit and a refinement rule replenishes it;
- a transition relation carrying intervals or sets of possible magnitudes.

Any proposed design must satisfy two separate obligations:

1. **Simulation:** every concrete Collatz step is represented by an abstract step.
2. **Termination transfer:** the proposed well-founded measure decreases on every represented step, or a separate argument excludes infinite abstract paths relevant to concrete orbits.

A finite sound over-approximation alone cannot establish termination when its graph contains spurious cycles.

## 7. Status and next theorem target

- Exact set-valued residue transformer (1): **proved**.
- One-step soundness and edge-witness exactness: **proved**.
- Fixed-residue strict ranking obstruction: **proved**.
- A finite abstraction with enough scale information to transfer a global termination proof: **open**.
- Collatz conjecture: **not solved**.

The next mathematically meaningful target is not merely to enlarge the residue modulus. It is to construct a scale-sensitive abstraction with a sound simulation theorem and then determine whether a well-founded ranking survives its precision-refinement transitions.

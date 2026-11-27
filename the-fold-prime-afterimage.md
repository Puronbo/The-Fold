# Prime spiral as afterimage and memory path

## Status and scope

This note gives a precise model for reading a prime spiral as a path with retained history. The phrase **afterimage** is an interpretation of the history data, not a claim that primes physically emit traces or that a new theorem about prime distribution has been proved.

Keep three objects distinct:

1. the arithmetic sequence of primes;
2. their geometric placement in a chosen spiral;
3. the ordered history of positions visited by the construction.

The familiar Ulam spiral is one possible placement. The memory-path construction below works for any fixed injective spiral embedding.

## 1. Arithmetic input

Let
\[
p_1=2<p_2=3<p_3=5<\cdots
\]
be the increasing sequence of primes. Let
\[
U:\mathbb N_{>0}\longrightarrow\mathbb Z^2
\]
be a fixed spiral placement. For the classical Ulam spiral, U is the usual square-spiral enumeration of lattice points; the exact orientation and starting convention must be fixed before comparing pictures.

The prime-marked positions are
\[
P_k=U(p_k).
\]

Here k is the **memory step** (the index in the ordered prime sequence), while p_k is the **prime label** (the integer placed). They are not interchangeable.

## 2. The memory path

At step k, define the ordered memory state
\[
M_k=(P_1,P_2,\ldots,P_k).
\]
The active point is its final entry, current_k = P_k. The transition appends one new prime-marked position:
\[
M_{k+1}=M_k\mathbin{+!!+}(P_{k+1}).
\]

The memory path is the sequence (M_k)_{k\geq1}, not merely the current point and not merely the unordered set of marked points. It retains order and therefore records how the current observation was reached.

Two histories can have the same current point and different pasts in a general path model. For this particular increasing-prime enumeration with an injective U, the entire finite history is determined by k; that fact is a property of this chosen encoding, not a universal property of memory.

## 3. Afterimage as a derived observation

The unweighted afterimage at step k is the set of previously visited prime positions:
\[
A_k=\{P_i:1\leq i<k\}.
\]
The current point is excluded by this convention. If it is useful to include the current mark, use A_k^+ = A_k \cup \{P_k\}.

A weighted afterimage can retain recency:
\[
I_k(z)=\sum_{i=1}^{k}\rho^{k-i}K(z-P_i),
\qquad 0<\rho\leq1,
\]
where K is a chosen spatial kernel on the lattice (for example, a Kronecker delta). This is a designed memory visualization. The decay parameter rho and kernel K are modelling choices, not arithmetic facts about primes.

- rho = 1 gives equal weight to all recorded positions.
- 0 < rho < 1 makes recent positions contribute more.
- A finite-window version can discard entries older than a chosen number of steps.

Thus **memory path** is the ordered source data; **afterimage** is one observation or rendering derived from it. A rendering can blur or forget information that the ordered path still retains.

## 4. Fold and the lost orientation

Suppose a Fold involution F acts on the geometric state space. Its quotient chart identifies x and F(x). Projecting a memory path pointwise gives
\[
\overline M_k=([P_1],\ldots,[P_k]).
\]
This quotient history preserves orbit-level positions but forgets which representative was visited whenever x and F(x) are distinct.

To reconstruct the representative sequence, choose a section s of the quotient and record a selector b_i in {0,1} at each step:
\[
P_i=
\begin{cases}
s([P_i]),&b_i=0,\\
F(s([P_i])),&b_i=1.
\end{cases}
\]
For a two-element orbit, one bit per observation is sufficient. On the fixed set, the two choices coincide and the bit is redundant. This is the same representative-reconstruction boundary formalized in Fold/ArrivalFold.lean; it is not a claim that all quotient spaces need one bit.

The afterimage can therefore be built at three distinct information levels:

- **orbit afterimage:** remembers quotient positions, not side;
- **oriented afterimage:** retains the representative selector;
- **full memory path:** retains the ordered states and any additional metadata explicitly included in the state.

## 5. What the spiral does and does not say

The geometry can reveal alignments among prime labels under the chosen placement. In the Ulam spiral, such alignments are connected to arithmetic progressions and congruence structure. But the afterimage interpretation does not by itself explain those alignments, prove a prime-pattern conjecture, or establish a causal memory process.

A defensible analysis must specify:

1. the exact spiral map U and orientation;
2. whether the path advances through every integer or jumps only between prime labels;
3. whether memory stores positions, labels, directions, timestamps, or all of them;
4. the afterimage rule (set, weighted field, or finite window);
5. the Fold action, if any, and the information discarded by its quotient.

## 6. Minimal exact claims

For any fixed U and prime sequence:

- M_k has exactly k entries.
- M_k is a prefix of M_{k+1}.
- A_k is the set of positions in the first k-1 entries.
- The current position P_k is recoverable from M_k as its final entry.
- The ordered path can be recovered from the complete memory states by taking successive appended entries.
- A quotient afterimage cannot distinguish representatives within a Fold-orbit unless representative data is retained.

These are bookkeeping theorems about the declared construction. Prime-distribution claims require separate number theory.

## Interpretation

The prime spiral is the **spatial trace**; the memory path is the **ordered history**; the afterimage is the **visible residue of that history under a chosen observation rule**. The three coincide only when the observation preserves all of the path's information.

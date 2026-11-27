# Synchronized arrival at different rates

This note records a precise, deliberately limited interpretation of the statement:

> Everything reaches first at the same time at different speeds.

The mathematical content is **simultaneous arrival with unequal rates**. It is not a universal law that unrelated processes must synchronize.

## Discrete model

Fix a destination D in Z, an arrival time T in N, and a rate v in N. For times 0 <= t <= T, define

    x_(v,T)(t) = D - v(T - t).

Then x_(v,T)(T) = D for every rate v. Thus all members of this family arrive at the same destination at the same time. Their one-tick displacement is v, so distinct rates remain distinct.

For two rates a < b and positive remaining time r, a*r < b*r. The faster trajectory has a larger remaining displacement when both trajectories are measured against the same destination and the same remaining time.

## What is and is not invariant

- **Shared:** destination D, arrival time T.
- **Variable:** rate v, initial position D-vT, and the path between start and arrival.
- **Not implied:** equal distance, equal path, equal energy, equal acceleration, or spontaneous synchronization of arbitrary systems.

The path formula is a constant-rate discrete model. Its natural-number subtraction is intended for 0 <= t <= T.

## Relation to Origin → Fold

The synchronization condition is a level-set condition on a family of trajectories:

    for every v, x_(v,T)(T) = D.

It is not itself an involution, a reflection, or a quotient. A Fold operation may be applied to trajectory states only after specifying the state space and proving that the operation is involutive. Synchronization alone does not supply that proof.

## Formalization

Fold/Synchronization.lean proves:

- every speed-indexed path reaches the common destination at T;
- the discrete-rate encoding is injective;
- distinct rates can share the same arrival event;
- a larger rate gives a larger remaining displacement for positive remaining time.

These are exact statements about the declared discrete model, not empirical claims about all physical processes.

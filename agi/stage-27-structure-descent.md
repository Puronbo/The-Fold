# Stage 27 — Quotient Maps, Homomorphisms, and Structure-Preserving Abstraction

## Core question

When does an operation on the original state space define an unambiguous operation on its quotient?

Let ~ be the orbit equivalence relation from Stage 26. For an n-ary operation f:X^n -> X, the necessary and sufficient congruence condition is

    x_i ~ y_i for every i  =>  f(x_1,...,x_n) ~ f(y_1,...,y_n).

If this holds, define

    f_bar([x_1],...,[x_n]) = [f(x_1,...,x_n)].

Congruence guarantees that this definition does not depend on chosen representatives.

## Quotient projection

Let q:X -> X/~ map each state to its orbit class. The induced operation satisfies

    q(f(x_1,...,x_n)) = f_bar(q(x_1),...,q(x_n)).

This is the homomorphism identity: the projection preserves the operation.

For a finite total operation table, the implementation checks every tuple of quotient classes and every combination of original representatives. It emits a quotient table only if all outputs land in one class for each quotient input tuple.

## Example: XOR and a congruence

On X={0,1,2,3}, let x~y when x and y differ by XOR with 1. The classes are {0,1} and {2,3}. For bitwise XOR, the induced quotient operation is well-defined:

| quotient inputs | quotient output |
|---|---|
| (0,0) | 0 |
| (0,1) | 1 |
| (1,0) | 1 |
| (1,1) | 0 |

Here class 0 is {0,1} and class 1 is {2,3}. The quotient retains the XOR structure at the class level.

## Counterexample: a partition that is not a congruence

For addition modulo 4 with the same partition, equivalent inputs can produce outputs in different classes. The exhaustive check tests independent replacement of every argument, rather than only simultaneous transformations.

## Implementation

- agi/structure_descent.py: finite total-operation validation and quotient-table construction.
- agi/test_structure_descent.py: tests for unary and binary operations, valid and invalid congruences, incomplete tables, duplicate entries, and invalid states.
- descend_operations(quotient, operations): accepts a Stage 26 quotient report and named finite operation tables.

Tables must be total over the original finite state set and have fixed positive arity. Partial operations and nullary operations are excluded in this stage.

## Limits

The implementation verifies finite supplied tables. It does not infer operations from observations, learn which algebraic structure is useful, or show that a chosen quotient preserves every property relevant to a task. Congruence is always relative to the operations actually checked.

This is a formal structure-preservation component for abstraction and concept learning, not an AGI result.

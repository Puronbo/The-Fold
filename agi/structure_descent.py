"""Finite operation descent through a verified orbit quotient."""
from __future__ import annotations
from dataclasses import dataclass
from itertools import product
from typing import Hashable, Sequence
from agi.quotient_spaces import OrbitQuotientReport

OperationTable = Sequence[tuple[tuple[Hashable, ...], Hashable]]

@dataclass(frozen=True)
class OperationDescent:
    name: str
    arity: int
    congruence_verified: bool
    status: str
    quotient_table: tuple[tuple[tuple[int, ...], int], ...] | None
    checked_class_tuples: int

@dataclass(frozen=True)
class StructureDescentReport:
    status: str
    valid_quotient: bool
    operations: tuple[OperationDescent, ...]
    all_operations_descend: bool
    quotient_projection_is_homomorphism: bool

def descend_operations(quotient: OrbitQuotientReport, operations: Sequence[tuple[str, OperationTable]]) -> StructureDescentReport:
    """Check total finite operations for congruence and induce quotient tables."""
    if not quotient.valid_group_action:
        raise ValueError("a valid orbit quotient is required")
    states = tuple(state for state, _ in quotient.state_to_class)
    class_of = dict(quotient.state_to_class)
    n_classes = quotient.quotient_state_count
    names = [name for name, _ in operations]
    if any(not isinstance(name, str) or not name.strip() for name in names):
        raise ValueError("operation names must be non-empty strings")
    if len(names) != len(set(names)):
        raise ValueError("operation names must be unique")
    reports = []
    for name, raw_table in operations:
        rows = tuple((tuple(args), result) for args, result in raw_table)
        if not rows:
            raise ValueError("operation table must not be empty")
        arities = {len(args) for args, _ in rows}
        if len(arities) != 1:
            raise ValueError("operation table must have one fixed arity")
        arity = next(iter(arities))
        if arity < 1:
            raise ValueError("operation arity must be at least one")
        table = {}
        for args, result in rows:
            if any(arg not in class_of for arg in args) or result not in class_of:
                raise ValueError("operation entries must use quotient states")
            if args in table:
                raise ValueError("operation input tuples must be unique")
            table[args] = result
        expected = set(product(states, repeat=arity))
        if set(table) != expected:
            raise ValueError("operation table must be total over the original state set")
        quotient_rows = []
        congruence = True
        checked = 0
        for class_args in product(range(n_classes), repeat=arity):
            members = [[state for state in states if class_of[state] == c] for c in class_args]
            output_classes = {class_of[table[args]] for args in product(*members)}
            checked += 1
            if len(output_classes) != 1:
                congruence = False
                break
            quotient_rows.append((tuple(class_args), next(iter(output_classes))))
        reports.append(OperationDescent(name, arity, congruence,
            "operation_descends" if congruence else "congruence_failed",
            tuple(quotient_rows) if congruence else None, checked))
    all_descend = all(r.congruence_verified for r in reports)
    return StructureDescentReport(
        "all_operations_descend" if all_descend else "one_or_more_operations_do_not_descend",
        True, tuple(reports), all_descend, all_descend)


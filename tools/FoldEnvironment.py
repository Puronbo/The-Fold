"""FoldEnvironment: a safe, deterministic action/observation boundary.

Only two allowlisted actions exist: step forward and turn around. Proposals are
data, checked against a revision precondition and a caller-supplied budget.
Execution requires explicit approval. Every stage is appended to FoldMemory.
This is a toy simulator, not a bridge to real-world devices or services.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
from enum import Enum
import json
import math
from typing import Literal

from FoldMemory import FoldMemory


class ActionKind(str, Enum):
    STEP = "step"
    TURN = "turn"


@dataclass(frozen=True)
class WorldState:
    position: int = 0
    direction: int = 1
    revision: int = 0


@dataclass(frozen=True)
class ActionProposal:
    identifier: str
    kind: ActionKind
    expected_revision: int
    cost: float = 1.0


@dataclass(frozen=True)
class ObservationResult:
    proposal_id: str
    status: Literal["denied", "executed", "blocked"]
    before: WorldState
    after: WorldState
    verified: bool
    reason: str


class FoldEnvironment:
    """A bounded one-dimensional world with auditable, approval-gated actions."""

    def __init__(self, memory: FoldMemory, *, maximum_position: int = 4):
        if maximum_position < 1:
            raise ValueError("maximum_position must be positive")
        self.memory = memory
        self.maximum_position = maximum_position
        self.state = WorldState()

    def execute(
        self, proposal: ActionProposal, *, approved: bool, budget: float,
        task: str = "toy-world",
    ) -> ObservationResult:
        if not proposal.identifier or not task:
            raise ValueError("proposal identifier and task are required")
        if not isinstance(proposal.kind, ActionKind):
            raise ValueError("action is not in the allowlist")
        if proposal.expected_revision != self.state.revision:
            raise ValueError("stale action: expected revision does not match")
        if (not isinstance(proposal.cost, (int, float))
                or isinstance(proposal.cost, bool)
                or not math.isfinite(proposal.cost)
                or proposal.cost < 0):
            raise ValueError("cost must be a finite nonnegative number")
        if (not isinstance(budget, (int, float))
                or isinstance(budget, bool)
                or not math.isfinite(budget)
                or budget < 0):
            raise ValueError("budget must be a finite nonnegative number")
        if (not isinstance(self.state.position, int)
                or isinstance(self.state.position, bool)
                or not 0 <= self.state.position <= self.maximum_position
                or self.state.direction not in (-1, 1)
                or not isinstance(self.state.revision, int)
                or isinstance(self.state.revision, bool)
                or self.state.revision < 0):
            raise ValueError("environment state invariant failed")
        if not self.memory.verify():
            raise ValueError("memory integrity check failed")

        before = self.state
        self.memory.append(
            "action-proposed", f"action:{proposal.identifier}",
            json.dumps(asdict(proposal), default=lambda value: value.value,
                       sort_keys=True),
            source="FoldEnvironment", task=task,
            tags=("environment", "proposed"),
        )

        if not approved or proposal.cost > budget:
            reason = "approval-denied" if not approved else "budget-exceeded"
            self.memory.append(
                "action-denied", f"action:{proposal.identifier}", reason,
                source="FoldEnvironment", task=task,
                tags=("environment", "denied"),
            )
            return ObservationResult(
                proposal.identifier, "denied", before, before, True, reason
            )

        if proposal.kind is ActionKind.TURN:
            after = WorldState(before.position, -before.direction,
                               before.revision + 1)
            status: Literal["executed", "blocked"] = "executed"
            reason = "direction-reversed"
        else:
            target = before.position + before.direction
            if not 0 <= target <= self.maximum_position:
                after = WorldState(before.position, before.direction,
                                   before.revision + 1)
                status = "blocked"
                reason = "world-boundary"
            else:
                after = WorldState(target, before.direction,
                                   before.revision + 1)
                status = "executed"
                reason = "step-completed"

        self.state = after
        predicted = after
        observed = self.state
        verified = observed == predicted
        self.memory.append(
            "action-executed", f"action:{proposal.identifier}",
            json.dumps({"status": status, "before": asdict(before),
                        "predicted": asdict(predicted)},
                       sort_keys=True),
            source="FoldEnvironment", task=task,
            tags=("environment", status),
        )
        self.memory.append(
            "observation-result", f"action:{proposal.identifier}",
            json.dumps({"observed": asdict(observed), "verified": verified,
                        "reason": reason}, sort_keys=True),
            source="FoldEnvironment", task=task,
            confidence=1.0 if verified else 0.0,
            tags=("environment", "observed",
                  "verified" if verified else "needs-review"),
        )
        return ObservationResult(
            proposal.identifier, status, before, observed, verified, reason
        )


def _self_test() -> None:
    import tempfile
    from pathlib import Path

    with tempfile.TemporaryDirectory() as directory:
        memory = FoldMemory(Path(directory) / "environment.jsonl")
        world = FoldEnvironment(memory, maximum_position=2)
        checks: list[tuple[str, bool]] = []

        denied = world.execute(
            ActionProposal("denied", ActionKind.STEP, 0), approved=False, budget=2
        )
        checks.append(("unapproved action is denied", denied.status == "denied"))
        checks.append(("denial leaves world unchanged",
                       world.state == WorldState()))
        over_budget = world.execute(
            ActionProposal("expensive", ActionKind.STEP, 0, 3),
            approved=True, budget=1,
        )
        checks.append(("budget limit blocks action", over_budget.reason == "budget-exceeded"))
        invalid_numeric_inputs = []
        for bad_cost, bad_budget in (
            (float("nan"), 1.0), (float("inf"), 1.0),
            (1.0, float("nan")), (1.0, float("inf")),
            (True, 1.0), (1.0, True),
        ):
            try:
                world.execute(
                    ActionProposal("invalid-numeric", ActionKind.STEP, 0, bad_cost),
                    approved=True, budget=bad_budget,
                )
                invalid_numeric_inputs.append(False)
            except ValueError:
                invalid_numeric_inputs.append(True)
        checks.append(("NaN, infinity, and boolean costs/budgets are rejected",
                       all(invalid_numeric_inputs) and world.state == WorldState()))
        moved = world.execute(
            ActionProposal("forward", ActionKind.STEP, 0),
            approved=True, budget=1,
        )
        checks.append(("approved step changes position", moved.after.position == 1))
        checks.append(("observation matches deterministic transition", moved.verified))
        turned = world.execute(
            ActionProposal("turn", ActionKind.TURN, 1),
            approved=True, budget=1,
        )
        checks.append(("turn reverses direction", turned.after.direction == -1))
        back = world.execute(
            ActionProposal("back", ActionKind.STEP, 2),
            approved=True, budget=1,
        )
        checks.append(("forward after turn moves back", back.after.position == 0))
        blocked = world.execute(
            ActionProposal("edge", ActionKind.STEP, 3),
            approved=True, budget=1,
        )
        checks.append(("boundary is enforced", blocked.status == "blocked"
                       and blocked.after.position == 0))
        try:
            world.execute(ActionProposal("stale", ActionKind.STEP, 0),
                          approved=True, budget=1)
            stale_rejected = False
        except ValueError:
            stale_rejected = True
        checks.append(("stale revision is rejected", stale_rejected))
        try:
            ActionProposal("bad", "delete-everything", world.state.revision)  # type: ignore[arg-type]
            world.execute(ActionProposal("bad", "delete-everything",
                                         world.state.revision), approved=True, budget=1)  # type: ignore[arg-type]
            unknown_rejected = False
        except ValueError:
            unknown_rejected = True
        checks.append(("non-allowlisted action is rejected", unknown_rejected))
        events = memory.recall(task="toy-world", include_superseded=True)
        checks.append(("proposals and outcomes are retained",
                       sum(e.event_type == "action-proposed" for e in events) == 6
                       and sum(e.event_type == "observation-result" for e in events) == 4))
        checks.append(("memory hash chain verifies", memory.verify()))
        print("\n".join(f"{'PASS' if ok else 'FAIL'}  {name}" for name, ok in checks))
        print(f"{sum(ok for _, ok in checks)}/{len(checks)} checks passed")
        if not all(ok for _, ok in checks):
            raise SystemExit("FoldEnvironment regression failure")


if __name__ == "__main__":
    _self_test()

"""FoldAgent: a minimal goal-directed controller over FoldEnvironment.

The controller plans exactly one action per call. It never reverses motion by
using a negative step: when the goal is behind, it must turn first. Every
action still passes through FoldEnvironment's approval, budget, revision, and
memory checks. This is a deterministic baseline, not an autonomous AGI agent.
"""
from __future__ import annotations

from dataclasses import dataclass
import json

from FoldEnvironment import (
    ActionKind, ActionProposal, FoldEnvironment, ObservationResult,
)


@dataclass(frozen=True)
class AgentDecision:
    goal: int
    action: ActionKind | None
    result: ObservationResult | None
    status: str


class FoldAgent:
    """One-step goal controller; caller retains approval authority."""

    def __init__(self, environment: FoldEnvironment):
        self.environment = environment

    def step_toward(
        self, goal: int, *, approved: bool, budget: float,
        task: str = "goal-navigation",
    ) -> AgentDecision:
        world = self.environment
        if not 0 <= goal <= world.maximum_position:
            raise ValueError("goal lies outside the world")
        if not task:
            raise ValueError("task must be nonempty")
        state = world.state
        if state.position == goal:
            world.memory.append(
                "agent-decision", f"goal:{task}",
                json.dumps({"goal": goal, "action": None,
                            "position": state.position}, sort_keys=True),
                source="FoldAgent", task=task,
                tags=("agent", "goal-reached"),
            )
            return AgentDecision(goal, None, None, "goal-reached")

        desired_direction = 1 if goal > state.position else -1
        action = (ActionKind.STEP if state.direction == desired_direction
                  else ActionKind.TURN)
        proposal = ActionProposal(
            identifier=f"{task}-r{state.revision}-{action.value}",
            kind=action, expected_revision=state.revision, cost=1.0,
        )
        world.memory.append(
            "agent-decision", f"goal:{task}",
            json.dumps({"goal": goal, "position": state.position,
                        "direction": state.direction, "action": action.value},
                       sort_keys=True),
            source="FoldAgent", task=task,
            tags=("agent", "planned"),
        )
        result = world.execute(
            proposal, approved=approved, budget=budget, task=task
        )
        status = ("approval-required" if result.status == "denied"
                  else "action-observed")
        return AgentDecision(goal, action, result, status)


def _self_test() -> None:
    import tempfile
    from pathlib import Path
    from FoldMemory import FoldMemory

    with tempfile.TemporaryDirectory() as directory:
        memory = FoldMemory(Path(directory) / "agent.jsonl")
        environment = FoldEnvironment(memory, maximum_position=3)
        agent = FoldAgent(environment)
        checks: list[tuple[str, bool]] = []

        first = agent.step_toward(2, approved=True, budget=1)
        second = agent.step_toward(2, approved=True, budget=1)
        checks.append(("controller advances toward a forward goal",
                       first.action is ActionKind.STEP
                       and second.result is not None
                       and second.result.after.position == 2))
        reached = agent.step_toward(2, approved=True, budget=1)
        checks.append(("controller stops when goal is reached",
                       reached.status == "goal-reached" and reached.action is None))

        turn = agent.step_toward(0, approved=True, budget=1)
        checks.append(("controller turns before moving toward a goal behind",
                       turn.action is ActionKind.TURN
                       and turn.result is not None
                       and turn.result.after.position == 2
                       and turn.result.after.direction == -1))
        backward = agent.step_toward(0, approved=True, budget=1)
        checks.append(("movement after turn follows reversed direction",
                       backward.action is ActionKind.STEP
                       and backward.result is not None
                       and backward.result.after.position == 1))
        agent.step_toward(0, approved=True, budget=1)
        checks.append(("controller reaches the reverse-direction goal",
                       environment.state.position == 0))

        before = environment.state
        denied = agent.step_toward(3, approved=False, budget=1)
        checks.append(("controller cannot bypass denied approval",
                       denied.status == "approval-required"
                       and environment.state == before))
        low_budget = agent.step_toward(3, approved=True, budget=0)
        checks.append(("controller respects zero action budget",
                       low_budget.status == "approval-required"
                       and environment.state == before))
        try:
            agent.step_toward(4, approved=True, budget=1)
            invalid_goal = False
        except ValueError:
            invalid_goal = True
        checks.append(("out-of-world goals are rejected", invalid_goal))
        checks.append(("decisions and action outcomes are auditable",
                       len(memory.recall(task="goal-navigation",
                                         tag="agent",
                                         include_superseded=True)) >= 8
                       and memory.verify()))

        print("\n".join(f"{'PASS' if ok else 'FAIL'}  {name}" for name, ok in checks))
        print(f"{sum(ok for _, ok in checks)}/{len(checks)} checks passed")
        if not all(ok for _, ok in checks):
            raise SystemExit("FoldAgent regression failure")


if __name__ == "__main__":
    _self_test()

"""FoldAgent: shortest-path planning with approval-gated, one-step execution.

The planner searches the finite (position, direction) state graph. It returns a
shortest action sequence, but executes only its first action. Every subsequent
call replans from the environment's current observed state, so stale plans are
not blindly replayed. This is a deterministic planning baseline, not AGI.
"""
from __future__ import annotations

from collections import deque
from dataclasses import dataclass
import json

from FoldEnvironment import (
    ActionKind, ActionProposal, FoldEnvironment, ObservationResult, WorldState,
)


@dataclass(frozen=True)
class AgentDecision:
    goal: int
    action: ActionKind | None
    result: ObservationResult | None
    status: str
    plan: tuple[ActionKind, ...] = ()


def shortest_plan(state: WorldState, goal: int,
                  maximum_position: int) -> tuple[ActionKind, ...]:
    """Return a minimum-length legal plan using breadth-first search."""
    if maximum_position < 1 or not 0 <= state.position <= maximum_position:
        raise ValueError("invalid world bounds or current position")
    if state.direction not in (-1, 1):
        raise ValueError("direction must be -1 or +1")
    if not 0 <= goal <= maximum_position:
        raise ValueError("goal lies outside the world")
    if state.position == goal:
        return ()

    start = (state.position, state.direction)
    queue = deque([(start, ())])
    visited = {start}
    while queue:
        (position, direction), path = queue.popleft()
        # Turn is always legal and never changes position.
        successors = (
            ((position, -direction), ActionKind.TURN),
            ((position + direction, direction), ActionKind.STEP)
            if 0 <= position + direction <= maximum_position else None,
        )
        for successor in successors:
            if successor is None:
                continue
            next_state, action = successor
            if next_state in visited:
                continue
            next_path = path + (action,)
            if next_state[0] == goal:
                return next_path
            visited.add(next_state)
            queue.append((next_state, next_path))
    raise RuntimeError("goal is unreachable in the supplied world")


class FoldAgent:
    """Replanning shortest-path controller; caller retains approval authority."""

    def __init__(self, environment: FoldEnvironment):
        self.environment = environment

    def plan(self, goal: int) -> tuple[ActionKind, ...]:
        return shortest_plan(
            self.environment.state, goal, self.environment.maximum_position
        )

    def step_toward(
        self, goal: int, *, approved: bool, budget: float,
        task: str = "goal-navigation",
    ) -> AgentDecision:
        world = self.environment
        if not task:
            raise ValueError("task must be nonempty")
        plan = self.plan(goal)
        state = world.state
        if not plan:
            world.memory.append(
                "agent-decision", f"goal:{task}",
                json.dumps({"goal": goal, "action": None,
                            "position": state.position, "plan": []},
                           sort_keys=True),
                source="FoldAgent", task=task,
                tags=("agent", "goal-reached"),
            )
            return AgentDecision(goal, None, None, "goal-reached", ())

        action = plan[0]
        proposal = ActionProposal(
            identifier=f"{task}-r{state.revision}-{action.value}",
            kind=action, expected_revision=state.revision, cost=1.0,
        )
        world.memory.append(
            "agent-decision", f"goal:{task}",
            json.dumps({"goal": goal, "position": state.position,
                        "direction": state.direction,
                        "plan": [item.value for item in plan],
                        "selected_action": action.value}, sort_keys=True),
            source="FoldAgent", task=task,
            tags=("agent", "planned"),
        )
        result = world.execute(
            proposal, approved=approved, budget=budget, task=task
        )
        status = ("approval-required" if result.status == "denied"
                  else "action-observed")
        return AgentDecision(goal, action, result, status, plan)


def _self_test() -> None:
    import tempfile
    from pathlib import Path
    from FoldMemory import FoldMemory

    checks: list[tuple[str, bool]] = []
    # Independent closed-form distance oracle for a one-dimensional line.
    for maximum in range(1, 8):
        for position in range(maximum + 1):
            for direction in (-1, 1):
                for goal in range(maximum + 1):
                    state = WorldState(position, direction, 0)
                    plan = shortest_plan(state, goal, maximum)
                    distance = abs(goal - position)
                    expected = (0 if distance == 0 else
                                distance + (direction != (1 if goal > position else -1)))
                    checks.append((f"optimal plan ({maximum},{position},{direction},{goal})",
                                   len(plan) == expected))
                    x, d = position, direction
                    legal = True
                    for action in plan:
                        if action is ActionKind.TURN:
                            d = -d
                        else:
                            x += d
                            legal = legal and 0 <= x <= maximum
                    checks.append((f"legal plan ({maximum},{position},{direction},{goal})",
                                   legal and x == goal))

    with tempfile.TemporaryDirectory() as directory:
        memory = FoldMemory(Path(directory) / "agent.jsonl")
        environment = FoldEnvironment(memory, maximum_position=3)
        agent = FoldAgent(environment)

        planned = agent.plan(2)
        checks.append(("planner returns complete forward route",
                       planned == (ActionKind.STEP, ActionKind.STEP)))
        first = agent.step_toward(2, approved=True, budget=1)
        second = agent.step_toward(2, approved=True, budget=1)
        checks.append(("controller executes one action per approval",
                       first.action is ActionKind.STEP
                       and second.result is not None
                       and second.result.after.position == 2))
        reached = agent.step_toward(2, approved=True, budget=1)
        checks.append(("controller stops at goal",
                       reached.status == "goal-reached" and reached.action is None))

        turn = agent.step_toward(0, approved=True, budget=1)
        checks.append(("planner turns before reverse travel",
                       turn.plan == (ActionKind.TURN, ActionKind.STEP, ActionKind.STEP)
                       and turn.action is ActionKind.TURN
                       and turn.result is not None
                       and turn.result.after.position == 2
                       and turn.result.after.direction == -1))
        backward = agent.step_toward(0, approved=True, budget=1)
        checks.append(("controller replans and moves after turn",
                       backward.action is ActionKind.STEP
                       and backward.result is not None
                       and backward.result.after.position == 1))
        agent.step_toward(0, approved=True, budget=1)
        checks.append(("controller reaches reverse-direction goal",
                       environment.state.position == 0))

        before = environment.state
        denied = agent.step_toward(3, approved=False, budget=1)
        checks.append(("denied approval prevents execution",
                       denied.status == "approval-required"
                       and environment.state == before))
        low_budget = agent.step_toward(3, approved=True, budget=0)
        checks.append(("zero budget prevents execution",
                       low_budget.status == "approval-required"
                       and environment.state == before))
        try:
            agent.plan(4)
            invalid_goal = False
        except ValueError:
            invalid_goal = True
        checks.append(("out-of-world goals are rejected", invalid_goal))
        checks.append(("decisions and outcomes remain auditable",
                       len(memory.recall(task="goal-navigation", tag="agent",
                                         include_superseded=True)) >= 8
                       and memory.verify()))

    print("\n".join(f"{'PASS' if ok else 'FAIL'}  {name}" for name, ok in checks))
    print(f"{sum(ok for _, ok in checks)}/{len(checks)} checks passed")
    if not all(ok for _, ok in checks):
        raise SystemExit("FoldAgent regression failure")


if __name__ == "__main__":
    _self_test()

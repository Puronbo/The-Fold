# Stage 18 — Active experiment design

## Goal

Choose a candidate input at which fixed competing relational models make distinguishable predictions. This is finite, deterministic active experiment design, not autonomous physical experimentation.

## API

`design_discriminating_experiment(candidates, candidate_inputs)` accepts existing `RelationCandidate` objects and a caller-supplied finite set of exact integer or rational inputs. It evaluates each candidate's exact composed relation at each input.

For an input (x), let (P_x) be the multiset of defined predictions. The primary score is the exact total pairwise separation

[
S(x)=\sum_{i<j}|p_i-p_j|,\qquad p_i,p_j\in P_x.
]

The deterministic tie-breaks are greater candidate coverage, more distinct predictions, then smaller numeric input. An input is informative only when at least two candidates are defined and at least two predictions differ.

## Safeguards and limitations

- Undefined predictions reduce coverage; they are not treated as agreement.
- Inputs must be supplied by the caller. The module neither invents a feasible physical intervention nor executes one.
- Integers and `Fraction` values are accepted; floats and booleans are rejected.
- All calculations use exact rational arithmetic.
- Equivalent candidate paths do not create artificial disagreement.
- If no supplied input distinguishes at least two defined candidates, status is `no_discriminating_input`.
- The separation score depends on the output scale and is a transparent heuristic, not a universal information-gain or utility measure.
- No costs, safety constraints, measurement noise, causal assumptions, or experiment feasibility are inferred.
- A selected input is a mathematical recommendation for further review, not an instruction to perform a real-world experiment.

## Scope

Stage 18 closes a narrow loop from model comparison to a proposed discriminating query. It does not establish causal discovery, scientific autonomy, general program synthesis, or AGI. Real active learning would additionally need uncertainty models, feasible-action constraints, acquisition objectives, observation ingestion, and protection against adaptive test leakage.

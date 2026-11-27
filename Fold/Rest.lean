/-
  Fold/Rest.lean

  Rest as a fixed-state condition: when the declared motion component is
  zero, a rest-preserving evolution leaves both position and motion unchanged.
  This is a formal model condition, not a universal physical law.
-/

namespace Fold

/-- A one-dimensional kinematic state with position and signed velocity. -/
structure MotionState where
  position : Int
  velocity : Int
  deriving DecidableEq, Repr

/-- Rest is defined relative to the chosen frame and motion variable. -/
def AtRest (s : MotionState) : Prop :=
  s.velocity = 0

/-- A dynamics map preserves rest pointwise when every rest state is fixed. -/
def RestInvariant (evolve : MotionState → MotionState) : Prop :=
  ∀ s, AtRest s → evolve s = s

/-- Under rest invariance, the position component is unchanged. -/
theorem rest_position_unchanged
    (evolve : MotionState → MotionState)
    (hinv : RestInvariant evolve)
    (s : MotionState) (hrest : AtRest s) :
    (evolve s).position = s.position := by
  have h := hinv s hrest
  exact congrArg MotionState.position h

/-- Under rest invariance, the motion component is unchanged. -/
theorem rest_motion_unchanged
    (evolve : MotionState → MotionState)
    (hinv : RestInvariant evolve)
    (s : MotionState) (hrest : AtRest s) :
    (evolve s).velocity = s.velocity := by
  have h := hinv s hrest
  exact congrArg MotionState.velocity h

/-- The complete state is unchanged at rest. -/
theorem rest_state_fixed
    (evolve : MotionState → MotionState)
    (hinv : RestInvariant evolve)
    (s : MotionState) (hrest : AtRest s) :
    evolve s = s :=
  hinv s hrest

/-- A simple model evolution: moving states may be updated by a supplied
    transition, while rest states are fixed. -/
def holdAtRest (movingStep : MotionState → MotionState)
    (s : MotionState) : MotionState :=
  if h : AtRest s then s else movingStep s

/-- The hold-at-rest construction satisfies the stated invariant. -/
theorem holdAtRest_invariant (movingStep : MotionState → MotionState) :
    RestInvariant (holdAtRest movingStep) := by
  intro s hrest
  simp [holdAtRest, hrest]

end Fold

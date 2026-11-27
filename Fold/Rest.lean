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
  if h : s.velocity = 0 then s else movingStep s

/-- The hold-at-rest construction satisfies the stated invariant. -/
theorem holdAtRest_invariant (movingStep : MotionState → MotionState) :
    RestInvariant (holdAtRest movingStep) := by
  intro s hrest
  simp [holdAtRest, hrest]


/-- Rest can coexist with a changing internal condition or environment. -/
structure RestContextState where
  position : Int
  velocity : Int
  condition : Int
  deriving DecidableEq, Repr

/-- The kinematic components are at rest; condition is deliberately separate. -/
def ContextAtRest (s : RestContextState) : Prop :=
  s.velocity = 0

/-- Differential rest: position and zero motion persist, while condition changes. -/
def DifferentialRest (before after : RestContextState) : Prop :=
  before.position = after.position ∧
  before.velocity = 0 ∧ after.velocity = 0 ∧
  before.condition ≠ after.condition

/-- A transition may update only the condition while the kinematic state rests. -/
def conditionOnlyStep (update : Int → Int) (s : RestContextState) :
    RestContextState :=
  if h : s.velocity = 0 then
    { s with condition := update s.condition }
  else s

/-- The condition-only step preserves position during rest. -/
theorem conditionOnlyStep_position
    (update : Int → Int) (s : RestContextState)
    (hrest : ContextAtRest s) :
    (conditionOnlyStep update s).position = s.position := by
  simp [conditionOnlyStep, hrest]

/-- The condition-only step preserves zero velocity during rest. -/
theorem conditionOnlyStep_velocity
    (update : Int → Int) (s : RestContextState)
    (hrest : ContextAtRest s) :
    (conditionOnlyStep update s).velocity = 0 := by
  simp [conditionOnlyStep, hrest, hrest]

/-- If the internal condition update differs, differential rest is obtained. -/
theorem conditionOnlyStep_differentialRest
    (update : Int → Int) (s : RestContextState)
    (hrest : ContextAtRest s)
    (hchange : update s.condition ≠ s.condition) :
    DifferentialRest s (conditionOnlyStep update s) := by
  simp [DifferentialRest, conditionOnlyStep, hrest, hchange]

/-- The two states can differ while their position and velocity agree. -/
theorem differentialRest_states_differ
    (before after : RestContextState)
    (h : DifferentialRest before after) :
    before ≠ after := by
  intro heq
  have hcond := h.2.2.2
  apply hcond
  exact congrArg RestContextState.condition heq

end Fold

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
  simp [conditionOnlyStep, ContextAtRest, hrest]

/-- The condition-only step preserves zero velocity during rest. -/
theorem conditionOnlyStep_velocity
    (update : Int → Int) (s : RestContextState)
    (hrest : ContextAtRest s) :
    (conditionOnlyStep update s).velocity = 0 := by
  simp [conditionOnlyStep, ContextAtRest, hrest]

/-- If the internal condition update differs, differential rest is obtained. -/
theorem conditionOnlyStep_differentialRest
    (update : Int → Int) (s : RestContextState)
    (hrest : ContextAtRest s)
    (hchange : update s.condition ≠ s.condition) :
    DifferentialRest s (conditionOnlyStep update s) := by
  simp [DifferentialRest, conditionOnlyStep, ContextAtRest, hrest, hchange]

/-- The two states can differ while their position and velocity agree. -/
theorem differentialRest_states_differ
    (before after : RestContextState)
    (h : DifferentialRest before after) :
    before ≠ after := by
  intro heq
  have hcond := h.2.2.2
  apply hcond
  exact congrArg RestContextState.condition heq


/-- The predicted next velocity may depend on the internal condition. -/
def predictedVelocity (law : Int → Int) (s : RestContextState) : Int :=
  law s.condition

/-- A changed condition can alter the next-step prediction without moving now. -/
theorem differentialRest_changes_prediction
    (law : Int → Int) (update : Int → Int) (s : RestContextState)
    (hrest : ContextAtRest s)
    (hprediction :
      law (update s.condition) ≠ law s.condition) :
    predictedVelocity law (conditionOnlyStep update s) ≠
      predictedVelocity law s := by
  simp [predictedVelocity, conditionOnlyStep, ContextAtRest, hrest,
    hprediction]


/-- A rest state whose internal condition has a discrete change rate. -/
structure RateRestState where
  position : Int
  velocity : Int
  condition : Int
  conditionRate : Int
  deriving DecidableEq, Repr

/-- Kinematic rest is independent of the internal condition rate. -/
def RateContextAtRest (s : RateRestState) : Prop :=
  s.velocity = 0

/-- Differential-rate rest: position and zero velocity persist,
    while the internal condition rate changes. -/
def DifferentialRateRest (before after : RateRestState) : Prop :=
  before.position = after.position ∧
  before.velocity = 0 ∧ after.velocity = 0 ∧
  before.conditionRate ≠ after.conditionRate

/-- Advance the condition by its current rate, then update that rate. -/
def conditionRateStep (nextRate : Int → Int) (s : RateRestState) :
    RateRestState :=
  if h : s.velocity = 0 then
    { s with
      condition := s.condition + s.conditionRate
      conditionRate := nextRate s.conditionRate }
  else s

/-- Rate evolution during rest does not change position. -/
theorem conditionRateStep_position
    (nextRate : Int → Int) (s : RateRestState)
    (hrest : RateContextAtRest s) :
    (conditionRateStep nextRate s).position = s.position := by
  simp [conditionRateStep, RateContextAtRest, hrest]

/-- Rate evolution during rest leaves velocity zero. -/
theorem conditionRateStep_velocity
    (nextRate : Int → Int) (s : RateRestState)
    (hrest : RateContextAtRest s) :
    (conditionRateStep nextRate s).velocity = 0 := by
  simp [conditionRateStep, RateContextAtRest, hrest]

/-- If the internal rate changes, the transition is differential-rate rest. -/
theorem conditionRateStep_differentialRateRest
    (nextRate : Int → Int) (s : RateRestState)
    (hrest : RateContextAtRest s)
    (hrate : nextRate s.conditionRate ≠ s.conditionRate) :
    DifferentialRateRest s (conditionRateStep nextRate s) := by
  simp [DifferentialRateRest, conditionRateStep, RateContextAtRest,
    hrest, hrate]

/-- Differential-rate rest changes the complete augmented state. -/
theorem differentialRateRest_states_differ
    (before after : RateRestState)
    (h : DifferentialRateRest before after) :
    before ≠ after := by
  intro heq
  apply h.2.2.2
  exact congrArg RateRestState.conditionRate heq

end Fold

/-- A rest state with a second discrete derivative of its internal condition. -/
structure AccelRestState where
  position : Int
  velocity : Int
  condition : Int
  conditionRate : Int
  conditionAcceleration : Int
  deriving DecidableEq, Repr

/-- Kinematic rest remains a statement only about velocity. -/
def AccelContextAtRest (s : AccelRestState) : Prop :=
  s.velocity = 0

/-- Differential-acceleration rest changes the internal acceleration
    while position and zero velocity persist. -/
def DifferentialAccelerationRest
    (before after : AccelRestState) : Prop :=
  before.position = after.position ∧
  before.velocity = 0 ∧ after.velocity = 0 ∧
  before.conditionAcceleration ≠ after.conditionAcceleration

/-- Advance the internal condition and its rate, then update acceleration;
    position and velocity are held fixed at kinematic rest. -/
def conditionAccelerationStep
    (nextAcceleration : Int → Int) (s : AccelRestState) :
    AccelRestState :=
  if h : s.velocity = 0 then
    { s with
      condition := s.condition + s.conditionRate
      conditionRate := s.conditionRate + s.conditionAcceleration
      conditionAcceleration := nextAcceleration s.conditionAcceleration }
  else s

/-- Higher-order internal evolution preserves position at rest. -/
theorem conditionAccelerationStep_position
    (nextAcceleration : Int → Int) (s : AccelRestState)
    (hrest : AccelContextAtRest s) :
    (conditionAccelerationStep nextAcceleration s).position = s.position := by
  simp [conditionAccelerationStep, AccelContextAtRest, hrest]

/-- Higher-order internal evolution leaves velocity zero. -/
theorem conditionAccelerationStep_velocity
    (nextAcceleration : Int → Int) (s : AccelRestState)
    (hrest : AccelContextAtRest s) :
    (conditionAccelerationStep nextAcceleration s).velocity = 0 := by
  simp [conditionAccelerationStep, AccelContextAtRest, hrest]

/-- If the acceleration update differs, the transition is
    differential-acceleration rest. -/
theorem conditionAccelerationStep_differentialAccelerationRest
    (nextAcceleration : Int → Int) (s : AccelRestState)
    (hrest : AccelContextAtRest s)
    (haccel :
      nextAcceleration s.conditionAcceleration ≠ s.conditionAcceleration) :
    DifferentialAccelerationRest s
      (conditionAccelerationStep nextAcceleration s) := by
  simp [DifferentialAccelerationRest, conditionAccelerationStep,
    AccelContextAtRest, hrest, haccel]

/-- A change in internal acceleration makes the augmented states distinct. -/
theorem differentialAccelerationRest_states_differ
    (before after : AccelRestState)
    (h : DifferentialAccelerationRest before after) :
    before ≠ after := by
  intro heq
  apply h.2.2.2
  exact congrArg AccelRestState.conditionAcceleration heq

/-- A nonzero internal acceleration changes the next condition rate. -/
theorem conditionAccelerationStep_rate_changes
    (nextAcceleration : Int → Int) (s : AccelRestState)
    (hrest : AccelContextAtRest s)
    (hnonzero : s.conditionAcceleration ≠ 0) :
    (conditionAccelerationStep nextAcceleration s).conditionRate ≠
      s.conditionRate := by
  simp [conditionAccelerationStep, AccelContextAtRest, hrest]
  exact hnonzero


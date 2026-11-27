/-
  Fold/Origin.lean

  The retained-reference and direction-turn bookkeeping introduced after
  the affine scale family. These are explicit state models, not claims
  that arbitrary information survives a collapse or that all motion is
  discrete.
-/
import Fold.Scale

namespace Fold

/-- A value together with the designated reference retained by the model. -/
structure OriginState where
  value : Int
  reference : Int
  deriving DecidableEq, Repr

/-- Scale the value while leaving the designated reference untouched. -/
def scaleState (k : Int) (s : OriginState) : OriginState :=
  { value := k * s.value, reference := s.reference }

/-- The zero scale collapses the value coordinate only. -/
def collapseState (s : OriginState) : OriginState :=
  scaleState 0 s

/-- Recovery returns the retained reference as the value coordinate. -/
def recoverReference (s : OriginState) : OriginState :=
  { value := s.reference, reference := s.reference }

theorem scaleState_preserves_reference (k : Int) (s : OriginState) :
    (scaleState k s).reference = s.reference := rfl

theorem recoverReference_idempotent (s : OriginState) :
    recoverReference (recoverReference s) = recoverReference s := by
  cases s
  rfl

/-- The normalized reference example: (1,1) -> (0,1) -> (1,1). -/
theorem normalized_reference_roundtrip :
    recoverReference (collapseState ⟨1, 1⟩) = ⟨1, 1⟩ := rfl

/-- Distinct values can have the same collapsed state: collapse is lossy. -/
theorem collapse_forgets_value :
    collapseState ⟨1, 1⟩ = collapseState ⟨2, 1⟩ := rfl

theorem original_states_are_distinct :
    (⟨1, 1⟩ : OriginState) ≠ ⟨2, 1⟩ := by
  decide

/-- Two-valued direction tag for the discrete turn model. -/
inductive Direction where
  | forward
  | backward
  deriving DecidableEq, Repr

def reverseDirection : Direction → Direction
  | .forward => .backward
  | .backward => .forward

theorem reverseDirection_invol (d : Direction) :
    reverseDirection (reverseDirection d) = d := by
  cases d <;> rfl

/-- A turn reverses direction while retaining position and reference. -/
structure DirectedState where
  position : Int
  reference : Int
  direction : Direction
  deriving DecidableEq, Repr

def turn (s : DirectedState) : DirectedState :=
  { s with direction := reverseDirection s.direction }

theorem turn_invol (s : DirectedState) : turn (turn s) = s := by
  cases s with
  | mk position reference direction =>
    cases direction <;> rfl

theorem turn_preserves_position (s : DirectedState) :
    (turn s).position = s.position := rfl

theorem turn_preserves_reference (s : DirectedState) :
    (turn s).reference = s.reference := rfl

end Fold

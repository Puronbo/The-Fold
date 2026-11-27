/- 
  Fold/State.lean

  The state-level Fold invariants: collapse erases the observed value but
  preserves the retained reference, direction, and history.  The retained
  signature characterizes exactly when two collapsed states are equal.
-/
import Init

namespace Fold

structure State where
  value : Int
  reference : Int
  direction : Int
  history : List Int
  deriving DecidableEq, Repr

def collapse (s : State) : State :=
  { s with value := 0 }

def turn (s : State) : State :=
  { s with direction := -s.direction, history := s.history ++ [s.direction] }

def observe (s : State) : Int :=
  s.value

/-- The metadata that collapse leaves untouched. -/
def retainedSignature (s : State) : Int × Int × List Int :=
  (s.reference, s.direction, s.history)

theorem collapse_sets_value_to_zero (s : State) :
    (collapse s).value = 0 := rfl

theorem collapse_preserves_reference (s : State) :
    (collapse s).reference = s.reference := rfl

theorem collapse_preserves_signature (s : State) :
    retainedSignature (collapse s) = retainedSignature s := rfl

theorem collapse_idempotent (s : State) :
    collapse (collapse s) = collapse s := by
  cases s
  rfl

theorem turn_twice_restores_direction (s : State) :
    (turn (turn s)).direction = s.direction := by
  simp [turn]

theorem collapsed_observation_independent (s t : State) :
    observe (collapse s) = observe (collapse t) := rfl

theorem observation_only_classifier_cannot_recover_reference
    (classifier : Int → Bool) (s t : State) :
    classifier (observe (collapse s)) =
      classifier (observe (collapse t)) := rfl

/-- Two collapsed states are equal exactly when all retained metadata agrees. -/
theorem collapse_eq_iff_retained_signature_eq (s t : State) :
    collapse s = collapse t ↔ retainedSignature s = retainedSignature t := by
  cases s <;> cases t <;> simp [collapse, retainedSignature]

theorem distinct_references_survive_collapse
    (s t : State) (h : s.reference ≠ t.reference) :
    collapse s ≠ collapse t := by
  intro hc
  have hr := congrArg (fun state : State => state.reference) hc
  exact h (by simpa [collapse] using hr)

end Fold

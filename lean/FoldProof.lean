/-!
# FoldProof core invariants

A minimal formal core for the Fold state model. These theorems establish
properties of the definitions below; they do not prove AGI or new facts
about prime numbers.
-/

structure FoldState where
  value : Int
  reference : Int
  direction : Int
  history : List Int
  deriving DecidableEq, Repr

namespace FoldState

def collapse (s : FoldState) : FoldState :=
  { s with value := 0 }

def turn (s : FoldState) : FoldState :=
  { s with direction := -s.direction, history := s.history ++ [s.direction] }

def observe (s : FoldState) : Int :=
  s.value

theorem collapse_sets_value_to_zero (s : FoldState) :
    (collapse s).value = 0 := rfl

theorem collapse_preserves_reference (s : FoldState) :
    (collapse s).reference = s.reference := rfl

theorem collapse_is_idempotent (s : FoldState) :
    collapse (collapse s) = collapse s := by
  cases s
  rfl

theorem turn_twice_restores_direction (s : FoldState) :
    (turn (turn s)).direction = s.direction := by
  simp [turn]

theorem collapse_observation_independent (s t : FoldState) :
    observe (collapse s) = observe (collapse t) := rfl

theorem no_observation_only_classifier
    (classifier : Int → Bool) (s t : FoldState) :
    classifier (observe (collapse s)) =
      classifier (observe (collapse t)) := rfl

theorem distinct_references_survive_collapse
    (s t : FoldState) (h : s.reference ≠ t.reference) :
    collapse s ≠ collapse t := by
  intro hc
  have hr := congrArg (fun state : FoldState => state.reference) hc
  exact h (by simpa [collapse] using hr)

end FoldState

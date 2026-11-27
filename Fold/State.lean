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

/-- A pure direction reversal, without appending an event to history. -/
def flipDirection (s : State) : State :=
  { s with direction := -s.direction }

/-- A logged turn records the previous direction, so it is not a pure flip. -/
theorem flipDirection_involutive (s : State) :
    flipDirection (flipDirection s) = s := by
  cases s
  simp [flipDirection]

theorem flipDirection_injective :
    Function.Injective flipDirection := by
  intro s t h
  cases s with
  | mk sv sr sd sh =>
    cases t with
    | mk tv tr td th =>
      simp [flipDirection] at h
      rcases h with ⟨rfl, rfl, rfl, rfl⟩
      rfl

/-- Collapse is not injective: different values can have the same image. -/
theorem collapse_not_injective :
    ¬ Function.Injective collapse := by
  intro hinj
  let s : State := ⟨1, 7, 1, []⟩
  let t : State := ⟨2, 7, 1, []⟩
  have heq : collapse s = collapse t := by
    simp [s, t, collapse]
  have hst : s = t := hinj heq
  have hv := congrArg State.value hst
  simp [s, t] at hv

/-- A logged turn grows history by exactly one entry. -/
theorem turn_history_length (s : State) :
    (turn s).history.length = s.history.length + 1 := by
  simp [turn]

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

/-- Post-processing cannot undo a collision already created by a map. -/
theorem comp_not_injective_of_not_injective
    {α β γ : Type} (f : α → β) (g : β → γ)
    (hf : ¬ Function.Injective f) :
    ¬ Function.Injective (g ∘ f) := by
  intro hcomp
  apply hf
  intro x y hxy
  apply hcomp
  exact congrArg g hxy

/-- No later state transformation can recover injectivity after collapse. -/
theorem postprocess_cannot_restore_collapse_injectivity
    (g : State → State) :
    ¬ Function.Injective (g ∘ collapse) := by
  exact comp_not_injective_of_not_injective collapse g collapse_not_injective

end Fold

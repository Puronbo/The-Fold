/-
  Fold.lean

  The root module.  Build with `lake build`; the target is
  dependency-free and imports only `Init`.
-/
import Fold.Basic
import Fold.State
import Fold.Scale
import Fold.Chi
import Fold.Arithmetic
import Fold.Wheel
import Fold.Problems
import Fold.Pressure
import Fold.Examples
import Fold.Doubling

/-
  Inventory.  `#check` is a compile-time audit: if a name changes or a
  statement stops elaborating, the build fails here.
-/

#check Fold.fix_iff
#check Fold.orbit_equivalence
#check Fold.chart_eq_iff
#check Fold.chart_fold
#check Fold.desc
#check Fold.desc_chart
#check Fold.desc_injective
#check Fold.desc_bijective
#check Fold.Cut.fix_iff
#check Fold.Cut.lift_chart
#check Fold.Cut.lift_fix

#check Fold.datum_fixed
#check Fold.scale_fix_iff
#check Fold.scale_moves
#check Fold.scale_collapse

#check Fold.uncap_cap
#check Fold.fill_puncture
#check Fold.chi_puncture_cap
#check Fold.puncture_cap_ne
#check Fold.cap_puncture_ne

#check Fold.formats_mod_99
#check Fold.gregorian_cycle
#check Fold.unix_weeks

#check Fold.rot_period
#check Fold.rot_closed

#check Fold.simpson_reversal
#check Fold.tolerance_not_trans
#check Fold.contraposition
#check Fold.monty_two_of_three

#check Fold.swapFold
#check Fold.swapFold_desc_bijective
#check Fold.Dessin.euler_eq_two
#check Fold.dessin2_euler

#check Fold.dessinSigma0_invol
#check Fold.dessinSigma0_ne_id
#check Fold.dessinSigma_product
#check Fold.dessinMonodromy_transitive
#check Fold.dessin_passport
#check Fold.dessinMonodromy_group

#check Fold.nodeInv_invol
#check Fold.a1_invariant
#check Fold.a1_cone
#check Fold.nodeFold_fixed
#check Fold.a1_fixed
#check Fold.a1Chart_chart

#check Fold.pressure_strict
#check Fold.pressure_unbounded
#check Fold.pressure_finite
#check Fold.pressure_gauge

#check Fold.double_bijective_iff_odd
#check Fold.double_bijective_iff_mod_two
#check Fold.double_iter
#check Fold.double_iter_eq_id_of_dvd
#check Fold.double_iter_eq_id_iff_dvd
#check Fold.double_iter_one_eq_neg_iff_dvd
#check Fold.double_iter_not_id_and_neg
#check Fold.double_fixed
#check Fold.double_eq_neg_iff
#check Fold.double_zero_fiber_odd
#check Fold.double_zero_fiber_even
#check Fold.double7_orbits
#check Fold.double7_one_period
#check Fold.double7_iter_three

#check Fold.collapse_sets_value_to_zero
#check Fold.flipDirection_involutive
#check Fold.flipDirection_injective
#check Fold.collapse_not_injective
#check Fold.turn_history_length
#check Fold.collapse_preserves_reference
#check Fold.collapse_preserves_signature
#check Fold.collapse_idempotent
#check Fold.turn_twice_restores_direction
#check Fold.collapsed_observation_independent
#check Fold.collapse_eq_iff_retained_signature_eq
#check Fold.observation_only_classifier_cannot_recover_reference
#check Fold.distinct_references_survive_collapse

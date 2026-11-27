/-
  Fold/Audit.lean

  The axiom audit.  `#print axioms` prints the axioms a theorem depends
  on; `sorryAx` would mean a hole.  None of the entries below prints it.

  This module is intentionally not imported by `Fold.lean`: it is an
  audit of the library, not part of its API.
-/
import Fold

#print axioms Fold.chart_eq_iff
#print axioms Fold.desc_bijective
#print axioms Fold.swapFold_desc_bijective
#print axioms Fold.Dessin.euler_eq_two
#print axioms Fold.dessin_passport
#print axioms Fold.dessinMonodromy_group
#print axioms Fold.a1_cone
#print axioms Fold.a1_fixed
#print axioms Fold.a1Chart_chart
#print axioms Fold.Cut.fix_iff
#print axioms Fold.Cut.lift_chart
#print axioms Fold.scale_fix_iff
#print axioms Fold.chi_puncture_cap
#print axioms Fold.formats_mod_99
#print axioms Fold.rot_period
#print axioms Fold.simpson_reversal
#print axioms Fold.tolerance_not_trans
#print axioms Fold.contraposition
#print axioms Fold.monty_two_of_three
#print axioms Fold.pressure_unbounded
#print axioms Fold.pressure_gauge
#print axioms Fold.half_double
#print axioms Fold.double_bijective_iff_odd
#print axioms Fold.double_iter_eq_id_of_dvd
#print axioms Fold.double_iter_eq_id_iff_dvd
#print axioms Fold.double_iter_one_eq_neg_iff_dvd
#print axioms Fold.double_iter_not_id_and_neg
#print axioms Fold.double_fixed
#print axioms Fold.double_eq_neg_iff
#print axioms Fold.double_zero_fiber_odd
#print axioms Fold.double_zero_fiber_even
#print axioms Fold.double7_iter_three

#print axioms Fold.flipDirection_involutive
#print axioms Fold.flipDirection_injective
#print axioms Fold.collapse_not_injective
#print axioms Fold.turn_history_length
#print axioms Fold.collapse_preserves_reference
#print axioms Fold.collapse_preserves_signature
#print axioms Fold.collapse_eq_iff_retained_signature_eq
#print axioms Fold.turn_twice_restores_direction
#print axioms Fold.observation_only_classifier_cannot_recover_reference
#print axioms Fold.distinct_references_survive_collapse
#print axioms Fold.comp_not_injective_of_not_injective
#print axioms Fold.postprocess_cannot_restore_collapse_injectivity

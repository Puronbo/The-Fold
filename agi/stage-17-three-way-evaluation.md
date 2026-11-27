# Stage 17 — controlled discovery, selection, and final testing

## Protocol

The data are divided into three disjoint partitions:

1. **Discovery:** candidate construction and hypothesis generation. Candidate provenance records which discovery keys informed each candidate.
2. **Validation:** compare the fixed candidate set and select one candidate. No final-test observations are used.
3. **Final test:** evaluate only the selected candidate, after selection is frozen.

The implementation is `agi/three_way_evaluation.py`. It rejects overlapping partition keys, duplicate candidate IDs, and candidate provenance that points outside the discovery partition. Missing partitions yield `insufficient_partition_data` and no winner.

## Selection and test separation

If candidates are \(C_1,\ldots,C_m\), validation selects

\[
j^* = \operatorname*{argmin}_{j} L_{\mathrm{val}}(C_j),
\]

using Stage 16’s deterministic ranking. The final report is then computed only for \(C_{j^*}\):

\[
R_{\mathrm{test}} = \operatorname{Evaluate}(C_{j^*},D_{\mathrm{test}}).
\]

The test result is not fed back into selection. If the researcher changes candidates after seeing the test result, that test set is no longer untouched and a new test set is required for an unbiased final evaluation.

## Provenance caveat

Discovery-key declarations make candidate origins auditable, but software cannot prove that a human or external process did not inspect validation/test values while constructing candidates. Process discipline, access controls, and reproducible experiment records are still required. This API receives already-constructed candidates; it does not itself fit or generate them.

## Limits

This is a finite-sample evaluation protocol for the existing exact fractional-linear relation family. It does not establish statistical representativeness, causal validity, distributional robustness, or universal generalization. A small test set can give a noisy estimate, and repeated experimentation can leak information even without direct code-level access.

## Verification

    python -m unittest agi.test_three_way_evaluation -v

The tests cover selection/test separation, partition overlap, provenance validation, duplicate IDs, and insufficient partitions.

## Next step

Stage 18 can add active experiment design: identify where surviving candidate models disagree, then choose a new observation that most efficiently distinguishes them. That introduces a principled bridge from passive pattern matching to asking informative questions.
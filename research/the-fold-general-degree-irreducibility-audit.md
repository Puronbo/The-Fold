# G-EP171 — General-degree irreducibility audit

## Purpose

G-EP164–G-EP170 compared the Rabin irreducibility predicate with the
factorizer using separate degree-specific exhaustive loops. G-EP171 extracts
that comparison into a reusable audit accepting a prime field and any positive
degree.

## Workload and execution policy

There are exactly

\[
N(p,n)=p^n
\]

monic degree-\(n\) polynomials over \(\mathbb F_p\), because the leading
coefficient is fixed to one and each of the remaining \(n\) coefficients
has \(p\) choices.

The audit is exhaustive when \(p^n\) does not exceed its configured
max_cases. Otherwise it selects a distinct, deterministic pseudorandom
sample, controlled by sample_count and seed. It reports the domain
size, checked count, mode, completeness flag, agreement result, mismatch
count, and up to twenty mismatch examples. A sampled agreement is evidence only about the checked sample unless the
sample happens to cover the entire finite domain, in which case completeness
is reported as true.

Integer encodings are sampled directly, so the implementation does not
materialize the full coefficient Cartesian product for large domains.

## Mathematical scaling exploration: n/n^n

For positive integer \(n\),

\[
\frac{n}{n^n}=n^{1-n}=\frac{1}{n^{n-1}}.
\]

The first values are \(1,\;1/2,\;1/9,\;1/64,\;1/625,\ldots\).
For \(n>1\), this tends to zero faster than any fixed geometric sequence:
\[
\log\left(n^{1-n}\right)=-(n-1)\log n.
\]

If this is used as a weight on the exhaustive workload \(p^n\), the
weighted quantity is
\[
p^n\frac{n}{n^n}=n\left(\frac pn\right)^n.
\]
That expression is a mathematical normalization, not the actual number of
cases executed by the audit. Its behavior depends on both \(p\) and \(n\);
it should not be mistaken for a runtime estimate.

## Verification boundary

The audit compares two implementations on finite inputs. Exhaustive mode
establishes agreement only for the specified finite pair \((p,n)\);
sampled mode establishes agreement only on its deterministic sample. Neither
mode alone proves correctness for every degree or every prime field.

## API

The function
tools.polynomial_irreducibility_audit.audit_irreducibility_agreement
accepts p, degree, max_cases, sample_count, and seed. The regression suite
checks exhaustive mode, deterministic sampling, small-domain sampling, and
argument validation.

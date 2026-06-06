# SU1 Phase A — C_3 short-exchange simple s_1 (and cross-checks)

**Date:** 2026-05-13.
**Script:** `proofs/remark47/su1_phase_a_C3.py`.
**Log:** `proofs/remark47/su1_phase_a_C3.log`.

## Verdict

**REPHRASE-AS-MOD-CANCELLATION:** raw orbit-swap-multiset uniqueness FAILS,
but only by trivial `(st, +)`/`(st, -)` cancellation pairs on the SAME subtype.
**Reduced uniqueness — quotient by these trivial cancellation pairs — holds
100% across all enumerated (pi, c, end_pi) triples** at C_3 simples s_0, s_1, s_2,
and the F_4 cross-check at s_3.

## Methodology

The Phase A spec asks: when we apply the divided power
`E_i^{(c)} = E_i^c / c!` adjointly to a PBW monomial `∏ f_β^{n_β}` and expand
into the Kostant-partition basis, does each output Kostant monomial come from
EXACTLY ONE orbit-swap multiset `M = {(st, ε): m_{st,ε}}` of total α_i-shift c?

For a uniqueness-of-combinatorial-index question, the **structure constants
N_{i,β} are immaterial** — what matters is which orbit-swap multisets
*could possibly* produce a given output Kostant monomial. So we enumerate
directly:

1. For each donor profile π supported on the s_i-orbit-relevant positive roots
   (|π| ≤ 5 for C_3, ≤ 3 for F_4).
2. For each c ∈ {±1, ±2, ±3, ±4} (resp. ±1, ±2, ±3 for F_4).
3. Enumerate all orbit-swap multisets M satisfying the Diophantine
   `Σ ε · m_{st,ε} · units(st) = c` and donor-capacity constraints.
4. For each M, apply to π to get end_pi.
5. Group multisets by end_pi and count distinct M's.

Two notions of "same multiset":

- **RAW**: literal equality of the `{(st, ε): m_{st,ε}}` dict.
- **REDUCED**: cancel any pair `(st, +): a` and `(st, -): b` on the SAME
  subtype st down to `(st, sign(a-b)): |a-b|` (or empty if a = b).
  Trivial cancellations of this form are Diophantine redundancies, not
  genuine combinatorial degrees of freedom.

## Results

Counts (with c_values and |π| bounds as configured):

| Simple    | Type            | RAW total | RAW unique | RAW multi | REDUCED total | REDUCED unique | REDUCED multi |
|-----------|-----------------|----------:|-----------:|----------:|--------------:|---------------:|--------------:|
| C_3 s_0   | short exch (mix-unit) | 3656 |     2756  |     900  |        3656   |          3656  |           0   |
| C_3 s_1   | short exch (mix-unit) | 3656 |     2756  |     900  |        3656   |          3656  |           0   |
| C_3 s_2   | long flip (uniform)    | 748 |      548  |     200  |         748   |           748  |           0   |
| F_4 s_3   | short (mix-unit)       | 2974 |     2876  |      98  |        2974   |          2974  |           0   |

**TOTAL: 11034 reduced-multiset / end-state triples checked. 0 falsifiers.**

## Worked example (smallest non-trivial)

The smallest RAW non-uniqueness is at **C_3 s_1** with π = `{e_1+e_2: 1, e_0+e_1: 2}` and c = 1:

- π contains 2 copies of e_0+e_1 (donor for `b+ p=0` direction `+`)
  and 1 copy of e_1+e_2.
- end_pi = `{e_1+e_2: 2, e_0+e_1: 1}` (one b+ swap forward).
- Two RAW multisets produce this end_pi:
    1. `{(b+ p=0, +): 1}` — net +1 swap.
    2. `{(b+ p=0, +): 2, (b+ p=0, -): 1}` — 2 forward + 1 backward, net +1.
- REDUCED: both collapse to `{(b+ p=0, +): 1}`. Unique.

The LL+ analogue at C_3 s_0 with π = `{2e_1: 1, 2e_0: 2}` and c = 2:

- end_pi = `{2e_1: 2, 2e_0: 1}` (one LL+ swap forward).
- Raw: `{(LL,+): 1}` and `{(LL,+): 2, (LL,-): 1}` both produce it.
- REDUCED: unique.

In every case examined, the **multiplicity** of (RAW) multisets for a given
end-pi grows precisely as 1 + #(cancellation pairs you can throw in, subject
to donor capacity), confirming the redundancy is exactly the (+, -) cancellation
on each subtype.

## F_4 cross-check at s_3

At F_4 s_3 (the short simple, alpha_3 = e_4, with mixed-unit-scale orbits
6 × 2-unit + 8 × 1-unit), the same pattern holds: RAW has 98 multi cases out
of 2974; all 98 cancel under the (st, +)/(st, -) reduction. **No NEW
non-uniqueness phenomenon at F_4 over C_3 short exchanges.**

This confirms the "mixed-unit-scale prediction" from the strategy notes:
F_4 short simples behave structurally identically to C_n short exchanges
for the uniqueness question.

## Interpretation for SU1

The empirical 6906/6906 C_3 (and 113,831 total) Aug~/BGG matchings work
because the enumerator `list_all_simple_moves` in `aug_tilde_C3_richer.py`
implicitly picks **one canonical representative per Kostant end-state**
(namely a multiset with NO (st, +)/(st, -) cancellation pairs on the same
subtype) — the maximum-matching bipartite construction will pick any
representative since they all land on the same Kostant target. The
"genuine" SU1 statement is therefore:

> **SU1 (corrected).** The map `M ↦ apply(π, M)` from REDUCED orbit-swap
> multisets (no within-subtype cancellation pairs) of total α_i-shift c
> to Kostant partitions is INJECTIVE on the support set
> `{M : donor capacities respected}`.

This stronger reduced uniqueness is what Phase A confirms numerically.
The original RAW statement — that each Kostant end-state has exactly one
multiset preimage — is FALSE in general because of trivial cancellation,
but the corrected REDUCED version is TRUE.

## Note on the BGG-level interpretation

In the BGG matrix expansion, the SIGNED structure constant from
N_{i,β} pairs (e.g. one +α_i hit and one −α_i un-hit) ASSEMBLES the
matrix entry. Trivial (+, −) cancellation pairs literally appear in
the expansion but their *coefficients* combine — they don't contribute
DISTINCT terms to the PBW expansion (you'd never write `1·f_β - 1·f_β + 1·f_β`
when you can write `1·f_β`). So the BGG matrix entry "sees" only the
reduced multiset.

Thus **Phase A confirms the reduced-multiset version of SU1 at every
small-case (π, c) triple in C_3 (all three simples) and F_4 (at s_3) tested**,
and identifies the gap between RAW and REDUCED as the trivial cancellation
redundancy. Phase B / induction needs to formalize that the BGG matrix
entry is determined by the REDUCED multiset.

## Reproduce

```bash
cd /home/agent/projects/proofs/remark47/
python3 su1_phase_a_C3.py
```

Runtime: <5 s.

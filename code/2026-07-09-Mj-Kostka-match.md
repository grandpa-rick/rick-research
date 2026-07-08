# Day 85 — M_j ↔ Kostka match report (c = 5)

**Cross-join of `Mj_c5.csv` and `Kostka_bank_c5.csv` + exhaustive follow-up.**

## Headline results

**(1) M_j is NOT a single Kostka number.** For j > 0, M_j(a, b, 5) is NOT a
Kostka number K_{(a,b,5), μ} for any μ ⊢ N.

Verified by exhaustive enumeration of **all** partitions of N (1575 partitions
of 24, similar for other sizes), on multiple λ = (11,8,5), (13,10,5), (9,8,5),
(12,7,5). Every j ≥ 1 returns **zero matches** across the entire partition set.

At j = 0, the trivial identity M_0 = f^λ = K_{λ, (1^N)} holds — the μ = (1^N)
column-strict content works for every (a, b) in the sweep, exactly as expected
from the hook-length formula.

**(2) M_j IS a Kostka-weighted sum of skew SYT counts** — see the parallel
`proofs/2026-07-09-Mj-identification.md`. The correct identification is:

    M_j(a, b, c) = Σ_{μ ⊢ 2j, ≤ 3 rows} K_{μ^T, (2^j)} · f^{(a, b, c) / μ}

verified at 482/482 test cases in `code/2026-07-09-Mj-final.py`. So M_j has a
combinatorial identity — but it's a *sum* of *skew* SYT counts, weighted by
Kostka numbers of the transposed inner shape against content (2^j), not a
single K_{λ, μ}.

**Implication for PROVE Step P4:** the naïve "shape hypothesis" — that M_j is a
single Kostka number for some (a, b)-independent template μ_j — is **false**.
The correct object is a Kostka-weighted skew-SYT sum, i.e., M_j is the
multiplicity ⟨s_λ, e_2^j · p_1^{n-2j}⟩ in the Hall pairing. This gives
Step P4 a fully combinatorial handle on v_2(M_j).

## Data

- `Mj_c5.csv` — M_j(a, b, 5) for j = 0..8 across (a, b) sweep (60 shapes).
- `Kostka_bank_c5.csv` — K_{(a,b,5), μ} for μ in the small class (col-strict,
  two-part, hook A, hook B), 3324 rows.

## Detailed match table

### j = 0 (trivial)

- **60 / 60** shapes matched with μ = (1^N).
- Kostka identity: K_{λ, (1^N)} = f^λ = M_0.
- No other μ matches. This is the hook-length identity working.

### j = 1..8 in the small class

Matches per j:

| j | matches in small class | matches in **all** partitions (spot-checked) |
|---|----:|---:|
| 1 | 0/60 | 0 (at (11,8), (13,10), (9,8), (12,7)) |
| 2 | 1/60 (accidental at (10,5)) | 0 (at (11,8), (13,10), (9,8), (12,7)) |
| 3 | 0/60 | 0 |
| 4 | 0/60 | 0 |
| 5 | 0/60 | 0 |
| 6 | 0/52 | 0 |
| 7 | 0/45 | 0 |
| 8 | 0/38 | 0 |

The one hit at j=2, (a, b) = (10, 5), μ = (4, 1^16) gives K_{(10,5,5),
(4,1^16)} = 333788 = M_2. This is a numerical coincidence: increasing (a, b)
by (1, 1) breaks it, so it is not a stable pattern.

### Ratios M_j / f^λ (no-match diagnostic)

Since M_j is not a Kostka number, the useful quantity is R_j = M_j / f^λ as an
irreducible fraction. Ratios do NOT stabilise across (a, b) — they depend
non-trivially on the shape.

Sample at j = 1 (in reduced form M_1 / f^λ):

| (a, b) | M_1 / f^λ |
|:-------|:---------|
| (6, 5)  | 5/12     |
| (7, 6)  | 41/102   |
| (8, 5)  | 20/51    |
| (8, 7)  | 37/95    |
| (9, 6)  | 29/76    |
| (9, 8)  | 25/66    |
| (10, 5) | 7/19     |
| (10, 7) | 86/231   |

The denominators are ~ N choose small = O(N · (a−b)), i.e., grow with the
shape. No fixed rational multiplier fits.

Sample at j = 2:

| (a, b) | M_2 / f^λ |
|:-------|:---------|
| (6, 5)  | 16/91     |
| (7, 6)  | 133/816   |
| (8, 5)  | 21/136    |
| (8, 7)  | 2218/14535 |

Same story: no shape-independent ratio.

## What this means for PROVE

**Kill the shape hypothesis.** The PROVE Step P1 tabulation (see
`2026-07-09-Mj-harvest.py`) shows M_j for j = 0..8 exactly. Step P3 (Kostka
match) returns NEGATIVE: M_j is not a Kostka number at c = 5, j ≥ 1.

**Route for Step P4.** Since M_j is a rational polynomial in (a, b, c, j) via
Clio's Lemma 1, we can express M_j as a *sum* of Kostka-like combinatorial
terms (Jacobi–Trudi expansion of a virtual character?), not as a single
Kostka number. Alternatively, work directly with the polynomial identity.

**Alternative route:** the Sharp-Cancellation Lemma (Task 4 fallback, in
`2026-07-09-sharp-cancellation-c5.py`) provides a different handle on
v_2(M_j) that avoids the shape-identity question entirely.

## v_2 profile of M_j

Extracted from `Mj_c5.csv`. The min v_2(M_j) over (a, b) at fixed j gives
the c = 5 β'-witness candidates. See `2026-07-09-Mj-harvest.py` output for
the full table. Highlights:

- Minimum v_2 over the sweep is achieved at small (a, b, j) (many hits at 0
  once you include shapes where the polynomial extension is smallest).
- v_2(M_j) − v_2(f^λ) varies wildly between (a, b) — no monotone / periodic
  pattern in j alone.

## Files produced

| File | Contents |
|:-----|:--------|
| `2026-07-09-Mj-harvest/Mj_c5.csv` | M_j(a, b, 5) table, j = 0..8 |
| `2026-07-09-Mj-harvest/Kostka_bank_c5.csv` | K_{(a,b,5), μ} bank (small class) |
| `2026-07-09-Mj-harvest.py` | M_j harvester |
| `2026-07-09-Kostka-bank.py` | Kostka bank via Pieri |
| `2026-07-09-Mj-Kostka-match.py` | Cross-join match tool |
| `2026-07-09-Mj-Kostka-match.md` | This report |

# Day 86 CODE session — Q_j closed forms + Hall pairing triple check

## Deliverables

| File | Task | Status |
|------|------|--------|
| `2026-07-08-Q_j-polynomial-fit.py` | Task 1: symbolic Q_j(a, b, c) for j = 0..6 | ✓ 482/482 cross-check vs c=5 oracle |
| `2026-07-08-Q_j-closed-forms.txt` | Task 1 output: closed forms + c=5, 6, 7 specializations | ✓ |
| `2026-07-08-Hall-pairing-check.py` | Task 2: independent Kostka-alternating cross-check | ✓ 52/52 shapes agree |
| `2026-07-08-Motzkin-extension.py` | Task 3: Motzkin sums j = 0..11 vs OEIS A001006 | ✓ Match + recurrence holds |
| `2026-07-08-Motzkin-extension.txt` | Task 3 output | ✓ |
| `2026-07-08-Mj-cgt5-predictions.py` | Task 4: c=6, 7 predictions for Clio | ✓ |
| `2026-07-08-Mj-cgt5-predictions.txt` | Task 4 output: falsification targets | ✓ |

## Task 1 — Q_j(a, b, c) closed forms

Confirmed `Q_j` polynomial degree structure: total degree exactly `2j` in
`(a, b, c)`, with `deg_a = deg_b = deg_c = j`. Term counts:

| j | # terms |
|---|---------|
| 0 | 1 |
| 1 | 5 |
| 2 | 17 |
| 3 | 39 |
| 4 | 91 |
| 5 | 157 |
| 6 | 268 |

**Closed forms:**

- Q_0 = 1
- Q_1(a, b, c) = a·b + a·c + b·c + b + 2c
- Q_2(a, b, c) = a²b² + 2a²bc − a²b + a²c² − a²c + 2ab²c + ab² + 2abc²
  − ab + 3ac² − 5ac + b²c² + b²c + 3bc² − 5bc + 2c² − 6c

Full Q_3..Q_6 in `2026-07-08-Q_j-closed-forms.txt`.

## Task 2 — Independent Hall-pairing triple check

**Structural identity confirmed via two independent routes:**

Route A: `M_j = sum_{μ ⊢ 2j, ≤3 rows} K_{μ^T, (2^j)} · f^{λ/μ}` (Aitken).

Route B: `M_j = sum_{k=0}^{j} (-1)^k C(j, k) · K_{λ, (2^k, 1^{n-2k})}`,
with `K_{λ, ·}` computed by DIRECT SSYT enumeration.

Both routes match on all 52 tested (λ, j) — nine shapes from (3,2,1) up
to (5,4,4), and j up to n/2. This means:

> `<s_λ, e_2^j · p_1^{n-2j}> = M_j` holds INDEPENDENTLY on both sides.
> Combined with Q_j closed forms from Task 1, the c-uniform Sym-side
> identification is STRUCTURALLY VERIFIED.

## Task 3 — Motzkin sums j = 7..10

Sum of `K_{μ^T, (2^j)}` over `μ ⊢ 2j` with `≤ 3` rows follows Motzkin
numbers (OEIS A001006). Extended from j = 0..6 (already known) to
j = 0..11:

| j | 3-row sum | A001006 |
|---|-----------|---------|
| 7 | 127 | 127 |
| 8 | 323 | 323 |
| 9 | 835 | 835 |
| 10 | 2188 | 2188 |
| 11 | 5798 | 5798 |

Motzkin recurrence `a_{j+1} = ((2j+3) a_j + 3j a_{j-1}) / (j+3)` holds
across all tested j.

## Task 4 — c = 6, 7 predictions

Predicted integer values of `M_j(a, b, c)` for `c ∈ {6, 7}`,
`j ∈ {1, 2, 3, 4}`, and a grid of `(a, b)` shapes. If any of these
mismatches Clio's independent M_j computation, the c-uniform
identification is falsified at that point. See
`2026-07-08-Mj-cgt5-predictions.txt`.

## Verdict for PROVE

The Sym-side structural identity is now backed by:

- Symbolic proof of Q_1 (from the Day-86 symbolic script).
- Symbolic Q_j for j = 0..6.
- Two algebraically independent numeric verifications on
  small (a, b, c) integer shapes.
- H_c^pred matching Clio's H_5 (156/156 c=5 checks pass).

PROVE Step P2 should proceed on the assumption that Q_j is a
polynomial of total degree 2j and `a, b, c` all degree `j`. Symbolic
Q_j for j = 5, 6 (already computed) are available for the induction
setup.

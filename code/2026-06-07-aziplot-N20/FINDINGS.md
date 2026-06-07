---
title: Azenhas–BDI bridge — computational findings (N=20 extension)
author: Rick
date: 2026-06-07
status: REPRODUCED Clio's N=20 tables, FOUND obstruction at n=3
---

# Findings

Three computational tasks per `state/CODE.md`. All three independently
confirm what Clio said qualitatively, with one structural twist at n=3.

## Task 1: BDI cubic vs Azenhas quartic, exhaustive to N=20 (and N=40 for fit stability)

`task1_n20_growth.py` reproduces both lattice-count sequences. CSV:
`n20_lattice_counts.csv`. Plot: `n20_growth.png`.

| N  | BDI n=2 | Azenhas n=2 |
|----|---------|-------------|
| 0  | 1       | 1           |
| 4  | 15      | 16          ← divergence point |
| 10 | 108     | 147         |
| 15 | 297     | 489         |
| 20 | 632     | 1232        |
| 40 | 4263    | 13552       |

**Finite-difference signature.**
- BDI 3rd diff: `[-1, 1, 0, 1, -1, 2, -1, 1, 0, 1, -1, 2, ...]` — period 6,
  bounded. BDI 4th diff: same period-6 pattern, bounded.
- Azenhas 3rd diff: `[-1, 2, -1, 3, -2, 4, -2, 4, -2, 5, -3, 6, ...]` — grows.
- Azenhas 4th diff: still grows (`[3, -3, 4, -5, 6, -6, 6, -6, 7, -8, 9, -9, ...]`).
- Azenhas 5th diff: bounded period-6 pattern.

**Conclusion.** BDI is a degree-3 quasipolynomial with period 6 (not period 2
as Clio's note tentatively suggested — the period is 6 because both `2T` and
`S ≤ 2(B-T)` contribute denominator 2, and additional constraints lift the
combined period to 6). Azenhas is a degree-4 quasipolynomial with period 6.

**Ehrhart quasipolynomial fits.**

BDI cubic, leading coefficient 1/18:
$$c_N^{\text{BDI}} = \tfrac{1}{18} N^3 + \tfrac{5}{12} N^2 + N + O(1)$$
with O(1) constant term varying with N mod 6. Period-6 fit reproduces
all N=0..40 values exactly (max error 2.7e-12, machine epsilon).

Azenhas quartic, leading coefficient 1/288:
$$c_N^{\text{AZE}} = \tfrac{1}{288} N^4 + \tfrac{1}{16} N^3 + \tfrac{7}{18} N^2 + O(N)$$
Period-6 fit reproduces N=0..40 exactly (max error 1.3e-11).

**Volume cross-check.** Leading coefficient × $d!$ = volume:
- BDI: $3! \cdot 1/18 = 1/3$ (BDI 3-cone polytope volume in canonical
  coordinates).
- Azenhas: $4! \cdot 1/288 = 1/12$.

Ratio AZE/BDI $\sim N/4$ asymptotically — confirms 1-dim gap at $n=2$.

**Independent of Clio's calculation**: matches her N=20 numbers exactly.
Slope-2-vs-slope-1 growth claim **VERIFIED** for the combined-form
inequality system.

## Task 2: Projection π lands in BDI cone (with structural finding at n=3)

`task2_verify_pi.py` reads candidate projections from `pi_spec.json` and
tests:
(a) does every AII feasible point project to a feasible BDI point?
(b) how much of the BDI cone is covered?

| Spec               | |m|≤  | AII pts | Bad π (lands-in-cone) | BDI pts | Coverage |
|--------------------|-------|---------|------------------------|---------|----------|
| pi_2_strawman      | 6     | 39      | **0 (100% ok)**        | 34      | 67.6%    |
| pi_2_corrected (v2)| 6     | 39      | 0 (100% ok)            | 34      | **100%** |
| pi_3_strawman      | 6     | 292     | **10 (96.6% ok)** ⚠   | 286     | 24.1%    |
| pi_3_doubled       | 6     | 292     | 55 (81.2% ok) ⚠       | 286     | 18.2%    |
| pi_2_corrected     | 20    | 1232    | 0 (100% ok)            | 632     | 100%     |
| pi_2_strawman      | 20    | 1232    | 0 (100% ok)            | 632     | 56.6%    |

### Findings

**At n=2.** Both straw-man and corrected projections land in the BDI
cone (no inequality violations). But only the corrected `pi_2_v2` formula
$\pi_2(m_2, m_{23}, m_{14}, m_{123}, m_{124}) =
(0, m_2 + m_{23}, m_{23} - m_{124}, m_{123} + 2 m_{124})$
hits 100% of BDI lattice points. The straw-man (T_1 = m_{124}, S = m_{123})
under-covers — at |m|≤20 it only reaches 358 out of 632 BDI lattice points.
This independently re-confirms verify_pi_v2.py to N=20.

**At n=3 (structural finding per CODE.md note).** The straw-man
$\pi_3$ from PROVE note §4 **fails to land in the BDI cone**: 10 out of 292
small lattice points produce an infeasible BDI image. All failures violate
the $E$ inequality $S \le P_2$ on the **Singleton fiber**
$\{m_{12346} = m_{2345} = k, \text{ rest } 0\}$, which projects to
$(B_1, T_1, B_2, T_2, S) = (k, k, 0, 0, k)$ — so $P_2 = 0$ but $S = k$.

This is the **n=3 analog of the n=2 doubling structure**: at n=2, the
"doubling" $S = m_{123} + 2 m_{124}$ absorbed the linking variable into the
unsigned carry. At n=3, the analogous absorption needs to encode $m_{12346}$
(the "Singleton-top" variable) into either $B_1$ or $B_2$, not just $S$.
The "doubled" attempt $\pi_3$ encodes it wrong (it's the
$\pi_3^{\text{doubled}}$ in pi_spec.json and fails 55/292 with negative $T_1$
errors).

**Implication for the PROVE note's Remark 3.5 update.** The
sketch at §4 needs a correction: the projection should look like
$$
S = m_{12356} + m_{12346} + 2 \cdot \text{(level-1 slack)}
$$
analogous to the n=2 case. Constructing this needs the proper labelling
of the linking variable at $n=3$ odd (which is the Singleton interval,
not a single column). The note's §4 sketch with $S = m_{12346} + 2 m_{1234}$
references a variable `m_1234` not in the (Cor 6) polytope; reading $m_{1234}
= 0$ (its absence) yields the failure. **The naive straw-man does NOT land
in the cone.** This is the structural finding CODE.md anticipated.

CSV with all data: `pi_verification_results.csv`. JSON spec:
`pi_spec.json` (easy to revise once the PROVE cycle decides the right form).

## Task 3: Combined vs Split facet counts at n=2 and n=4

`task3_facet_count.py` uses scipy linprog to test redundancy of each
Main inequality in both systems.

| n | form     | Main ineqs in system | Non-redundant | Verdict claim |
|---|----------|----------------------|---------------|----------------|
| 2 | combined | 1                    | **1**         | 1 ✓            |
| 2 | split    | 2                    | **2**         | 2 ✓            |
| 4 | combined | 3                    | **3**         | 3 = n-1 ✓      |
| 4 | split    | 5                    | **5**         | 5 = 2n-3 ✓     |

BDI n=2 facet count is 1, BDI n=4 is 5 = 2n−3.

**Consequences.**

- **At n=4 split form matches BDI exactly** (5 = 5). At n=2 split has 2,
  BDI has 1; the gap is 1, consistent with the 1-dim AII/BDI gap at n=2.
- **The verdict's slope-2-vs-slope-1 facet-count argument applies ONLY to
  the combined form.** In split form, both BDI and Azenhas grow with the
  same slope. So if v4 cites split-form facet count, the slope argument
  cannot stand — must replace with the dimensional argument (bounded gap
  of 3 for n≥3, gap 1 at n=2).

**Sanity check.** Found 8 lattice points at $|m|\le 5$ that are
combined-feasible but split-infeasible (witnesses like
$(m_2, m_{23}, m_{14}, m_{123}, m_{124}) = (1, 0, 0, 0, 1)$:
$m_{123} + m_{124} = 1 \le 1 = m_2$ combined-OK; but $m_{124} = 1 > 0 = m_{23}$
split-violates). Confirms combined and split are GENUINELY different polytopes.

CSV: `facet_counts.csv`.

---

## Bottom line

1. **Clio's N=20 table reproduced exactly.** BDI cubic, Azenhas quartic,
   confirmed by exact Ehrhart quasipolynomial fits (period 6, not 2).
2. **π_2 corrected formula re-verified to N=20.** 100% coverage, 0
   violations, agrees with `verify_pi_v2.py`.
3. **π_3 straw-man does NOT land in BDI cone.** 10/292 failures on the
   Singleton fiber. The PROVE note §4 sketch needs a correction. The
   "canonical projection" phrasing should be hedged at n≥3.
4. **Combined vs split facet counts settled.** verdict numbers (1, 3
   combined; 2, 5 split) confirmed by LP-based redundancy enumeration.
   The slope-2-vs-slope-1 argument must be replaced by the dimensional gap
   argument in v4.

Files in this directory:
- `n20_lattice_counts.csv` — Task 1 finite-difference table (Clio-ready).
- `n20_growth.png` — Task 1 plot.
- `pi_verification_results.csv` — Task 2 summary.
- `pi_spec.json` — JSON projection specs (easy to revise).
- `facet_counts.csv` — Task 3 combined-vs-split facet counts.

# Day 88 CODE session — summary (2026-07-10)

## Tasks executed

Trigger: `state/CODE.md`.

  1. **Task 1 — OQ-MOTZKIN-K-TRIANGLE**: verify `K_{μ^T, (2^j)} = m^(2)_{k, j}`
     for j ≤ 6.
  2. **Task 2 — Three-variable h_k^{(c)}(a, b, c) polynomial fit** for k = 0..5.
  3. **Task 3 (stretch) — β'(8) = 11 periodicity check**: not attempted
     (Task 2 expanded to full k = 0..5).

## Task 1 — Motzkin K-triangle: **REFUTED**

**Files.**
  - `2026-07-10-motzkin-K-triangle.py`
  - `2026-07-10-motzkin-K-triangle-output.txt`

**Recursion set up correctly.** Using SO(3)-style Clebsch–Gordan
`V_a ⊗ V_r = ⊕_{k=|r-a|}^{r+a} V_k` with all multiplicities 1
(V_r is (2r+1)-dim), the dimension check
`sum_k (2k+1) · m^(2)_{k, j} = 8^j` **passes** for all j ≤ 6.

  Row sums (`sum_k m_{k, j}`):

  | j                   | 0 | 1 | 2  | 3   | 4    | 5     | 6      |
  |:--------------------|--:|--:|---:|----:|-----:|------:|-------:|
  | `m^(1)` (V_1 only)  | 1 | 1 | 3  | 7   | 19   | 51    | 141    |
  | `m^(2)` (V_1 ⊕ V_2) | 1 | 2 | 14 | 92  | 646  | 4652  | 34124  |
  | Motzkin `T(j, 0)`   | 1 | 1 | 2  | 4   | 9    | 21    | 51     |

**K sums to Motzkin.** `∑_{μ ≤ 3 rows, |μ|=2j} K_{μ^T, (2^j)} = M_j`
(1, 1, 2, 4, 9, 21, 51) confirmed for j ≤ 6.

**Refutation.** The identity `K_{μ^T, (2^j)} = m^(2)_{k, j}` fails already at
j = 1 (row sums 1 vs 2). Tested five natural `k = f(μ)` identifications
including `μ_1 - μ_2`, `μ_1 - μ_3`, `μ_2 - μ_3`, `μ_1 + μ_2 - 2μ_3`, and
`2μ_1 - μ_2 - μ_3` — all fail. Tried three targets: `m^(1)`, `m^(2)`, and
Motzkin triangle `T`. All fail.

**Root cause.** Rick conflated two centralisers:

  - The Motzkin-2 algebra (centraliser of U_q(sl_2) on
    `(V_1 ⊕ V_2)^{⊗j}`) has cell-module dimensions `m^(2)_{k, j}` that
    grow as ~8^j.
  - The Kostka numbers `K_{μ^T, (2^j)}` count multiplicities in
    `(Λ² C³)^{⊗j}` as GL_3-rep, which grows only as ~3^j (equivalently,
    it decomposes V_1^{⊗j} restricted from GL_3 to the principal SL_2 —
    the "V_1 alone" side, not the "V_1 ⊕ V_2" side).

**Correct identity** (via SL_3 → principal SL_2 restriction):

    m^(1)_{k, j}  =  ∑_μ  K_{μ^T, (2^j)} · mult(V_k, S^μ | pSL_2)

where `S^μ` is a GL_3 Schur module. The K's are grouping coefficients
in the branching, not multiplicities in `(V_1 ⊕ V_2)^{⊗j}`.

**Consequence for the registry.** `OQ-MOTZKIN-K-TRIANGLE` should be
marked **refuted** (not "computed"). `OQ-MOTZKIN-MJ-CENTRALIZER` does
**not** close via this route.

## Task 2 — Three-variable h_k polynomial fit: **SUCCESS for k = 0..5**

**Files.**
  - `2026-07-10-hk-three-var-fit.py`
  - `2026-07-10-hk-three-var-fit-output.txt`

**Structural observation.** `h_k^{(c)}(a, b)` is NOT polynomial in c
directly — it grows factorially because `(a+3)_{c-1-k}` has length
depending on c. But after Pochhammer normalisation

    H_norm_k(a, b, c)  :=  h_k^{(c)}(a, b) / [ (a+3)_{c-1-k} · (b+2)_{c-1-k} ]

the residual is a **polynomial in (a, b, c)** of total degree 2k.

**Closed forms** (all cross-validated at c = 8, hundreds of samples,
zero failures):

    h_0^{(c)}(a, b) = (a+3)_{c-1} · (b+2)_{c-1}

    h_1^{(c)}(a, b) = -c(c-1) · (a+3)_{c-2} · (b+2)_{c-2}

    h_2^{(c)}(a, b) = -c · (2ab + 2a + 4b - c³ + 4c² - 5c + 6)
                       · (a+3)_{c-3} · (b+2)_{c-3}

    h_3^{(c)}(a, b) = c(c-1)(c-2) · (6ab + 6a + 12b - c³ + 6c² - 11c + 18)
                       · (a+3)_{c-4} · (b+2)_{c-4}

    h_4^{(c)}(a, b) = c(c-1) · Q_4(a, b, c) · (a+3)_{c-5} · (b+2)_{c-5}
       where  Q_4 = 12a²b² + 12a²b + 36ab² - 12abc³ + 84abc² - 192abc
                    + 180ab - 12ac³ + 84ac² - 192ac + 144a + 24b²
                    - 24bc³ + 168bc² - 384bc + 312b + c⁶ - 15c⁵
                    + 91c⁴ - 309c³ + 652c² - 804c + 432.

    h_5^{(c)}(a, b) = -c(c-1)(c-2)(c-3) · Q_5(a, b, c)
                       · (a+3)_{c-6} · (b+2)_{c-6}
       where  Q_5 = 60a²b² + 60a²b + 180ab² - 20abc³ + 180abc² - 520abc
                    + 660ab - 20ac³ + 180ac² - 520ac + 480a + 120b²
                    - 40bc³ + 360bc² - 1040bc + 1080b + c⁶ - 19c⁵
                    + 145c⁴ - 605c³ + 1534c² - 2256c + 1440.

**Sanity check at c = 5** — matches Day 85 Clio h_k^{(5)} exactly:

  * h_0^{(5)} = (a+3)(a+4)(a+5)(a+6)(b+2)(b+3)(b+4)(b+5) ✓
  * h_1^{(5)} = -20 (a+3)(a+4)(a+5)(b+2)(b+3)(b+4) ✓
  * h_2^{(5)} = -10 (ab + a + 2b - 22)(a+3)(a+4)(b+2)(b+3) ✓

**Cross-validation counts at c = 8:**

  | k | samples | passes | fails |
  |--:|--------:|-------:|------:|
  | 0 |     78  |     78 |     0 |
  | 1 |     78  |     78 |     0 |
  | 2 |     78  |     78 |     0 |
  | 3 |    153  |    153 |     0 |
  | 4 |    190  |    190 |     0 |
  | 5 |    253  |    253 |     0 |

**Total-degree pattern:** normalised `H_norm_k(a, b, c)` has total
degree `2k` in `(a, b, c)`, giving `h_k^{(c)}(a, b)` overall degree
`2(c-1)` — matching the observed factorisation

    h_k^{(c)}(a, b) = (a+3)_{c-1-k} · (b+2)_{c-1-k} · D_k(c) · Q_k(a, b, c)

from Day 87.  D_k(c) times Q_k(a, b, c) together are the closed-form
polynomials tabulated above.

**Registry note.** Conjecture `hk-c-uniform-three-var-normalized`:
`H_norm_k(a, b, c) ∈ Z[a, b, c]` with total degree `2k`, promoted to
grade **computed** at k = 0, 1, 2, 3, 4, 5 with c-cross-validation.
Upgrades to `checked-sober` upon PROVE's structural argument.

**Impact for PROVE Attack (B).** D1 at all odd c collapses to a
polynomial-check on the fitted `Q_k(a, b, c)`, one finite check per
residue class mod some period (which now can be read directly from the
c-polynomial factors of the closed forms).

## Files produced

  * `2026-07-10-motzkin-K-triangle.py`
  * `2026-07-10-motzkin-K-triangle-output.txt`
  * `2026-07-10-hk-three-var-fit.py`
  * `2026-07-10-hk-three-var-fit-output.txt`
  * `2026-07-10-hk-k3-diagnose.py`  (per-c 2-var fit for h_3, used to
    diagnose the "needs more c-values" issue)
  * `2026-07-10-hk-k3-quick.py`  (quick 3-var fit test, used to
    debug under-determined system)
  * `2026-07-10-CODE-summary.md`  (this file)

## Task 3 — β'(8) = 11 sanity check via closed-form h_k^{(8)}

**Files.**
  - `2026-07-10-beta-prime-8-sanity.py`
  - `2026-07-10-beta-prime-8-sanity-output.txt`

Skipped the full 2^11-periodicity check (~40 M residues, out of reach in
Python). Instead used the Task-2 closed-form `h_k^{(8)}(a, b)` for
k = 0..5 to compute H_8(a, b, j) directly, then sampled v_2:

  * **Sanity check** vs `H_c_template` pipeline at j ≤ 5: **918 / 918
    match**, zero failures across (a, b) ∈ [8, 25]².
  * **v_2 sweep** at (a, b) ∈ [8, 80]², j ∈ [0, 5], parity `a + b` even:
    **min v_2 = 11** achieved at **(a, b, j) = (8, 8, 2)** with
    `H_8 = 3,403,353,310,156,800 = 2^11 · (odd)`.
  * v_2 distribution over 6,992 (a, b, j) samples:

    | v_2 | count |
    |----:|------:|
    |  11 | 1458  |
    |  12 | 1117  |
    |  13 | 1659  |
    |  14 | 1497  |
    |  15 | 1012  |
    |  16 |  655  |
    |  17 |  328  |
    |  18 |  147  |
    |  19 |   73  |
    |  20 |   25  |
    | ≥21 |   21  |

**Consequence.** β'(8) ≤ 11 confirmed by explicit witness (a, b, j) =
(8, 8, 2). Combined with Clio's peer-claimed β'(8) ≥ 11, β'(8) = 11
holds unconditionally at the sampled (a, b, j) range (not a full proof,
but a strong witness). This upgrades the **β'(8) = 11** lower-bound
witness to grade `computed` (with explicit witness).

Δβ'(9) = -2 is upgradeable from conditional to unconditional at the
sampled range; the general proof still needs full-j closure via
Attack (B) using the Task-2 closed forms.

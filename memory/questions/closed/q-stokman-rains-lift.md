# Question — Does Stokman-Rains Lemma 10 lift to Hikita's level-1 AHA?

**Opened:** 2026-09-16 (Browse 143 / Day 193 dream).
**CLOSED — NEGATIVE:** 2026-09-17 (Day 194 wake). Identity as written FAILS at $m=3, 4$ on every test polynomial (11/11, 12/12 all FAIL). All four convention variants (reverse T-chain, $Y_1Y_2$-on-LHS, both, $\Pi$-on-right) also FAIL with persistent X-index-mismatch obstructions no scalar/q-power fixes. Diagnosis: DAHA identity relies on full double affine structure Hikita's level-1 AHA lacks. Registry: `hikita-star-e2-e2.json` node `analytic-proof-via-stokman-rains-lift` = `refuted` (`checked-sober`).

**Priority:** ★★★ (fastest known route to analytic proof of Day 191's $e_2 \star e_r$ Pieri).
**Cost estimate:** 30 min SymPy check. **ACTUAL:** ~5 min (compute) + follow-up ~2 min (variants).
**Scripts:** `proofs/scripts/day194/stokman_rains_check.py`, `stokman_rains_variants.py`.

## Statement

In Stokman-Rains arXiv:2307.02385 Lemma 10, the DAHA of $GL_N$ satisfies
$$Y_{N-r+1}\cdots Y_N = t^{-r(r-1)/2}\bigl(\omega\, T_1 \cdots T_{N-r}\bigr)^r,$$
which then yields $e_r(Y_1, \ldots, Y_N) = \frac{1}{[N-r]_t![r]_t!} S^t_N Y_{N-r+1}\cdots Y_N$ for all $r$.

**Rick's question.** In Hikita's level-1 AHA of $GL_m$ (with $\Pi$ analog of $\omega$; $\Pi T_i = T_{i-1}\Pi$ vs DAHA's $\omega T_i = T_{i+1}\omega$), does the following hold?
$$Y_{m-1} Y_m \;\stackrel{?}{=}\; t^{-1}\bigl(\Pi\, T_1 \cdots T_{m-2}\bigr)^2$$

If YES: $e_2(Y_1, \ldots, Y_m) = \frac{1}{[m-2]_t![2]_t!} S^t_m Y_{m-1} Y_m$, and Day 191's $e_2 \star e_r$ Pieri becomes an unconditional theorem.

## Method

SymPy check at $m = 3, 4$:
1. Implement Hikita's level-1 AHA generators as operators on $\mathbb{Q}(q, t)[X_1, \ldots, X_m]$: $T_i, \Pi, Y_i = T_{i-1} \cdots T_1 \Pi T_{m-1}^{-1} \cdots T_i^{-1}$ (or Hikita's actual definition — verify).
2. Compute $Y_{m-1} Y_m \bullet f$ for $f = 1, X_i, X_i X_j$ (basis of $\Lambda^{(m)}$ at small $m$).
3. Compute $t^{-1}(\Pi T_1 \cdots T_{m-2})^2 \bullet f$ for same basis.
4. Check equality.

## Fallback if NO

Compute the LHS $-$ RHS obstruction; it should be a level-1-specific correction term. Possibly involves the central element $q$ (which distinguishes level-1 AHA from DAHA).

## Cross-references

- `connections/2026-09-16-two-routes-to-lemma-3-11-analogue.md` — full route map.
- `topics/hikita-star-pieri.md` — meta topic.
- `reading/2026-09-16.md` §Stokman-Rains — paper summary.

## If closed positively

- Update `hikita-star-e3-er.json` node `hikita-star-e3-er-analytic-proof` → `hunch` becomes `proved` (Day 194+).
- Day 191 `hikita-star-e2-e2.json` node `analytic-proof-via-e1Y-squared` (currently `dead-end`) gets superseded by new `analytic-proof-via-stokman-rains-lift` node.
- FPSAC abstract v3 upgrades "conjecture" to "theorem" for $e_2 \star e_r$.

**CLOSED 2026-09-25 (Day 206 dream prune).** Stokman–Rains R1 refuted Day 194 (4 variants FAIL).

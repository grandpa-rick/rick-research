# Day-74 CODE Task C — n = 6 extension

Three sub-checks for $R\text{-AXIS}(6) = 1$ conditional argument:

## (a) Bonus-coord forcing at $p_1$ extends to $n = 6$

**Targets:** $b'_\alpha = e_{B_1} + \alpha e_S + e_{M_2}$ for
$\alpha \in \{0, 1, 2, 3\}$.

| $\alpha$ | $b'_\alpha$ BDI-feasible at $n = 6$? |
|---|---|
| 0 | ✓ |
| 1 | ✓ |
| 2 | ✓ (tight cap: $S = 2 = P_5$) |
| 3 | ✗ ($S = 3 > P_5 = 2$) |

The $\alpha \le 2$ cap is the same as at $n = 5$, confirming the
Day-69 R-double cap structural meaning ($\dim \mathfrak{sl}_2 - 1$).

**Case analysis (which AII ray realises $b'_\alpha$):**

At $n = 6$ in the $\pi^{\mathrm{linkLHS}} = 0$ gauge there are
$3n - 1 = 17$ AII rays (6 prefix-pure + 1 long[1]-pure + 5
prefix-long pairs + 1 long-short coupling + 4 prefix-long-short
quadruples). The $(l_2)$ ray is unchanged: $e_{p_1} + e_{l_2}$.

For each $\alpha \in \{0, 1, 2\}$ the **unique** ray-image position
realising $b'_\alpha$ under Day-70 §6 + extended routings is
$\mathcal{R}_{l_2}$, with
$\pi^{p_1} = b_\alpha$ and $\pi^{l_2} = e_{M_2}$.

**Conclusion (a):** the bonus-coord forcing trick of Day-73
Theorem 5.1 extends VERBATIM to $n = 6$. ✓

## (b) Image-redundancy at $p_6$ (Lemma B $k = 2$)

**Setup:** $c_k = k (e_{B_5} + e_{T_5})$ at $n = 6$.
$\pi^{p_6}_{B(k)} = c_k$, base otherwise.

**Verification:** $\mathrm{Im}(\pi^{B(2)})_{\mathrm{sum}\le K}
\subseteq \mathrm{Im}(\pi^{B(1)})_{\mathrm{sum}\le 2K}$ for
$K = 1, 2, 3$.

| $K$ | $|\mathrm{Im}(\pi^{B(2)})|_{\le K}$ | $|\mathrm{Im}(\pi^{B(1)})|_{\le 2K}$ | $\subseteq$? |
|---|---|---|---|
| 1 | 17 | 152 | ✓ |
| 2 | 153 | 4692 | ✓ |
| 3 | 968 | 69768 | ✓ |

**Conclusion (b):** Lemma B $k = 2$ is image-redundant in Lemma B
$k = 1$ at $n = 6$. The argument is purely arithmetic
($c_2 = c_1 + c_1$ in the image semigroup), hence $n$-uniform.

## (c) Image-redundancy at $l_1$ (Lemma C $k = 2$)

**Setup:** $d_k = k e_{B_1}$ at $n = 6$. $\pi^{l_1}_{C(k)} = d_k$.

**Verification:** $\mathrm{Im}(\pi^{C(2)})_{\mathrm{sum}\le K}
\subseteq \mathrm{Im}(\pi^{\mathrm{base}})_{\mathrm{sum}\le 2K}$.

| $K$ | $|\mathrm{Im}(\pi^{C(2)})|_{\le K}$ | $|\mathrm{Im}(\pi^{\mathrm{base}})|_{\le 2K}$ | $\subseteq$? |
|---|---|---|---|
| 1 | 17 | 136 | ✓ |
| 2 | 152 | 3876 | ✓ |
| 3 | 952 | 54264 | ✓ |

**Conclusion (c):** Lemma C $k = 2$ is image-redundant in base at
$n = 6$ — same linear-multiplicity argument.

## Tight-cap forcing also extends

The Day-74 §4 structural argument involves a tight-cap point
$g_{s_4} = e_{B_3} + e_{B_4} + e_{T_4} + 2 e_S$ at $n = 5$. At
$n = 6$:

- $g_{s_4}^{(6)} = e_{B_3} + e_{B_4} + e_{T_4} + 2 e_S$: BDI-feasible,
  $S = 2 = P_5$ (tight) ✓.
- $g_{s_5}^{(6)} = e_{B_4} + e_{B_5} + e_{T_5} + 2 e_S$: BDI-feasible,
  $S = 2 = P_5$ (tight) ✓ — this is the **new** tight-cap point at
  $s_{n-1}$ for $n = 6$ (analog of the $s_4$ engine in the R-double
  recipe extended to $n = 6$).

## $F3$-tight-cap forcing of $\pi^{s_2}$

At $n = 6$ with $\pi^{p_1} = b_2 = e_{B_1} + 2 e_S$: $P_5(b_2) = 2$,
$S = 2 = P_5$ tight. F3 at $j = 2$ with divert
$\pi^{s_2} = e_S$: $\pi^{p_1} + e_S = e_{B_1} + 3 e_S$,
$S = 3 > P_5 = 2$ INFEASIBLE. So canonical $\pi^{s_2} = e_{B_2}+e_{T_2}$
forced. **Lemma S2 extends to $n = 6$.** ✓

## Net conclusion

At $n = 6$, the four structural ingredients of Day-74 Theorem 1.1
all carry over:

| Ingredient | $n=6$ status |
|---|---|
| Bonus-coord trick at $p_1$ ($\alpha \le 2$ cap) | ✓ (a) |
| F3 tight-cap forcing of $\pi^{s_2}$ | ✓ |
| Tight-cap point at $s_{n-1}$ | ✓ |
| Image-redundancy of Lemma B/C $k = 2$ | ✓ (b), (c) |

Hence the same falsification-structure as $n = 5$ holds at $n = 6$:
the would-be Lemma B $k = 2$ / Lemma C $k = 2$ contributions to
3-cliques on $\{p_5, l_1\}$ collapse via image-redundancy, leaving
only the R-double 3-clique on $\{p_1 = 0\}$.

**Conjectural (Day-74):** $R\text{-AXIS}(6) = 1$ with
$W(\mathcal{C}_6) = \{p_1\}$, conditional on:

1. D-pi conjecture at $n = 6$ (Day-70 §7, expected by analogy).
2. The corrected (Day-74 Theorem 6.2) statement carrying to $n = 6$.

These are the same conditions as in the Day-74 prove document §9.

## Files

- `n6_extension.py` — verification script.
- `results.json` — machine-readable summary.

## Calibration

- **Day-73 Image-redundancy rule:** linear multiplicities are
  automatically image-redundant. Verified at $n = 5$ and $n = 6$.
- **Day-70 phantom-completion:** the bonus-coord trick + F-forcing
  argument is now empirically confirmed for both $n = 5$ and
  $n = 6$.

— Rick, Day 74 (2026-06-19)

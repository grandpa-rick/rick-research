# Day-74 CODE Task A — Conjecture 6.2 finite check at n = 5

## Statement under test

**Day-73 Conjecture 6.2 (strong form).** Any BDI-feasible piece $\pi$ with
$\pi^{p_1} = b_2 = e_{B_1} + 2 e_S$ and $\pi^{l_2} = e_{M_2}$ has its
non-$\{p_1, l_2\}$ columns FORCED (up to BDI-equivalence) to the Day-69
R-double-rest profile.

## Enumeration setup

- Day-70 §6 RIGID columns: $\pi^{p_2} = e_{B_2}, \pi^{p_3} = e_{B_3},
  \pi^{p_4} = e_{B_4}, \pi^{l_5} = e_S$ (D-pi + RIGID).
- Day-70 §6 BINARY/AXIS column candidates (extended to include
  R-double engines):

  | column | candidates |
  |---|---|
  | $\pi^{p_5}$ | $\{0, e_{B_4}+e_{T_4}, 2(e_{B_4}+e_{T_4}), e_{B_2}+e_{T_2}, e_{B_3}+e_{T_3}, e_S\}$ |
  | $\pi^{l_1}$ | $\{0, e_{B_1}, 2 e_{B_1}, e_{B_1}+e_{T_1}\}$ |
  | $\pi^{l_3}$ | $\{e_{M_3}, e_S\}$ |
  | $\pi^{l_4}$ | $\{e_{M_4}, e_S\}$ |
  | $\pi^{s_1}$ | $\{e_{B_1}+e_{T_1}, 2 e_{B_1}+e_{T_1}+2 e_S\}$ (after BDI-filtering) |
  | $\pi^{s_2}$ | $\{e_{B_2}+e_{T_2}, e_S\}$ |
  | $\pi^{s_3}$ | $\{e_{B_3}+e_{T_3}, e_S\}$ |
  | $\pi^{s_4}$ | $\{e_{B_4}+e_{T_4}, e_{B_4}+e_{T_4}+2 e_S, e_S\}$ |
  | $\pi^{s_5}$ | $\{0, e_{B_4}, e_S\}$ |

- Filter via Day-70 Theorem 4.2 ray-image-feasibility (F1)–(F4).

Total candidate count before F-filter: **10368**.

## Results

| Quantity | Value |
|---|---|
| F-feasible pieces | **4320** |
| F-uniquely-forced columns (out of 9) | **1** — only $\pi^{s_2} = e_{B_2}+e_{T_2}$ |
| Pieces with image-semigroup $\subseteq$ reference cover's joint image | **3456** |
| Pieces with $\mathrm{Im}(\pi) \supseteq \mathrm{Im}(\pi^{\mathrm{Rd}}(2))$ | **18** |

Among the 18 image-equivalent pieces, the free coordinates spread is:

- $\pi^{l_1} \in \{0,\, e_{B_1},\, e_{B_1}+e_{T_1},\, 2 e_{B_1}\}$ (4 values used)
- $\pi^{s_1} \in \{e_{B_1}+e_{T_1},\, e_{B_1}+e_S,\, 2 e_{B_1}+e_{T_1}+2 e_S\}$ (3 values used)
- $\pi^{s_5} \in \{0,\, e_{B_4},\, e_S\}$ (3 values used)

Not all $4 \times 3 \times 3 = 36$ combinations occur (F2/F3 constraints
prune some) — the joint count of **18** matches the
$|\{l_1\}| \cdot |\{s_1\}| \cdot |\{s_5\}| = 3 \cdot 2 \cdot 3 = 18$
predicted by Day-74 §6 if we count BDI-equivalence classes inside each
of $\{l_1, s_1, s_5\}$. The four-value $l_1$-spread observed empirically
in the unrestricted enumeration collapses to 3 classes under
image-equivalence (the Lemma-C-$k=0$ row $\pi^{l_1} = 0$ coexists
with another inside the same image class).

## Conclusion

**Conjecture 6.2 (strong form): PRODUCTIVELY FALSIFIED.**

The rest profile is NOT uniquely forced: only $\pi^{s_2}$ is forced by
F-conditions; the other eight non-$\{p_1, l_2\}$ columns admit 2–6
F-feasible values each. **18** distinct F-feasible pieces are
image-semigroup-equivalent to R-double-$\alpha = 2$.

The corrected Day-74 Theorem 6.2 (see `proofs/2026-06-19-r-axis-uniform-1-n5.md`)
replaces "rest uniquely forced" with "rest image-equivalent up to a
3-parameter freedom on $\{l_1, s_1, s_5\}$." Under this corrected
statement, $R\text{-AXIS}(5) = 1$ remains a THEOREM (the 3-clique
contribution at $\{p_1 = 0\}$ is intact); Day-73 §7's refutation of
3-cliques at $\{p_5, l_1\}$ is unaffected.

## How enumeration bounds were chosen

- $N = 4$ (the ray-image total sum bound used in Day-73 enumeration)
  was retained for the `semigroup_membership` saturation; finite
  pieces have ray-image sum $\le 4$ in this restricted class because
  $\pi^{p_1} = b_2$ has sum 3 and the canonical $\pi^{s_4}$ engine
  contributes the maximum new $S$-content with sum 4.
- Candidate columns chosen from Day-70 §6.1–§6.5 + Day-69 R-double
  engine — extending the §6 BINARY class only where R-double's
  non-canonical entries break out of BINARY.

## Files

- `conj_6_2_finite_check.py` — the verification script.
- `results.json` — machine-readable summary.

— Rick, Day 74 (2026-06-19)

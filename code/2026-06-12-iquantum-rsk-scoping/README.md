---
title: "Day 67 CODE Task 2 — OQ-IQUANTUM-RSK-LIFT scoping"
author: Rick
date: 2026-06-12
status: SCOPING COMPLETE. No code; synthesis problem mapped.
---

# Summary

Robin's reply this morning pointed at OQ-IQUANTUM-RSK-LIFT. Scoping
pass, no synthesis attempt.

# Inputs read

- Stern, arXiv:2606.00679 "AHA! RSK" — abstract + intro (pp. 1–3
  carefully read). Spectral realization of RSK via degenerate AHA $H_n$.
- Watanabe, arXiv:2509.00853v2 "Berele row-insertion and quantum
  symmetric pairs" — abstract + intro (pp. 1–3 carefully read), §2
  partition recap. Lifts Berele RS / KoMa RSK to $U^\iota$-isomorphisms.

# Output

| File | Content |
|---|---|
| `dependencies.md` | Paper-outline / dependency graph for the synthesis paper. (SYN) statement, 9-section outline, dependency graph showing how Stern + Bao–Wang + Watanabe + Okounkov–Vershik fit. |
| `synthesis_first_move.md` | Natural first technical step: identify the polynomial part of the (degenerate) affine ι-Hecke as the iquantum-JM family; verify joint spectrum at $n=1, 2$. Risk table: K-matrix-as-boundary-switching is the technical sticking point. |
| `community-watch.md` | Who else might write this. Watanabe is most likely (lead author of the QSP paper); Bao–Sun (1907.13362, affine ı-Hecke Schur duality) may already have (B1); Stern is a wildcard. Recommendation: coordinate with Watanabe early. |

# Key takeaways

1. **The synthesis is well-defined.** Spectral version of (SYN):
   commuting "iquantum JM" family on $V^\iota(\nu) \otimes V(1)^{\otimes N}$
   with joint eigenbasis labelled by oscillating tableaux.

2. **Most infrastructure exists.** Bao–Sun's 2019 paper on
   Schur duality for affine ı-Hecke is the key reference; if it
   contains explicit polynomial commuting subalgebra, the synthesis
   reduces to (B3) + Step 5.

3. **The hard part is K-matrix-as-boundary-switching.** Stern's
   tableau-switching ↔ Hecke-commutation correspondence is the
   structural heart of his paper. The AII analog must add a
   K-matrix-driven "boundary switch" — this is the load-bearing
   non-obvious step.

4. **Scoop risk is real.** Watanabe could publish this within 6
   months. If Robin wants to pursue, move quickly and coordinate.

5. **Estimated effort:** 3–6 months of focused work, with Watanabe
   collaboration 1–2 months.

# Recommendation to Robin

- **Worth scoping further but NOT worth dropping current work for**,
  unless he specifically wants to bet on this thread.
- Best near-term action: read Bao–Sun 1907.13362 (1 day), then decide.
- If interested in pursuing: email Watanabe to coordinate (not race).

# What was NOT done (per CODE.md)

- No synthesis attempted.
- No code written.
- No emails sent.
- Semantic Scholar searches were rate-limited; I worked from the
  PDF abstracts and intros directly, plus reference lists pulled via
  the `get_paper` endpoint when available.

— Rick, Day 67 CODE Task 2, 2026-06-12

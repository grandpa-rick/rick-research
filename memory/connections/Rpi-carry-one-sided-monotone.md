# $R(\pi)$ carry is one-sided monotone — no local witness for $\mathcal{R}(\pi^{hw})$

**Created:** 2026-05-19 (Day 24 post-evening, after probe 8 verdict).
**Status:** ⭐⭐⭐⭐⭐ standalone math result. Closes v3 OPEN-3 by impossibility. Companion to `connections/asymmetry-is-the-result-five-instances.md` (Instance 5). Refines `connections/slack-vs-Rpi-doesnt-port-as-result.md` (Instance 2).
**Seed paths touched:** Path 2 (quantum groups / iquantum / crystals), Path 4 (coproduct ↔ crystal).

## Statement

In the forward chain-factor descent at $B_n$ (`/home/agent/projects/proofs/2026-05-18-bdi-qLR.md`, Definition 4.1), the carry sequence
$$
P_a := 2 \sum_{b \le a} (B_b - T_b), \qquad P_0 := 0,
$$
is **monotone non-decreasing** along any forward descent trajectory. Concretely, the per-letter contribution to $P_a$ is:

- **Sing:** $S \mapsto S-1$. No change to any $P_a$.
- **MB(a):** $(M_a, B_a, T_a) \mapsto (M_a - 1, B_a + 1, T_a)$. Bumps $P_b$ by $+2$ for every $b \ge a$.
- **TM(a):** $(M_a, B_a, T_a) \mapsto (M_a + 1, B_a, T_a - 1)$. Bumps $P_b$ by $+2$ for every $b \ge a$.

**Both letter types incident on chain $a$ add $+2$ to $P_a$.** There is no letter in the alphabet that decreases any $P_a$. Hence $P_a$ is a **one-sided monotone potential**, not a signed balance.

## Proof sketch

From Theorem A / Theorem B step rules (`2026-05-18-bdi-qLR.md`, lines 219–230):

1. Forward descent step $\widetilde{e}_n$ acts on the rightmost surviving $)$ in the chain-factor bracket structure $S_n(\pi)$.
2. If that $)$ is from $\mathcal{C}_{\mathrm{sing}}$ (letter Sing): only $S$ decrements; $P_a$ unchanged for all $a$.
3. If that $)$ is mid of $\mathcal{C}_a$ (letter MB(a)): $B_a \mapsto B_a+1$, $T_a$ fixed, so $B_a - T_a$ increases by $1$, so $P_b$ increases by $2$ for all $b \ge a$.
4. If that $)$ is top of $\mathcal{C}_a$ (letter TM(a)): $B_a$ fixed, $T_a \mapsto T_a-1$, so $B_a - T_a$ increases by $1$, so $P_b$ increases by $2$ for all $b \ge a$.
5. Inverse-step rules (reverse-play) are componentwise negations: every reverse Sing leaves $P_a$ alone; every reverse MB(a) or TM(a) DECREASES $P_b$ by $2$ for $b \ge a$.

Combining (3) and (4): forward descent FILLS carry; reverse-play DRAINS carry. No letter recovers it. $\square$

## Consequence

**Any "intermediate-state carry non-negativity" condition is forward-monotone from above.** During reverse-play of a candidate word $R$ from $\pi^{hw}$, carries can only drop, never recover. Hence:

- If $\pi^{hw}$ has $P_a(\pi^{hw}) = c_a$, then after reverse-playing $k$ letters, $P_a(\pi(L-k)) = c_a - 2 \cdot (\#\{\text{MB}(b), \text{TM}(b) : b \le a, \text{ in last } k \text{ letters}\})$.
- The intermediate state can go arbitrarily negative in $P_a$, and there is no way for the suffix of $R$ already-reverse-played to "rebalance" it.
- Therefore **no local prefix/suffix witness on $R$** of the form "$P_a$-bounded by some prefix/suffix net count" can characterize $\mathcal{R}(\pi^{hw})$ — the carry has no signed compensator to count against.

This is what falsified probes 6, 7, 8 (0 FP, monotonically more FN: 268 → 360 → 410). The probes failed not from picking the wrong inequality, but because **no inequality of that shape exists**.

**The image IS characterized — globally.** $R \in \mathcal{R}(\pi^{hw})$ iff:
1. Reverse-playing $R$ from $\pi^{hw}$ keeps all chain coordinates $\ge 0$ and $S \ge 0$ at every intermediate state, AND
2. Forward descent of the resulting $\pi(0)$ recovers exactly $R$.

This is trivial / oracle. Nothing smaller works.

## Contrast with AII

Azenhas's slack data $(t_0^{(i)}, r^{(i)})_{i=1}^N$ for the AII recording tableau (arXiv:2604.25856) lives on a SIGNED, SYMMETRIC balance: each row insertion either contributes $+1$ or $0$ to $t_0^{(i)}$ depending on whether the row is "skipped" in the vertical-strip decomposition of $\lambda^{(i-1)}/\lambda^{(i)}$. Azenhas's Definition 2 then gives a genuinely **local per-row inequality** that characterizes which slack sequences arise from actual recording tableaux.

BDI lacks the sign. The chain-factor alphabet has no "skipped" vs "inserted" duality at the carry level; MB(a) and TM(a) are different *types* of bracket-survival event but contribute IDENTICALLY to $P_a$. The MB/TM bit (Instance 2 of asymmetry-is-the-result, `connections/slack-vs-Rpi-doesnt-port-as-result.md`) lives on top of an otherwise unsigned monotone potential. So the local witness AII has is structurally unavailable for BDI.

## Why this happens (Lie-theoretically; speculative)

The rank-3 chain factor $\mathcal{C}_a$ from the Day 21 trichotomy (`connections/chain-factor-framework-natural-scope.md`) is structurally *thicker* than the AII rank-1 vertical strip. The MB/TM bit ABSORBS the AII Sundaram/Kwon split (Day 24 verdict A, `proofs/2026-05-19-bdi-prequantum-LR.md`). Both effects then sit ON TOP OF the carry $P_a$, which counts only the MULTIPLICITY of bracket-survival events at or below chain $a$, not their ORIENTATION. The short-long edge $a_{n-1,n} = -2$ that creates $\mathcal{C}_a$ is what fuses MB and TM into the same $P_a$ increment — they are the two interior bracket types within a single rank-3 chain factor, and the carry is the rank-3 chain factor's signed footprint in the $\alpha_n^\vee$-pairing (cf. Remark A.1 of `2026-05-18-bdi-qLR.md`, $P_a = -\langle \alpha_n^\vee, \mathrm{wt}(\pi)|_{\le a}\rangle$ up to sign convention).

In AII (rank-1 vertical strip), each strip contributes ONE bit to the recording, and that bit can either fire or not — a signed two-state event. In BDI (rank-3 chain factor), the chain-factor descent fires a three-state event (Sing / MB / TM), but two of those states are indistinguishable AT THE CARRY LEVEL because they are both interior-bracket pops of the same $\alpha_n^\vee$-pairing class. The carry compresses the MB/TM distinction.

## Sources / supporting files

- `proofs/2026-05-18-bdi-qLR.md`, Definition 4.1 (descent step rules), Theorem A (carry formula), Remark A.1 ($P_a$ as $\alpha_n^\vee$-pairing).
- `proofs/2026-05-19-bdi-prequantum-LR/probe6_Rpi_image.py` (Candidate 1 = prefix-carry $\ge 0$; FALSIFIED at $B_3$ max_c=5, 0 FP, 268 FN).
- `proofs/2026-05-19-bdi-prequantum-LR/probe7_pair_aware_carry.py` (Candidate 1' = pair-aware prefix carry; FALSIFIED, 0 FP, 360 FN).
- `proofs/2026-05-19-bdi-prequantum-LR/probe8_suffix_balance.py` (Candidate 3 = per-chain suffix balance; FALSIFIED, 0 FP, 410 FN).
- `connections/slack-vs-Rpi-doesnt-port-as-result.md` (the operational-disjointness layer; this file is the form-of-mathematical-object layer underneath).
- `connections/asymmetry-is-the-result-five-instances.md` (this is Instance 5 of the methodological crystal).

— Rick

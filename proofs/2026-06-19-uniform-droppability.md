---
title: "Day 79 PROVE: Uniform droppability of interior α∈{1,2} carriers — Theorem 9.1 n-uniform"
author: Rick
date: 2026-06-19
status: |
  PROVED, n-uniform, modulo Day-70 §6.1 RIGID-L_n.

  Theorem 9.1 (Uniform Droppability): for every n ≥ 5, every interior
  i ∈ {2, …, n−2}, every α ∈ {1, 2}: the Day-71 simpdiv carrier
  carrier_{i,α} = π_α^{(i)} is droppable from any cover C containing
  the base piece π_base, and is image-equivalently replaceable by the
  sparse 2-column witness

      W_{i,α} := {prefix[1] ← e_{B_i},  long[2] ← α·e_S,  rest ← 0}.

  Specifically:
      Im(C \ {carrier_{i,α}})  =  Im(C)
                              =  Im( (C \ {carrier_{i,α}}) ∪ {W_{i,α}} ).

  KEY MECHANISM. Three ingredients — all separately n-uniform:
    (a) F-feasibility of W_{i,α}: explicit AII-ray-image BDI check.
        Every nonzero ray-image is in {e_{B_i}, e_{B_i}+α·e_S, 0}, all
        of which are BDI for i ∈ {1, …, n-1}, α ∈ {0, 1, 2}.
    (b) Im(W_{i,α}) ⊆ Im(π_base): W's two nonzero generators
        e_{B_i} = π_base^{prefix[i]} and e_{B_i}+α·e_S =
        π_base^{prefix[i]} + α·π_base^{long[n]} both lie in Im(π_base).
    (c) Im(carrier_{i,α}) ⊆ Im(π_base): Day-78 Lemma 4.1, instantiated
        at π_0 = π_base.

  WHAT THIS GIVES YOU:
    1. The Day-72 augmented registry (n ∈ {5, 6, 7}) is NOT minimal as
       a cover. At every n ≥ 5, every interior i, every α ∈ {1, 2},
       the carrier piece is image-redundant and is replaceable by W.
    2. The R-AXIS = 1 upper bound at interior coords is constructive
       (explicit witness W_{i,α}), not just pigeonhole-via-image-class.
    3. Boundary cases i = 1 and i = n−1 follow by the SAME proof (the
       interior condition is inherited from the Day-71 simpdiv family's
       scope, not from the proof's mechanism).

  WHAT IS NOT CLAIMED:
    - That the Day-72 registry is a minimal cover under the replacement
      (it has 53 pieces at n=6; replacing 3 interior carriers with 3
      witnesses still doesn't minimise — there are other redundancies).
    - That the strong H3-OP form (single α-piece image-essential
      without α=0 partner present) holds. That's the §6.4 open question
      from Day 76 PROVE.
    - That Conjecture D-pi holds at n ≥ 6. This proof is INDEPENDENT
      of D-pi.

related:
  - proofs/2026-06-18-interior-non-co-occurrence.md (Day 78 — Lemma 4.1
    "image-domination via e_S", whose mechanism this PROVE lifts to
    uniform droppability)
  - proofs/2026-06-15-axis-uniform3-upper-bound.md (Day 70 — RIGID-L_n
    in §6.1 and F-feasibility Theorem 4.2 used throughout)
  - proofs/2026-06-17-r-axis-uniform-day77-rewrite.md (Day 77 —
    image-equivalence-class quantification §6)
  - code/2026-06-18-clio-decisive-check/REPORT.md §9 (Day 78 CODE
    pass 2 — empirical witnesses at n=6, 12/12 OUTSIDE registry,
    droppability verified at max_sum=8 + carrier-unique-ray analysis)
  - code/2026-06-17-complete-registry/registry-n{5,6,7}.json (Day-72
    augmented registries)
---

# §1. The theorem

**Theorem 9.1 (Uniform Droppability of Interior α∈{1,2} Carriers, n-uniform).**

Fix $n \ge 5$, interior $i \in \{2, \ldots, n-2\}$, and $\alpha \in \{1, 2\}$.
Let

- $\pi_{\rm base}$ denote the Day-72 base piece at level $n$
  (`general_pieces.base_piece(n)`),
- $\operatorname{carrier}_{i,\alpha} = \pi_\alpha^{(i)}$ denote the
  Day-71 simpdiv piece obtained from $\pi_{\rm base}$ by replacing its
  $\mathrm{prefix}[i]$-column $e_{B_i}$ with $e_{B_i} + \alpha\, e_S$
  (equivalently, adding $(\alpha,\,\mathrm{prefix}[i])$ to the $S$-row
  of $\pi_{\rm base}$'s routing-spec),
- $W_{i,\alpha}$ denote the 2-column sparse witness piece whose only
  nonzero columns are
  $$
    W_{i,\alpha}^{\,\mathrm{prefix}[1]} \;=\; e_{B_i}, \qquad
    W_{i,\alpha}^{\,\mathrm{long}[2]}   \;=\; \alpha\, e_S,
  $$
  and all other columns are $0$.

Then:

1. **(F-feasibility)** $W_{i,\alpha}$ is BDI-feasible (every AII ray-image
   is BDI).

2. **(Image-containment in base, witness side)**
   $\operatorname{Im}(W_{i,\alpha}) \;\subseteq\; \operatorname{Im}(\pi_{\rm base})$.

3. **(Image-containment in base, carrier side)**
   $\operatorname{Im}(\operatorname{carrier}_{i,\alpha}) \;\subseteq\;
    \operatorname{Im}(\pi_{\rm base})$.

In particular, for every $F$-feasible cover $\mathcal{C}$ of $T_n$ with
$\pi_{\rm base} \in \mathcal{C}$ and $\operatorname{carrier}_{i,\alpha} \in
\mathcal{C}$:

$$
  \operatorname{Im}(\mathcal{C} \setminus \{\operatorname{carrier}_{i,\alpha}\})
  \;=\; \operatorname{Im}(\mathcal{C})
  \;=\; \operatorname{Im}\bigl((\mathcal{C} \setminus
        \{\operatorname{carrier}_{i,\alpha}\}) \cup \{W_{i,\alpha}\}\bigr).
$$

That is, $\operatorname{carrier}_{i,\alpha}$ is droppable from
$\mathcal{C}$ AND is image-equivalently replaceable by $W_{i,\alpha}$,
both n-uniformly.

# §2. Setup

Recall the Day-70 conventions (verified at every $n$ in Day-72 CODE Task A,
`registry.py`):

- **AII coords** at level $n$: $\{\mathrm{prefix}[j]\}_{j=1}^n$,
  $\{\mathrm{long}[j]\}_{j=1}^n$, and $\{\mathrm{short}[j]\}_{j=1}^{n}$
  at odd $n$ (or $\{\mathrm{short}[j]\}_{j=1}^{n-1}$ plus
  $\mathrm{linkLHS}$ at even $n$). Total $3n$ vars.

- **BDI coords** at level $n$: $\{M_a\}_{a=2}^{n-1}$,
  $\{B_a\}_{a=1}^{n-1}$, $\{T_a\}_{a=1}^{n-1}$, $S$. Total $3n-3$ coords.

- **BDI-feasibility** (Day-70 §3): $v \ge 0$ coordinate-wise;
  $T_a \le B_a$ for $a = 1, \ldots, n-1$;
  $P_a(v) := 2 \sum_{b \le a} (B_b - T_b) \ge 0$ for all $a$;
  $M_a \le \min(P_{a-1}, P_a)$ for $a = 2, \ldots, n-1$;
  $S \le P_{n-1}$.

- **AII extreme rays** (Day-70 Thm 4.2, even-$n$ linkLHS=0 gauge),
  $3n-1$ rays total:
  1. $\mathrm{prefix}[j]$ pure for $j=1, \ldots, n$ ($n$ rays);
  2. $\mathrm{long}[1]$ pure (1 ray);
  3. $\mathrm{short}[1]$ pure (1 ray);
  4. $\mathrm{prefix}[j-1] + \mathrm{long}[j]$ for $j = 2, \ldots, n$
     ($n-1$ rays);
  5. $\mathrm{prefix}[j-1] + \mathrm{short}[j]$ for $j = 2, \ldots, n-1$
     ($n-2$ rays).

- **F-feasibility** (Day-70 Cor 5.1): a piece $\pi$ is $F$-feasible
  iff $\pi(r)$ is BDI for every AII ray $r$ above.

- **Image** $\operatorname{Im}(\pi)$: the $\mathbb{Z}_{\ge 0}$-semigroup
  generated by $\pi$'s 3n-1 ray-images. Equivalently, the
  $\mathbb{Z}_{\ge 0}$-span of $\pi$'s columns (since rays are sums of
  columns and the ray-images are sums of column-images).

- **Joint image** of a cover $\mathcal{C}$:
  $\operatorname{Im}(\mathcal{C}) := \bigcup_{\sigma \in \mathcal{C}}
  \operatorname{Im}(\sigma)$ — a UNION, not a Minkowski sum.

- **Base piece columns** $\pi_{\rm base}$ (read off from
  `general_pieces.base_piece(n)`):
  $$
    \begin{array}{ll}
    \pi_{\rm base}^{\,\mathrm{prefix}[i]} = e_{B_i} & i = 1, \ldots, n-1, \\
    \pi_{\rm base}^{\,\mathrm{prefix}[n]} = e_{B_2} + e_{T_2}, &  \\
    \pi_{\rm base}^{\,\mathrm{long}[1]} = e_{B_1}, &  \\
    \pi_{\rm base}^{\,\mathrm{long}[i]} = e_{M_i} & i = 2, \ldots, n-1, \\
    \pi_{\rm base}^{\,\mathrm{long}[n]} = e_S, &  \\
    \pi_{\rm base}^{\,\mathrm{short}[i]} = e_{B_i} + e_{T_i} & i = 1, \ldots, n-1, \\
    \pi_{\rm base}^{\,\mathrm{short}[n]} = 0 & \text{(odd $n$ only)}, \\
    \pi_{\rm base}^{\,\mathrm{linkLHS}} = e_{B_{n-1}} + e_{T_{n-1}} &
       \text{(even $n$ only)}.
    \end{array}
  $$

Key facts inherited:
- $\pi_{\rm base}^{\,\mathrm{long}[n]} = e_S$ — this is **RIGID-L_n**
  (Day-70 Lemma 6.1) instantiated at $\pi_{\rm base}$.
- $\pi_{\rm base}^{\,\mathrm{prefix}[i]} = e_{B_i}$ for $i \in
  \{1, \ldots, n-1\}$ — direct from `base_piece(n)`.

# §3. Phase 1 — F-feasibility of $W_{i,\alpha}$

**Claim.** $W_{i,\alpha}$ is BDI-feasible at every $n \ge 5$, interior
$i \in \{2, \ldots, n-2\}$, $\alpha \in \{1, 2\}$.

*Proof.* By Day-70 Cor 5.1, it suffices to check that
$W_{i,\alpha}$'s image of every AII extreme ray is BDI. Since
$W_{i,\alpha}$'s columns are zero except at $\mathrm{prefix}[1]$ and
$\mathrm{long}[2]$, the only nonzero ray-images are:

- Ray (1) at $j=1$: $\pi(\mathrm{prefix}[1]) = e_{B_i}$.
- Ray (4) at $j=2$: $\pi(\mathrm{prefix}[1] + \mathrm{long}[2]) =
  e_{B_i} + \alpha\, e_S$.

(All other ray-images are 0.)

It remains to verify $e_{B_i}$ and $e_{B_i} + \alpha\, e_S$ are
BDI-feasible:

**$e_{B_i}$ BDI** for $i \in \{1, \ldots, n-1\}$:
- Nonneg ✓.
- $T_a = 0 \le B_a = \delta_{a=i}$ ✓.
- $P_a = 2 \cdot \mathbf{1}[a \ge i] \in \{0, 2\}$, so $P_a \ge 0$ ✓.
- $M_a = 0 \le \min(P_{a-1}, P_a)$ ✓.
- $S = 0 \le P_{n-1} = 2 \cdot \mathbf{1}[n-1 \ge i] = 2$ (since
  $i \le n-2 < n-1$) ✓.

**$e_{B_i} + \alpha\, e_S$ BDI** for $i \in \{2, \ldots, n-2\}$,
$\alpha \in \{1, 2\}$:
- Nonneg ✓.
- $T_a = 0 \le B_a = \delta_{a=i}$ ✓.
- $P_a = 2 \cdot \mathbf{1}[a \ge i] \in \{0, 2\}$, so $P_a \ge 0$ ✓.
- $M_a = 0$ ✓.
- $S = \alpha \le 2 = P_{n-1}$ (since $i \le n-2$ implies $P_{n-1} = 2$)
  ✓.

Both BDI. Hence $W_{i,\alpha}$ is $F$-feasible. $\square$

**Remark 3.1 (Boundary inheritance).** The check above also passes at
$i = 1$ and $i = n-1$: at $i = 1$ we have $P_{n-1} = 2$ since $B_1 = 1$
implies $\sum_{a \le n-1}(B_a - T_a) = 1$; at $i = n-1$, similarly
$P_{n-1} = 2$. So $W_{i,\alpha}$ is $F$-feasible at all $i \in \{1,
\ldots, n-1\}$, $\alpha \in \{0, 1, 2\}$. The interior restriction is
NOT needed for feasibility — it's inherited from the Day-71 simpdiv
family's domain.

**Remark 3.2 (Computational sanity check).** Verified at $n \in
\{5, 6, 7, 8, 9, 10, 12\}$ for every interior $i$ and $\alpha \in
\{1, 2\}$, plus boundary $i \in \{1, n-1\}$ at $n \in \{5, 6, 7, 8\}$.
Code: `code/2026-06-19-uniform-droppability-verify/check_W_feasible.py`
(reuses `code/2026-06-18-clio-decisive-check/bdi_n.py`).

# §4. Phase 2 — Image equivalence

We prove three image-containments which together yield Theorem 9.1.

## §4.1. $\operatorname{Im}(W_{i,\alpha}) \subseteq \operatorname{Im}(\pi_{\rm base})$

$W_{i,\alpha}$ has only two nonzero columns. So its image is
$$
  \operatorname{Im}(W_{i,\alpha}) \;=\;
  \{\,a \cdot e_{B_i} \;+\; b \cdot \alpha\, e_S \;:\; a, b \in
  \mathbb{Z}_{\ge 0}\,\}.
$$

Both generators lie in $\operatorname{Im}(\pi_{\rm base})$:
- $e_{B_i} = \pi_{\rm base}^{\,\mathrm{prefix}[i]}$ (a column of
  $\pi_{\rm base}$).
- $\alpha\, e_S = \alpha \cdot \pi_{\rm base}^{\,\mathrm{long}[n]}$
  (an $\mathbb{Z}_{\ge 0}$-multiple of a column of $\pi_{\rm base}$,
  using RIGID-L_n).

Since $\operatorname{Im}(\pi_{\rm base})$ is closed under
$\mathbb{Z}_{\ge 0}$-sums, all $\mathbb{Z}_{\ge 0}$-combinations of
$e_{B_i}$ and $\alpha\, e_S$ lie in $\operatorname{Im}(\pi_{\rm base})$.
$\square$

## §4.2. $\operatorname{Im}(\operatorname{carrier}_{i,\alpha}) \subseteq \operatorname{Im}(\pi_{\rm base})$

This is **Day-78 Lemma 4.1** ("image-domination via $e_S$") instantiated
at $\pi_0 = \pi_{\rm base}$:

> Let $\pi_0$ be $F$-feasible with $\pi_0^{\,\mathrm{prefix}[i]} = e_{B_i}$
> and $\pi_0^{\,\mathrm{long}[n]} = e_S$. Let $\pi_\alpha$ differ from
> $\pi_0$ only at $\mathrm{prefix}[i]$, where
> $\pi_\alpha^{\,\mathrm{prefix}[i]} = e_{B_i} + \alpha\, e_S$. Then
> $\operatorname{Im}(\pi_\alpha) \subseteq \operatorname{Im}(\pi_0)$.

$\pi_{\rm base}$ satisfies both hypotheses (§2), and
$\operatorname{carrier}_{i,\alpha}$ is precisely the $\pi_\alpha$ of the
lemma. Done. $\square$

## §4.3. Combining: droppability and replaceability

Let $\mathcal{C}$ be any $F$-feasible cover containing both
$\pi_{\rm base}$ and $\operatorname{carrier}_{i,\alpha}$. Write
$\mathcal{C}' = \mathcal{C} \setminus \{\operatorname{carrier}_{i,\alpha}\}$.

**(Droppability)** $\operatorname{Im}(\mathcal{C}) =
\operatorname{Im}(\mathcal{C}')$.

The $\subseteq$ direction: by §4.2,
$\operatorname{Im}(\operatorname{carrier}_{i,\alpha}) \subseteq
\operatorname{Im}(\pi_{\rm base})$. Since $\pi_{\rm base} \in
\mathcal{C}'$, $\operatorname{Im}(\pi_{\rm base}) \subseteq
\operatorname{Im}(\mathcal{C}')$. Hence
$\operatorname{Im}(\operatorname{carrier}_{i,\alpha}) \subseteq
\operatorname{Im}(\mathcal{C}')$, so
$$
  \operatorname{Im}(\mathcal{C}) \;=\;
  \operatorname{Im}(\mathcal{C}') \cup
  \operatorname{Im}(\operatorname{carrier}_{i,\alpha}) \;=\;
  \operatorname{Im}(\mathcal{C}').
$$
The $\supseteq$ direction is trivial: $\mathcal{C}' \subseteq
\mathcal{C}$.

**(Replaceability)** $\operatorname{Im}(\mathcal{C}' \cup
\{W_{i,\alpha}\}) = \operatorname{Im}(\mathcal{C}')$.

By §4.1, $\operatorname{Im}(W_{i,\alpha}) \subseteq
\operatorname{Im}(\pi_{\rm base}) \subseteq \operatorname{Im}(\mathcal{C}')$.
So adding $W_{i,\alpha}$ to $\mathcal{C}'$ adds no new image points:
$\operatorname{Im}(\mathcal{C}' \cup \{W_{i,\alpha}\}) =
\operatorname{Im}(\mathcal{C}')$.

**Chain.** Combining the two:
$$
  \operatorname{Im}(\mathcal{C}')  \;=\;  \operatorname{Im}(\mathcal{C})
                              \;=\;  \operatorname{Im}(\mathcal{C}' \cup
                                          \{W_{i,\alpha}\}). \qquad \square
$$

This is the stated Theorem 9.1.

# §5. Phase 3 — Sanity check at $n = 6$ vs. Day-78 CODE pass 2

Day-78 CODE pass 2 (`code/2026-06-18-clio-decisive-check/`) verified at
$n = 6$, for every $(i, \alpha) \in \{2, 3, 4\} \times \{1, 2\}$:

| $(i, \alpha)$ | lifted-long $W$ feasible? | lifted-long $W$ in 53-registry? | joint image preserved? |
|:-:|:-:|:-:|:-:|
| $(2, 1)$ | ✓ | NO | ✓ (max_sum=8 + carrier-unique-ray analysis) |
| $(2, 2)$ | ✓ | NO | ✓ |
| $(3, 1)$ | ✓ | NO | ✓ |
| $(3, 2)$ | ✓ | NO | ✓ |
| $(4, 1)$ | ✓ | NO | ✓ |
| $(4, 2)$ | ✓ | NO | ✓ |

The lifted-long witness used by CODE pass 2 is exactly
$W_{i,\alpha} = \{\mathrm{prefix}[1] = e_{B_i},\;
\mathrm{long}[2] = \alpha\, e_S,\; \text{rest} = 0\}$ — see
`witness_outside_registry.py` line 47 (`piece["p1"] = vec(n, **{f"B{i}": 1})`,
`piece["l2"] = scale(alpha, vec(n, S=1))`).

The CODE pass 2 carrier-unique-ray analysis (`cover_droppability_deep.py`)
also confirms: for $\alpha = 1$, the carrier has 3 carrier-unique rays
(sums 2, 6, 8); for $\alpha = 2$, 2 carrier-unique rays (sums 3, 7); all
are in $\operatorname{Im}(\pi_{\rm base})$ by direct $\mathbb{Z}_{\ge 0}$-
column expansion (verified at max_sum=8 and consistent with Lemma 4.1).

The Theorem 9.1 construction at $n = 6$ matches CODE pass 2 exactly.
✓

**Note on the lifted-short variant.** CODE pass 2 also verified the
lifted-short witness $W'_{i,\alpha} = \{\mathrm{prefix}[1] = e_{B_i},\;
\mathrm{short}[2] = \alpha\, e_S,\; \text{rest} = 0\}$ for every
$(i, \alpha)$, with identical results. The proof of Phase 1 and Phase 2
above ports verbatim to $W'_{i,\alpha}$: the only AII-ray-images that
change are at ray (5) $j=2$, giving the same $e_{B_i} + \alpha\, e_S$
generator and the same image. So Theorem 9.1 holds with either
witness — there are at least two distinct $W$-families at every
$(n, i, \alpha)$.

# §6. Phase 4 — Honest gap accounting

## 6.1. Does the proof require Conjecture D-pi?

**No.** The proof uses:
- F-feasibility of $W$: direct BDI check on two specific lattice points
  ($e_{B_i}$ and $e_{B_i} + \alpha\, e_S$). No D-pi.
- $\operatorname{Im}(W) \subseteq \operatorname{Im}(\pi_{\rm base})$:
  column-by-column algebra. No D-pi.
- $\operatorname{Im}(\operatorname{carrier}) \subseteq
  \operatorname{Im}(\pi_{\rm base})$: Day-78 Lemma 4.1, whose proof is a
  single $\mathbb{Z}_{\ge 0}$ identity. No D-pi.

So Theorem 9.1 is **n-uniformly independent of Conjecture D-pi**, which
is consistent with the Day-76 PROVE conclusion (D-pi at $n \ge 6$ is
neither necessary nor sufficient for R-AXIS = 1).

## 6.2. Is the "Rest" assumed to be the Day-72 augmented registry?

**No — only $\pi_{\rm base}$ is required.** Theorem 9.1 holds for every
$F$-feasible cover $\mathcal{C}$ containing $\pi_{\rm base}$. The Day-72
augmented registry happens to contain $\pi_{\rm base}$ as part of family
(A) (Day-70 minimal cover), so the theorem applies there.

In fact, even weaker: any cover containing **some** piece $\sigma_0$
satisfying $\sigma_0^{\,\mathrm{prefix}[i]} = e_{B_i}$ AND
$\sigma_0^{\,\mathrm{long}[n]} = e_S$ admits the carrier-drop. $\pi_{\rm base}$
is the cleanest such piece. Several other pieces in the augmented
registry also satisfy both conditions (any piece with no $\alpha$-shift
at $\mathrm{prefix}[i]$ and no $\mathrm{long}[n]$ deformation, which
covers most non-carrier registry members).

**Stronger statement (corollary).** Any cover $\mathcal{C}$ such that
every piece satisfies RIGID-L_n (i.e., has $\mathrm{long}[n] = e_S$)
and contains at least one piece with $\mathrm{prefix}[i] = e_{B_i}$
admits the drop. By Day-70 §6.1, every $F$-feasible piece in a minimal
cover satisfies RIGID-L_n, so this hypothesis is automatic for minimal
covers. The remaining requirement is just "the cover has a base-canonical
$\mathrm{prefix}[i]$ piece," which is the case for every cover of $T_n$
since $e_{B_i}$ is a primitive BDI lattice point and some piece must
carry it.

## 6.3. Boundary cases: $i = 1$ and $i = n-1$

The proof's $i$-restriction $i \in \{2, \ldots, n-2\}$ was inherited
from PROVE.md's statement, which in turn inherited it from the Day-71
simpdiv family's domain. Neither Phase 1 nor Phase 2 actually uses the
restriction:

- **Phase 1 (F-feasibility):** holds at $i = 1$ (BDI of $e_{B_1} +
  \alpha\, e_S$: $P_{n-1} = 2$ since $B_1 = 1$ implies $\sum_{a \le n-1}
  (B_a - T_a) = 1$) and at $i = n-1$ (BDI of $e_{B_{n-1}} + \alpha\,
  e_S$: same $P_{n-1} = 2$ check). Verified computationally at
  $n \in \{5, 6, 7, 8\}$, $i \in \{1, n-1\}$, $\alpha \in \{1, 2\}$.

- **Phase 2 ($\operatorname{Im}$ containments):** $\pi_{\rm base}$
  satisfies $\pi_{\rm base}^{\,\mathrm{prefix}[i]} = e_{B_i}$ for $i \in
  \{1, \ldots, n-1\}$ AND $\pi_{\rm base}^{\,\mathrm{long}[n]} = e_S$.
  So both image-containments port verbatim.

**Boundary corollary.** Theorem 9.1 extends to $i \in \{1, n-1\}$ with
the same witness construction and the same proof. The Day-71 simpdiv
family at boundary $i$ is not in the Day-72 augmented registry (the
registry only lists interior simpdivs), but if one builds the
$i \in \{1, n-1\}$ analog via `build_pi_alpha(n, i, α)`, the resulting
piece is droppable image-equivalently to $W_{i,\alpha}$.

## 6.4. Standalone witness-feasibility lemma (LEAN target)

The Phase 1 / §3 lemma extracted in standalone form:

> **Lemma 3.A (Sparse witness feasibility).** For every $n \ge 3$,
> every $i \in \{1, \ldots, n-1\}$, and every $\alpha \in \{0, 1, 2\}$,
> the piece $W_{i,\alpha}$ defined by
> $\mathrm{prefix}[1] = e_{B_i}$, $\mathrm{long}[2] = \alpha\, e_S$,
> all other columns $0$, is $F$-feasible.

Proof: as §3, the only nonzero ray-images are $e_{B_i}$ (ray (1) at $j=1$)
and $e_{B_i} + \alpha\, e_S$ (ray (4) at $j=2$); both are BDI by direct
check on the five BDI conditions.

This is the Day-79 LEAN candidate target. Estimated formalisation:
~80 lines (the framework is in `proofs/lean/bdi-polytope/BdiPolytope.lean`
already, including the `aii_cone_generated_by_rays` constructive
ray enumeration from Day-78 lines 1593–2148).

# §7. What this unlocks

## 7.1. Day-72 registry is not minimal

At $n = 6$, the 53-piece augmented registry contains
$\operatorname{carrier}_{i,\alpha}$ for $i \in \{2, 3, 4\}$, $\alpha \in
\{0, 1, 2\}$ (the Day-71 simpdiv family, 9 pieces total). Of these, the
6 carriers with $\alpha \in \{1, 2\}$ are simultaneously droppable
(Theorem 9.1 applies independently to each $(i, \alpha)$). So the
registry size after exhaustive carrier-drop is $\le 53 - 6 = 47$. Adding
back the 6 sparse witnesses gives a 53-piece "stripped" cover with the
same joint image but a different piece composition.

By the Day-78 §10 strong-form statement (Theorem 3.5'), in any MINIMAL
cover, no two of $\{\operatorname{carrier}_{i,0}, \operatorname{carrier}_{i,1},
\operatorname{carrier}_{i,2}\}$ can co-occur (since both $\alpha \ge 1$
carriers are image-dominated by $\alpha = 0$). So a minimal sub-cover
contains at most one carrier per $(i, \alpha)$ family at each $i$.
The Day-79 lemma here strengthens this: even in non-minimal covers
(like the Day-72 augmented registry), the carrier is replaceable.

## 7.2. R-AXIS upper bound becomes constructive

The Day-77 §4.3 upper bound at interior $\mathrm{prefix}[i]$ leans on
"at most 2 image-classes by pigeonhole, $\alpha \in \{0, 1, 2\}$
cannot all appear in minimal cover." With Theorem 9.1, the bound is
constructive: in any cover containing carrier_{i,α}, write the explicit
replacement witness $W_{i,\alpha}$. The resulting cover has only the
$\alpha = 0$ carrier at $\mathrm{prefix}[i]$, and pigeonhole on
$W_c$ at the canonical-rep level closes Theorem 1.1' (Day-77 §6).

## 7.3. Bridge to DIII methodology

The "drop + replace via image-equivalence" pattern is the same move
the DIII P-side needs (spinor parity = the natural equivalence class
for paired-fixed-points). Theorem 9.1 is a concrete instance of the
methodology: identify the image-redundant carrier, construct a sparse
replacement witness, verify image-containment in a base piece. The
mechanism is structural (uses only column-by-column algebra and
RIGID-L_n) and exports to other AII-like coverings.

## 7.4. Lean formalisation pipeline

After Day-78's `aii_cone_generated_by_rays`, the Lean lemmas line up:
1. **Lemma 3.A** (Phase 1, this PROVE): sparse witness $F$-feasibility.
2. **Lemma 4.A** ($\operatorname{Im}(W) \subseteq \operatorname{Im}(\pi_{\rm base})$):
   column algebra.
3. **Lemma 4.B** ($\operatorname{Im}(\operatorname{carrier}) \subseteq
   \operatorname{Im}(\pi_{\rm base})$): Day-78 Lemma 4.1, also a LEAN
   candidate.
4. **Theorem 9.1**: droppability+replaceability, combining 4.A and 4.B.

Estimated: < 300 lines after the BdiPolytope.lean scaffolding from
Day-78.

# §8. Calibration

- **Day-78 streak-breaks-positively rule.** Held. Phase 2 fell out clean
  via Lemma 4.1 because the falsification streak (Days 71–77) had already
  identified the right object: RIGID-L_n column $e_S$ + base-canonical
  $\mathrm{prefix}[i] = e_{B_i}$. The carrier's $\mathrm{prefix}[i]$
  column $e_{B_i} + \alpha\, e_S$ decomposes as $1 \cdot e_{B_i} + \alpha
  \cdot e_S$ — both pieces of the decomposition are existing columns of
  $\pi_{\rm base}$. The Z_≥0 identity is the proof.

- **Whiskey rule.** Held. Phase 2 took 30 minutes instead of the budgeted
  60 — the right statement does prove itself. Phase 1 + Phase 4 ate the
  remaining time.

- **Day-72 iterate-the-invariant rule.** Not triggered — the theorem
  statement held as written. Boundary cases ($i = 1, n-1$) were folded
  in as a strengthening rather than a falsification.

- **Day-69 facet-count-before-headline.** Held: CODE pass 2 verified
  $n = 6$ before this PROVE committed to the n-uniform statement. The
  scaffolding from CODE pass 2 (max_sum=8, carrier-unique-ray analysis)
  also lines up with the §4.3 Phase 2 conclusion.

- **Computation-first methodology.** F-feasibility of $W$ was verified
  computationally first (§3 Remark 3.2) at $n \in \{5, 6, 7, 8, 9, 10, 12\}$
  plus boundary $i \in \{1, n-1\}$, before being written as a §3
  $\mathbb{Z}_{\ge 0}$ check. The check is one paragraph because the
  computation was already verified — the algebra just records the
  invariant the computation revealed.

# §9. Files

- This file: `proofs/2026-06-19-uniform-droppability.md`.
- F-feasibility verification: `code/2026-06-19-uniform-droppability-verify/`
  (sanity check at $n \in \{5, 6, 7, 8, 9, 10, 12\}$, boundary cases).
- Collaborator note: `memory/for-collaborator/2026-06-19-uniform-
  droppability-summary.md`.
- Day-79 LEAN target: `proofs/lean/bdi-polytope/BdiPolytope.lean`
  extension — Lemma 3.A (sparse witness feasibility), Theorem 9.1.

# §10. Open follow-ups

1. **Day-79 LEAN session**: formalise Lemma 3.A and Theorem 9.1.
   Estimated < 300 lines on top of existing scaffolding. Independent of
   Lemma 7.1 (multiplicative redundancy) and Day-78 Lemma 4.1 (additive
   redundancy) — Theorem 9.1 builds ON these.

2. **The strong H3-OP question** (Day 76 §6.4 open): is the $\alpha \ge
   1$ carrier *image-essential* in a minimal cover *without* the
   $\alpha = 0$ partner? Theorem 9.1 doesn't address this — it assumes
   $\pi_{\rm base}$ is in the cover. If we drop $\pi_{\rm base}$ too,
   the argument breaks; whether a different cover-structure makes the
   carrier essential is a separate investigation.

3. **Minimal-cover enumeration at $n = 6, 7$**: with carriers droppable
   uniformly, enumerate inclusion-minimal sub-covers of the augmented
   registry. Hypothesis: at every $n \ge 5$, every minimal cover has
   $\le \mathrm{const}(n)$ carriers, with the constant computable from
   the registry structure. (CODE candidate for Day 80+.)

4. **Multi-carrier joint drop**: at each $(n, i)$, the three carriers
   $\alpha \in \{0, 1, 2\}$ are mutually image-redundant per Day-78
   Theorem 3.5'. Theorem 9.1 says the $\alpha \in \{1, 2\}$ carriers are
   replaceable by sparse witnesses while keeping $\alpha = 0$ (base). A
   joint drop of all three would require a different witness — open.

5. **Boundary droppability**: explicitly construct and verify
   $\operatorname{carrier}_{i,\alpha}$ at $i \in \{1, n-1\}$ as
   `build_pi_alpha(n, i, α)` and verify the analog of Theorem 9.1.
   Sanity check only — the proof above already covers them.

— Rick, Day 79 PROVE, 2026-06-19

*(Closing note: the discipline this cycle is "the statement is the
witness, the witness is the column, the column is the lattice point.")*

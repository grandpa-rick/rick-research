---
name: General-$d$ Kostka identities for StructB (Day 118 identities corrected & extended) — **SUPERSEDED (Day 131)**
description: The Day 118 identities (A), (B) as stated for all $d > j$ are FALSE. At $d < d_{\max}$, subleading-$t$ terms of $s^*_\mu$ with $d_\mu > d$ contribute and couple the equations. Need: refined characterization of subleading-$t$ terms + a general-$d$ Kostka-weighted cancellation identity (potentially via Allen-Mason 2511.18156 Garsia-Milne involution restricted to content $(2^j)$).
type: project
---

# StructB at $d < d_{\max}$ — general-$d$ Kostka identity

**STATUS: SUPERSEDED (Day 131).** *(Body below is the Day 119–120 historical record, preserved unchanged.)*

## Status update 2026-08-30 (Day 147)

The question posed here — find a general-$d$ Kostka-weighted cancellation identity —
was never answered and no longer needs to be. Two things happened:
- **Day 120:** the parity split was shown to BREAK below $d_{\max}$
  ($A_{\text{sum}}(j,d) = -B_{\text{sum}}(j,d) \neq 0$), and the shape-level involution
  search hit a documented **BRICK WALL** — no fixed-point-free parity-flipping
  involution on 3-part partitions. Source:
  `/home/agent/projects/beta-prime/notes/2026-08-21-day120-general-d-frontier.md` §6.
  Allen–Celano–Mason 2511.18156 is not transportable: their involutions are
  shape-preserving, Rick needed shape-changing.
- **Day 123 → Day 131:** StructB was reformulated away from Kostka combinatorics
  into the E-basis Main Conjecture (`/home/agent/projects/proofs/2026-08-21-day123-e-basis-reformulation.md`),
  and that was PROVED at all $d$ on Day 131 via the operator formula $\Psi(f)=T(fV)/V$
  and $F = A\cdot B$ (`/home/agent/projects/proofs/2026-08-23-psi-e2-egf-closed-form.md`;
  `/home/agent/projects/memory/SUMMARY.md` Day 146 registry, PROVED).

Note the Day 118 identities (A), (B) **as originally posed** remain FALSE for
$d < d_{\max}$ (Day 119 counterexample $j=7$, $d=9$: $K_{(5,5,4)',(2^7)} = 21 \neq 0$);
the corrected $d_{\max}$ versions are theorems. Source:
`/home/agent/projects/proofs/2026-08-20-day119-kostka-ballot-identities.md`.

## Status (as of Day 119/120 — historical)

**Open.** The naïve Day 118 identities are false at $d < d_{\max}$; Day 119 proved the correct identities at $d = d_{\max}$ specifically. For $d < d_{\max}$, no clean identity is yet known — subleading-$t$ terms of $s^*_\mu$ with $d_\mu > d$ couple the equations.

Empirically: $\deg_{u, \pi}(S_j) = j$ for $j \le 8$ (`route_v_probe.py`). So StructB holds at all $d > j$, but the mechanism for $d < d_{\max}$ is different from the $d = d_{\max}$ ballot-cancellation story.

## The obstruction

At $d = d_{\max}$: contribution to $[t^d] S_j$ comes only from $\mu$ with $d_\mu = d$. Top-part 2-dim image (Day 118) gives clean constant + $s$-linear forms. Alternating identities on Kostkas hold via ballot-number formula.

At $d < d_{\max}$: contribution to $[t^d] S_j$ comes from ALL $\mu$ with $d_\mu \ge d$. Subleading-$t$ terms of $s^*_\mu$ (with $d_\mu > d$) contribute to the $[t^d]$ coefficient too. These are NOT controlled by the 2-dim top-part image; they involve higher $s$-degree terms.

**Concrete example (Day 119).** $j = 7, d = 9$: only $\mu = (5, 5, 4)$ has $d_\mu = 9$ (odd parity). But $[t^9] S_7$ also gets contributions from $\mu$'s with $d_\mu \in \{10, 11\}$ via their subleading-$t$ terms. These non-trivially cancel the single $d_\mu = 9$ contribution.

## What's needed

**Task 1: Subleading-$t$ formula for $s^*_\mu$.** Need explicit form of $[t^{d_\mu - k}] s^*_\mu(u=t, y+c=s, yc=t)$ for $k \ge 1$. Candidates:

- Direct Jacobi-Trudi + Molev-Sagan branching (extend Day 118 §2 argument).
- Molev-Sagan Thm 3.1 recursive expansion.
- BHS 2410.06582 §7 "Deformed Miwa parameters" if the Miwa deformation packages subleading terms.

**Task 2: General-$d$ Kostka identity.** Given the subleading formula, express $[t^d] S_j = 0$ (for $j < d < d_{\max}$) as a signed sum over $(\mu, k)$ pairs with $d_\mu = d + k$ and $k \ge 0$. Each pair contributes $K_{\mu', (2^j)} \cdot \text{coeff}_{d, k}(s, \mu)$. The identity is:

$$\sum_{k \ge 0} \sum_{d_\mu = d+k} K_{\mu', (2^j)} \cdot \text{coeff}_{d, k}(s, \mu) = 0 \quad \text{(as polynomial in } s\text{)}.$$

**Task 3: Involution / bijection proof.** Ideally, adapt the Allen-Mason 2511.18156 Garsia-Milne involution to pair $(\mu, T)$ tuples where $T \in \text{SSYT}(\mu', (2^j))$ with appropriate signs. If the involution respects the $d$-filtration, individual $d$-level identities decouple; if it MIXES $d$-levels (as expected), it gives the coupled cancellation directly.

## Attack angles

### Route Allen-Mason (highest priority)

Read Allen-Mason 2511.18156 §2-3 in next PROVE. Adapt tunnel-hook involution to content $(2^j)$. Check whether the pairing respects the $(d_\mu, \mu_2 - \mu_3 \text{ parity})$ structure. If yes → direct cancellation for all $d$.

### Route Local Kostka framework (arXiv:2505.10783)

Explicitly covers $K_{\mu', (2^j)}$ rectangular Kostka. Local bijective inversion. Check whether the bijection has a $(\mu_2 - \mu_3)$-parity filtration.

### Route Lee two-color (2607.02108)

Half-vertex operators on strict partitions with two-color grading. If the two colors = $(\mu_2 - \mu_3)$-parity in Rick's setup, subleading-$t$ terms might have a natural half-vertex-operator expression.

### Route BHS Deformed Miwa (2410.06582 §7)

Miwa parameter deformation in KP hierarchy. May give a shift-parameter degree control on shifted Schurs matching Rick's $(u, \pi)$-wdeg exactly. If yes → StructB is a formal consequence of Miwa filtration.

### Route Direct Molev-Sagan expansion

Compute subleading-$t$ terms of $s^*_\mu$ directly from Molev-Sagan Thm 3.1. Explicit formulas exist for the coefficients $g^\mu_\lambda$ in $s^*_\mu = \sum_{\lambda \subseteq \mu} g^\mu_\lambda s_\lambda$. Track how the $g$'s translate through the $u = t, y+c = s, yc = t$ substitution.

### Route "Differentiate the generating function"

Day 119 discovered that alternating Kostka sums with polynomial-in-$m$ weights reduce to unweighted sums via $(n-2r)\binom{n}{r} = n[\binom{n-1}{r} - \binom{n-1}{r-1}]$. Iterated application should handle polynomial weights of any degree. This gives a **complete toolkit** for the alternating-sum side; what's missing is the closed form of the subleading-$t$ contributions.

## Empirical hints

$\deg_{u, \pi}(S_j) = j$ verified $j \le 8$. So all identities empirically hold.

Numerical pattern to check next PROVE: for $j = 7, d = 9$, compute $[t^9] S_7$ explicitly as a polynomial in $s$. Decompose the contribution by $d_\mu$ (i.e., by $\mu_1$-value). Observe the cancellation pattern. This is the smallest non-trivial coupled case.

## Related open questions

- `q-c1-c2-kostka-auxiliary-identities.md` — the auxiliaries for odd-$j$ $s^0$-part at $d_{\max}$.
- `q-structB-e-wdeg-bound.md` — parent question.

## Files

- `proofs/2026-08-20-day119-kostka-ballot-identities.md` §6 — states the gap explicitly.
- `beta-prime/code/day119/lower_d_check.py` — verifies at what $d$'s the identity holds/fails.
- `for-collaborator/2026-08-20-day119-ballot-kostka-status.md` — Robin update.

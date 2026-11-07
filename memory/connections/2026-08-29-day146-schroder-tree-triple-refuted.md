---
name: Day 146 wake — three template attacks refuted
description: JVMV, AZ, and Rubine all fail as mod-3 templates; Day 145 dream damaged; pivot to Ψ-recursion mod 3
type: project
---

# Day 146 wake — three template attacks REFUTED

**Date:** 2026-08-29 (Day 146)
**Status:** Three strong negatives. Day 145 dream's Schröder tree crown jewel damaged.

**Why:** FPSAC writing kickoff Sept 1 (in 2 days). Need to know before then which templates work and which don't, to correctly frame §5 conjecture stanza.

**How to apply:** When drafting FPSAC §5, phrase the mod-3 sub-claim as an
OPEN CONJECTURE with independent numerical evidence — not as "provable via
Rubine template" or "provable via Schröder tree identification." Both were
attempted and failed. Cite Day 145 Reduction Theorem as the strongest
existing structural result.

## The three failures

### 1. Josuat-Vergès Eq (69) at $e_n = (-1)^n$ — STRONG NEGATIVE

**Paper:** arXiv:1604.04759 (Josuat-Vergès, Menous, Novelli, Thibon, "Free
cumulants, Schröder trees, and operads", Adv. Appl. Math. 2017). Downloaded
to `/home/agent/papers/josuat-verges-schroder-trees-1604.04759.pdf`.

**Formula (Eq 69):** $\kappa_n = \sum_{t \in \mathrm{PST}_n} (-1)^{i(t)-1} S^t$
where $\mathrm{PST}_n$ = prime Schröder trees of weight $n$ (= leaves − 1),
$i(t)$ = number of internal nodes, and $S^t$ is the Polish-notation monomial
in noncommutative moment symbols $S_j$.

**Test:** Substitute $S_j$ from the "$e_n = (-1)^n$" specialization (via
$E(t)H(t)=1$: $h_1=1$, $h_j=0$ for $j \ge 2$, so $S_1 = 1$, $S_{j \ge 2} = 0$).
Result: $\kappa_n = (-1)^{n-1} C_{n-1}$ (alternating Catalans $1, -1, 2, -5, 14, -42, \ldots$).

**Rick's $b_k = 3, 27, 417, 7851, 164124, 3661389, 85384566, 2056373739$ —
does NOT match alternating Catalans.**

**Applicability:** Josuat-Vergès Eq (69) IS the correct free-cumulant formula
and applies to Rick's $M = 1-2F$, but with $S_j = m_j = -2b_j$ (the ACTUAL
moments). This gives:
$$\kappa_n = -\sum_{t \in PST_n} 2^{i(t)} \prod_{v} b_{arity(v)}.$$
Every summand has $\ge 1$ factor of $b_r$ (since $i(t) \ge 1$ for $n \ge 1$
in $PST_n$). So $b_r \equiv 0 \pmod 3 \forall r \implies \kappa_n \equiv 0 \pmod 6$.
**Reproves Day 145's Speicher-Möbius reduction — no new mod-3 machinery.**

**Conclusion:** Day 145 dream's "$b_k$ = Schröder tree weight at $e_n = (-1)^n$"
identification is FALSE at the natural JVMV specialization. The Rick sequence
is elsewhere in the Schröder tree world (if anywhere).

### 2. Amdeberhan-Zeilberger 2506.17862 — SOFT NEGATIVE

**Paper:** arXiv:2506.17862 = **Amdeberhan-Zeilberger**, "Proofs Of Three
Geode Conjectures" (June 2025). *Not Rubine.* (Browse 115 memory had this
misattributed.)

**Technique:** Lagrange inversion + Wilf-Zeilberger certificates to derive
exact closed-form factorial expressions for Geode array slices. Integrality
follows because closed forms are factorials divided by factorials.

**Applicability:** Rick has NO closed form for $b_k$ (Day 144 confirmed not
P-recursive at low order, not in OEIS). His problem is a CONGRUENCE, not a
closed form. Templates don't transfer. Day 144's Lagrange ansatz already
tried and failed (denominators clean but numerators dirty).

### 3. Rubine 2507.04552 — SOFT NEGATIVE

**Paper:** arXiv:2507.04552 = **Dean Rubine**, "Hyper-Catalan and Geode
Recurrences and Three Conjectures of Wildberger" (July 2025). Downloaded
to `/home/agent/papers/rubine-hyper-catalan-recurrences-2507.04552.pdf`.

**Recurrences:**
- Hyper-Catalan (Thm 2): multivariate quadratic-in-index convolution with
  multinomial coefficient.
- Geode (Thm 8): short alternating difference $G_{\mathbf m} = C_{\mathbf m + \vec X} - \sum G_{\text{lesser}}$.

**Proofs:** elementary induction using the two recurrences + factorial
manipulation. Ships closed forms for one-shape and two-shape Geode slices
(Thms 7, 9, 10, 11, 14).

**Applicability to Rick:**
1. **Setting mismatch.** Rubine works in unbounded multivariate $(t_2, t_3, \ldots)$
   ring. Rick's $F$ is univariate. Collapsing to one variable trivializes
   $\mathbf{S}_1 = t_2 + t_3 + \cdots$, which is the Geode factorization's key.
2. **Wrong flavor of integrality.** Rubine proves ℤ-integrality (over integers),
   not mod-p divisibility. No divisibility-by-a-prime statements anywhere in
   the paper.
3. **Coupled system genuinely under-determined.** Rick's $F$/$A$ pair satisfies
   $a_k = -b_k + \sum b_i b_j$ AND $b_k = -a_k + \sum b_i b_j$ — these are the
   SAME identity rearranged. No independent constraint. Rubine's technique
   doesn't generate the missing constraint either.

## What survives

**Day 145 Reduction Theorem** ($\kappa_n \in 6\mathbb{Z} \iff b_n \in 3\mathbb{Z}$)
remains the strongest structural result for the sub-claim. Empirical verification
extended to $n \le 8$. No proof of either direction beyond this equivalence.

**Celestino-Vargas 2311.07824** (Schröder tree antipode formula for
Ebrahimi-Fard–Patras double tensor Hopf algebra) — the OTHER leg of the Day 145
dream's three-way convergence — is UNTOUCHED. Still worth investigating post-FPSAC
for the NSym antipode thread. Independent of today's negatives.

## Pivot direction — Day 146 PROVE seed

**Attack via Ψ-recursion mod 3 (DEFINITION side, not identity side).**

Full Ψ-recursion (Day 131 Theorem A):
$$\Psi_{b+1} = [E_2 - (b+1)E_1 + (b+1)^2]\Psi_b - 3b E_3 \sigma(\Psi_{b-1}) - b(b-1)(E_1 - 2b - 2) E_3 \sigma(\Psi_{b-2}).$$

**Mod 3 observations:**
- $-3b E_3 \sigma(\Psi_{b-1}) \equiv 0 \pmod 3$ — the middle term VANISHES.
- $-2b - 2 \equiv b + 1 \pmod 3$.
- $\sigma(E_1) = E_1 - 3 \equiv E_1$; $\sigma(E_2) = E_2 - 2E_1 + 3 \equiv E_2 + E_1$;
  $\sigma(E_3) = E_3 - E_2 + E_1 - 1$.

So mod 3: $\Psi_{b+1} \equiv [E_2 - (b+1)E_1 + (b+1)^2]\Psi_b - b(b-1)(E_1 + b + 1) E_3 \sigma(\Psi_{b-2}) \pmod 3$.

**A first-and-third-order mod-3 recurrence.** If this induces a mod-3 structure
on $F_P \pmod 3$ that forces $\log(F_P/f) \equiv 0 \pmod 3$ (equivalently, all
$b_k \equiv 0 \pmod 3$), we're done.

**Day 146 PROVE compute plan:** compute $\Psi_b \pmod 3$ for $b = 1, \ldots, 12$
directly and look for the vanishing structural pattern.

## Files

- `/home/agent/papers/josuat-verges-schroder-trees-1604.04759.pdf`
- `/home/agent/papers/rubine-geode-integrality-2506.17862.pdf` (AZ, mislabeled)
- `/home/agent/papers/rubine-hyper-catalan-recurrences-2507.04552.pdf`
- `/home/agent/projects/beta-prime/code/day146_schroder/RESULT.md` — enumeration test.
- `/home/agent/projects/beta-prime/code/day146_schroder/enumerate_schroder.py`,
  `enumerate_v2.py` — five naive Schröder conventions tried, all negative.

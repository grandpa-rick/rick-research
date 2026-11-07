# NC-Geode k=−1 ↔ Free cumulants ↔ FGCCHA free Lie generators (potential triangle)

**Date:** 2026-09-10 (Day 185 dream)
**Status:** hunch — testable in 20 lines of SymPy
**Path bridges:** Path 1 (combinatorial Hopf — FGCCHA) ↔ Path 1 (NT geode / free probability) ↔ Path 4 (Λ* / Kerov, potentially)
**Seed connection:** unifies three independent structural identifications of the same $b_k$ sequence.

---

## The three identifications

Rick's $b_k = (3, 27, 417, 7851, 164124, \ldots)$ (from the algebraic GF $(\dagger)$) admits three structural characterizations, each from an independent origin:

1. **FGCCHA graded dims (Day 183+, unconditional).** $b_k = \dim(U(L(a))_k)$ where $L(a)$ is the free Lie algebra on generators counted by $a_k = \text{INVERTi}(b_k) = (3, 18, 282, 5268, 109647, \ldots)$. AGGSZ Thm 4.2 (arXiv:2505.06941) + Day 183+ $a_k > 0$ proof. Milnor–Moore: $U(L(a))$ is the free graded-commutative Hopf algebra on $a_k$ generators in degree $k$.

2. **Novelli-Thibon geode at k=−1 (Day 143, conjectured).** The quadratic identity $(1 - 2F)^2 = 1 + 4A$ (equivalently $a_k = -b_k + \sum b_i b_j$) is the $k = -1$ slice of the NT noncommutative geode (arXiv:2511.18366).

3. **NEW (Browse 138): free cumulants at k=−1.** NT's geode at $k = -1$ specializes to **free cumulants** via $K = g(-A)^{-1}$ in the free probability sense.

**Claim to test.** The three identifications should refer to the *same* $a_k$: free Lie generator counts (identification 1) = free cumulants of $b(t)$ (identification 3), via the geode k=−1 slice (identification 2).

---

## Why this might be true

**Milnor–Moore over $\mathbb C$:** any graded connected cocommutative Hopf algebra is $U(L)$ for $L$ its primitive Lie subalgebra. When $L$ is free, $U(L)$ is the free non-commutative associative algebra on the same generators (as a bialgebra, ignoring cocommutativity vs. commutativity for the moment).

**Free probability:** the free-cumulant sequence of a random variable determines it (via Cauchy transform inversion). Free cumulants count *free* Lie-algebraic objects when the moment sequence is realized as a Hopf-algebraic sequence.

**Geode k=−1:** the geode's $k = -1$ slice is precisely the free-cumulant-moment inversion identity in NT's noncommutative framework.

**Together:** if $b(t) = \sum b_k t^k$ has free-cumulant sequence $c_k$, and Milnor–Moore gives $U(L(a))$ with $a_k = \text{INVERTi}(b_k)$, then plausibly $c_k = a_k$ up to sign/index conventions. The geode k=−1 provides the bridge.

---

## Verification protocol (20-line SymPy)

Standard free-probability moment-to-cumulant inversion (Speicher-Nica): if $M(t) = \sum m_n t^n$ and $C(t) = \sum c_n t^n$ are moment and cumulant series, then $M(t) = 1/(1 - tC(tM(t)))$ or equivalently $M(t) = 1 + tM(t)C(tM(t))$ (Nica-Speicher §11).

**Concrete test.**
- Let $m_n = b_n$ (Rick's sequence), so $M(t) = 1 + \sum_{n \ge 1} b_n t^n$.
- Compute $c_n$ by inverting the moment-cumulant relation.
- Compare $c_n$ to $a_n = (3, 18, 282, 5268, 109647, \ldots)$.

**Alternative convention.** Some free-probability sources put moments in one series and cumulants in the "reciprocal" one via $K(t) = t / g^{\langle -1 \rangle}(t)$ where $g$ is the Cauchy transform. Try both conventions; agreement in either is meaningful.

**Expected outcomes:**
- **Agreement:** the three-way identification is a theorem (modulo verifying the geode k=−1 is literally the Speicher-Nica inversion). Rick gains a new Path 1 tool: free-probability-of-b(t) is a natural home.
- **Disagreement by a sign/shift:** likely the free-cumulant sequence is a mild transform of $a_k$; still a real connection.
- **Total disagreement:** the geode k=−1 free-cumulant is a different object from Speicher-Nica free cumulants; the connection is looser than hoped. Register as refuted with clear boundary.

---

## Downstream if the triangle holds

**Kerov polynomial bridge.** Λ*-side (Path 1 Λ*, Days 149–150) uses Kerov's polynomials in free cumulants of the *transition measure* to encode normalized character values. If $a_k = \text{free cumulants of } b(t)$, we have:
- $b_k$ = FGCCHA graded dims (algebraic side)
- $a_k$ = free-cumulant generators (free-probability side)
- Kerov polynomial expansion in $a_k$ = normalized $S_n$ character values?

That would be a Path 1 (Hopf) $\leftrightarrow$ Path 1 (Λ*) bridge — Rick would have two independent Path 1 tools converging on the same sequence.

**FPSAC 2027 framing.** If the triangle is provable, this becomes a 6th pillar for the abstract: "$b_k$ = graded dims of a free graded-commutative Hopf algebra whose primitives count free cumulants of the algebraic-GF measure." Even stronger unification story.

---

## Cautions

- **Kerov bridge to Rick's $b_k$-Λ was DEAD as of Day 151** (Rule 6 v2 firing #11) — the Kerov polynomial expansion in free cumulants of transition measures did *not* match Rick's ring. This might be a different Kerov connection (via $a_k$, not via a transition measure of a Young graph walk).
- **"Free cumulants" is convention-dependent.** Speicher-Nica free cumulants (planar non-crossing partitions) vs. NT geode k=−1 free cumulants may not coincide off the shelf.
- **Overclaim risk.** The 3-way identification is aesthetically appealing (Rule 11 flavour: unify by unifying obstructions) but not obviously true. **Numerical test first, structural claim later.**

---

## Related registry / memory

- `chindris-hopf-home-theorem-level.md` (2026-09-09) — the Hopf-home identification.
- `2026-09-09-ak-positive-FGCCHA-unconditional.md` (Day 183+) — the elementary $a_k > 0$ proof.
- `2026-08-28-day143-quadratic-identity-is-geode.md` (Day 143) — the geode-at-k=−1 identification.
- `feedback_log_positivity_lagrange_kernel.md` — the Day 183+ technique.
- Registry claim to add if verified: `bk-ak-are-moment-cumulant-pair` at grade `computed` (after numerical test) → `checked-sober` (after structural argument).

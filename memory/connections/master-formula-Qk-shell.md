---
name: Master Formula for Q_{2m+1}(a, 0, c) at the universal shell point
description: Day 96 PROVE crown jewel. Universal shell point (T-2, 0) with T = smallest 2^t > c−2 lies in EVERY odd-k joint-**Pochhammer**-min shell simultaneously. From there Q_{2m+1}(a, 0, c) factors cleanly into a product of (c−i) factors times a linear-in-a bracket. Verified at m ∈ {0,1,2}; Day 97 CODE extended empirical to m ∈ {3, 4, 5} (72/72). Closes ♥ recursion (**generalised to c EVEN Day 97**) modulo Sub-conjecture 5.2 linearity. CAVEAT (Day 97 CODE): (T−2, 0) is Poch-min but NOT globally shell-min at c=20 for odd k ∈ {9, 11, 13, 15} (interior (2, 4) beats corner by 1); see `corner-first-heuristic-refuted-at-c20.md`.
type: project
tier: S
status: sketched (m ≤ 2 proved rigorously; m ∈ {3, 4, 5} 72/72 empirical Day 97 CODE)
---

## Day 97 update

- **CODE (Day 97):** (M) verified at m ∈ {4, 5} across c ∈ {12, 16, 20, 24, 28, 32} × a ∈ {0..5}: 72/72 exact matches. All 12 factorisations linear in a — matches (M) shape `Q_{2m+1}(a, 0, c) = prefactor · [2m(2m+1)(a+2) − const(c)]`. Empirical support m ≤ 3 → m ≤ 5. Extraction pipeline is fast (<1s per (c, k) fit).
- **PROVE (Day 97):** ♥ recursion generalised from c ≡ 0 mod 4 (Day 96) to c EVEN (Theorem 4.1). Same arithmetic since v_2(c−1) = 0 for all c even. c ≡ 0 mod 4 and c ≡ 6 mod 8 subbranches of D(c) sketched-derived.
- **CAVEAT — corner NOT globally optimal at c=20:** For c=20 odd k ∈ {9, 11, 13, 15}, corner (T−2, 0) v_2 = 34, but interior (2, 4) v_2 = 33. Anomaly locus v_2(c−4) = v_2(16) = 4. (T−2, 0) is Poch-min at Kummer floor but Q_k(a, b, c) has (c−i)² factors that can pick up extra v_2 at interior alignments when v_2(c−i) is anomalously large. **Potential falsification of digit-sum formula at c=20 open** — direct H_20 evaluation is Day 98 CODE priority. See `corner-first-heuristic-refuted-at-c20.md`.


# Master Formula for Q_{2m+1}(a, 0, c) at the Universal Shell Point

**Origin:** Day 96 PROVE (three cycles, 2026-07-14). Files: `projects/proofs/2026-07-14-delta-recursion-odd-k-attempt.md` (main writeup), `projects/proofs/2026-07-14-digit-sum-odd-c-attempt.md` (Day 95 predecessor). For-collaborator note: `memory/for-collaborator/2026-07-14-master-formula-Qk-shell.md`.

## The setup

The Day 88 three-variable factorisation:
```
h_k^{(c)}(a, b) = (a+3)_{c-1-k} · (b+2)_{c-1-k} · Q_k(a, b, c)
```

The joint-Pochhammer-min shell is the set of (a, b) achieving the minimum v_2 of the two Pochhammer factors simultaneously. **Choose:** `T = smallest power of 2 > c − 2`. Then evaluate at `(a, b) = (T − 2, 0)`.

**Why this point works.** At `a = T − 2` and `b = 0`:
- `(a+3)_{c-1-k}` becomes `(T+1)_{c-1-k}` — a Pochhammer starting just past T = 2^t.
- `(b+2)_{c-1-k}` becomes `(2)_{c-1-k} = (c-k)! / 1! = (c-k)!`.

Both Pochhammer factors sit at their Kummer floor because `T = 2^t` shifts them into a regime where every consecutive factor's v_2 is the v_2 of its natural counterpart — the block-arithmetic trick from the Day-93 LB_1 Lean proof, exactly. It's `2^K + i ≡ i (mod higher powers of 2)` applied at the joint level.

**The point is c-uniform:** as c varies, T tracks c but the SHAPE of the achiever `(T−2, 0)` is uniform. This is the crucial thing — no ad-hoc per-c achiever hunting.

## The Master Formula (M)

For k = 2m+1, m ≥ 1:
```
Q_{2m+1}(a, 0, c) = c(c-1)(c-2m) · [Π_{i=2}^{2m-1}(c-i)^2] · [2m(2m+1)(a+2) − (c-1)(c-2m)(c-2m-1)]
```

**Structure:**
- **Prefactor** `c(c-1)(c-2m) · Π_{i=2}^{2m-1}(c-i)^2` — a product of (c-i) factors with specific multiplicities. All the "interior" factors get squared; three boundary factors (c, c-1, c-2m) appear linearly.
- **Bracket** `[2m(2m+1)(a+2) − (c-1)(c-2m)(c-2m-1)]` — linear in a. The a-linear term `2m(2m+1)(a+2)` looks like a Pochhammer coefficient; the a-independent term `(c-1)(c-2m)(c-2m-1)` picks out three boundary factors of the (c-i) range.

**Verification:**
- **m = 0 (k = 1):** Direct from Q_1 = −c(c-1) — trivially matches (empty product).
- **m = 1 (k = 3):** Verified at all c ≥ 4 against Day 88 catalog.
- **m = 2 (k = 5):** Verified at all c ≥ 6 against Day 88 catalog.
- **m = 3 (k = 7):** Prediction:
    ```
    Q_7(a, 0, c) = c(c-1)(c-2)²(c-3)²(c-4)²(c-5)²(c-6) · [42(a+2) − (c-1)(c-6)(c-7)]
    ```
  Matches empirical Δ_7 at c ∈ {12, 16, 20, 24, 28, 32}. Not verified against direct Q_7 catalog extraction (that would upgrade to `checked-sober`).

## Consequence — the ♥ recursion closes uniformly (modulo linearity)

If (M) holds for all m ≥ 1, then for c ≡ 0 mod 4 and k odd, 1 ≤ k ≤ c−3:
```
Δ_{k+2}^{(c)} − Δ_k^{(c)} = 2·v_2(c-1-k)      (♥, verified empirical at c ∈ {8, 12, 16})
```
follows uniformly. Combined with the Day 94 result `LB_1 = target at c ≡ 0 mod 4`, this closes the c ≡ 0 mod 4 branch of the digit-sum formula fully (modulo SCP LB=UB, which is a lower-order gap).

## The master identity (◊) and unconditional [a^k] Q_k = 0

Cycle 2 (Day 96) introduced:
```
(c − k + 1)_{k−j} · c^{↓j} = c^{↓k}      (◊)
```
where c^{↓k} is the falling factorial. **Two-line proof.**

**Corollary:** `[a^k] Q_k(a, 0, c) = 0` for k ≥ 1, unconditionally at k ≤ 6. Conditional on `L_j(c) := [a^j] P_j(a, 0, c) = c^{↓j}` for j ≥ 7.

**Theorem 11.5 (bootstrap equivalence):** `L_j = c^{↓j} for all j ⇔ [a^k] Q_k = 0 for all k`.

This drops rigorous `deg_a Q_k(a, 0, c) ≤ k − 1` from the empirical `≤ 1`. The gap between k−1 and 1 is Sub-conjecture 5.2 (see `questions/q-subconjecture-52-Qk-linearity.md`).

## The subleading identity (★★) and L_{j, 1}(c) bootstrap

Cycle 3 (Day 96) attacked `[a^{k-1}] Q_k(a, 0, c) = 0` for k ≥ 3. Splits into TermA (from L_{j, 1}(c) coefficients of P_j) and TermB (from Vieta e_1 acting on L_j). TermB vanishes automatically via the forward-difference identity
```
Σ (-1)^m C(k, m)·poly(m, deg<k) = 0    for k ≥ 3
```
which is Hopf-algebraic in flavour (finite-difference operator ~ coproduct evaluation).

TermA gives a recursion on L_{j, 1}(c), bootstrap-solved:

| j | L_{j, 1}(c) |
|---|-------------|
| 0 | 0 |
| 1 | 2c |
| 2 | c(3c − 5) |
| 3 | 3c(c − 2)(c − 3) |
| 4 | 2c(c − 2)(c − 3)(c − 7) |

All verified against direct extraction from Clio's H_5 catalog. **Sketched** for k ≤ 4; extending to k ≥ 5 needs general-c closed forms of P_3, P_4, P_5, P_6 (Clio-ping request filed at `for-collaborator/2026-07-14-Pj-closed-forms-request.md`).

## Registry disposition

- `Qk-leading-a-vanishing` — **proved** for k ≤ 6, conditional for k ≥ 7 on L_j = c^{↓j}.
- `Pj-leading-coefficient-c-falling-factorial` — **checked-sober** (empirical for j ≤ 6; part of the equivalence Theorem 11.5).
- `subleading-a-k-minus-1-vanishing-in-Qk` — **sketched** for k ≤ 4; needs P_j closed forms for k ≥ 5.
- `Lj1-bootstrap-formula` — **checked-sober** for j ≤ 4.
- Master Formula (M) itself: **sketched** — proved at m ∈ {0,1,2}, verified empirically at m = 3.

## Seed connections

**Path 1 (Combinatorial Hopf Algebras).** The P_j polynomial is `Σ_μ K_{μ^T, (2^j)} R_μ(a, b, c)` where K is a Kostka number and R_μ = D_μ/D_∅ is an Aitken-determinant ratio. The Master Formula is what happens when this Kostka sum is evaluated at the universal shell point. That's a genuine Sym-side identity. The forward-difference vanishing (TermB) is Hopf-algebraic: finite differences dualize to divided-power coproduct evaluations.

**Path 4 (Coproduct-Crystal).** The (◊) master identity `(c-k+1)_{k-j} · c^{↓j} = c^{↓k}` is a Pochhammer/falling-factorial identity — the same shape as identities that appear in crystal counting when restricting a rectangular tableau to a subshape. Speculative but worth revisiting.

## Why this matters — the "changing the question" move

Day 95 tried ad-hoc achievers per c and only closed k = 3. The universal shell point (T-2, 0) gives a c-uniform member of the joint-Pochhammer-min shell — one point that works for all c. This reduces the whole ♥ question to the 2-adic behaviour of Q_k at a single specific integer point, and the pattern reveals itself.

**Meta-lesson:** when stuck on "find an achiever at each c", ask "find a c-uniform achiever." The c-uniform member usually sits at a corner of the shell lattice, and corners are usually where the arithmetic simplifies. This is Rick's version of "change the problem": one level of abstraction up, one level of computation down.

## What could kill this

- **Sub-conjecture 5.2 falsification.** If Q_k(a, 0, c) is NOT linear in a for some k, the Master Formula generalizes but doesn't have the clean bracket shape. Empirical evidence for linearity is strong (k ≤ 6) but not proved.
- **(M) at m ≥ 3 doesn't match direct Q_7 extraction.** The empirical Δ_7 match at 6 c-values is strong evidence but not a direct catalog check. A CODE cycle should extract Q_7(a, 0, c) as a polynomial in (a, c) and compare against (M) at m = 3.

## Companion connection

See `connections/amdeberhan-formula-as-Dc-tool.md` — the Amdeberhan v_2((a)_k) formula is the tool for translating this Q_k-side result to the D(c) side (i.e., the digit-sum formula for β'(c)).

## Cross-program pattern — corner of the coordinate lattice (Day 96 dream 2)

The universal shell point (T−2, 0) is a **corner** of the (a, b) coordinate plane on the parity shell (b at minimum; a just past a power-of-2 boundary). This is the fourth data point of **single-carrier dominance** (Day 89 dream 2) with a spatial refinement: the winning carrier lives at a corner of a natural coordinate object.

Sibling instances:
- **SCP** (`sharp-cancellation-single-carrier.md`) — β'(c) achievers (0,0,0), (3,0,2), (7,0,2), (8,8,2) all near axis/diagonal corners of (a, b, k).
- **R-AXIS** (`cover-restricted-axis-as-right-invariant.md`) — p_1 vertex of the axis simplex.
- **Bucket-0** (`bucket-0-as-sl2-rump.md`) — one piece of the 26-piece minimal cover.

Shared shape: **invariant realized at a vertex/corner/boundary of the natural coordinate space, not in the interior**. Corners kill degrees of freedom, saturate inequalities, or hit special integer alignments. Predictive content: **hunt at corners first** when looking for c-uniform or n-uniform witnesses.

— Rick, Day 96 dream cycle, 2026-07-14.

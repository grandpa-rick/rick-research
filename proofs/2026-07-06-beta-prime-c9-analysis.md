# β' at c=9 — analysis of the dimer-law breakdown

**Author:** Rick
**Date:** 2026-07-06 (Day 82)
**Trust:** computed / hunch (NOT proved).
**Files:**
- `/home/agent/projects/code/2026-07-06-beta-prime-analysis.py` (main analysis)
- `/home/agent/projects/code/2026-07-06-beta-prime-c11-scan.py` (extension attempt)
- Ground truth: `/home/agent/projects/reviews/2026-07-05-review-clio.md` §2
- Clio's data: mail 2026-07-04 05:28 and 17:56; 2026-07-05

---

## 1. Precise setup

Let λ = (a+b+c, b+c, c) with a ≥ 0, b ≥ 0, c ≥ 1 (three-row shape).
Let H_c(a,b,j) be Clio's *heavy quotient* — a polynomial in (a,b,j) sitting in
the M_j = Q_c/L_c decomposition (see her c=5 note §1.1).

- **β(c)** = **rigid NL anchor**. Closed form:
  β(c) = (c-1) + v₂((c-1)!) = 2(c-1) − s₂(c-1).
  Values c=1..12: 0, 1, 3, 4, 7, 8, 10, 11, **15**, 16, 18, 19.
  Ambient carry floor coming from a single binomial C(m,j) in Kummer's identity.
  **Monotone** in c.

- **β'(c)** = **heavy-quotient constant floor**:
  β'(c) := min over box-interior (a,b,j) of v₂(H_c(a,b,j)).
  Values (Clio) c=4..10: 4, 3, 7, 6, 11, **9**, 14.
  **Non-monotone**; NO known closed form.

- **γ(c)** = content of H_c(0) on the valid-parity sheet (Theorem A closed form):
  even c=2k:  γ = 4k − 2 − s₂(k) − s₂(k−1);
  odd  c=2k+1: γ = 4k − 2·s₂(k).
  γ(c) upper-bounds β'(c) (achievable at j=0).

- **Dimer law** (Job B conjecture): β'(2k+1) = β'(2k) − 1.
  This holds at c=5 (3 = 4−1) and c=7 (6 = 7−1), but **fails at c=9**:
  β'(9) = 9, not β'(8) − 1 = 10.

- **Why c=9 matters**: this is Clio's marquee anomaly — the first case where the
  clean odd-even dimer pattern breaks. If Rick's FREE/RIGID calculus can *predict*
  this failure from the ambient/internal decoupling, that is the joint-note headline.

---

## 2. Table of the two floors and γ, dip for c ∈ {1..12}

| c   | c−1  | s₂(c−1) | v₂(c−1) | v₂((c−1)!) | β(c) | γ(c) | β'(c) | γ − β' (dip) |
|-----|------|---------|---------|------------|------|------|-------|--------------|
|  1  |  0   |   0     |   ∞     |   0        |  0   |  0   |   —   |   —          |
|  2  |  1   |   1     |   0     |   0        |  1   |  1   |   —   |   —          |
|  3  |  2   |   1     |   1     |   1        |  3   |  2   |   —   |   —          |
|  4  |  3   |   2     |   0     |   1        |  4   |  4   |   4   |   0          |
|  5  |  4   |   1     |   2     |   3        |  7   |  6   |   3   |   3          |
|  6  |  5   |   2     |   0     |   3        |  8   |  7   |   7   |   0          |
|  7  |  6   |   2     |   1     |   4        | 10   |  8   |   6   |   2          |
|  8  |  7   |   3     |   0     |   4        | 11   | 11   |  11   |   0          |
|  9  |  8   |   1     |   3     |   7        | 15   | 14   |   9   |   **5**      |
| 10  |  9   |   2     |   0     |   7        | 16   | 15   |  14   |   1          |
| 11  | 10   |   2     |   1     |   8        | 18   | 16   |   ?   |   ?          |
| 12  | 11   |   3     |   0     |   8        | 19   | 18   |   ?   |   ?          |

β'(c) for c ∈ {1,2,3,11,12}: **not yet computed** — I do not have Clio's full
H_c closed form (only H_5 explicit in code). γ(c) provides upper bounds.

---

## 3. Rick's hypothesis — refined

**Original hypothesis (email 07-05):** c ≡ 1 (mod 4) is where "internal 2-adic
decouples from ambient." **Rebutted by data**: c=5 is c ≡ 1 (mod 4) but the dimer
law HOLDS at c=5. So the mod-4 form is too coarse.

**Refined hypothesis (this note):** the correct 2-adic obstruction is

  **v₂(c − 1) ≥ 3**, equivalently  **c ≡ 1 (mod 8)**.

Test against all known data:
- c=3  (v₂=1): dimer status unknown, but not predicted to fail. ok.
- c=5  (v₂=2): dimer holds ✓ (predicted no fail).
- c=7  (v₂=1): dimer holds ✓ (predicted no fail).
- c=9  (v₂=3): dimer **FAILS** ✓ (predicted fail — first case where c−1 = 2³ is a
  pure power of 2).
- Predicted for future test:
  - **c=13 (v₂=2): should HOLD.**
  - **c=17 (v₂=4): should FAIL** (c−1 = 16 = 2⁴, even more so than c=9).
  - c=11, 15, 19 (v₂=1): should hold.
  - c=25 (v₂=3): should FAIL.
  - c=33 (v₂=5): should FAIL.

**Explanation:** Kummer's identity for v₂((c−1)!) picks up a *jump* of exactly
v₂(c−1) when incrementing c-1 by 1 into a multiple of 8. That jump enters β
additively (β = 2(c−1) − s₂(c−1)), but in the heavy quotient H_c it enters
multiplicatively via the run-content — and when the jump is ≥ 3, the internal
factorization admits an extra collapse at some (a,b,j) that the run-content
minimum γ(c) can't see. β' picks up this collapse; β does not.

**Structural precondition for the refinement:** the dip γ(c) − β'(c) grows sharply
with v₂(c−1) among odd c:

| c  | v₂(c−1) | γ − β' |
|----|---------|--------|
|  5 |   2     |   3    |
|  7 |   1     |   2    |
|  9 |   3     |   **5**|

The dip at c=9 is more than double the dip at c=7 — a signature of the extra 2-adic
event when c-1 is a pure power of 2 ≥ 8.

**Secondary hint (also just a hunch):** track Δ(β − β') across consecutive c to see
where the "channels decouple":

| step   | Δv₂((c−1)!) | Δβ | Δβ' | Δ(β − β') |
|--------|-------------|-----|-----|-----------|
| 4 → 5  |  +2         | +3  | −1  |    +4     |
| 6 → 7  |  +1         | +2  | −1  |    +3     |
| 8 → 9  |  +3         | +4  | −2  |    +6     |

Δ(β − β') at 8→9 is *exactly* 2·v₂(c−1) = 2·3 = 6, and at 4→5 is 2·v₂(4) = 4.
At 6→7 it's 3 vs 2·v₂(6) = 2, off by 1 (s₂ carry). The clean pattern is:
**Δ(β − β') ≈ 2·v₂(c−1) at odd c**, with a +1 correction when s₂(c−1) climbs.
This is a testable secondary prediction alongside the mod-8 hypothesis.

---

## 4. What this DOES NOT prove

- No closed-form derivation of β'(c) — this is a data-fitted hypothesis.
- I have not independently computed β'(9) = 9; I am relying on Clio's report
  (her witness at (31,24,2), quoted in the 07-05 review). Reproducing β'(9)
  independently is the immediate follow-up.
- No mechanism-level proof that "v₂(c−1) ≥ 3 forces extra collapse." The story
  I told (Kummer jump enters H_c multiplicatively) is a **hunch**, not a proof.
- I did not compute β' for c ∈ {11, 12, 13} — this needs Clio's general H_c form
  or a from-scratch reconstruction of the M_j = Q_c/L_c expansion.

---

## 5. Next experiment (1 sentence)

**Compute β'(13) and β'(17) directly**: if β'(13) satisfies the dimer law
(β'(13) = β'(12) − 1) but β'(17) breaks it, the "c ≡ 1 (mod 8)" refinement is
confirmed and the joint-note headline is essentially written.

---

## 6. Registration

Trust level: **computed** for the numeric table (γ(c) formula independently
reproduced against brute-force at c ∈ {4..12}), **hunch** for the "c ≡ 1 mod 8"
hypothesis. NOT proved.

Filed under: joint-note preparation, β/β' two-floor structure.

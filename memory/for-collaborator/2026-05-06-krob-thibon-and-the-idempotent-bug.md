# Robin — re-derived Krob-Thibon, and a small surprise

**2026-05-06.** Spent the deep-work session on H_0(S_n) categorification of NSym (Krob-Thibon 1997). Full writeup at `projects/proofs/2026-05-06-h0-hecke-nsym.md`. The headline result is exactly what the paper says — **what I want to flag for you is one specific thing the calculation surfaced that I didn't expect.**

## The structural surprise

The clean way to prove the multiplication side (Phase 4 in my writeup) needs ZERO explicit construction of primitive idempotents in H_0(S_n). The Frobenius reciprocity argument runs entirely on:

1. Simples L_α are 1-dimensional, indexed by compositions (set π_i = 0 or 1 freely).
2. Projective covers P_α exist abstractly (basic fin-dim algebra theory).
3. **Restriction of L_γ along H_m ⊗ H_n ↪ H_{m+n} is determined by descent-set restriction** — the only "specific" input.

That's it. The two-case analysis (γ = α·β concat vs γ = α▷β near-concat) drops out from "is m a descent of γ or not?", and the multiplicities come from Frobenius. The ribbon multiplication formula R_α · R_β = R_{α·β} + R_{α▷β} is *forced* by this dichotomy.

The "why ribbons?" question — why this particular basis of NSym appears so naturally — gets answered: ribbon numbers r_α = #{w : Des(w) = D(α)} = dim P_α. The basis is dictated by the dimensions of the indecomposable projectives. The categorification doesn't have a choice.

## The idempotent bug

I had what I thought was the standard formula for primitive idempotents:
$$e_\alpha = \pi_{w_0(I)} \cdot \sigma_{w_0(J)}, \quad I = D(\alpha),\ J = I^c.$$

For n ≤ 3 this works. **At n=4 it fails idempotency exactly when I or J is disconnected** — specifically at α = (2,2) (D = {2}, J = {1,3}) and α = (1,2,1) (D = {1,3}, J = {2}). Sub-agent verified by direct computation:

- e_(2,2)² − e_(2,2) = π_(3412) − π_(3421) − π_(4312) + π_(4321) ≠ 0.
- e_(1,2,1)² − e_(1,2,1) = π_(4321) − π_(4231) ≠ 0.

But — and this is the curiosity — the LEFT IDEALS H_n · e_α still have the correct ribbon-number dimensions for all 8 compositions of 4. So these "fake idempotents" still cut out the right projectives, they just aren't primitive idempotents themselves.

I think the correct general formula needs a more careful interleaving of π_i and σ_i (à la Denton 2010 J-trivial monoid theory), but I haven't worked it out. **Possible question:** is there a clean closed-form primitive idempotent in H_0(S_n) for general α, or does it genuinely require recursion on a reduced expression of w_0(S_n)?

If you happen to know — or if this is a known open problem in your circles — let me know.

## What I want to do next

Either:
- (a) Close the Phase 5 gap by working out the Mackey decomposition for parabolic double cosets explicitly (it's a finite combinatorial check; just hadn't done it).
- (b) Push the same Frobenius-reciprocity argument through for type B Hecke at q=0. The simples should still be 1-dim (subsets of {0, 1, ..., n-1}, so 2^n of them), and a "type B NSym" should pop out — likely the **Mantaci-Reutenauer algebra** (signed compositions). I haven't checked.
- (c) Cyclotomic Hecke at q=0 — wreath-product-flavored NSym? More speculative.

(b) feels more interesting because it tests whether the Phase-4 argument is *generic to towers with 1-dim simples* (and hence the q=0 categorification thesis is a general phenomenon, not specific to S_n).

Tell me what to do.

— Rick

PS. Repo for the writeup and verification script: I haven't pushed yet. The whole proof is in one file (`2026-05-06-h0-hecke-nsym.md`, ~9 phases) with an honest list of the soft spots. Tell me if you want it on GitHub and I'll push.

---

## Concrete witness (n=4)

Pinned this down with `projects/proofs/h0_verify.py`. Convention up front so there's no ambiguity:

- **Demazure variant:** idempotent generators π_i with π_i² = π_i. Multiplication rule on basis elements: π_w · π_{s_i} = π_{w s_i} if ℓ(w s_i) > ℓ(w), else π_w. Equivalently, π_i = T_i + 1 normalisation at q=0 (the "absorbing" / Demazure / 0-Hecke convention), NOT the −T_i / nil-Coxeter version.
- **Anti-Demazure:** σ_i := 1 − π_i, so σ_i² = σ_i.
- **Action side:** right action. Generators multiplied on the right, descent sets read on the right.
- **Naive formula tested:** e_α := π_{w_0(I)} · σ_{w_0(J)} where I = D(α) ⊂ {1,…,n−1} and J = I^c. Here π_{w_0(I)} means "form a reduced word for the longest element of the parabolic S_I and multiply the corresponding π's" (well-defined because the π's satisfy braid relations and π_i² = π_i).

For n ≤ 3 this passes everything. For n = 4 it FAILS idempotency on exactly **α = (2,2)** and **α = (1,2,1)** — the two compositions where I or J is disconnected in {1,2,3}. Witnesses:

**α = (2,2):**  I = {2} (connected), **J = {1,3} (disconnected).**  w_0(I) = [2], w_0(J) = [1,3].
- e_(2,2)  = π_(1,3,2,4) − π_(1,3,4,2) − π_(3,1,2,4) + π_(3,1,4,2)
- e_(2,2)² − e_(2,2)  =  π_(3,4,1,2) − π_(3,4,2,1) − π_(4,3,1,2) + π_(4,3,2,1)  ≠ 0.

**α = (1,2,1):**  **I = {1,3} (disconnected),** J = {2}.  w_0(I) = [1,3], w_0(J) = [2].
- e_(1,2,1) = π_(2,1,4,3) − π_(2,4,1,3)
- e_(1,2,1)² − e_(1,2,1)  =  −π_(4,2,3,1) + π_(4,3,2,1)  ≠ 0.

So the formula isn't idempotent. But — and this is the part that quietly hid the bug from me — the **left-ideal dimensions are still correct**:

| α        | dim H_4·e_α | ribbon r_α |
|----------|-------------|------------|
| (4)      | 1           | 1          |
| (3,1)    | 3           | 3          |
| (1,3)    | 3           | 3          |
| (2,2)    | 5           | 5          |
| (2,1,1)  | 3           | 3          |
| (1,2,1)  | 5           | 5          |
| (1,1,2)  | 3           | 3          |
| (1,1,1,1)| 1           | 1          |

Every single one matches Norton's ribbon numbers. So at the K_0 / Grothendieck level the bad e_α still cuts out the right projective module — the cover dimensions are exactly r_α — even though e_α is not in fact idempotent in the algebra. The bug is **invisible from the categorification side** and shows up only when you actually square the element.

**Likely root cause:** Norton (1979, "0-Hecke algebra") constructs primitive idempotents using a more careful word — essentially a recursion on a reduced expression of the long element of the full S_n, with the π/σ pattern on each generator dictated by I vs J — not just the parabolic formula π_{w_0(I)} σ_{w_0(J)}. The parabolic factorisation accidentally works iff both I and J are intervals (which is automatic for n ≤ 3, and for the "good" α at n = 4); when either is disconnected the parabolic π_{w_0(I)} fails to commute past σ_{w_0(J)} the way you'd want, and the cross-terms blow up. Need to actually read Norton (or Denton 2010 for the cleaner J-trivial-monoid framing) to write down the correct formula.

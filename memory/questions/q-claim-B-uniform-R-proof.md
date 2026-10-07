---
name: OQ-CLAIM-B-UNIFORM-R — uniform-in-R proof of v_2(Q_{2R}(R-2, R, c)) = C_R constant
description: Day 113 update. (M) Day 109, (R_1) Day 110, (T-a) Day 112, Lemma 1 Day 113. $(\star)_{R=2}$ IS A THEOREM. For R ≥ 3: still need Slice-k for k ≥ 2 independently. Full Claim B (higher c_k v_2 constancy): still open, will be corollary once (★) is uniform.
type: project
---

## Day 113 headline (2026-08-19)

**$(\star)_{R=2}$ is a THEOREM** via Lemma 1 (Day 113) closing the reduction
chain. For $R \geq 3$: Sahi–Okounkov saturation reaches only $R = 2$; Slice-$k$
for $k \geq 2$ must be proved independently. Route: shifted-Schur interpolation
should handle each Sublemma $(U_k)$ directly.

Full Claim B (higher c_k v_2 constancy) is still separate — arithmetic beyond
the algebraic-uniformity attack.

---


# OQ-CLAIM-B-UNIFORM-R

**Priority:** HIGH — narrowed further Day 112; **$(\star)_{R=2}$ now theorem modulo one lemma**.

**Day 112 update.** **(T-a) PROVED modulo $(\star\star\text{-}a'')_{p \geq 1}$**;
by $(a \leftrightarrow b)$-symmetry, (T-b) follows via mirror lemma.
Hence (T) = (T-a) ∧ (T-b) PROVED modulo two mirror lemmas. See
`connections/T-bound-split-Ta-Tb.md` and `proofs/2026-08-19-day112-Ta-proved.md`.

**Consequence at $R = 2$:** Sahi–Okounkov mental calc — with 3 unknowns
$f_0, f_1, f_2$ in the ansatz, Slice-0 = (M), Slice-1 = $(R_1)$, and
(T) + symmetry saturate the constraint on $f_2$. Slice-2 becomes AUTOMATIC.
So $(\star)_{R = 2}$ is a THEOREM modulo $(\star\star\text{-}a'')_{p = 1}$ (and
$b$-mirror) — a single Pochhammer-factorization lemma. See
`proofs/2026-08-19-day112-SYNTHESIS.md`.

**Day 110 update.** **(R_1) PROVED uniformly in R** — see
`connections/M-and-R1-slice-decomposition-framework.md` and
`proofs/2026-08-18-day110-R-level1-proved.md`. Interpolation theorem
built: full slice decomposition reduces to (T) + Slice-k for k ≥ 2. At R = 2,
$(\star)$ is contingent only on (T). Once (T) closes, $(\star)_{R=2}$ becomes
a theorem. Once (T) + Slice-2 close, $(\star)_{R=3}$ too. Recipe extends.

**Day 109 update.** **(M) PROVED uniformly in k** — see
`connections/M-master-identity-PROVED.md` and `proofs/2026-08-18-day109-M-proved.md`.
This makes Appendix F a theorem (special case k = 2R). Consequence: (★) uniform
proof now reduces to (R) recursion + (LC) leading coef. The c_0(R) part of Claim B
is CLOSED via (M) + Appendix F.

**Day 107 status update.** The closed form (★) `Q_{2R}(a, b, R) = (-1)^R
(2R)! · A_R(a) · B_R(b)` (verified R = 2..5 full polynomial identity) gives
c_0(R) = Q_{2R}(R-2, R, R) UNIFORMLY in R, modulo the uniform-in-R proof of
(★) itself. The uniform proof reduces to Appendix F (Weyl-boundary
b-independence), see `connections/Q-boundary-b-independence.md`.

**Remaining gap for FULL Claim B:** prove that ALL higher c_k coefficients
(k ≥ 1) of Q_{2R}(R-2, R, R + 16t) satisfy v_2(c_k) ≥ C_R + 1. This is
the "constancy" part of Claim B that (★) does NOT immediately give.

**Statement.** Prove that for all R ≥ 2 and all c ≡ R mod 16 with c ≥ 2R + 1,
```
v_2(Q_{2R}(R-2, R, c)) = C_R,
```
where C_R is the specific integer given by (H3-C_R):
```
C_R = ⌈log_2(R+2)⌉ + 4R - 2 - s_2(R-1) - s_2(R) - s_2(R+1) - K_R,
K_R = s_2((c-R)/4 - 1) - s_2((c-R)/16)   (c-uniform).
```

## Individual R status (Day 104)

| R  | C_R | proof technique                                | file                                     |
|----|-----|------------------------------------------------|------------------------------------------|
| 2  | 5   | elementary Q_4 mod 32                          | `proofs/2026-08-13-day104-...md` §5.5    |
| 4  | 13  | symbolic Q_8 mod 2^14 (crown-jewel)            | `proofs/2026-08-13-day104-...md` §5.4    |
| 6  | 18  | polynomial fit Q_{12} + coef v_2 mod 2^19      | `proofs/2026-08-13-day104-...md` §5.3    |
| 10 | 34  | polynomial fit Q_{20} + coef v_2 mod 2^35      | `code/2026-08-13-day104-R10-proof-via-fit.py` |
| 14 | 47  | empirical (1 pt, via identity ♦)               | Day 102 `2026-07-18-...anchor...json`    |

## Why per-R doesn't generalize

Each per-R proof reduces to computing a polynomial Q(t) = Q_{2R}(R-2, R, R + 16t)
mod 2^{C_R+1} and checking:
- constant coefficient c_0 has v_2 = C_R exactly;
- all higher-degree coefficients c_k (k ≥ 1) are divisible by 2^{C_R+1}.

For a given R this is a finite computation of size O((2R)^3) in the polynomial fit
plus O(2R · C_R) in the modular reduction. But there's no uniform ARGUMENT for
why this pattern should hold for all R.

## Route 1: Kummer #728 (Erdős Problem, 2601.07421)

**Technique:** stratify a combinatorial sum by 2-adic carry patterns and use
Kummer's theorem (v_2(C(n, k)) = number of carries when adding k and n-k) to
control class-uniform 2-adic behavior.

**Fit to Claim B:** if Q_{2R}(R-2, R, R + 16t) admits a decomposition as a
sum of binomials Σ_j α_j(R) · C(N(R, t), M(R, t, j)) with class-controlled
carry structure, Kummer gives the class-uniform v_2.

**Priority read:** 2601.07421, Day 105 wake.

**See:** `connections/kummer-728-carry-counting-for-claim-B.md` for the full
argument sketch.

## Route 2: Beluhov abacus (2506.12789)

**Technique:** encode combinatorial data on an abacus and read off v_2 as a
carry count. Beluhov's ν_2(W_d(n)) = (ν_2(d)+1) · s_2(n) has the same
structural shape as Rick's D(c) = s_2(m) + v_2(m).

**Fit to Claim B:** if Q admits an abacus interpretation with beads
positioned by R-related data and c-related shift, carrier constants become
counts of specific bead configurations, and c-uniform-modularity follows.

**Priority read:** Beluhov 2506.12789 §2-3, deferred from Days 96-101.

**See:** `connections/beluhov-abacus-template-for-dc.md`.

## Route 3: Symbolic Q_{2R} via generating functions

**Technique:** attempt to derive a closed-form generating function for
Q_{2R}(R-2, R, c) valid for general R, then reduce mod 2^{C_R+1} symbolically.

**Status:** UNLIKELY. Q_k(a, b, c) is polynomial in a, b, c (Day 88 three-var
factorization) but has degree 2k in c. Closed-form GF would need to encode
this in one variable — no known technique.

**Priority:** LOW. Try only if Routes 1 & 2 fail.

## Route 4: Categorification via Sym ⊗ Sym

**Technique:** Q_{2R}(R-2, R, c) is (up to the Pochhammer factor) a value of
h_{2R}^{(c)}(R-2, R), which is a Sym-function multiplicity ⟨s_μ, ...⟩. If
the multiplicity has a plethystic / crystal / Hopf-algebraic interpretation
with c encoded as a formal variable, 2-adic behavior might follow from
representation-theoretic constraints.

**Status:** SPECULATIVE. Requires the Day 85 `Mj-as-sym-function-multiplicity`
framework to extend to Q, which it doesn't obviously.

**Priority:** LOW-MEDIUM. Track passively.

## Falsification conditions

The question is FALSIFIED if:
- Any R gives v_2(Q_{2R}(R-2, R, c)) ≠ C_R for some c ≡ R mod 16.
- Specifically: R = 18 empirical measurement giving C_18 = 65 (Family A)
  would kill H3 as stated (though a modified `ε_R = min(⌈log_2(R+2)⌉, ...)`
  saturation variant might survive).

## Related open questions

- **OQ-CLAIM-A-RIGOR** — single-carrier at k = 2R. Empirically overwhelming
  but not proved. Route: mod-2^ν residue check extended to k = 0, ..., 2R-1.
- **OQ-R-18-CHEAP-PROBE** — need a computationally cheap R = 18 discriminator.
  Full Q_{36} catalog fit ~15h.

## Impact if closed

If Claim B is proved uniformly:
- **H3 becomes a theorem.** ε_R = ⌈log_2(R+2)⌉ uniformly.
- **The piecewise D_anchor(c) conjecture is CLOSED** (contingent on Claim A).
- **The R = 18 test resolves** without empirical computation.
- **Day 104's four per-R proofs become instances** of a general theorem.
- **The β' program has a structural spine** — everything can be re-derived
  from the anchor-family carrier structure.

This would be the LARGEST structural result of the β' branch since Day 92
(Rowland-Yassawi polynomial-valuation impossibility) closed the polynomial
route.

## Meta

Rick's β' arc: Days 91–102 were computation-heavy pattern-hunting; Day 103
did the pattern-match; Day 104 nailed the per-R mechanism. The uniform-R
step is the next abstraction level up. Kummer #728 dropping in Browse 96
(same day as Day 104) is fortuitous — this technique wasn't on Rick's
radar before then.

— Rick, Day 104 dream, 2026-08-13.

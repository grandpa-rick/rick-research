---
name: All three routes to Mj-c-uniform-conjecture promotion CLOSED NEGATIVE (Day 90)
description: Day 90 (2026-07-12) — Routes (i) Kannan-Song Λ^[2] plethystic action, (ii) Motzkin K-triangle single-family identification, and (iii) Bechtloff Weising plethystic (α, β) hunt all closed NEGATIVE in one wake session. M_j c-uniformity is NOT explainable by any of the three suspected mechanisms. Pivot: elementary LB_k^{(c)} closed form via Kummer/Legendre + Q_k mod 2, targeting SCP → `proved uniformly` and D1 → `proved` bypassing M_j promotion entirely.
type: project
---

# All three routes to M_j c-uniformity CLOSED NEGATIVE (Day 90)

## TL;DR

Day 89 SUMMARY listed three attack routes for `Mj-c-uniform-conjecture` (`checked-sober`) → `proved`. Day 90 wake dispatched sub-agents on all three simultaneously. All three came back NEGATIVE.

M_j c-uniformity is genuine — empirically 482/482 at c=5 (Day 85), matches Clio's H_c at c=6,7,8,9 (Day 87-89). But it is NOT because of the three "obvious" structural bridges. Elementary route via LB_k^{(c)} closed form is now the primary attack.

## Route (i) Kannan-Song 2509.18298 Λ^[2] plethystic action — CLOSED NEGATIVE

Paper is graph-enumeration for M̄_{g,n}. Thm 3.19 gives Λ^[2] × Λ̂ → Λ̂ action via
    `p_n(µ) ~∘ f = ψ_n(∂^µ f)`
(Adams operation composed with Macdonald skewing). This is NOT the wreath-Frobenius map Λ(S_2) ≅ Λ ⊗ Λ that BW uses. The two are structurally distinct maps on related-but-different algebras — no compatibility, no shortcut.

See `connections/kannan-song-lambda2-not-a-shortcut.md` for the full analysis.

## Route (ii) Motzkin K-triangle single-family identification — FALSIFIED

Conjecture: `K_{μ^T, (2^j)} = m^(2)_{k,j}` for some clean single-family rule μ = μ(k, j).

Sub-agent tested μ ∈ {(j+k, j-k), conj(j+k,j-k), (2^((j+k)/2), 1^(j-k)), ((j+k)/2, (j-k)/2), (j+k, 1^(j-k))} — all fail 21-27 / 28 test cases.

NO single-partition family works because the codomain {K_{μ^T,(2^j)} : μ ⊢ 2j} is too sparse; values like m^(2)_{2,3} = 5, m^(2)_{4,4} = 4, ... are never attained by any single K_{μ^T,(2^j)}.

He-Tubbenhauer β_{j,k} formula from SUMMARY is non-integer as written; agent used the standard Motzkin triangle recurrence instead. Row sums = Motzkin numbers ✓.

Script/output: `code/2026-07-12-motzkin-kostka-check.py`, `code/2026-07-12-motzkin-kostka-output.txt`.

## Route (iii) Bechtloff Weising 2506.07727 Cor 3.19 plethystic hunt — FALSIFIED

Search: for n = 2..7 and 0 ≤ 2j ≤ n, enumerate all partition pairs (α, β) with |α|, |β| ≤ 6 and compute deg-n component of s_α[S_+] · s_β[S_-] where S_+ = Σ h_{2k}, S_- = Σ h_{2k+1}. Compare to e_2^j · p_1^{n-2j}.

Only match: n=2, j=1 (degree-2 artefact — S_- truncates to p_1 so s_{(1,1)}[S_-] = e_2 at degree 2). No pattern extends. Even scalar multiples don't match.

**Verdict:** e_2^j · p_1^{n-2j} is NOT in the image of {s_α[S_+] · s_β[S_-]}.

This closes the highest-priority route since Day 87. See `BW-reciprocity-vs-Mj.md`, `free-vs-plethystic-power-obstructs-BW.md`.

Scripts: `code/2026-07-12-bechtloff-plethystic-hunt.py`, `-diagnostic.py`, `-wider-search.py`.

## Salvage angles considered

(a) **Linear combinations** Σ c_{αβ} s_α[S_+] · s_β[S_-] — but then "c-uniform by construction" no longer follows; each summand needs its own c-uniformity. Loses the point.

(b) **Different target** (e.g., s_λ itself) — but {s_λ} is a basis so any equality forces trivial identification. Nothing gained.

(c) **Plethystic substitution of target** — untested but structurally weak.

None promising.

## Structural conclusion

M_j c-uniformity is genuine (empirical evidence strong) but NOT reducible to any of the three known wreath / plethystic mechanisms. Two possibilities:

(a) It's a NEW structural mechanism we haven't identified yet, OR
(b) It's an artefact of the Sym-side identity `p_1^n = Σ_λ f^λ s_λ` (see `free-vs-plethystic-power-obstructs-BW.md`), meaning c-uniformity is "just" a consequence of the Sym-function tautology and NOT a categorification/wreath fact.

Cf. `Mj-as-sym-function-multiplicity.md`, `three-communities-at-sl2-plethysm.md`, `gutierrez-plethystic-vs-Mj.md`, `sharp-cancellation-single-carrier.md`.

## The pivot: elementary LB_k^{(c)} route

Rick's Day-90 structural insight (see PROVE.md): for k ≤ c-1 (clean regime),
    h_k^{(c)}(a, b) = (a+3)_{c-1-k} · (b+2)_{c-1-k} · Q_k(a, b, c)
and by Kummer/Legendre:
    LB_k^{(c)} = 2 · v_2((c-1-k)!) + Δ_k^{(c)}
where Δ_k^{(c)} = min v_2(Q_k(a, b, c)) over Poch-min-achieving (a, b) in shell.

Verified c=5, k=2 (Δ = 1) and c=9, k=2 (Δ = 1). If Δ_k^{(c)} has a c-uniform closed form (candidate: Δ_k^{(c)} = v_2 of some c-independent polynomial in a small basis of "Q_k mod 2" invariants), then LB_k does, and β'(c) = min_k LB_k^{(c)} does.

This proves SCP `proved uniformly` AND D1 `proved` without needing M_j promotion.

## Registry impact

- `Mj-c-uniform-conjecture` STAYS `checked-sober`.
- Three attack routes CLOSED as attack angles today (not the conjecture itself).
- NEW primary target: LB_k^{(c)} elementary route via SCP.

## Calibration rule addition

**Three-parallel-routes-negative rule:** when a high-value conjecture has three plausible attack angles that ALL fail on serious testing, look for an elementary route THAT AVOIDS THE PROMOTION rather than pushing harder on the categorification. Sometimes the theorem you actually need is smaller than the theorem you were chasing.

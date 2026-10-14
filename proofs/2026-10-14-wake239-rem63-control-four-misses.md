# Wake 239 — Clio UID 388: "the 4 misses in your Rem 6.3 replacement control (213/217)"

## 0. Attribution: the control is not a Rem 6.3 control

The 213/217 does not come from Rem 6.3. It is the **Thm 4.5 (block multiplicativity, FPSAC numbering) wrong-order replacement
control** in `scripts/day233b/s2d.py` (log `scripts/day233b/s2d.log`). It is recorded in
`proofs/2026-10-12-day237-section6-print-gaps.md` §(d), lines 157–159.

The 10-13 email to Clio (sent/20261013_002351) has the subject "Rem 6.3/6.4 now print-checked; your Thm 4.4/4.5 control flag
measured". It put both topics in one paragraph, which is probably where the conflation came from. The Rem 6.3 controls
(`work-in-progress/scripts/day237/rem63_bridge_check{,_n4pts}.{py,log}`) all broke as intended: 74 PASS symbolic plus 51/51 at
three points, 0 FAIL. Rem 6.3 has no 213/217.

## 1. What the control is

Thm 4.5 says: [(s−1)^{ℓ(λ)−κ}] c_{λμ} = Σ over set partitions π of the parts of λ into κ blocks, and over sub-partition assignments
ν_C ⊢ |λ_C|, of ∏_C [(s−1)^{|C|−1}] c_{λ_C,ν_C}.

The replacement control uses [(s−1)^{|C|}] in place of [(s−1)^{|C|−1}] in every factor. It is **supposed to break**, so a "4 ok"
means the wrong formula happens to agree in 4 cases. These 4 are not failures of the theorem. Thm 4.5 itself is 217/217.
The control is a mod-p check (p is the engine prime) at the single random point t0 = 750776399.

## 2. The 4 cases (rerun 2026-10-14; s2d.log reproduced)

All 4 have κ = 1 and ℓ(λ) = 2. So π = {one block of size 2}, and the comparison reduces to [ε^1] c vs [ε^2] c with ε = s − 1:

| λ | μ | [ε^1] = [ε^2] at t0 (mod p) | exact c_{λμ}(s,t) |
|---|---|---|---|
| (2,2) | (3,1) | 322965389 | −[2]_t · s(s−1) |
| (3,2) | (4,1) | 749081804 | −[3]_t · s(s−1) |
| (4,2) | (5,1) | 329163022 | −[4]_t · s(s−1) |
| (5,2) | (6,1) | 914833229 | −[5]_t · s(s−1) |

The closed form was checked at t = 3, 5, 7 and a random t. The ε-series is exactly (0, A, A, 0, 0, …) with A = −[a]_t, e.g.
−13 = −(1+3+9) for a = 3 at t = 3. The case (6,2)→(7,1) follows the same pattern (−[6]_t s(s−1)). It lies outside the n ≤ 7 range,
which is the only reason it is not a fifth miss.

## 3. Why they coincide (structural, not numerical luck)

- In all four, c_{λμ} is a **pure monomial in s up to a t-factor**: c = A(t) · s^{n(μ)} (s−1)^{v}.
  - n(μ) is the s-adic valuation (Thm DS).
  - v = ℓ(λ) − κ is the (s−1)-valuation (s=1 law).
  - Here the s-degree equals n(μ) + v, so nothing else survives.
- For such c, [ε^{v+1}] c / [ε^v] c = n(μ), because s^{n(μ)} = (1+ε)^{n(μ)}. The wrong-order control is therefore blind exactly when
  **n(μ) = 1** (μ = (m,1)) **and c is pure**, given κ = 1 so the single factor is c itself.
- Contrast cases from the same rerun, where the control fires:
  - (2,1)→(3): pure, n(μ) = 0, series (0, A, 0).
  - (3,3)→(4,2) and (4,3)→(5,2): pure, n(μ) = 2, series A·(0, 1, 2, 1).
  - (2,2)→(4) and (3,2)→(5): not pure.
- All 4 misses have κ = 1. In those cases Thm 4.5 is a tautology (one block, factor = lhs), as Day 237 already noted (56 of the
  217 cases). So on the **161 substantive (κ ≥ 2) cases the replacement control fires 161/161**. The weakness is confined to the
  tautological stratum, where no control can test the theorem anyway.

## 4. Printed claims

- No change is needed.
  - longversion.tex does not print this control or any 213/217/161 count (grep confirms).
  - Thm 4.5 itself passes 217/217.
  - Rem 6.3 and its controls are unaffected.
- Optional improvement for the internal record only: report the replacement control as 161/161 on κ ≥ 2 plus 52/56 on κ = 1.
  The 4 blind cases are explained by n(μ) = 1 purity.
- Suggested reply to Clio: correct the attribution (Thm 4.5 wrong-order control, not Rem 6.3), give the table above, and state that
  the misses are the n(μ) = 1 pure κ = 1 family. Nothing has been sent.

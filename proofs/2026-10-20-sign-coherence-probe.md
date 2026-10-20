# Sign-coherence probe of the "zero window = C_n wall strip" hunch

Wake 248 compute probe, 2026-10-20. **Grade: computed.** **Verdict: DIES** under the natural precise version, and
under every weakening I tried short of vacuity.
Hunch: `memory/connections/2026-10-19-zero-window-is-a-cn-wall-crossing-strip.md`.
Scripts: `work-in-progress/scripts/wake248/`.

## 0. Making the hunch precise

The hunch says to take "R / Weyl denominator" and check (i) that it is Laurent and (ii) that it is one-signed. That
assumes R behaves like a Weyl *numerator*. It does not.
- In Lemma Δ, K_n ∝ 1/Π_{i<j}(w_j−w_i)(w_iw_j−1): see the proof, where ℓ(e_L) = monomial·V(y^L)/Π(…). So
  C(∅,∅,[n];c) is already numerator/denominator, i.e. character-shaped.
- The exact A-residues are genuine rational functions with root-hyperplane poles. Example:
  R^A(∅,∅,[4];1,2;5) = −w1³w3³w4⁴ / [(w1²−1)²(w1−w3)(w1−w4)(w3+1)(w4+1)(w1w3−1)(w1w4−1)].
- Dividing by a further Weyl denominator therefore makes no sense.

Statement tested:
- **(P1\*), main.** Write R^A = Num/Den in lowest terms over ℚ[w] (variables w_j, j ≠ b, where w_b = 1/w_a).
  - Den was checked in every case to be a product of C-root factors: w_i, w_i±1, w_i−w_j, w_iw_j−1.
  - Strip every C-root factor from Num, leaving Num = monomial·Π(root factors)^e·P.
  - R is *sign-coherent* iff all coefficients of P have one sign.
  - Re-orienting root factors flips only a global sign, so P1\* is well defined.
- **Hunch claim.** Every allowed nonzero R is P1\*-coherent for c > 2N−4, and also for c ≤ −1 (with the opposite sign).
  Inside [0,2N−4] some must fail.
- **Weakenings also checked.**
  - Robust: P takes both signs on the positive orthant (300 rational points).
  - Twisted: P(s·w) is one-signed for some sign vector s ∈ {±1}^{N−1}, either per case or uniformly.
  - The raw unstripped Num (P1) is also recorded. It fails massively, because numerators carry root factors, which is
    why stripping is needed.

## 1. Tables (all allowed A-cases; exact over ℚ(w) via python-flint)

N = 3 (25 allowed; window {2}):

| c | −2 | −1 | 0 | 1 | 2 | 3..8 |
|---|---|---|---|---|---|---|
| coherent / incoherent / zero | 25/0/0 | 25/0/0 | 25/0/0 | 25/0/0 | 22/0/3 | 25/0/0 each |

N = 4 (408 allowed; window [0,4]):

| c | −2 | −1 | 0 | 1 | 2 | 3 | 4 | **5** | **6** | **7** | **8** |
|---|---|---|---|---|---|---|---|---|---|---|---|
| coherent | 292 | 293 | 316 | 333 | 298 | 301 | 289 | 298 | 292 | 292 | 292 |
| incoherent | 116 | 115 | 91 | 72 | 58 | 101 | 107 | **110** | **116** | **116** | **116** |
| zero | 0 | 0 | 1 | 3 | 52 | 6 | 12 | 0 | 0 | 0 | 0 |

- Every incoherent case is *robustly* incoherent: P changes sign on w > 0.
- About half are repaired by some sign twist (c = 6: 53 of 116). No single uniform twist works at any c.
- 106 of the 116 incoherent cases at c = 6, 8 have λ, μ ∈ G. That is exactly the class where Theorem U_G already
  *proves* nonvanishing.
- Zero counts reproduce `prove247/n4.txt` (1, 3, 52, 6, 12, 0 at c = 0..5).
- The exact engine matches `prove247/mp.py` mod p on 5 spot cases (`xchk.py`).
- c = 9, 10 and N = 5 (c ∈ {6,..,9}) were **not run**. The exact engine needed more than 8 minutes for a single N = 5
  case, so I aborted it. It is not needed for the kill.

**Explicit witness (beyond the last wall).** R^A(∅,∅,{1,3,4}; 1,2; c=6) has
- Den = (w1²−1)²(w1−w3)(w1−w4)(w1w3−1)(w1w4−1);
- Num = −w1³w4·P with P = w1(w3+w4)(w3²+w4²+1) − w3w4(w3²+w3w4+w4²+1), which is irreducible.

At (w3,w4) = (2,3), P(6/5) = −36 and P(19/10) = +13. Both points lie in the *same* Weyl chamber
1 < w1 < w3 < w4, w1w3 > 1. So R changes sign inside one chamber, and even "one sign per chamber" evaluation
coherence fails. The same triple is incoherent at every c ∈ {−2,−1,3,4,5,6,7,8} and coherent at 0, 1 (zero at 2).

## 2. Negative control

The known zero (∅,{3},{1,2,4}) H12 at c = 0 is classified **zero**. No zero residue was ever called coherent, so
the test is sound in that sense. But it **does not separate**:
- that same triple is P1\*-coherent at every other c, inside the window (1..4) as well as outside;
- inside the window, 289–333 nonzero cases per c are coherent;
- outside it there are 110–116 incoherent cases per c, the same order as inside.

At N = 3 everything is coherent everywhere, which is vacuous. Coherence is uncorrelated with the window.

## 3. Verdict

**DIES (computed, N = 4).** The kill condition fires: there are mixed-sign stripped quotients at c = 5..8 > 2N−4, and the
symmetric c ≤ −1 prediction fails too (115–116 incoherent cases). The hunch's escape clause, "unless a sum of two
sign-coherent blocks", is vacuous: every polynomial is its positive part plus its negative part, so the clause
cannot rescue anything.

The Weyl-wall reading survives only as the *literal* statement for κ = [n] (Lemma Δ). Upper-end nonvanishing
for the non-G triples remains with the certifier / block-sum route (gap 1).
- Tomorrow's PROVE should not target positivity.
- The possible salvage is a *twisted* coherence, which repairs about 50%, case-dependently. It looks like the same
  "block sum" phenomenon in disguise and is not recommended.

## 4. Scripts (`work-in-progress/scripts/wake248/`)
- `ff.py`, `eng.py`: exact Q(w) engine. The logic is copied from `prove247/sy.py`; the field is now flint fmpq_mpoly
  with gcd-reduced fractions.
- `cen.py`: census, writing `cohN_c*.txt` and `log4_*.txt`.
- `post.py`: robust test and per-triple tracks.
- `post2.py`: sign twists.
- `show.py`: factored forms.
- `xchk.py`: cross-check against the mod-p engine.
- `n5s.py`: N = 5 spot sample, aborted for time.
- `cen_core.py`: the analyse() function as a module.

# Day 97 Task C — Novelty audit for (♣) formula

**Formula (♣):** β(c) − LB_1(c) = s_2(c-1) + v_2(c-1) − v_2(c)

where β(c) = 2(c-1) − s_2(c-1) is the naïve k=1 Kummer-floor bound and
LB_1(c) is the actual Δ_1-based lower bound from Day 93 catalog. The
question: does (♣) or any obvious rearrangement of it appear in the
p-adic-valuation literature?

## Method

Downloaded and grepped the following three papers:

- **arXiv:0707.2119** — Amdeberhan-Manna-Moll, *The 2-adic valuation of a
  sequence arising from a rational integral*.
- **arXiv:2505.08935** — Alekseyev-Amdeberhan-Shallit-Vukusic, *On the
  p-adic valuations of values of Legendre polynomials*.
- **arXiv:2603.11069** — Iverson, *On the 3-adic valuation of a cubic
  binomial sum*.

Searched for: `s_2(n-1)+v_2(n-1)`, `s_2(n)-v_2(n+1)`, `β(c)`,
`LB`, `Kummer floor`, `Legendre digit sum`, `s2`, `v2`, `ν2`,
`digit sum`, and various rearrangements. Also read intros and main
theorems of each paper.

## Paper-by-paper verdict

### arXiv:0707.2119 (Amdeberhan-Manna-Moll)

Subject: 2-adic valuation of A_{l,m} = (l! m! / 2^{m-l}) · Σ_{k=l}^m 2^k
· C(2m-2k, m-k) · C(m+k, m) · C(k, l), arising from ∫ dx/(x^4 + 4ax^2 + 1)^{m+1}.

Uses `s_2` in Cor. 5.6 (`Ω(l)` has cardinality s_2(l)), Eq. (5.8) is a
sum over Kummer-floor differences ν_2(M_{k_i} − ⌊l/2^{1+k_i}⌋), and
Eq. (5.11) (De Wannemacker) is ν_2(S(n,k)) ≥ s_2(k) − s_2(n) for
Stirling numbers of the second kind.

None of these match (♣). The closest structural analogue is Eq. (5.8),
which decomposes a valuation as `2l + ν_2(l!) + [Kummer-floor tail]`.
Our LB_1(c) = 2·v_2((c-1)!) + Δ_1 has a similar 2·v_2 structure, but the
`s_2(c-1) + v_2(c-1) − v_2(c)` combination is not present. **No match.**

### arXiv:2505.08935 (Alekseyev-Amdeberhan-Shallit-Vukusic)

Subject: p-adic valuation of Legendre polynomials P_n(p). Main theorem
gives ν_p(P_n(p)) in closed form using s_p and v_p((n-k)!) via Legendre.

Uses Legendre's formula (Eq. (2): v_p(n!) = (n − s_p(n))/(p−1)) and
Kummer's theorem for binomial valuations. Key equation used:
ν_2(C(2m, m)) = 2s_2(m) − s_2(2m) = s_2(2m) = 2m − v_2((2m)!).

This is Kummer for the central binomial, i.e. a `2s_2 − s_2` combination.
Different from (♣)'s `s_2(c-1) + v_2(c-1) − v_2(c)` combination.
**No match.**

### arXiv:2603.11069 (Iverson)

Subject: 3-adic valuation of Σ_{r=0}^n C(n,r)^3 · 2^r, proving a
conjecture of Alekseyev-Amdeberhan-Shallit-Vukusic. Theorem 1 gives
ν_3(S_n) as a piecewise function of parity of n and s_3(⌊n/2⌋).

Uses `s_3` (base-3 digit sum) and Legendre's formula throughout. Not
about 2-adic valuations; the digit-sum + valuation combination in (♣)
does not appear. **No match.**

## Verdict

**No match after ~30 min of grep and inspection.**

The specific identity β(c) − LB_1(c) = s_2(c-1) + v_2(c-1) − v_2(c) —
or equivalently LB_1(c) = 2·v_2((c-1)!) − v_2(c-1) + v_2(c) — does
not appear in these three papers. The building blocks (Legendre's
formula v_p(n!) = (n − s_p(n))/(p-1), Kummer's carry theorem) are
classical, but the combination `s_2(c-1) + v_2(c-1) − v_2(c)` is not
one of the standard identities that pop up in the literature I searched.

**Registry action:** annotate `beta-LB1-universal-identity` with tag
`novelty-unaudited-open` (was: `novelty-unaudited-until-verified`).
Queue browse cycle to check:
- Additional Amdeberhan/Boros/Moll papers on 2-adic valuations of
  hypergeometric-like sequences (Byrnes-Moll-Reyes, Sun-Moll, etc.).
- The De Wannemacker line of work on Stirling number valuations.
- Anything citing arXiv:0707.2119 with a similar `s_2 + v_2 - v_2`
  structural identity.

If the identity remains unfound after one more browse cycle, upgrade
the novelty flag to `novelty-original-pending-audit`.

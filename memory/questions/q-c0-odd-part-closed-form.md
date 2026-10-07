---
name: [CLOSED Day 106] Closed form for odd part of c_0 = Q_{2R}(R-2, R, R)
description: Day 105 hunch H4. CLOSED Day 106 by H5′′ = triple-factorial identity c_0(R) = (-1)^R R!(R+1)!(2R)!. Legendre applied to the three factorials gives v_p(c_0) for every prime p at once. Day 107 (★) makes this an immediate corollary of a stronger polynomial identity.
type: project
---

# [CLOSED] Odd-part closed form for c_0

## Resolution (Day 106 wake)

H5′′ (Day 106) gives the FULL closed form:
```
    c_0(R) = Q_{2R}(R-2, R, R) = (-1)^R · R! · (R+1)! · (2R)!
```

For each prime p, apply Legendre's formula:
```
    v_p(c_0(R)) = v_p(R!) + v_p((R+1)!) + v_p((2R)!)
                = (R − s_p(R))/(p−1) + (R+1 − s_p(R+1))/(p−1) + (2R − s_p(2R))/(p−1)
```

This gives ALL prime valuations of c_0 at once. The Day 105 "doubling
pattern" hunch (H4) was correct AT THE DATA POINTS R = 4, 10 because both
happened to fall into the Legendre-pattern regime, but the underlying
mechanism is factorial, not iterated Pochhammer.

## Day 107 upgrade

The stronger Day 107 result (★) `Q_{2R}(a, b, R) = (-1)^R (2R)! · A_R(a) B_R(b)`
subsumes H5′′ as the (a, b) = (R−2, R) special case. So the odd-part closed
form is a corollary of a corollary now.

## What H4 got right

H4 correctly predicted:
- Prime support = {odd primes ≤ 2R − 1}. Correct — Legendre confirms this.
- Exponent decreasing with prime index. Correct — Legendre gives roughly
  $v_p \sim (4R + 1) / (p - 1)$ modulo digit-sum corrections.
- Doubling pattern at consecutive primes for specific R. Correct at R = 4, 10
  but coincidental — the actual mechanism is more delicate.

## What H4 got wrong

- The "iterated Pochhammer" structural intuition. Actual mechanism: three
  factorials from three-row wall reduction.

## Files

- `connections/H5-doubleprime-c0-triple-factorial.md` — the resolution.
- `connections/Q-closed-form-at-c-R.md` — the Day 107 upgrade.
- `proofs/2026-08-14-H5doubleprime-proof-day107.md` — Day 107 proof memo.

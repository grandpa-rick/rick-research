# Day 130 — Top-weight expansions of Ψ(e_2^b), closed forms

## Full coefficient table (top-weight part, E-basis)

For each b, we list ALL monomials E1^{a1} E2^{a2} E3^{a3} with a1 + a2 + 2 a3 = b,
i.e. all monomials of maximal (1,1,2)-weight = b.

| b | (a1,a2,a3) | coeff |
|---|-----------|------:|
| 2 | (2,0,0) |    2 |
| 2 | (1,1,0) |   -3 |
| 2 | (0,2,0) |    1 |
| 2 | (0,0,1) |   -3 |
| 3 | (3,0,0) |   -6 |
| 3 | (2,1,0) |   11 |
| 3 | (1,2,0) |   -6 |
| 3 | (0,3,0) |    1 |
| 3 | (1,0,1) |   25 |
| 3 | (0,1,1) |   -9 |
| 4 | (4,0,0) |   24 |
| 4 | (3,1,0) |  -50 |
| 4 | (2,2,0) |   35 |
| 4 | (1,3,0) |  -10 |
| 4 | (0,4,0) |    1 |
| 4 | (2,0,1) | -190 |
| 4 | (1,1,1) |  118 |
| 4 | (0,2,1) |  -18 |
| 4 | (0,0,2) |   27 |
| 5 | (5,0,0) | -120 |
| 5 | (4,1,0) |  274 |
| 5 | (3,2,0) | -225 |
| 5 | (2,3,0) |   85 |
| 5 | (1,4,0) |  -15 |
| 5 | (0,5,0) |    1 |
| 5 | (3,0,1) | 1526 |
| 5 | (2,1,1) |-1260 |
| 5 | (1,2,1) |  340 |
| 5 | (0,3,1) |  -30 |
| 5 | (1,0,2) | -615 |
| 5 | (0,1,2) |  135 |
| 6 | (6,0,0) |  720 |
| 6 | (5,1,0) |-1764 |
| 6 | (4,2,0) | 1624 |
| 6 | (3,3,0) | -735 |
| 6 | (2,4,0) |  175 |
| 6 | (1,5,0) |  -21 |
| 6 | (0,6,0) |    1 |
| 6 | (4,0,1) |-13356|
| 6 | (3,1,1) |13276 |
| 6 | (2,2,1) |-4845 |
| 6 | (1,3,1) |  770 |
| 6 | (0,4,1) |  -45 |
| 6 | (2,0,2) |10300 |
| 6 | (1,1,2) |-4095 |
| 6 | (0,2,2) |  405 |
| 6 | (0,0,3) | -405 |

All top-weight monomials are nonzero.

## Closed forms

### k=0 slice (a3=0)

Coefficient of E1^{b-j} E2^j (0 ≤ j ≤ b) equals s(b+1, j+1),
the signed Stirling number of the first kind.

Equivalent product form:
  P_b(E1, E2, 0) = ∏_{r=1}^b (E2 − r E1).

### Stirling formula for E1^{b-1} E2

Coefficient of E1^{b-1} E2 in Ψ(e_2^b)|_top is (-1)^{b-1} · c(b+1, 2)
                                              = (-1)^{b-1} · b! · H_b
where H_b = 1 + 1/2 + ... + 1/b is the harmonic number.
Verified for b=2..6: -3, 11, -50, 274, -1764.

### Pure-E3 slice (E1=E2=0)

Coefficient of E3^{b/2} (b even) in Ψ(e_2^b)|_top is
  (-1)^{b/2} · 3^{b/2} · (b-1)!!.
Odd b gives 0 there.

### E2 E3^j slice (b odd)

For b = 2j+1, coefficient of E2 E3^j is (-1)^j · 3^j · (2j+1)!!.

## The EGF FACTORIZES completely (verified through T^6)

Define the EGF:
  F(T) = Σ_{b≥0} Ψ(e_2^b)|_top · T^b / b!

Then
```
F(T) = (1 + T·E1)^{E2/E1 - 1}
     · exp( E3 · [ T / (E1 · (1 + E1 T)^2)  -  log(1 + E1 T)/E1^2 ] )
```

Equivalently, with y = E1·T:
```
F(T) = (1+y)^{E2/E1 - 1} · exp( (E3/E1^2) · [ y/(1+y)^2 - log(1+y) ] )
```

Verified: expanding this in T through T^6 reproduces P_b for b = 0, 1, 2, 3, 4, 5, 6.

### The log-linearity in E3

Because F factors as A(T)·exp(E3·M(T,E1)) with M independent of E2, we have
log( F(T) / (1+T·E1)^{E2/E1-1} ) is *linear* in E3 and independent of E2.
Its Taylor coefficients are exactly:

  [T^n] log G = (-1)^{n-1} · (n^2 − 1)/n · E1^{n-2} · E3     for n ≥ 2

(so no E3^2, E2, E3·E2 terms appear in log G — every higher power of E3
that appears in F comes from exponentiation).

## OGF

The OGF Σ_b P_b T^b has coefficient (−1)^b · b! · E1^b already at
the pure-E1 slice, i.e. Σ_b (−1)^b b! (E1 T)^b, which has zero radius
of convergence and no rational closed form. The OGF does NOT factor
nicely; the EGF is the right generating function.

## Files

- `analyze.py` — Recomputes P_b, dumps table, checks Stirling patterns.
- `factorize.py` — Extracts G(T) = F(T) / (1+T·E1)^{E2/E1-1}.
- `factorize2.py` — Takes log to find the E3-linear structure.
- `verify_egf.py`, `verify_egf2.py` — Derive and verify the closed form.
- `coefficients_table.txt` — Machine-readable coefficient table.
- `log_G_expansion.txt` — log G(T) truncated.
- `G_expansion.txt` — G(T) truncated.

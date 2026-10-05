#!/usr/bin/env python3
"""
Day 186 — Free-cumulant test for Rick's b_k series.

Question: Do the Speicher-Nica free cumulants of B(t) = 1+3t+27t^2+417t^3+7851t^4+164124t^5
coincide with a_k = INVERTi(b_k) = (3, 18, 282, 5268, 109647)?
"""
import sympy as sp

t = sp.symbols('t')
N = 6  # truncate at t^N (compute k up to N-1)

# ------------------------------------------------------------------
# 1. Rick's b_k and INVERTi -> a_k
# ------------------------------------------------------------------
b = [1, 3, 27, 417, 7851, 164124]  # b_0 .. b_5
B = sum(b[k] * t**k for k in range(N))

# a_k defined by B(t) = 1 / (1 - A(t)), so A(t) = 1 - 1/B(t)
one_over_B = sp.series(1 / B, t, 0, N).removeO()
A_series = sp.expand(1 - one_over_B)
a = [sp.Poly(A_series, t).coeff_monomial(t**k) for k in range(N)]

print("=" * 60)
print("Rick's sequences:")
print("=" * 60)
print(f"  b_k (k=0..5): {b}")
print(f"  a_k = INVERTi(b_k), k=1..5: {[a[k] for k in range(1, N)]}")
print()

# Sanity check against stated a_k
a_expected = [3, 18, 282, 5268, 109647]
a_computed = [a[k] for k in range(1, N)]
assert a_computed == a_expected, f"INVERTi mismatch: {a_computed} vs {a_expected}"
print("  [OK] INVERTi(b) matches (3, 18, 282, 5268, 109647).")
print()

# ------------------------------------------------------------------
# 2. Free cumulants of M(t) = B(t) via K(t*M(t)) = M(t)
# ------------------------------------------------------------------
# K(u) = 1 + k1 u + k2 u^2 + k3 u^3 + k4 u^4 + k5 u^5.
# Substitute u = t*M(t) and match coefficients.
print("=" * 60)
print("Candidate A: free cumulants of M(t) = B(t)")
print("=" * 60)

ks = sp.symbols('k1 k2 k3 k4 k5')
K_of_u = 1 + sum(ks[i] * sp.Symbol('u')**(i+1) for i in range(5))
u = t * B
K_sub = K_of_u.subs(sp.Symbol('u'), u)
K_series = sp.series(K_sub, t, 0, N).removeO()
K_poly = sp.expand(K_series)

# Match coefficient of t^k in K_series to b_k, solve sequentially.
free_cum = {}
for k in range(1, N):
    coeff_K = sp.Poly(K_poly, t).coeff_monomial(t**k)
    eqn = sp.Eq(coeff_K, b[k])
    sol = sp.solve(eqn, ks[k-1])
    assert len(sol) == 1
    free_cum[ks[k-1]] = sol[0]
    K_poly = sp.expand(K_poly.subs(ks[k-1], sol[0]))

kappa = [free_cum[ks[i]] for i in range(5)]
print(f"  kappa_1..kappa_5 (free cumulants of B): {kappa}")
print()

# ------------------------------------------------------------------
# 3. Log-coefficients of B(t): log B(t) = sum c_k t^k
# ------------------------------------------------------------------
print("=" * 60)
print("Log-coefficients: log B(t) = sum c_k t^k")
print("=" * 60)
logB = sp.series(sp.log(B), t, 0, N).removeO()
logB = sp.expand(logB)
c = [sp.Poly(logB, t).coeff_monomial(t**k) for k in range(1, N)]
print(f"  c_1..c_5 = {c}")
print()

# ------------------------------------------------------------------
# 4. Comparison table
# ------------------------------------------------------------------
print("=" * 60)
print("Comparison table")
print("=" * 60)
print(f"{'k':>3} | {'b_k':>10} | {'a_k=INVERTi':>12} | {'free_cum(B)':>14} | {'log_coeff(B)':>14}")
print("-" * 65)
for k in range(1, N):
    print(f"{k:>3} | {str(b[k]):>10} | {str(a[k]):>12} | {str(kappa[k-1]):>14} | {str(c[k-1]):>14}")
print()

# ------------------------------------------------------------------
# 5. Verdict
# ------------------------------------------------------------------
print("=" * 60)
print("Verdict")
print("=" * 60)
match = all(kappa[k-1] == a[k] for k in range(1, N))
if match:
    print("  YES: free_cum(B) == a_k = INVERTi(b_k).")
    print("  This upgrades q-geode-k-minus-1-and-bk to proved-numerical.")
else:
    print("  NO: free_cum(B) != a_k.")
    print(f"      free_cum(B) = {kappa}")
    print(f"      a_k         = {[a[k] for k in range(1, N)]}")
    print(f"      diff        = {[kappa[k-1] - a[k] for k in range(1, N)]}")

# ------------------------------------------------------------------
# 6. Bonus: what IS free_cum(B) as a sequence?  Try INVERT of kappa,
#    also try log, and see if kappa matches any obvious transform.
# ------------------------------------------------------------------
print()
print("=" * 60)
print("Diagnostics: what is free_cum(B)?")
print("=" * 60)

# INVERT of kappa: interpret kappa as A_new, form 1/(1-A_new), see coeffs
A_new = sum(kappa[k-1] * t**k for k in range(1, N))
invert_kappa = sp.series(1/(1 - A_new), t, 0, N).removeO()
invert_kappa = sp.expand(invert_kappa)
inv_seq = [sp.Poly(invert_kappa, t).coeff_monomial(t**k) for k in range(1, N)]
print(f"  INVERT(kappa)  = {inv_seq}")
print(f"  (compare b_k)  = {b[1:]}")

# INVERTi of kappa
K_as_moment = 1 + A_new
one_over_K = sp.series(1/K_as_moment, t, 0, N).removeO()
inverti_kappa_series = sp.expand(1 - one_over_K)
inverti_kappa = [sp.Poly(inverti_kappa_series, t).coeff_monomial(t**k) for k in range(1, N)]
print(f"  INVERTi(kappa) = {inverti_kappa}")

# Ratio kappa_k / a_k
print(f"  kappa_k / a_k  = {[sp.Rational(kappa[k-1], a[k]) for k in range(1, N)]}")

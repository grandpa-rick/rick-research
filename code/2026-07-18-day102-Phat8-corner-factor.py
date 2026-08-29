"""Day 102 — investigate P_hat_8(0, 0, m) and P_hat_7(0, 0, m) symbolically.

Day 101 empirical: v_2(P_hat_8(0, 0, m)) = 5 + 2·v_2(m-1) at (a,b)=(0,0).
Question: does P_hat_8(0, 0, m) factor as 32·(m-1)^2 · R(m) with R(m) odd
uniformly? If yes, UB8-strong closes structurally.
"""
import sympy as sp
from sympy import symbols, factor, expand, simplify

a_, b_, c_, m_ = symbols('a b c m')

# Copy from Day 101 file
S_8_bracket = (
    1680*a_**4*b_**4 - 3360*a_**4*b_**3 - 1680*a_**4*b_**2 + 3360*a_**4*b_ + 3360*a_**3*b_**4
    - 3360*a_**3*b_**3*c_**3 + 43680*a_**3*b_**3*c_**2 - 188160*a_**3*b_**3*c_ + 262080*a_**3*b_**3
    - 3360*a_**3*b_**2 + 3360*a_**3*b_*c_**3 - 43680*a_**3*b_*c_**2 + 188160*a_**3*b_*c_ - 262080*a_**3*b_
    - 1680*a_**2*b_**4 - 10080*a_**2*b_**3*c_**3 + 131040*a_**2*b_**3*c_**2 - 564480*a_**2*b_**3*c_ + 809760*a_**2*b_**3
    + 840*a_**2*b_**2*c_**6 - 22680*a_**2*b_**2*c_**5 + 252840*a_**2*b_**2*c_**4 - 1489320*a_**2*b_**2*c_**3 + 4887120*a_**2*b_**2*c_**2 - 8467200*a_**2*b_**2*c_ + 6049680*a_**2*b_**2
    + 840*a_**2*b_*c_**6 - 22680*a_**2*b_*c_**5 + 252840*a_**2*b_*c_**4 - 1479240*a_**2*b_*c_**3 + 4756080*a_**2*b_*c_**2 - 7902720*a_**2*b_*c_ + 5238240*a_**2*b_
    - 3360*a_*b_**4 - 6720*a_*b_**3*c_**3 + 87360*a_*b_**3*c_**2 - 376320*a_*b_**3*c_ + 544320*a_*b_**3
    + 2520*a_*b_**2*c_**6 - 68040*a_*b_**2*c_**5 + 758520*a_*b_**2*c_**4 - 4467960*a_*b_**2*c_**3 + 14661360*a_*b_**2*c_**2 - 25401600*a_*b_**2*c_ + 18147360*a_*b_**2
    - 56*a_*b_*c_**9 + 2352*a_*b_*c_**8 - 43344*a_*b_*c_**7 + 462168*a_*b_*c_**6 - 3156384*a_*b_*c_**5 + 14377608*a_*b_*c_**4 - 43826776*a_*b_*c_**3 + 86374512*a_*b_*c_**2 - 99859200*a_*b_*c_ + 51468480*a_*b_
    - 56*a_*c_**9 + 2352*a_*c_**8 - 43344*a_*c_**7 + 459648*a_*c_**6 - 3088344*a_*c_**5 + 13619088*a_*c_**4 - 39365536*a_*c_**3 + 71800512*a_*c_**2 - 74833920*a_*c_ + 33868800*a_
    + 1680*b_**2*c_**6 - 45360*b_**2*c_**5 + 505680*b_**2*c_**4 - 2978640*b_**2*c_**3 + 9774240*b_**2*c_**2 - 16934400*b_**2*c_ + 12096000*b_**2
    - 112*b_*c_**9 + 4704*b_*c_**8 - 86688*b_*c_**7 + 920976*b_*c_**6 - 6222048*b_*c_**5 + 27743856*b_*c_**4 - 81709712*b_*c_**3 + 153375264*b_*c_**2 - 166602240*b_*c_ + 79833600*b_
    + c_**12 - 58*c_**11 + 1517*c_**10 - 23742*c_**9 + 248487*c_**8 - 1838382*c_**7 + 9888647*c_**6 - 39061538*c_**5 + 112617892*c_**4 - 231115320*c_**3 + 319957056*c_**2 - 267442560*c_ + 101606400
)

S8_at_c = sp.expand(S_8_bracket.subs(c_, 4*m_ + 2))
P_hat_8 = sp.expand(S8_at_c / 16)

# Evaluate at (a, b) = (0, 0)
P8_00 = sp.expand(P_hat_8.subs({a_: 0, b_: 0}))
print("P_hat_8(0, 0, m) as poly in m:")
print(sp.Poly(P8_00, m_).as_expr())
print()

# Factor
print("Factored form:")
print(factor(P8_00))
print()

# Check divisibility by (m - 1)^2 and by 32
P8_over_32 = sp.expand(P8_00 / 32)
print("P_hat_8(0, 0, m) / 32:")
print(sp.Poly(P8_over_32, m_).as_expr())
print()

# Try dividing by (m - 1)^2
q1, r1 = sp.div(P8_00, (m_ - 1)**2, m_)
print(f"P_hat_8(0, 0, m) mod (m-1)^2: remainder = {r1}")
print(f"  quotient = {q1}")
q1_expanded = sp.expand(q1)
print(f"  quotient expanded: {q1_expanded}")
print()

# Try (m-1)^k for larger k
for k in [1, 2, 3, 4]:
    q, r = sp.div(P8_00, (m_ - 1)**k, m_)
    print(f"  P_8(0,0,m) mod (m-1)^{k}: rem = {sp.expand(r)}, quotient factored = {sp.factor(q)}")

print()
print("=" * 78)
print("Check: is P_hat_8(0, 0, m) = 32 · (m - 1)^2 · (odd polynomial in m)?")

quot = P8_00 / ((m_ - 1) ** 2)
quot_simp = sp.simplify(quot)
print(f"P_hat_8(0, 0, m) / (m - 1)^2 = {quot_simp}")
print(f"Poly form: {sp.Poly(sp.expand(quot_simp), m_).as_expr() if sp.expand(quot_simp).is_polynomial(m_) else 'NOT a polynomial'}")

# Numerical: for m = 3, 5, 7, ..., compute v_2 and compare 5 + 2 v_2(m-1)
print()
print("Numerical check: v_2(P_hat_8(0, 0, m)) vs 5 + 2·v_2(m-1) at m odd:")
Pfn = sp.lambdify(m_, P8_00, 'math')
def v2(n):
    if n == 0: return None
    v = 0
    while n % 2 == 0: n //= 2; v += 1
    return v
print(f"{'m':>4} | {'P8(0,0,m)':>15} | {'v_2':>4} | {'v_2(m-1)':>8} | {'expected':>8} | {'match':>5}")
for m in [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 25, 33, 49, 65, 129]:
    if m == 1:
        v = "inf" # (m-1) = 0 makes P8(0,0,1) = 0
        continue
    val = int(Pfn(m))
    v = v2(val) if val else None
    v_m_1 = v2(m - 1)
    expected = 5 + 2 * v_m_1 if v_m_1 is not None else "N/A"
    match = (v == expected)
    print(f"{m:>4} | {val:>15} | {str(v):>4} | {str(v_m_1):>8} | {str(expected):>8} | {str(match):>5}")

# Also m even
print()
print("m EVEN — check v_2(P8(0,0,m)):")
print(f"{'m':>4} | {'P8(0,0,m)':>15} | {'v_2':>4}")
for m in [2, 4, 6, 8, 10, 12, 14, 16, 20, 24, 32, 64]:
    val = int(Pfn(m))
    v = v2(val) if val else None
    print(f"{m:>4} | {val:>15} | {str(v):>4}")

# Now P_hat_7
print()
print("=" * 78)
print("P_hat_7(0, 0, m):")
S_7_bracket = (
    840*a_**3*b_**3 - 840*a_**3*b_ + 2520*a_**2*b_**3
    - 420*a_**2*b_**2*c_**3 + 5040*a_**2*b_**2*c_**2 - 19740*a_**2*b_**2*c_ + 25200*a_**2*b_**2
    - 420*a_**2*b_*c_**3 + 5040*a_**2*b_*c_**2 - 19740*a_**2*b_*c_ + 22680*a_**2*b_
    + 1680*a_*b_**3
    - 1260*a_*b_**2*c_**3 + 15120*a_*b_**2*c_**2 - 59220*a_*b_**2*c_ + 75600*a_*b_**2
    + 42*a_*b_*c_**6 - 1050*a_*b_*c_**5 + 10710*a_*b_*c_**4 - 58170*a_*b_*c_**3 + 180768*a_*b_*c_**2 - 308700*a_*b_*c_ + 225120*a_*b_
    + 42*a_*c_**6 - 1050*a_*c_**5 + 10710*a_*c_**4 - 56910*a_*c_**3 + 165648*a_*c_**2 - 249480*a_*c_ + 151200*a_
    - 840*b_**2*c_**3 + 10080*b_**2*c_**2 - 39480*b_**2*c_ + 50400*b_**2
    + 84*b_*c_**6 - 2100*b_*c_**5 + 21420*b_*c_**4 - 114660*b_*c_**3 + 341376*b_*c_**2 - 538440*b_*c_ + 352800*b_
    - c_**9 + 39*c_**8 - 660*c_**7 + 6426*c_**6 - 40089*c_**5 + 167811*c_**4 - 474410*c_**3 + 874044*c_**2 - 946440*c_ + 453600
)
S7_at_c = sp.expand(S_7_bracket.subs(c_, 4*m_ + 2))
P_hat_7 = sp.expand(S7_at_c / -8)
P7_00 = sp.expand(P_hat_7.subs({a_: 0, b_: 0}))
print(f"P_hat_7(0, 0, m) = {sp.Poly(P7_00, m_).as_expr()}")
print(f"Factored: {factor(P7_00)}")
for k in [1, 2, 3, 4]:
    q, r = sp.div(P7_00, (m_ - 1)**k, m_)
    print(f"  P_7(0,0,m) mod (m-1)^{k}: rem = {sp.expand(r)}, quotient factored = {sp.factor(q)}")

# Numerical
Pfn7 = sp.lambdify(m_, P7_00, 'math')
print()
print("Numerical P_hat_7(0, 0, m):")
print(f"{'m':>4} | {'P7(0,0,m)':>15} | {'v_2':>4} | {'v_2(m-1)':>8}")
for m in [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 17, 33, 65]:
    val = int(Pfn7(m))
    v = v2(val) if val else None
    v_m_1 = v2(m - 1) if m > 1 else None
    print(f"{m:>4} | {val:>15} | {str(v):>4} | {str(v_m_1):>8}")

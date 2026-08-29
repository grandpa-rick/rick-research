"""Day 101 — investigate v_2(P_hat_8).

k=8 empirical:
- m even: v_2(P_hat_8) min = 5, achieved at (0, 2j)
- m odd: v_2(P_hat_8) min = 6, achieved at (2, 4), (2, 6), (2, 12), etc.

Try to identify uniform lower bounds (mod-N identities).
"""
import sympy as sp
from sympy import symbols

a_, b_, c_, m_ = symbols('a b c m')

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
P_hat_8_poly = sp.Poly(P_hat_8, a_, b_, m_)
print("P_hat_8 leading coeffs (integer?):", all(sp.Rational(c).q == 1 for c in P_hat_8_poly.coeffs()))

# Check divisibility by 32 (i.e., v_2(P_hat_8) >= 5 unconditionally?)
Pfn = sp.lambdify([a_, b_, m_], P_hat_8, 'math')
print()
print("P_hat_8 mod 32 for (a mod 32, b mod 32, m mod 32):")
worst_mod = 0
worst_config = None
for am in range(16):
    for bm in range(16):
        for mm in range(16):
            val = int(Pfn(am, bm, mm)) % 32
            if val > worst_mod:
                worst_mod = val
                worst_config = (am, bm, mm)
print(f"  max val mod 32 over (a,b,m in [0,16)) = {worst_mod} at {worst_config}")
# If all zero mod 32, v_2 >= 5

# Try mod 64
print()
print("P_hat_8 mod 64 on FULL (a, b, m) in [0, 32)^3:")
allzero_64 = True
for am in range(32):
    for bm in range(32):
        for mm in range(32):
            val = int(Pfn(am, bm, mm)) % 64
            if val != 0:
                allzero_64 = False
                break
        if not allzero_64: break
    if not allzero_64: break
print(f"  {'YES' if allzero_64 else 'NO'}: P_hat_8 divisible by 64 uniformly")

def v2(n):
    if n == 0: return 10**9
    v = 0
    while n % 2 == 0: n //= 2; v += 1
    return v

# Min v_2(P_hat_8) over integer grid (not just shell)
print()
print("v_2(P_hat_8) statistics on integer grid [0, 40)^3:")
minv = 10**9
minconf = None
for am in range(0, 40):
    for bm in range(0, 40):
        for mm in range(1, 30):
            val = int(Pfn(am, bm, mm))
            if val == 0: continue
            v = v2(val)
            if v < minv:
                minv = v
                minconf = (am, bm, mm)
print(f"  Global min v_2(P_hat_8) = {minv} at {minconf}")

# Split by m parity
print()
print("v_2(P_hat_8) min by (a+b) parity and m parity:")
for shell_parity in ['EE', 'EO', 'OE', 'OO']:
    for m_parity in ['odd', 'even']:
        minv = 10**9
        minconf = None
        for am in range(0, 40):
            for bm in range(0, 40):
                if shell_parity[0] == 'E' and am % 2 != 0: continue
                if shell_parity[0] == 'O' and am % 2 != 1: continue
                if shell_parity[1] == 'E' and bm % 2 != 0: continue
                if shell_parity[1] == 'O' and bm % 2 != 1: continue
                for mm in range(1, 30):
                    if m_parity == 'odd' and mm % 2 == 0: continue
                    if m_parity == 'even' and mm % 2 == 1: continue
                    val = int(Pfn(am, bm, mm))
                    if val == 0: continue
                    v = v2(val)
                    if v < minv:
                        minv = v
                        minconf = (am, bm, mm)
        print(f"  parity {shell_parity} m {m_parity}: min v_2 = {minv} at {minconf}")

# Similarly analyze P_hat_7
print()
print("=" * 78)
print("P_hat_7 also (for completeness):")
print("=" * 78)
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
Pfn7 = sp.lambdify([a_, b_, m_], P_hat_7, 'math')

# Verify v_2(P_hat_7) >= 2 across a finer grid
allzero_4 = True
for am in range(0, 8):
    for bm in range(0, 8):
        for mm in range(0, 8):
            v = int(Pfn7(am, bm, mm)) % 4
            if v != 0:
                allzero_4 = False
print(f"  P_hat_7 divisible by 4 for (a, b, m) in [0, 8)^3: {allzero_4}")
# But is there a higher uniform bound?
allzero_8 = True
for am in range(0, 16):
    for bm in range(0, 16):
        for mm in range(0, 16):
            v = int(Pfn7(am, bm, mm)) % 8
            if v != 0:
                allzero_8 = False
                break
        if not allzero_8: break
    if not allzero_8: break
print(f"  P_hat_7 divisible by 8 for (a, b, m) in [0, 16)^3: {allzero_8}")

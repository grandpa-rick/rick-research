"""Day 101 — RIGOROUS verification of the uniform mod-N bounds:
- P_hat_7(a, b, m) ≡ 0 (mod 4) for ALL integer (a, b, m)
- P_hat_8(a, b, m) ≡ 0 (mod 32) for ALL integer (a, b, m)

Since P_hat_k are polynomials with integer coefficients, their values mod N
depend only on inputs mod N. So checking on (Z/NZ)^3 is a finite,
rigorous proof.

For P_hat_7 we need (Z/4Z)^3 = 64 evals.
For P_hat_8 we need (Z/32Z)^3 = 32768 evals.
"""
import sympy as sp
from sympy import symbols

a_, b_, c_, m_ = symbols('a b c m')

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

# Substitute c = 4m+2 and divide
S7_at_c = sp.expand(S_7_bracket.subs(c_, 4*m_ + 2))
P_hat_7 = sp.expand(S7_at_c / -8)
S8_at_c = sp.expand(S_8_bracket.subs(c_, 4*m_ + 2))
P_hat_8 = sp.expand(S8_at_c / 16)

# Verify integer coefficients
poly7 = sp.Poly(P_hat_7, a_, b_, m_)
poly8 = sp.Poly(P_hat_8, a_, b_, m_)
assert all(sp.Rational(c).q == 1 for c in poly7.coeffs())
assert all(sp.Rational(c).q == 1 for c in poly8.coeffs())
print("Both P_hat_7 and P_hat_8 have integer coefficients: OK")

# Rigorous mod-4 check for P_hat_7 on full (Z/4Z)^3 = 64 evaluations
Pfn7 = sp.lambdify([a_, b_, m_], P_hat_7, 'math')
Pfn8 = sp.lambdify([a_, b_, m_], P_hat_8, 'math')

print()
print("=" * 78)
print("RIGOROUS Lemma UB7: P_hat_7 ≡ 0 (mod 4) on (Z/4Z)^3 = 64 evaluations")
print("=" * 78)
fail7 = 0
for am in range(4):
    for bm in range(4):
        for mm in range(4):
            val = int(Pfn7(am, bm, mm)) % 4
            if val != 0:
                fail7 += 1
                print(f"  FAIL: (a,b,m) mod 4 = ({am},{bm},{mm}): P_hat_7 = {val} mod 4")
print(f"  Result: {'PASS - proved v_2(P_hat_7) >= 2 uniformly' if fail7 == 0 else f'{fail7} FAILS'}")

print()
print("=" * 78)
print("RIGOROUS Lemma UB8: P_hat_8 ≡ 0 (mod 32) on (Z/32Z)^3 = 32768 evaluations")
print("=" * 78)
fail8 = 0
for am in range(32):
    for bm in range(32):
        for mm in range(32):
            val = int(Pfn8(am, bm, mm)) % 32
            if val != 0:
                fail8 += 1
                if fail8 < 5:
                    print(f"  FAIL: (a,b,m) mod 32 = ({am},{bm},{mm}): P_hat_8 = {val} mod 32")
print(f"  Result: {'PASS - proved v_2(P_hat_8) >= 5 uniformly' if fail8 == 0 else f'{fail8} FAILS'}")

# Also, is P_hat_7 divisible by 8 conditionally on (a+b) even (shell)?
print()
print("=" * 78)
print("Bonus: Is P_hat_7 ≡ 0 (mod 8) on shell (a+b even)? Check (Z/8Z)^3, shell only.")
print("=" * 78)
fail_shell = 0
for am in range(8):
    for bm in range(8):
        if (am + bm) % 2: continue
        for mm in range(8):
            val = int(Pfn7(am, bm, mm)) % 8
            if val != 0:
                fail_shell += 1
                if fail_shell < 5:
                    print(f"  Shell FAIL: ({am},{bm},{mm}): P_hat_7 = {val} mod 8")
print(f"  Result: {'YES - v_2(P_hat_7) >= 3 on shell (uniformly)' if fail_shell == 0 else f'NO - {fail_shell} shell fails'}")

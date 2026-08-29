"""Day 101 BONUS — try to extract clean factorisations of P_hat_k for k = 7, 8.

Q_7 = c(c-4)(c-3)(c-2)(c-1) * S_7 (from catalog).
Q_8 = c(c-3)(c-2)(c-1) * S_8.

Extract S_k(a, b, 4m+2) and look for structure analogous to (S_4♠), (S_5♠), (S_6♠).
"""
import sympy as sp
from sympy import symbols, expand, factor, Poly

a, b, c, m, A, B = symbols('a b c m A B')

# From catalog (Day 100 Q_k extension):
# Q_7 = c*(c-4)*(c-3)*(c-2)*(c-1)*S_7, where S_7 is the bracket:
S_7_bracket = (
    840*a**3*b**3 - 840*a**3*b + 2520*a**2*b**3 - 420*a**2*b**2*c**3 + 5040*a**2*b**2*c**2 - 19740*a**2*b**2*c + 25200*a**2*b**2
    - 420*a**2*b*c**3 + 5040*a**2*b*c**2 - 19740*a**2*b*c + 22680*a**2*b + 1680*a*b**3
    - 1260*a*b**2*c**3 + 15120*a*b**2*c**2 - 59220*a*b**2*c + 75600*a*b**2
    + 42*a*b*c**6 - 1050*a*b*c**5 + 10710*a*b*c**4 - 58170*a*b*c**3 + 180768*a*b*c**2 - 308700*a*b*c + 225120*a*b
    + 42*a*c**6 - 1050*a*c**5 + 10710*a*c**4 - 56910*a*c**3 + 165648*a*c**2 - 249480*a*c + 151200*a
    - 840*b**2*c**3 + 10080*b**2*c**2 - 39480*b**2*c + 50400*b**2
    + 84*b*c**6 - 2100*b*c**5 + 21420*b*c**4 - 114660*b*c**3 + 341376*b*c**2 - 538440*b*c + 352800*b
    - c**9 + 39*c**8 - 660*c**7 + 6426*c**6 - 40089*c**5 + 167811*c**4 - 474410*c**3 + 874044*c**2 - 946440*c + 453600
)

S_8_bracket = (
    1680*a**4*b**4 - 3360*a**4*b**3 - 1680*a**4*b**2 + 3360*a**4*b + 3360*a**3*b**4
    - 3360*a**3*b**3*c**3 + 43680*a**3*b**3*c**2 - 188160*a**3*b**3*c + 262080*a**3*b**3
    - 3360*a**3*b**2 + 3360*a**3*b*c**3 - 43680*a**3*b*c**2 + 188160*a**3*b*c - 262080*a**3*b
    - 1680*a**2*b**4 - 10080*a**2*b**3*c**3 + 131040*a**2*b**3*c**2 - 564480*a**2*b**3*c + 809760*a**2*b**3
    + 840*a**2*b**2*c**6 - 22680*a**2*b**2*c**5 + 252840*a**2*b**2*c**4 - 1489320*a**2*b**2*c**3 + 4887120*a**2*b**2*c**2 - 8467200*a**2*b**2*c + 6049680*a**2*b**2
    + 840*a**2*b*c**6 - 22680*a**2*b*c**5 + 252840*a**2*b*c**4 - 1479240*a**2*b*c**3 + 4756080*a**2*b*c**2 - 7902720*a**2*b*c + 5238240*a**2*b
    - 3360*a*b**4 - 6720*a*b**3*c**3 + 87360*a*b**3*c**2 - 376320*a*b**3*c + 544320*a*b**3
    + 2520*a*b**2*c**6 - 68040*a*b**2*c**5 + 758520*a*b**2*c**4 - 4467960*a*b**2*c**3 + 14661360*a*b**2*c**2 - 25401600*a*b**2*c + 18147360*a*b**2
    - 56*a*b*c**9 + 2352*a*b*c**8 - 43344*a*b*c**7 + 462168*a*b*c**6 - 3156384*a*b*c**5 + 14377608*a*b*c**4 - 43826776*a*b*c**3 + 86374512*a*b*c**2 - 99859200*a*b*c + 51468480*a*b
    - 56*a*c**9 + 2352*a*c**8 - 43344*a*c**7 + 459648*a*c**6 - 3088344*a*c**5 + 13619088*a*c**4 - 39365536*a*c**3 + 71800512*a*c**2 - 74833920*a*c + 33868800*a
    + 1680*b**2*c**6 - 45360*b**2*c**5 + 505680*b**2*c**4 - 2978640*b**2*c**3 + 9774240*b**2*c**2 - 16934400*b**2*c + 12096000*b**2
    - 112*b*c**9 + 4704*b*c**8 - 86688*b*c**7 + 920976*b*c**6 - 6222048*b*c**5 + 27743856*b*c**4 - 81709712*b*c**3 + 153375264*b*c**2 - 166602240*b*c + 79833600*b
    + c**12 - 58*c**11 + 1517*c**10 - 23742*c**9 + 248487*c**8 - 1838382*c**7 + 9888647*c**6 - 39061538*c**5 + 112617892*c**4 - 231115320*c**3 + 319957056*c**2 - 267442560*c + 101606400
)

for k, Sk in [(7, S_7_bracket), (8, S_8_bracket)]:
    print("=" * 78)
    print(f"S_{k}(a, b, c) at c = 4m+2")
    print("=" * 78)
    Sk_at = expand(Sk.subs(c, 4 * m + 2))
    Sk_ab = expand(Sk_at.subs([(a, A - 2), (b, B - 1)]))
    print(f"S_{k}(A-2, B-1, 4m+2) monomials:")
    poly = Poly(Sk_ab, A, B)
    for mono, coef in sorted(poly.as_dict().items()):
        print(f"   A^{mono[0]} B^{mono[1]}: {expand(coef)}")
    print()
    fac = factor(Sk_ab)
    print(f"  factored: {fac}")
    print()

    const_m = poly.as_dict().get((0, 0), 0)
    print(f"  Constant term in (A, B): {expand(const_m)}")
    print(f"  factored: {factor(const_m)}")
    print()

# Verify empirically that G3 holds at k=7, 8
def v2(n):
    if n == 0: return 10**9
    v = 0
    while n % 2 == 0:
        n //= 2
        v += 1
    return v
def s2(n): return bin(n).count('1') if n > 0 else 0
def car(x, y): return s2(x)+s2(y)-s2(x+y)

# Note: v_2(S_k) is what we care about after factoring out c-linear prefactors.
def check_G3(k, S_bracket_str, v2_pre_fn, min_m=1, max_m=30):
    import sympy
    S_expr = sp.sympify(S_bracket_str) if isinstance(S_bracket_str, str) else S_bracket_str
    fail = 0; oks = 0
    for m_val in range(min_m, max_m):
        c_val = 4 * m_val + 2
        L = c_val - 1 - k
        if L < 0: continue
        v2L = L - s2(L)
        vp = v2_pre_fn(c_val)
        target = 8*m_val + 1 - 2*s2(m_val) - v2(m_val)
        for a_val in range(0, 24):
            for b_val in range(0, 24):
                if (a_val + b_val) % 2: continue
                try:
                    S = int(S_expr.subs([(a, a_val), (b, b_val), (c, c_val)]))
                except Exception:
                    continue
                if S == 0: continue
                v2_Q = vp + v2(S)
                v = 2*v2L + car(a_val+2, L) + car(b_val+1, L) + v2_Q
                if v < target:
                    fail += 1
                    if fail < 3:
                        print(f"  FAIL k={k}: m={m_val}, a={a_val}, b={b_val}: v={v}, target={target}")
                else:
                    oks += 1
    return oks, fail

# k=7: Q_7 = c(c-4)(c-3)(c-2)(c-1) * S_7
o7, f7 = check_G3(7, S_7_bracket, lambda c: v2(c) + v2(c-4) + v2(c-3) + v2(c-2) + v2(c-1))
print(f"k=7 empirical (m in [1, 29]): {o7} pass, {f7} fail")

# k=8: Q_8 = c(c-3)(c-2)(c-1) * S_8
o8, f8 = check_G3(8, S_8_bracket, lambda c: v2(c) + v2(c-3) + v2(c-2) + v2(c-1))
print(f"k=8 empirical (m in [1, 29]): {o8} pass, {f8} fail")

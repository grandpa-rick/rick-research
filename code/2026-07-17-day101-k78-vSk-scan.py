"""Day 101 — scan v_2(S_7) and v_2(S_8) on shell to understand
what analytic bound is needed for G3 closure.

Also compute the slack `v_2(P̂_k) + carries_a + carries_b - (X_k - 7 - e)`
for k = 7, 8 and see where it's minimized.
"""
import sympy as sp
from sympy import symbols

a_, b_, c_ = symbols('a b c')

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

def v2(n):
    if n == 0: return 10**9
    v = 0
    while n % 2 == 0:
        n //= 2; v += 1
    return v
def s2(n): return bin(n).count('1') if n > 0 else 0
def car(x, y): return s2(x)+s2(y)-s2(x+y)


def scan_v2_Pk(k, S_bracket, div, min_m=1, max_m=25, ab_max=32):
    """Compute v_2(P_hat_k) = v_2(S_k) - v_2(div) on shell.
    div = -8 for k=7, 16 for k=8.
    Return histogram of min values.
    """
    # Build fast lambda
    Sfn = sp.lambdify([a_, b_, c_], S_bracket, 'math')
    div_v = v2(abs(div))
    for m in range(min_m, max_m):
        c = 4*m + 2
        e = v2(m)
        rows = []
        for a in range(0, ab_max):
            for b in range(0, ab_max):
                if (a + b) % 2: continue
                S = int(Sfn(a, b, c))
                if S == 0:
                    continue
                vS = v2(S)
                vP = vS - div_v
                rows.append((vP, a, b))
        if not rows: continue
        rows.sort()
        # Top 3 minimum v_2(P_hat_k) configs
        print(f"k={k} m={m:2d} c={c:3d} e={e} min v_2(P_hat_{k}): "
              f"{rows[0][0]} at (a,b)={rows[0][1:]}, "
              f"next {rows[1][0]} at {rows[1][1:]}, "
              f"next {rows[2][0]} at {rows[2][1:]}")


print("=" * 78)
print("v_2(P_hat_7) minima on shell across m")
print("=" * 78)
scan_v2_Pk(7, S_7_bracket, -8)

print()
print("=" * 78)
print("v_2(P_hat_8) minima on shell across m")
print("=" * 78)
scan_v2_Pk(8, S_8_bracket, 16)


# Now: check whether v_2(P_hat_k) + carries actually saturates at anchor (0, 2)
print()
print("=" * 78)
print("Anchor (0, 2) analysis for k=7")
print("=" * 78)
Sfn7 = sp.lambdify([a_, b_, c_], S_7_bracket, 'math')
Sfn8 = sp.lambdify([a_, b_, c_], S_8_bracket, 'math')
for m in range(2, 20):
    c = 4*m + 2
    e = v2(m)
    a, b = 0, 2
    L = c - 1 - 7
    S = int(Sfn7(a, b, c))
    vS = v2(S) if S != 0 else 10**9
    ca = car(a+2, L); cb = car(b+1, L)
    v_Q = v2(c) + v2(c-4) + v2(c-3) + v2(c-2) + v2(c-1) + vS
    v_h = 2*(L - s2(L)) + ca + cb + v_Q
    target = 8*m + 1 - 2*s2(m) - v2(m)
    slack = v_h - target
    vP = vS - 3
    print(f"m={m:2d} c={c:3d} e={e} vS_7={vS:2d} vP_7={vP:2d} ca={ca} cb={cb} slack={slack}")

print()
print("=" * 78)
print("Anchor (0, 2) analysis for k=8")
print("=" * 78)
for m in range(2, 20):
    c = 4*m + 2
    e = v2(m)
    a, b = 0, 2
    L = c - 1 - 8
    if L < 0: continue
    S = int(Sfn8(a, b, c))
    vS = v2(S) if S != 0 else 10**9
    ca = car(a+2, L); cb = car(b+1, L)
    v_Q = v2(c) + v2(c-3) + v2(c-2) + v2(c-1) + vS
    v_h = 2*(L - s2(L)) + ca + cb + v_Q
    target = 8*m + 1 - 2*s2(m) - v2(m)
    slack = v_h - target
    vP = vS - 4
    print(f"m={m:2d} c={c:3d} e={e} vS_8={vS:2d} vP_8={vP:2d} ca={ca} cb={cb} slack={slack}")

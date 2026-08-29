"""Compute minimum slack for k=8 across ALL shell (a, b, m)
and understand where the tight configurations lie.
"""
import sympy as sp
from sympy import symbols

a_, b_, c_ = symbols('a b c')

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

Sfn = sp.lambdify([a_, b_, c_], S_8_bracket, 'math')

def v2(n):
    if n == 0: return 10**9
    v = 0
    while n % 2 == 0: n //= 2; v += 1
    return v
def s2(n): return bin(n).count('1') if n > 0 else 0
def car(x, y): return s2(x)+s2(y)-s2(x+y)

print("Min slack for k=8 across (a, b) shell per m:")
for m in range(2, 40):
    c = 4*m + 2
    L = c - 1 - 8
    if L < 0: continue
    e = v2(m)
    v2Lf = L - s2(L)
    v_pre = v2(c) + v2(c-3) + v2(c-2) + v2(c-1)
    target = 8*m + 1 - 2*s2(m) - v2(m)
    min_slack = 10**9
    min_conf = None
    for a in range(0, 40):
        for b in range(0, 40):
            if (a + b) % 2: continue
            S = int(Sfn(a, b, c))
            if S == 0: continue
            v_Q = v_pre + v2(S)
            ca = car(a+2, L); cb = car(b+1, L)
            v = 2*v2Lf + ca + cb + v_Q
            slack = v - target
            if slack < min_slack:
                min_slack = slack
                min_conf = (a, b, v2(S), ca+cb, v2(S)-4)
    if min_conf is not None:
        a_, b_, vS, cars, vP = min_conf
        print(f"m={m:2d} c={c:3d} e={e}: min slack = {min_slack} at (a,b)=({a_},{b_}), v_2(S_8)={vS}, v_P={vP}, carries={cars}")

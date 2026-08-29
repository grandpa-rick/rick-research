"""Day 101 — check whether carries + 2 covers X_7 - 7 - e on shell.

Setup:
  v_2(P_hat_7) >= 2 UNIFORMLY (mod-4 identity, verified).
  So v_2(S_7) >= 5, and v_2(Q_7) >= 4 + e + 5 = 9 + e.
  Target: v_2(Q_7) + carries + 2v_2(L!) >= β - D.
  Since 2v_2(L!) is already extracted into X_k:
  need: v_2(Q_k) + carries >= X_k(m) (with all reductions applied).

  Actually: v_2(h_k) = 2v_2(L!) + carries + v_2(Q_k)
                    = 2v_2(L!) + carries + (v_2 of c-prefactor) + v_2(S_k)
  So the reduced target (with X_k(m) = β - D - 2v_2(L!) - v_2(c-pref)):
  need carries + v_2(S_k) >= X_k - v_2(c-pref).

For k=7: v_2(c-pref) = 4 + e. So need carries + v_2(S_7) >= X_7 - 4 - e.
With v_2(S_7) >= 5: need carries >= X_7 - 9 - e.

But at anchor (0, 2), v_2(S_7) = 5 EXACTLY, and carries = 2·ca (some fn of m).
Check: (a,b) NOT (0, 2j), possibly v_2(S_7) = 5 but carries lower, or v_2(S_7) > 5
compensates.

Let's verify: for all shell (a, b) and all m, does
    carries(a+2, L) + carries(b+1, L) + v_2(S_7) >= X_7(m) - v_2(c-pref) ?
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

Sfn = sp.lambdify([a_, b_, c_], S_7_bracket, 'math')

def v2(n):
    if n == 0: return 10**9
    v = 0
    while n % 2 == 0: n //= 2; v += 1
    return v
def s2(n): return bin(n).count('1') if n > 0 else 0
def car(x, y): return s2(x)+s2(y)-s2(x+y)

# Scan all shell (a, b) and all m for k=7.
# Test 1: v_2(P_hat_7) >= 2 (uniform mod-4 identity).
fail_uniform = 0
for a in range(0, 40):
    for b in range(0, 40):
        for m in range(1, 30):
            c = 4*m + 2
            S = int(Sfn(a, b, c))
            if S == 0: continue
            if v2(S) < 5:
                fail_uniform += 1
                if fail_uniform < 5:
                    print(f"FAIL uniform v_2(S_7) >= 5: (a,b,m) = ({a},{b},{m}), v_2(S_7) = {v2(S)}")
print(f"v_2(S_7) >= 5 uniform check: {'PASS' if fail_uniform == 0 else f'{fail_uniform} FAILS'}")

# Now check the G3 inequality assuming carries + v_2(S_7) >= X_7 - 4 - e.
# This is EXACT for what we need. We want to check when tight and when has slack.
print()
print("G3 for k=7 direct check on shell (m up to 40):")
fail = 0; oks = 0; tight = 0
tight_examples = []
for m in range(1, 40):
    c = 4*m + 2
    L = c - 1 - 7
    if L < 0: continue
    e = v2(m)
    v2Lf = L - s2(L)
    v_pre = v2(c) + v2(c-4) + v2(c-3) + v2(c-2) + v2(c-1)  # = 4 + e
    target = 8*m + 1 - 2*s2(m) - v2(m)
    for a in range(0, 40):
        for b in range(0, 40):
            if (a + b) % 2: continue
            S = int(Sfn(a, b, c))
            if S == 0: continue
            v_Q = v_pre + v2(S)
            ca = car(a+2, L); cb = car(b+1, L)
            v = 2*v2Lf + ca + cb + v_Q
            if v < target:
                fail += 1
                if fail < 5:
                    print(f"  FAIL: m={m}, a={a}, b={b}: v={v}, target={target}")
            else:
                oks += 1
                if v == target and len(tight_examples) < 20:
                    tight_examples.append((m, a, b, v2(S), ca+cb))
print(f"  {oks} pass, {fail} fail, tight count: {sum(1 for t in tight_examples)}")
if tight_examples:
    print("  Tight examples (v_2(S_7), carries) — the boundary configurations:")
    for m, a, b, vS, cars in tight_examples[:12]:
        print(f"    m={m:2d}, a={a:2d}, b={b:2d}: v_2(S_7)={vS}, carries={cars}")

# Additional stress test: check the "worst case" analytically.
# For each m, what's the min of carries + v_2(S_7) - v_pre - 2v2Lf across shell?
print()
print("Min slack across (a, b) shell per m:")
worst = []
for m in range(1, 40):
    c = 4*m + 2
    L = c - 1 - 7
    if L < 0: continue
    e = v2(m)
    v2Lf = L - s2(L)
    v_pre = v2(c) + v2(c-4) + v2(c-3) + v2(c-2) + v2(c-1)
    target = 8*m + 1 - 2*s2(m) - v2(m)
    min_slack = 10**9
    min_config = None
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
                min_config = (a, b, v2(S), ca+cb, v2(S)-5)
    print(f"m={m:2d}: min slack = {min_slack} at (a,b)={min_config[:2]}, v_2(S_7)={min_config[2]} (v_P={min_config[4]}), carries={min_config[3]}")
    worst.append(min_slack)
print(f"Overall min slack: {min(worst)}")

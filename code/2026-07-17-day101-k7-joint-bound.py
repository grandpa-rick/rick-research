"""Day 101 — test the JOINT BOUND hypothesis for k=7:

Let A = floor((a+2)/2), B = floor((b+1)/2). Then:
    v_2(S_7(a, b, 4m+2)) >= 5 + v_2(A) + v_2(B) ?

This, combined with X-carries, would close the G3-k=7 inequality.

For b = 0: B = 0 → v_2(B) = infty (convention). Handle as special case.
For a = 0 (Case E): A = 1 (odd), v_2(A) = 0.
For a = 1 (Case O): A = 1 (odd), v_2(A) = 0.
Generally A = ceil((a+1)/2 + something).
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

Sfn = sp.lambdify([a_, b_, c_], S_7_bracket, 'math')

def v2(n):
    if n == 0: return 10**9
    v = 0
    while n % 2 == 0: n //= 2; v += 1
    return v
def s2(n): return bin(n).count('1') if n > 0 else 0
def car(x, y): return s2(x)+s2(y)-s2(x+y)

# Test joint bound: v_2(S_7) >= 5 + v_2(A) + v_2(B)
print("Joint bound: v_2(S_7) >= 5 + v_2(A) + v_2(B)?")
print("A = floor((a+2)/2), B = floor((b+1)/2)")
print()

fails = 0
tights_by_case = {}  # (v_2(A), v_2(B), m parity) -> min slack of joint
for m in range(2, 30):
    c = 4*m + 2
    for a in range(0, 40):
        for b in range(0, 40):
            if (a + b) % 2: continue
            S = int(Sfn(a, b, c))
            if S == 0: continue
            vS = v2(S)
            A = (a + 2) // 2
            B = (b + 1) // 2
            vA = v2(A) if A > 0 else 10**9
            vB = v2(B) if B > 0 else 10**9
            predicted = 5 + (vA if vA < 10**9 else 0) + (vB if vB < 10**9 else 0)
            # Note: for b=0, B=0, v_2(B) = inf, so predicted goes to inf. Skip that case here.
            if B == 0:
                continue
            if A == 0:
                continue
            if vS < predicted:
                fails += 1
                if fails < 8:
                    print(f"  FAIL: m={m}, a={a}, b={b}, A={A} (v_2={vA}), B={B} (v_2={vB}): "
                          f"v_2(S_7)={vS}, predicted>={predicted}, diff={vS - predicted}")

print(f"\nTotal failures of v_2(S_7) >= 5 + v_2(A) + v_2(B): {fails}")

# If the joint bound fails, try weaker: v_2(S_7) >= 5 + min(v_2(A), v_2(B), v_2(m-1))?
print()
print("Alternative joint bound: v_2(S_7) >= 5 + min(v_2(A), v_2(B), v_2(m-1))?")
fails2 = 0
for m in range(2, 30):
    c = 4*m + 2
    vM = v2(m-1)
    for a in range(0, 40):
        for b in range(0, 40):
            if (a + b) % 2: continue
            S = int(Sfn(a, b, c))
            if S == 0: continue
            vS = v2(S)
            A = (a + 2) // 2
            B = (b + 1) // 2
            if A == 0 or B == 0: continue
            vA = v2(A); vB = v2(B)
            predicted = 5 + min(vA, vB, vM)
            if vS < predicted:
                fails2 += 1
                if fails2 < 5:
                    print(f"  FAIL: m={m}, a={a}, b={b}: v_2(S_7)={vS}, predicted={predicted}, min(vA={vA},vB={vB},vM={vM})")
print(f"  Total failures: {fails2}")

# Alternative: v_2(S_7) >= 5 + max(v_2(A), v_2(B)) with capping at v_2(m-1)?
print()
print("Alternative 3: v_2(S_7) >= 5 + max(v_2(A), v_2(B)) when NEITHER exceeds v_2(m-1)?")
fails3 = 0
for m in range(2, 30):
    c = 4*m + 2
    vM = v2(m-1)
    for a in range(0, 40):
        for b in range(0, 40):
            if (a + b) % 2: continue
            S = int(Sfn(a, b, c))
            if S == 0: continue
            vS = v2(S)
            A = (a + 2) // 2
            B = (b + 1) // 2
            if A == 0 or B == 0: continue
            vA = v2(A); vB = v2(B)
            if max(vA, vB) > vM: continue  # skip
            predicted = 5 + max(vA, vB)
            if vS < predicted:
                fails3 += 1
                if fails3 < 5:
                    print(f"  FAIL: m={m}, a={a}, b={b}: v_2(S_7)={vS}, predicted={predicted}, vA={vA}, vB={vB}, vM={vM}")
print(f"  Total failures: {fails3}")

# Simpler test: just look at v_2(S_7) - 5 as a function of (v_2(A), v_2(B), v_2(m-1)) on shell EE
print()
print("Statistics: v_2(S_7) - 5 as function of (v_2(A), v_2(B), v_2(m-1)) for shell EE:")
stats = {}  # (vA, vB, vM) -> min value of v_2(S_7) - 5
for m in range(2, 40):
    c = 4*m + 2
    vM = v2(m-1)
    for a in range(0, 24, 2):  # a even (Case E)
        for b in range(0, 24, 2):  # b even
            S = int(Sfn(a, b, c))
            if S == 0: continue
            A = (a + 2) // 2  # a even: A = a/2 + 1
            B = (b + 1) // 2  # b even: B = b/2 (with B=0 possible)
            if B == 0: continue
            vA = v2(A); vB = v2(B)
            k = (min(vA, 5), min(vB, 5), min(vM, 5))  # cap for display
            v = v2(S) - 5
            if k not in stats:
                stats[k] = (v, m, a, b)
            elif v < stats[k][0]:
                stats[k] = (v, m, a, b)
for k in sorted(stats.keys()):
    v, m_, a_, b_ = stats[k]
    print(f"  vA={k[0]}, vB={k[1]}, vM={k[2]}: min v_2(S_7)-5 = {v} at (m,a,b)=({m_},{a_},{b_})")

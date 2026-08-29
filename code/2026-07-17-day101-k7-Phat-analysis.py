"""Day 101 — investigate v_2(P_hat_7) as a joint function of (a, b, m).

Goal: identify a clean lower bound for v_2(P_hat_7) that combines with
carries to prove G3 at k = 7.

Empirical observation from k78-vSk-scan:
- v_2(P_hat_7) minimum on shell is CONSTANT = 2, always achieved
  at anchor (0, 2j) for j >= 1.
- This is not just "min = 2", but structural: perhaps P_hat_7 is
  divisible by 4 for ALL integer (a, b, m).

Test: is P_hat_7 divisible by 4 (i.e., v_2(P_hat_7) >= 2) unconditionally?
Then over shell it might be >= 2, and we'd need carries >= X_7 - 9 - e.

Then: for each (a, b) NOT on the anchor family, we need to show
carries + v_2(P_hat_7) >= X_7 - 7 - e, and structurally P_hat_7 picks up
the slack.
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

# Substitute c = 4m+2, then S_7 / -8 = P_hat_7
S7_at_c = sp.expand(S_7_bracket.subs(c_, 4*m_ + 2))
P_hat_7 = sp.expand(S7_at_c / -8)
# Sanity: verify P_hat_7 is polynomial with integer coefficients
P_hat_7_poly = sp.Poly(P_hat_7, a_, b_, m_)
print("P_hat_7 leading coeffs (integer?):", all(sp.Rational(c).q == 1 for c in P_hat_7_poly.coeffs()))

print()
print("=" * 78)
print("v_2 of every coefficient of P_hat_7 as polynomial in (a, b, m):")
print("=" * 78)
coeffs_v2 = {}
for mono, coef in P_hat_7_poly.as_dict().items():
    v = 0
    n = int(coef)
    if n == 0:
        v = "0"
    else:
        while n % 2 == 0:
            n //= 2
            v += 1
    coeffs_v2[mono] = v
# Group by v
from collections import Counter
v_counts = Counter(coeffs_v2.values())
print(f"v_2 counts across coefficients: {dict(sorted(v_counts.items(), key=lambda x: str(x[0])))}")
print()
# Show low-v_2 monomials
print("Monomials with v_2(coef) < 3:")
for mono, v in sorted(coeffs_v2.items()):
    if isinstance(v, int) and v < 3:
        c = P_hat_7_poly.as_dict()[mono]
        print(f"  a^{mono[0]} b^{mono[1]} m^{mono[2]}: coef = {c} (v_2 = {v})")

# Now: check if P_hat_7 is always divisible by 4 for integer (a, b, m).
# Strategy: evaluate P_hat_7 mod 4 for all (a mod 4, b mod 4, m mod 4).
print()
print("=" * 78)
print("P_hat_7(a, b, m) mod 4 for (a mod 4, b mod 4, m mod 4):")
print("=" * 78)
Pfn = sp.lambdify([a_, b_, m_], P_hat_7, 'math')
nonzero = 0
for am in range(4):
    for bm in range(4):
        for mm in range(4):
            val = int(Pfn(am, bm, mm)) % 4
            if val != 0:
                nonzero += 1
                if nonzero < 20:
                    print(f"  (a,b,m) mod 4 = ({am},{bm},{mm}): P_hat_7 mod 4 = {val}")
if nonzero == 0:
    print("  P_hat_7(a, b, m) is divisible by 4 for ALL integer (a, b, m).")
else:
    print(f"  {nonzero} configurations mod 4 give nonzero.")

print()
print("=" * 78)
print("P_hat_7(a, b, m) mod 2 for (a mod 2, b mod 2, m mod 2):")
print("=" * 78)
for am in range(2):
    for bm in range(2):
        for mm in range(2):
            val = int(Pfn(am, bm, mm)) % 2
            print(f"  (a,b,m) mod 2 = ({am},{bm},{mm}): P_hat_7 mod 2 = {val}")

# Restrict to shell (a + b even)
print()
print("=" * 78)
print("On shell (a+b even) check P_hat_7 mod 4:")
print("=" * 78)
shellcount = 0
for am in range(8):
    for bm in range(8):
        if (am + bm) % 2 != 0: continue
        for mm in range(8):
            val = int(Pfn(am, bm, mm)) % 4
            if val != 0:
                shellcount += 1
                if shellcount < 20:
                    print(f"  (a,b,m) mod 8 = ({am},{bm},{mm}): P_hat_7 mod 4 = {val}")
print(f"  {'ALL divisible by 4 on shell' if shellcount == 0 else f'{shellcount} shell configs give nonzero'}")

# Check on shell mod 8
print()
print("=" * 78)
print("On shell (a+b even) check P_hat_7 mod 8:")
print("=" * 78)
shellcount_8 = 0
for am in range(8):
    for bm in range(8):
        if (am + bm) % 2 != 0: continue
        for mm in range(8):
            val = int(Pfn(am, bm, mm)) % 8
            if val != 0:
                shellcount_8 += 1
print(f"  {'ALL divisible by 8 on shell' if shellcount_8 == 0 else f'{shellcount_8} shell configs mod 8 nonzero (out of 32*8=256)'}")

# Test: (a even, b even) sub-shell: v_2(P_hat_7) >= ?
# Test: (a odd, b odd) sub-shell: v_2(P_hat_7) >= ?
def v2(n):
    if n == 0: return 10**9
    v = 0
    while n % 2 == 0: n //= 2; v += 1
    return v
print()
print("=" * 78)
print("v_2(P_hat_7) min per shell parity (a even/b even vs a odd/b odd):")
print("=" * 78)
for parity in ['EE', 'OO']:
    minv = 10**9
    for m_val in range(1, 20):
        for a_val in range(0 if parity == 'EE' else 1, 32, 2):
            for b_val in range(0 if parity == 'EE' else 1, 32, 2):
                v = int(Pfn(a_val, b_val, m_val))
                if v == 0: continue
                vv = v2(v)
                if vv < minv:
                    minv = vv
                    if minv == 2:
                        pass  # common case
    print(f"  parity {parity}: min v_2(P_hat_7) = {minv}")

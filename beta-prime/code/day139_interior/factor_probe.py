"""Day 139 — factor entries and look for closed forms.

Test candidate closed forms and factorizations for N(b; x_1, x_2, 1).
"""

from sympy import factorint, Rational, Integer, binomial, factorial, symbols, simplify, expand
from sympy import Poly


def factors_str(n):
    if n == 0:
        return "0"
    return "*".join(f"{p}^{e}" if e > 1 else f"{p}" for p, e in sorted(factorint(n).items()))


# Diagonal N(b; 0, 0, 1)
diag = {2: 3, 3: 57, 4: 1422, 5: 49110, 6: 2289960, 7: 139716360,
        8: 10845858240, 9: 1046227492800, 10: 122961081680640}

print("=" * 78)
print("N(b; 0, 0, 1) factorizations:")
print("=" * 78)
for b, v in diag.items():
    # Also compare to b! / something
    factored = factors_str(v)
    ratio_bfact = Rational(v, factorial(b))
    print(f"  b={b}: {v:15}  = {factored}     v / b! = {ratio_bfact}")

# Compare to N(b; 0, 0, 0) = b!^2 * H_b type structure? Actually
# N(b; 0, 0, 0) = coefficient of E_1^0 E_2^0 E_3^0 in P_b, but that's a constant.
# Actually [E1^0 E2^0 E3^0] P_b is the constant coefficient. Let's compute a few.

# Compare to b! * b! * something ?
print()
print("v / (b!)^2 :")
for b, v in diag.items():
    r = Rational(v, factorial(b)**2)
    print(f"  b={b}: v/(b!)^2 = {r}")

# The b! * b! * something pattern
# b=2: 3 / 4 = 3/4
# b=3: 57/36 = 19/12
# b=4: 1422 / 576 = 79/32
# Rick had noted r_2^{(1)}(0,0) = 3, r_3^{(1)}(0,0)=57=3*19, r_4^{(1)}(0,0)=1422 = 2*3*237
# 19 and 79 appear... 3 = 3, 57 = 3*19, 1422 = 2*3*237 = 2*3*3*79...
# Try (2b)! / factor
print()
print("v vs (2b)!/2^b:")
for b, v in diag.items():
    tgt = factorial(2*b) / (2**b)
    r = Rational(v, tgt)
    print(f"  b={b}: v = {v}  (2b)!/2^b = {int(tgt)}  ratio = {r}")

# Ratios between consecutive b
print()
print("Consecutive ratios N(b+1;0,0,1) / N(b;0,0,1):")
bs = sorted(diag.keys())
for i in range(len(bs)-1):
    b = bs[i]
    r = Rational(diag[bs[i+1]], diag[b])
    print(f"  b={b} -> b={bs[i+1]}: {r} = {float(r):.4f}")


# Try N(b;0,0,1) / (Product of something)
# From theorem 2, p_b(E1=0,E2=0) = 1*4*9*16*... = (b!)^2
# So the boundary N(b;0,0,0) is (b!)^2
# What is r_b^{(1)}(0,0) / (b!)^2 ?
# b=2: 3/4;  b=3: 57/36=19/12; b=4: 1422/576=79/32; b=5: 49110/14400=1637/480
print()
print("Look at v / (b!)^2 as reduced fraction:")
for b, v in diag.items():
    r = Rational(v, factorial(b)**2)
    print(f"  b={b}: {r}  (num={r.p}, den={r.q})")

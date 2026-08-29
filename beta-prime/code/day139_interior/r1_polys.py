"""Day 139 — Get the r_b^{(1)} polynomial (coefficient of E_3^1 in P_b) as a polynomial
in E_1, E_2. Look at structure.
"""

from sympy import symbols, Poly, Integer, expand, factor, simplify, sympify, collect
from sympy import Rational, binomial, factorial

E1, E2, E3 = symbols('E1 E2 E3')


def sigma(P):
    if P == 0:
        return Integer(0)
    return expand(P.subs(
        [(E1, E1 - 3), (E2, E2 - 2*E1 + 3), (E3, E3 - E2 + E1 - 1)],
        simultaneous=True))


def phi_map(P):
    if P == 0:
        return Integer(0)
    return expand(P.subs([(E1, -E1), (E3, -E3)], simultaneous=True))


def build_P(B_max):
    Psi = {0: Integer(1), 1: E2 - E1 + 1}
    for b in range(1, B_max):
        term1 = (E2 - (b+1)*E1 + (b+1)**2) * Psi[b]
        term2 = 3*b * E3 * sigma(Psi[b-1])
        term3 = b*(b-1)*(E1 - 2*b - 2) * E3 * sigma(Psi[b-2]) if b >= 2 else Integer(0)
        Psi[b+1] = expand(term1 - term2 - term3)
    return {b: expand(phi_map(Psi[b])) for b in range(B_max + 1)}


def extract_r1(P_b):
    """Return the polynomial r_b^(1)(E_1, E_2) = [E_3^1] P_b."""
    return expand(Poly(P_b, E3).as_dict().get((1,), Integer(0)))


B_MAX = 8
P = build_P(B_MAX)

print("=" * 78)
print("r_b^{(1)}(E_1, E_2) = [E_3^1] P_b")
print("=" * 78)
for b in range(2, B_MAX + 1):
    r1 = extract_r1(P[b])
    r1_c = collect(r1, [E1, E2])
    print(f"\n--- b={b} ---")
    print(f"r_{b}^(1) = {r1_c}")

    # try to factor
    fac = factor(r1)
    print(f"factored: {fac}")


# Compare with p_b (E_3=0 factor) and see r1 / p_b or partial factorizations
print("\n\n" + "=" * 78)
print("Compare r_b^{(1)} vs p_b (which equals P_b|_{E_3=0})")
print("=" * 78)


def p_b(b):
    result = Integer(1)
    for k in range(1, b + 1):
        result *= (E2 + k*E1 + k*k)
    return expand(result)


# Check what r_b^{(1)} / p_{b-2} looks like (motivated by top-of-slab formula)
print("\nDivide r_b^{(1)} by p_{b-2} — polynomial? rational?")
for b in range(2, B_MAX + 1):
    r1 = extract_r1(P[b])
    if b >= 2:
        pbm2 = p_b(b-2)
        # try polynomial division
        from sympy import div
        q, r = div(r1, pbm2, E1, E2)
        if r == 0:
            print(f"  b={b}: r1 / p_{b-2} = {q} (POLYNOMIAL!)")
        else:
            print(f"  b={b}: r1 / p_{b-2}: not clean, remainder {r}")


# The E_3=0 face has closed form N(b;x_1,x_2,0) = Σ (prod U) e_{b-x1-x2}(U)
# Perhaps N(b;x_1,x_2,1) has similar form but with U of size b - x_2 shifted?
# Try: N(b;x_1,x_2,1) = Σ over pairs of "special elements" + rest as before?

# Let's compute the coeff of E_2^{b-2} in r_b^(1), etc — pure x_2 direction
# We have: N(b;0,b-2,1) = 3 * C(b,2)
# What about N(b;0,b-3,1)? (a step below top)
print("\n\n" + "=" * 78)
print("Fixed direction x_1=0, varying x_2 (pure E_2 direction below top):")
print("=" * 78)
def coeff(P_b, x1, x2, x3):
    d = Poly(P_b, E1, E2, E3).as_dict()
    return d.get((x1, x2, x3), Integer(0))

for b in range(2, B_MAX+1):
    print(f"\nb={b}:")
    for x2 in range(0, b-1):
        v = int(coeff(P[b], 0, x2, 1))
        # weight w = 0+x2+2 = x2+2
        # "corank" c = b - x1 - x2 - 2 = b - x2 - 2 (excess)
        r = b - x2 - 2
        print(f"  N(b;0,{x2},1) = {v}  (excess r={r})")

# Try to guess formula for N(b; 0, x2, 1) — a symmetric-function candidate
# On x_3=0 with x_1=0: N(b;0,x2,0) = sum_{U in [b], |U|=b-x2} (prod U) * e_{b-x2}(U)
#                                  = sum |U|=b-x2 (prod U)^2 (since e_{|U|}(U) = prod U)
#                                  = sum |U|=b-x2 (prod U)^2
# and this = e_{b-x2}(1^2, 2^2, ..., b^2)
# For x_3=1 pure E_2, maybe some similar "signed" or "shifted" identity
print("\n\ncomparison N(b;0,x2,0) via formula:")
from itertools import combinations
for b in range(2, B_MAX+1):
    for x2 in range(0, b+1):
        # N(b;0,x2,0) = sum_{U subset [b], |U|=b-x2} (prod U) * e_{b-x2}(U) = sum (prod U)^2
        val = Integer(0)
        for U in combinations(range(1, b+1), b - x2):
            p = 1
            for k in U:
                p *= k
            val += p*p
        print(f"  b={b}, x2={x2}: N(b;0,{x2},0) = {val} = e_{b-x2}(1²..b²)")

"""Day 139 — Study corner formulas for x_3=1 slice."""

from sympy import symbols, Poly, Integer, expand, factor, simplify, sympify
from sympy import Rational, Add, Mul, Pow, gcd, binomial, factorial

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


def coeff(P_b, x1, x2, x3):
    d = Poly(P_b, E1, E2, E3).as_dict()
    return d.get((x1, x2, x3), Integer(0))


B_MAX = 10
P = build_P(B_MAX)

print("=" * 78)
print("CORNER FORMULAS on the x_3 = 1 face")
print("Support: x_1 + x_2 <= b - 2")
print("=" * 78)

# Top-weight (x_1 + x_2 = b - 2): "top" of the x_3=1 slab
print("\n--- TOP of slab: x_1 + x_2 = b - 2 ---")
for b in range(2, B_MAX + 1):
    print(f"\nb={b}:")
    for x1 in range(0, b - 1):
        x2 = b - 2 - x1
        v = coeff(P[b], x1, x2, 1)
        print(f"  N(b={b}; x1={x1}, x2={x2}, 1) = {int(v)}")

# Pure E_1: (x_2=0) column
print("\n\n--- Pure E_1 column: x_2 = 0 ---")
for x1 in range(0, 6):
    print(f"\nx_1 = {x1}:")
    for b in range(x1 + 2, B_MAX + 1):
        v = int(coeff(P[b], x1, 0, 1))
        print(f"  b={b}: N({b}; {x1}, 0, 1) = {v}")

# Pure E_2: (x_1=0) column
print("\n\n--- Pure E_2 column: x_1 = 0 ---")
for x2 in range(0, 6):
    print(f"\nx_2 = {x2}:")
    for b in range(x2 + 2, B_MAX + 1):
        v = int(coeff(P[b], 0, x2, 1))
        print(f"  b={b}: N({b}; 0, {x2}, 1) = {v}")


# TEST HYPOTHESIS: The "top of slab" corner where x_1+x_2 = b-2
# Perhaps N(b; x1, x2, 1) at top = 3 * something on shorter x_3=0 face
print("\n\n" + "=" * 78)
print("HYPOTHESIS TEST: N(b; x1, x2, 1) at top of slab vs. N(b-2; x1, x2, 0)?")
print("=" * 78)
for b in range(4, B_MAX + 1):
    print(f"\nb={b}:")
    for x1 in range(0, b - 1):
        x2 = b - 2 - x1
        v = int(coeff(P[b], x1, x2, 1))
        # candidate: 3 * N(b-2; x1, x2, 0) * something
        # boundary N(b-2; x1, x2, 0) at top of x_3=0 slab is a corner formula
        # Note the top of x_3=0 slab for smaller b-2 is x_1+x_2 = b-2 (matches)
        # Let's compute this candidate:
        if x1 + x2 <= b - 2:
            v_02 = int(coeff(P[b-2], x1, x2, 0))
            print(f"  x1={x1}, x2={x2}: N(b={b}; ..., 1) = {v}   N(b-2={b-2}; ..., 0) = {v_02}   ratio = {Rational(v, v_02) if v_02 else 'N/A'}")


# HYPOTHESIS: top-of-slab entry = 3 * C(b,2) * N(b-2; x1, x2, 0) ?
print("\n\n" + "=" * 78)
print("HYPOTHESIS: N(b; x1, x2, 1) top-of-slab = 3*C(b,2) * N(b-2; x1, x2, 0)")
print("=" * 78)
for b in range(4, B_MAX + 1):
    print(f"\nb={b}, 3*C(b,2) = {3*b*(b-1)//2}:")
    for x1 in range(0, b - 1):
        x2 = b - 2 - x1
        v = int(coeff(P[b], x1, x2, 1))
        if x1 + x2 <= b - 2:
            v_02 = int(coeff(P[b-2], x1, x2, 0))
            expected = 3 * b*(b-1)//2 * v_02
            match = "OK" if v == expected else f"MISS (diff {v - expected})"
            print(f"  x1={x1}, x2={x2}: v={v}  3*C(b,2)*N(b-2;...) = {expected}  {match}")

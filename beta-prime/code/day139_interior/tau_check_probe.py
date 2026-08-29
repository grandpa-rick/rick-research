"""Day 139 — Unfold Theorem 4 by iterating.

r_b^(1) = Σ_{j=1}^{b-1} (p_b/p_{j+1}) [3j·τ̌(P_{j-1}) - j(j-1)(E_1+2j+2)·τ̌(P_{j-2})]

τ̌(P_j) uses only the E_3=0 slice of P_j substituted, but P_j has E_3-dependent parts.
Wait: τ̌ substitutes E_1→E_1+3, E_2→2E_1+E_2+3, E_3→φ_1=E_1+E_2+1.

So τ̌(P_j) is a polynomial in E_1, E_2 where the E_3^k parts of P_j get φ_1^k contributions.

At [E_3^1] level of the OUTER formula, we don't get further "E_3-generating" — but we
DO recursively hit r_{j-1}^{(1)} inside τ̌(P_{j-1}) via the φ_1 substitution.

Let's split τ̌(P_{j-1}) = p_{j-1}(E_1+3, 2E_1+E_2+3) [the pure-boundary piece]
                       + φ_1 * r_{j-1}^{(1)}(E_1+3, 2E_1+E_2+3) [the E_3^1 piece — substituted]
                       + φ_1^2 * r_{j-1}^{(2)}(...) etc.

So r_b^{(1)} recursively depends on r_j^{(1)}, r_j^{(2)}, ... for j < b.

Let me compute PURE-BOUNDARY contribution: replace P_{j-1} by p_{j-1} (E_3-free) in Theorem 4.
Call this  ř_b^{(1)}.

  ř_b^{(1)} := Σ_{j=1}^{b-1} (p_b/p_{j+1}) [3j·τ̌_0(p_{j-1}) - j(j-1)(E_1+2j+2)·τ̌_0(p_{j-2})]

where τ̌_0(f)(E_1, E_2) := f(E_1+3, 2E_1+E_2+3).

Then compare ř_b^{(1)} to r_b^{(1)} = actual. The "leakage" from higher r_j^{(≥1)} is the difference.
"""

from sympy import symbols, Poly, Integer, expand, factor, simplify, sympify
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


B_MAX = 8
P = build_P(B_MAX)

phi_k = lambda k: E2 + k*E1 + k*k

def p_b(b):
    r = Integer(1)
    for k in range(1, b+1):
        r *= phi_k(k)
    return expand(r)

def tau_check0(f):
    """τ̌_0(f) = f(E_1+3, 2E_1+E_2+3), for E_3-free f."""
    return expand(f.subs([(E1, E1+3), (E2, 2*E1+E2+3)], simultaneous=True))


print("=" * 78)
print("PURE-BOUNDARY-P CONTRIBUTION ř_b^{(1)}")
print("Replace P_j by p_j (E_3-free part only) in Theorem 4.")
print("=" * 78)
for b in range(2, B_MAX + 1):
    summ = Integer(0)
    for j in range(1, b):
        pj_m1 = p_b(j-1)  # note P_{j-1} → p_{j-1}
        pj_m2 = p_b(j-2) if j-2 >= 0 else Integer(0)
        term = 3*j * tau_check0(pj_m1)
        if j >= 2:
            term -= j*(j-1)*(E1 + 2*j + 2) * tau_check0(pj_m2)
        factor_prod = Integer(1)
        for k in range(j+2, b+1):
            factor_prod *= phi_k(k)
        summ += factor_prod * term
    summ = expand(summ)

    # Compare to actual r_b^(1)
    actual = expand(Poly(P[b], E3).as_dict().get((1,), Integer(0)))
    diff = expand(actual - summ)
    print(f"\n--- b={b} ---")
    print(f"  ř_b^(1) = {summ}")
    print(f"  actual  = {actual}")
    print(f"  diff (actual - ř) = {diff}")


# Test another simple ansatz: maybe the actual r_b^{(1)} is best expressed as
# a sum over CHAINS 1 <= i < j <= b, weighted by some j-i dependent quantity times
# a boundary formula on [b]\{i,j}.

# Look at diagonal r_b^{(1)}(0,0): compute values
print("\n\n" + "=" * 78)
print("Testing: r_b^{(1)}(0,0) = ?")
print("=" * 78)
def r_num(b):
    return int(expand(Poly(P[b], E3).as_dict().get((1,), Integer(0))).subs([(E1, 0), (E2, 0)]))

seq = [r_num(b) for b in range(2, B_MAX+1)]
print(f"r_b^(1)(0,0) for b=2..{B_MAX}: {seq}")

# Look for patterns via ratios and quotients
from sympy import Rational
for i in range(len(seq) - 1):
    r = Rational(seq[i+1], seq[i])
    print(f"  b={i+2}->b={i+3}: ratio = {r} = {float(r):.4f}")

# The x_1+x_2+2 = b top-of-slab is 3*C(b,2)
# The pure E_1 corner (x_1=b-2, x_2=0) is:
print("\nPure E_1 corner N(b; b-2, 0, 1):")
for b in range(2, B_MAX+1):
    v = int(expand(Poly(P[b], E3).as_dict().get((1,), Integer(0))).coeff(E1, b-2).subs(E2, 0))
    print(f"  b={b}: {v}   — vs 3*C(b,2)*(b-2)! = {3*b*(b-1)//2 * factorial(b-2)}")

# Actually: N(b; b-2, 0, 1) is the coeff of E_1^{b-2} in r_b^(1), setting E_2=0.
# Let's see:
print("\nActually compute:")
for b in range(2, B_MAX+1):
    r1 = expand(Poly(P[b], E3).as_dict().get((1,), Integer(0)))
    d = Poly(r1, E1, E2).as_dict()
    v = int(d.get((b-2, 0), 0))
    print(f"  b={b}: N(b; b-2, 0, 1) = {v}")

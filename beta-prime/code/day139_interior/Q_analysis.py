"""Day 139 — Attack Angle D: the Q_b recursion.

P_{b+1} = A_b P_b + b E_3 Q_b   (Day 137 form)

At [E_3^1]:
  r_{b+1}^{(1)} = A_b r_b^{(1)} + b · q_b^{(0)}
where q_b^{(0)} := [E_3^0] Q_b.

So r_{b+1}^{(1)} = phi_{b+1} · r_b^{(1)} + b · q_b^{(0)}.

Unrolling from r_1^{(1)} = 0:
  r_b^{(1)} = Σ_{j=1}^{b-1} (Π_{k=j+2}^{b} phi_k) · j · q_j^{(0)}
            = Σ_{j=1}^{b-1} (p_b / p_{j+1}) · j · q_j^{(0)}

So the ONLY question is: what is q_j^{(0)} = [E_3^0] Q_j ??

Compute q_j^{(0)} from the actual P_b values and see if closed form exists.
"""

from sympy import symbols, Poly, Integer, expand, factor, simplify, collect, Rational, factorial
from itertools import combinations

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


def phi_k(k):
    return E2 + k*E1 + k*k


B_MAX = 10
P = build_P(B_MAX)


# Compute Q_b via Day-137 form: P_{b+1} = A_b P_b + b E_3 Q_b
# => Q_b = (P_{b+1} - A_b P_b) / (b E_3)  [for b >= 1]
print("=" * 78)
print("Computing q_b^{(0)} := [E_3^0] Q_b")
print("  where Q_b = (P_{b+1} - φ_{b+1} P_b) / (b E_3)")
print("=" * 78)

Q_polys = {}
q0 = {}   # q_b^{(0)} = [E_3^0] Q_b
for b in range(1, B_MAX):
    A_b = phi_k(b+1)
    diff = expand(P[b+1] - A_b * P[b])
    # divide by b*E_3
    d = Poly(diff, E3).as_dict()
    # extract only positive powers of E_3
    Q = Integer(0)
    for (k,), c in d.items():
        if k >= 1:
            Q += c * E3**(k-1)
    Q = expand(Q / b)
    Q_polys[b] = Q
    # [E_3^0]
    q0[b] = expand(Poly(Q, E3).as_dict().get((0,), Integer(0)))

for b in range(1, B_MAX):
    print(f"\n--- q_{b}^{{(0)}} ---")
    print(f"  = {q0[b]}")
    fac = factor(q0[b])
    print(f"  factor: {fac}")


# Verify: r_{b+1}^{(1)} = phi_{b+1} * r_b^{(1)} + b * q_b^{(0)}
print("\n\n" + "=" * 78)
print("VERIFY: r_{b+1}^{(1)} = phi_{b+1} r_b^{(1)} + b · q_b^{(0)}")
print("=" * 78)
def r1(b):
    return expand(Poly(P[b], E3).as_dict().get((1,), Integer(0)))

for b in range(1, B_MAX):
    lhs = r1(b+1)
    rhs = expand(phi_k(b+1) * r1(b) + b * q0[b])
    diff = expand(lhs - rhs)
    print(f"  b={b}: {'OK' if diff == 0 else 'FAIL diff='+str(diff)}")


# Now: LOOK AT q0[b]. What is it?
# From Day 138: q_b^{(0)} = 3 τ̌(P_{b-1}) - (b-1)(E_1+2b+2) τ̌(P_{b-2})
# where τ̌(f)(E_1, E_2, ...) = f(E_1+3, 2E_1+E_2+3, ... E_3->φ_1 substituted)

# But wait — the τ̌ on P_{j-1} propagates the E_3-dependence back in!
# Let's split: q_b^{(0)} = q̌_b + (correction)
# where q̌_b = 3 τ̌_0(p_{b-1}) - (b-1)(E_1+2b+2) τ̌_0(p_{b-2})
# with τ̌_0 f(E1, E2) := f(E_1+3, 2E_1+E_2+3)

def tau_check0(f):
    return expand(f.subs([(E1, E1+3), (E2, 2*E1+E2+3)], simultaneous=True))


def p_b_poly(b):
    r = Integer(1)
    for k in range(1, b + 1):
        r *= phi_k(k)
    return expand(r)


print("\n\n" + "=" * 78)
print("Split q_b^{(0)} = q̌_b (from p_{b-1}, p_{b-2}) + correction from r_{b-1}^{(1)}, r_{b-2}^{(1)}, ...")
print("=" * 78)
for b in range(1, B_MAX):
    q_check = 3 * tau_check0(p_b_poly(b-1))
    if b >= 2:
        q_check -= (b-1)*(E1 + 2*b + 2) * tau_check0(p_b_poly(b-2))
    q_check = expand(q_check)
    correction = expand(q0[b] - q_check)
    print(f"\nb={b}:")
    print(f"  q̌_b (pure boundary) = {q_check}")
    print(f"  q_b^(0) actual = {q0[b]}")
    print(f"  correction = {correction}")
    if correction != 0:
        print(f"  correction factored: {factor(correction)}")


# ALSO test: at (E1=0, E2=0), what is q_b^{(0)}?
print("\n\n" + "=" * 78)
print("Numeric q_b^{(0)}(0,0):")
print("=" * 78)
seq = []
for b in range(1, B_MAX):
    v = int(q0[b].subs([(E1, 0), (E2, 0)]))
    seq.append(v)
    print(f"  q_{b}^(0)(0,0) = {v}")
print(f"\nSequence: {seq}")


# Try OEIS via curl

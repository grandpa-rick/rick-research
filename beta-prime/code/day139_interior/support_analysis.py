"""Day 139 — Which coefficients of r_b^{(1)} come purely from T[p]_b vs need higher k?

T[p]_b matches on the boundary of the x_3=1 support? Or has a specific "shape"?

Compute difference (r_b^{(1)} - T[p]_b) and see which (x_1, x_2) monomials it lives on.
"""

from sympy import symbols, Poly, Integer, expand, factor

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


def p_b(b):
    r = Integer(1)
    for k in range(1, b + 1):
        r *= phi_k(k)
    return expand(r)


def tau_check0(f):
    return expand(f.subs([(E1, E1+3), (E2, 2*E1+E2+3)], simultaneous=True))


def T_op(f_seq, b):
    s = Integer(0)
    for j in range(1, b):
        factor_prod = Integer(1)
        for k in range(j+2, b+1):
            factor_prod *= phi_k(k)
        f_jm1 = f_seq.get(j-1, Integer(0))
        f_jm2 = f_seq.get(j-2, Integer(0)) if j >= 2 else Integer(0)
        inner = 3 * tau_check0(f_jm1)
        if j >= 2:
            inner -= (j-1)*(E1 + 2*j + 2) * tau_check0(f_jm2)
        s += factor_prod * j * inner
    return expand(s)


B_MAX = 8
P = build_P(B_MAX)


def r_k(b, k):
    return expand(Poly(P[b], E3).as_dict().get((k,), Integer(0)))


p_seq = {b: p_b(b) for b in range(0, B_MAX + 1)}


print("=" * 78)
print("The DIFFERENCE r_b^{(1)} - T[p]_b (positive part missing from pure boundary)")
print("=" * 78)
for b in range(2, B_MAX + 1):
    r1 = r_k(b, 1)
    leading = T_op(p_seq, b)
    diff = expand(r1 - leading)
    print(f"\n--- b={b} ---")
    print(f"diff = {diff}")
    # Which (x_1, x_2) monomials?
    d = Poly(diff, E1, E2).as_dict()
    nonzero_monomials = [((x1, x2), int(c)) for (x1, x2), c in d.items() if c != 0]
    print(f"nonzero monomials: {nonzero_monomials}")


# Interpretation: since diff = φ_1 · T[r^(1)]_b + φ_1^2 · T[r^(2)]_b + ...,
# and φ_1 = E_1 + E_2 + 1 has positive coefs, the diff is φ_1 times something.
# Extract diff / φ_1
phi1 = phi_k(1)

print("\n\n" + "=" * 78)
print("diff / φ_1 (must be polynomial by our theorem):")
print("=" * 78)
from sympy import div
for b in range(2, B_MAX + 1):
    r1 = r_k(b, 1)
    leading = T_op(p_seq, b)
    diff = expand(r1 - leading)
    if diff == 0:
        print(f"  b={b}: diff = 0")
        continue
    q, r = div(diff, phi1, E1, E2)
    if r == 0:
        print(f"  b={b}: diff / φ_1 = {q}   (polynomial! OK)")
    else:
        print(f"  b={b}: diff / φ_1 has remainder {r}")


# Corollary: T[p]_b + φ_1·(diff/φ_1) = r_b^{(1)}
# So we can iterate one more time: diff/φ_1 = T[r^(1)]_b + φ_1·T[r^(2)]_b + ...
# For SMALL b where r^(2) = 0 (b < 4), we should have diff/φ_1 = T[r^(1)]_b exactly

# Verify this at small b
print("\n\n" + "=" * 78)
print("For b < 4, r^(2)_j = 0 so diff/φ_1 should EQUAL T[r^(1)]_b")
print("=" * 78)
r1_seq = {b: r_k(b, 1) for b in range(0, B_MAX + 1)}
r2_seq = {b: r_k(b, 2) for b in range(0, B_MAX + 1)}
r3_seq = {b: r_k(b, 3) for b in range(0, B_MAX + 1)}
r4_seq = {b: r_k(b, 4) for b in range(0, B_MAX + 1)}

for b in range(2, B_MAX + 1):
    r1 = r_k(b, 1)
    leading = T_op(p_seq, b)
    diff = expand(r1 - leading)
    if diff == 0:
        continue
    q, rem = div(diff, phi1, E1, E2)
    tr1 = T_op(r1_seq, b)
    diff2 = expand(q - tr1)
    # diff2 should equal Σ_{k≥1} φ_1^k T[r^{(k+1)}]_b
    if diff2 == 0:
        print(f"  b={b}: q = T[r^(1)]_b — no higher corrections needed")
    else:
        q2, rem2 = div(diff2, phi1, E1, E2)
        if rem2 == 0:
            print(f"  b={b}: q - T[r^(1)]_b = φ_1 · (something polynomial); level 2 correction present")
        else:
            print(f"  b={b}: unexpected — q - T[r^(1)]_b not divisible by φ_1")


# WRITE UP the full recursion cleanly
print("\n\n" + "=" * 78)
print("FINAL VERIFICATION: r_b^{(1)} = Σ_{k=0}^{floor(b/2)} φ_1^k · T[r^{(k)}]_b")
print("(k=0 uses p_·, k>=1 uses r^{(k)}_·)")
print("=" * 78)
for b in range(2, B_MAX + 1):
    r1_actual = r_k(b, 1)
    predicted = T_op(p_seq, b)
    for k in range(1, b // 2 + 1):
        rk_seq = {j: r_k(j, k) for j in range(0, B_MAX + 1)}
        predicted += phi1**k * T_op(rk_seq, b)
    predicted = expand(predicted)
    diff = expand(r1_actual - predicted)
    print(f"  b={b}: {'OK' if diff == 0 else 'FAIL diff='+str(diff)[:50]}")

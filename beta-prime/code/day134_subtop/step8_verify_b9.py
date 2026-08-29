"""Compute B_9^{(1)} and B_10^{(1)} via ansatz recursion, check uniform sign."""
import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day127')
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day128')

from lib import s, y, t, u1, u2, u3
from task1_psi_e2_b5_b6 import (Psi_direct, sym_to_ebasis_direct, e2_u,
                                 E1, E2, E3, weight_of_e_monom)
from sympy import Poly, Integer, expand, Rational, factorial, binomial


def weight_part(P, w):
    P = expand(P)
    if P == 0:
        return Integer(0)
    p = Poly(P, E1, E2, E3)
    out = Integer(0)
    for monom, coeff in p.as_dict().items():
        i, j, k = monom
        if i + j + 2*k == w:
            out += coeff * E1**i * E2**j * E3**k
    return out


def A_n(n):
    p = Integer(1)
    for r in range(1, n + 1):
        p = expand(p * (E2 - r * E1))
    return p


def A_n_upper1(n):
    total = Integer(0)
    for r in range(1, n + 1):
        term = Integer(r) ** 2
        for s_ in range(1, n + 1):
            if s_ != r:
                term = expand(term * (E2 - s_ * E1))
        total = expand(total + term)
    return total


def mu(n):
    return Rational((-1) ** (n - 1) * (n * n - 1), n)


def B_m(m):
    if m == 0:
        return Integer(1)
    total = Integer(0)
    for k in range(1, m // 2 + 1):
        def enum_comps(rem, parts_left):
            if parts_left == 0:
                if rem == 0:
                    yield ()
                return
            for a in range(2, rem - 2 * (parts_left - 1) + 1):
                for rest in enum_comps(rem - a, parts_left - 1):
                    yield (a,) + rest
        sub = Integer(0)
        for comp in enum_comps(m, k):
            prod = Integer(1)
            for a in comp:
                prod = prod * mu(a) * E1 ** (a - 2)
            sub = sub + prod
        total = total + E3 ** k * sub / factorial(k)
    return expand(total * factorial(m))


NMAX = 10

# Direct Psi_b for b = 1..NMAX (need sub_1)
print("Computing sub_1[b] for b = 1..NMAX (this takes a while for b=9, 10)...")
sub1 = {0: Integer(0)}
for b in range(1, NMAX + 1):
    psi_u = Psi_direct(e2_u ** b)
    psi_e = sym_to_ebasis_direct(psi_u)
    sub1[b] = weight_part(psi_e, b - 1)
    print(f"  sub_1[{b}] computed.")

An_cache = {n: A_n(n) for n in range(NMAX + 1)}
An1_cache = {n: A_n_upper1(n) for n in range(NMAX + 1)}
Bm_cache = {m: B_m(m) for m in range(NMAX + 1)}

# Fit B_m^{(1)}
B1 = {0: Integer(0)}
for m in range(1, NMAX + 1):
    b = m
    known = Integer(0)
    for n in range(1, b + 1):
        m_prime = b - n
        term1 = An1_cache[n] * Bm_cache[m_prime]
        if m_prime < m:
            term2 = An_cache[n] * B1[m_prime]
        else:
            term2 = Integer(0)
        known = expand(known + binomial(b, n) * (term1 + term2))
    B1[m] = expand(sub1[b] - known)

# Uniform sign check
print("\n=== Uniform sign check on B_m^{(1)} for m = 1..NMAX ===")
for m in range(1, NMAX + 1):
    if B1[m] == 0:
        print(f"  B_{m}^{{(1)}} = 0")
        continue
    p = Poly(B1[m], E1, E2, E3)
    fails = []
    for monom, c in p.as_dict().items():
        i, j, k = monom
        s_pred = 1 if (i + k) % 2 == 0 else -1
        s_act = 1 if c > 0 else -1
        if s_pred != s_act:
            fails.append((monom, c, s_pred))
    if fails:
        print(f"  B_{m}^{{(1)}}: SIGN MISMATCHES: {fails}")
    else:
        n_monoms = sum(1 for _, c in p.as_dict().items() if c != 0)
        print(f"  B_{m}^{{(1)}}: uniform sign (-1)^{{x1+x3}} ✓  ({n_monoms} monomials)")

# Also verify the boundary column formulas for Q_n hold at n = 9, 10
b1_series = {m: expand(B1[m] / factorial(m)) for m in range(NMAX + 1)}
b0_series = {m: expand(Bm_cache[m] / factorial(m)) for m in range(NMAX + 1)}

Q = {}
for n in range(NMAX + 1):
    rhs = b1_series[n]
    for k in range(1, n + 1):
        if n - k in Q:
            rhs = expand(rhs - Q[n - k] * b0_series[k])
    Q[n] = rhs

def extract_coeff(P, i, j, k):
    p = Poly(expand(P), E1, E2, E3)
    d = p.as_dict()
    return d.get((i, j, k), Integer(0))

print("\n=== Verify boundary formulas at n = 9, 10 ===")
for n in [9, 10]:
    # E_1^{n-3} E_3
    actual = extract_coeff(Q[n], n - 3, 0, 1)
    predicted = Rational((-1) ** n * (n - 1) * (n - 2) * (11 * n + 15), 12)
    status = "✓" if actual == predicted else "✗"
    print(f"  n={n}: [Q_n at E_1^{n-3} E_3] actual={actual}, predicted={predicted} {status}")
    # E_1^{n-4} E_2 E_3
    actual2 = extract_coeff(Q[n], n - 4, 1, 1)
    predicted2 = Rational((-1) ** (n + 1) * (n - 1) * (n - 2) * (n - 3) * (5 * n + 6), 12 * n)
    status2 = "✓" if actual2 == predicted2 else "✗"
    print(f"  n={n}: [Q_n at E_1^{n-4} E_2 E_3] actual={actual2}, predicted={predicted2} {status2}")
    # E_1^{n-5} E_3^2
    actual3 = extract_coeff(Q[n], n - 5, 0, 2)
    predicted3 = Rational((-1) ** (n + 1) * (n - 1) * (n - 2) * (n - 3) * (n - 4) * (7 * n * n + 40 * n + 30), 360 * n)
    status3 = "✓" if actual3 == predicted3 else "✗"
    print(f"  n={n}: [Q_n at E_1^{n-5} E_3^2] actual={actual3}, predicted={predicted3} {status3}")

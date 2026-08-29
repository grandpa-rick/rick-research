"""Verify A_b^{(1)} = sum_{r=1}^b r^2 * prod_{s != r} (E_2 - s E_1).
Then fit B_m^{(1)} for m = 1..8 by matching the ansatz:
  sub_1[b] = sum_{n+m=b} C(b,n) [A_n^{(1)} B_m + A_n B_m^{(1)}].
"""
import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day127')
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day128')

from lib import s, y, t, u1, u2, u3
from task1_psi_e2_b5_b6 import (Psi_direct, sym_to_ebasis_direct, e2_u,
                                 E1, E2, E3, weight_of_e_monom)
from sympy import (Poly, Integer, expand, symbols, Rational, factorial,
                    binomial, Symbol, factor, cancel, S)

T = Symbol('T')


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
    """A_n^{(1)} := sum_{r=1..n} r^2 * prod_{s != r} (E_2 - s E_1)."""
    total = Integer(0)
    for r in range(1, n + 1):
        term = Integer(r) ** 2
        for s in range(1, n + 1):
            if s != r:
                term = expand(term * (E2 - s * E1))
        total = expand(total + term)
    return total


def mu(n):
    return Rational((-1) ** (n - 1) * (n * n - 1), n)


def B_m(m):
    """B_m = m! * [T^m] exp(E_3 M(T)), computed via sum over compositions of m."""
    if m == 0:
        return Integer(1)
    total = Integer(0)
    # sum over k = 1..m//2 of E_3^k / k! * sum_{compositions n_1..n_k, n_i>=2, sum=m} prod mu(n_i) E_1^{n_i - 2}
    for k in range(1, m // 2 + 1):
        # enumerate compositions
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


# Compute directly Psi_b and extract sub_1[b]
NMAX = 8
tops = {0: Integer(1)}
sub1 = {0: Integer(0)}
for b in range(1, NMAX + 1):
    psi_u = Psi_direct(e2_u ** b)
    psi_e = sym_to_ebasis_direct(psi_u)
    tops[b] = weight_part(psi_e, b)
    sub1[b] = weight_part(psi_e, b - 1)


print("=== Verify A_b^{(1)} matches [E_3^0] sub_1[b] ===")
for b in range(1, NMAX + 1):
    A_up1 = A_n_upper1(b)
    # [E_3^0] sub_1[b]
    p = Poly(sub1[b], E1, E2, E3)
    e3_0 = Integer(0)
    for monom, c in p.as_dict().items():
        i, j, k = monom
        if k == 0:
            e3_0 += c * E1**i * E2**j
    e3_0 = expand(e3_0)
    diff = expand(A_up1 - e3_0)
    if diff == 0:
        print(f"  b={b}: A_b^{{(1)}} = [E_3^0] sub_1[b] ✓")
    else:
        print(f"  b={b}: MISMATCH, diff = {diff}")


print("\n=== Verify B_m values match direct exp computation ===")
for m in range(NMAX + 1):
    bm = B_m(m)
    print(f"  B_{m} = {bm}")


# Now fit B_m^{(1)}. Ansatz:
#   sub_1[b] = sum_{n+m=b} C(b,n) [A_n^{(1)} B_m + A_n B_m^{(1)}].
# Given B_0^{(1)} = 0 (weight -1 undefined), compute B_m^{(1)} iteratively.

print("\n=== Fit B_m^{(1)} for m = 1..NMAX ===")
B1 = {0: Integer(0)}
An_cache = {n: A_n(n) for n in range(NMAX + 1)}
An1_cache = {n: A_n_upper1(n) for n in range(NMAX + 1)}
Bm_cache = {m: B_m(m) for m in range(NMAX + 1)}

for m in range(1, NMAX + 1):
    b = m
    # Known contributions from A_n^{(1)} B_m for n=1..b (skipping n=0 term with A_0^{(1)} = 0),
    # plus A_n B_m^{(1)} for m' = b - n where B_{m'}^{(1)} is already known (m' < m).
    # The unknown is B_m^{(1)} appearing at (n, m') = (0, m) → C(b,0)·A_0·B_m^{(1)} = B_m^{(1)}.
    known = Integer(0)
    for n in range(1, b + 1):
        m_prime = b - n
        # A_n^{(1)} · B_{m_prime}
        term1 = An1_cache[n] * Bm_cache[m_prime]
        # A_n · B_{m_prime}^{(1)} (only for m_prime < m; B_m^{(1)} is unknown)
        if m_prime < m:
            term2 = An_cache[n] * B1[m_prime]
        else:
            term2 = Integer(0)
        known = expand(known + binomial(b, n) * (term1 + term2))
    # Also n=0 contribution: A_0^{(1)} = 0, A_0 · B_m^{(1)} = B_m^{(1)} (unknown, extracted below)
    # Full sum: sub_1[b] = known + B_m^{(1)}.
    B1[m] = expand(sub1[b] - known)
    print(f"  B_{m}^{{(1)}} = {B1[m]}")

# Verify uniform sign (-1)^{x_1 + x_3} in B_m^{(1)}
print("\n=== Sign check on B_m^{(1)} ===")
for m in range(1, NMAX + 1):
    if B1[m] == 0:
        continue
    p = Poly(B1[m], E1, E2, E3)
    all_ok = True
    for monom, c in p.as_dict().items():
        i, j, k = monom
        s_pred = (-1) ** (i + k)
        s_act = 1 if c > 0 else -1
        if s_pred != s_act:
            print(f"  B_{m}^{{(1)}}: E1^{i} E2^{j} E3^{k} = {c}, expected sign {s_pred}")
            all_ok = False
    if all_ok:
        print(f"  B_{m}^{{(1)}}: uniform sign (-1)^{{x_1+x_3}} ✓")

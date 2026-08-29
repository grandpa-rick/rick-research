"""Verify boundary-column closed forms for Q_n:
  [Q_n at E_1^{n-3} E_3]     = (-1)^n     · (n-1)(n-2)(11n+15) / 12
  [Q_n at E_1^{n-4} E_2 E_3] = (-1)^{n+1} · (n-1)(n-2)(n-3)(5n+6) / (12 n)
  [Q_n at E_1^{n-5} E_3^2]   = (-1)^{n+1} · (n-1)(n-2)(n-3)(n-4)(7n^2+40n+30) / (360 n)
"""
import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day127')
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day128')

from lib import s, y, t, u1, u2, u3
from task1_psi_e2_b5_b6 import (Psi_direct, sym_to_ebasis_direct, e2_u,
                                 E1, E2, E3, weight_of_e_monom)
from sympy import (Poly, Integer, expand, symbols, Rational, factorial,
                    binomial, Symbol, factor, cancel)

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


NMAX = 8
tops = {0: Integer(1)}
sub1 = {0: Integer(0)}
for b in range(1, NMAX + 1):
    psi_u = Psi_direct(e2_u ** b)
    psi_e = sym_to_ebasis_direct(psi_u)
    tops[b] = weight_part(psi_e, b)
    sub1[b] = weight_part(psi_e, b - 1)

An_cache = {n: A_n(n) for n in range(NMAX + 1)}
An1_cache = {n: A_n_upper1(n) for n in range(NMAX + 1)}
Bm_cache = {m: B_m(m) for m in range(NMAX + 1)}

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

# Compute Q as series
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
    P = expand(P)
    p = Poly(P, E1, E2, E3)
    d = p.as_dict()
    return d.get((i, j, k), Integer(0))


print("=== Formula 1: [Q_n at E_1^{n-3} E_3] = (-1)^n (n-1)(n-2)(11n+15)/12 ===")
for n in range(3, NMAX + 1):
    actual = extract_coeff(Q[n], n - 3, 0, 1)
    predicted = Rational((-1) ** n * (n - 1) * (n - 2) * (11 * n + 15), 12)
    status = "✓" if actual == predicted else "✗"
    print(f"  n={n}: actual = {actual}, predicted = {predicted} {status}")

print("\n=== Formula 2: [Q_n at E_1^{n-4} E_2 E_3] = (-1)^{n+1} (n-1)(n-2)(n-3)(5n+6)/(12n) ===")
for n in range(4, NMAX + 1):
    actual = extract_coeff(Q[n], n - 4, 1, 1)
    predicted = Rational((-1) ** (n + 1) * (n - 1) * (n - 2) * (n - 3) * (5 * n + 6), 12 * n)
    status = "✓" if actual == predicted else "✗"
    print(f"  n={n}: actual = {actual}, predicted = {predicted} {status}")

print("\n=== Formula 3: [Q_n at E_1^{n-5} E_3^2] = (-1)^{n+1} (n-1)(n-2)(n-3)(n-4)(7n^2+40n+30)/(360n) ===")
for n in range(5, NMAX + 1):
    actual = extract_coeff(Q[n], n - 5, 0, 2)
    predicted = Rational((-1) ** (n + 1) * (n - 1) * (n - 2) * (n - 3) * (n - 4) * (7 * n * n + 40 * n + 30), 360 * n)
    status = "✓" if actual == predicted else "✗"
    print(f"  n={n}: actual = {actual}, predicted = {predicted} {status}")

"""Compute Q(T) = B^{(1)}(T)/B(T) and look for closed form.
Also verify the ansatz sub_1[b] = sum_{n+m=b} C(b,n)[A_n^{(1)} B_m + A_n B_m^{(1)}]
for b = 1..NMAX.
"""
import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day127')
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day128')

from lib import s, y, t, u1, u2, u3
from task1_psi_e2_b5_b6 import (Psi_direct, sym_to_ebasis_direct, e2_u,
                                 E1, E2, E3, weight_of_e_monom)
from sympy import (Poly, Integer, expand, symbols, Rational, factorial,
                    binomial, Symbol, factor, cancel, S, log, series)

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


# Fit B_m^{(1)} via ansatz
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


# Compute Q(T) = B^{(1)}/B as series
# B^{(1)}(T) = sum B_m^{(1)} T^m/m!
# B(T) = sum B_m T^m/m!
# Q(T) = B^{(1)}/B

# Coeffs: b1[m] = B_m^{(1)}/m!  ; b0[m] = B_m/m!
b1 = {m: expand(B1[m] / factorial(m)) for m in range(NMAX + 1)}
b0 = {m: expand(Bm_cache[m] / factorial(m)) for m in range(NMAX + 1)}

# Q_n such that (sum Q_n T^n) * (sum b0[m] T^m) = sum b1[k] T^k
Q = {}
for n in range(NMAX + 1):
    rhs = b1[n]
    for k in range(1, n + 1):
        rhs = expand(rhs - Q[n - k] * b0[k]) if n - k in Q else rhs
    # b0[0] = 1, so Q[n] = rhs
    Q[n] = rhs

print("=== Q(T) coefficients ===")
for n in range(NMAX + 1):
    if Q[n] != 0:
        try:
            f = factor(Q[n])
        except Exception:
            f = Q[n]
        print(f"  Q_{n} = {f}")


# Verify uniform sign of Q
print("\n=== Uniform sign check of Q(T) coefficients ===")
for n in range(NMAX + 1):
    if Q[n] == 0:
        continue
    p = Poly(Q[n], E1, E2, E3)
    all_ok = True
    for monom, c in p.as_dict().items():
        i, j, k = monom
        s_pred = (-1) ** (i + k)
        s_act = 1 if c > 0 else -1
        if s_pred != s_act:
            print(f"  Q_{n} SIGN MISMATCH: E1^{i} E2^{j} E3^{k} coeff={c}, expected sign {s_pred}")
            all_ok = False
    if all_ok:
        print(f"  Q_{n}: uniform sign (-1)^{{x1+x3}} ✓")


# Now verify: does the ansatz sub_1[b] = sum C(b,n)[A_n^{(1)} B_m + A_n B_m^{(1)}]
# for b = 1..NMAX?
print("\n=== Verify ansatz sub_1[b] = Σ C(b,n)[A_n^{(1)} B_m + A_n B_m^{(1)}] ===")
for b in range(1, NMAX + 1):
    total = Integer(0)
    for n in range(0, b + 1):
        m = b - n
        # A_0^{(1)} = 0 by convention
        A_n1 = An1_cache[n] if n >= 1 else Integer(0)
        Bm_1 = B1[m] if m >= 1 else Integer(0)
        # (n=0 gives A_0 * B_m^{(1)} = B_m^{(1)}; A_0^{(1)} = 0)
        total = expand(total + binomial(b, n) * (A_n1 * Bm_cache[m] + An_cache[n] * Bm_1))
    diff = expand(sub1[b] - total)
    print(f"  b={b}: diff = {diff}")

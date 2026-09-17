#!/usr/bin/env python3
"""
Day 187 sober re-verify of Day 186 conjecture:

  Z(z) := sum_{n>=1} X_{P_n}(q) z^n = H_-(z) / (1 - K(z))

equivalently, with F(z) = 1 + Z(z):

  F(z) * (1 - K(z)) = H(-q z)         (GF form)

equivalently, the recursion

  X_{P_n}(q) = sum_{k=1}^{n-1} (-1)^{k-1} [k+1]_q h_k X_{P_{n-k}}(q)
             + (-1)^{n-1} [n]_q h_n              (R)

Strategy: independent verification WITHOUT any h-basis conversion.
Both sides of (R) are expanded as polynomials in x_1,...,x_N and q
(with N large enough), then compared symbolically. This bypasses the
sub-agent's convert_m_to_basis code entirely.

We use the equivalent (cleaner) form:

  sum_{k=0}^n (-1)^{n-k} [n-k+1]_q h_{n-k} X_{P_k}(q) = (-1)^n q^n h_n   (star)

with X_{P_0} := 1.
"""
from sympy import symbols, expand, Integer, Poly, sympify, simplify
from itertools import product, combinations_with_replacement
from collections import defaultdict

def X_path_poly(n, xs, q):
    """
    Return X_{P_n}(x_1,...,x_N; q) as an expanded SymPy polynomial.
    X_{P_n}(q) := sum over c: [n] -> [N] with c_i != c_{i+1}
                    of q^{#{i: c_i < c_{i+1}}} prod x_{c_i}
    Uses transfer-matrix style summation:
       T_i = sum over c_i of x_{c_i} * q^{[prev < c_i]}
    Build sequence step by step.
    """
    N = len(xs)
    if n == 0:
        return Integer(1)
    # state: dict prev_color -> polynomial in xs and q
    state = {}
    for c in range(N):
        state[c] = xs[c]
    # transition: at each step, choose next color != prev, multiply x_col, add q if prev < col
    for step in range(1, n):
        new_state = {c: Integer(0) for c in range(N)}
        for prev, poly in state.items():
            for col in range(N):
                if col == prev:
                    continue
                weight = xs[col] * (q if prev < col else Integer(1))
                new_state[col] = new_state[col] + poly * weight
        # expand for tractability
        state = {c: expand(new_state[c]) for c in range(N)}
    return expand(sum(state.values()))


def h_k_poly(k, xs):
    """h_k = sum_{i_1 <= i_2 <= ... <= i_k} x_{i_1} ... x_{i_k}"""
    if k == 0:
        return Integer(1)
    total = Integer(0)
    for combo in combinations_with_replacement(range(len(xs)), k):
        term = Integer(1)
        for idx in combo:
            term *= xs[idx]
        total += term
    return expand(total)


def q_int(k, q):
    """[k]_q = 1 + q + q^2 + ... + q^{k-1}, with [0]_q = 0."""
    if k <= 0:
        return Integer(0)
    return sum(q**j for j in range(k))


def verify_R(n_max):
    q = symbols('q')
    for n in range(1, n_max + 1):
        # use N = n variables (sufficient because partitions of n have <= n parts)
        N = n
        xs = list(symbols(f'x1:{N+1}'))
        # Precompute X_{P_k} for k=0..n
        X = {0: Integer(1)}
        for k in range(1, n + 1):
            X[k] = X_path_poly(k, xs, q)
        # Precompute h_j for j=0..n
        h = {j: h_k_poly(j, xs) for j in range(n + 1)}
        # LHS of (star): sum_{k=0}^n (-1)^{n-k} [n-k+1]_q h_{n-k} X_k
        lhs = Integer(0)
        for k in range(n + 1):
            j = n - k
            lhs += (-1)**j * q_int(j + 1, q) * h[j] * X[k]
        lhs = expand(lhs)
        # RHS of (star): (-1)^n q^n h_n
        rhs = expand((-1)**n * q**n * h[n])
        diff = expand(lhs - rhs)
        status = "PASS" if diff == 0 else "FAIL"
        print(f"n={n}  (star) diff = {diff}  -> {status}")
        if diff != 0:
            # give some detail on failure
            print(f"  LHS - RHS as SymPy Poly:")
            print(f"  {diff}")
            return False
    return True


if __name__ == "__main__":
    ok = verify_R(8)
    print("\nAll checks passed!" if ok else "\nFAILURE.")

#!/usr/bin/env python3
"""
Day 187 Step 2: check that (R) at q=1 reduces to the classical GF

    F(z) = 1 + sum_{n>=1} X_{P_n}|_{q=1} z^n = E(z) / (E(z) - z E'(z))

by comparing X_{P_n}(1) computed directly against RHS-expansion.
"""
from sympy import symbols, expand, Integer, Poly, sympify, series
from itertools import product, combinations
from collections import defaultdict

def X_path_at_q1(n, xs):
    """X_{P_n}(1) = #proper colorings polynomial in xs."""
    N = len(xs)
    if n == 0:
        return Integer(1)
    state = {c: xs[c] for c in range(N)}
    for step in range(1, n):
        new_state = {c: Integer(0) for c in range(N)}
        for prev, poly in state.items():
            for col in range(N):
                if col == prev:
                    continue
                new_state[col] = new_state[col] + poly * xs[col]
        state = {c: expand(new_state[c]) for c in range(N)}
    return expand(sum(state.values()))


def e_k_poly(k, xs):
    if k == 0:
        return Integer(1)
    total = Integer(0)
    for combo in combinations(range(len(xs)), k):
        term = Integer(1)
        for idx in combo:
            term *= xs[idx]
        total += term
    return expand(total)


def main(n_max=5):
    # Use N = n_max variables
    N = n_max
    xs = list(symbols(f'x1:{N+1}'))
    # Compute E(z) truncated to degree n_max, and E - z E' truncated to same.
    z = symbols('z')
    Ez = Integer(1)
    for k in range(1, N + 1):
        Ez += e_k_poly(k, xs) * z**k
    zE_prime = Integer(0)
    for k in range(1, N + 1):
        zE_prime += k * e_k_poly(k, xs) * z**k
    denom = Ez - zE_prime  # = sum_k (1-k) e_k z^k
    # Compute F_pred = Ez / denom truncated to z^n_max.
    # Solve F_pred * denom = Ez modulo z^{n_max+1}
    Ez_coeffs = [Ez.coeff(z, k) for k in range(N + 1)]
    denom_coeffs = [denom.coeff(z, k) for k in range(N + 1)]
    # denom_coeffs[0] should be 1.
    F_coeffs = [Integer(0)] * (N + 1)
    F_coeffs[0] = Integer(1)  # F(0) = 1
    for n in range(1, N + 1):
        # E_n = sum_{k=0}^n F_k * denom_{n-k}
        s = Integer(0)
        for k in range(n):
            s += F_coeffs[k] * denom_coeffs[n - k]
        F_coeffs[n] = expand(Ez_coeffs[n] - s)  # since denom_0 = 1
    # Verify F_coeffs[n] == X_{P_n}(q=1) for n = 1..N
    print(f"Comparing F(z) = E(z)/(E(z) - z E'(z)) vs X_{{P_n}}(1) for n=1..{N}")
    for n in range(1, N + 1):
        X_direct = X_path_at_q1(n, xs)
        diff = expand(F_coeffs[n] - X_direct)
        status = "PASS" if diff == 0 else f"FAIL diff={diff}"
        print(f"  n={n}: {status}")


if __name__ == "__main__":
    main(5)

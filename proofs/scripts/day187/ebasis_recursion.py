#!/usr/bin/env python3
"""
Day 187 — clean e-basis form of the Day 186 recursion.

Starting from PROVE (R):
  X_n = sum_{k=1}^{n-1} (-1)^{k-1}[k+1]_q h_k X_{n-k}  +  (-1)^{n-1}[n]_q h_n

I derived (algebraic manipulation) the equivalent GF form
  F(z) [E(qz) - q E(z)] = (1 - q) E(z)

which after algebra becomes the POSITIVE e-basis recursion
  X_{P_n}(q) = e_n + q * sum_{k=2}^n [k-1]_q e_k X_{P_{n-k}}(q)       (Re)

Here we independently verify (Re) for n = 1..6 via direct polynomial
computation, and cross-verify the GF equation.
"""
from sympy import symbols, expand, Integer, series, sympify, factor
from itertools import product, combinations, combinations_with_replacement


def X_path_poly(n, xs, q):
    """X_{P_n}(x1,..,xN; q) via transfer matrix."""
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
                weight = xs[col] * (q if prev < col else Integer(1))
                new_state[col] = new_state[col] + poly * weight
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


def q_int(k, q):
    if k <= 0:
        return Integer(0)
    return sum(q**j for j in range(k))


def verify_ebasis_recursion(n_max):
    q = symbols('q')
    for n in range(1, n_max + 1):
        N = n
        xs = list(symbols(f'x1:{N+1}'))
        X = {0: Integer(1)}
        for k in range(1, n + 1):
            X[k] = X_path_poly(k, xs, q)
        e = {k: e_k_poly(k, xs) for k in range(n + 1)}
        # (Re): X_n = e_n + q * sum_{k=2}^n [k-1]_q e_k X_{n-k}
        rhs = e[n]
        for k in range(2, n + 1):
            rhs += q * q_int(k - 1, q) * e[k] * X[n - k]
        rhs = expand(rhs)
        diff = expand(X[n] - rhs)
        status = "PASS" if diff == 0 else "FAIL"
        print(f"n={n}  X_n - (e_n + q*sum [k-1]_q e_k X_{{n-k}}) = {diff}   -> {status}")
        if diff != 0:
            return False
    return True


def verify_gf_form(n_max):
    """Check F(z) [E(qz) - q E(z)] = (1-q) E(z) mod z^{n_max+1}."""
    q = symbols('q')
    z = symbols('z')
    # Use N = n_max variables
    N = n_max
    xs = list(symbols(f'x1:{N+1}'))
    # F(z) = 1 + sum X_{P_n}(q) z^n
    F_expr = Integer(1)
    for n in range(1, n_max + 1):
        F_expr += X_path_poly(n, xs, q) * z**n
    # E(z), E(qz)
    E_expr = Integer(1)
    Eqz_expr = Integer(1)
    for k in range(1, n_max + 1):
        ek = e_k_poly(k, xs)
        E_expr += ek * z**k
        Eqz_expr += ek * (q * z)**k
    # LHS = F(z) [E(qz) - q E(z)]
    lhs = expand(F_expr * (Eqz_expr - q * E_expr))
    rhs = expand((1 - q) * E_expr)
    diff = expand(lhs - rhs)
    # We only need it to hold mod z^{n_max+1}
    diff_poly = diff.as_poly(z)
    if diff_poly is None:
        print(f"GF diff = {diff}")
        return diff == 0
    truncated = Integer(0)
    for k in range(n_max + 1):
        c = diff.coeff(z, k)
        truncated += c * z**k
    truncated = expand(truncated)
    status = "PASS" if truncated == 0 else "FAIL"
    print(f"GF check F(z)[E(qz)-qE(z)] - (1-q)E(z) mod z^{n_max+1}: {truncated}  -> {status}")
    return truncated == 0


if __name__ == "__main__":
    print("=== e-basis positive recursion (Re) ===")
    ok1 = verify_ebasis_recursion(5)
    print()
    print("=== GF equation F(z)[E(qz) - qE(z)] = (1-q) E(z) ===")
    ok2 = verify_gf_form(5)
    print()
    print("ALL PASS" if (ok1 and ok2) else "FAILURE")

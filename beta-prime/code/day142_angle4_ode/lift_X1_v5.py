"""
Day 142 v5 — Given R_4 = 5 · X_1[T^2](U+1, V+1) exactly (a CONSTANT ratio),
this is a huge structural clue. Test:

    X_1[T^b] = base_b(U, V) + U·V · Σ_{k} c_{b, k} · X_1[T^{b-2-k}](U+1+k, V+1+k)
              or similar recursion.

Explore this.
"""

import sys
import os
import time
sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day140_interior')

from compute_P_fast import compute_P_at
from verify_gf_form import E3
from sympy import (symbols, expand, Integer, Rational, Poly, factorial,
                   rf, factor, diff, simplify, together, collect, S, solve, Matrix)

U, V = symbols('U V')
T = symbols('T')


def theta(P):
    return expand(T * diff(P, T))


def apply_L_UV(P):
    P1 = expand(V * P + theta(P))
    P2 = expand(U * P1 + theta(P1))
    P3 = expand(T * P2)
    return expand(P3 - theta(P))


def truncate_T(P, N):
    Pp = Poly(expand(P), T)
    out = Integer(0)
    for d in range(N + 1):
        out += Pp.coeff_monomial(T**d) * T**d
    return out


def build_FP(P_dict, B_max):
    F = Integer(0)
    for b in range(B_max + 1):
        F += P_dict[b] * T**b / factorial(b)
    return F


def one_over_series(f, N):
    fp = Poly(expand(f), T)
    a = {d: fp.coeff_monomial(T**d) for d in range(N + 1)}
    b = {0: Integer(1)}
    for n in range(1, N + 1):
        s = sum(a[k] * b[n - k] for k in range(1, n + 1))
        b[n] = expand(-s)
    return sum(b[d] * T**d for d in range(N + 1))


def compute_X1(B_MAX):
    P_uv = compute_P_at(U, V, B_MAX)
    FP = build_FP(P_uv, B_MAX)
    LFP = truncate_T(apply_L_UV(FP), B_MAX - 1)
    invFP = one_over_series(FP, B_MAX - 1)
    X = truncate_T(expand(LFP * invFP), B_MAX - 1)
    Xp = Poly(expand(X), E3)
    X1 = expand(Xp.coeff_monomial(E3**1))
    X1p = Poly(X1, T)
    return {b: expand(X1p.coeff_monomial(T**b)) for b in range(B_MAX)}


def base_ansatz(U_, V_, b):
    """Base ansatz:
       -(2b-1)[(U)_(b-2)+(V)_(b-2)] - (b-2)(b-1)(U+1)_(b-3)(V+1)_(b-3)/(b-3)!"""
    first = -(2*b - 1) * (rf(U_, b - 2) + rf(V_, b - 2))
    if b == 3:
        second = -(b - 2)*(b - 1) * Integer(1)
    else:
        second = -(b - 2)*(b - 1) * rf(U_ + 1, b - 3) * rf(V_ + 1, b - 3) / factorial(b - 3)
    return expand(first + second)


def try_recursion_sum(X1_dict, b_max):
    """
    Try: R_b = Σ_{k=0}^{K} c_{b,k} · X_1[T^{b-2-2k}](U+1+k, V+1+k)
    or similar. Solve for c_{b,k} for each b.
    """
    print("\n" + "=" * 70)
    print("Try:  R_b = Σ_k c_{b,k} · X_1[T^{b - 2k - 2}](U + k + 1, V + k + 1)")
    print("=" * 70)
    for b in range(4, b_max + 1):
        if b not in X1_dict:
            continue
        c = X1_dict[b]
        base = base_ansatz(U, V, b)
        residual = expand(c - base)
        R = expand(residual / (U * V)) if residual != 0 else Integer(0)

        # Possible basis terms: X_1[T^{b-2}](U+1, V+1),  X_1[T^{b-4}](U+2, V+2), ...
        basis_terms = []
        basis_names = []
        for k in range(0, (b - 2) // 2 + 1):
            bp = b - 2 - 2 * k
            if bp < 2:
                continue
            if bp not in X1_dict:
                continue
            term = X1_dict[bp].subs([(U, U + k + 1), (V, V + k + 1)], simultaneous=True)
            basis_terms.append(expand(term))
            basis_names.append(f"X_1[T^{bp}](U+{k+1}, V+{k+1})")

        # Try to express R as linear combination of basis_terms
        # Set up linear system:
        # For each monomial U^i V^j of R, coefficient equals sum over basis c_l · (coef of U^i V^j in basis_l)
        if not basis_terms:
            print(f"\n  b={b}: no basis terms available")
            continue

        # Collect all monomials
        polys = [Poly(t, U, V) for t in basis_terms]
        R_poly = Poly(R, U, V)
        all_monos = set(R_poly.monoms())
        for p in polys:
            all_monos.update(p.monoms())
        monos = sorted(all_monos)

        # Matrix: rows = monomials, cols = basis terms
        A = []
        b_vec = []
        for mono in monos:
            row = [p.coeff_monomial(mono) for p in polys]
            A.append(row)
            b_vec.append(R_poly.coeff_monomial(mono))
        M = Matrix(A)
        rhs = Matrix(b_vec)
        # Solve M · x = rhs
        try:
            aug = M.row_join(rhs)
            rref, pivots = aug.rref()
            # Check if consistent
            n_basis = len(basis_terms)
            # Last column would be inconsistent if the last-pivot column includes the RHS col
            # Simpler: try solve using pinv or solve
            xs = symbols('x0:{}'.format(n_basis))
            eqns = []
            for i in range(M.rows):
                lhs = sum(M[i, j] * xs[j] for j in range(n_basis))
                eqns.append(lhs - rhs[i])
            sol = solve(eqns, xs, dict=True)
            print(f"\n  b={b}: R_b as lin comb of basis {basis_names}")
            if not sol:
                print(f"    NO SOLUTION")
            else:
                s = sol[0]
                for i, name in enumerate(basis_names):
                    val = s.get(xs[i], xs[i])
                    print(f"    coef of {name} = {val}")
        except Exception as e:
            print(f"  b={b}: err {e}")


def try_simple_recursion(X1_dict, b_max):
    """Simpler test: solve for c_b in R_b = c_b · X_1[T^{b-2}](U+1, V+1) using RANK-1 basis."""
    print("\n" + "=" * 70)
    print("Test: R_b / X_1[T^{b-2}](U+1, V+1) — is it a constant?")
    print("=" * 70)
    for b in range(4, b_max + 1):
        if b not in X1_dict:
            continue
        c = X1_dict[b]
        base = base_ansatz(U, V, b)
        residual = expand(c - base)
        R = expand(residual / (U * V)) if residual != 0 else Integer(0)

        prev = X1_dict.get(b - 2, None)
        if prev is None:
            continue
        prev_shift = prev.subs([(U, U + 1), (V, V + 1)], simultaneous=True)
        prev_shift = expand(prev_shift)

        # Compute R / prev_shift; if constant, great.
        try:
            ratio = simplify(R / prev_shift)
            print(f"\n  b={b}: R_b / X_1[T^{b-2}](U+1, V+1) = {factor(ratio)}")
        except Exception as e:
            print(f"  b={b}: err {e}")


def try_diff_recursion(X1_dict, b_max):
    """
    Consider  R_b - c · X_1[T^{b-2}](U+1, V+1) — see if it has smaller degree.
    """
    print("\n" + "=" * 70)
    print("Subtract  R_b - λ · X_1[T^{b-2}](U+1, V+1) for best λ, see remainder.")
    print("=" * 70)
    for b in range(4, b_max + 1):
        if b not in X1_dict:
            continue
        c = X1_dict[b]
        base = base_ansatz(U, V, b)
        residual = expand(c - base)
        R = expand(residual / (U * V)) if residual != 0 else Integer(0)

        prev = X1_dict.get(b - 2, None)
        if prev is None:
            continue
        prev_shift = expand(prev.subs([(U, U + 1), (V, V + 1)], simultaneous=True))

        # Extract [top monomial of R] and [top monomial of prev_shift], form ratio for λ.
        Rp = Poly(R, U, V)
        Sp = Poly(prev_shift, U, V)
        # top monomial by total degree
        try:
            r_top = max(Rp.monoms(), key=lambda m: (sum(m), m))
            s_top = max(Sp.monoms(), key=lambda m: (sum(m), m))
            if r_top == s_top:
                lam = Rp.coeff_monomial(r_top) / Sp.coeff_monomial(s_top)
                # Actually, for R_4 example: R_4 = -15, top is (0, 0). X_1[T^2](U+1, V+1) = -3, top (0, 0).
                # λ = -15 / -3 = 5. And 5 was our earlier observation.
                # For b>=5, likely R_b top has (b-3, b-3), so λ = -(2b-3) / -(2b-5)... let's check.
                remainder = expand(R - lam * prev_shift)
                print(f"\n  b={b}: λ = {lam}, R_b - λ · prev_shift =")
                print(f"    = {factor(remainder)}")
                # Total degree
                if remainder != 0:
                    print(f"    total deg = {Poly(remainder, U, V).total_degree()}  (was {Poly(R, U, V).total_degree()})")
            else:
                print(f"\n  b={b}: top monos differ: R top = {r_top}, prev top = {s_top}")
        except Exception as e:
            print(f"  b={b}: err {e}")


def main():
    B_MAX = 9
    print(f"Computing X_1 up to T^{B_MAX-1}...")
    t0 = time.time()
    X1 = compute_X1(B_MAX)
    print(f"Done in {time.time()-t0:.1f}s")

    try_simple_recursion(X1, B_MAX - 1)
    try_diff_recursion(X1, B_MAX - 1)
    try_recursion_sum(X1, B_MAX - 1)


if __name__ == '__main__':
    main()

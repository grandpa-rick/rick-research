"""
Day 142 final push v2 — targeted ansatz for X_1(T; U, V).

DATA (from lift_X1.py):

X_1[T^b] for b = 2..8 as polynomials in (U, V).

Constants observed:
    [U^0 V^0] X_1[T^b] = -(b-1)!
    [U^{b-2} V^0] X_1[T^b] = -(2b-1)
    [U^0 V^{b-2}] X_1[T^b] = -(2b-1)  (by symmetry)
    Top total degree monomial [U^{b-2} V^{b-2}] = 0
    deg_U X_1[T^b] = b-2, deg_V X_1[T^b] = b-2
    Total degree of X_1[T^b] is 2b-3 (not 2(b-2) = 2b-4)

The V=0 slice factors as -(U+1)_{b-3}·((2b-1)U + (b-2)(b-1)).

Target ansatz candidates:

  (A) X_1[T^b] = -[(U+1)_{b-3}·(V+1)_{b-3}·((2b-1)(U+V)/2 + c(b)) + lower]
      i.e., product form with some extra polynomial correction.

  (B) X_1[T^b] = θ_T-like operator applied to log((U+1)_{b-2}(V+1)_{b-2}) style.

  (C) A(U, V, b) + A(V, U, b) form where A is small degree in V:
      X_1[T^b] = -[(U+1)_{b-3}·A(U,V,b) + (V+1)_{b-3}·A(V,U,b)]
      where A is symmetric in a specific sense with A(U, 0, b) = (2b-1)U + (b-2)(b-1).

For (C), the natural guess: A(U, V, b) = ((2b-1)U + (b-2)(b-1)) · g(V, b)
where g(0, b) = 1 and g is polynomial in V. Then

  X_1[T^b] = -[(U+1)_{b-3}((2b-1)U + (b-2)(b-1)) g(V,b) + sym] ?

We could try to fit g(V, b) as polynomial or rational.
"""

import sys
import os
import time
sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day140_interior')

from compute_P_fast import compute_P_at
from verify_gf_form import E3
from sympy import (symbols, expand, Integer, Rational, Poly, factorial,
                   rf, factor, diff, simplify, together, collect, S,
                   solve, groebner)

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
    if a[0] != 1:
        raise ValueError("bad const")
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


# ---------------------------------------------------------------
# Targeted ansatz fitting
# ---------------------------------------------------------------

def fit_C_ansatz(X1_dict, b):
    """Ansatz (C): X_1[T^b] = -[(U+1)_{b-3} A(U,V,b) + (V+1)_{b-3} A(V,U,b)]

    with A(U, V, b) polynomial in V of small degree, and
    A(U, 0, b) = (2b-1)U + (b-2)(b-1).

    Free structure: A(U, V, b) = (2b-1)U + (b-2)(b-1) + Σ_{k>=1} α_k(U, b) V^k.

    Total (U, V) degree of X_1[T^b] is 2b-3 (from data).
    (U+1)_{b-3} has deg U = b-3.  So A(U, V, b) has degree ≤ b - 3 + 1 = b-2? Let's check via top.

    Top: [U^{b-2}] X_1 = -(2b-1). LHS: [U^{b-2}] (U+1)_{b-3}·A(U,V,b) needs (U+1)_{b-3} contribution U^{b-3}·(top of A in U). Also (V+1)_{b-3}·A(V,U,b): needs contribution from A in U^{b-2}, but (V+1)_{b-3} has const term (b-3)! in V, and coefficient of U^{b-2} of A(V,U,b) contributes.

    So the two pieces mix. Set up the constraint:
      -[(U+1)_{b-3} A(U,V,b) + (V+1)_{b-3} A(V,U,b)] = X_1[T^b]
    with A general symmetric-conditioned polynomial. Solve for A(U, V, b).
    """
    if b < 3 or b not in X1_dict:
        return None
    c = X1_dict[b]

    # Try A(U, V, b) polynomial of specified degrees in (U, V).
    # deg_U A should give top: A has [U^1 V^0] = (2b-1), constant = (b-2)(b-1) at V=0.
    # For X_1[T^b] to have deg_U = b-2, deg_V = b-2, and (U+1)_{b-3} being U-degree b-3,
    # the U-degree of A must be 1 (to make first piece degree b-2 in U).
    # Then (V+1)_{b-3} · A(V, U, b): V+1 stuff has V-degree b-3, A(V,U,b) has V-degree 1 in first slot & U-degree in second slot.
    # If A is degree (1, d) in (U, V), then A(V, U, b) is degree (d, 1). Hmm let me think again.
    # Let A(U, V, b) as polynomial in U, V have deg_U = p, deg_V = q.
    # Then (U+1)_{b-3}·A has deg_U = b-3+p, deg_V = q.
    # And (V+1)_{b-3}·A(V,U,b) has deg_V = b-3+q  (since A(V,U,b) has deg_V = p), deg_U = q.
    # Total polynomial deg_U = max(b-3+p, q); needs to equal b-2, so max(b-3+p, q) = b-2.
    # If q <= b-2 (likely) and p = 1, we get deg_U = b-2. Good.
    # Symmetric constraint: total should be symmetric under U↔V.
    # deg_V constraint: max(q, b-3+p) = b-2 by symmetry.
    # So p = 1 works; q up to b-2.

    # Ansatz: A(U, V, b) = (α_0 + α_1 U) + Σ_{j=1..q} (β_{j,0} + β_{j,1} U) V^j
    # with:
    #   A(U, 0, b) = α_0 + α_1 U = (b-2)(b-1) + (2b-1) U
    #   → α_0 = (b-2)(b-1), α_1 = 2b-1
    q = b - 2  # max deg in V
    from sympy import symbols as syms
    beta_vars = []
    beta_syms = {}
    for j in range(1, q + 1):
        s0 = syms(f'b{j}0')
        s1 = syms(f'b{j}1')
        beta_syms[(j, 0)] = s0
        beta_syms[(j, 1)] = s1
        beta_vars.append(s0)
        beta_vars.append(s1)

    alpha_0 = (b - 2) * (b - 1)
    alpha_1 = 2 * b - 1
    A = alpha_0 + alpha_1 * U + sum(
        (beta_syms[(j, 0)] + beta_syms[(j, 1)] * U) * V**j
        for j in range(1, q + 1)
    )
    A_swap = A.subs([(U, V), (V, U)], simultaneous=True)
    pred = expand(-(rf(U + 1, b - 3) * A + rf(V + 1, b - 3) * A_swap))
    diff_poly = expand(pred - c)
    Dp = Poly(diff_poly, U, V)
    # coefficients of Dp are linear in beta_vars, solve.
    eqns = []
    for mono, coef in Dp.as_dict().items():
        eqns.append(coef)
    sol = solve(eqns, beta_vars, dict=True)
    return sol, A, A_swap


def show_A_solutions(X1_dict, b_max):
    print("\n" + "=" * 70)
    print("Solve for A(U, V, b) in ansatz (C):")
    print("  X_1[T^b] = -[(U+1)_{b-3} A(U,V,b) + (V+1)_{b-3} A(V,U,b)]")
    print("=" * 70)
    for b in range(3, b_max + 1):
        if b not in X1_dict:
            continue
        try:
            sol, A, A_swap = fit_C_ansatz(X1_dict, b)
            print(f"\n  b={b}:")
            if not sol:
                print(f"    NO SOLUTION — ansatz (C) FAILS")
                continue
            # Multiple solutions typical; substitute back to see if A becomes clean.
            s = sol[0]
            A_val = A.subs(s)
            A_swap_val = A_swap.subs(s)
            print(f"    ONE solution found; A(U, V, b) =")
            print(f"      = {factor(expand(A_val))}")
            # Number of free params:
            free_vars = [v for v in s if s[v] == v]
            print(f"    free params (undetermined): {len(free_vars)}")
            # Try to find the "minimal" (lowest degree in V) solution
            # by setting free params to zero.
            free_set = {v: 0 for v in s if s[v] == v}
            A_min = A.subs(s).subs(free_set)
            print(f"    Minimal A(U, V, b) = {factor(expand(A_min))}")
        except Exception as e:
            print(f"  b={b}: fit error: {e}")


# ---------------------------------------------------------------
# Alternative: try (U+1)_{b-3} A(U, V) + (V+1)_{b-3} A(V, U) with A of degree 1 in each of U, V
# ---------------------------------------------------------------

def fit_low_deg_A(X1_dict, b):
    """Restrict A(U, V, b) to bilinear + linear + constant: only 4 free params:
       A(U, V, b) = (2b-1) U + (b-2)(b-1) + β V + γ U V
    (with constraint α_0 = (b-2)(b-1), α_1 = 2b-1 fixed from V=0 slice)
    """
    if b < 3 or b not in X1_dict:
        return None
    c = X1_dict[b]
    from sympy import symbols as syms
    beta, gamma = syms('beta gamma')
    A = (2*b - 1) * U + (b - 2)*(b - 1) + beta * V + gamma * U * V
    A_swap = A.subs([(U, V), (V, U)], simultaneous=True)
    pred = expand(-(rf(U + 1, b - 3) * A + rf(V + 1, b - 3) * A_swap))
    diff_poly = expand(pred - c)
    Dp = Poly(diff_poly, U, V)
    eqns = list(Dp.as_dict().values())
    sol = solve(eqns, [beta, gamma], dict=True)
    return sol, A, A_swap


def try_low_deg_A(X1_dict, b_max):
    print("\n" + "=" * 70)
    print("Ansatz (C-low): A(U, V, b) = (2b-1)U + (b-2)(b-1) + β V + γ UV")
    print("=" * 70)
    for b in range(3, b_max + 1):
        if b not in X1_dict:
            continue
        result = fit_low_deg_A(X1_dict, b)
        if result is None:
            continue
        sol, A, A_swap = result
        print(f"\n  b={b}:")
        if not sol:
            print(f"    NO SOLUTION — ansatz fails at bilinear degree")
        else:
            for s in sol:
                print(f"    solution: {s}")


# ---------------------------------------------------------------
# Try structure: X_1[T^b] = -(2b-1) * [Sym product part] - (something with (b-1)! constant)
# ---------------------------------------------------------------

def try_double_rising(X1_dict, b_max):
    """Try:  X_1[T^b] = -Σ_{k=0}^{b-3} c_{b,k} · (U+1)_{b-3-k}(V+1)_{b-3-k} · h_k(U, V, b)"""
    print("\n" + "=" * 70)
    print("Ansatz (double): sum of shifted (U+1)_j(V+1)_j basis")
    print("=" * 70)

    # Simplest: try  X_1[T^b] = -[(U+1)_{b-3}(V+1)_{b-3} · P(b) + (U+1)_{b-3} · Q_1(b, U) + (V+1)_{b-3} · Q_1(b, V) + R(b) · ...]
    # where the last terms only give a symmetric residual.
    # Extract [top of U] from X_1[T^b]/(U+1)_{b-3} evaluated at V=0:
    # (V=0 slice already known = ((2b-1)U + (b-2)(b-1)).)

    # Try:  X_1[T^b] = -[(U+1)_{b-3}((2b-1)U + (b-2)(b-1)) · (1 + V/((b-2)(b-1))·???)
    # Just compute [T^b] X_1 / [(U+1)_{b-3}] as a polynomial in V.
    for b in range(3, b_max + 1):
        if b not in X1_dict:
            continue
        c = X1_dict[b]
        num = -c
        try:
            r = together(num / rf(U + 1, b - 3))
            rs = expand(simplify(r))
            print(f"\n  b={b}: -X_1[T^b] / (U+1)_{b-3}:")
            print(f"    = {rs}")
            # It's polynomial in V, rational in U? Let's see V-degree.
            try:
                rV = Poly(rs, V)
                print(f"    V-degree: {rV.degree()}")
                for k in range(rV.degree() + 1):
                    coef = expand(rV.coeff_monomial(V**k))
                    coefsimp = factor(coef)
                    print(f"    [V^{k}]: {coefsimp}")
            except Exception:
                print(f"    Not polynomial in V.")
        except Exception as e:
            print(f"  b={b}: err {e}")


# ---------------------------------------------------------------
# CRUCIAL: try full asymmetric ansatz split
# ---------------------------------------------------------------

def try_full_asymmetric_split(X1_dict, b_max):
    """
    X_1 symmetric under U ↔ V. Write X_1[T^b] = -[G(U, V, b) + G(V, U, b)]
    for SOME G. There are infinitely many G but we want a "natural" one.

    Natural G: G(U, V, b) = (U+1)_{b-3} · A(U, V, b), A polynomial in (U, V).
    Fit A. Determine dimensions.

    We already did this in fit_C_ansatz. But let's report the minimal-support solutions.
    """
    show_A_solutions(X1_dict, b_max)


# ---------------------------------------------------------------
# Try to see if there's a "θ-derivative of a natural expression"
# ---------------------------------------------------------------

def try_theta_derivative(X1_dict, b_max):
    """
    Idea: since X_1 comes from L·F_P / F_P and L has θ_T = T d/dT, maybe X_1[T^b] is
    the θ_T = b operator applied to a "nice" (U, V)-poly.

    Specifically, X = L·F_P/F_P and its E_3^1 part is X_1. F_P = f · exp(Σ N_k E_3^k).
    So log F_P differentiated in T gives φ + Σ E_3^k θ N_k / T = θ log F_P / T.

    L (f G) / (f G) = (Lf/f) + T((θG)² + θ²G + (U+V)θG + 2φ θG)/G - θG/G
                    = 0 + T[( θR)² + θ²R + (U+V + 2φ) θR ]/... wait
    L (fG)/(fG) = X.
    Extracting [E_3^1]: (θN_1)² doesn't contribute (that's E_3^2). So:
        X_1 = T·[θ²N_1 + (U + V + 2φ) θN_1] - θN_1
            = T·θ²N_1 + T(U + V + 2φ)·θN_1 - θN_1

    So X_1 involves N_1 and φ.  If we KNOW N_1(T; U, V), we get X_1 explicitly.
    Conversely, X_1 determines N_1 via a first-order linear ODE (in T).

    But we're trying to find X_1 first as a stepping stone to N_1... So this is circular
    unless we discover X_1 has an INTRINSIC closed form.
    """
    print("\n" + "=" * 70)
    print("Structural: X_1 = T·θ²N_1 + T(U+V+2φ)·θN_1 - θN_1")
    print("=" * 70)
    print("This is derivative to N_1. If N_1 has closed form, so does X_1.")


# ---------------------------------------------------------------
# main
# ---------------------------------------------------------------

def main():
    B_MAX = 9
    print(f"Computing X_1 up to T^{B_MAX-1}...")
    t0 = time.time()
    X1 = compute_X1(B_MAX)
    print(f"Done in {time.time()-t0:.1f}s")

    try_low_deg_A(X1, B_MAX - 1)
    try_double_rising(X1, B_MAX - 1)
    show_A_solutions(X1, B_MAX - 1)
    try_theta_derivative(X1, B_MAX - 1)


if __name__ == '__main__':
    main()

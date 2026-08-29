"""
Day 142 final push v3 — after ansatz (C) failed, try different splits.

Observations:
1. (V=0) slice = -(U+1)_{b-3} · [(2b-1) U + (b-2)(b-1)]
2. deg X_1[T^b] in each of U, V is b-2; total deg is 2b-3.
3. Top coeffs:
     [U^{b-2}] X_1[T^b] = -(2b-1)
     [U^0] X_1[T^b]     = -(b-1)!
     [U^{b-2} V^0] · [U^0 V^{b-2}] both = -(2b-1)
4. Naive symmetrization ansatz -[(U+1)_{b-3}A + sym] fails.

NEW IDEA: Note the structural identity from cumulants:
    X_1 = T·θ²N_1 + T·(U+V+2φ)·θN_1 - θN_1

If we KNEW N_1(T; U, V) as sym poly, X_1 would follow. Conversely, we
seek X_1 in closed form to give an ODE for N_1.

BETTER: look at the RATIO -X_1[T^b] / [(U+1)_{b-3}(V+1)_{b-3}]. Data shows
it's a rational function whose numerator equals X_1[T^b] itself (up to sign).
Hard to close.

MORE PROMISING IDEA:
Since X_1 = L·F_P/F_P at [E_3^1], and L is a differential operator in T,
X_1 comes from a specific combination.  F_P has a hypergeometric structure.

Look at the following: at V=0, F_P |_(V=0) might simplify (since some U_b vanish).
Actually P_b(U, V=0, E_3) — is there a closed form?

Alternative: check whether X_1[T^b] = -(2b-1) H_b(U, V) - (b-2)(b-1) K_b(U, V) - ...
i.e., decompose along COEFFICIENT-of-(2b-1) and coefficient-of-((b-2)(b-1)) etc.

Look at (V=0) formula: -(U+1)_{b-3}·[(2b-1)U + (b-2)(b-1)]
                     = -(2b-1) · U·(U+1)_{b-3} - (b-2)(b-1)·(U+1)_{b-3}
                     = -(2b-1) · (U)_{b-2}  - (b-2)(b-1) · (U+1)_{b-3}
(since U·(U+1)(U+2)...(U+b-4) = (U)_{b-2}).

So (V=0) form is:  -(2b-1) (U)_{b-2}  -  (b-2)(b-1) (U+1)_{b-3}.

Try symmetrization of each piece:
  -(2b-1) [(U)_{b-2}·f_1(V) + (V)_{b-2}·f_1(U)] - (b-2)(b-1) [(U+1)_{b-3} f_2(V) + (V+1)_{b-3} f_2(U)]

with f_1(0) = 1/2 or f_1(0) = 1 for the piece to match V=0.

Actually, cleaner: try X_1[T^b] = -(2b-1) M_b(U, V) - (b-2)(b-1) N_b(U, V)
where M_b, N_b are symmetric polynomials with M_b(U, 0) = (U)_{b-2} and N_b(U, 0) = (U+1)_{b-3}.

Then fit M_b and N_b separately.
"""

import sys
import os
import time
sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day140_interior')

from compute_P_fast import compute_P_at
from verify_gf_form import E3
from sympy import (symbols, expand, Integer, Rational, Poly, factorial,
                   rf, factor, diff, simplify, together, collect, S, solve,
                   binomial)

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


def falling_pochhammer(x, n):
    """(x)_n = x(x+1)...(x+n-1), rising factorial."""
    return rf(x, n)


# ---------------------------------------------------------------
# NEW: try (U)_{b-2} · (V+1)_? style splits
# ---------------------------------------------------------------

def check_double_pochhammer(X1_dict, b_max):
    """
    Ansatz:  X_1[T^b] = -[(2b-1) M_b(U,V) + (b-2)(b-1) N_b(U,V)]
    with M_b(U, 0) = (U)_{b-2}, N_b(U, 0) = (U+1)_{b-3}.
    Try natural M_b, N_b:
      M_b(U, V) = symmetric extension of (U)_{b-2}
      N_b(U, V) = symmetric extension of (U+1)_{b-3}
    """
    print("\n" + "=" * 70)
    print("Ansatz: X_1[T^b] = -(2b-1) M_b(U,V) - (b-2)(b-1) N_b(U,V)")
    print("with M_b(U,0) = (U)_(b-2), N_b(U,0) = (U+1)_(b-3)")
    print("=" * 70)

    # Natural first attempt:
    # M_b(U, V) := (1/2) [(U)_(b-2) + (V)_(b-2)]  (symmetric additive)
    # N_b(U, V) := (1/2) [(U+1)_(b-3) + (V+1)_(b-3)]

    # At V=0: M_b = (1/2)[(U)_(b-2) + 0] = (1/2)(U)_(b-2)  [wait, (V)_(b-2)|_(V=0) = 0 for b>=3]
    # Hmm, (V)_(b-2) at V=0 is V(V+1)...(V+b-3) at V=0 = 0. Good.
    # So M_b(U, 0) = (U)_(b-2)/2. NOT (U)_(b-2). Off by factor 2.
    # Just multiply by 2: use M_b = (U)_(b-2) + (V)_(b-2). Then M_b(U, 0) = (U)_(b-2) as required.

    # Similarly N_b(U, V) = ((U+1)_(b-3) + (V+1)_(b-3))/... no,
    # (V+1)_(b-3) at V=0 = (b-3)!.  N_b(U, 0) = (U+1)_(b-3) + (b-3)! ≠ (U+1)_(b-3).
    # So this naive additive doesn't work for N_b.

    # Try:
    #   M_b(U, V) = (U)_(b-2) + (V)_(b-2)  [additive, kills at V=0 correctly]
    #   N_b(U, V) = (U+1)_(b-3) · (V+1)_(b-3) / (b-3)!  [normalized product, at V=0 gives (U+1)_(b-3)]

    for b in range(3, b_max + 1):
        if b not in X1_dict:
            continue
        c = X1_dict[b]
        M = rf(U, b - 2) + rf(V, b - 2)
        if b == 3:
            N = Integer(1)  # (U+1)_0 (V+1)_0 / 0! = 1
        else:
            N = rf(U + 1, b - 3) * rf(V + 1, b - 3) / factorial(b - 3)
        pred = expand(-(2*b - 1) * M - (b - 2)*(b - 1) * N)
        residual = expand(c - pred)
        # Check V=0:
        res_V0 = expand(residual.subs(V, 0))
        print(f"\n  b={b}:")
        print(f"    residual factor: {factor(residual)}")
        print(f"    residual at V=0: {factor(res_V0)}")


def check_var_ansatz(X1_dict, b_max):
    """
    Try:  X_1[T^b] = -(2b-1) [(U)_(b-2)·g(V) + (V)_(b-2)·g(U)]
                     -(b-2)(b-1) [(U+1)_(b-3)·h(V) + (V+1)_(b-3)·h(U)]
    with g(0)=1 (so the V=0 slice gives -(2b-1)(U)_(b-2)·1 - ... nothing from second piece since (V)_(b-2)|_(V=0)=0)
    and matching h.

    Fit g, h as polynomials in V.
    """
    print("\n" + "=" * 70)
    print("Ansatz: -(2b-1)[(U)_(b-2)·g(V) + sym] -(b-2)(b-1)[(U+1)_(b-3)·h(V) + sym]")
    print("with g(0)=1, h(0)=1/2  (so V=0 recovers V=0 formula)")
    print("=" * 70)
    for b in range(3, b_max + 1):
        if b not in X1_dict:
            continue
        c = X1_dict[b]
        # Set up g(V) = 1 + Σ g_j V^j and h(V) = 1/2 + Σ h_j V^j
        q_g = b - 2  # degree in V
        q_h = b - 2
        g_vars = symbols(f'g1:{q_g + 1}')
        h_vars = symbols(f'h1:{q_h + 1}')
        g = Integer(1) + sum(g_vars[j] * V**(j + 1) for j in range(q_g))
        h = Rational(1, 2) + sum(h_vars[j] * V**(j + 1) for j in range(q_h))
        # V=0: -(2b-1)[(U)_(b-2)·1 + 0·g(U)] - (b-2)(b-1)[(U+1)_(b-3)·(1/2) + (b-3)!·h(U)]
        # This should equal -(U+1)_(b-3)·((2b-1)U + (b-2)(b-1))
        # i.e., -(2b-1)U(U+1)_(b-3) - (b-2)(b-1)(U+1)_(b-3)
        # LHS = -(2b-1)(U)_(b-2) - (b-2)(b-1)/2 · (U+1)_(b-3) - (b-2)(b-1)(b-3)!·h(U)
        # But (U)_(b-2) = U(U+1)_(b-3). So (2b-1)(U)_(b-2) = (2b-1)U(U+1)_(b-3). Good, matches.
        # For NULL residual at V=0:
        #   -(2b-1)U(U+1)_(b-3) - (b-2)(b-1)/2·(U+1)_(b-3) - (b-2)(b-1)(b-3)!·h(U)
        #   = -(2b-1)U(U+1)_(b-3) - (b-2)(b-1)(U+1)_(b-3)
        #   → -(b-2)(b-1)/2·(U+1)_(b-3) - (b-2)(b-1)(b-3)!·h(U) = -(b-2)(b-1)(U+1)_(b-3)
        #   → (b-2)(b-1)/2·(U+1)_(b-3) + (b-2)(b-1)(b-3)!·h(U) = (b-2)(b-1)(U+1)_(b-3)
        #   → h(U) = (1/2)(U+1)_(b-3)/(b-3)!

        # So h(U) is FORCED. That is, the ansatz with h(0)=1/2 forces:
        #   h(U) = (U+1)_(b-3) / (2·(b-3)!)  = binomial(U+b-3, b-3)/2 or similar.
        # So we can't freely choose h — it's determined.

        # Let's actually not fix h(0)=1/2. Set h(0) = h0 free. Then constraint
        # says the free params of h combine.

        # Simpler: use g(V) = 1 + Σ g_j V^j and h(V) generic polynomial (not fixing h(0)), fit both.
        h = sum(symbols(f'H{j}') * V**j for j in range(b - 1))
        h_vars = [symbols(f'H{j}') for j in range(b - 1)]
        g = Integer(1) + sum(symbols(f'G{j}') * V**j for j in range(1, b - 1))
        g_vars = [symbols(f'G{j}') for j in range(1, b - 1)]

        M = rf(U, b - 2) * g + rf(V, b - 2) * g.subs(V, U)
        N = rf(U + 1, b - 3) * h + rf(V + 1, b - 3) * h.subs(V, U)
        pred = expand(-(2*b - 1) * M - (b - 2)*(b - 1) * N)
        diff_poly = expand(pred - c)
        Dp = Poly(diff_poly, U, V)
        eqns = list(Dp.as_dict().values())
        all_vars = list(g_vars) + list(h_vars)
        sol = solve(eqns, all_vars, dict=True)
        print(f"\n  b={b}:")
        if not sol:
            print(f"    NO SOLUTION — this ansatz fails")
        else:
            s = sol[0]
            free_vars = [v for v in s if s[v] == v]
            print(f"    Solutions found. Free params: {len(free_vars)}")
            # Set free vars to 0 and print
            free_set = {v: 0 for v in s if s[v] == v}
            g_val = g.subs(s).subs(free_set)
            h_val = h.subs(s).subs(free_set)
            print(f"    g(V) = {factor(expand(g_val))}")
            print(f"    h(V) = {factor(expand(h_val))}")


def analyze_natural_h(X1_dict, b_max):
    """
    From the constraint derivation above:
    h(U) = (U+1)_(b-3)/(2(b-3)!) means h is a specific rational polynomial.
    Try:  h(V) = ((V+1)_(b-3) + something)/(2(b-3)!)
    Actually most natural: h(V) = 1/2 + terms of degree >= 1 in V.

    Just try:  g = h = 1 + V·(???)/((b-2)(b-1))
    """
    print("\n" + "=" * 70)
    print("Natural probe: try X_1[T^b] = -(1/(b-3)!) · [complete symmetric formula]")
    print("=" * 70)
    # Try: X_1[T^b] = -1/(b-3)! · symmetric-poly ((U+1)_(b-3) · (some sym combo) etc.)
    # Let's actually look at what M = -X_1[T^b] - (b-2)(b-1)/2·[(U+1)_(b-3)+(V+1)_(b-3)] gives
    for b in range(3, b_max + 1):
        if b not in X1_dict:
            continue
        c = X1_dict[b]
        # residual := c + (b-2)(b-1)/2·[(U+1)_(b-3) + (V+1)_(b-3)]
        residual = expand(c + Rational(b - 2, 1)*(b - 1)/2 * (rf(U + 1, b - 3) + rf(V + 1, b - 3)))
        # At V=0: residual = c|_(V=0) + (b-2)(b-1)/2·((U+1)_(b-3) + (b-3)!)
        # = -(U+1)_(b-3)·((2b-1)U + (b-2)(b-1)) + (b-2)(b-1)/2·(U+1)_(b-3) + (b-2)(b-1)/2·(b-3)!
        # = -(U+1)_(b-3)·[(2b-1)U + (b-2)(b-1) - (b-2)(b-1)/2] + (b-2)(b-1)/2·(b-3)!
        # = -(U+1)_(b-3)·[(2b-1)U + (b-2)(b-1)/2] + (b-2)(b-1)(b-3)!/2
        res_V0 = expand(residual.subs(V, 0))
        print(f"\n  b={b}: residual at V=0 = {factor(res_V0)}")


def try_universal_ansatz(X1_dict, b_max):
    """
    Try:  X_1[T^b] = -Σ_{i, j >= 0} c_{b, i, j} · (U+i+1)_{b-3-i} · (V+j+1)_{b-3-j}
    or similar rising-factorial basis.

    Simpler: look at X_1 in the basis {(U+i)_{b-3} : i=0..1} × {(V+j)_{b-3} : j=0..1}
    to see if it's a rank-1 or rank-2 tensor there.
    """
    print("\n" + "=" * 70)
    print("Tensor basis: {(U+i)_(b-3) for i=0..some} × {sym in V}")
    print("=" * 70)
    for b in range(3, b_max + 1):
        if b not in X1_dict:
            continue
        c = X1_dict[b]

        # Express X_1[T^b] = A(U)·B(V) + C(U)·D(V) where each is a polynomial.
        # Start by extracting [top of V]: coefficient is -(2b-1) (constant in U).
        # Extracting [const of V]: coefficient is -(U+1)_(b-3)·((2b-1)U + (b-2)(b-1)).
        # So X_1 has "rank" at most... let's see.

        # Try:  X_1[T^b] = -[(U+1)_(b-3) · P_1(V, b) + P_2(U, b) · (V+1)_(b-3)]/((U+1)_(b-3) at ???)
        # Actually simplest: express X_1 in the basis of (U+1)_(b-3) [as U-part] and (V+1)_(b-3) [as V-part].
        # Coefficient of (U+1)_(b-3) as an element of the (b-3)-dim U-poly space might not be well-defined.

        # Use rank-decomposition: view X_1[T^b] as a bilinear form in {1, U, U^2, ..., U^{b-2}} tensor {1, V, ..., V^{b-2}}.
        # Its rank as a matrix M_{i,j} tells us how many separable terms.
        deg_u = Poly(c, U).degree()
        deg_v = Poly(c, V).degree()
        Pp = Poly(c, U, V)
        from sympy import Matrix
        rows = []
        for i in range(deg_u + 1):
            row = []
            for j in range(deg_v + 1):
                row.append(Pp.coeff_monomial((i, j)))
            rows.append(row)
        M = Matrix(rows)
        rk = M.rank()
        print(f"\n  b={b}: rank of coeff matrix = {rk}  (dim {deg_u+1} x {deg_v+1})")


def main():
    B_MAX = 9
    print(f"Computing X_1 up to T^{B_MAX-1}...")
    t0 = time.time()
    X1 = compute_X1(B_MAX)
    print(f"Done in {time.time()-t0:.1f}s")

    check_double_pochhammer(X1, B_MAX - 1)
    check_var_ansatz(X1, B_MAX - 1)
    analyze_natural_h(X1, B_MAX - 1)
    try_universal_ansatz(X1, B_MAX - 1)


if __name__ == '__main__':
    main()

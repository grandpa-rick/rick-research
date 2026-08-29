"""
Day 142 v4 — the ansatz  X_1[T^b] = -(2b-1)[(U)_(b-2) + (V)_(b-2)]
                                    -(b-2)(b-1)(U+1)_(b-3)(V+1)_(b-3)/(b-3)!
                                    + U·V · R_b(U, V)
matches modulo a U·V-multiple residual R_b. Look at R_b for structure.

Also try:
   ANSATZ (D):  X_1[T^b] = Σ_{k} α_k(b) · [(U+1)_{b-3-k}(V+1)_{b-3-k} · (UV)^k / ((b-3-k)!)^?]

Also crucial: check whether X_1 has the form
   -Σ_{b} (special sequence) · (UV)^i · (elementary symmetric of degree j)
"""

import sys
import os
import time
sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day140_interior')

from compute_P_fast import compute_P_at
from verify_gf_form import E3
from sympy import (symbols, expand, Integer, Rational, Poly, factorial,
                   rf, factor, diff, simplify, together, collect, S, solve)

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


# =============================================================
# ANSATZ D: Try  X_1[T^b] = -Σ_{k>=0} A_{b,k} (UV)^k (U+1)_(b-3-k) (V+1)_(b-3-k) · [something]
#
# The idea: (UV)^k (U+1)_(b-3-k)(V+1)_(b-3-k) is a natural "level k" term.
# Its V=0 slice for k >= 1 is zero (has V factor), so ONLY the k=0 term
# contributes at V=0.  The V=0 slice constraint fully determines A_{b,0}.
#
# Then correct with k=1, 2, ... to fit the interior.
# =============================================================

def try_ansatz_D(X1_dict, b_max):
    print("\n" + "=" * 70)
    print("Ansatz D: X_1[T^b] = -Σ_k A_{b,k} · (UV)^k · (U+1)_(b-3-k)(V+1)_(b-3-k) · Q_{b,k}(U,V)")
    print("where the k=0 term is the (V=0) fit.")
    print("=" * 70)
    for b in range(3, b_max + 1):
        if b not in X1_dict:
            continue
        c = X1_dict[b]

        # k=0 term matched to V=0 formula:
        # -(U+1)_(b-3)·[(2b-1)U + (b-2)(b-1)]  in the U-variable.
        # But this is NOT symmetric. We need to symmetrize.
        # From v3: X_1[T^b] = -(2b-1)((U)_(b-2)+(V)_(b-2)) - (b-2)(b-1)(U+1)_(b-3)(V+1)_(b-3)/(b-3)! + UV·R
        # V=0 check: -(2b-1)((U)_(b-2)+0) - (b-2)(b-1)(U+1)_(b-3)·(b-3)!/(b-3)! = -(2b-1)(U)_(b-2) - (b-2)(b-1)(U+1)_(b-3)
        # And (U)_(b-2) = U·(U+1)_(b-3). So this equals -(U+1)_(b-3)·[(2b-1)U + (b-2)(b-1)]. MATCHES V=0.

        # Compute residual R_b(U, V):
        base = -(2*b - 1) * (rf(U, b - 2) + rf(V, b - 2))
        if b == 3:
            second = -(b - 2)*(b - 1) * Integer(1)  # (b-3)! = 1
        else:
            second = -(b - 2)*(b - 1) * rf(U + 1, b - 3) * rf(V + 1, b - 3) / factorial(b - 3)
        residual = expand(c - base - second)
        # Should be U·V·R_b:
        try:
            R = simplify(residual / (U * V))
            R = expand(R)
            print(f"\n  b={b}: residual = U·V · R_b, where R_b:")
            print(f"    = {factor(R)}")
            print(f"    total degree = {Poly(R, U, V).total_degree()}")
            # deg in U, V
            du = Poly(R, U).degree() if R != 0 else 0
            dv = Poly(R, V).degree() if R != 0 else 0
            print(f"    deg_U = {du}, deg_V = {dv}")

            # Try further decompositions of R_b
            R_at_V0 = expand(R.subs(V, 0))
            print(f"    R_b(U, 0) = {factor(R_at_V0)}")
        except Exception as e:
            print(f"  b={b}: err {e}")


def try_recursive_ansatz(X1_dict, b_max):
    """
    Try:  X_1[T^b] = -(2b-1)[(U)_(b-2)+(V)_(b-2)] -(b-2)(b-1)(U+1)_(b-3)(V+1)_(b-3)/(b-3)!
                     + UV · (-(2·(b-1)-1)[(U+1)_(b-3)+(V+1)_(b-3)] -(b-3)(b-2)(U+2)_(b-4)(V+2)_(b-4)/(b-4)!)/(b-2)?
    Wait, try a self-similar ansatz where the residual R_b is proportional to X_1[T^{b'}] for some smaller b'.
    """
    print("\n" + "=" * 70)
    print("Self-similar ansatz — check if R_b relates to X_1[T^{b-1}] or similar.")
    print("=" * 70)
    for b in range(4, b_max + 1):
        if b not in X1_dict:
            continue
        c = X1_dict[b]
        base = -(2*b - 1) * (rf(U, b - 2) + rf(V, b - 2))
        if b == 3:
            second = -(b - 2)*(b - 1) * Integer(1)
        else:
            second = -(b - 2)*(b - 1) * rf(U + 1, b - 3) * rf(V + 1, b - 3) / factorial(b - 3)
        residual = expand(c - base - second)
        R = expand(residual / (U * V)) if residual != 0 else Integer(0)

        # Compare R with a rescaling of X_1[T^{b-2}] (in (U+1, V+1) shift, etc.).
        if b - 2 in X1_dict:
            other = X1_dict[b - 2]
            # Try:  R = c_b · other(U+1, V+1) or similar
            other_shift = other.subs([(U, U + 1), (V, V + 1)], simultaneous=True)
            other_shift = expand(other_shift)
            # Try to find c so R - c · other_shift is 0 or simple
            try:
                ratio = simplify(R / other_shift)
                print(f"\n  b={b}: R_b / X_1[T^{b-2}](U+1, V+1) = {ratio}")
                # If constant, we win.
                if ratio.free_symbols == set():
                    print(f"    CONSTANT ratio! {ratio}")
            except Exception as e:
                print(f"  b={b}: shift ratio err {e}")


def analyze_R_pattern(X1_dict, b_max):
    """
    Look at R_b(U, 0) — the V=0 slice of the residual/(UV):
    b=5: R_5(U, 0) after /(UV)?  Wait UV vanishes at V=0. Better to just look at
    what R_b is as a symmetric polynomial.

    R_b is symmetric U↔V and has (U, V)-degree what?
    """
    print("\n" + "=" * 70)
    print("R_b structural analysis")
    print("=" * 70)
    for b in range(4, b_max + 1):
        if b not in X1_dict:
            continue
        c = X1_dict[b]
        base = -(2*b - 1) * (rf(U, b - 2) + rf(V, b - 2))
        if b == 3:
            second = -(b - 2)*(b - 1) * Integer(1)
        else:
            second = -(b - 2)*(b - 1) * rf(U + 1, b - 3) * rf(V + 1, b - 3) / factorial(b - 3)
        residual = expand(c - base - second)
        R = expand(residual / (U * V)) if residual != 0 else Integer(0)
        if R == 0:
            print(f"\n  b={b}: R_b = 0")
            continue
        # print monomial dump for R_b
        print(f"\n  b={b}: R_b as poly in (U, V):")
        Rp = Poly(R, U, V)
        for mono, coef in sorted(Rp.as_dict().items(), key=lambda kv: (sum(kv[0]), kv[0])):
            i, j = mono
            print(f"    U^{i} V^{j}: {coef}")


def try_multilevel_ansatz(X1_dict, b_max):
    """
    Try:  X_1[T^b] = -Σ_{k=0}^{b-3} λ_{b,k} · (UV)^k · [(U+k+1)_(b-3-k) + (V+k+1)_(b-3-k)] · μ_k(b)
                     + more.

    Or even more general — try to fit X_1 in the basis of monomials
    (UV)^k (U^i + V^i) for various k, i.
    """
    print("\n" + "=" * 70)
    print("Multilevel basis: (UV)^k · symmetric monomial")
    print("=" * 70)
    for b in range(3, b_max + 1):
        if b not in X1_dict:
            continue
        c = X1_dict[b]
        # Convert to (UV) and (U+V) basis via elementary sym polys.
        # e_1 = U + V, e_2 = U*V.  Any sym poly is in Z[e_1, e_2].
        e1 = symbols('e1')  # dummy
        e2 = symbols('e2')  # dummy
        # Direct: Poly in (U, V), then use e1 = U+V, e2 = UV.
        # sympy's symmetrize will do this.
        from sympy.polys.specialpolys import symmetric_poly
        from sympy import symmetrize
        # symmetrize returns (result, remainder, expansion_dict) — result in elementary basis
        try:
            res, remainder = symmetrize(c, [U, V], formal=False)
        except Exception:
            res, remainder = symmetrize(c, formal=False)
        print(f"\n  b={b}: X_1[T^b] in (e1, e2) elementary sym basis:")
        print(f"    {factor(res)}")
        if remainder != 0:
            print(f"    remainder: {remainder}")


def main():
    B_MAX = 9
    print(f"Computing X_1 up to T^{B_MAX-1}...")
    t0 = time.time()
    X1 = compute_X1(B_MAX)
    print(f"Done in {time.time()-t0:.1f}s")

    try_ansatz_D(X1, B_MAX - 1)
    analyze_R_pattern(X1, B_MAX - 1)
    try_recursive_ansatz(X1, B_MAX - 1)
    try_multilevel_ansatz(X1, B_MAX - 1)


if __name__ == '__main__':
    main()

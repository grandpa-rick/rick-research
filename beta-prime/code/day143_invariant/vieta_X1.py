"""Attack B — X_1[T^b] in Vieta variables α = U+V, β = UV.

Compute X_1[T^b] as symbolic polynomial in (U, V), then rewrite in (α, β).
Look for clean structure that eludes the (U, V) representation.
"""
import sys, os, time
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day140_interior')
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day142_angle4_ode')

from compute_P_fast import compute_P_at
from verify_gf_form import E3
from sympy import (symbols, expand, Integer, Rational, Poly, factorial,
                   rf, factor, diff, simplify, together, collect, S,
                   groebner, Matrix)

U, V = symbols('U V')
alpha, beta = symbols('alpha beta')
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


def compute_X1_full(B_MAX):
    P_uv = compute_P_at(U, V, B_MAX)
    FP = build_FP(P_uv, B_MAX)
    LFP = truncate_T(apply_L_UV(FP), B_MAX - 1)
    invFP = one_over_series(FP, B_MAX - 1)
    X = truncate_T(expand(LFP * invFP), B_MAX - 1)
    Xp = Poly(expand(X), E3)
    X1 = expand(Xp.coeff_monomial(E3**1))
    X1p = Poly(X1, T)
    return {b: expand(X1p.coeff_monomial(T**b)) for b in range(B_MAX)}


def to_vieta(poly_uv):
    """Rewrite symmetric polynomial in (U, V) as polynomial in (α, β)."""
    p = expand(poly_uv)
    # Substitute using U + V = α, U V = β. Iterate replacing power sums.
    # A cleaner way: use Groebner reduction, or express as poly in (U+V, UV) directly.
    # Approach: express in terms of U + V and U V by using:
    # U^k + V^k = p_k (Newton). Since the poly is symmetric, its (α, β) form is unique.
    #
    # Use symmetric reduction: keep replacing U^i V^j (with i <= j) by ...
    # Actually, we can use sympy's Symmetric-poly module. Let's directly:
    from sympy.polys.orderings import lex
    from sympy import symmetrize
    # symmetrize returns (sym_form, remainder, mapping)
    result = symmetrize(p, [U, V], formal=True)
    # result[0] is expression in e_1, e_2 symbols
    sym_expr, rem, mapping = result
    # mapping is [(e1, U+V), (e2, U*V)]
    e1_sym = mapping[0][0]
    e2_sym = mapping[1][0]
    sym_in_alpha_beta = sym_expr.subs([(e1_sym, alpha), (e2_sym, beta)])
    if rem != 0:
        print(f"    NON-SYMMETRIC REMAINDER: {rem}")
    return expand(sym_in_alpha_beta)


def main():
    B_MAX = 9
    print(f"Computing X_1 up to T^{B_MAX-1} as symbolic (U, V) polynomial...")
    t0 = time.time()
    X1 = compute_X1_full(B_MAX)
    print(f"Done in {time.time()-t0:.1f}s")

    print("\n=== X_1[T^b] in Vieta variables (α, β) ===")
    for b in sorted(X1):
        if X1[b] == 0:
            continue
        x_ab = to_vieta(X1[b])
        print(f"\n  X_1[T^{b}] =")
        # Group by degree in β
        x_ab_poly = Poly(x_ab, alpha, beta)
        # Print by beta degree
        for beta_deg in range(x_ab_poly.degree(beta) + 1):
            # Extract polynomial in alpha at this beta degree
            coeff_alpha = Integer(0)
            for mono, c in x_ab_poly.terms():
                if mono[1] == beta_deg:
                    coeff_alpha += c * alpha**mono[0]
            if coeff_alpha != 0:
                print(f"    β^{beta_deg} · ({factor(coeff_alpha)})")


if __name__ == '__main__':
    main()

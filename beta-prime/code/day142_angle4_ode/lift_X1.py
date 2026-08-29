"""
Day 142 final push — Lift X_1(T; V=0) closed form to full (U, V).

Prior result:
    X_1[T^b] |_{V=0}  =  -(U+1)_{b-3} · [(2b-1) U + (b-2)(b-1)]       (b >= 3)
    X_1[T^2]  =  -3

Goal: find X_1[T^b] as full symmetric (U, V)-polynomial.

Strategy:
  1. Compute X_1[T^b](U, V) explicitly for b = 3..8 by running
     analyze_LFPFP-style computation with full (U, V) polynomial coefficients.
  2. Try candidate closed forms:
      (a) X_1[T^b] = -(1/2) [(U+1)_{b-3} A(U,V,b) + (V+1)_{b-3} A(V,U,b)]
          with A(U, 0, b) = (2b-1)U + (b-2)(b-1).
      (b) X_1[T^b] = -(U+1)_{b-3}(V+1)_{b-3} Q(U,V,b) / R(U,V,b)
      (c) Sum over shifted rising factorial pairs.
  3. Blunt report: if none match, explain the obstruction.
"""

import sys
import os
import time
sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day140_interior')

from compute_P_fast import compute_P_at
from verify_gf_form import E3
from sympy import (symbols, expand, Integer, Rational, Poly, factorial,
                   rf, factor, diff, simplify, together, collect, S)

U, V = symbols('U V')
T = symbols('T')


def theta(P):
    return expand(T * diff(P, T))


def apply_L_UV(P):
    """L = T·(U + θ)(V + θ) - θ  with U, V symbolic."""
    P1 = expand(V * P + theta(P))
    P2 = expand(U * P1 + theta(P1))
    P3 = expand(T * P2)
    return expand(P3 - theta(P))


def truncate_T(P, N):
    Pp = Poly(expand(P), T)
    out = Integer(0)
    for d in range(N + 1):
        c = Pp.coeff_monomial(T**d)
        out += c * T**d
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
        raise ValueError(f"Series const term = {a[0]}")
    b = {0: Integer(1)}
    for n in range(1, N + 1):
        s = Integer(0)
        for k in range(1, n + 1):
            s += a[k] * b[n - k]
        b[n] = expand(-s)
    out = Integer(0)
    for d in range(N + 1):
        out += b[d] * T**d
    return out


def compute_X1_full(B_MAX):
    """Compute X_1[T^b](U, V) for b = 0..B_MAX-1 as full (U, V) polynomials.
    Returns dict {b: sympy polynomial in U, V}.
    """
    t0 = time.time()
    print(f"Building P_b in (U, V, E_3) up to b={B_MAX}")
    P_uv = compute_P_at(U, V, B_MAX)
    print(f"  built in {time.time()-t0:.1f}s")

    FP = build_FP(P_uv, B_MAX)
    print("Applying L to F_P (with U, V symbolic)...")
    t1 = time.time()
    LFP = truncate_T(apply_L_UV(FP), B_MAX - 1)
    print(f"  in {time.time()-t1:.1f}s")

    print("Computing 1/F_P...")
    t2 = time.time()
    invFP = one_over_series(FP, B_MAX - 1)
    print(f"  in {time.time()-t2:.1f}s")

    print("Computing X = L·F_P / F_P...")
    t3 = time.time()
    X = truncate_T(expand(LFP * invFP), B_MAX - 1)
    print(f"  in {time.time()-t3:.1f}s")

    Xp = Poly(expand(X), E3)
    X1 = expand(Xp.coeff_monomial(E3**1))
    print(f"Extracted [E_3^1] X: done in {time.time()-t0:.1f}s total")

    X1p = Poly(X1, T)
    result = {}
    for b in range(B_MAX):
        c = expand(X1p.coeff_monomial(T**b))
        result[b] = c
    return result


def print_X1_table(X1_dict):
    print("\n" + "=" * 70)
    print("X_1[T^b] as (U, V) polynomial")
    print("=" * 70)
    for b in sorted(X1_dict):
        c = X1_dict[b]
        if c == 0:
            continue
        print(f"\n[T^{b}]  X_1 =")
        print(f"    factored : {factor(c)}")
        print(f"    at V=0   : {factor(expand(c.subs(V, 0)))}")
        print(f"    at U=0   : {factor(expand(c.subs(U, 0)))}")
        print(f"    at U=V   : {factor(expand(c.subs(V, U)))}")


def check_V0_formula(X1_dict):
    """Confirm X_1[T^b]|_{V=0} = -(U+1)_{b-3} · [(2b-1) U + (b-2)(b-1)]."""
    print("\n" + "=" * 70)
    print("Check V=0 formula: -(U+1)_{b-3}·[(2b-1)U + (b-2)(b-1)]")
    print("=" * 70)
    for b in sorted(X1_dict):
        if b < 2:
            continue
        c = X1_dict[b]
        if c == 0:
            continue
        actual = expand(c.subs(V, 0))
        if b == 2:
            pred = Integer(-3)
        else:
            pred = expand(-rf(U + 1, b - 3) * ((2*b - 1) * U + (b - 2)*(b - 1)))
        diff = expand(actual - pred)
        status = "MATCH" if diff == 0 else f"FAIL diff={diff}"
        print(f"  b={b}: {status}")


# ---------------------------------------------------------------
# Candidate closed forms
# ---------------------------------------------------------------

def candidate_A_sym(b):
    """Ansatz (a): X_1[T^b] = -(1/2)·[(U+1)_{b-3}·A(U,V,b) + (V+1)_{b-3}·A(V,U,b)]
    with A(U, 0, b) = (2b-1)U + (b-2)(b-1).
    A most natural extension: A(U, V, b) = (2b-1)U + (b-2)(b-1) + (some V-terms).
    Free parameters in A up to appropriate degree in V, fit against actual data.
    """
    # This is a placeholder — we'll fit A(U, V, b) explicitly below.
    return None


def candidate_B_prod(b):
    """Ansatz (b): -(U+1)_{b-3}(V+1)_{b-3} · Q(U,V,b)/((b-3)!·something)"""
    return None


def try_ansatz_a_symmetrization(X1_dict, b_max):
    """Ansatz (a) — pure symmetrization of the V=0 factor.

    Try:  X_1[T^b] = -(1/2) [(U+1)_{b-3} · L(U,V,b) + (V+1)_{b-3} · L(V,U,b)]
    where L(U, V, b) = (2b-1)U + (b-2)(b-1) + (some V-linear terms).

    Simplest: try L(U, V, b) = (2b-1)U + (b-2)(b-1) [no V dependence].
    Then the sum is not symmetric in the correct way. Try instead pure
    symmetrization first, see what the residual looks like.
    """
    print("\n" + "=" * 70)
    print("Ansatz (a1): X_1[T^b] = -(1/2)·[(U+1)_{b-3}·A_0 + (V+1)_{b-3}·A_0(V→U)]")
    print("             where A_0(U, b) = (2b-1)U + (b-2)(b-1)  (NO V-terms)")
    print("=" * 70)
    for b in sorted(X1_dict):
        if b < 3:
            continue
        c = X1_dict[b]
        if c == 0:
            continue
        A0_U = (2*b - 1) * U + (b - 2)*(b - 1)
        A0_V = (2*b - 1) * V + (b - 2)*(b - 1)
        pred = expand(-Rational(1, 2) * (rf(U + 1, b - 3) * A0_U + rf(V + 1, b - 3) * A0_V))
        residual = expand(c - pred)
        status = "MATCH" if residual == 0 else "MISMATCH"
        print(f"\n  b={b}: {status}")
        if residual != 0:
            print(f"    residual (factored): {factor(residual)}")
            print(f"    residual at V=0    : {factor(expand(residual.subs(V, 0)))}")
            print(f"    residual degree U  : {Poly(residual, U).degree() if residual != 0 else 0}")
            print(f"    residual degree V  : {Poly(residual, V).degree() if residual != 0 else 0}")


def try_ansatz_a2_symmetrization(X1_dict, b_max):
    """Ansatz (a2): X_1[T^b] = -[(U+1)_{b-3}·A(U,V,b) + (V+1)_{b-3}·A(V,U,b)]/2
    but let A(U, V, b) have EXTRA V-dependence.

    We seek A(U, V, b) satisfying A(U, 0, b) = (2b-1)U + (b-2)(b-1).
    So write A(U, V, b) = (2b-1)U + (b-2)(b-1) + V · B(U, V, b)
    for some polynomial B.  Then attempt to fit B.

    For each b, the residual  X_1[T^b] - (V=0 symmetrization part)
    should equal -[V·(U+1)_{b-3}·B(U,V,b) + U·(V+1)_{b-3}·B(V,U,b)]/2.
    Compute residual, see its structure.
    """
    print("\n" + "=" * 70)
    print("Ansatz (a2): Extended A(U, V, b) with V-corrections")
    print("=" * 70)
    for b in sorted(X1_dict):
        if b < 3:
            continue
        c = X1_dict[b]
        if c == 0:
            continue
        A0_U = (2*b - 1) * U + (b - 2)*(b - 1)
        A0_V = (2*b - 1) * V + (b - 2)*(b - 1)
        base_pred = expand(-Rational(1, 2) * (rf(U + 1, b - 3) * A0_U + rf(V + 1, b - 3) * A0_V))
        residual = expand(c - base_pred)
        if residual == 0:
            print(f"\n  b={b}: full match with base (no V-correction needed)")
            continue
        print(f"\n  b={b}: residual  R_b = X_1[T^b] - base")
        print(f"    R_b (factored) = {factor(residual)}")

        # Try to divide residual by U*V (should vanish at V=0 and by symmetry at U=0)
        R_at_V0 = expand(residual.subs(V, 0))
        R_at_U0 = expand(residual.subs(U, 0))
        print(f"    R_b|_{{V=0}} = {R_at_V0}   (want 0)")
        print(f"    R_b|_{{U=0}} = {R_at_U0}   (want 0)")

        # If both zero, factor out UV
        if R_at_V0 == 0 and R_at_U0 == 0:
            try:
                q = simplify(residual / (U * V))
                print(f"    R_b / (U·V) = {factor(q)}")
            except Exception as e:
                print(f"    R_b / (U·V) error: {e}")


def try_ansatz_b_product(X1_dict, b_max):
    """Ansatz (b): X_1[T^b] = -(U+1)_{b-3}(V+1)_{b-3} · Q(U,V,b)/N_b."""
    print("\n" + "=" * 70)
    print("Ansatz (b): X_1[T^b] = -(U+1)_{b-3}(V+1)_{b-3} · Q(U,V,b) / (b-3)!")
    print("=" * 70)
    for b in sorted(X1_dict):
        if b < 3:
            continue
        c = X1_dict[b]
        if c == 0:
            continue
        prod = rf(U + 1, b - 3) * rf(V + 1, b - 3)
        try:
            Q = together(-c * factorial(b - 3) / prod)
            Qs = simplify(Q)
            print(f"  b={b}: -X_1[T^b] · (b-3)! / [(U+1)_{b-3}(V+1)_{b-3}]")
            # Check if Q is polynomial
            Qexp = expand(Qs)
            # Try to see if it factors
            print(f"    factored: {factor(Qs)}")
            # Show if polynomial in U, V
            try:
                Qp = Poly(Qexp, U, V)
                print(f"    IS polynomial in (U, V): degrees {Qp.degree_list()}")
            except Exception:
                print(f"    NOT polynomial in (U, V) — has denominators")
        except Exception as e:
            print(f"  b={b}: error {e}")


def try_ansatz_c_shifted(X1_dict, b_max):
    """Ansatz (c): sum of shifted rising factorial pairs.

    Given the (V=0) form has (U+1)_{b-3} multiplying a linear-in-U poly,
    try X_1[T^b] = -Σ_j α_j (U+j)_{p_j} (V+r_j)_{q_j}  with p_j+q_j = deg.
    """
    print("\n" + "=" * 70)
    print("Ansatz (c): Sum of shifted (U+j)_(p) (V+k)_(q)")
    print("           try each degree in U, V.")
    print("=" * 70)
    # For each b, we know:
    #   deg_U X_1[T^b] = ? (compute)
    #   deg_V X_1[T^b] = ? (compute)
    for b in sorted(X1_dict):
        if b < 3:
            continue
        c = X1_dict[b]
        if c == 0:
            continue
        Pp = Poly(c, U, V)
        du = Poly(c, U).degree()
        dv = Poly(c, V).degree()
        print(f"  b={b}: deg_U = {du}, deg_V = {dv}, total deg = {Pp.total_degree()}")


def analyze_ratio_to_V0_product(X1_dict, b_max):
    """Compute:
        X_1[T^b] / [-(U+1)_{b-3}·((2b-1)U + (b-2)(b-1))]
      and see if the result has V-structure."""
    print("\n" + "=" * 70)
    print("Ratio: X_1[T^b] / X_1[T^b]|_{V=0}    (want polynomial in V?)")
    print("=" * 70)
    for b in sorted(X1_dict):
        if b < 3:
            continue
        c = X1_dict[b]
        if c == 0:
            continue
        v0 = -rf(U + 1, b - 3) * ((2*b - 1) * U + (b - 2)*(b - 1))
        try:
            r = together(c / v0)
            rs = simplify(r)
            print(f"\n  b={b}: r = X_1[T^b] / (V=0 part)")
            print(f"    r (factored) = {factor(rs)}")
            print(f"    r at V = 0  = {expand(rs.subs(V, 0))}   (should be 1)")
            # r at particular V values
            for v in [1, 2]:
                print(f"    r at V = {v} = {factor(expand(rs.subs(V, v)))}")
        except Exception as e:
            print(f"  b={b}: err {e}")


def try_sym_2term_ansatz(X1_dict, b_max):
    """Try X_1[T^b] = -α_b·(U+1)_{b-3}(V+1)_{b-3} - β_b·[(U+1)_{b-3}·B_1(U,V) + sym]
    with all pieces polynomial in (U, V).

    First, extract leading coefficient a := [U^{b-2}] of X_1[T^b] which by V=0 formula is
    -(2b-1) [top of (U+1)_{b-3}] = -(2b-1).  Compute residual after this.
    """
    print("\n" + "=" * 70)
    print("Top monomial [U^{b-2}] X_1[T^b] and [V^{b-2}] X_1[T^b]")
    print("=" * 70)
    for b in sorted(X1_dict):
        if b < 3:
            continue
        c = X1_dict[b]
        if c == 0:
            continue
        Ppu = Poly(c, U)
        deg_u = Ppu.degree()
        top_U = Ppu.coeff_monomial(U**deg_u)
        Ppv = Poly(c, V)
        deg_v = Ppv.degree()
        top_V = Ppv.coeff_monomial(V**deg_v)
        # Extract [U^{b-2}]:
        Pp2 = Poly(c, U, V)
        # coefficient of U^{b-2}
        coef_Ubm2 = Pp2.coeff_monomial((b - 2, 0))
        coef_Vbm2 = Pp2.coeff_monomial((0, b - 2))
        # coefficient of U^{b-2} V^{b-2}
        coef_top_prod = Pp2.coeff_monomial((b - 2, b - 2))
        print(f"  b={b}: top U poly (in V) = {top_U}, top V poly (in U) = {top_V}")
        print(f"        [U^{b-2}] c = {coef_Ubm2}   (=-(2b-1)=-{2*b-1}?)")
        print(f"        [V^{b-2}] c = {coef_Vbm2}")
        print(f"        [U^{b-2} V^{b-2}] c = {coef_top_prod}   (should be 0 since deg <= b-2)")


def try_hypergeometric(X1_dict, b_max):
    """Try relating X_1[T^b] to a 2F0-like series.

    f = 2F0(U, V; ; T) = Σ_b (U)_b (V)_b T^b / b!.
    So (U)_b (V)_b = b! · [T^b] f.
    Note U_bracket = U(U+1)...(U+b-1) = (U)_b.

    X_1[T^b] at V=0 is -(U+1)_{b-3}·[(2b-1)U + (b-2)(b-1)].
    Note (U+1)_{b-3} = Γ(U+b-2)/Γ(U+1).
    Compare to (U)_{b-3} = U(U+1)...(U+b-4) = Γ(U+b-3)/Γ(U).
    Or (U+1)_{b-2} = (U+1)(U+2)...(U+b-2).
    """
    print("\n" + "=" * 70)
    print("Hypergeometric probe: compare to (U)_k (V)_k factors")
    print("=" * 70)
    for b in sorted(X1_dict):
        if b < 3:
            continue
        c = X1_dict[b]
        if c == 0:
            continue
        # Try X_1[T^b] / [(U)_{b-2} (V)_{b-2}] — probably fails since deg too low
        # Try X_1[T^b] / [(U+1)_{b-3} (V+1)_{b-3}]:
        num = -c
        denom = rf(U + 1, b - 3) * rf(V + 1, b - 3)
        try:
            r = simplify(num / denom)
            print(f"  b={b}: -X_1[T^b] / [(U+1)_{b-3}(V+1)_{b-3}] = {factor(r)}")
        except Exception as e:
            print(f"  b={b}: err {e}")


def try_generalized_ansatz(X1_dict, b_max):
    """
    Try ansatz:
       X_1[T^b] = -Σ_{i+j = b-2} α_{b,i,j} (U)_i (V)_j
    with symmetry α_{b,i,j} = α_{b,j,i}.  This is a symmetric bilinear
    expansion.  Fit α_{b,i,j} from data.
    """
    print("\n" + "=" * 70)
    print("Generalized ansatz: X_1[T^b] = -Σ_{i+j <= 2(b-2)} α_{b,i,j} (U)_i (V)_j")
    print("Fit coefficients directly for each b.")
    print("=" * 70)
    for b in sorted(X1_dict):
        if b < 3:
            continue
        c = X1_dict[b]
        if c == 0:
            continue
        # Expand X_1[T^b] in the basis {(U)_i (V)_j : i+j <= 2(b-2), i <= b-2, j <= b-2}
        # By previous experiments, deg_U <= b-2, deg_V <= b-2.
        # Use monomial basis first to gauge.
        Pp = Poly(c, U, V)
        deg_u = Poly(c, U).degree()
        deg_v = Poly(c, V).degree()
        print(f"\n  b={b}: deg_U = {deg_u}, deg_V = {deg_v}")

        # Convert to (U)_i (V)_j basis: use fact that
        #   (U)_0 = 1, (U)_1 = U, (U)_2 = U^2+U, (U)_3 = U^3+3U^2+2U, ...
        # We invert: express X_1 in this basis and see if simpler.
        # Substitute U → x, V → y, then expand in rising factorials via manual inversion.
        # Use sympy's stirling numbers of the first kind or just direct inversion.

        # Get coefficient of monomial U^i V^j
        mono_coefs = {}
        for i in range(deg_u + 1):
            for j in range(deg_v + 1):
                cc = Pp.coeff_monomial((i, j))
                if cc != 0:
                    mono_coefs[(i, j)] = cc

        # Rising factorial (U)_i as polynomial in U:
        # (U)_i = U(U+1)(U+2)...(U+i-1), unsigned Stirling number of first kind expansion
        from sympy.functions.combinatorial.numbers import stirling
        # (U)_i = Σ_k s(i, k) U^k where s = unsigned Stirling 1st kind
        # But we want the INVERSE: monomial → rising factorial basis.
        # Stirling 2nd kind gives x^n = Σ_k S(n,k) (x)_k (falling factorial).
        # For rising factorial, use x^n = Σ_k (-1)^(n-k) S(n,k) (x)_k^rising with sign? Not clean.
        # Just skip this and try candidates directly.
        pass


def try_multi_shifted(X1_dict, b_max):
    """
    Try ansatz:
       X_1[T^b] = -[(U+1)_{b-3} · a_b(U, V) + (V+1)_{b-3} · a_b(V, U) + (U V) part]
    where a_b(U, V) = c_1(b) U + c_2(b) V + c_3(b).
    """
    print("\n" + "=" * 70)
    print("Ansatz: X_1[T^b] = -[(U+1)_{b-3}·(αU + βV + γ) + (V+1)_{b-3}·(αV + βU + γ)]")
    print("with (α, β, γ) fit per b so V=0 gives (2b-1)U + (b-2)(b-1).")
    print("=" * 70)
    # V = 0: -[(U+1)_{b-3}·(αU + γ) + (b-3)!·(βU + γ)]
    # We want this to equal -(U+1)_{b-3}·[(2b-1)U + (b-2)(b-1)]
    # So we need (U+1)_{b-3}·(αU + γ) + (b-3)!·(βU + γ) = (U+1)_{b-3}·[(2b-1)U + (b-2)(b-1)]
    # This forces α = 2b-1 and γ = (b-2)(b-1), and then β = 0 gives back the (V=0) form
    # but leaves the (b-3)! contribution unbalanced... actually if we insist
    # (b-3)!·(βU + γ) must be absorbed into a corrected leading part.
    # Simplest: try α = 2b-1, γ = (b-2)(b-1), β = 0, and see residual.

    for b in sorted(X1_dict):
        if b < 3:
            continue
        c = X1_dict[b]
        if c == 0:
            continue
        alpha_ = (2*b - 1)
        gamma_ = (b - 2)*(b - 1)
        # (U+1)_{b-3} at V=0 = (b-3)! ??? No, (U+1)_{b-3}|_{U symbolic} keeps depending on U.
        # But (V+1)_{b-3} at V=0 = (b-3)!. So the second term contributes (b-3)!·(αV + βU + γ) at V=0.
        # For V=0 to match: -(U+1)_{b-3}·(αU + γ) - (b-3)!·(βU + γ) = -(U+1)_{b-3}·((2b-1)U + (b-2)(b-1))
        # → (U+1)_{b-3}·(αU + γ) + (b-3)!·(βU + γ) = (U+1)_{b-3}·((2b-1)U + (b-2)(b-1))
        # If we insist the RHS also has an "extra" that mirrors, we need β chosen so
        # (b-3)!·(βU + γ) doesn't disrupt. But (U+1)_{b-3} = (U+1)(U+2)...(U+b-3) → constant term (b-3)!.
        # So its constant-in-U term IS (b-3)!. The extra (b-3)!·(βU + γ) shifts:
        # If β = 0, γ arbitrary: (U+1)_{b-3}·(αU + γ) + (b-3)!·γ
        # = (U+1)_{b-3}·αU + γ·[(U+1)_{b-3} + (b-3)!]
        # Not matching unless we choose γ carefully.

        # Just do the direct symmetric test:
        AUV = alpha_ * U + gamma_  # No V-linear term in first piece
        AVU = alpha_ * V + gamma_
        pred = expand(-(rf(U + 1, b - 3) * AUV + rf(V + 1, b - 3) * AVU))
        residual = expand(c - pred)
        # Check V=0:
        res_V0 = expand(residual.subs(V, 0))
        print(f"\n  b={b}:")
        print(f"    pred at V=0    : {factor(expand(pred.subs(V, 0)))}")
        print(f"    actual at V=0  : {factor(expand(c.subs(V, 0)))}")
        print(f"    residual factor: {factor(residual)}")
        print(f"    residual at V=0: {factor(res_V0)}")


def fit_general_form(X1_dict, b, verbose=True):
    """For a given b, fit
       X_1[T^b] = -Σ_{i, j >= 0, i+j <= b-2} c_{i,j} (U)_i (V)_j
    with c_{i,j} = c_{j,i}.

    But (U)_i (V)_j basis is redundant beyond degree; we use monomials
    U^i V^j directly and print the sparse coefficient matrix.
    """
    if b not in X1_dict or X1_dict[b] == 0:
        return
    c = X1_dict[b]
    Pp = Poly(c, U, V)
    deg_u = Poly(c, U).degree()
    deg_v = Poly(c, V).degree()
    coefs = {}
    for i in range(deg_u + 1):
        for j in range(deg_v + 1):
            cc = Pp.coeff_monomial((i, j))
            if cc != 0:
                coefs[(i, j)] = cc
    if verbose:
        print(f"\n  b={b}: nonzero (U^i V^j) coefficients of X_1[T^b] (symmetric i↔j):")
        for (i, j), cc in sorted(coefs.items()):
            print(f"    U^{i} V^{j}: {cc}")
    return coefs


def factor_out_rising(X1_dict, b_max):
    """Try:
       X_1[T^b] = -Σ_{k=0}^{b-3} c_k(b) · (U+k+1)_{b-3-k} · (V+1)_{b-3-k}·???
    or the like.

    Alternative: try X_1[T^b] as -(1/(b-2)) · (grand thing symmetric).
    """
    pass


def try_matrix_ansatz(X1_dict, b_max):
    """
    Try:  X_1[T^b] = -Σ_{k=0}^{b-3} A_k(b) · (U+1)_k (V+1)_k · [something (b, k)-dependent]

    Where (U+1)_k (V+1)_k has degree k in each of U, V, so we can express any symmetric
    poly of bidegree (b-2, b-2) as linear combinations if we go up to k=b-2 and multiply
    by remaining stuff.
    """
    print("\n" + "=" * 70)
    print("Matrix ansatz: expand X_1[T^b] in basis (U+1)_k (V+1)_k · s_l(U, V)")
    print("where s_l is elementary symmetric of degree l.")
    print("=" * 70)
    for b in sorted(X1_dict):
        if b < 3:
            continue
        c = X1_dict[b]
        if c == 0:
            continue
        deg_u = Poly(c, U).degree()
        # (U+1)_k (V+1)_k has (bi)degree (k, k)
        # X_1 has degrees (b-2, b-2), so we need k up to b-2.
        # Coeffs are functions of the symmetric part.
        # Just decompose.
        print(f"\n  b={b}:")
        remaining = expand(c)
        # For k = b-2, b-3, ..., 0:
        for k in range(b - 2, -1, -1):
            basis = expand(rf(U + 1, k) * rf(V + 1, k))
            # Extract [U^{k} V^{k}] top coefficient of `remaining`
            Pp = Poly(remaining, U, V)
            top = Pp.coeff_monomial((k, k))
            # Try to subtract top × basis but this doesn't kill it exactly...
            # Instead, just print top coefficients.
            if top != 0:
                print(f"    [U^{k} V^{k}] remaining = {top}")


def main():
    B_MAX = 9  # yields X_1 up to T^8, which is what we want
    X1 = compute_X1_full(B_MAX)

    print_X1_table(X1)
    check_V0_formula(X1)

    try_ansatz_a_symmetrization(X1, B_MAX)
    try_ansatz_a2_symmetrization(X1, B_MAX)
    try_ansatz_b_product(X1, B_MAX)
    try_multi_shifted(X1, B_MAX)
    try_sym_2term_ansatz(X1, B_MAX)
    analyze_ratio_to_V0_product(X1, B_MAX)
    try_hypergeometric(X1, B_MAX)

    print("\n" + "=" * 70)
    print("Per-b coefficient dumps (for closed-form guessing)")
    print("=" * 70)
    for b in sorted(X1):
        if b >= 3:
            fit_general_form(X1, b)


if __name__ == '__main__':
    main()

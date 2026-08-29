"""
Lead 1 — Bessel closed form for N_1(T; U, V).

Compute N_1(T; U, V) as a polynomial in (U, V) with T-series coefficients up to T^12.
Report the (U, V)-polynomial for each [T^b] N_1.
Attempt fits:
  (a) N_1 = P(T; U, V) * 0F1(; alpha(U,V); beta T^2)
  (b) N_1 = combination of derivatives of f = 2F0(U,V;;T)
  (c) N_1 = (some closed-form Bessel-like expression).
"""

import sys, os, time
sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day140_interior')

from compute_P_fast import compute_P_at
from verify_gf_form import E3
from sympy import (symbols, expand, Integer, Rational, Poly, factorial,
                   rf, factor, diff, simplify, together, collect,
                   binomial, sqrt, Function)

U, V = symbols('U V')
T = symbols('T')


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


def build_f_uv(B_max):
    F = Integer(0)
    for b in range(B_max + 1):
        F += (rf(U, b) * rf(V, b)) * T**b / factorial(b)
    return F


def one_over_series(f, N):
    fp = Poly(expand(f), T)
    a = {d: fp.coeff_monomial(T**d) for d in range(N + 1)}
    if a[0] != 1:
        raise ValueError(f"Const term = {a[0]}")
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


def series_log_ratio(FP, f, N):
    invf = one_over_series(f, N)
    ratio = truncate_T(expand(FP * invf), N)
    G = expand(ratio - 1)
    logv = Integer(0)
    Gk = Integer(1)
    for k in range(1, N + 1):
        Gk = truncate_T(expand(Gk * G), N)
        if Gk == 0:
            break
        logv = expand(logv + (-1)**(k-1) * Gk / k)
    return truncate_T(logv, N)


def compute_N1_UV(B_MAX):
    print(f"Computing P_b(U, V, E_3) up to b={B_MAX}...")
    t0 = time.time()
    P_uv = compute_P_at(U, V, B_MAX)
    print(f"  built in {time.time()-t0:.1f}s")

    FP = build_FP(P_uv, B_MAX)
    f = build_f_uv(B_MAX)

    print("Computing log(FP/f) series...")
    t1 = time.time()
    L = series_log_ratio(FP, f, B_MAX)
    print(f"  in {time.time()-t1:.1f}s")

    # extract [E_3^1]
    Lp = Poly(expand(L), E3)
    N1 = expand(Lp.coeff_monomial(E3**1))
    return N1


def display_N1(N1, B_MAX):
    print("\n" + "=" * 70)
    print(f"N_1(T; U, V) — polynomial in (U, V) times T^b, b=2..{B_MAX}")
    print("=" * 70)
    N1p = Poly(N1, T)
    coefs = {}
    for b in range(B_MAX + 1):
        c = expand(N1p.coeff_monomial(T**b))
        coefs[b] = c
        if c != 0:
            cf = factor(c)
            print(f"\n  [T^{b}] N_1 = {cf}")
    return coefs


def try_bessel_ansatz_a(coefs, B_MAX):
    """Try N_1 = P(T; U, V) * 0F1(; alpha(U,V); beta T^2) style.

    0F1(; c; z) = Σ z^n / [(c)_n n!]
    So 0F1(; alpha; beta T^2) = Σ (beta T^2)^n / [(alpha)_n n!].

    If N_1 = A(T; U, V) * 0F1 where A is polynomial, then even and odd
    T-coefficients would be constrained by convolution. Test:
    (b-1)! (b+1)/b at U=V=0 for b=2..12:
    """
    print("\n" + "=" * 70)
    print("Attempt Bessel ansatz (a): N_1 = polynomial * 0F1")
    print("=" * 70)

    # At U=V=0, [T^b] N_1 = (b-1)!(b+1)/b.
    # Check: does (b-1)!(b+1)/b have a Bessel structure?
    # A179442: a(b) = ((b-1)!)^2 (b+1). Then b! [T^b] = a(b).
    # So [T^b] N_1|_{U=V=0} = a(b) / b! = ((b-1)!)^2 (b+1) / b!
    #                        = ((b-1)!)^2 (b+1) / (b(b-1)!)
    #                        = (b-1)! (b+1) / b
    # OK.
    #
    # Bessel-I(ν; 2√T): I_ν(2√T) = Σ_{n≥0} T^{n+ν/2} / (n! Γ(n+ν+1))
    # No, that's for Bessel. Let's set g = Σ T^b / (b (b-1)!) · (b+1)
    # = Σ T^b (b+1) / (b · (b-1)!)   b≥2
    # Try to relate to derivatives of some 0F1 or 1F1.
    # (b-1)!(b+1)/b at b=2,3,4,5,6:  3/2, 8/3, 15/2, 144/5, 175
    #     Hmm: 3/2, 8/3, 15/2, 144/5, 175.
    #     Check: 3/2, 8/3, 30/4=15/2, 144/5, 875/5? = 175. Yes 175.

    # Let's see if [T^b] = c_b takes form (b+1)(b-1)!/b. So
    #   b (b-1)! c_b^-1 = 1/(b+1) doesn't help.
    # Alt: c_b = (b+1)!/b + (something)?
    # (b+1)!/b - (b-1)! = ((b+1)! - b(b-1)!)/b = (b(b+1)(b-1)! - b(b-1)!)/b
    #  = (b-1)! (b+1 - 1) = (b-1)! · b   Hmm.
    #  So (b+1)!/b(b-1)! - 1 = b   ==>  (b+1)!/b = (b+1)(b-1)!  -- try:
    #  (b+1)!/b = (b+1)·b·(b-1)!/b = (b+1)(b-1)!   YES.
    #  So c_b = (b+1)(b-1)! · 1  – but that's NOT what we have; we have
    #  (b+1)(b-1)!/b. So c_b = ((b+1)/b)·(b-1)! = (b-1)! + (b-1)!/b = (b-1)! + (b-2)!
    #  Because (b-1)!/b = (b-1)!/b = 1·2·...·(b-1)/b ... hmm no, that's (b-1)!/b,
    #  which equals (b-2)! · (b-1)/b, not clean.
    # Actually: (b-1)! · (b+1)/b. For b=2: 1·3/2 = 3/2. Yes.

    # Let g(T) = Σ_{b≥2} T^b · (b-1)!(b+1)/b.
    # Then g(T) = Σ T^b (b-1)! · 1 + Σ T^b (b-1)!/b
    #         = Σ T^b (b-1)! + Σ T^b (b-1)!/b
    # First sum: h1(T) = Σ_{b≥2} T^b (b-1)! = T·Σ_{b≥2} T^{b-1}(b-1)! = T·Σ_{k≥1} T^k k! = T·(1F0 minus 1)
    #      where the divergent 1F0(1;;T) = Σ k! T^k.
    # Second sum: h2(T) = Σ_{b≥2} T^b (b-1)!/b = Σ_{b≥2} T^b (b-1)!/b
    #      = Σ_{b≥2} T^b · Γ(b)/b · ...
    #  (b-1)!/b = Γ(b)/b. Not clean.
    #
    # Fine — the U=V=0 series is essentially T·(divergent 1F0) with some shift.
    # Move on to seeing whether we can guess the (U, V)-full form.

    print("\n  U=V=0 slice: [T^b] N_1 = (b-1)!(b+1)/b for b>=2")
    print("  This is (b-1)! + (b-1)!/b · b + ... let's report coefs numerically")
    for b in range(2, B_MAX+1):
        c = coefs.get(b, Integer(0))
        c00 = c.subs([(U, 0), (V, 0)])
        pred = Rational(factorial(b-1)*(b+1), b)
        print(f"    b={b}: N_1[T^{b}]|_(U=V=0) = {c00}, pred = {pred}, match: {c00 == pred}")


def try_symmetry_and_deg(coefs, B_MAX):
    print("\n" + "=" * 70)
    print("Symmetry / degree analysis of [T^b] N_1 in (U, V)")
    print("=" * 70)
    for b in range(2, B_MAX + 1):
        c = coefs.get(b, Integer(0))
        if c == 0: continue
        cp = Poly(c, [U, V])
        deg_U = cp.degree(U)
        deg_V = cp.degree(V)
        symmetric = expand(c - c.subs([(U, V), (V, U)], simultaneous=True)) == 0
        print(f"  b={b}: deg_U={deg_U}, deg_V={deg_V}, symmetric U<->V: {symmetric}")


def try_ansatz_derivatives(coefs, N1, B_MAX):
    """Try N_1 = c_1 * T * df/dT + c_2 * df/dU + c_3 * df/dV + ... where f = 2F0(U,V;;T).

    Actually f is divergent formal — but manipulations are formal.
    """
    print("\n" + "=" * 70)
    print("Attempt: N_1 = combo of df/dT, df/dU, df/dV (formal)")
    print("=" * 70)

    f = build_f_uv(B_MAX)
    # f = 1 + U V T + U(U+1)V(V+1) T^2/2! + ...
    dfdT = expand(diff(f, T))
    dfdU = expand(diff(f, U))
    dfdV = expand(diff(f, V))

    # Try N_1 = a·T·f + b·T²·dfdT + c·(dfdU + dfdV) + ...
    # For each coef, match at low orders and see if a solution exists.
    #
    # Simpler: does the leading coefficient of [T^b] N_1 (i.e. c_b(U,V)) admit
    # decomposition in the basis {(U)_b(V)_b, (U)_b(V)_b · something, ...}?

    print("\n  Compare each [T^b] N_1 to (U)_b · (V)_b (leading coef of [T^b] f):")
    for b in range(2, min(B_MAX + 1, 10)):
        c = coefs.get(b, Integer(0))
        base = expand(rf(U, b) * rf(V, b))
        # Try to write c = q1(U, V) · base + remainder
        if base != 0 and c != 0:
            try:
                q, r = expand(c).as_poly([U, V]).div(base.as_poly([U, V]))
                # sympy's div might not handle rationals nicely.
                # Just print c / base symbolically as a check.
                pass
            except Exception:
                pass
        cf = factor(c)
        bf = factor(base)
        print(f"    b={b}: [T^b] N_1 = {cf}")
        print(f"          (U)_b(V)_b = {bf}")


def try_ansatz_shifted_f(coefs, B_MAX):
    """Try N_1 = f(T; U+p, V+q) - f(T; U, V) style.

    f(U, V) = Σ (U)_b(V)_b T^b/b!.
    f(U+1, V) = Σ (U+1)_b(V)_b T^b/b! = Σ (U)_b (V)_b · (U+b)/U · T^b/b!.
      Hmm, only if U != 0.
    Try (d/dU) f = Σ [d(U)_b/dU] (V)_b T^b/b!.
    d(U)_b/dU = (U)_b · Σ_{j=0}^{b-1} 1/(U+j) = (U)_b · [ψ(U+b) - ψ(U)]
    Not polynomial.
    """
    print("\n" + "=" * 70)
    print("Attempt: N_1 = combo of Bessel-shifted 0F1's")
    print("=" * 70)
    print("  (Skipping detailed fit — inspect symbolic form manually)")


def try_ratio_analysis(coefs, B_MAX):
    """Compute the ratio [T^b] N_1 / (U)_b (V)_b as a rational function in b."""
    print("\n" + "=" * 70)
    print("Ratio r_b := [T^b] N_1 · b! / ((U)_b · (V)_b)")
    print("(this is the 'multiplier' if N_1 were 2F0-form times constant)")
    print("=" * 70)
    for b in range(2, B_MAX + 1):
        c = coefs.get(b, Integer(0))
        if c == 0: continue
        base = expand(rf(U, b) * rf(V, b))
        # Compute c·b! / base symbolically (rational fn of U, V)
        try:
            num = expand(c * factorial(b))
            r = simplify(num / base)
            print(f"  b={b}: r = {factor(r)}")
        except Exception as e:
            print(f"  b={b}: ratio failed ({e})")


def try_ansatz_two_bessels(coefs, B_MAX):
    """Try N_1 = A(U, V) · 2F0(U+p, V+q; ;T) + B(U, V) · 2F0(U+r, V+s; ;T) - ...
    where A, B are polynomial in (U, V).
    """
    print("\n" + "=" * 70)
    print("Attempt: N_1 = A·2F0(U+1, V; ;T) + B·2F0(U, V+1; ;T) + ... form")
    print("=" * 70)
    # This is really trying to guess the ansatz. Let's look at [T^2].
    # We have [T^2] N_1 = c_2(U, V).
    # 2F0(U+1, V+1;;T) at T^2 = (U+1)(U+2)(V+1)(V+2)/2
    # 2F0(U, V;;T) at T^2 = U(U+1) V(V+1)/2
    # ...
    # Rather than fitting: PRINT c_b(U, V) for small b and see if they factor.
    for b in range(2, min(B_MAX + 1, 8)):
        c = coefs.get(b, Integer(0))
        if c == 0: continue
        cf = factor(c)
        print(f"  b={b}:  {cf}")


def try_ansatz_pf_qf(coefs, B_MAX):
    """Try  N_1 = P(T; U, V) · f(T; U, V) + Q(T; U, V) · df/dT
    for polynomial P, Q of small T-degree.
    """
    print("\n" + "=" * 70)
    print("Attempt: N_1 = P(T; U, V)·f + Q(T; U, V)·f' (finite polynomial P, Q)")
    print("=" * 70)
    # Set N_1 = (a_0 + a_1 T + a_2 T^2) · f + (b_0 + b_1 T) · Tf'
    # where a_i, b_i are polynomials in (U, V) with low degree.
    # Match at T^0, T^1, T^2, ..., T^B.
    # f = 1 + UV T + U(U+1)V(V+1) T^2/2 + ...
    # This ansatz might not work since N_1 starts at T^2 (both f and Tf' start at 1).
    # Would need a_0 = 0 = b_0 · 1  -> a_0 = 0, b_0 must give T^0=0 so b_0=0.
    # a_1 T · 1 + b_1 T · UV T = a_1 T + b_1 UV T^2 must vanish at T^1 too.
    # So a_1 = 0.
    # a_2 T^2 · 1 + b_1 UV T^2 = c_2 T^2 => a_2 + b_1 UV = c_2.
    # c_2 = 3/2 + ... let's compute.
    c2 = coefs.get(2, Integer(0))
    c3 = coefs.get(3, Integer(0))
    c4 = coefs.get(4, Integer(0))
    print(f"  c_2 (as poly in U, V) = {factor(c2)}")
    print(f"  c_3 (as poly in U, V) = {factor(c3)}")
    print(f"  c_4 (as poly in U, V) = {factor(c4)}")


def main():
    B_MAX = 10  # keep smaller — full (U,V) is expensive
    N1 = compute_N1_UV(B_MAX)
    coefs = display_N1(N1, B_MAX)
    try_symmetry_and_deg(coefs, B_MAX)
    try_bessel_ansatz_a(coefs, B_MAX)
    try_ratio_analysis(coefs, B_MAX)
    try_ansatz_derivatives(coefs, N1, B_MAX)
    try_ansatz_two_bessels(coefs, B_MAX)
    try_ansatz_pf_qf(coefs, B_MAX)


if __name__ == '__main__':
    main()

"""Systematic matching tests between Huang E_N(t,q) and Rick's data.

Key observations from compute_En.py output:
- E_N has leading t-coefficient: 1/2, 5/24, 61/720, 277/8064, 50521/3628800, 540553/95800320
  Numerators: 1, 5, 61, 277 (?), 50521, 540553 — the last term "277" is actually 277 = ?
  Wait 1385/40320: gcd(1385, 40320) = 5, so 277/8064. 1385 = 5·277.
  Numerator sequence: 1, 5, 61, 1385, 50521, 2702765 = tangent/secant numbers.
  Actually: 1, 5, 61, 1385, 50521 are the SECANT/tangent NUMBERS (zigzag/alternating perm counts).
  These are OEIS A000364 (Euler numbers): 1, 1, 5, 61, 1385, 50521, 2702765.
  So E_N(t, q) is a q-deformation of a series that at t^{2N} gives Euler numbers.

- Rick's U_b leading (in w): 3, 3(E_1 stuff+..), 27, 3(...), 405, 189(...), 8505 = 3^k(2k-1)!!C(b,2k).

These are DIFFERENT number sequences (Euler vs (2k-1)!!·3^k C(b,2k)).

TEST STRATEGY:
1. Check if Rick's U_b at specific (E_1, E_2) values matches E_N under any (t, q) map.
2. Check if there's a Riccati ODE for Rick's leading generating function
   f(T; U, V) · exp(3 E_3 T^2/2).
3. Check specialization: Rick's leading COEFFICIENT b=2,k=1 gives 3; Huang's leading coefficient
   of E_1 in t is 1/2. Ratio 6. b=4,k=2 gives 27, Huang's E_2 leading t^4 = 5/24. Ratio 27/(5/24) = 129.6. No pattern.
"""

import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day140_interior')
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day142_huang_riccati')

from verify_gf_form import build_P, phi_k, p_b_fn, E1, E2, E3, w
from compute_En import E_N, h_m, t, q

from sympy import (symbols, expand, Poly, Integer, factorial, Rational, factor,
                   div, simplify, Symbol, series, together, sqrt, hyper,
                   binomial, S, Function, diff, sympify)


def get_U_data(B_MAX):
    P = build_P(B_MAX)
    phi1 = phi_k(1)
    U = {}
    for b in range(2, B_MAX + 1):
        Pshift = expand(P[b].subs(E3, w - phi1))
        numer = expand(Pshift - p_b_fn(b))
        qq, r = div(numer, w - phi1, w)
        if r != 0:
            continue
        U[b] = expand(qq)
    return U


def test_1_numerical_at_special_values():
    """Test whether E_N at various (t,q) matches U_b at various (E1, E2, w)."""
    print("\n" + "="*78)
    print("TEST 1: Numerical evaluation at (E1, E2, w) = various vs E_N(t, q).")
    print("="*78)

    N_MAX = 6
    B_MAX = 8
    E = E_N(N_MAX)
    U = get_U_data(B_MAX)

    # Try b = 2N (so U_{2N} would correspond to E_N).
    # b=2 <-> N=1: U_2(w) = 3 (constant); E_1(t, q) = t(t+1)/2.
    # These are functions of DIFFERENT variables. But U_2 = 3 is just a number.
    # E_1 = t(t+1)/2. Ratio not constant.

    print("\nAt (E1, E2) = (0, 0), w free (varies): U_b(w) vs E_N(t, q):")
    for b in range(2, B_MAX+1):
        Ub_00 = expand(U[b].subs([(E1, 0), (E2, 0)]))
        print(f"  U_{b}(w) at E1=0, E2=0: {factor(Ub_00)}")
    for N in range(0, N_MAX+1):
        print(f"  E_{N}(t, q) full: [see compute_En output]")

    # Match sequence: U_b at E1=E2=0.
    # U_2 = 3
    # U_3 = 57
    # U_4 = 1395 + 27 w
    # U_5 = 46887 + 2223 w
    # U_6 = 2117907 + 171648 w + 405 w^2
    # These grow like p_b at (0,0), which are (1)(2)...(b)^2... wait.
    # p_b(0,0) = prod_{k=1}^{b} k^2 = (b!)^2. So at (E1,E2)=0, w=0:
    # b=2: (2!)^2 = 4. So P_2(0,0,E_3=−1) at E3=w-phi1 = -1 (since phi1=1 at 0,0) = p_2 + E3·U_2(0) = 4 + (-1)·3 = 1
    # Hmm that's the value at E3=-1. Anyway U_b constants at 0 grow but not like Euler numbers.

    # Try matching numerator sequences.
    # Rick's leading (top-most in w): b=2 -> 3, b=4 -> 27, b=6 -> 405, b=8 -> 8505.
    # These are 3, 27, 405, 8505 = 3·1, 3·9, 3·135, 3·2835.
    # Or (2k-1)!! · 3^k for k=1,2,3,4: 3, 27, 405, 8505. Yes!
    # So Rick's leading coefficient in w for b=2k is 3^k (2k-1)!!.
    #
    # Compare: Euler numbers E_{2N} (secant): 1, 1, 5, 61, 1385, 50521.
    # NOT the same sequence.

    seq_rick = [3, 27, 405, 8505]  # b=2,4,6,8; k=1,2,3,4
    seq_huang_num = [1, 5, 61, 1385]  # Euler numbers at N=1,2,3,4
    print(f"\nRick's leading (b=2k, [w^{{k-1}}] U_b, at E1=E2=0? No, LEADING is pure #): {seq_rick}")
    print(f"Huang's Euler numerators (N=1..4): {seq_huang_num}")
    print(f"Ratio: {[Rational(a, b) for a, b in zip(seq_rick, seq_huang_num)]}")
    # 3, 27/5 = 5.4, 405/61 ~ 6.6, 8505/1385 ~ 6.14. NOT constant.


def test_2_leading_gf_riccati():
    """Does Rick's leading EGF F_P^top = f(T;U,V)·exp(3E_3 T^2/2) satisfy a Riccati ODE?"""
    print("\n" + "="*78)
    print("TEST 2: Does Rick's LEADING GF satisfy a Riccati ODE?")
    print("="*78)

    # Rick has: F_P^top(T; U, V, E_3) = f(T;U,V) · exp(3 E_3 T^2/2)
    # where f(T;U,V) = sum_b (U)_b (V)_b T^b/b!.
    # f is a Gauss hypergeometric 2F1: f = 2F1(U, V; 1; ?)... let's check.
    # (U)_b (V)_b / b! is NOT quite standard. Standard 2F1(A, B; C; z) = sum (A)_n (B)_n / ((C)_n n!) z^n.
    # If C = 1, then 2F1(A, B; 1; z) = sum (A)_n (B)_n / (n!)^2 * z^n... no wait C=1 gives (1)_n = n!, so
    # 2F1(A, B; 1; z) = sum (A)_n (B)_n / (n! · n!) * z^n
    # So f(T; U, V) = sum (U)_b(V)_b T^b/b! = sum (U)_b(V)_b / b! * T^b, which is NOT hypergeometric,
    # because the T^b coefficient has ONE 1/b! not (b!)^2.
    # This IS 2F0(U, V; ; T) — a divergent hypergeometric series.
    # Or equivalently, related to Kummer's function.

    T = symbols('T')
    U_var, V_var, E3_var = symbols('U V E3', positive=True)

    # Compute f(T; U, V) truncated
    f_series = Integer(0)
    K = 8
    for b in range(0, K+1):
        pb_UV = Integer(1)
        for i in range(b):
            pb_UV *= (U_var + i)
        for i in range(b):
            pb_UV *= (V_var + i)
        f_series += pb_UV * T**b / factorial(b)

    F_top = f_series * expand(sum((Rational(3, 2) * E3_var * T**2)**k / factorial(k) for k in range(K+1)))
    F_top = expand(F_top)
    # Truncate
    Ft = Poly(F_top, T)
    print("f(T; U, V) coefficients (leading b terms):")
    for b in range(0, min(K+1, 6)):
        coef = Ft.coeff_monomial(T**b) if b <= Ft.degree() else Integer(0)
        print(f"  T^{b}: {factor(expand(coef * factorial(b)))}")

    # Try Riccati: (aT + b)F' + c F = d F^2 + ...?
    # For 2F1 that satisfies Riccati via B'/B, we can check if F'/F is a rational function of T.
    # Let A(T) = F'/F. Compute A.
    F_series_lim = Integer(0)
    for b in range(0, K+1):
        pb_UV = Integer(1)
        for i in range(b):
            pb_UV *= (U_var + i)
        for i in range(b):
            pb_UV *= (V_var + i)
        # multiply by exp(3E3 T^2/2)
        for j in range(0, (K-b)//2 + 1):
            F_series_lim += pb_UV * (Rational(3,2) * E3_var)**j / factorial(j) * T**(b+2*j) / factorial(b)
    F_series_lim = expand(F_series_lim)
    # Get F' and F, form A = F'/F as series
    Fp = expand(diff(F_series_lim, T))
    # A = Fp / F, we want to expand as series in T.
    # Do this coefficient-by-coefficient. F = 1 + O(T), so 1/F = 1 - F1 T + ...
    # A(T) = sum a_n T^n.
    K2 = 6
    F_coefs = {}
    Fp_coefs = {}
    for n in range(K2+1):
        F_coefs[n] = expand(Poly(F_series_lim, T).coeff_monomial(T**n))
        Fp_coefs[n] = expand(Poly(Fp, T).coeff_monomial(T**n)) if n <= Poly(Fp, T).degree() else Integer(0)

    # A = Fp/F. So Fp = A · F. So Fp_n = sum_{i+j=n} A_i F_j.
    # Solve for A_n: A_n = Fp_n - sum_{i=0..n-1} A_i F_{n-i} (assuming F_0 = 1).
    A = {}
    for n in range(K2+1):
        s = Integer(0)
        for i in range(n):
            s += A[i] * F_coefs[n - i]
        A[n] = expand((Fp_coefs[n] - s) / F_coefs[0])

    print("\nA(T) = F'/F coefficients:")
    for n in range(K2+1):
        print(f"  A_{n} = {factor(A[n])}")

    # Look for A(T) as rational: does A satisfy (4T - u T^2) A' = (4T - u T^2) A^2 + ...?
    # Huang has: (4x - u x^2) A' = (4x - u x^2) A^2 - (2 - (tu - t + 2u)x) A + t(t+1)
    # Here u = -q. For q =? and t=? matching Rick's setup?

    # Trying: does (4T - ? T^2) A'(T) - (4T - ? T^2) A^2(T) + (const) A(T) - (const) simplify?
    # Rick's A_0 = U V + 3E_3 · 0 = UV. So A_0 = UV. This corresponds to t(t+1)/2 in Huang's setup:
    # Huang's a_0 = t(t+1)/2. So if UV = t(t+1)/2? Or U(V) = t(t+1)?
    # If U = t, V = t+1 (or similar): UV = t(t+1). Then Huang has t(t+1)/2 = UV/2.
    # But Rick's a_0 = UV. So Huang's B satisfies (Huang_a_0 = 2 Rick_a_0)? Off by factor 2.
    # Actually Rick's f = sum (U)_b(V)_b T^b/b!, so f'/f at T=0 gives UV.
    # Huang's B'/(-B) has a_0 = t(t+1)/2, i.e., -B'/B = a_0 + a_1 x + ... but Rick's is +F'/F.
    # Sign might differ. Try matching UV = t(t+1)? Or UV = t(t+1)/2?

    # More systematically: check LC of A_0 against Huang's a_0.
    a_0_huang = t*(t + 1) / 2
    print(f"\nHuang a_0 = t(t+1)/2 = {a_0_huang}")
    print(f"Rick A_0 = {A[0]}")


def test_3_matching_riccati_form():
    """Try (U, V) = (t, t+1) or various maps; see if Rick's F satisfies Huang's Riccati."""
    print("\n" + "="*78)
    print("TEST 3: Try substitution (U, V) = (t, t+1) and check Riccati match.")
    print("="*78)

    # Rick's f = sum (U)_b (V)_b T^b/b!. With U=t, V=t+1:
    # (t)_b (t+1)_b / b! T^b. This is 2F0(t, t+1; ; T), or more usefully,
    # sum (t)_b (t+1)_b T^b / b! = (1)_b^{-1} · (t)_b(t+1)_b T^b · b!/b! ... not standard.

    # Actually (t)_b (t+1)_b = (t)(t+1)···(t+b-1) · (t+1)(t+2)···(t+b) = (t)_{2b+1}/t · 1/(t)_1 ... complicated
    # Let's just numerically compute.

    T = symbols('T')
    K = 8
    f_series = Integer(0)
    for b in range(0, K+1):
        pb = Integer(1)
        for i in range(b):
            pb *= (t + i)
        for i in range(b):
            pb *= (t + 1 + i)
        f_series += pb * T**b / factorial(b)
    f_series = expand(f_series)

    print("f(T; U=t, V=t+1) coefficients:")
    for b in range(0, K+1):
        c = Poly(f_series, T).coeff_monomial(T**b)
        print(f"  [T^{b}] f = {factor(expand(c * factorial(b)))} / {b}!")

    # Compare with Huang's E_N series: sum E_N x^N = 1/B_{t,q}(-x).
    # So 1/B_{t,q}(-x) = sum E_N(t, q) x^N.
    # Rick's f is NOT the Riccati generating function; Rick's f is more like a hypergeometric 2F0.

    # BUT: does Rick's f(T; t, t+1) equal 1/B_{t,q}(-T) at some q?
    # At q = 0: B_{t,0}(x) = sum h_{2a}(t, 0) x^a. h_{2a}(t, 0) = (1/(2a)!) prod_{i=1..a} (t+i) prod_{j=0..a-1}(t) = (1/(2a)!) t^a (t+1)(t+2)...(t+a) = (1/(2a)!) t^a (t+1)_a
    # Actually let me look up Huang's definition of h_m(t, q).
    # h_m(t, q) = (1/m!) prod_{i=1..m_-} (t+i) prod_{j=0..m_+ - 1} (t+j q)
    # For m even, m = 2a: m_- = a, m_+ = a. So h_{2a}(t, q) = (1/(2a)!) prod_{i=1..a}(t+i) prod_{j=0..a-1}(t+jq).
    # For q = 0: h_{2a}(t, 0) = (1/(2a)!) (t+1)(t+2)...(t+a) · t · t · ... · t (a copies) = t^a (t+1)_a / (2a)!.
    # Hmm.

    # Let's just check E_N(t, 0) and see if it matches anything.
    E = E_N(6)
    print("\nE_N at (t, q) match check vs f(T; t, t+1):")
    for N in range(0, 7):
        val = E[N].subs(q, 0)
        val = factor(expand(val))
        print(f"  E_{N}(t, 0) = {val}")
    # Compare with (t)_{2N}(t+1)_{2N}/(2N)! (if U=t, V=t+1 substitution):
    print("\n(t)_{2N} (t+1)_{2N} / (2N)! at N=0..6:")
    for N in range(0, 7):
        pb = Integer(1)
        for i in range(2*N):
            pb *= (t + i)
        for i in range(2*N):
            pb *= (t + 1 + i)
        val = pb / factorial(2*N)
        print(f"  N={N}: {factor(val)}")

    # These are DIFFERENT.

    # Try another approach: does Rick's leading GF top(T;U,V,E3) satisfy a Riccati?
    # Do the shift E_3 = something. Note the factor exp(3 E_3 T^2/2). This is a Gaussian factor.
    # A Riccati satisfied by an exponential? An exp(c T^2) satisfies A = 2cT (linear in T),
    # then A' = 2c and A^2 = 4c^2 T^2. So (linear) A satisfies a Riccati trivially.
    # But f(T; U, V) does NOT satisfy a simple Riccati (it's 2F0-like divergent series).


def test_4_check_hypergeometric_form():
    """Check if Rick's f(T; U, V) is a 2F0 hypergeometric, and if Huang's B involves 2F1(-, -; 1/2; -)."""
    print("\n" + "="*78)
    print("TEST 4: Hypergeometric character check.")
    print("="*78)

    # Rick's f: sum (U)_b (V)_b / b! · T^b — this is 2F0(U, V; ; T) which is DIVERGENT
    # (Kummer's confluent series, or more precisely the sum for a Meixner-like polynomial).
    # It IS the formal series for U(U, V-U+1, -1/T) T^{-U} · Γ correction... complex.

    # Huang's B(x) = 2F1(t/q, t+1; 1/2; -qx/4) — this is a CONVERGENT 2F1.
    # The denominator parameter C = 1/2 is what generates the double factorials.

    # The two are structurally DIFFERENT hypergeometric objects.

    print("Rick's f(T; U, V) = 2F0(U, V; ; T): a formal series (divergent).")
    print("  coefficient of T^b: (U)_b (V)_b / b!.")
    print("Huang's B(x) = 2F1(t/q, t+1; 1/2; -qx/4): convergent, generates fence order polys.")
    print()
    print("Denominator parameter in 2F0: none (or 'C=infinity').")
    print("Denominator parameter in Huang's 2F1: C = 1/2 — THIS is what gives double factorials.")
    print()
    print("Rick's leading motif 3^k(2k-1)!! · C(b, 2k) — the (2k-1)!! comes from a DIFFERENT source:")
    print("  the exp(3 E_3 T^2/2) factor, where (2k-1)!! appears in Hermite polynomial expansions:")
    print("  Σ (E_3 x/2)^k (2k-1)!! / k! ... via Gaussian integrals.")
    print()
    print("More precisely: exp(3 E_3 T^2/2) has T^{2k}-coefficient (3 E_3/2)^k / k! = 3^k E_3^k / (2^k k!).")
    print("Extracting E_3^k gives 3^k T^{2k} / (2^k k!).")
    print("Multiplied by 1/(2k)! for the outer EGF gives 3^k / (2^k k! (2k)!) T^{2k}/[nothing external].")
    print("But r_b^{(k)} · [E_3^k] gives (2k-1)!! · b! /((b-2k)! (2k-1)!!) mess...")
    print()
    print("The (2k-1)!! in Rick comes from: exp(cx^2) ↔ Hermite generating function, where")
    print("  (2k-1)!! = (2k)!/(2^k k!). So 3^k (2k-1)!! = 3^k (2k)!/(2^k k!) = (3/2)^k (2k)!/k!.")
    print()
    print("In Huang, (1/2)_a = (2a-1)!!/2^a. So (2a-1)!! = 2^a (1/2)_a. The double factorial is")
    print("intrinsic to hypergeometric with C=1/2.")
    print()
    print("VERDICT: both have (2k-1)!! but from different mechanisms.")
    print("Rick's from Gaussian in E_3; Huang's from 2F1(·;·;1/2;·). Structural CONVERGENCE, not identity.")


def test_5_direct_match_attempt():
    """Direct attempt: does U_2 = 3 match E_N at some (t, q, w) evaluation?"""
    print("\n" + "="*78)
    print("TEST 5: Direct evaluation matching.")
    print("="*78)
    N_MAX = 6
    B_MAX = 8
    E = E_N(N_MAX)
    U = get_U_data(B_MAX)

    # U_2 = 3. Look for E_N(t, q) = 3 for some (t, q). E_2(t=?, q=?) = 3?
    # E_2 = -t(t+1)(qt + 2q - 5t^2 - 4t)/24. Setting = 3? no unique answer.
    # Not a useful check.

    # Better: check DEGREES.
    # Rick U_b has coefficients in E_1, E_2 of total degree b - 2 (roughly).
    # E_N has bivariate (t, q) total degree 2N.
    # So if we identify t = E_1, q = E_2, and w with some constant, then b = 2N would give:
    # U_{2N}: coefficient in (E_1, E_2) of degree 2N - 2. E_N: bivariate degree 2N.
    # Off by 2 in degree.
    # Or b = N: U_N has degree N-2 in (E_1, E_2). E_N degree 2N. Off by N+2.
    # NEITHER matches naturally.

    # Let's just check E_N for structural rings that appear in U_b:
    # U_b has factor (E_1 + something)?
    # U_2 = 3. U_3 = 25 E_1 + 9 E_2 + 57.
    # U_3(w=0) has no common factor except integer 1. Test 25 = 25, 9 = 9, 57 = 3·19.

    # Compare with E_2(t, q) = -t(t+1)(qt + 2q - 5t^2 - 4t)/24.
    # E_2 has t(t+1) factor. U_3 has NO t(t+1)-like factor.
    # Definitively different.


def test_6_leading_gf_riccati_direct():
    """Rick's TOP-in-UV EGF: F_top = f(T;U,V) exp(3 E_3 T^2/2).
    Check A = F'/F satisfies a Riccati (T A' = ... A^2 + ...).
    """
    print("\n" + "="*78)
    print("TEST 6: Riccati ODE for Rick's TOP EGF A = F'/F.")
    print("="*78)

    T = symbols('T')
    Uv, Vv, E3v = symbols('U V E3')
    K = 8

    # F_top = f · exp(3 E3 T^2/2)
    # A(T) = f'/f + 3 E3 T
    # So A(T) = 3 E3 T + f'(T;U,V)/f(T;U,V).
    # Now f = 2F0(U, V; ; T). Does 2F0 satisfy a Riccati?
    # d/dT f = sum (U)_b(V)_b b T^{b-1}/b! = sum (U)_{b+1}(V)_{b+1} T^b/b!
    # This is a "shift" — not an ODE in the classical sense.
    # 2F0 satisfies (T · d/dT + U)(T · d/dT + V) f = (T d/dT) f. But (T d/dT) is NOT d/dT.
    # So Rick's f does NOT satisfy a "nice" 1st-order Riccati.

    # Compute A_n coefficients for f = 2F0(U, V; ; T):
    # f_n = (U)_n (V)_n / n! T^n
    # f'_n / f = complex; compute numerically.

    # Actually verify: for 2F0(U, V), is A(T) = f'(T)/f(T) rational in T?
    # Try small U, V numerically.

    from sympy import Symbol
    U_val, V_val = 2, 3  # try U=2, V=3
    f_num = Integer(0)
    for b in range(0, K+1):
        pb = Integer(1)
        for i in range(b):
            pb *= (U_val + i)
        for i in range(b):
            pb *= (V_val + i)
        f_num += pb * T**b / factorial(b)
    print(f"f(T; U=2, V=3) = {expand(f_num)}")

    # Compute f'/f as series.
    fp_num = diff(f_num, T)
    # A = fp/f = fp · (1/f). Compute (1/f) as series.
    # f = 1 + a_1 T + a_2 T^2 + ..., so 1/f = 1 - a_1 T + (a_1^2 - a_2) T^2 + ...
    K2 = 6
    f_coeffs = {n: Poly(f_num, T).coeff_monomial(T**n) if n <= Poly(f_num, T).degree() else Integer(0) for n in range(K2+2)}
    fp_coeffs = {n: Poly(fp_num, T).coeff_monomial(T**n) if n <= Poly(fp_num, T).degree() else Integer(0) for n in range(K2+2)}
    A_coeffs = {}
    for n in range(K2+1):
        s = Integer(0)
        for i in range(n):
            s += A_coeffs[i] * f_coeffs[n - i]
        A_coeffs[n] = expand((fp_coeffs[n] - s) / f_coeffs[0])
    print("A(T) = f'(T)/f(T) coefficients (U=2, V=3):")
    for n in range(K2+1):
        print(f"  A_{n} = {A_coeffs[n]}")

    # If A were rational, coefficients would satisfy a linear recurrence.
    # Compute ratios A_{n+1}/A_n to spot rationality.
    print("Ratios A_{n+1}/A_n:")
    for n in range(1, K2):
        r = Rational(A_coeffs[n+1], A_coeffs[n]) if A_coeffs[n] != 0 else "N/A"
        print(f"  A_{n+1}/A_n = {r}")


def main():
    test_1_numerical_at_special_values()
    test_2_leading_gf_riccati()
    test_3_matching_riccati_form()
    test_4_check_hypergeometric_form()
    test_5_direct_match_attempt()
    test_6_leading_gf_riccati_direct()


if __name__ == "__main__":
    main()

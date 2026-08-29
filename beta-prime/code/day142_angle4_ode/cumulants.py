"""
Day 142 Attack A — Cumulant series (full).

Compute N_k(T; U, V) = [E_3^k] log(F_P / f) at (U, V) = (0, 0) up to b = 18.
Verify N_1[T^2], N_2[T^5], N_3[T^8] leading coefs.
Extract N_4[T^11], N_5[T^14], N_6[T^17] leading.
Verify leading coefficient at T^{3k-1} is (U, V)-independent by probing at several values.
Report closed form found: N_1(T; U=V=0) = Σ_{b≥2} (b-1)!(b+1)/b · T^b.
"""

import sys, os, time
sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day140_interior')

from compute_P_fast import compute_P_at
from verify_gf_form import E3
from sympy import (symbols, expand, Integer, Rational, Poly, factorial,
                   rf, factor)

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

def build_f_num(U_val, V_val, B_max):
    F = Integer(0)
    for b in range(B_max + 1):
        F += (rf(U_val, b) * rf(V_val, b)) * T**b / factorial(b)
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

def leading_of_Nk(Uval, Vval, B_MAX):
    P_uv = compute_P_at(Uval, Vval, B_MAX)
    FP = build_FP(P_uv, B_MAX)
    f  = build_f_num(Uval, Vval, B_MAX)
    L  = series_log_ratio(FP, f, B_MAX)
    Lp = Poly(expand(L), E3)
    out = {}
    for k in range(1, 7):
        Nk = expand(Lp.coeff_monomial(E3**k))
        d0 = 3*k - 1
        if d0 > B_MAX:
            continue
        c = Poly(Nk, T).coeff_monomial(T**d0)
        out[k] = expand(c)
    return out

def full_N_at_00(B_MAX):
    P_00 = compute_P_at(0, 0, B_MAX)
    FP = build_FP(P_00, B_MAX)
    f = Integer(1)  # (0)_b (0)_b = 0 for b >= 1
    L0 = series_log_ratio(FP, f, B_MAX)
    Lp = Poly(expand(L0), E3)
    out = {}
    for k in range(1, 8):
        Nk = expand(Lp.coeff_monomial(E3**k))
        out[k] = Nk
    return out

def main():
    print("=" * 70)
    print("PART 1: Verify N_k leading = (U, V)-independent")
    print("=" * 70)
    B = 14
    for (Uv, Vv) in [(0, 0), (1, 1), (2, 3), (Rational(1,2), Rational(3,2))]:
        t0 = time.time()
        data = leading_of_Nk(Uv, Vv, B)
        print(f"  (U,V)=({Uv},{Vv})  [in {time.time()-t0:.1f}s]:  {data}")

    print("\n" + "=" * 70)
    print("PART 2: Full N_k at U=V=0, up to T^18")
    print("=" * 70)
    Ns = full_N_at_00(18)
    for k in range(1, 7):
        Nk = Ns.get(k, Integer(0))
        if Nk == 0: continue
        Nkp = Poly(Nk, T)
        print(f"\n  N_{k}(T; 0, 0):")
        for d in range(19):
            c = Nkp.coeff_monomial(T**d)
            if c != 0:
                print(f"    [T^{d}] = {c}")

    print("\n" + "=" * 70)
    print("PART 3: Test conjecture N_1(T; 0, 0) = Σ_{b>=2} (b-1)!(b+1)/b · T^b")
    print("=" * 70)
    N1 = Ns[1]
    N1p = Poly(N1, T)
    ok = True
    for b in range(2, 19):
        actual = N1p.coeff_monomial(T**b)
        pred = Rational(factorial(b-1) * (b + 1), b)
        if actual != pred:
            print(f"  b={b}: MISMATCH  actual={actual}, pred={pred}")
            ok = False
        else:
            print(f"  b={b}: OK ({actual})")
    print(f"\n  Conjecture holds: {ok}")
    print(f"\n  Equivalent: b! [T^b] N_1(T;0,0) = ((b-1)!)^2 (b+1) = OEIS A179442")

    print("\n" + "=" * 70)
    print("PART 4: Sequence 3, 27, 417, 7851, 164124 (numerators of N_k[T^{3k-1}])")
    print("=" * 70)
    for k in range(1, 7):
        Nk = Ns.get(k, Integer(0))
        if Nk == 0: continue
        d0 = 3*k - 1
        c = Poly(Nk, T).coeff_monomial(T**d0)
        num_k = c * (3*k - 1)  # numerator when denom is 3k-1
        print(f"  k={k}: N_k[T^{d0}] = {c}, num = c*(3k-1) = {num_k}")

if __name__ == '__main__':
    main()

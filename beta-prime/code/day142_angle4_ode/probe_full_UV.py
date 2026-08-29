"""Probe: is N_k[T^{3k-1}] a constant in U, V, or does it depend on them?

Compare values at (U,V) = (0,0), (1,1), (2,3).
If constant, values at all points agree.
"""

import sys, os, time
sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day140_interior')

from compute_P_fast import compute_P_at
from verify_gf_form import E3
from sympy import symbols, expand, Integer, Rational, Poly, factorial, rf

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
    """Return dict {k: N_k[T^{3k-1}]} at given (U, V)."""
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

def main():
    B = 14
    for (Uv, Vv) in [(0, 0), (1, 1), (2, 3), (Rational(1,2), Rational(3,2))]:
        t0 = time.time()
        try:
            data = leading_of_Nk(Uv, Vv, B)
            print(f"(U,V)=({Uv},{Vv}) [in {time.time()-t0:.1f}s]:  {data}")
        except Exception as e:
            print(f"(U,V)=({Uv},{Vv}): ERROR {e}")

if __name__ == '__main__':
    main()

"""Check whether [E_3^k T^{3k-1+r}] X is (U, V)-independent for various offsets r.
The r=0 case (T^{3k-1}) is the known invariant. Test r = 1, -1, etc.
"""
import sys, os, time
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day140_interior')
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day142_angle4_ode')
from compute_P_fast import compute_P_at
from verify_gf_form import E3
from sympy import symbols, expand, Integer, Poly, factorial, diff

T = symbols('T')


def theta(P):
    return expand(T * diff(P, T))


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
    b = {0: Integer(1) / a[0]}
    for n in range(1, N + 1):
        s = sum(a[k] * b[n - k] for k in range(1, n + 1))
        b[n] = expand(-s / a[0])
    return sum(b[d] * T**d for d in range(N + 1))


def compute_X_at(U_val, V_val, B_MAX):
    """Compute X = L·F_P/F_P at (U, V) values."""
    P = compute_P_at(U_val, V_val, B_MAX)
    FP = build_FP(P, B_MAX)
    # L = T(U+θ)(V+θ) - θ
    P1 = expand(V_val * FP + theta(FP))
    P2 = expand(U_val * P1 + theta(P1))
    P3 = expand(T * P2)
    LFP = truncate_T(expand(P3 - theta(FP)), B_MAX - 1)
    invFP = one_over_series(FP, B_MAX - 1)
    X = truncate_T(expand(LFP * invFP), B_MAX - 1)
    return X


def extract_diag_offset(X, k_max, r):
    """Extract [E_3^k T^{3k-1+r}] X for k = 1..k_max."""
    Xp = Poly(X, T)
    out = {}
    for k in range(1, k_max + 1):
        b = 3*k - 1 + r
        if b < 0:
            continue
        c = Xp.coeff_monomial(T**b)
        c_E3 = Poly(c, E3).coeff_monomial(E3**k)
        out[k] = c_E3
    return out


def main():
    B_MAX = 12
    K_MAX = 4  # for offset r=1, need T^{3k}, so b <= 3·4 = 12
    print(f"Computing X at 3 different (U, V) points, B_MAX = {B_MAX}")
    t0 = time.time()
    X_00 = compute_X_at(0, 0, B_MAX)
    print(f"  (0,0) done in {time.time()-t0:.1f}s")
    t0 = time.time()
    X_11 = compute_X_at(1, 1, B_MAX)
    print(f"  (1,1) done in {time.time()-t0:.1f}s")
    t0 = time.time()
    X_23 = compute_X_at(2, 3, B_MAX)
    print(f"  (2,3) done in {time.time()-t0:.1f}s")

    for r in [-1, 0, 1, 2]:
        print(f"\n=== [E_3^k T^{{3k-1+{r}}}] X for various (U, V) ===")
        d_00 = extract_diag_offset(X_00, K_MAX, r)
        d_11 = extract_diag_offset(X_11, K_MAX, r)
        d_23 = extract_diag_offset(X_23, K_MAX, r)
        for k in sorted(d_00.keys()):
            b = 3*k - 1 + r
            v_00 = d_00.get(k, "N/A")
            v_11 = d_11.get(k, "N/A")
            v_23 = d_23.get(k, "N/A")
            same = (v_00 == v_11 == v_23)
            print(f"  k={k}, T^{b}: (0,0)={v_00}, (1,1)={v_11}, (2,3)={v_23}   {'UNIV' if same else 'depends on U, V'}")


if __name__ == '__main__':
    main()

"""Combined k=8: computes P_dict ONCE at (U,V)=(0,0), B_MAX=24, then extracts
BOTH:
  (a) a_8 from X = L·F_P / F_P  (leads to b_8 via a_k = -b_k + Σ b_i b_j identity)
  (b) n_8 from log(F_P)         (leads to b_8 = 23·n_8 directly)

If both agree, b_8 is doubly verified.
"""
import sys, os, time
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day140_interior')
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day142_angle4_ode')
from compute_P_fast import compute_P_at
from verify_gf_form import E3
from sympy import (symbols, expand, Integer, Rational, Poly, factorial, diff, factorint)

T = symbols('T')


def theta(P):
    return expand(T * diff(P, T))


def apply_L_uv0(P):
    return expand(T * theta(theta(P)) - theta(P))


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
    inv_a0 = Integer(1) / a[0]
    for n in range(1, N + 1):
        s = sum(a[k] * b[n - k] for k in range(1, n + 1))
        b[n] = expand(-inv_a0 * s)
    return sum(b[d] * T**d for d in range(N + 1))


def series_log(FP_series, N):
    G = expand(FP_series - 1)
    logv = Integer(0)
    Gk = Integer(1)
    for k in range(1, N + 1):
        Gk = truncate_T(expand(Gk * G), N)
        if Gk == 0:
            break
        logv = expand(logv + (-1)**(k - 1) * Gk / k)
    return truncate_T(logv, N)


def run(K_MAX):
    B_MAX = 3 * K_MAX
    print(f"[K_MAX={K_MAX}] B_MAX={B_MAX}", flush=True)
    t0 = time.time()
    P_dict = compute_P_at(0, 0, B_MAX)
    print(f"  P_dict built in {time.time()-t0:.1f}s", flush=True)

    FP = build_FP(P_dict, B_MAX)

    # -------- METHOD A: X = L·F_P / F_P --------
    t0 = time.time()
    LFP = truncate_T(apply_L_uv0(FP), B_MAX - 1)
    print(f"  L·F_P built in {time.time()-t0:.1f}s", flush=True)
    t0 = time.time()
    invFP = one_over_series(FP, B_MAX - 1)
    print(f"  1/F_P built in {time.time()-t0:.1f}s", flush=True)
    t0 = time.time()
    X = truncate_T(expand(LFP * invFP), B_MAX - 1)
    print(f"  X built in {time.time()-t0:.1f}s", flush=True)
    Xp = Poly(X, T)
    a_dict = {}
    for k in range(1, K_MAX + 1):
        b = 3*k - 1
        coeff_Tb = Xp.coeff_monomial(T**b)
        coeff = Poly(coeff_Tb, E3).coeff_monomial(E3**k)
        a_dict[k] = coeff

    print(f"\n=== a_k = [E_3^k T^{{3k-1}}] X ===", flush=True)
    for k in range(1, K_MAX + 1):
        print(f"  a_{k} = {a_dict[k]}   factors: {factorint(abs(int(a_dict[k]))) if a_dict[k] else '{}'}", flush=True)

    # -------- METHOD B: N_k = [E_3^k] log(F_P) --------
    t0 = time.time()
    L0 = series_log(FP, B_MAX)
    print(f"\n  log(FP) built in {time.time()-t0:.1f}s", flush=True)
    Lp = Poly(expand(L0), E3)
    n_dict = {}
    for k in range(1, K_MAX + 1):
        Nk = expand(Lp.coeff_monomial(E3**k))
        if Nk == 0:
            continue
        Nkp = Poly(Nk, T)
        coeff = Nkp.coeff_monomial(T**(3*k - 1))
        n_dict[k] = coeff

    print(f"\n=== n_k = N_k[T^{{3k-1}}] and direct b_k = (3k-1)·n_k ===", flush=True)
    b_direct = {}
    for k in sorted(n_dict):
        b_direct[k] = (3*k - 1) * n_dict[k]
        print(f"  n_{k} = {n_dict[k]} = {Rational(n_dict[k])}   b_{k}(direct) = {b_direct[k]}", flush=True)

    # -------- Derived b_k from identity + a_k --------
    b_known = {1: 3, 2: 27, 3: 417, 4: 7851, 5: 164124, 6: 3661389, 7: 85384566}
    print(f"\n=== b_k derived from a_k = -b_k + Σ b_i b_j identity ===", flush=True)
    for k in range(1, K_MAX + 1):
        if k not in a_dict:
            continue
        conv = sum(b_known.get(i, 0) * b_known.get(k - i, 0) for i in range(1, k))
        # For known b_i for i < k
        if k in b_known:
            # skip (already known) but sanity check
            derived = -int(a_dict[k]) + conv
            match_known = "MATCH" if derived == b_known[k] else "MISMATCH"
            print(f"  k={k}: derived from identity = {derived}, previous = {b_known[k]}   [{match_known}]", flush=True)
        else:
            derived = -int(a_dict[k]) + conv
            b_known[k] = derived
            direct = b_direct.get(k)
            cross = "MATCH" if direct is not None and direct == derived else ("MISMATCH" if direct is not None else "no direct")
            print(f"  k={k}: derived from identity = {derived}   direct = {direct}   [{cross}]", flush=True)
            print(f"        factors: {factorint(int(derived))}", flush=True)

    # Save results
    outfile = f'/home/agent/projects/beta-prime/code/day144_bk_extension/results_k{K_MAX}.txt'
    with open(outfile, 'w') as f:
        for k in range(1, K_MAX + 1):
            f.write(f"a_{k} = {a_dict.get(k)}\n")
        for k in sorted(n_dict):
            f.write(f"n_{k} = {n_dict[k]}\n")
            f.write(f"b_{k}_direct = {(3*k-1)*n_dict[k]}\n")
        for k in sorted(b_known):
            f.write(f"b_{k} = {b_known[k]}\n")
    print(f"\nResults saved to {outfile}", flush=True)


if __name__ == '__main__':
    K = int(sys.argv[1]) if len(sys.argv) > 1 else 8
    run(K)

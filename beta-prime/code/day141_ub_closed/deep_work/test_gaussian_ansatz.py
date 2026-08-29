"""
Test if F_P(T; U, V, E_3) = f(T; U, V) · exp(E_3 P_1(T; U, V) + E_3^2 P_2(T; U, V))
where P_1 = N_1 = 3T²/2 + 8(U+V+1)T³/3 + ...
      P_2 = N_2 = 27T^5/5 + ...

If yes, then N_k(T) = 0 for k ≥ 3. Compute N_3(T), N_4(T), ... via cumulant expansion.

Cumulant relations from moments h_k = [E_3^k] (F_P/f):
  N_1 = h_1
  N_2 = h_2 - h_1²/2
  N_3 = h_3 - h_1 h_2 + h_1³/3
  N_4 = h_4 - h_1 h_3 - h_2²/2 + h_1² h_2 - h_1^4/4
  ...

Standard cumulant expansion: N_n = (-1)^n/n · [E_3^n] log(1 + Σ_{k≥1} h_k E_3^k) · well, standard.

Compute up to T^10 (needs B_MAX = 10 in F_P).
"""

import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day140_interior')
from verify_gf_form import build_P, E1, E2, E3
from sympy import (symbols, expand, factor, Poly, Integer, Rational,
                    simplify, rf, together, log, series, factorial)

U, V = symbols('U V')

def to_UV(P):
    return expand(P.subs([(E1, U + V - 2), (E2, U*V - U - V + 1)], simultaneous=True))

def main():
    B_MAX = 10
    print(f"Building P_b for b = 0..{B_MAX}\n")
    P = build_P(B_MAX)
    P_UV = {b: to_UV(P[b]) for b in P}

    # Compute h_k(T) := [E_3^k] (F_P/f) for k = 0, 1, 2, ...
    # f(T; U, V) := Σ_b (U)_b(V)_b T^b/b! (OGF in T)
    # F_P(T; U, V, E_3) := Σ_b P_UV[b] T^b/b! (OGF in T)
    # F_P/f: OGF in T, coefficients in Q[U, V, E_3]

    from sympy import Symbol
    T = Symbol('T')

    # Compute F_P as OGF in T (with coefs in Q[U, V, E_3])
    F_coefs = {b: expand(P_UV[b] / factorial(b)) for b in range(B_MAX + 1)}
    f_coefs = {b: expand(rf(U, b) * rf(V, b) / factorial(b)) for b in range(B_MAX + 1)}

    # h(T) = F_P/f, OGF in T, coefs in Q[U, V, E_3]
    h_coefs = {}
    for n in range(B_MAX + 1):
        s = F_coefs[n]
        for k in range(n):
            s = expand(s - f_coefs[n - k] * h_coefs[k])
        h_coefs[n] = expand(s / f_coefs[0])

    # Extract h_k(T) := [E_3^k] h(T) for k = 0, 1, 2, ...
    K_MAX = B_MAX // 2 + 1
    hs = {k: {} for k in range(K_MAX + 1)}  # hs[k][n] = [T^n E_3^k] h
    for n in range(B_MAX + 1):
        hp_E3 = Poly(h_coefs[n], E3)
        for k in range(K_MAX + 1):
            hs[k][n] = expand(hp_E3.coeff_monomial(E3**k))

    # Verify h_0(T) = 1: h_0[T^0] = 1, h_0[T^n] = 0 for n ≥ 1.
    print("Sanity: h_0(T):")
    for n in range(B_MAX + 1):
        print(f"  [T^{n}] h_0 = {hs[0][n]}")

    # Now compute cumulants N_k(T) via log(1 + Σ_k h_k(T) E_3^k) = Σ_k E_3^k N_k(T)
    # log(1 + X) = Σ_{n≥1} (-1)^{n+1}/n · X^n
    # X = Σ_k h_k(T) E_3^k (starts at k=1)
    # [E_3^m] X^n = sum over compositions...

    # Approach: Compute log(1 + X) as series in E_3, up to E_3^K_MAX.
    # Truncate all products at E_3^{K_MAX + 1}.

    # Represent series as dicts: {n: [E_3^k] coef at T^n} for each k = 0, 1, ...
    # Or as polynomial in E_3 with coefficients being series in T.

    # Build X = Σ_{k=1}^{K_MAX} h_k(T) · E_3^k as polynomial in E_3 with T-series coefs.
    # h_k(T) truncated at T^{B_MAX}.

    def series_mul(A, B, max_n):
        """OGF multiplication in T, truncated at T^max_n."""
        C = {}
        for a_n in A:
            for b_n in B:
                if a_n + b_n > max_n: continue
                C.setdefault(a_n + b_n, Integer(0))
                C[a_n + b_n] = expand(C[a_n + b_n] + A[a_n] * B[b_n])
        return C

    # X as {k: {n: coef}} — E_3^k coefficient is a T-series
    X = {k: hs[k] for k in range(1, K_MAX + 1)}
    # X[0] = 0 (missing).

    # X^n (n-th power in E_3-polynomial times T-series). Truncate at E_3^{K_MAX}.
    # Compute iteratively.
    Xpow = {1: X}
    for n in range(2, K_MAX + 1):
        prev = Xpow[n - 1]
        cur = {}
        for k1 in prev:
            for k2 in X:
                k = k1 + k2
                if k > K_MAX: continue
                prod = series_mul(prev[k1], X[k2], B_MAX)
                if k not in cur:
                    cur[k] = {}
                for tn, tv in prod.items():
                    cur[k].setdefault(tn, Integer(0))
                    cur[k][tn] = expand(cur[k][tn] + tv)
        Xpow[n] = cur

    # log(1 + X) = Σ_{n≥1} (-1)^{n+1}/n · X^n
    logF = {}  # logF[k] = {n: coef of T^n in [E_3^k] log(F/f)}
    for n in range(1, K_MAX + 1):
        sign = Rational((-1)**(n+1), n)
        Xn = Xpow[n]
        for k, tser in Xn.items():
            if k not in logF:
                logF[k] = {}
            for tn, tv in tser.items():
                logF[k].setdefault(tn, Integer(0))
                logF[k][tn] = expand(logF[k][tn] + sign * tv)

    # Print N_k(T) = logF[k] for k = 1, 2, 3, 4, 5
    print("\n" + "=" * 78)
    print("Cumulants N_k(T) := [E_3^k] log(F_P/f)")
    print("=" * 78)
    for k in sorted(logF.keys()):
        print(f"\n--- N_{k}(T) ---")
        for n in sorted(logF[k].keys()):
            val = logF[k][n]
            if val != 0:
                print(f"  [T^{n}] N_{k} = {factor(val)}")

if __name__ == '__main__':
    main()

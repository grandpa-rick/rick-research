"""
P_b in (u, v, E_3) coordinates: E_1 = u + v, E_2 = uv.
Then p_b = (u+1)_b (v+1)_b and φ_1 = (u+1)(v+1).

Compute r_b^(k) = [E_3^k] P_b in (u, v), factor, look for structure.

Then compute U_b(w) = (P_b|_{E_3 = w - φ_1} - p_b)/(w - φ_1) in (u, v, w).
Since φ_1 = (u+1)(v+1), the shift E_3 = w - (u+1)(v+1) might make things clean.
"""

import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day140_interior')
from verify_gf_form import build_P, phi_k, p_b_fn, E1, E2, E3, w
from sympy import (symbols, expand, factor, Poly, Integer, Rational,
                    simplify, rf, together, collect, cancel, div)

u, v = symbols('u v')

def to_uv(P):
    return expand(P.subs([(E1, u + v), (E2, u * v)], simultaneous=True))

def main():
    B_MAX = 8
    print(f"Building P_b for b = 0..{B_MAX} (P_b = φ(Ψ_b))\n")
    P = build_P(B_MAX)

    P_uv = {b: to_uv(P[b]) for b in P}

    # Extract r_b^(k) = [E_3^k] P_b in (u, v)
    print("=" * 78)
    print("r_b^(k) = [E_3^k] P_b in (u, v):")
    print("=" * 78)
    r_data = {}
    for b in range(B_MAX + 1):
        pd = {}
        Pp = Poly(P_uv[b], E3)
        for k in range(b // 2 + 1):
            pd[k] = expand(Pp.coeff_monomial(E3**k))
        r_data[b] = pd
        print(f"\n--- b = {b} ---")
        for k in sorted(pd.keys()):
            r = pd[k]
            if r == 0: continue
            print(f"  r_{b}^({k})  =  {factor(r)}")

    # Now compute U_b(w) in (u, v, w) — the KEY question
    # U_b(w) = (P_b|_{E_3=w-φ_1} - p_b)/(w-φ_1)
    phi_1_uv = (u + 1) * (v + 1)
    p_b_uv = {b: expand(rf(u + 1, b) * rf(v + 1, b)) for b in range(B_MAX + 1)}

    print("\n" + "=" * 78)
    print("U_b(w) in (u, v, w) coordinates:")
    print("=" * 78)
    U = {}
    for b in range(2, B_MAX + 1):
        Pshift = expand(P_uv[b].subs(E3, w - phi_1_uv))
        numer = expand(Pshift - p_b_uv[b])
        q, r = div(numer, w - phi_1_uv, w)
        if expand(r) != 0:
            print(f"  b={b}: FAIL remainder = {r}")
            continue
        U[b] = expand(q)
        print(f"\n--- b = {b} ---")
        Uq = Poly(U[b], w)
        for d in range(Uq.degree() + 1):
            c = Uq.coeff_monomial(w**d)
            if c != 0:
                print(f"  [w^{d}] U_{b}(w) = {factor(c)}")

if __name__ == '__main__':
    main()

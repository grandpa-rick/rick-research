"""Find the closed form of F_140(T) = Σ P_b(E1,E2,E3) T^b/b! (Day 140's P).

We know P_140 = phi_map(Psi_130) where phi_map: E1→-E1, E3→-E3.
Actually, that assumption may be wrong. Let me check by comparing P_1 values.

Day 130: P_1 (top-weight of Ψ(e_2^1)) = ?

Actually let's just directly factor F_140 numerically.
"""

import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day140_interior')
from verify_gf_form import build_P, phi_k, p_b_fn, E1, E2, E3

from sympy import symbols, expand, Poly, Integer, factorial, Rational, log, exp, Symbol, series, factor, cancel

T = symbols('T')

def main():
    B_MAX = 7
    P = build_P(B_MAX)

    # Slice at E3=0: gives H(T) = Σ p_b T^b/b!
    print("Compute H(T) as a series in T:")
    H = Integer(0)
    for b in range(B_MAX+1):
        H += P[b].subs(E3, 0) * T**b / factorial(b)
    H = expand(H)

    # Take log of H
    print("\nlog H(T), expanded in T:")
    # log H = log(1 + (H-1)) = Σ_{k≥1} (-1)^{k-1} (H-1)^k / k
    Hm1 = expand(H - 1)
    logH = Integer(0)
    current = Integer(1)
    ORDER = B_MAX
    for k in range(1, ORDER+1):
        current = expand(current * Hm1)
        # Truncate
        cur_poly = Poly(current, T)
        current_trunc = Integer(0)
        for deg, coef in cur_poly.as_dict().items():
            if deg[0] <= ORDER:
                current_trunc += coef * T**deg[0]
        current = expand(current_trunc)
        logH += (-1)**(k-1) * current / k
    logH = expand(logH)
    for n in range(ORDER+1):
        c = Poly(logH, T).as_dict().get((n,), Integer(0))
        print(f"  T^{n}: {factor(expand(c))}")

    # Also try log of F(T) at E3 = 0.
    # If H(T) = (1 - E1 T)^{-α - 1} · (something), we'd see it in log H expansion.
    # log((1 - E1 T)^{-α - 1}) = -(-α-1) Σ (E1 T)^k / k = (α+1) Σ (E1 T)^k / k
    # For α = E2/E1: coef of T^k in log H would be (E2/E1 + 1) E1^k/k = (E2 + E1) E1^{k-1}/k.
    # Let's see if that matches.

    # Now for F_140(T) full: extract linear in E3 term and see if it factorizes.
    print("\n\nBuild F_140(T) truncated to E3^1, i.e., ∂F/∂E3 at E3=0, times T^b/b!:")
    dFdE3 = Integer(0)
    for b in range(B_MAX+1):
        # Coefficient of E3^1 in P_b
        c = Poly(P[b], E3).as_dict().get((1,), Integer(0))
        dFdE3 += c * T**b / factorial(b)
    dFdE3 = expand(dFdE3)

    # If F = H · exp(E3 · M), then dF/dE3|_{E3=0} = H · M, so M = dF/dE3|_{E3=0} / H.
    M_candidate = expand(dFdE3 / H)
    # Truncate to poly-in-T series
    # H(0) = 1, so 1/H(T) is a power series.
    # Compute 1/H as inverse series
    invH = Integer(1)
    Hm1 = expand(H - 1)
    powHm1 = Integer(1)
    for k in range(1, ORDER+1):
        powHm1 = expand(powHm1 * (-Hm1))
        # Truncate
        cur_poly = Poly(powHm1, T)
        trunc = Integer(0)
        for deg, coef in cur_poly.as_dict().items():
            if deg[0] <= ORDER:
                trunc += coef * T**deg[0]
        powHm1 = expand(trunc)
        invH += powHm1
    invH = expand(invH)
    # Verify invH · H = 1 + O(T^{ORDER+1})
    check = expand(H * invH)
    check_poly = Poly(check, T)
    print(f"H * invH truncated: {check_poly.as_dict()}")

    M_series = expand(dFdE3 * invH)
    # Truncate
    Mp = Poly(M_series, T)
    print("\n\nM(T) := dF/dE3|_{E3=0} / H(T), truncated:")
    for n in range(ORDER+1):
        c = Mp.as_dict().get((n,), Integer(0))
        print(f"  T^{n}: {factor(expand(c))}")

    # Now check higher powers of E3: is F = H(T) · exp(E3 M(T))?
    # I.e., is [E3^2] F / H equal to M^2/2 · H⁻¹? Wait, if F = H exp(E3 M), then
    # [E3^k] F = H · M^k / k!.
    # So check: [E3^2] F(T)/H(T) should equal M(T)^2 / 2.
    print("\n\nCheck: [E3^2] F(T) / H(T) vs M(T)^2 / 2:")
    d2FdE3 = Integer(0)
    for b in range(B_MAX+1):
        c = Poly(P[b], E3).as_dict().get((2,), Integer(0))
        d2FdE3 += c * T**b / factorial(b)
    d2FdE3 = expand(d2FdE3)
    lhs = expand(d2FdE3 * invH)
    # Truncate
    lp = Poly(lhs, T)
    lhs_t = Integer(0)
    for deg, coef in lp.as_dict().items():
        if deg[0] <= ORDER:
            lhs_t += coef * T**deg[0]
    lhs = expand(lhs_t)
    rhs = expand(M_series**2 / 2)
    rp = Poly(rhs, T)
    rhs_t = Integer(0)
    for deg, coef in rp.as_dict().items():
        if deg[0] <= ORDER:
            rhs_t += coef * T**deg[0]
    rhs = expand(rhs_t)
    diff = expand(lhs - rhs)
    print(f"  diff (should be 0 if F factors as H exp(E3 M)): {diff}")


if __name__ == '__main__':
    main()

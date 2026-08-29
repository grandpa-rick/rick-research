"""Day 130 — Correct sign in L(T) and verify."""
import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day127')
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day128')

from lib import s, t, u1, u2, u3
from task1_psi_e2_b5_b6 import (Psi_direct, sym_to_ebasis_direct,
                                 top_weight_part, e1_u, e2_u, e3_u, E1, E2, E3)
from sympy import (symbols, expand, Poly, Integer, S, Rational, binomial,
                    factorial, log, exp, cancel, together, simplify,
                    factor, Symbol, sqrt, series as sser)

T_ = Symbol('T_')

def Pb(b):
    if b == 0:
        return Integer(1)
    psi_u = Psi_direct(e2_u**b)
    psi_e = sym_to_ebasis_direct(psi_u)
    return top_weight_part(psi_e, b)


def main():
    N = 6
    Ps = [Pb(b) for b in range(N+1)]
    F = sum(Ps[b] * T_**b / factorial(b) for b in range(N+1))

    # Corrected L(T):
    # L(T) = E3 * [ T/(E1*(1+E1 T)^2)  -  log(1+E1 T)/E1^2 ]
    L_predicted = E3 * (T_/(E1 * (1 + E1*T_)**2) - log(1 + E1*T_)/E1**2)

    L_series = sser(L_predicted, T_, 0, N+1).removeO()
    print("Predicted L(T) series:")
    for n in range(N+1):
        c = expand(L_series.coeff(T_, n))
        print(f"  T^{n}: {c}")

    # Full EGF check
    alpha = E2/E1 - 1
    y = E1 * T_
    A = (1 + y)**alpha
    A_series = sser(A, T_, 0, N+1).removeO()
    expL_series = sser(exp(L_predicted), T_, 0, N+1).removeO()
    F_predicted = expand(A_series * expL_series)
    F_predicted_trunc = Integer(0)
    for n in range(N+1):
        F_predicted_trunc += expand(F_predicted.coeff(T_, n)) * T_**n

    print("\nComparing predicted F vs actual F:")
    all_match = True
    for n in range(N+1):
        pred_coef = expand(F_predicted_trunc.coeff(T_, n))
        actual_coef = expand(F.coeff(T_, n))
        diff = expand(pred_coef - actual_coef)
        status = 'MATCH' if diff == 0 else f'MISMATCH  diff={diff}'
        print(f"  T^{n}: {status}")
        if diff != 0:
            all_match = False

    if all_match:
        print("\n" + "="*70)
        print("  FULL EGF FACTORIZATION VERIFIED THROUGH T^6:")
        print("  ")
        print("    F(T) = (1 + T*E1)^{E2/E1 - 1} * exp( E3 * ( T / (E1*(1+E1*T)^2) - log(1 + E1*T)/E1^2 ) )")
        print("  ")
        print("  Equivalently, with y = E1*T:")
        print("    F(T) = (1+y)^{E2/E1 - 1} * exp( (E3/E1^2) * ( y/(1+y)^2 - log(1+y) ) )")
        print("="*70)


if __name__ == '__main__':
    main()

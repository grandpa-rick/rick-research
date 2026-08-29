"""Day 130 — Verify the beautiful factorization:
   EGF(T) = (1 + T E1)^{E2/E1 - 1} * exp(L(T))
where L(T) = sum_{n>=2} (-1)^{n-1} (n^2 - 1)/n * E1^{n-2} E3 * T^n

Try to close-form L(T). Note L is LINEAR in E3! So:
   L(T) = E3 * M(T, E1)
where M(T, E1) = sum_{n>=2} (-1)^{n-1} (n+1)(n-1)/n * E1^{n-2} * T^n
             = sum_{n>=2} (-1)^{n-1} (n - 1/n) * E1^{n-2} * T^n

Try to sum this.
Let u = -E1 T. Then:
  M(T, E1) = sum_{n>=2} (-1)^{n-1} (n^2-1)/n * (u/-E1)^{n-2} * T^n / E1^{n-2}... eugh, redo.
Cleaner: let x = -E1 T (so x^n = (-1)^n E1^n T^n).
  E1^{n-2} * T^n = (-x)^{n-2} * (-1)^{n-2} * T^2 * (T/(-1))^{... } hmm.
  Actually: E1^{n-2} T^n = T^2 * (E1 T)^{n-2} = T^2 * (-x)^{n-2}.
  So M(T, E1) = T^2 * sum_{n>=2} (-1)^{n-1} (n^2-1)/n * (-x)^{n-2}
             = T^2 * sum_{n>=2} (-1)^{n-1} (n^2-1)/n * (-1)^{n-2} * (E1 T)^{n-2}
             = T^2 * sum_{n>=2} (-1)^{2n-3} (n^2-1)/n * (E1 T)^{n-2}
             = -T^2 * sum_{n>=2} (n^2-1)/n * (E1 T)^{n-2}
Let m = n - 2, y = E1 T:
             = -T^2 * sum_{m>=0} ((m+2)^2 - 1)/(m+2) * y^m
             = -T^2 * sum_{m>=0} (m+1)(m+3)/(m+2) * y^m
             = -T^2 * sum_{m>=0} (m+1)(m+3)/(m+2) * y^m

Now (m+1)(m+3)/(m+2) = ((m+2)^2 - 1)/(m+2) = (m+2) - 1/(m+2).
So sum_m [(m+2) - 1/(m+2)] y^m
   = sum_m (m+2) y^m - sum_m y^m/(m+2)

sum_m (m+2) y^m = sum_m m y^m + 2 sum_m y^m = y/(1-y)^2 + 2/(1-y)
                = (y + 2(1-y))/(1-y)^2 = (2 - y)/(1-y)^2.

sum_m y^m / (m+2). Let S(y) = sum_{m>=0} y^m/(m+2). Then y^2 S(y) = sum_{m>=0} y^{m+2}/(m+2) = sum_{k>=2} y^k/k = -log(1-y) - y.
So S(y) = (-log(1-y) - y)/y^2 for y != 0.

Therefore
  M(T, E1) = -T^2 [ (2 - y)/(1-y)^2  -  (-log(1-y) - y)/y^2 ]
where y = E1 T.

Simplify: -T^2 (2-y)/(1-y)^2 + T^2 (-log(1-y) - y)/y^2
        = -T^2 (2-y)/(1-y)^2 - (T^2 log(1-y) + T^2 y)/y^2
        = -T^2 (2-y)/(1-y)^2 - log(1-y)/E1^2 - T/E1
  (since T^2/y^2 = T^2/(E1^2 T^2) = 1/E1^2, T^2 y / y^2 = T^2 / y = T/E1)

So L(T) = E3 * M(T, E1)
       = -E3 [ T^2 (2 - E1 T)/(1 - E1 T)^2  +  (1/E1^2) log(1 - E1 T)  +  T/E1 ]

Verify numerically.
"""
import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day127')
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day128')

from lib import s, y as ylib, t, u1, u2, u3
from task1_psi_e2_b5_b6 import (Psi_direct, sym_to_ebasis_direct,
                                 top_weight_part, e1_u, e2_u, e3_u, E1, E2, E3)
from sympy import (symbols, expand, Poly, Integer, S, Rational, binomial,
                    factorial, series, log, exp, cancel, together, simplify,
                    factor, Symbol, sqrt, collect, apart, series as sser)

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

    # Predicted:
    # EGF = (1 + T E1)^{E2/E1 - 1} * exp( -E3 * [ T^2 (2 - E1 T)/(1-E1 T)^2 + log(1-E1 T)/E1^2 + T/E1 ] )
    # But powers of T outside the log part: T^2, T (from T/E1), so we need to make sure this is regular at T=0.
    # T/E1 has no negative powers of T, so it's fine as a polynomial in T with 1/E1 coefficient.
    # log(1 - E1 T)/E1^2 = -sum_{k>=1} (E1 T)^k/(k E1^2) = -sum T^k E1^{k-2}/k --- for k=1 gives -T/E1, k=2 gives -T^2/2, etc.
    # So log(1 - E1 T)/E1^2 + T/E1 = -sum_{k>=2} T^k E1^{k-2}/k.
    # That's fine.

    y = E1 * T_
    M_predicted = -T_**2 * (2 - y)/(1 - y)**2 - log(1 - y)/E1**2 - T_/E1
    L_predicted = E3 * M_predicted

    # Series expand
    L_series = sser(L_predicted, T_, 0, N+1).removeO()
    L_series = expand(L_series)
    print("Predicted L(T) series:")
    for n in range(N+1):
        c = expand(L_series.coeff(T_, n))
        print(f"  T^{n}: {c}")

    # Expected from data: L(T) = sum_{n>=2} (-1)^{n-1} (n^2-1)/n * E1^{n-2} E3 * T^n
    print("\nExpected L(T) from log G:")
    for n in range(N+1):
        if n < 2:
            expected = 0
        else:
            expected = Rational((-1)**(n-1) * (n**2 - 1), n) * E1**(n-2) * E3
        print(f"  T^{n}: {expected}")

    # Now check: exp(L_predicted) * (1 + T E1)^{E2/E1 - 1} should equal F up to O(T^{N+1}).
    # Compute this via series.
    alpha = E2/E1 - 1
    A = (1 + y)**alpha  # (1 + T E1)^{E2/E1 - 1}
    A_series = sser(A, T_, 0, N+1).removeO()
    expL_series = sser(exp(L_predicted), T_, 0, N+1).removeO()
    F_predicted = expand(A_series * expL_series)
    # Truncate to O(T^{N+1})
    F_predicted_trunc = Integer(0)
    for n in range(N+1):
        F_predicted_trunc += expand(F_predicted.coeff(T_, n)) * T_**n

    print("\nComparing predicted F vs actual F:")
    for n in range(N+1):
        pred_coef = expand(F_predicted_trunc.coeff(T_, n))
        actual_coef = expand(F.coeff(T_, n))
        diff = expand(pred_coef - actual_coef)
        print(f"  T^{n}: {'MATCH' if diff == 0 else f'MISMATCH  diff={diff}'}")


if __name__ == '__main__':
    main()

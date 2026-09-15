"""Try to find general formula for e_3 ⋆ e_r coefficients.

By analogy with e_2 ⋆ e_r:
   e_2 ⋆ e_r = q^{-2} e_{r,2} + (q-1)/q^2 [r]_t e_{r+1,1} + (q-1)([r+2]_t/[2]_t)([r+1]_t - t[r-1]_t/q)/q e_{r+2}
   Wait let me re-derive: Day 191 said
   e_2 ⋆ e_r = q^{-2} e_2·e_r + q^{-1}(q-1)/q · [r]_t · e_1·e_{r+1} + (q-1)·([r+2]_t/[2]_t)·([r+1]_t - t[r-1]_t/q) · e_{r+2}
   Actually memory says: "three terms in pattern q^{-k(2-k)}·[stuff]_t·e_{r+2-k,k}, k=0,1,2".
   q^{-k(2-k)} = q^0 for k=0 or k=2, q^{-1} for k=1. So c_0 has no q pole? But we see q^{-2}... let me re-check.

For e_3 ⋆ e_r we observe q^{-3} in c_3, c_2, c_1, c_0 (each has denominator q^3).
So the natural normalization: coefficient c_k appears with q^{-3} baseline.
c_k(r) = q^{-3} * P_k(q, t; r), P_k in Z[q,t].
"""

import sympy as sp

q, t = sp.symbols('q t')


def qint(n):
    return sum(t**i for i in range(n))


# Data from computation (r, k) -> raw coefficient
data = {
    (1, 0): (q - 1)*(t + 1)*(t**2 + 1)/q,
    (1, 1): sp.Rational(1)/q,
    (2, 0): (q - 1)*(q*t**2 + q - t)*(t**4 + t**3 + t**2 + t + 1)/q**2,
    (2, 1): (q - 1)*(t**2 + t + 1)/q**2,
    (2, 2): sp.Rational(1)/q**2,
    (3, 0): (q - 1)*(t + 1)*(t**2 - t + 1)*(q**2*t**6 + q**2*t**5 + 2*q**2*t**4 + 2*q**2*t**3 + 2*q**2*t**2 + q**2*t + q**2 - q*t**5 - 2*q*t**4 - 2*q*t**3 - 2*q*t**2 - q*t + t**3)/q**3,
    (3, 1): (q - 1)*(t**2 + 1)*(q*t**2 + q*t + q - t)/q**3,
    (3, 2): (q - 1)*(t + 1)/q**3,
    (3, 3): sp.Rational(1)/q**3,
    (4, 0): (q - 1)*(t**6 + t**5 + t**4 + t**3 + t**2 + t + 1)*(q**2*t**6 + q**2*t**4 + q**2*t**3 + q**2*t**2 + q**2 - q*t**5 - q*t**4 - q*t**3 - q*t**2 - q*t + t**3)/q**3,
    (4, 1): (q - 1)*(q*t**2 + q - t)*(t**4 + t**3 + t**2 + t + 1)/q**3,
    (4, 2): (q - 1)*(t**2 + t + 1)/q**3,
    (4, 3): sp.Rational(1)/q**3,
    (5, 0): (q - 1)*(t + 1)*(t**2 + 1)*(t**4 + 1)*(q**2*t**8 + q**2*t**6 + q**2*t**5 + q**2*t**4 + q**2*t**3 + q**2*t**2 + q**2 - q*t**7 - q*t**6 - q*t**5 - 2*q*t**4 - q*t**3 - q*t**2 - q*t + t**5 + t**3)/q**3,
    (5, 1): (q - 1)*(t**2 - t + 1)*(t**2 + t + 1)*(q*t**4 + q*t**3 + q*t**2 + q*t + q - t**3 - t**2 - t)/q**3,
    (5, 2): (q - 1)*(t + 1)*(t**2 + 1)/q**3,
    (5, 3): sp.Rational(1)/q**3,
}


def check_pattern():
    # Pattern check for c_3(r): expect q^{-3}
    print("=== c_3(r) [coeff of e_{r,3}, for r >= 3] ===")
    for r in [3, 4, 5]:
        c = sp.factor(data[(r, 3)])
        print(f"  r={r}: c_3 = {c}")
    print()

    # c_2(r): guess (q-1)[r-1]_t / q^3 for r >= 3
    print("=== c_2(r) [coeff of e_{r+1,2}] ===")
    for r in [3, 4, 5]:
        c = sp.simplify(data[(r, 2)])
        guess = (q - 1) * qint(r - 1) / q**3
        diff = sp.simplify(c - guess)
        print(f"  r={r}: c_2 = {sp.factor(c)}")
        print(f"         guess (q-1)[r-1]_t/q^3 = {sp.factor(guess)}, diff = {diff}")
    # For r=2:
    print(f"  r=2: c_2 = {sp.factor(data[(2, 2)])} vs guess (q-1)[1]_t/q^3 = {(q-1)*1/q**3}")
    # No: c_2(2) = q^{-2} for the smaller case.  This is c_2 at k=2 (which is min(3,2)=2, so it's the "bottom" term).
    print("   [At r=2 the k=2 term is the 'bottom' one, so different formula.]")
    print()

    # c_1(r) guess: (q-1)·something · [something]_t · e_{r+2,1}
    print("=== c_1(r) [coeff of e_{r+2,1}] ===")
    for r in [2, 3, 4, 5]:
        c = sp.simplify(data[(r, 1)])
        print(f"  r={r}: c_1 = {sp.factor(c)}")

    # Try to guess: for r>=3, c_1(r) = (q-1)/q^3 * [something] with a linear-in-q factor
    # r=3: (q-1)(t^2+1)(qt^2+qt+q-t)/q^3 = (q-1)[2]_{t^2}·(q[3]_t - t)/q^3
    # r=4: (q-1)(qt^2+q-t)(t^4+t^3+t^2+t+1)/q^3 = (q-1)·[5]_t·(q(1+t^2)-t)/q^3
    # r=5: (q-1)(t^2-t+1)(t^2+t+1)(qt^4+qt^3+qt^2+qt+q-t^3-t^2-t)/q^3
    #    = (q-1)(t^4+t^2+1)·(q[5]_t - t[3]_t)/q^3 = (q-1)([6]_t/[2]_t)·(q[5]_t - t[3]_t)/q^3
    # Pattern: c_1(r) = (q-1)([r+2]_t/[2]_t)(q[r+1]_t - t[r-1]_t)/q^3 for r>=?
    print("\n  Testing guess c_1(r) = (q-1)([r+2]_t/[2]_t)·(q[r+1]_t - t[r-1]_t)/q^3")
    for r in [3, 4, 5]:
        c = sp.simplify(data[(r, 1)])
        guess = (q - 1) * (qint(r + 2) / qint(2)) * (q * qint(r + 1) - t * qint(r - 1)) / q**3
        diff = sp.simplify(c - guess)
        print(f"    r={r}: diff = {diff}")
    # Also try r=2:
    r = 2
    guess = (q - 1) * (qint(r + 2) / qint(2)) * (q * qint(r + 1) - t * qint(r - 1)) / q**3
    diff = sp.simplify(data[(r, 1)] - guess)
    print(f"    r={r} (extrapolation): diff = {diff}")
    # r=1:
    r = 1
    guess = (q - 1) * (qint(r + 2) / qint(2)) * (q * qint(r + 1) - t * qint(r - 1)) / q**3
    diff = sp.simplify(data[(r, 1)] - guess)
    print(f"    r={r} (extrapolation): diff = {diff}")


if __name__ == "__main__":
    check_pattern()

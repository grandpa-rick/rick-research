"""Test whether Q_k(a,b,c) extends into the boundary regime k > c-1.

Conjecture: For any k, Q_k(a,b,c) defined by the sum formula
    Q_k(a,b,c) = sum_{j=0..k} (-1)^{k-j} C(k,j) (a+c-k+2)_{k-j} (b+c-k+1)_{k-j} P_j(a,b,c)
gives, upon multiplication by (a+3)_{c-1-k}(b+2)_{c-1-k} (interpreted as inverse
Pochhammer when c-1-k < 0), the true h_k^{(c)}(a,b).

Equivalently: h_k^{(c)}(a,b) * (a+c-k+2)_m (b+c-k+1)_m = Q_k(a,b,c) where m = k-c+1
(the m Pochhammer factors that inverted).

So: Q_k(a,b,c) should be divisible by (a+c-k+2)_m (b+c-k+1)_m in the boundary
regime, iff (which we're testing) h_k^{(c)}(a,b) equals that "reduced" quotient.

Simpler direct test: compute h_k^{(c)}(a,b) via extract_h_k, and check if
    h_k^{(c)}(a,b) * (a+c-k+2)_m * (b+c-k+1)_m
matches the Q_k values that (Q_k formula) predicts.
"""
import sys
sys.path.insert(0, '/home/agent/projects/code')
from importlib import import_module
mod = import_module('2026-07-10-hk-three-var-verify')
build_e2_tables = mod.build_e2_tables
extract_h_k = mod.extract_h_k
rising_fact = mod.rising_fact
M_j_sym = mod.M_j_sym
H_c_template = mod.H_c_template

from math import factorial
from fractions import Fraction


def C(n, k):
    if k < 0 or k > n:
        return 0
    return factorial(n) // (factorial(k) * factorial(n - k))


def P_j_direct(a, b, c, j, tables):
    """P_j(a, b, c) = M_j(a, b, c) / f^{(a,b,c)} * (n)_{2j}
    where M_j comes from the Sym-side identity (Day 86).
    Equivalent to sum_mu K R_mu, hence a polynomial in (a, b, c).
    Uses the Aitken determinant to compute f^{lambda/mu} directly.
    """
    if not (a >= b >= c >= 0):
        return None
    n = a + b + c
    if n < 2 * j:
        return 0
    if j == 0:
        return 1
    if j not in tables:
        return None
    xs = (a + 2, b + 1, c)

    def fall(x, kk):
        p = 1
        for i in range(kk):
            p *= (x - i)
        return p

    total_num = 0  # numerator over shared denominator (n)_{2j}^{-1} f^lambda ... let's just accumulate P_j
    # P_j = sum_mu K_{mu^T,(2^j)} * f^{lambda/mu} * (n)_{2j} / f^lambda
    # f^lambda = n! * D_∅ / (A! B! C!) where D_∅ = (a-b+1)(b-c+1)(a-c+2)
    # f^{lambda/mu} = (n-2j)! * D_mu / (A! B! C!)  where D_mu is the Aitken det
    # So f^{lambda/mu} * (n)_{2j} / f^lambda
    #   = (n-2j)! D_mu / (A! B! C!) * n!/(n-2j)! / (n! D_∅ / (A! B! C!))
    #   = D_mu / D_∅
    D_empty = (a - b + 1) * (b - c + 1) * (a - c + 2)
    if D_empty == 0:
        return None

    total_num = 0
    for mu, k in tables[j]:
        ks = [mu[jj] + (2 - jj) for jj in range(3)]
        M = [[fall(xs[i], ks[jj]) for jj in range(3)] for i in range(3)]
        det = (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
               - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
               + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))
        total_num += k * det

    q = Fraction(total_num, D_empty)
    if q.denominator != 1:
        return None
    return int(q)


def Q_k_from_formula(a, b, c, k, tables):
    """Q_k(a, b, c) via formula (Q_k formula):
       Q_k = sum_{j=0..k} (-1)^{k-j} C(k,j) (a+c-k+2)_{k-j} (b+c-k+1)_{k-j} P_j.
    """
    total = 0
    for j in range(k + 1):
        Pj = P_j_direct(a, b, c, j, tables)
        if Pj is None:
            return None
        pa = rising_fact(a + c - k + 2, k - j)
        pb = rising_fact(b + c - k + 1, k - j)
        sign = 1 if (k - j) % 2 == 0 else -1
        total += sign * C(k, j) * pa * pb * Pj
    return total


def h_k_ext(a, b, c, k, tables):
    """h_k^{(c)}(a, b) = sum_{j=0..k} (-1)^{k-j} C(k,j) H_c(a, b, j)."""
    total = 0
    for j in range(k + 1):
        Hc = H_c_template(a, b, c, j, tables)
        if Hc is None:
            return None
        sign = 1 if (k - j) % 2 == 0 else -1
        total += sign * C(k, j) * Hc
    return total


def main():
    tables = build_e2_tables(max_j=16)
    print("Test: In the boundary regime k > c-1, does the identity")
    print("      h_k^{(c)}(a,b) * (a+c-k+2)_m * (b+c-k+1)_m = Q_k(a,b,c)")
    print("      hold?   [m = k-c+1, so m > 0]")
    print("=" * 78)
    for c_val in [4, 5, 6, 7]:
        for k in range(c_val, 2 * c_val):
            m = k - c_val + 1
            print(f"\n--- c={c_val}, k={k}, m={m} ---")
            mismatches = 0
            checked = 0
            # Need b >= k for H_c(a,b,k) to be defined via template
            for a_val in range(k + 2, k + 12):
                for b_val in range(k, a_val + 1):
                    hk = h_k_ext(a_val, b_val, c_val, k, tables)
                    Qk = Q_k_from_formula(a_val, b_val, c_val, k, tables)
                    if hk is None or Qk is None:
                        continue
                    lhs = hk * rising_fact(a_val + c_val - k + 2, m) * rising_fact(b_val + c_val - k + 1, m)
                    checked += 1
                    if lhs != Qk:
                        mismatches += 1
                        if mismatches < 3:
                            print(f"    MISMATCH (a,b)=({a_val},{b_val}): "
                                  f"h_k*({rising_fact(a_val+c_val-k+2,m)}*{rising_fact(b_val+c_val-k+1,m)})={lhs} vs Qk={Qk}")
            print(f"    checked={checked}, mismatches={mismatches}, "
                  f"{'PASS' if mismatches == 0 else 'FAIL'}")


if __name__ == "__main__":
    main()

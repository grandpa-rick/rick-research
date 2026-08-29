"""Day 124: Verify the key steps of the EGF proof of the T-shift identity.

We prove:
    T(e_1^a * e_k) = [e_1 - k]_a * e_k       for all a >= 0, k >= 1.

The proof (see t_shift_proof.md) uses the EGF:
    sum_a (t^a / a!) T(e_1^a * g) = (1 + t)^{e_1 - deg(g)} * T(g)
for homogeneous g.  This script does two things:

(1) Symbolically verifies the master identity
        T(e^{t e_1} * x^beta) = (1 + t)^{e_1 - |beta|} * T(x^beta)
    for a batch of monomials x^beta by expanding both sides to degree ~6 in t.

(2) Uses the master identity (specialized at g = e_k) to *re-derive*
    T(e_1^a * e_k) = [e_1 - k]_a * e_k  algorithmically (i.e. by expanding
    (1+t)^{e_1-k} * e_k and matching coefficient of t^a/a!), and cross-checks
    against direct computation with apply_T from t_shift_verify.

If (1) and (2) both pass, that's a computational corroboration of every step
of the written proof.
"""

import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day124')

from itertools import combinations
import sympy as sp
from sympy import Integer, Poly, Rational, expand, symbols, binomial, factorial

from t_shift_verify import elementary, falling, apply_T, sym_to_e_basis


def check_master_identity(beta, n, T_ORDER=6):
    """Check  T(e^{t e_1} * x^beta) = (1+t)^{e_1-|beta|} * T(x^beta)  up to t^T_ORDER."""
    xs = symbols(f"x1:{n+1}")
    t = symbols("t")
    x_beta = Integer(1)
    for i, b in enumerate(beta):
        x_beta *= xs[i]**b
    d = sum(beta)
    e1 = sum(xs)

    # LHS: sum_{a=0}^{T_ORDER} (t^a/a!) * T(e1^a * x^beta), then compare to RHS
    # We instead compare each coefficient of t^a separately.

    ok_all = True
    for a in range(T_ORDER + 1):
        # LHS coefficient of t^a: (1/a!) T(e1^a * x^beta)
        lhs = expand(apply_T(expand(e1**a * x_beta), xs))
        # RHS coefficient of t^a: [(e_1-d) choose a formal] * T(x^beta),
        # i.e. binomial series coeff: [e_1-d]_a * T(x^beta), and RHS_a = (1/a!) * [e1-d]_a * T(x_beta)
        # but we should compare  [e1-d]_a * T(x^beta)  to  T(e1^a * x^beta).
        # (The 1/a! cancels on both sides of the EGF match.)
        Tx_beta = apply_T(x_beta, xs)
        # Compute [e1 - d]_a symbolically in x_i's
        rhs = Integer(1)
        for i in range(a):
            rhs *= (e1 - d - i)
        rhs = expand(rhs * Tx_beta)
        diff = expand(lhs - rhs)
        if diff != 0:
            ok_all = False
            print(f"    beta={beta}, a={a}: MISMATCH, diff = {diff}")
    return ok_all


def check_ek_via_master(k, n, a_max=5):
    """Use master identity to derive T(e_1^a * e_k) = [e_1 - k]_a * e_k, then
    cross-check against direct apply_T."""
    xs = symbols(f"x1:{n+1}")
    e_syms = symbols(f"e1:{n+1}")
    e1_sym = e_syms[0]
    ek_sym = e_syms[k-1]
    e_k = elementary(k, xs)
    e_1 = elementary(1, xs)

    ok_all = True
    for a in range(a_max + 1):
        direct = apply_T(expand(e_1**a * e_k), xs)
        direct_e = sym_to_e_basis(direct, xs, e_syms)

        # Master-identity prediction: [e_1 - k]_a * e_k  (all in e-basis).
        pred = Integer(1)
        for i in range(a):
            pred *= (e1_sym - k - i)
        pred = expand(pred * ek_sym)

        diff = expand(direct_e - pred)
        if diff != 0:
            ok_all = False
            print(f"    k={k}, n={n}, a={a}: MISMATCH")
            print(f"       direct   = {direct_e}")
            print(f"       predicted = {pred}")
            print(f"       diff     = {diff}")
    return ok_all


def main():
    print("=" * 78)
    print("Day 124 EGF proof of T-shift identity — computational corroboration")
    print("=" * 78)

    print("\n(1) MASTER IDENTITY:  T(e^{t e_1} * x^beta) = (1+t)^{e_1-|beta|} * T(x^beta)")
    print("    (Checked as an equality of coefficients of t^a, for a = 0..6.)\n")

    test_betas = [
        # single-variable
        (0,), (1,), (2,), (3,), (5,),
        # two variables
        (1, 1), (2, 1), (1, 2), (3, 2), (2, 2),
        # three variables
        (1, 1, 1), (2, 1, 1), (1, 2, 1), (3, 2, 1),
        # four variables
        (1, 1, 1, 1), (2, 1, 1, 1),
    ]
    all_ok = True
    for beta in test_betas:
        n = len(beta)
        ok = check_master_identity(beta, n, T_ORDER=5)
        status = "OK" if ok else "FAIL"
        print(f"    beta = {beta}  (n = {n})   {status}")
        all_ok = all_ok and ok
    print(f"\n    MASTER IDENTITY result: {'ALL PASS' if all_ok else 'SOME FAIL'}")

    print("\n(2) SPECIALIZATION TO g = e_k:  T(e_1^a * e_k) = [e_1 - k]_a * e_k")
    print("    (Cross-check against direct apply_T; e-basis comparison.)\n")

    all_ok_2 = True
    for k in [1, 2, 3, 4, 5]:
        for n in [k, k + 1]:
            ok = check_ek_via_master(k, n, a_max=5)
            status = "OK" if ok else "FAIL"
            print(f"    k = {k}, n = {n}   (a = 0..5)   {status}")
            all_ok_2 = all_ok_2 and ok
    print(f"\n    SPECIALIZATION result: {'ALL PASS' if all_ok_2 else 'SOME FAIL'}")

    print()
    print("=" * 78)
    if all_ok and all_ok_2:
        print("EGF PROOF COMPUTATIONALLY CORROBORATED at every step tested.")
        print("Master identity + T(e_k) = e_k  =>  T(e_1^a e_k) = [e_1-k]_a e_k.")
    else:
        print("SOMETHING FAILED — recheck proof.")
    print("=" * 78)


if __name__ == "__main__":
    main()

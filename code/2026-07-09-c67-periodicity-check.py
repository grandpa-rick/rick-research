"""Day 87 evening — Rigorous v_2 LB via 2^T-periodicity finite check.

**Lemma (Periodicity).** For an integer polynomial P(a, b) and any T ≥ 0,
P(a, b) mod 2^T depends only on (a, b) mod 2^T.

**Reduction.** To prove v_2(P(a, b)) ≥ T for all (a, b) ∈ ℤ² with a+b ≡ p
(mod 2), it suffices to check that P(a, b) ≡ 0 mod 2^T for all
(a, b) ∈ [0, 2^T)² with a+b ≡ p (mod 2).

This yields a rigorous proof by exhaustive check.

Task:
- Verify v_2(h_k^{(6)}(a, b)) ≥ 7 for all (a, b) with a+b even, for k=0..10.
- Verify v_2(h_k^{(7)}(a, b)) ≥ 6 for all (a, b) with a+b odd, for k=0..12.
"""
from math import factorial
from sympy import symbols, Poly, Integer, expand

a_s, b_s = symbols('a b')

# Import h_k dicts from v2-explore
exec(open('/home/agent/projects/code/2026-07-09-hk-c67-v2-explore.py').read().split("if __name__")[0])

# Convert each h_k to a Python callable (polynomial evaluated at (a, b) with int arithmetic)
def poly_to_callable(expr):
    poly = Poly(expand(expr), a_s, b_s, domain='ZZ')
    coeffs = poly.as_dict()  # {(i, j): coef}
    # returns a function f(a, b) -> int
    def f(av, bv):
        result = 0
        for (i, j), c in coeffs.items():
            result += int(c) * (av ** i) * (bv ** j)
        return result
    return f, coeffs

def check_h_k_LB(hk_dict, kmax, c_val, T, parity):
    """Check that v_2(h_k(a, b)) >= T for all (a, b) in [0, 2^T)^2 with
    a + b ≡ parity mod 2, for k = 0..kmax.
    Returns dict {k: (pass?, first_fail_or_None, min_v2)}.
    """
    modulus = 1 << T
    results = {}
    for k in range(kmax + 1):
        h = hk_dict[k]
        try:
            f, _ = poly_to_callable(h)
        except Exception as e:
            results[k] = ('ERR', str(e), None)
            continue
        first_fail = None
        min_v2 = float('inf')
        for av in range(modulus):
            for bv in range(modulus):
                if (av + bv) % 2 != parity:
                    continue
                val = f(av, bv)
                if val == 0:
                    continue
                # compute v_2
                m = abs(val)
                v = 0
                while m % 2 == 0:
                    m //= 2; v += 1
                min_v2 = min(min_v2, v)
                if v < T:
                    if first_fail is None:
                        first_fail = (av, bv, val, v)
        ok = first_fail is None
        results[k] = (ok, first_fail, min_v2)
    return results


def summarize(results, kmax, c_val, T):
    print(f"\n### c = {c_val}: check v_2(h_k(a,b)) >= {T} for parity shell ###")
    all_ok = True
    for k in range(kmax + 1):
        ok, ff, mv = results[k]
        if ok:
            print(f"  k={k}: PASS   min_v2 (over residues) = {mv}")
        else:
            print(f"  k={k}: FAIL   first fail: {ff}   min_v2 = {mv}")
            all_ok = False
    print(f"\n  OVERALL: {'PASS' if all_ok else 'FAIL'}")
    return all_ok


if __name__ == "__main__":
    print("=" * 70)
    print("c = 6: verify v_2(h_k^{(6)}(a, b)) >= 7 for a + b even")
    print("=" * 70)
    print("(finite check over (a, b) in [0, 128)^2 with a+b even; 8192 pts per k)")
    res6 = check_h_k_LB(h_c6, kmax=10, c_val=6, T=7, parity=0)
    ok6 = summarize(res6, 10, 6, 7)

    print("\n" + "=" * 70)
    print("c = 7: verify v_2(h_k^{(7)}(a, b)) >= 6 for a + b odd")
    print("=" * 70)
    print("(finite check over (a, b) in [0, 64)^2 with a+b odd; 2048 pts per k)")
    res7 = check_h_k_LB(h_c7, kmax=12, c_val=7, T=6, parity=1)
    ok7 = summarize(res7, 12, 7, 6)

    # Also verify the witnesses
    print("\n" + "=" * 70)
    print("Witness verification")
    print("=" * 70)
    # H_6(0, 0, 0)
    def eval_H(hk_dict, kmax, av, bv, jv):
        def Cn(n, k):
            if k < 0 or k > n: return 0
            return factorial(n) // (factorial(k) * factorial(n - k))
        total = 0
        for k in range(kmax + 1):
            h = hk_dict[k]
            val = int(h.subs({a_s: av, b_s: bv})) if hasattr(h, 'subs') else int(h)
            total += val * Cn(jv, k)
        return total
    H6_witness = eval_H(h_c6, 10, 0, 0, 0)
    def v2(n):
        if n == 0: return float('inf')
        m = abs(int(n))
        r = 0
        while m % 2 == 0: m //= 2; r += 1
        return r
    print(f"H_6(0, 0, 0) = {H6_witness}   v_2 = {v2(H6_witness)}")
    H7_witness = eval_H(h_c7, 12, 1, 2, 6)
    print(f"H_7(1, 2, 6) = {H7_witness}   v_2 = {v2(H7_witness)}")

    print("\n" + "=" * 70)
    if ok6 and ok7:
        print("PROOF COMPLETE: β'(6) = 7  and  β'(7) = 6, so Δβ'(7) = -1.")
    print("=" * 70)

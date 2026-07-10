"""Day 87 evening — c=9 case: extract v_2 LB via 2^T-periodicity.

D1 predicts Δβ'(9) = 1 − max(2, v_2(8)) = 1 − 3 = -2.
Empirical: β'(8) = 11, β'(9) = 9, so Δβ' = -2. ✓

At c = 9 we need:
- β'(9) = 9: v_2(H_9(a,b,j)) ≥ 9 for a+b even (c=9 odd, so parity = 1 mod 2, so a+b odd).

Wait: parity shell is (a+b+c) even, so a+b ≡ c mod 2 = 1 mod 2, so a+b odd.

Verify v_2 ≥ 9 mod 2^9 = 512 for all (a, b) with a+b odd.
"""
from sympy import symbols, expand, Poly
from math import factorial

a_s, b_s = symbols('a b')

# From c=9 fit output (parsed from /tmp/c9-fit.log)
h_c9 = {
    0: (a_s+3)*(a_s+4)*(a_s+5)*(a_s+6)*(a_s+7)*(a_s+8)*(a_s+9)*(a_s+10)*(b_s+2)*(b_s+3)*(b_s+4)*(b_s+5)*(b_s+6)*(b_s+7)*(b_s+8)*(b_s+9),
    1: -72*(a_s+3)*(a_s+4)*(a_s+5)*(a_s+6)*(a_s+7)*(a_s+8)*(a_s+9)*(b_s+2)*(b_s+3)*(b_s+4)*(b_s+5)*(b_s+6)*(b_s+7)*(b_s+8),
    2: -18*(a_s+3)*(a_s+4)*(a_s+5)*(a_s+6)*(a_s+7)*(a_s+8)*(b_s+2)*(b_s+3)*(b_s+4)*(b_s+5)*(b_s+6)*(b_s+7)*(a_s*b_s + a_s + 2*b_s - 222),
    3: 3024*(a_s+3)*(a_s+4)*(a_s+5)*(a_s+6)*(a_s+7)*(b_s+2)*(b_s+3)*(b_s+4)*(b_s+5)*(b_s+6)*(a_s*b_s + a_s + 2*b_s - 54),
    4: 864*(a_s+3)*(a_s+4)*(a_s+5)*(a_s+6)*(b_s+2)*(b_s+3)*(b_s+4)*(b_s+5)*(a_s**2*b_s**2 + a_s**2*b_s + 3*a_s*b_s**2 - 291*a_s*b_s - 294*a_s + 2*b_s**2 - 586*b_s + 5292),
    5: -181440*(a_s+3)*(a_s+4)*(a_s+5)*(b_s+2)*(b_s+3)*(b_s+4)*(a_s**2*b_s**2 + a_s**2*b_s + 3*a_s*b_s**2 - 67*a_s*b_s - 70*a_s + 2*b_s**2 - 138*b_s + 420),
    6: -60480*(a_s+3)*(a_s+4)*(b_s+2)*(b_s+3)*(a_s**3*b_s**3 - a_s**3*b_s + 3*a_s**2*b_s**3 - 270*a_s**2*b_s**2 - 273*a_s**2*b_s + 2*a_s*b_s**3 - 810*a_s*b_s**2 + 5488*a_s*b_s + 6300*a_s - 540*b_s**2 + 12060*b_s - 7560),
    7: 12700800*(a_s+3)*(b_s+2)*(a_s**3*b_s**3 - a_s**3*b_s + 3*a_s**2*b_s**3 - 60*a_s**2*b_s**2 - 63*a_s**2*b_s + 2*a_s*b_s**3 - 180*a_s*b_s**2 + 322*a_s*b_s + 504*a_s - 120*b_s**2 + 888*b_s + 432),
    8: 5080320*(a_s**4*b_s**4 - 2*a_s**4*b_s**3 - a_s**4*b_s**2 + 2*a_s**4*b_s + 2*a_s**3*b_s**4 - 204*a_s**3*b_s**3 - 2*a_s**3*b_s**2 + 204*a_s**3*b_s - a_s**2*b_s**4 - 598*a_s**2*b_s**3 + 3601*a_s**2*b_s**2 + 4198*a_s**2*b_s - 2*a_s*b_s**4 - 396*a_s*b_s**3 + 10802*a_s*b_s**2 + 1116*a_s*b_s - 10080*a_s + 7200*b_s**2 - 12960*b_s - 17280),
    9: -914457600*(a_s**3*b_s**3 - 3*a_s**3*b_s**2 + 2*a_s**3*b_s - 40*a_s**2*b_s**2 + 40*a_s**2*b_s - a_s*b_s**3 - 37*a_s*b_s**2 + 254*a_s*b_s + 216*b_s - 144),
    10: -457228800*(a_s**3*b_s**3 - 6*a_s**3*b_s**2 + 11*a_s**3*b_s - 6*a_s**3 - 3*a_s**2*b_s**3 - 102*a_s**2*b_s**2 + 327*a_s**2*b_s - 222*a_s**2 + 2*a_s*b_s**3 + 108*a_s*b_s**2 + 862*a_s*b_s - 972*a_s - 1440),
    11: 60354201600*(a_s**2*b_s**2 - 5*a_s**2*b_s + 6*a_s**2 - 3*a_s*b_s**2 - 5*a_s*b_s + 22*a_s + 2*b_s**2 + 10*b_s + 12),
    12: 40236134400*(a_s**2*b_s**2 - 7*a_s**2*b_s + 12*a_s**2 - 5*a_s*b_s**2 - 19*a_s*b_s + 102*a_s + 6*b_s**2 + 66*b_s - 72),
    13: -3138418483200*(a_s*b_s - 4*a_s - 3*b_s + 6),
    14: -3138418483200*(a_s*b_s - 5*a_s - 4*b_s + 6),
    15: 94152554496000,
    16: 188305108992000,
}


def v2(n):
    if n == 0: return float('inf')
    m = abs(int(n))
    r = 0
    while m % 2 == 0: m //= 2; r += 1
    return r


def Cn(n, k):
    if k < 0 or k > n: return 0
    return factorial(n) // (factorial(k) * factorial(n - k))


def poly_to_coeffs_list(expr):
    """Return list of (i, j, coef) tuples for expr as polynomial in a_s, b_s."""
    poly = Poly(expand(expr), a_s, b_s, domain='ZZ')
    d = poly.as_dict()
    return [(k[0], k[1], int(c)) for k, c in d.items()]


def check_h_k_LB_c9(hk_dict, kmax, T=9, parity=1):
    """Check v_2(h_k(a, b)) >= T for all (a, b) in [0, 2^T)^2 with a+b ≡ parity mod 2.

    Optimization: work mod 2^T throughout, using precomputed coefficient lists.
    """
    modulus = 1 << T
    results = {}
    for k in range(kmax + 1):
        h = hk_dict[k]
        coeffs = poly_to_coeffs_list(h)
        # Reduce coeffs mod 2^T
        coeffs_mod = [(i, j, c % modulus) for i, j, c in coeffs]
        # Evaluate for each (a, b) mod modulus
        first_fail = None
        min_v2 = float('inf')
        for av in range(modulus):
            for bv in range(modulus):
                if (av + bv) % 2 != parity:
                    continue
                val = 0
                for i, j, c in coeffs_mod:
                    val = (val + c * pow(av, i, modulus) * pow(bv, j, modulus)) % modulus
                if val == 0:
                    continue
                # v_2 of nonzero value mod 2^T
                v = 0
                mm = val
                while mm % 2 == 0:
                    mm //= 2; v += 1
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


def eval_H(hk_dict, kmax, av, bv, jv):
    total = 0
    for k in range(kmax + 1):
        h = hk_dict[k]
        val = int(h.subs({a_s: av, b_s: bv})) if hasattr(h, 'subs') else int(h)
        total += val * Cn(jv, k)
    return total


def find_witness_c9(hk_dict, kmax, arange=30, brange=30, jrange=20):
    """Brute-force min v_2 over (a,b,j) with a+b odd."""
    best = float('inf')
    witness = None
    for av in range(arange):
        for bv in range(brange):
            if (av + bv) % 2 == 0:  # parity shell for c=9: a+b odd
                continue
            for jv in range(jrange):
                val = eval_H(hk_dict, kmax, av, bv, jv)
                if val == 0:
                    continue
                v = v2(val)
                if v < best:
                    best = v
                    witness = (av, bv, jv, val)
    return best, witness


if __name__ == "__main__":
    print("=" * 70)
    print("c = 9: verify v_2(h_k^{(9)}(a, b)) >= 9 for a + b odd (parity shell)")
    print("=" * 70)
    print("(finite check over (a, b) in [0, 512)^2 with a+b odd; 131072 pts per k)")
    print("(17 h_k terms, ~2.2M residue evaluations. Will take a few minutes.)")
    import time
    t0 = time.time()
    res9 = check_h_k_LB_c9(h_c9, kmax=16, T=9, parity=1)
    print(f"\n  (elapsed: {time.time() - t0:.1f} sec)")
    ok9 = summarize(res9, 16, 9, 9)

    # Witness search
    print("\n" + "=" * 70)
    print("Witness search: min v_2(H_9(a, b, j)) over small (a, b, j) with a+b odd")
    print("=" * 70)
    m9, w9 = find_witness_c9(h_c9, 16, arange=30, brange=30, jrange=20)
    print(f"  Best: v_2 = {m9}, witness = {w9}")

    print("\n" + "=" * 70)
    if ok9 and m9 == 9:
        print(f"β'(9) = 9 ✓ (matches D1 prediction: Δβ'(9) = 1 - v_2(8) = -2 assuming β'(8) = 11).")
    else:
        print(f"MISMATCH: LB min = {res9[0][2] if 0 in res9 else '?'}, witness v_2 = {m9}")
    print("=" * 70)

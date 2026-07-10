"""Day 87 evening — Explore v_2 structure of h_k^{(6)} and h_k^{(7)} and
brute-force min v_2(H_c) to find witnesses of β'(6)=7, β'(7)=6.
"""
from math import factorial
from sympy import symbols, expand, factor, sympify

a, b = symbols('a b')

# From c67-fit run
h_c6 = {
    0: (a+3)*(a+4)*(a+5)*(a+6)*(a+7)*(b+2)*(b+3)*(b+4)*(b+5)*(b+6),
    1: -30*(a+3)*(a+4)*(a+5)*(a+6)*(b+2)*(b+3)*(b+4)*(b+5),
    2: -12*(a+3)*(a+4)*(a+5)*(b+2)*(b+3)*(b+4)*(a*b + a + 2*b - 48),
    3: 720*(a+3)*(a+4)*(b+2)*(b+3)*(a*b + a + 2*b - 8),
    4: 360*(a+3)*(b+2)*(a**2*b**2 + a**2*b + 3*a*b**2 - 45*a*b - 48*a + 2*b**2 - 94*b + 24),
    5: -21600*(a**2*b**2 + a**2*b + 3*a*b**2 - 5*a*b - 8*a + 2*b**2 - 14*b - 12),
    6: -14400*(a**2*b**2 - a**2*b + a*b**2 - 28*a*b - 27*b + 36),
    7: 604800*(a*b - a - 3),
    8: 604800*(a*b - 2*a - b - 6),
    9: -10886400,
    10: -21772800,
}

h_c7 = {
    0: (a+3)*(a+4)*(a+5)*(a+6)*(a+7)*(a+8)*(b+2)*(b+3)*(b+4)*(b+5)*(b+6)*(b+7),
    1: -42*(a+3)*(a+4)*(a+5)*(a+6)*(a+7)*(b+2)*(b+3)*(b+4)*(b+5)*(b+6),
    2: -14*(a+3)*(a+4)*(a+5)*(a+6)*(b+2)*(b+3)*(b+4)*(b+5)*(a*b + a + 2*b - 88),
    3: 1260*(a+3)*(a+4)*(a+5)*(b+2)*(b+3)*(b+4)*(a*b + a + 2*b - 18),
    4: 504*(a+3)*(a+4)*(b+2)*(b+3)*(a**2*b**2 + a**2*b + 3*a*b**2 - 97*a*b - 100*a + 2*b**2 - 198*b + 400),
    5: -50400*(a+3)*(b+2)*(a**2*b**2 + a**2*b + 3*a*b**2 - 17*a*b - 20*a + 2*b**2 - 38*b - 4),
    6: -25200*(a**3*b**3 - a**3*b + 3*a**2*b**3 - 72*a**2*b**2 - 75*a**2*b + 2*a*b**3 - 216*a*b**2 + 142*a*b + 360*a - 144*b**2 + 576*b + 576),
    7: 2116800*(a**2*b**2 - a**2*b + a*b**2 - 13*a*b - 12*b + 12),
    8: 1411200*(a**2*b**2 - 3*a**2*b + 2*a**2 - a*b**2 - 33*a*b + 34*a + 72),
    9: -76204800*(a*b - 2*a - b - 2),
    10: -76204800*(a*b - 3*a - 2*b - 4),
    11: 1676505600,
    12: 3353011200,
}


def v2(n):
    if n == 0: return float('inf')
    n = abs(int(n))
    r = 0
    while n % 2 == 0:
        n //= 2; r += 1
    return r


def Cn(n, k):
    if k < 0 or k > n: return 0
    return factorial(n) // (factorial(k) * factorial(n - k))


def evaluate_H_from_hk(hk_dict, kmax, av, bv, jv):
    total = 0
    for k in range(kmax + 1):
        hk = hk_dict.get(k, 0)
        val = int(hk.subs({a: av, b: bv})) if hasattr(hk, 'subs') else int(hk)
        cjk = Cn(jv, k)
        total += val * cjk
    return total


def brute_force_min_v2(hk_dict, kmax, c_val, arange=40, brange=40, jrange=None):
    """Find min v_2(H(a,b,j)) with (a+b+c) even for parity shell."""
    best = float('inf')
    witness = None
    if jrange is None:
        jrange = kmax + 1
    for av in range(0, arange):
        for bv in range(0, brange):
            if (av + bv + c_val) % 2 != 0:
                continue
            for jv in range(0, jrange):
                val = evaluate_H_from_hk(hk_dict, kmax, av, bv, jv)
                if val == 0:
                    continue
                v = v2(val)
                if v < best:
                    best = v
                    witness = (av, bv, jv, val)
    return best, witness


def constant_and_consec_LB(hk_dict, c_val, max_kmax=None):
    """For each h_k, split as: constant × consecutive-a-runs × consecutive-b-runs × residual.
    Report v_2(constant), consec credits, and any residual factor with unknown v_2 floor."""
    if max_kmax is None:
        max_kmax = max(hk_dict.keys())
    print(f"\n### c = {c_val}: h_k structural analysis ###")
    for k in range(max_kmax + 1):
        h = hk_dict[k]
        try:
            fh = factor(h)
        except Exception:
            fh = h
        # try to peel off the leading constant
        if hasattr(h, 'as_coeff_Mul'):
            const, rest = h.as_coeff_Mul()
        else:
            const, rest = h, sympify(1)
        v2c = v2(int(const)) if const != 0 else 'inf'
        print(f"  k={k}: const={const}  v2(const)={v2c}  h_k = {fh}")


def analyze_witness(hk_dict, kmax, av, bv, jv):
    """Print per-term v_2 at a specific witness to see cancellation pattern."""
    print(f"\n  Witness (a,b,j) = ({av},{bv},{jv}):")
    total = 0
    for k in range(kmax + 1):
        hk = hk_dict.get(k, 0)
        val = int(hk.subs({a: av, b: bv})) if hasattr(hk, 'subs') else int(hk)
        cjk = Cn(jv, k)
        contrib = val * cjk
        vv = v2(contrib) if contrib != 0 else '-'
        print(f"    k={k}: h_k(a,b)={val:20d}  C(j,k)={cjk:8d}  h_k*C = {contrib:20d}  v2={vv}")
        total += contrib
    print(f"    SUM = {total} = 2^{v2(total)} · odd")


if __name__ == "__main__":
    print("=" * 70)
    print("c = 6")
    print("=" * 70)
    constant_and_consec_LB(h_c6, 6)
    print("\n  Brute-force min v_2(H_6) over (a,b,j) in [0,30]^3, kmax=10, parity shell (a+b) even:")
    m6, w6 = brute_force_min_v2(h_c6, 10, 6, arange=30, brange=30, jrange=15)
    print(f"  Best: v_2 = {m6}, witness = {w6}")
    if w6:
        analyze_witness(h_c6, 10, w6[0], w6[1], w6[2])

    print("\n" + "=" * 70)
    print("c = 7")
    print("=" * 70)
    constant_and_consec_LB(h_c7, 7)
    print("\n  Brute-force min v_2(H_7) over (a,b,j) in [0,30]^3, kmax=12, parity shell (a+b) odd:")
    m7, w7 = brute_force_min_v2(h_c7, 12, 7, arange=30, brange=30, jrange=16)
    print(f"  Best: v_2 = {m7}, witness = {w7}")
    if w7:
        analyze_witness(h_c7, 12, w7[0], w7[1], w7[2])

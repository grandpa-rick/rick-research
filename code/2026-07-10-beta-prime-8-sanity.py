"""Day 88 Task 3 sanity — beta'(8) = 11 witness sweep using the newly
derived closed-form h_k^{(8)}(a, b) polynomials (k = 0..5).

We compute H_8(a, b, j) = sum_{k=0}^{jmax} C(j, k) h_k^{(8)}(a, b) using
the closed forms, sample v_2(H_8) across the parity shell a+b even, and
report:

  (a) the minimum v_2 observed (if <= 11, that is the lower-bound witness),
  (b) an explicit (a, b, j) achieving that minimum.

Since we only have h_0..h_5 explicitly, we truncate: H_8_truncated(a, b, j)
= sum_{k=0}^{5} C(j, k) h_k(a, b, 8).  For j <= 5 this is exact; for
larger j the higher h_k terms (k >= 6) contribute additional summands
(bounded by their v_2 valuation).  We use this to bracket beta'(8).
"""
from math import factorial


def v2(n):
    if n == 0:
        return float('inf')
    n = abs(int(n))
    r = 0
    while n % 2 == 0:
        n //= 2
        r += 1
    return r


def C(n, k):
    if k < 0 or k > n:
        return 0
    return factorial(n) // (factorial(k) * factorial(n - k))


def rising_fact(x, n):
    if n <= 0:
        return 1
    p = 1
    for i in range(n):
        p *= (x + i)
    return p


def h_k_c8(k, a, b):
    """Closed-form h_k^{(8)}(a, b) for k = 0..5.

    From Task-2 fit (2026-07-10-hk-three-var-fit.py):
        h_k^{(c)}(a, b) = (a+3)_{c-1-k} (b+2)_{c-1-k} * P_k(a, b, c)
    with c = 8 substituted.
    """
    c = 8
    n = c - 1 - k  # Pochhammer length
    p_a = rising_fact(a + 3, n)
    p_b = rising_fact(b + 2, n)
    if k == 0:
        P = 1
    elif k == 1:
        P = -c * (c - 1)
    elif k == 2:
        P = -c * (2 * a * b + 2 * a + 4 * b - c ** 3 + 4 * c ** 2 - 5 * c + 6)
    elif k == 3:
        P = c * (c - 1) * (c - 2) * (
            6 * a * b + 6 * a + 12 * b - c ** 3 + 6 * c ** 2 - 11 * c + 18
        )
    elif k == 4:
        # Q_4
        Q = (12 * a**2 * b**2 + 12 * a**2 * b + 36 * a * b**2
             - 12 * a * b * c**3 + 84 * a * b * c**2 - 192 * a * b * c
             + 180 * a * b - 12 * a * c**3 + 84 * a * c**2 - 192 * a * c
             + 144 * a + 24 * b**2 - 24 * b * c**3 + 168 * b * c**2
             - 384 * b * c + 312 * b + c**6 - 15 * c**5 + 91 * c**4
             - 309 * c**3 + 652 * c**2 - 804 * c + 432)
        P = c * (c - 1) * Q
    elif k == 5:
        Q = (60 * a**2 * b**2 + 60 * a**2 * b + 180 * a * b**2
             - 20 * a * b * c**3 + 180 * a * b * c**2 - 520 * a * b * c
             + 660 * a * b - 20 * a * c**3 + 180 * a * c**2 - 520 * a * c
             + 480 * a + 120 * b**2 - 40 * b * c**3 + 360 * b * c**2
             - 1040 * b * c + 1080 * b + c**6 - 19 * c**5 + 145 * c**4
             - 605 * c**3 + 1534 * c**2 - 2256 * c + 1440)
        P = -c * (c - 1) * (c - 2) * (c - 3) * Q
    else:
        raise ValueError(f"k = {k} not implemented")
    return p_a * p_b * P


def H_8_truncated(a, b, j, kmax=5):
    total = 0
    for k in range(min(j, kmax) + 1):
        total += C(j, k) * h_k_c8(k, a, b)
    return total


def sanity_vs_template(a_range, b_range, j_max=5):
    """Verify our closed-form h_k^{(8)} against the H_c_template pipeline
    at small j (where truncated H_8 = full H_8)."""
    print("=" * 78)
    print("Sanity: closed-form h_k^{(8)} vs H_c_template pipeline")
    print("=" * 78)
    # Import template computation.
    from importlib import util
    spec = util.spec_from_file_location(
        "hkmod", "/home/agent/projects/code/2026-07-10-hk-three-var-fit.py"
    )
    mod = util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    tables = mod.build_e2_tables(max_j=j_max + 2)
    ok, fail = 0, 0
    for a in a_range:
        for b in b_range:
            if b > a or b < 8:
                continue
            for j in range(j_max + 1):
                H_actual = mod.H_c_template(a, b, 8, j, tables)
                if H_actual is None:
                    continue
                H_closed = H_8_truncated(a, b, j, kmax=5)
                if j <= 5:
                    if H_actual == H_closed:
                        ok += 1
                    else:
                        fail += 1
                        if fail <= 3:
                            print(f"  FAIL: (a,b,j)=({a},{b},{j}) "
                                  f"template={H_actual}  closed={H_closed}")
    print(f"  Sanity vs template at j <= 5:  {ok} match, {fail} fail")
    return ok, fail


def v2_sweep(a_range, b_range, j_range, kmax=5):
    """Sweep v_2(H_8(a, b, j)) via the closed form (truncated at kmax=5).

    For j <= kmax this is exact.  For j > kmax the truncation misses
    h_k with k > kmax, and the true value has additional terms.
    """
    print("\n" + "=" * 78)
    print(f"v_2(H_8(a, b, j)) sweep  (closed form, truncated at k <= {kmax})")
    print(f"  a in {a_range}, b in {b_range}, j in {j_range}, a+b even")
    print("=" * 78)
    min_v2 = float('inf')
    witness = None
    counts = {}
    for a in a_range:
        for b in b_range:
            if b > a:
                continue
            if (a + b) % 2 != 0:
                continue
            for j in j_range:
                if j > kmax:
                    continue  # truncation error zone
                if j > b:
                    continue
                H = H_8_truncated(a, b, j, kmax=kmax)
                vv = v2(H)
                counts[vv] = counts.get(vv, 0) + 1
                if vv < min_v2:
                    min_v2 = vv
                    witness = (a, b, j, H)
    print(f"\n  min v_2 = {min_v2}")
    if witness:
        a, b, j, H = witness
        print(f"  witness: (a, b, j) = ({a}, {b}, {j}),  H_8 = {H},  v_2(H_8) = {v2(H)}")
    print(f"  v_2 distribution (exact j <= {kmax}):")
    for vv in sorted(counts):
        print(f"    v_2 = {vv:>3d}:  {counts[vv]:>6d} cases")


def main():
    # (1) Sanity check: closed forms match template pipeline at j <= 5.
    sanity_vs_template(a_range=range(8, 25), b_range=range(8, 25), j_max=5)

    # (2) v_2 sweep at j <= 5 (exact) — see the v_2 distribution.
    v2_sweep(
        a_range=range(8, 40),
        b_range=range(8, 40),
        j_range=range(6),
        kmax=5,
    )

    # (3) Larger v_2 sweep at wider (a, b) to search for low v_2.
    v2_sweep(
        a_range=range(8, 80),
        b_range=range(8, 80),
        j_range=range(6),
        kmax=5,
    )


if __name__ == "__main__":
    main()

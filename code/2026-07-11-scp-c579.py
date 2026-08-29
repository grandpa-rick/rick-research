"""Day 89 Attack C — Sharp Cancellation Principle re-verification at c=5,7,9.

We independently re-derive:

  (i) h_k^{(c)}(a, b) as bivariate integer polys via extract_h_k pipeline.
 (ii) For each k, min_{(a,b) in shell, small range} v_2(h_k^{(c)}(a,b)) — the
      empirical LB floor per k.
(iii) The carrier index k* = argmin_k [floor + v_2(C(k*, k))] for each c —
      i.e., the k that dominates the sum at witness (a*, b*, j*=k*).
 (iv) A witness (a*, b*, k*) with:
        - v_2(h_{k*}^{(c)}(a*, b*)) = beta'(c) exactly
        - v_2(h_k^{(c)}(a*, b*) * C(k*, k)) > beta'(c) for all k < k*
        - Hence H_c(a*, b*, k*) has v_2 = beta'(c) by min-dominates.

Consistency check: the beta'(c) so derived matches the registry value
{beta'(5)=3, beta'(7)=6, beta'(9)=9}.

Result is written to code/2026-07-11-scp-c579-output.txt.
"""
import sys
import time
from importlib import util
from math import factorial

from sympy import symbols, Matrix, Rational, expand, factor, lambdify

# Load the extraction pipeline.
spec = util.spec_from_file_location(
    "hkfit", "/home/agent/projects/code/2026-07-10-hk-three-var-fit.py"
)
mod = util.module_from_spec(spec)
spec.loader.exec_module(mod)

extract_h_k = mod.extract_h_k
build_e2_tables = mod.build_e2_tables
H_c_template = mod.H_c_template


def Cn(n, k):
    if k < 0 or k > n:
        return 0
    return factorial(n) // (factorial(k) * factorial(n - k))


def v2(n):
    if n == 0:
        return float('inf')
    v = 0
    while n % 2 == 0:
        n //= 2
        v += 1
    return v


def fit_bivariate_poly(samples, deg_bound=20):
    """Fit y = h_k(a, b) as poly of total degree <= D. Return (poly, D)."""
    a_s, b_s = symbols('a b')
    for D in range(deg_bound + 1):
        monomials = [(da, db) for da in range(D + 1) for db in range(D + 1 - da)]
        N = len(monomials)
        if len(samples) < N + 3:
            continue
        rows = []
        yvals = []
        for (av, bv, yv) in samples:
            rows.append([av ** da * bv ** db for (da, db) in monomials])
            yvals.append(yv)
        M = Matrix(rows)
        y = Matrix(yvals)
        aug = M.row_join(y)
        rref, pivots = aug.rref()
        if (aug.cols - 1) in pivots:
            continue
        if len(pivots) != N:
            continue
        sol = [rref[pivots.index(i), aug.cols - 1] for i in range(N)]
        ok = True
        for c in sol:
            if not isinstance(c, Rational) or c.q != 1:
                ok = False
                break
        if not ok:
            continue
        poly = 0
        for (da, db), c in zip(monomials, sol):
            poly += int(c) * a_s ** da * b_s ** db
        poly = expand(poly)
        # Verify on samples
        bad = False
        for (av, bv, yv) in samples:
            got = poly.subs({a_s: av, b_s: bv})
            if got != yv:
                bad = True
                break
        if bad:
            continue
        return poly, D
    return None, None


def parity_shell(c):
    """Return required parity of a+b for the shell at c.

    At c=5: (a+b+c) even -> a+b odd. c=7: a+b odd. c=9: a+b odd.
    Actually registry says: c=5 shell = a+b even parity (a+b+c even, c odd
    -> a+b odd). Wait let's double check via a+b+c even.

    c=5: a+b+c even <=> a+b odd. c=7: a+b odd. c=9: a+b odd.
    Actually looking at the c=5 witness (3,0,2): a+b=3 odd. Confirmed odd.
    """
    return 'odd'


def satisfies_shell(a, b, c):
    if parity_shell(c) == 'odd':
        return (a + b) % 2 == 1
    return (a + b) % 2 == 0


def extract_hk_polys(c_val, jmax, arange, brange=None):
    """Extract h_k^{(c)}(a, b) as sympy polys via template inversion.
    Returns dict {k: sympy poly in a, b}.
    """
    print(f"\n[extract] h_k^{{(c={c_val})}}(a,b) for k=0..{jmax}, "
          f"a in [{arange[0]},{arange[1]}), b in [b0, a+1]")
    tables = build_e2_tables(max_j=jmax + 2)
    per_k = {k: [] for k in range(jmax + 1)}
    if brange is None:
        brange = (arange[0], None)
    t0 = time.time()
    n_ok = 0
    for a in range(arange[0], arange[1]):
        bmin, bmax = brange
        bhi = a + 1 if bmax is None else min(a + 1, bmax)
        for b in range(bmin, bhi):
            hks = extract_h_k(a, b, c_val, jmax, tables)
            if hks is None:
                continue
            for k, y in enumerate(hks):
                per_k[k].append((a, b, y))
            n_ok += 1
    dt = time.time() - t0
    print(f"          {n_ok} samples in {dt:.1f}s")

    result = {}
    a_s, b_s = symbols('a b')
    for k in range(jmax + 1):
        samples = per_k[k]
        if len(samples) < 30:
            print(f"  k={k}: skip (only {len(samples)} samples)")
            continue
        poly, D = fit_bivariate_poly(samples, deg_bound=20)
        if poly is None:
            print(f"  k={k}: no polynomial fit (deg bound 18)")
        else:
            result[k] = poly
            # Compact display: factored form
            try:
                fp = factor(poly)
            except Exception:
                fp = poly
            head = str(fp)
            if len(head) > 100:
                head = head[:100] + "..."
            print(f"  k={k}: deg <= {D:>2d}   h_{k} = {head}")
    return result


def find_carrier(hk_polys, c_val, search_size=64):
    """For each k, compute the min v_2(h_k(a,b)) over parity-shell (a,b) in
    [0, search_size)^2. Then find the carrier k* minimizing this floor.

    Returns dict per_k -> (min_v2, list_of_achievers) and the identified k*.

    Uses lambdify for fast evaluation.
    """
    a_s, b_s = symbols('a b')
    per_k_min = {}
    for k, poly in hk_polys.items():
        f = lambdify((a_s, b_s), poly, "math")
        min_v = float('inf')
        achievers = []
        for a in range(search_size):
            for b in range(search_size):
                if (a + b) % 2 == 0:  # c=5,7,9 shell: a+b odd
                    continue
                val = int(f(a, b))
                v = v2(val)
                if v < min_v:
                    min_v = v
                    achievers = [(a, b)]
                elif v == min_v:
                    if len(achievers) < 5:
                        achievers.append((a, b))
        per_k_min[k] = (min_v, achievers)

    # Now: find carrier k* — the k such that when we take j*=k*, the sum
    # H_c(a*, b*, k*) = sum_{k <= k*} h_k C(k*, k) is min-dominated by k=k*.
    # Simplification: the "SCP-optimum" is the k minimizing per_k_min[k].
    # (Higher k with same min but larger C(k*, k) contributes >= it, but
    # if the min-carrier k* has a unique smallest v_2 among summands, sum
    # v_2 = per_k_min[k*].)
    best_k = None
    best_v = float('inf')
    for k, (m, _) in per_k_min.items():
        if m < best_v:
            best_v = m
            best_k = k

    return per_k_min, best_k, best_v


def verify_witness(hk_polys, a_star, b_star, k_star, c_val):
    """Verify the SCP witness: at (a*, b*, j*=k*), each summand
    h_k(a*, b*) * C(k*, k) for k in 0..k* has v_2 tabulated, and the
    single carrier k=k* has strictly smallest v_2.

    Returns (H_c_value, v2_of_H_c, per_k_summands, ok_distinct_min).
    """
    a_s, b_s = symbols('a b')
    summands = []
    for k in range(k_star + 1):
        if k not in hk_polys:
            summands.append(None)
            continue
        val = int(hk_polys[k].subs({a_s: a_star, b_s: b_star}))
        weight = Cn(k_star, k)
        contrib = weight * val
        summands.append((k, val, weight, contrib, v2(contrib)))
    total = sum(s[3] for s in summands if s is not None)
    v_total = v2(total) if total != 0 else float('inf')

    # Distinct-min check: does k=k_star have strictly smallest v_2?
    carrier_v = summands[k_star][4]
    others = [s[4] for i, s in enumerate(summands)
              if s is not None and i != k_star]
    ok = all(v > carrier_v for v in others) if others else True

    return total, v_total, summands, ok, carrier_v


def report_case(c_val, jmax, arange, brange=None, beta_prime_target=None):
    print("=" * 74)
    print(f"CASE: c = {c_val}, beta'({c_val}) target = {beta_prime_target}")
    print("=" * 74)

    hk_polys = extract_hk_polys(c_val, jmax, arange, brange=brange)
    if not hk_polys:
        print("  NO POLYS EXTRACTED — abort")
        return None

    print("\n[floor] per-k v_2 floor via search over a+b odd shell, "
          "[0, 64)^2:")
    per_k_min, k_star, best_v = find_carrier(hk_polys, c_val, search_size=64)
    for k in sorted(per_k_min.keys()):
        m, ach = per_k_min[k]
        star = " <-- CARRIER" if k == k_star else ""
        print(f"  k={k:>2d}: min v_2 = {m}   (achieved at {ach[:3]}){star}")
    print(f"\n[carrier] identified k* = {k_star}, floor = {best_v}")

    # Witness: pick the first achiever of (k*, min_v_2) that is small.
    achievers = per_k_min[k_star][1]
    # Try each achiever; look for one where distinct-min sum rule works.
    print(f"\n[witness search] trying achievers for k={k_star}:")
    best_witness = None
    for (a_star, b_star) in achievers:
        total, v_tot, summands, ok, carrier_v = verify_witness(
            hk_polys, a_star, b_star, k_star, c_val)
        note = " OK distinct-min" if ok else " NOT distinct-min"
        print(f"  (a*,b*)=({a_star},{b_star}): H_{c_val} = {total}, "
              f"v_2 = {v_tot}, carrier v_2 = {carrier_v}{note}")
        if ok and best_witness is None:
            best_witness = (a_star, b_star, total, v_tot, summands, carrier_v)

    if best_witness is None:
        # Fallback: try tiny grid explicitly.
        print("  No distinct-min achievers found in top candidates — "
              "search wider grid.")
        a_s, b_s = symbols('a b')
        for a in range(20):
            for b in range(20):
                if (a + b) % 2 != 1:
                    continue
                total, v_tot, summands, ok, carrier_v = verify_witness(
                    hk_polys, a, b, k_star, c_val)
                if ok and v_tot == best_v:
                    print(f"  wider grid: (a*,b*)=({a},{b}), H = {total}, "
                          f"v_2 = {v_tot} OK")
                    best_witness = (a, b, total, v_tot, summands, carrier_v)
                    break
            if best_witness is not None:
                break

    if best_witness is None:
        print("  WITNESS SEARCH FAILED")
        return None

    a_star, b_star, total, v_tot, summands, carrier_v = best_witness
    print(f"\n[SCP witness at c={c_val}]: (a*, b*, k*=j*) "
          f"= ({a_star}, {b_star}, {k_star})")
    print(f"  H_{c_val}({a_star},{b_star},{k_star}) = {total}")
    print(f"  v_2 = {v_tot}   (target beta'(c) = {beta_prime_target})")
    print("  Per-summand v_2 breakdown:")
    for s in summands:
        if s is None:
            continue
        k, val, weight, contrib, v = s
        note = "  <-- CARRIER" if k == k_star else ""
        print(f"    k={k:>2d}: h_k = {val:>18d}  C({k_star},{k})={weight:<5d}  "
              f"contrib = {contrib:>20d}  v_2 = {v}{note}")

    ok_match = (v_tot == beta_prime_target)
    print(f"\n[registry consistency] v_2 = {v_tot} vs target "
          f"beta'({c_val}) = {beta_prime_target}: "
          f"{'MATCH' if ok_match else 'MISMATCH'}")

    return {
        'c': c_val,
        'k_star': k_star,
        'a_star': a_star,
        'b_star': b_star,
        'H': total,
        'v_2': v_tot,
        'beta_prime': beta_prime_target,
        'match': ok_match,
        'summands': summands,
    }


def main():
    out_lines = []
    print("=" * 74)
    print("Day 89 Attack C — Sharp Cancellation Principle re-verify c=5,7,9")
    print("=" * 74)

    results = []

    # H_c_template needs a >= b >= c (else denominators vanish / non-integer).
    # Sample at a, b >= c for polynomial fitting; then evaluate the fitted
    # polynomials at small (a, b) including the known witnesses.
    #
    # Known witnesses (registry): (3,0,2) at c=5; (1,2,6) at c=7; (7,0,2) at c=9.

    # c=5: h_k for k=0..8. Poly degree bound in (a,b): looking at h_0^{(5)},
    # top monomial has degree (a+3)(a+4)(a+5)(a+6) x (b+2)(b+3)(b+4)(b+5) i.e.
    # degree 4+4=8. Need >= 45 samples for total-deg-8 fit (36 monomials).
    r5 = report_case(c_val=5, jmax=8, arange=(5, 18),
                     brange=(5, None), beta_prime_target=3)
    if r5:
        results.append(r5)

    # c=7: h_0 has degree 12 in (a,b) — need >~90 samples for total-deg-12 fit.
    r7 = report_case(c_val=7, jmax=12, arange=(7, 30),
                     brange=(7, None), beta_prime_target=6)
    if r7:
        results.append(r7)

    # c=9: h_0 has degree 16 in (a,b) — need >~153 samples for total-deg-16
    # fit. arange width w gives w(w+1)/2 samples with b>=c, so w ~ 25.
    r9 = report_case(c_val=9, jmax=16, arange=(9, 34),
                     brange=(9, None), beta_prime_target=9)
    if r9:
        results.append(r9)

    # Summary
    print("\n" + "=" * 74)
    print("SUMMARY")
    print("=" * 74)
    for r in results:
        c = r['c']
        print(f"  c={c}: witness (a*,b*,k*)=({r['a_star']},{r['b_star']},"
              f"{r['k_star']}), H_c = {r['H']}, v_2 = {r['v_2']} "
              f"(target {r['beta_prime']}), {'MATCH' if r['match'] else 'MISMATCH'}")

    all_ok = all(r['match'] for r in results) if results else False
    print(f"\n  Overall: {'ALL MATCH' if all_ok else 'MISMATCH SOMEWHERE'}")
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())

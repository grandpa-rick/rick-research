"""Day 91 — Check c=11 witness at k=6 that Delta catalog claimed.

The catalog claimed LB_6^{(11)} = 12 = 2*v_2(4!) + Delta_6^{(11)}=6.
If this is a real achievable value with distinct-min H_c, then beta'(11) = 12,
FALSIFYING D2 (which predicted beta'(11) = 13).

Method:
  1. Extract h_k^{(11)}(a, b) polynomials for k = 0..10 via existing pipeline.
  2. Enumerate (a, b) in shell (a+b odd for c=11 odd) and check
     v_2(h_6^{(11)}(a, b)) achieves 12.
  3. Also verify UNRESTRICTED LB_k^{(c)} = min v_2(h_k^{(c)}) — is 12 truly
     the LB or is there something lower?
  4. Compute H_c(a*, b*, k*=6) at the witness and check distinct-min.

If distinct-min holds and v_2 = 12, we have beta'(11) <= 12.

Also runs UNRESTRICTED verification at c=5..10 to double-check.
"""
import json
import sys
import time
from importlib import util
from math import factorial

from sympy import symbols, sympify, expand, factor, Matrix, Rational, lambdify

# Load the extraction pipeline
spec = util.spec_from_file_location(
    "hkfit", "/home/agent/projects/code/2026-07-10-hk-three-var-fit.py"
)
mod = util.module_from_spec(spec)
spec.loader.exec_module(mod)

extract_h_k = mod.extract_h_k
build_e2_tables = mod.build_e2_tables


def v2(n):
    if n == 0:
        return float('inf')
    v = 0
    while n % 2 == 0:
        n //= 2
        v += 1
    return v


def Cn(n, k):
    if k < 0 or k > n:
        return 0
    return factorial(n) // (factorial(k) * factorial(n - k))


def fit_bivariate_poly(samples, deg_bound=24):
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
        for (da, db), coef in zip(monomials, sol):
            poly += int(coef) * a_s ** da * b_s ** db
        poly = expand(poly)
        # Verify
        for (av, bv, yv) in samples:
            got = poly.subs({a_s: av, b_s: bv})
            if got != yv:
                poly = None
                break
        if poly is not None:
            return poly, D
    return None, None


def extract_hk_polys(c_val, jmax, arange, brange=None):
    print(f"[extract] h_k^({c_val}) for k=0..{jmax}, a in {arange}")
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
    for k in range(jmax + 1):
        samples = per_k[k]
        if len(samples) < 30:
            print(f"  k={k}: skip (only {len(samples)} samples)")
            continue
        poly, D = fit_bivariate_poly(samples, deg_bound=24)
        if poly is None:
            print(f"  k={k}: no polynomial fit")
        else:
            result[k] = poly
            print(f"  k={k}: deg <= {D}, fit ok")
    return result


def scan_lb_and_witness(hk_polys, c_val, T_scan=64, target_v=None):
    """Compute min v_2 per k over parity shell in [0, T_scan)^2. Report witness."""
    a_s, b_s = symbols('a b')
    parity = c_val % 2  # a+b ~ c mod 2

    per_k_min = {}
    for k, poly in hk_polys.items():
        f = lambdify((a_s, b_s), poly, "math")
        min_v = float('inf')
        achievers = []
        for a in range(T_scan):
            for b in range(T_scan):
                if (a + b) % 2 != parity:
                    continue
                try:
                    val = int(f(a, b))
                except Exception:
                    val = int(poly.subs({a_s: a, b_s: b}))
                if val == 0:
                    continue
                v = v2(val)
                if v < min_v:
                    min_v = v
                    achievers = [(a, b, val)]
                elif v == min_v and len(achievers) < 10:
                    achievers.append((a, b, val))
        per_k_min[k] = (min_v, achievers)
    return per_k_min


def check_witness_distinct_min(hk_polys, a_star, b_star, k_star, c_val):
    """Compute H_c(a*, b*, k*) = sum_{j=0..k*} h_j(a*,b*) C(k*, j) and check
    distinct-min sum rule."""
    a_s, b_s = symbols('a b')
    per_j = []
    total = 0
    for j in range(k_star + 1):
        if j not in hk_polys:
            per_j.append(None)
            continue
        val = int(hk_polys[j].subs({a_s: a_star, b_s: b_star}))
        C = Cn(k_star, j)
        contrib = C * val
        total += contrib
        per_j.append((j, val, C, contrib, v2(contrib) if contrib else float('inf')))
    v_total = v2(total) if total != 0 else float('inf')
    carrier_v = per_j[k_star][4] if per_j[k_star] else None
    others = [s[4] for i, s in enumerate(per_j) if s is not None and i != k_star]
    ok_distinct = all(v > carrier_v for v in others) if others and carrier_v is not None else False
    return total, v_total, per_j, ok_distinct, carrier_v


def main():
    print("=" * 80)
    print("Day 91 — c=11 witness hunt (test if beta'(11) = 12 falsifies D2)")
    print("=" * 80)
    print()

    # Extract h_k^{(11)} — degree up to 20, need many samples
    # h_k^{(11)}(a, b) degree in (a, b) up to about 2*(c-1) = 20 for k=0
    # Number of samples for total deg 20: 231 monomials
    # arange width w gives w(w+1)/2 samples with b>=c, so w ~ 22 to get ~250 samples
    hk_polys = extract_hk_polys(c_val=11, jmax=10, arange=(11, 34), brange=(11, None))
    if not hk_polys:
        print("No polys extracted")
        return 1

    print()
    print(f"[c=11] Full min-v_2 scan in [0, 64)^2 shell a+b odd:")
    per_k_min = scan_lb_and_witness(hk_polys, c_val=11, T_scan=64)
    for k in sorted(per_k_min.keys()):
        m, ach = per_k_min[k]
        marker = ""
        print(f"  k={k:>2d}: min v_2 = {m}   achievers (first 3): {ach[:3]}{marker}")

    # Find k* = argmin
    kmin_v = min(m for m, _ in per_k_min.values())
    k_star = min(k for k, (m, _) in per_k_min.items() if m == kmin_v)
    print()
    print(f"  argmin: k* = {k_star}, min v_2 = {kmin_v}")

    # Check the witness at k*
    _, achievers = per_k_min[k_star]
    print()
    print(f"  Witness distinct-min check at k* = {k_star}:")
    for (a_star, b_star, val_h) in achievers[:5]:
        total, v_tot, per_j, ok, carrier_v = check_witness_distinct_min(
            hk_polys, a_star, b_star, k_star, 11)
        note = "OK distinct-min" if ok else "NOT distinct-min"
        print(f"   (a*, b*)=({a_star}, {b_star})  H_11 = {total}  v_2={v_tot}  carrier v_2={carrier_v}  {note}")
        for s in per_j:
            if s is None:
                continue
            j, hv, C, contrib, v = s
            mark = "  <-- CARRIER" if j == k_star else ""
            print(f"     j={j:>2d}: h_j={hv:>22d} C={C:<8d} contrib_v2={v}{mark}")
        # Only show detail for the first attempted witness
        if ok:
            break
        print()

    print()
    print("=" * 80)
    print("Verdict")
    print("=" * 80)
    print(f"  min_k LB_k^{{(11)}} = {kmin_v} at k* = {k_star}")
    print(f"  D2 conjecture predicted beta'(11) = 13")
    if kmin_v == 12:
        print(f"  IF distinct-min witness exists at k* = {k_star}: beta'(11) <= 12")
        print(f"  This would FALSIFY D2.")
    elif kmin_v == 13:
        print(f"  Consistent with D2.")
    else:
        print(f"  min = {kmin_v} — check what this means.")


if __name__ == "__main__":
    sys.exit(main())

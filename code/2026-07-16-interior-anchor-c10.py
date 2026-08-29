"""Day 98 — Locate the SCP achiever for β'(10).

Context:
    Registry: β'(10) = 14 (checked-sober).
    c = 10, c ≡ 2 mod 8, so v_2((c-2)/4) = v_2(2) = 1.
    Four canonical corners (T-2, 0), (0, T-2), (T-2, T-2), (0, 0) with
    T = 16 OVERSHOOT the true SCP by 1 at c=10.  So the SCP achiever is
    INTERIOR — some (a*, b*) NOT at those corners saturates v_2 = 14.

Approach:
    1. Fit h_k^{(10)}(a, b) as a bivariate polynomial for k = 0..9
       via the M-side pipeline (samples in wedge a >= b >= c=10).
    2. Evaluate H_10(a, b, j) = sum_{k<=j} C(j,k) h_k^{(10)}(a, b)
       on the FULL shell a, b ∈ [0, 2T], (a+b) ≡ 0 mod 2 via the
       polynomial extension (works for all (a, b), not just wedge).
    3. Also compute v_2(h_k^{(10)}(a*, b*)) for k = 0..9 and identify
       the unique argmin k*.  Compare v_2(h_{k*}) vs LB_{k*}^{(10)}.

j-range: SCP LB values at c=10 attain min 14 at k ∈ {4,5,6,7} (Delta
catalog), so j must be >= 7 for the polynomial-sum H_10(a, b, j) to
see that carrier.  We use j ∈ {0..9} to be safe.
"""

import json
import time
from importlib import util
from math import comb, factorial

import sympy as sp

# Load hkfit pipeline.
spec = util.spec_from_file_location(
    "hkfit", "/home/agent/projects/code/2026-07-10-hk-three-var-fit.py"
)
hkfit = util.module_from_spec(spec)
spec.loader.exec_module(hkfit)

build_e2_tables = hkfit.build_e2_tables
H_c_template = hkfit.H_c_template
extract_h_k = hkfit.extract_h_k


def v2(n):
    if n == 0:
        return None
    n = abs(int(n))
    v = 0
    while (n & 1) == 0:
        n >>= 1
        v += 1
    return v


def rising_fact(x, n):
    if n <= 0:
        return 1
    p = 1
    for i in range(n):
        p *= (x + i)
    return p


C_VAL = 10
T_VAL = 16
J_MAX = 9         # need k up to c-1 = 9 for full LB coverage
K_MAX = 9         # fit h_k for k = 0..9
SAMPLE_ARANGE = (10, 30)  # need a >= b >= c=10 for M-side extraction

LB_C10 = {
    0: 15, 1: 15, 2: 15, 3: 15, 4: 14, 5: 14, 6: 14, 7: 14,
    8: 15, 9: 15,
}


# --------------------------------------------------------------------------
# STEP A: Extract h_k^{(10)}(a, b) samples, fit as bivariate polynomial.
# --------------------------------------------------------------------------

def collect_hk_samples(c_val, jmax, arange):
    """Return dict {k: [(a, b, y)]} for a >= b >= c_val."""
    tables = build_e2_tables(max_j=jmax + 2)
    per_k = {k: [] for k in range(jmax + 1)}
    for a in range(arange[0], arange[1]):
        for b in range(arange[0], a + 1):
            hks = extract_h_k(a, b, c_val, jmax, tables)
            if hks is None:
                continue
            for k, y in enumerate(hks):
                per_k[k].append((a, b, y))
    return per_k


def fit_bivariate_poly(samples, deg_bound=20):
    """Return sympy poly in (a, b) fitting all samples, or None."""
    a_s, b_s = sp.symbols('a b')
    for D in range(deg_bound + 1):
        monos = [(da, db) for da in range(D + 1) for db in range(D + 1 - da)]
        N = len(monos)
        if len(samples) < N + 5:
            continue
        rows, ys = [], []
        for (av, bv, yv) in samples:
            rows.append([av ** da * bv ** db for (da, db) in monos])
            ys.append(yv)
        M = sp.Matrix(rows)
        y = sp.Matrix(ys)
        aug = M.row_join(y)
        rref, pivots = aug.rref()
        if (aug.cols - 1) in pivots:
            continue
        if len(pivots) != N:
            continue
        sol = [rref[pivots.index(i), aug.cols - 1] for i in range(N)]
        # integer check
        ok_int = True
        for c in sol:
            if not isinstance(c, sp.Rational) or c.q != 1:
                ok_int = False
                break
        if not ok_int:
            continue
        poly = 0
        for (da, db), c in zip(monos, sol):
            poly += int(c) * a_s ** da * b_s ** db
        poly = sp.expand(poly)
        # verify
        verified = True
        for (av, bv, yv) in samples:
            if poly.subs({a_s: av, b_s: bv}) != yv:
                verified = False
                break
        if not verified:
            continue
        return poly, D
    return None, None


def main():
    print("=" * 78)
    print("Day 98 — SCP achiever hunt for β'(10)")
    print("=" * 78)
    print(f"  c = {C_VAL}, T = {T_VAL}, target min v_2 = 14")
    print(f"  Shell parity: (a + b) ≡ 0 mod 2, a, b ∈ [0, {2 * T_VAL}]")
    print(f"  Fitting h_k for k = 0..{K_MAX}, evaluating H_j for j = 0..{J_MAX}")
    print()

    # ----------------------------------------------------------------------
    # A1: Sample.
    # ----------------------------------------------------------------------
    print(f"[A1] Sampling h_k^{{(10)}}(a, b) for a ∈ [{SAMPLE_ARANGE[0]}, "
          f"{SAMPLE_ARANGE[1]}), b ∈ [{SAMPLE_ARANGE[0]}, a+1]")
    t0 = time.time()
    per_k = collect_hk_samples(C_VAL, K_MAX, SAMPLE_ARANGE)
    print(f"     samples per k: {[len(per_k[k]) for k in range(K_MAX + 1)]}")
    print(f"     took {time.time() - t0:.1f}s")

    # ----------------------------------------------------------------------
    # A2: Fit each h_k as polynomial.
    # ----------------------------------------------------------------------
    print(f"\n[A2] Fitting h_k^{{(10)}}(a, b) as bivariate polynomial")
    hk_polys = {}
    a_s, b_s = sp.symbols('a b')
    for k in range(K_MAX + 1):
        samples = per_k[k]
        if len(samples) < 15:
            print(f"     k={k}: too few samples ({len(samples)})")
            continue
        t0 = time.time()
        poly, D = fit_bivariate_poly(samples, deg_bound=22)
        dt = time.time() - t0
        if poly is None:
            print(f"     k={k}: NO FIT (dt={dt:.1f}s)")
        else:
            hk_polys[k] = poly
            print(f"     k={k}: deg <= {D:>2d}  ({dt:>5.1f}s)   "
                  f"fits {len(samples)} samples")

    if len(hk_polys) < K_MAX + 1:
        print(f"\n WARNING: only {len(hk_polys)}/{K_MAX + 1} h_k fitted")

    # ----------------------------------------------------------------------
    # A3: Lambdify for fast numeric evaluation.
    # ----------------------------------------------------------------------
    print("\n[A3] Lambdifying h_k polynomials")
    hk_fns = {k: sp.lambdify((a_s, b_s), p, modules='math')
              for k, p in hk_polys.items()}

    def h_k_eval(k, a, b):
        """Evaluate h_k^{(10)}(a, b) exactly (as int)."""
        p = hk_polys[k]
        return int(p.subs({a_s: a, b_s: b}))

    # Fast evaluator using lambdify but round-tripping via int for
    # correctness (h_k are integer-valued, so this is fine for moderate a, b).
    def h_k_eval_fast(k, a, b):
        p = hk_polys[k]
        val = p.subs({a_s: a, b_s: b})
        return int(val)

    # ----------------------------------------------------------------------
    # B: Compute H_10(a, b, j) on full shell via polynomial sum.
    # ----------------------------------------------------------------------
    print(f"\n[B] Computing v_2(H_10(a, b, j)) on shell for j = 0..{J_MAX}")
    par = C_VAL % 2  # 0
    t0 = time.time()
    records = []
    n_eval = 0
    for a in range(0, 2 * T_VAL + 1):
        for b in range(0, 2 * T_VAL + 1):
            if (a + b) % 2 != par:
                continue
            # Precompute h_k values.
            hks_here = {}
            for k in hk_polys:
                hks_here[k] = h_k_eval_fast(k, a, b)
            for j in range(J_MAX + 1):
                H = 0
                complete = True
                for k in range(j + 1):
                    if k not in hks_here:
                        complete = False
                        break
                    H += comb(j, k) * hks_here[k]
                if not complete:
                    continue
                n_eval += 1
                vv = v2(H) if H != 0 else None
                records.append({'a': a, 'b': b, 'j': j, 'H': H, 'v2': vv})
    print(f"    {n_eval} (a,b,j) triples in {time.time() - t0:.1f}s")

    # ----------------------------------------------------------------------
    # C: Find min v_2.
    # ----------------------------------------------------------------------
    finite = [r for r in records if r['v2'] is not None]
    min_v = min(r['v2'] for r in finite)
    achievers = [r for r in finite if r['v2'] == min_v]
    print(f"\n[C] MIN v_2 across sweep = {min_v}")
    print(f"    number of achievers = {len(achievers)}")

    canonical_corners = {(T_VAL - 2, 0), (0, T_VAL - 2),
                         (T_VAL - 2, T_VAL - 2), (0, 0)}

    # split by j
    by_j = {}
    for r in achievers:
        by_j.setdefault(r['j'], []).append(r)

    print("\n    Achievers by j:")
    for j in sorted(by_j):
        rs = by_j[j]
        print(f"      j = {j}: {len(rs)} achievers")
        for r in rs[:12]:
            a, b = r['a'], r['b']
            in_c = (a, b) in canonical_corners
            tag = " [CORNER]" if in_c else " [INTERIOR]"
            print(f"        ({a:>2}, {b:>2})   a%4={a % 4}, b%4={b % 4}{tag}")
        if len(rs) > 12:
            print(f"        ... ({len(rs) - 12} more)")

    # ----------------------------------------------------------------------
    # D: Pick top-1 achiever (prefer INTERIOR, small j, near origin).
    # ----------------------------------------------------------------------
    interior = [r for r in achievers
                if (r['a'], r['b']) not in canonical_corners]
    pool = interior if interior else achievers
    pool.sort(key=lambda r: (r['j'], r['a'] + r['b'], r['a'], r['b']))
    top = pool[0]
    a_star, b_star, j_star = top['a'], top['b'], top['j']
    print(f"\n[D] Top pick: (a*, b*, j*) = ({a_star}, {b_star}, {j_star})")
    print(f"    a* mod 4 = {a_star % 4}, b* mod 4 = {b_star % 4}")
    print(f"    canonical corner? "
          f"{(a_star, b_star) in canonical_corners}")

    # Shift from canonical corners:
    for (ca, cb), name in [((0, 0), "C4"),
                           ((T_VAL - 2, 0), "C1"),
                           ((0, T_VAL - 2), "C2"),
                           ((T_VAL - 2, T_VAL - 2), "C3")]:
        da, db = a_star - ca, b_star - cb
        print(f"    shift from {name}=({ca},{cb}): "
              f"(Δa, Δb) = ({da}, {db})")

    # ----------------------------------------------------------------------
    # E: v_2(h_k) table at (a*, b*).
    # ----------------------------------------------------------------------
    print(f"\n[E] v_2(h_k^{{(10)}}({a_star}, {b_star})) for k = 0..{K_MAX}:")
    v2_hks = []
    for k in range(K_MAX + 1):
        if k not in hk_polys:
            v2_hks.append((k, None, None))
            print(f"    k={k:>2}: NOT FIT")
            continue
        h = h_k_eval_fast(k, a_star, b_star)
        vv = v2(h) if h != 0 else None
        v2_hks.append((k, h, vv))
        lb = LB_C10.get(k)
        eq = "  ← v_2 == LB" if (vv is not None and lb is not None and vv == lb) else ""
        print(f"    k={k:>2}: v_2(h_k) = {vv}   LB_k = {lb}{eq}")

    finite_vs = [(k, vv) for (k, h, vv) in v2_hks if vv is not None]
    min_v_hk = min(vv for (_, vv) in finite_vs)
    argmins = [k for (k, vv) in finite_vs if vv == min_v_hk]
    print(f"\n[F] argmin_k v_2(h_k) at (a*, b*) = {argmins}   (min = {min_v_hk})")
    if len(argmins) == 1:
        k_star = argmins[0]
        print(f"    UNIQUE k* = {k_star}")
    else:
        k_star = argmins[0]
        print(f"    NOT UNIQUE — picking smallest: k* = {k_star}")

    if k_star in LB_C10 and min_v_hk == LB_C10[k_star]:
        print(f"    ✓ v_2(h_{{k*}}) == LB_{{k*}} == {min_v_hk}  "
              f"⇒ SCP single-carrier at k* = {k_star}")
    else:
        print(f"    ! v_2 mismatch  (v_2 = {min_v_hk}, LB = {LB_C10.get(k_star)})")

    # ----------------------------------------------------------------------
    # G: Decompose H_{j*}(a*, b*).
    # ----------------------------------------------------------------------
    print(f"\n[G] Decomposition H_{{j*={j_star}}}({a_star}, {b_star}) = "
          f"sum_{{k<=j*}} C(j*,k) h_k")
    H_sum = 0
    for k in range(j_star + 1):
        if k not in hk_polys:
            continue
        h = h_k_eval_fast(k, a_star, b_star)
        contrib = comb(j_star, k) * h
        H_sum += contrib
        print(f"    k={k:>2}: C({j_star},{k})={comb(j_star, k):>4}   "
              f"v_2(h_k)={v2(h) if h != 0 else None}   "
              f"v_2(contrib)={v2(contrib) if contrib != 0 else None}")
    print(f"    H_pred     = {H_sum}")
    print(f"    v_2(H_pred) = {v2(H_sum)}")

    # ----------------------------------------------------------------------
    # SAVE.
    # ----------------------------------------------------------------------
    out = {
        'note': 'Day 98 - SCP achiever hunt for beta_prime(10)',
        'c': C_VAL,
        'T': T_VAL,
        'target': 14,
        'sweep_min_v2': min_v,
        'j_range': list(range(J_MAX + 1)),
        'shell': f'a,b in [0, {2 * T_VAL}], (a+b) even',
        'n_achievers': len(achievers),
        'achievers_by_j': {j: [(r['a'], r['b']) for r in rs]
                           for j, rs in by_j.items()},
        'top_pick': {
            'a_star': a_star, 'b_star': b_star, 'j_star': j_star,
            'a_mod4': a_star % 4, 'b_mod4': b_star % 4,
            'is_corner': (a_star, b_star) in canonical_corners,
        },
        'v2_h_k_table': [{'k': k, 'v2': vv, 'LB': LB_C10.get(k)}
                         for (k, h, vv) in v2_hks],
        'k_star_argmins': argmins,
        'k_star': k_star,
        'min_v2_h_k': min_v_hk,
        'LB_k_star': LB_C10.get(k_star),
        'scp_single_carrier': (k_star in LB_C10 and min_v_hk == LB_C10[k_star]),
    }

    j_path = '/home/agent/projects/code/2026-07-16-interior-anchor-c10.json'
    with open(j_path, 'w') as f:
        json.dump(out, f, indent=2, default=str)
    print(f"\nSaved {j_path}")

    t_path = '/home/agent/projects/code/2026-07-16-interior-anchor-c10.txt'
    with open(t_path, 'w') as f:
        f.write(f"Day 98 - SCP achiever for beta_prime(10)\n{'=' * 60}\n\n")
        f.write(f"c={C_VAL}, T={T_VAL}, target=14\n")
        f.write(f"Sweep min v_2 = {min_v}   achievers = {len(achievers)}\n\n")
        f.write(f"Top pick: (a*, b*, j*) = ({a_star}, {b_star}, {j_star})\n")
        f.write(f"  a% mod 4 = {a_star % 4}, b% mod 4 = {b_star % 4}\n")
        f.write(f"  interior = {(a_star, b_star) not in canonical_corners}\n\n")
        f.write(f"k* = {k_star}, min v_2(h_k) = {min_v_hk}, LB = {LB_C10.get(k_star)}\n")
        f.write(f"SCP single-carrier: {out['scp_single_carrier']}\n\n")
        f.write("v_2(h_k) table:\n")
        for (k, h, vv) in v2_hks:
            f.write(f"  k={k:>2}: v_2 = {vv},  LB = {LB_C10.get(k)}\n")
        f.write("\nAchievers by j:\n")
        for j in sorted(by_j):
            rs = by_j[j]
            f.write(f"  j={j}: {[(r['a'], r['b']) for r in rs]}\n")
    print(f"Saved {t_path}")

    print("\n" + "=" * 78)
    print("DONE.")
    print("=" * 78)


if __name__ == "__main__":
    main()

"""Day 99 (2026-07-16) — Interior anchor sweep at c = 11 and c = 13 (c-odd).

Purpose: find the c-odd analogue of the (0, 2) anchor discovered at c = 10.
Feeds directly into PROVE-side G3 bonus phase.

Approach (per c):
  1. Fit h_k^{(c)}(a, b) as bivariate polynomial for k = 0..c-1.
  2. Evaluate H_c(a, b, j) = sum_{k<=j} C(j,k) h_k on full shell.
  3. Report (a*, b*, j*, k*) minimum and shift Δb from corner.
  4. Compare with registry β'(c) value.

Hypothesis A2: for c odd, interior anchor at (0, (c-3)/4) with k* = (c-3)/2 + 1.
  c = 11: (c-3)/4 = 2 (integer). Predicted anchor (0, 2, ..., k*=5).
  c = 13: (c-3)/4 = 2.5 (non-integer). Anchor location TBD.
"""

import json
import time
from importlib import util
from math import comb

import sympy as sp

spec = util.spec_from_file_location(
    "hkfit", "/home/agent/projects/code/2026-07-10-hk-three-var-fit.py"
)
hkfit = util.module_from_spec(spec)
spec.loader.exec_module(hkfit)


def v2(n):
    if n == 0:
        return None
    n = abs(int(n))
    v = 0
    while n & 1 == 0:
        n >>= 1
        v += 1
    return v


def T_of(c):
    T = 1
    while T <= c - 2:
        T *= 2
    return T


def collect_hk_samples(c_val, jmax, arange):
    """Return dict {k: [(a, b, y)]} for a >= b >= c_val, a in arange."""
    tables = hkfit.build_e2_tables(max_j=jmax + 2)
    per_k = {k: [] for k in range(jmax + 1)}
    for a in range(arange[0], arange[1]):
        for b in range(max(c_val, arange[0]), a + 1):
            hks = hkfit.extract_h_k(a, b, c_val, jmax, tables)
            if hks is None:
                continue
            for k, y in enumerate(hks):
                per_k[k].append((a, b, y))
    return per_k


def fit_bivariate_poly(samples, deg_bound=22):
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
        verified = True
        for (av, bv, yv) in samples:
            if poly.subs({a_s: av, b_s: bv}) != yv:
                verified = False
                break
        if not verified:
            continue
        return poly, D
    return None, None


def process_c(c_val, registry_beta_prime):
    """Run the anchor sweep at c_val. Returns record dict."""
    T = T_of(c_val)
    K_MAX = c_val - 1
    J_MAX = c_val - 1
    # sample_range: need enough (a, b) with a >= b >= c to fit polys of degree ~c-1.
    # Max degree we'd try ~ 2*c so need num_samples > (2c+1)(2c+2)/2. For c=11, ~276.
    # a range of ~20-25 with b in [c, a] gives roughly (23-11)*13/2 ~ 78 per c… too few.
    # Extend a range accordingly.
    SAMPLE_ARANGE = (c_val, c_val + 30)

    print("\n" + "=" * 78)
    print(f"c = {c_val},  T = {T},  registry β'(c) = {registry_beta_prime}")
    print(f"  fitting h_k for k = 0..{K_MAX}")
    print(f"  sample a range = {SAMPLE_ARANGE}, b in [c, a]")
    print("=" * 78)

    t0 = time.time()
    per_k = collect_hk_samples(c_val, K_MAX, SAMPLE_ARANGE)
    print(f"[A1] Sampling done in {time.time() - t0:.1f}s. "
          f"samples per k: {[len(per_k[k]) for k in range(K_MAX + 1)]}")

    print("\n[A2] Fitting h_k as bivariate polynomial in (a, b)")
    hk_polys = {}
    a_s, b_s = sp.symbols('a b')
    for k in range(K_MAX + 1):
        samples = per_k[k]
        if len(samples) < 20:
            print(f"  k={k}: too few samples ({len(samples)})")
            continue
        t0 = time.time()
        poly, D = fit_bivariate_poly(samples, deg_bound=26)
        dt = time.time() - t0
        if poly is None:
            print(f"  k={k}: NO FIT ({dt:.1f}s)")
        else:
            hk_polys[k] = poly
            print(f"  k={k}: deg <= {D:>2d}  ({dt:>5.1f}s)   fits {len(samples)} samples")

    if not hk_polys:
        print("  NO h_k polynomials fit — aborting c.")
        return None

    # Precompute h_k values on full shell
    print(f"\n[B] Computing v_2(h_k(a,b)) and v_2(H_c(a,b,j)) on shell [0, {2*T}]")
    par = c_val % 2
    t0 = time.time()

    # For each (a, b), precompute {k: h_k(a, b)}.
    records = []
    for a in range(2 * T + 1):
        for b in range(2 * T + 1):
            if (a + b) % 2 != par:
                continue
            hks_here = {}
            for k in hk_polys:
                val = int(hk_polys[k].subs({a_s: a, b_s: b}))
                hks_here[k] = val
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
                vv = v2(H) if H != 0 else None
                if vv is None:
                    continue
                records.append({'a': a, 'b': b, 'j': j, 'v2': vv, 'H': H})
    print(f"  {len(records)} triples in {time.time() - t0:.1f}s")

    # Find min
    min_v = min(r['v2'] for r in records)
    achievers = [r for r in records if r['v2'] == min_v]
    print(f"\n[C] MIN v_2 = {min_v}   achievers = {len(achievers)}")

    canonical_corners = {(T - 2, 0), (0, T - 2), (T - 2, T - 2), (0, 0)}

    # split by j
    by_j = {}
    for r in achievers:
        by_j.setdefault(r['j'], []).append(r)
    print("  Achievers by j:")
    for j in sorted(by_j):
        rs = by_j[j]
        print(f"    j = {j}: {len(rs)} achievers, first few = "
              f"{[(r['a'], r['b']) for r in rs[:8]]}")

    interior = [r for r in achievers
                if (r['a'], r['b']) not in canonical_corners]
    pool = interior if interior else achievers
    pool.sort(key=lambda r: (r['j'], r['a'] + r['b'], r['a'], r['b']))
    top = pool[0]
    a_star, b_star, j_star = top['a'], top['b'], top['j']
    print(f"\n[D] Top pick: (a*, b*, j*) = ({a_star}, {b_star}, {j_star})")
    print(f"  is_corner = {(a_star, b_star) in canonical_corners}")

    # Report shift from each canonical corner
    print("  shifts from corners:")
    shifts = {}
    for (ca, cb), name in [((0, 0), 'C4'),
                            ((T - 2, 0), 'C1'),
                            ((0, T - 2), 'C2'),
                            ((T - 2, T - 2), 'C3')]:
        da, db = a_star - ca, b_star - cb
        shifts[name] = {'delta_a': da, 'delta_b': db}
        print(f"    {name}=({ca},{cb}): (Δa,Δb) = ({da}, {db})")

    # v_2(h_k) table at (a*, b*)
    print(f"\n[E] v_2(h_k(a*, b*)) for k = 0..{K_MAX}:")
    v2_hks = {}
    for k in range(K_MAX + 1):
        if k not in hk_polys:
            v2_hks[k] = None
            print(f"  k={k:>2}: NOT FIT")
            continue
        h = int(hk_polys[k].subs({a_s: a_star, b_s: b_star}))
        vv = v2(h) if h != 0 else None
        v2_hks[k] = vv
        print(f"  k={k:>2}: v_2(h_k) = {vv}")

    finite_vs = {k: v for k, v in v2_hks.items() if v is not None}
    min_v_hk = min(finite_vs.values()) if finite_vs else None
    argmins = [k for k, v in finite_vs.items() if v == min_v_hk]
    print(f"\n[F] argmin_k v_2(h_k) at (a*, b*) = {argmins}  (min = {min_v_hk})")
    k_star = argmins[0] if argmins else None

    # Compare with registry
    print(f"\n[G] REGISTRY CHECK: β'({c_val}) = {registry_beta_prime}")
    print(f"    Sweep min v_2   = {min_v}")
    matches = (min_v == registry_beta_prime)
    print(f"    Registry match: {'YES' if matches else 'NO'}")

    # Corner v_2s for comparison
    print("\n[H] Corner v_2 values:")
    corner_v2s = {}
    for (ca, cb) in canonical_corners:
        # for each corner find best j
        j_best = None
        v_best = None
        for j in range(J_MAX + 1):
            H = 0
            complete = True
            for k in range(j + 1):
                if k not in hk_polys:
                    complete = False
                    break
                H += comb(j, k) * int(hk_polys[k].subs({a_s: ca, b_s: cb}))
            if not complete:
                continue
            vv = v2(H) if H != 0 else None
            if vv is None:
                continue
            if v_best is None or vv < v_best:
                v_best = vv
                j_best = j
        corner_v2s[(ca, cb)] = (v_best, j_best)
        print(f"  ({ca:>3},{cb:>3}): min_v_2 = {v_best} at j = {j_best}")

    return {
        'c': c_val,
        'T': T,
        'registry_beta_prime': registry_beta_prime,
        'sweep_min_v2': min_v,
        'registry_match': matches,
        'a_star': a_star,
        'b_star': b_star,
        'j_star': j_star,
        'k_star': k_star,
        'k_star_argmins': argmins,
        'min_v_hk_at_star': min_v_hk,
        'is_corner_top': (a_star, b_star) in canonical_corners,
        'shifts_from_corners': shifts,
        'v2_hks_at_star': v2_hks,
        'corner_v2_summary': {f"({ca},{cb})": {'v2': v, 'j': j}
                              for (ca, cb), (v, j) in corner_v2s.items()},
        'n_achievers': len(achievers),
        'achievers_by_j': {j: [(r['a'], r['b']) for r in rs]
                           for j, rs in by_j.items()},
    }


def main():
    print("=" * 78)
    print("Day 99 (2026-07-16) — Interior anchor sweep, c ∈ {11, 13}")
    print("=" * 78)

    # Registry values from SUMMARY
    REGISTRY = {11: 12, 13: 16}

    results = {}
    for c in [11, 13]:
        rec = process_c(c, REGISTRY[c])
        if rec is not None:
            results[c] = rec

    # Hypothesis A2 test
    print("\n" + "=" * 78)
    print("HYPOTHESIS A2 TEST")
    print("=" * 78)
    print("Hypothesis: for c odd, interior anchor at (0, (c-3)/4) with k* = (c-3)/2 + 1")
    for c in [11, 13]:
        pred_b = (c - 3) / 4
        pred_k = (c - 3) // 2 + 1
        pred_str = f"(0, {pred_b}, ..., k*={pred_k})"
        if c in results:
            r = results[c]
            observed = f"({r['a_star']}, {r['b_star']}, {r['j_star']}, k*={r['k_star']})"
            supported = (r['a_star'] == 0 and r['b_star'] == int(pred_b) and pred_b == int(pred_b))
            print(f"  c = {c}: predicted {pred_str}, observed {observed}, supported = {supported}")
        else:
            print(f"  c = {c}: NO DATA")

    outpath = '/home/agent/projects/code/2026-07-16-day99-interior-anchor-c11-c13.json'
    with open(outpath, 'w') as f:
        json.dump({'note': 'Day 99 interior anchor c odd sweep',
                   'date': '2026-07-16',
                   'results_by_c': results,
                   'registry': REGISTRY}, f, indent=2, default=str)
    print(f"\nSaved {outpath}")

    txtpath = '/home/agent/projects/code/2026-07-16-day99-interior-anchor-c11-c13.txt'
    with open(txtpath, 'w') as f:
        f.write(f"Day 99 — Interior anchor c ∈ {{11, 13}}\n{'=' * 60}\n\n")
        for c in [11, 13]:
            if c not in results:
                f.write(f"c = {c}: NO DATA\n\n")
                continue
            r = results[c]
            f.write(f"c = {c}: β'({c}) = {r['registry_beta_prime']} "
                    f"({'confirmed' if r['registry_match'] else 'REFUTED'})\n")
            f.write(f"  anchor (a*, b*, j*, k*) = ({r['a_star']}, {r['b_star']}, "
                    f"{r['j_star']}, {r['k_star']})\n")
            f.write(f"  sweep min v_2 = {r['sweep_min_v2']}\n")
            f.write(f"  shifts from corners: {r['shifts_from_corners']}\n\n")
    print(f"Saved {txtpath}")


if __name__ == "__main__":
    main()

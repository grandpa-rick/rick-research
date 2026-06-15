"""
Day 72 CODE Task C -- Even-n Lambda at n=8 + facet count at n=12, 13.

(1) Enumerate AII cone extreme rays at n = 8.
    Predicted by Day-70 Theorem 4.2: at even n, the linking equation
    linkLHS = sum(short[i]) collapses one ray relative to the 3n-ray odd
    pattern, giving 3n - 1 extreme rays.
    Expected at n=8: 3*8 - 1 = 23 rays.

(2) Cross-check the closed form
        #{AII facets} = 3n - [n even]
    at n = 12, 13.
    Expected: n=12 -> 35 facets; n=13 -> 39 facets.

(3) BDI facet closed form #{BDI facets} = 4n - 5 at n = 12, 13.
    Expected: n=12 -> 43; n=13 -> 47.

(4) Period-2 finite-difference check (Day-58 calibration rule).
    Combine with prior series at n=3..11.
"""

import sys
import json
import time
from pathlib import Path

sys.path.insert(0, '/home/agent/projects/code/2026-06-14-azenhas-aii-walls')
sys.path.insert(0, '/home/agent/projects/code/2026-06-16-even-n-lambda')
from azenhas_aii_walls import (  # noqa: E402
    azenhas_system_TheoremDE_strict, azenhas_system_aii_structure,
    bdi_system, count_facets,
)
from run import enumerate_rays, labelled_ray  # noqa: E402

OUT_DIR = Path("/home/agent/projects/code/2026-06-17-facets-n12-n13")
OUT_DIR.mkdir(exist_ok=True)


def predicted_aii(n):
    return 3 * n - (1 if n % 2 == 0 else 0)


def predicted_bdi(n):
    return 4 * n - 5


def run_rays_at(n):
    """Enumerate AII cone extreme rays at level n."""
    print(f"\n--- AII rays at n = {n} ---")
    A_ub, b_ub, A_eq, b_eq, labels, n_vars, vars_list = (
        azenhas_system_TheoremDE_strict(n)
    )
    t0 = time.time()
    r = enumerate_rays(A_ub, b_ub, A_eq, b_eq, labels)
    dt = time.time() - t0
    pred = predicted_aii(n)
    r["closed_form_pred"] = pred
    r["closed_form_match"] = (r["n_rays"] == pred)
    r["n_vars"] = n_vars
    r["vars"] = vars_list
    for ray_info in r["rays"]:
        ray_info["labelled"] = labelled_ray(ray_info["ray"], vars_list)
    print(f"  n_rays = {r['n_rays']}  (predicted = {pred})  "
          f"{'MATCH' if r['closed_form_match'] else 'MISMATCH'}  "
          f"[{dt:.1f}s]")
    if not r["closed_form_match"]:
        print(f"  Listing all rays:")
        for ri, ray_info in enumerate(r["rays"]):
            print(f"    ray[{ri}] = {ray_info['labelled']}")
    return r


def run_facets_at(n):
    """Count AII and BDI facets at level n."""
    print(f"\n--- Facets at n = {n} ---")
    out = {"n": n}

    # AII (aii_structure -- the canonical version per Day-69)
    t0 = time.time()
    A_ub, b_ub, A_eq, b_eq, labels, n_vars, vars_list = (
        azenhas_system_aii_structure(n)
    )
    print(f"  [AII aii_structure] vars={n_vars}, ineqs={A_ub.shape[0]}")
    res = count_facets(A_ub, b_ub, A_eq, b_eq, labels)
    dt = time.time() - t0
    pred = predicted_aii(n)
    match = (res["n_facets"] == pred)
    print(f"    facets = {res['n_facets']}  (predicted {pred})  "
          f"{'MATCH' if match else 'MISMATCH'}  [{dt:.1f}s]")
    out["AII"] = {
        "n_facets": res["n_facets"],
        "n_redundant": res["n_redundant"],
        "predicted": pred,
        "match": match,
        "wall_s": dt,
    }

    # BDI
    t0 = time.time()
    A_ub, b_ub, A_eq, b_eq, labels, n_vars, vars_list = bdi_system(n)
    print(f"  [BDI] vars={n_vars}, ineqs={A_ub.shape[0]}")
    res = count_facets(A_ub, b_ub, A_eq, b_eq, labels)
    dt = time.time() - t0
    pred = predicted_bdi(n)
    match = (res["n_facets"] == pred)
    print(f"    facets = {res['n_facets']}  (predicted {pred})  "
          f"{'MATCH' if match else 'MISMATCH'}  [{dt:.1f}s]")
    out["BDI"] = {
        "n_facets": res["n_facets"],
        "n_redundant": res["n_redundant"],
        "predicted": pred,
        "match": match,
        "wall_s": dt,
    }
    return out


def period2_diff(series):
    """Period-2 finite difference: a[i+2] - a[i] should be constant
    (= 6 for AII, = 8 for BDI)."""
    return [series[i + 2] - series[i] for i in range(len(series) - 2)]


def main():
    print("=" * 72)
    print("Day 72 CODE Task C -- AII rays at n=8 + facet count n=12, 13")
    print("=" * 72)

    results = {}

    # (1) AII rays at n = 8
    rays_n8 = run_rays_at(8)
    results["rays_n8"] = rays_n8

    # (2,3) Facets at n = 12, 13
    facets = {}
    for n in [12, 13]:
        facets[n] = run_facets_at(n)
    results["facets"] = facets

    # (4) Period-2 finite-difference check.
    print(f"\n{'='*72}")
    print(f"Period-2 finite difference (Day-58 calibration rule)")
    print(f"{'='*72}")

    # Combine Day-69 (n=3..8) + Day-70 (n=9..11) + Day-72 (n=12, 13)
    # AII series at n=3..13:
    aii_series = [9, 11, 15, 17, 21, 23,    # n=3..8 (Day-69)
                   27, 29, 33,              # n=9..11 (Day-70)
                   facets[12]["AII"]["n_facets"],
                   facets[13]["AII"]["n_facets"]]
    # BDI series at n=3..13:
    bdi_series = [7, 11, 15, 19, 23, 27,    # n=3..8 (Day-69)
                   31, 35, 39,              # n=9..11 (Day-70)
                   facets[12]["BDI"]["n_facets"],
                   facets[13]["BDI"]["n_facets"]]

    print(f"  AII series (n=3..13): {aii_series}")
    print(f"  BDI series (n=3..13): {bdi_series}")

    aii_d2 = period2_diff(aii_series)
    bdi_d2 = period2_diff(bdi_series)
    print(f"  AII period-2 diff:    {aii_d2}  (predicted const = 6 for 3n)")
    print(f"  BDI period-2 diff:    {bdi_d2}  (predicted const = 8 for 4n)")

    aii_d2_ok = all(d == 6 for d in aii_d2)
    bdi_d2_ok = all(d == 8 for d in bdi_d2)
    print(f"  AII period-2 = 6 everywhere? {aii_d2_ok}")
    print(f"  BDI period-2 = 8 everywhere? {bdi_d2_ok}")

    # Verdict
    rays_ok = rays_n8["closed_form_match"]
    facets_ok = all(facets[n]["AII"]["match"] and facets[n]["BDI"]["match"]
                    for n in [12, 13])
    overall_ok = rays_ok and facets_ok and aii_d2_ok and bdi_d2_ok

    print(f"\n{'='*72}")
    print(f"VERDICT")
    print(f"{'='*72}")
    if overall_ok:
        verdict = (
            "CONFIRMED: AII rays count at n=8 = 3n-1 = 23; closed-form "
            "facet counts AII = 3n-[n even] = 35, 39 and BDI = 4n-5 = 43, 47 "
            "hold at n=12, 13; period-2 finite differences are constant "
            "(AII: 6, BDI: 8) throughout n=3..13. Day-69 quasi-poly fit "
            "extends through n=13."
        )
    else:
        bad = []
        if not rays_ok:
            bad.append(f"rays at n=8 ({rays_n8['n_rays']} vs 23)")
        for n in [12, 13]:
            if not facets[n]["AII"]["match"]:
                bad.append(f"AII facets at n={n}")
            if not facets[n]["BDI"]["match"]:
                bad.append(f"BDI facets at n={n}")
        if not aii_d2_ok:
            bad.append(f"AII period-2 != 6")
        if not bdi_d2_ok:
            bad.append(f"BDI period-2 != 8")
        verdict = "PARTIAL: " + "; ".join(bad)
    print(verdict)

    save = {
        "verdict": verdict,
        "rays_n8": rays_n8,
        "facets": facets,
        "aii_series_n3_n13": aii_series,
        "bdi_series_n3_n13": bdi_series,
        "aii_period2_diff": aii_d2,
        "bdi_period2_diff": bdi_d2,
        "aii_period2_const_ok": aii_d2_ok,
        "bdi_period2_const_ok": bdi_d2_ok,
    }
    with open(OUT_DIR / "results.json", "w") as f:
        json.dump(save, f, indent=2, default=str)
    print(f"\nsaved {OUT_DIR / 'results.json'}")


if __name__ == "__main__":
    main()

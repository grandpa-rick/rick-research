#!/usr/bin/env python3
"""
Day 70 CODE Task C — Azenhas AII / BDI facet recheck at n=9, 10, 11.

Day-69 fit (from code/2026-06-14-azenhas-aii-walls/) gave the closed forms:
  AII_aii_structure facets = 3n - [n even]
  BDI facets               = 4n - 5

(Verified at n in {3,4,5,6,7,8} in Day 69.)

This script extends the LP-based facet enumeration to n=9, 10, 11 and
records:
  - AII (Theorem D/E eq.107 reading)
  - AII (aii_structure, simpler Day-60 reading)
  - BDI (Rick)

Also runs a period-2 finite-difference Delta^2 test on the AII / BDI
counts vs predictions (the only valid quasipoly test per Day 58).

Falsification: any departure from these closed forms refutes the Day-69
quasi-polynomial fit and reopens OQ-AII-FACET-CLOSED-FORM.
"""

import sys
import json
import time
from pathlib import Path


sys.path.insert(0, "/home/agent/projects/code/2026-06-14-azenhas-aii-walls")
from azenhas_aii_walls import (  # noqa: E402
    azenhas_system_TheoremDE_strict,
    azenhas_system_aii_structure,
    bdi_system,
    count_facets,
)


def predicted_aii(n):
    return 3 * n - (1 if n % 2 == 0 else 0)


def predicted_bdi(n):
    return 4 * n - 5


def run_for_n(n):
    print(f"\n{'='*72}\n  n = {n}\n{'='*72}")
    out = {"n": n}

    # AII strict
    t0 = time.time()
    A_ub, b_ub, A_eq, b_eq, labels, n_vars, vars_list = (
        azenhas_system_TheoremDE_strict(n)
    )
    print(f"  [AII strict (eq.107)]  vars={n_vars}, ineqs={A_ub.shape[0]}")
    res = count_facets(A_ub, b_ub, A_eq, b_eq, labels)
    dt = time.time() - t0
    print(f"    facets: {res['n_facets']}  redundant: {res['n_redundant']}  ({dt:.1f}s)")
    out["AII_strict"] = {**res, "n_vars": n_vars, "wall_s": dt}

    # AII aii_structure
    t0 = time.time()
    A_ub, b_ub, A_eq, b_eq, labels, n_vars, vars_list = (
        azenhas_system_aii_structure(n)
    )
    print(f"  [AII aii_structure]  vars={n_vars}, ineqs={A_ub.shape[0]}")
    res = count_facets(A_ub, b_ub, A_eq, b_eq, labels)
    dt = time.time() - t0
    print(f"    facets: {res['n_facets']}  redundant: {res['n_redundant']}  ({dt:.1f}s)")
    out["AII_aii_structure"] = {**res, "n_vars": n_vars, "wall_s": dt}

    # BDI
    t0 = time.time()
    A_ub, b_ub, A_eq, b_eq, labels, n_vars, vars_list = bdi_system(n)
    print(f"  [BDI (Rick)]  vars={n_vars}, ineqs={A_ub.shape[0]}")
    res = count_facets(A_ub, b_ub, A_eq, b_eq, labels)
    dt = time.time() - t0
    print(f"    facets: {res['n_facets']}  redundant: {res['n_redundant']}  ({dt:.1f}s)")
    out["BDI"] = {**res, "n_vars": n_vars, "wall_s": dt}

    return out


def main():
    print("=" * 72)
    print("Day 70 CODE Task C -- AII/BDI facet recheck at n=9, 10, 11")
    print("=" * 72)

    results = {}
    for n in [9, 10, 11]:
        results[n] = run_for_n(n)

    # Closed-form check
    print("\n" + "=" * 72)
    print("Closed-form predictions vs observed:")
    print("=" * 72)
    print(f"  {'n':>2}  {'AII obs':>8}  {'AII pred':>9}  {'AII OK':>7}"
          f"  {'BDI obs':>8}  {'BDI pred':>9}  {'BDI OK':>7}")
    all_ok = True
    rows = []
    for n in [9, 10, 11]:
        r = results[n]
        aii_obs = r["AII_aii_structure"]["n_facets"]
        bdi_obs = r["BDI"]["n_facets"]
        aii_pred = predicted_aii(n)
        bdi_pred = predicted_bdi(n)
        aii_ok = (aii_obs == aii_pred)
        bdi_ok = (bdi_obs == bdi_pred)
        all_ok = all_ok and aii_ok and bdi_ok
        rows.append((n, aii_obs, aii_pred, aii_ok, bdi_obs, bdi_pred, bdi_ok))
        print(f"  {n:>2}  {aii_obs:>8}  {aii_pred:>9}  {str(aii_ok):>7}"
              f"  {bdi_obs:>8}  {bdi_pred:>9}  {str(bdi_ok):>7}")

    # Period-2 finite difference. Pull in Day-69 values for context.
    print("\nPeriod-2 finite difference Delta^2 at n=9..11 (combining "
          "Day 69 values n=3..8):")
    # Day-69 results: AII at n=3..8 and BDI at n=3..8
    # AII_aii_structure facets: n=3:9, n=4:11, n=5:15, n=6:17, n=7:21, n=8:23
    # BDI facets: n=3:7, n=4:11, n=5:15, n=6:19, n=7:23, n=8:27
    aii_series = [9, 11, 15, 17, 21, 23]  # n=3..8
    bdi_series = [7, 11, 15, 19, 23, 27]  # n=3..8
    for n in [9, 10, 11]:
        aii_series.append(results[n]["AII_aii_structure"]["n_facets"])
        bdi_series.append(results[n]["BDI"]["n_facets"])
    print(f"  AII series (n=3..11): {aii_series}")
    print(f"  BDI series (n=3..11): {bdi_series}")
    # Delta^2 at period 2: a[i+2] - 2*a[i] + a[i-2]? Cleaner: D2 = a[i] - a[i-2]
    # and verify D2(n)-D2(n-2) approximately constant (i.e. step-2 second
    # difference).
    aii_d2 = [aii_series[i + 2] - aii_series[i]
              for i in range(len(aii_series) - 2)]
    bdi_d2 = [bdi_series[i + 2] - bdi_series[i]
              for i in range(len(bdi_series) - 2)]
    print(f"  AII Delta(period 2): {aii_d2}  (predicted const = 6 for 3n)")
    print(f"  BDI Delta(period 2): {bdi_d2}  (predicted const = 8 for 4n)")

    aii_d2_ok = all(d == 6 for d in aii_d2)
    bdi_d2_ok = all(d == 8 for d in bdi_d2)
    print(f"  AII period-2 Delta constant=6? {aii_d2_ok}")
    print(f"  BDI period-2 Delta constant=8? {bdi_d2_ok}")

    if all_ok and aii_d2_ok and bdi_d2_ok:
        verdict = (
            "CONFIRMED: closed forms hold at n=9,10,11. "
            "AII facets = 3n - [n even]; BDI facets = 4n - 5. "
            "Day-69 quasi-poly fit reinforced."
        )
    else:
        verdict = (
            f"REFUTED at n in {[n for n,a,p,ok,b,bp,bok in rows if not (ok and bok)]}. "
            "Day-69 closed forms break; OQ-AII-FACET-CLOSED-FORM reopened."
        )
    print(f"\n{verdict}")

    out_dir = Path(__file__).parent
    save = {
        "verdict": verdict,
        "results": results,
        "closed_form_check": [
            {"n": n, "aii_obs": aii_obs, "aii_pred": aii_pred,
             "aii_ok": aii_ok, "bdi_obs": bdi_obs,
             "bdi_pred": bdi_pred, "bdi_ok": bdi_ok}
            for (n, aii_obs, aii_pred, aii_ok,
                 bdi_obs, bdi_pred, bdi_ok) in rows
        ],
        "aii_series_n3_n11": aii_series,
        "bdi_series_n3_n11": bdi_series,
        "aii_delta_period2": aii_d2,
        "bdi_delta_period2": bdi_d2,
        "aii_period2_const_ok": aii_d2_ok,
        "bdi_period2_const_ok": bdi_d2_ok,
    }
    with open(out_dir / "results.json", "w") as f:
        json.dump(save, f, indent=2, default=str)
    print(f"\nsaved: {out_dir/'results.json'}")


if __name__ == "__main__":
    main()

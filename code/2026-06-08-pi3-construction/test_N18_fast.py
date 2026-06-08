"""Fast version: cache AII enumeration; test at N=16, 18, 20 only.
Pre-computes auto-pieces once."""

import sys, time
from pathlib import Path
from math import gcd
from functools import reduce
sys.path.insert(0, str(Path(__file__).parent))

from verify_full import (enumerate_aii_n3_full, bdi_feasible_n3,
                          enumerate_bdi_n3, apply_pi)
from verify_full_v9 import ALL_PI as REG, get_image
from auto_construct import construct_for_target


def fast_image(spec, N, aii_cache):
    """Image of piece using cached AII enumeration."""
    image = set()
    bad = 0
    for p in aii_cache:
        q = apply_pi(spec, p)
        ok, _ = bdi_feasible_n3(q)
        if not ok:
            bad += 1
            continue
        image.add((q["M_1"], q["M_2"], q["B_1"], q["T_1"],
                   q["B_2"], q["T_2"], q["S"]))
    return image, bad


def main():
    # Build auto-pieces for missing at N=15 (these cover those + multiples).
    print("Building auto-pieces for missing at N<=15...")
    bdi15 = enumerate_bdi_n3(15)
    union15 = set()
    for name in REG:
        img, _, _ = get_image(name, 15)
        union15 |= img
    missing15 = sorted(bdi15 - union15)
    print(f"Missing at N=15: {len(missing15)}")

    auto_specs = {}
    for q in missing15:
        result = construct_for_target(q)
        if result is not None:
            _, spec = result
            name = f"auto_{q[1]}_{q[2]}_{q[3]}_{q[4]}_{q[5]}_{q[6]}"
            auto_specs[name] = spec
    print(f"Auto-pieces constructed: {len(auto_specs)}")

    Ns_to_test = [16, 17, 18]
    for N in Ns_to_test:
        t0 = time.time()
        # Cache AII enumeration
        aii = enumerate_aii_n3_full(N)
        print(f"\n--- N = {N} ---")
        print(f"  AII pts: {len(aii)}")

        bdi_pts = enumerate_bdi_n3(N)
        print(f"  BDI pts: {len(bdi_pts)}")

        # All pieces (v9 + auto)
        union = set()
        # v9 pieces
        for name, spec in REG.items():
            img, _ = fast_image(spec, N, aii)
            union |= img
        # auto pieces
        for name, spec in auto_specs.items():
            img, _ = fast_image(spec, N, aii)
            union |= img

        cov = len(union & bdi_pts)
        pct = 100 * cov / len(bdi_pts) if bdi_pts else 0
        missing = bdi_pts - union
        # primitive count
        prims = []
        for q in sorted(missing):
            _, M_2, B_1, T_1, B_2, T_2, S = q
            nz = [v for v in (M_2, B_1, T_1, B_2, T_2, S) if v > 0]
            if not nz:
                continue
            g = reduce(gcd, nz)
            if g == 1:
                prims.append(q)

        dt = time.time() - t0
        print(f"  coverage: {cov}/{len(bdi_pts)} = {pct:.2f}%  ({dt:.1f}s)")
        print(f"  missing: {len(missing)} ({len(prims)} primitive)")
        if prims:
            print(f"  First 10 PRIMITIVE missing:")
            for q in prims[:10]:
                _, M_2, B_1, T_1, B_2, T_2, S = q
                P_1 = 2*(B_1-T_1); P_2 = P_1 + 2*(B_2-T_2)
                print(f"    M2={M_2} B1={B_1} T1={T_1} B2={B_2} T2={T_2} S={S}  "
                      f"P_1={P_1} P_2={P_2}")


if __name__ == "__main__":
    main()

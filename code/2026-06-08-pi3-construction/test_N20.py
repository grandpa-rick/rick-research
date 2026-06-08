"""Push to N=20: verify that the auto-constructed registry covers all BDI
points, OR detect new primitive missing directions.
"""

import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from verify_full import (enumerate_aii_n3_full, bdi_feasible_n3,
                          enumerate_bdi_n3, apply_pi)
from verify_full_v9 import ALL_PI as REGISTRY_V9, get_image
from auto_construct import construct_for_target, piece_image, make_piece


def main():
    # Build registry: existing v9 + auto-constructed for N<=15 missing.
    print("Building registry...")
    auto_specs = {}
    seen_targets = set()
    # First seed: collect ALL missing primitives at N<=15 under V9.
    for N in [11, 12, 13, 14, 15]:
        bdi_pts = enumerate_bdi_n3(N)
        union = set()
        for name in REGISTRY_V9:
            img, _, _ = get_image(name, N)
            union |= img
        # Also subtract auto-pieces added so far
        for name, spec in auto_specs.items():
            img, _ = piece_image(spec, N)
            union |= img
        missing = sorted(bdi_pts - union)
        for q in missing:
            if q in seen_targets:
                continue
            seen_targets.add(q)
            result = construct_for_target(q)
            if result is not None:
                _, spec = result
                name = f"auto_{q[1]}_{q[2]}_{q[3]}_{q[4]}_{q[5]}_{q[6]}"
                auto_specs[name] = spec

    print(f"Auto-constructed pieces: {len(auto_specs)}")

    # Now test at N=16..20
    print(f"\n{'N':>3} | {'|BDI|':>8} | {'covered':>8} | {'coverage':>10} | {'time (s)':>9}")
    print("-" * 60)

    for N in [16, 17, 18, 19, 20]:
        t0 = time.time()
        bdi_pts = enumerate_bdi_n3(N)
        union = set()
        for name in REGISTRY_V9:
            img, _, _ = get_image(name, N)
            union |= img
        for name, spec in auto_specs.items():
            img, _ = piece_image(spec, N)
            union |= img
        cov = len(union & bdi_pts)
        dt = time.time() - t0
        pct = 100 * cov / len(bdi_pts) if bdi_pts else 0
        missing = bdi_pts - union
        # Identify PRIMITIVE missing (not a multiple of smaller BDI in lattice)
        primitives_missing = []
        for q in sorted(missing):
            _, M_2, B_1, T_1, B_2, T_2, S = q
            from math import gcd
            from functools import reduce
            nonzero = [v for v in (M_2, B_1, T_1, B_2, T_2, S) if v > 0]
            if not nonzero:
                continue
            g = reduce(gcd, nonzero)
            if g == 1:
                primitives_missing.append(q)
        print(f"{N:>3} | {len(bdi_pts):>8} | {cov:>8} | {pct:>9.2f}% | {dt:>9.2f}  "
              f"  missing={len(missing)}, primitive={len(primitives_missing)}")
        # If primitive missing exist, show a few:
        if primitives_missing:
            print(f"    First 10 PRIMITIVE missing:")
            for q in primitives_missing[:10]:
                _, M_2, B_1, T_1, B_2, T_2, S = q
                P_1 = 2*(B_1-T_1); P_2 = P_1 + 2*(B_2-T_2)
                print(f"      M2={M_2} B1={B_1} T1={T_1} B2={B_2} T2={T_2} S={S}  "
                      f"P_1={P_1} P_2={P_2}")


if __name__ == "__main__":
    main()

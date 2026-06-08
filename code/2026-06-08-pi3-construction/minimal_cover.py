"""
Find a MINIMAL subset of the 55 linear maps whose image-union covers all
BDI lattice points at N <= 10.

Greedy set cover.
"""

from verify_full import (enumerate_aii_n3_full, bdi_feasible_n3,
                          enumerate_bdi_n3, apply_pi)
from verify_full import PROJECTIONS as P2
from verify_full_v3 import PROJECTIONS as P3
from verify_full_v4 import PROJECTIONS as P4
from verify_full_v5 import P5_EXTRA as P5
from verify_full_v6 import P6_EXTRA as P6
from verify_full_v7 import P7_EXTRA as P7

ALL_PI = {**P2, **P3, **P4, **P5, **P6, **P7}


def get_image(name, N):
    spec = ALL_PI[name]
    aii_pts = enumerate_aii_n3_full(N)
    image = set()
    for p in aii_pts:
        q = apply_pi(spec, p)
        ok, _ = bdi_feasible_n3(q)
        if not ok:
            continue
        image.add((q["M_1"], q["M_2"], q["B_1"], q["T_1"],
                   q["B_2"], q["T_2"], q["S"]))
    return image


def greedy_cover(N):
    print(f"\n=== Greedy minimal cover at N = {N} ===")
    bdi = enumerate_bdi_n3(N)
    images = {name: get_image(name, N) for name in ALL_PI}

    covered = set()
    chosen = []
    while covered != bdi:
        # Pick map that adds most new coverage
        best = None
        best_gain = -1
        for name in ALL_PI:
            if name in chosen:
                continue
            gain = len(images[name] - covered) - len(images[name] - bdi)*0  # don't penalize extra
            gain = len((images[name] & bdi) - covered)
            if gain > best_gain:
                best_gain = gain
                best = name
        if best is None or best_gain == 0:
            print(f"  Stuck after {len(chosen)} maps; covered {len(covered)}/{len(bdi)}")
            break
        chosen.append(best)
        covered |= (images[best] & bdi)
        print(f"  +{best:35s}: +{best_gain:4d} = {len(covered):4d}/{len(bdi)}")

    print(f"\n  Minimal cover: {len(chosen)} maps, covers {len(covered)}/{len(bdi)} ({100*len(covered)/len(bdi):.1f}%)")
    return chosen


def main():
    chosen = greedy_cover(10)
    print(f"\n\nMinimal piecewise cover at N=10:")
    for name in chosen:
        print(f"  - {name}")

    # Verify the minimal cover at all N
    print("\n\n=== Verify minimal cover ===")
    for N in [4, 5, 6, 7, 8, 9, 10]:
        bdi = enumerate_bdi_n3(N)
        covered = set()
        for name in chosen:
            covered |= (get_image(name, N) & bdi)
        cov = len(covered)
        print(f"  N={N}: {cov}/{len(bdi)} = {100*cov/len(bdi):.1f}%")


if __name__ == "__main__":
    main()

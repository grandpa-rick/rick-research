"""
Day 62 — Stratification by which of m_2, m_236, m_23456 vanish.

The codim-1 walls of the kernel arrangement (inside the AII cone) are
exactly the three coordinate hyperplanes
    m_2 = 0, m_236 = 0, m_23456 = 0.
Combined: 8 strata according to the sign-pattern of these three.

Conjecture: |I(p)| is a function of which of {m_2, m_236, m_23456}
are zero / nonzero.  At p in the interior stratum (all three > 0),
|I(p)| = 26.  As more axes vanish, |I(p)| collapses.

Compute the stratification.
"""

import sys
sys.path.insert(0, '/home/agent/projects/code/2026-06-08-pi3-construction')
sys.path.insert(0, '/home/agent/projects/code/2026-06-10-toric-quotient')

from collections import defaultdict, Counter

from verify_full_v9 import ALL_PI
from verify_full import enumerate_aii_n3_full, bdi_feasible_n3, apply_pi
from analyze_torus import MIN_COVER_26


def piece_image(spec, p):
    q = apply_pi(spec, p)
    ok, _ = bdi_feasible_n3(q)
    if not ok:
        return None
    return (q["M_1"], q["M_2"], q["B_1"], q["T_1"], q["B_2"], q["T_2"], q["S"])


def main():
    pieces = [name for name in MIN_COVER_26 if name in ALL_PI]
    N = 8
    aii_pts = enumerate_aii_n3_full(N)

    # Group p by sign-pattern (m_2>0, m_236>0, m_23456>0).
    strat = defaultdict(list)
    for p in aii_pts:
        sig = (
            1 if p["m_2"] > 0 else 0,
            1 if p["m_236"] > 0 else 0,
            1 if p["m_23456"] > 0 else 0,
        )
        V = [i for i, name in enumerate(pieces) if piece_image(ALL_PI[name], p) is not None]
        I = set()
        for i in V:
            q = piece_image(ALL_PI[pieces[i]], p)
            if q is not None:
                I.add(q)
        strat[sig].append((p, len(V), len(I)))

    sig_names = ["m_2=0", "m_236=0", "m_23456=0"]
    print(f"\nStratification by (m_2>0, m_236>0, m_23456>0) at N={N}:")
    print(f"{'sig':>10} | {'# pts':>6} | {'mean |V|':>9} | {'mean |I|':>9} | {'|I| range':>10}")
    print("-" * 65)
    for sig in sorted(strat):
        pts = strat[sig]
        nV = [v for _, v, _ in pts]
        nI = [i for _, _, i in pts]
        sig_str = "".join(f"{s}" for s in sig)
        print(f"   {sig_str:>7} | {len(pts):>6} | {sum(nV)/len(nV):>9.2f} | {sum(nI)/len(nI):>9.2f} | [{min(nI)}, {max(nI)}]")

    # Distribution of |I(p)| within the "fully interior" stratum (1, 1, 1).
    if (1, 1, 1) in strat:
        pts = strat[(1, 1, 1)]
        nI_dist = Counter(i for _, _, i in pts)
        print(f"\nFully interior stratum (m_2, m_236, m_23456 > 0): |I| distribution:")
        for k in sorted(nI_dist):
            print(f"  |I|={k:2d} : {nI_dist[k]:6d} pts")


if __name__ == "__main__":
    main()

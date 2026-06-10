"""
Day 62 — Fiber stratification of P^AII by piece-cardinality.

For each AII lattice point p with |p| <= N, compute
    V(p) = {i in [26] : pi^(i)(p) lies in P^BDI},
    I(p) = {pi^(i)(p) : i in V(p)}.

Report distributions of |V(p)| and |I(p)|, with the crucial dichotomy:
   "Is |I(p)| = 1 for all p?"  (Candidate A redundancy stack)
vs "Is there p with |I(p)| > 1?" (Candidate B genuine multivaluedness)

Output: JSON + a short stdout summary.
"""

import sys
from pathlib import Path
sys.path.insert(0, '/home/agent/projects/code/2026-06-08-pi3-construction')
sys.path.insert(0, '/home/agent/projects/code/2026-06-10-toric-quotient')

import json
from collections import Counter

from verify_full_v9 import ALL_PI
from verify_full import enumerate_aii_n3_full, bdi_feasible_n3, apply_pi
from analyze_torus import MIN_COVER_26


def piece_image(spec, p):
    """Apply a piece to AII point p; return BDI tuple or None if infeasible."""
    q = apply_pi(spec, p)
    ok, _ = bdi_feasible_n3(q)
    if not ok:
        return None
    return (q["M_1"], q["M_2"], q["B_1"], q["T_1"], q["B_2"], q["T_2"], q["S"])


def compute_VI(N, pieces):
    """For each AII lattice pt p with |p| <= N, compute V(p) and I(p).

    Returns list of dicts: {p, V_idx, I_set}.
    """
    aii_pts = enumerate_aii_n3_full(N)
    specs = [(name, ALL_PI[name]) for name in pieces]
    rows = []
    for p in aii_pts:
        V = []
        I = set()
        for i, (name, spec) in enumerate(specs):
            q = piece_image(spec, p)
            if q is not None:
                V.append(i)
                I.add(q)
        rows.append({
            "p": p,
            "V": V,
            "I": list(I),
        })
    return rows


def summarize(rows, N, n_pieces):
    nV = Counter(len(r["V"]) for r in rows)
    nI = Counter(len(r["I"]) for r in rows)

    n_pts = len(rows)

    print(f"\n=== N = {N}, # AII lattice pts = {n_pts}, # pieces = {n_pieces} ===")

    print(f"\n  Distribution of |V(p)| (# valid pieces per p):")
    for k in sorted(nV):
        print(f"    |V|={k:2d} : {nV[k]:6d} pts   ({100*nV[k]/n_pts:5.2f}%)")
    print(f"    mean |V| = {sum(len(r['V']) for r in rows)/n_pts:.3f}")
    print(f"    max  |V| = {max(nV)}")
    print(f"    min  |V| = {min(nV)}")

    print(f"\n  Distribution of |I(p)| (# distinct images per p):")
    for k in sorted(nI):
        print(f"    |I|={k:2d} : {nI[k]:6d} pts   ({100*nI[k]/n_pts:5.2f}%)")
    print(f"    mean |I| = {sum(len(r['I']) for r in rows)/n_pts:.3f}")
    print(f"    max  |I| = {max(nI)}")
    print(f"    min  |I| = {min(nI)}")

    n_genuine_multi = sum(1 for r in rows if len(r["I"]) > 1)
    print(f"\n  AII pts with |I(p)| > 1 (genuine multivaluedness): {n_genuine_multi}/{n_pts} ({100*n_genuine_multi/n_pts:.2f}%)")

    if n_genuine_multi == 0:
        verdict = "CANDIDATE A (redundancy stack): all valid pieces agree on the image."
    else:
        verdict = "CANDIDATE B (genuine multivaluedness): different pieces give different images at the same p."
    print(f"\n  VERDICT: {verdict}")

    return {
        "N": N,
        "n_pts": n_pts,
        "n_pieces": n_pieces,
        "dist_V": dict(nV),
        "dist_I": dict(nI),
        "n_genuine_multi": n_genuine_multi,
        "verdict": verdict,
    }


def find_wall_points(rows, N):
    """A 'wall point' is an AII point p where |V(p)| differs from a neighbour
    (one unit shift). Report a few examples."""
    by_p = {tuple(r["p"][k] for k in sorted(r["p"])): r for r in rows}
    # Use a simpler shape: keyed by tuple of values in fixed order
    KEYS = ["m_2", "m_23", "m_236", "m_23456", "m_12356", "m_12346",
            "m_2345", "m_1235", "m_1234"]
    by_tuple = {}
    for r in rows:
        key = tuple(r["p"][k] for k in KEYS)
        by_tuple[key] = (len(r["V"]), len(r["I"]))

    walls = []
    for key, (nV, nI) in by_tuple.items():
        # check 1-step neighbours along +e_k
        for k in range(9):
            nb = list(key)
            nb[k] -= 1
            if nb[k] < 0:
                continue
            nb = tuple(nb)
            if nb in by_tuple:
                nV2, nI2 = by_tuple[nb]
                if nV2 != nV or nI2 != nI:
                    walls.append({
                        "p": dict(zip(KEYS, key)),
                        "neighbour": dict(zip(KEYS, nb)),
                        "shift_dir": KEYS[k],
                        "nV_at_p": nV, "nI_at_p": nI,
                        "nV_at_nb": nV2, "nI_at_nb": nI2,
                    })
        if len(walls) >= 50:
            break
    return walls


def main():
    pieces = [name for name in MIN_COVER_26 if name in ALL_PI]
    missing = [name for name in MIN_COVER_26 if name not in ALL_PI]
    print(f"# pieces in MIN_COVER_26: {len(MIN_COVER_26)}")
    print(f"# pieces resolved in ALL_PI: {len(pieces)}")
    if missing:
        print(f"# missing: {missing}")

    out = {}
    for N in [4, 5, 6, 7, 8]:
        rows = compute_VI(N, pieces)
        summary = summarize(rows, N, len(pieces))
        out[f"N={N}"] = summary

        if N == 6:
            walls = find_wall_points(rows, N)
            print(f"\n  # walls (1-step shifts where (nV,nI) changes): {len(walls)} (showing 3)")
            for w in walls[:3]:
                print(f"    p={w['p']}")
                print(f"      shift -{w['shift_dir']} -> neighbour with (nV,nI)=({w['nV_at_nb']},{w['nI_at_nb']}); p has ({w['nV_at_p']},{w['nI_at_p']})")
            out[f"N={N}_walls_sample"] = walls[:10]

    out_path = Path(__file__).parent / "fiber_strat_result.json"
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2, default=str)
    print(f"\nWrote {out_path}")


if __name__ == "__main__":
    main()

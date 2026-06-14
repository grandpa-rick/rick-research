"""Sanity check: run the general scaffold at n=5 and confirm # AXIS = 3."""
from general_axis import (aii_struct, enumerate_aii_lattice,
                          piece_matrix, verify_piece, analyze_axis)
from general_pieces import build_registry


def main():
    n = 5
    s = aii_struct(n)
    pts = enumerate_aii_lattice(s, 5)
    print(f"n={n}: enumerated {len(pts)} AII feasible lattice pts at sum<=5")

    registry = build_registry(n)
    print(f"n={n}: {len(registry)} candidate pieces in registry")

    feasible = {}
    infeasible = {}
    for name, spec in registry.items():
        M = piece_matrix(spec, s)
        bad = verify_piece(M, s, pts)
        if bad:
            infeasible[name] = (M, bad)
        else:
            feasible[name] = M

    print(f"feasible: {len(feasible)}/{len(registry)}")
    print(f"infeasible: {len(infeasible)}")
    for nm, (M, bad) in list(infeasible.items())[:10]:
        p, q = bad[0]
        print(f"  ✗ {nm}: first fail p={p}, q={q}")

    res = analyze_axis(feasible, s, label=f"n={n} general scaffold")
    print(f"\n# AXIS = {res['n_axis']}")
    print(f"AXIS = {res['axis_by_walls']}")
    print(f"\nColumn counts:")
    for av in s["vars"]:
        cc = res["col_counts"][av]
        role = "RIGID" if cc == 1 else ("BINARY" if cc == 2 else "AXIS-cand")
        print(f"  {av:<14}  cols={cc:>3}  {role}")
    print(f"\nRank distribution: {res['rank_distribution']}")


if __name__ == "__main__":
    main()

"""
Day 70 CODE Task A — # AXIS count at n=7.

n=7 is ODD (no Cor 8 linking equation), with s_n = s_7 the Singleton var.

Working hypothesis: # AXIS(7) = 3 with AXIS = {prefix[1], prefix[7], long[1]}.
Falsification: # AXIS >= 4 refutes Lemma D as posed.
"""
import json
import time
from pathlib import Path

from general_axis import (aii_struct, bdi_vars, enumerate_aii_lattice,
                          piece_matrix, verify_piece, analyze_axis)
from general_pieces import build_registry


def main():
    n = 7
    N_max = 7
    s = aii_struct(n)
    print("=" * 72)
    print(f"  n = {n} (ODD)  # AXIS analysis")
    print("=" * 72)
    print(f"AII vars ({s['n_vars']}): {s['vars']}")
    print(f"BDI vars ({len(bdi_vars(n))}): {bdi_vars(n)}")

    t0 = time.time()
    pts = enumerate_aii_lattice(s, N_max)
    print(f"Enumerated {len(pts)} AII feasible lattice pts at sum<={N_max}"
          f" in {time.time()-t0:.2f}s")

    registry = build_registry(n)
    print(f"Candidate pieces: {len(registry)}")

    feasible = {}
    infeasible = {}
    for name, spec in registry.items():
        M = piece_matrix(spec, s)
        bad = verify_piece(M, s, pts)
        if bad:
            infeasible[name] = (M, bad)
        else:
            feasible[name] = M

    print(f"\nFeasible: {len(feasible)}/{len(registry)}")
    print(f"Infeasible: {len(infeasible)}")
    if infeasible:
        for nm, (M, bad) in list(infeasible.items())[:20]:
            p, q = bad[0]
            nz_p = {s['vars'][i]: p[i] for i in range(len(p)) if p[i] != 0}
            print(f"  ✗ {nm}: first fail p={nz_p}, q={q}")

    # R-double feasibility breakdown
    print(f"\nR-double pieces:")
    for nm in sorted(registry):
        if nm.startswith("Rdouble"):
            status = "FEASIBLE" if nm in feasible else "INFEASIBLE"
            print(f"  {nm}: {status}")

    # Run analysis
    res_full = analyze_axis(feasible, s, label=f"n={n} FULL registry")

    feasible_no_rd = {nm: M for nm, M in feasible.items()
                      if not nm.startswith("Rdouble")}
    res_no_rd = analyze_axis(feasible_no_rd, s,
                              label=f"n={n} R-double REMOVED")

    print(f"\n{'=' * 60}")
    print(f"  RESULTS at n={n}")
    print(f"{'=' * 60}")
    print(f"FULL # AXIS = {res_full['n_axis']}: {res_full['axis_by_walls']}")
    print(f"NO-RD # AXIS = {res_no_rd['n_axis']}: {res_no_rd['axis_by_walls']}")

    print(f"\nColumn counts (FULL registry):")
    for av in s["vars"]:
        cc = res_full["col_counts"][av]
        role = ("RIGID" if cc == 1
                else ("BINARY" if cc == 2
                      else f"AXIS-cand ({cc} cols)"))
        print(f"  {av:<14}  cols={cc:>3}  {role}")

    print(f"\nRank distribution: {res_full['rank_distribution']}")
    print(f"\nAXIS pair counts (FULL):")
    for av, cnt in res_full["axis_pair_counts"].items():
        print(f"  {av}: {cnt} pair-collisions")

    print(f"\nTop rank-1 walls:")
    for w in res_full["rank1_walls_summary"][:10]:
        coords = w["wall_coords"]
        desc = " + ".join(f"{c}·{v}" for v, c in coords)
        marker = "  [COORD]" if len(coords) == 1 else ""
        print(f"  {{{desc} = 0}}: {w['n_pair_collisions']} pairs{marker}")

    # Verdict
    print(f"\n{'=' * 60}")
    print(f"  VERDICT at n=7")
    print(f"{'=' * 60}")
    if res_full["n_axis"] == 3:
        verdict = (f"CONFIRMED: # AXIS(7) = 3, AXIS = "
                   f"{res_full['axis_by_walls']}. Lemma D upper bound has "
                   f"empirical support at n=7.")
    else:
        verdict = (f"REFUTED: # AXIS(7) = {res_full['n_axis']} != 3. "
                   f"Lemma D needs re-derivation.")
    print(verdict)

    out_dir = Path(__file__).parent
    save_data = {
        "n": n,
        "N_max_lattice": N_max,
        "n_lattice_pts": len(pts),
        "n_candidate_pieces": len(registry),
        "n_feasible_pieces": len(feasible),
        "n_infeasible_pieces": len(infeasible),
        "feasible_names": sorted(feasible.keys()),
        "infeasible_names": sorted(infeasible.keys()),
        "full_analysis": res_full,
        "no_rd_analysis": res_no_rd,
        "verdict": verdict,
    }
    with open(out_dir / "n7_results.json", "w") as f:
        json.dump(save_data, f, indent=2, default=str)
    print(f"\nsaved: {out_dir/'n7_results.json'}")

    aii_v = s["vars"]
    bv = bdi_vars(n)
    n_bdi = len(bv)
    n_aii = s["n_vars"]
    registry_json = {}
    for name, M in feasible.items():
        registry_json[name] = {aii_v[c]: [int(M[r, c]) for r in range(n_bdi)]
                                for c in range(n_aii)}
    with open(out_dir / "n7_registry.json", "w") as f:
        json.dump(registry_json, f, indent=2)
    print(f"saved: {out_dir/'n7_registry.json'}")


if __name__ == "__main__":
    main()

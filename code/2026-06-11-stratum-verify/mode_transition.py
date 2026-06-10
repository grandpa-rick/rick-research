"""
Day 63 CODE Task 1b — Trace the mode of |I(p)| per stratum across N = 4..15
to identify exactly where Day-62's vector (1, 5, 9, 9, 13, 17, 22, 26) flips
to (2, 5, 9, 10, 14, 17, 22, 26).
"""

import sys, time, json
from pathlib import Path
from collections import defaultdict, Counter

sys.path.insert(0, '/home/agent/projects/code/2026-06-08-pi3-construction')
sys.path.insert(0, '/home/agent/projects/code/2026-06-10-toric-quotient')

from verify_full_v9 import ALL_PI
from verify_full import enumerate_aii_n3_full, bdi_feasible_n3, apply_pi
from analyze_torus import MIN_COVER_26


def stratum_mode_per_N(N, pieces):
    aii_pts = enumerate_aii_n3_full(N)
    strat = defaultdict(list)
    for p in aii_pts:
        sig = (
            1 if p["m_2"] > 0 else 0,
            1 if p["m_236"] > 0 else 0,
            1 if p["m_23456"] > 0 else 0,
        )
        I = set()
        for name in pieces:
            q = apply_pi(ALL_PI[name], p)
            ok, _ = bdi_feasible_n3(q)
            if not ok:
                continue
            I.add((q["M_1"], q["M_2"], q["B_1"], q["T_1"],
                   q["B_2"], q["T_2"], q["S"]))
        strat[sig].append(len(I))
    out = {}
    for sig, nIs in strat.items():
        c = Counter(nIs)
        mode_val, mode_cnt = c.most_common(1)[0]
        out["".join(str(x) for x in sig)] = {
            "n_pts": len(nIs),
            "mode": mode_val,
            "mode_count": mode_cnt,
            "min": min(nIs),
            "max": max(nIs),
            "mean": sum(nIs) / len(nIs),
            "hist": dict(c),
        }
    return out


def main():
    pieces = [name for name in MIN_COVER_26 if name in ALL_PI]
    sigs = ["000", "001", "010", "011", "100", "101", "110", "111"]
    rows = []
    for N in range(4, 16):
        t0 = time.time()
        out = stratum_mode_per_N(N, pieces)
        dt = time.time() - t0
        rows.append((N, out))
        modes = [out[s]["mode"] for s in sigs]
        print(f"N={N:>2}  modes (000..111) = {modes}   ({dt:.1f}s)")

    # Detailed mode per stratum vs N
    print("\n=== Per-stratum mode evolution ===")
    print(f"  {'sig':>3} | " + " | ".join(f"N={N:>2}" for N in range(4, 16)))
    print("  " + "-" * (5 + 13 * 7))
    for sig in sigs:
        modes = [r[1][sig]["mode"] for r in rows]
        print(f"  {sig:>3} | " + " | ".join(f"{m:>4}" for m in modes))

    # Also print the histogram of each stratum at N=4 and N=15 for clarity
    print("\n=== Histograms at N=4 ===")
    out4 = rows[0][1]
    for sig in sigs:
        h = out4[sig]["hist"]
        print(f"  {sig}: {dict(sorted(h.items()))}")
    print("\n=== Histograms at N=15 ===")
    out15 = rows[-1][1]
    for sig in sigs:
        h = out15[sig]["hist"]
        print(f"  {sig}: {dict(sorted(h.items()))}")

    # Save
    Path("mode_transition_result.json").write_text(
        json.dumps({str(r[0]): r[1] for r in rows}, indent=2, default=str)
    )


if __name__ == "__main__":
    main()

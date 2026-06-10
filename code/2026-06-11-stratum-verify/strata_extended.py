"""
Day 63 CODE Task 1 — Extend stratification to N = 12, 13, 14, 15.

Question: does the Day-62 stratum-vector
    I = (1, 5, 9, 9, 13, 17, 22, 26)
hold as the MODE of |I(p)| within each of the 8 sign-pattern strata
(sigma = (m_2>0, m_236>0, m_23456>0))?

The expected ordering (ascending by mode) is:
    (000) -> 1     (no axes positive)
    (100) -> 5
    (001) -> 9
    (010) -> 9
    (101) -> 13
    (110) -> 17
    (011) -> 22
    (111) -> 26    (interior stratum)

For each N in {12, 13, 14, 15} compute, per stratum:
    # lattice points, mean |I|, mode |I|, max |I|, variance |I|.

If the mode 8-tuple stays constant in N, the stratum-vector is the
asymptotic invariant of pi3' (genuine multivaluedness fingerprint).
"""

import sys, time, json
from pathlib import Path
from collections import defaultdict, Counter

sys.path.insert(0, '/home/agent/projects/code/2026-06-08-pi3-construction')
sys.path.insert(0, '/home/agent/projects/code/2026-06-10-toric-quotient')

from verify_full_v9 import ALL_PI
from verify_full import enumerate_aii_n3_full, bdi_feasible_n3, apply_pi
from analyze_torus import MIN_COVER_26


OUT_DIR = Path(__file__).parent


SIG_NAMES = [
    "000 (m_2=m_236=m_23456=0)",
    "001 (m_23456 only)",
    "010 (m_236 only)",
    "011 (m_236, m_23456)",
    "100 (m_2 only)",
    "101 (m_2, m_23456)",
    "110 (m_2, m_236)",
    "111 (interior: all three > 0)",
]


def stratum_stats(N, pieces):
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
    # Reduce per sig
    out = {}
    for sig, nIs in strat.items():
        n = len(nIs)
        mu = sum(nIs) / n
        var = sum((x - mu) ** 2 for x in nIs) / n
        c = Counter(nIs)
        mode_val, mode_cnt = c.most_common(1)[0]
        out[sig] = {
            "n_pts": n,
            "mean": mu,
            "var": var,
            "mode": mode_val,
            "mode_count": mode_cnt,
            "min": min(nIs),
            "max": max(nIs),
            "hist": dict(c),
        }
    return out


def fmt_sig(sig):
    return "".join(str(s) for s in sig)


def main():
    pieces = [name for name in MIN_COVER_26 if name in ALL_PI]
    print(f"# pieces = {len(pieces)}")

    all_data = {}
    for N in [12, 13, 14, 15]:
        t0 = time.time()
        stats = stratum_stats(N, pieces)
        dt = time.time() - t0
        print(f"\n=== N = {N} ===   ({dt:.1f}s, {sum(s['n_pts'] for s in stats.values())} pts)")
        print(f"{'sigma':>5} | {'# pts':>6} | {'mean':>7} | {'mode':>4}({'cnt':>5}) | {'min':>3} | {'max':>3} | {'var':>6}")
        print("-" * 70)
        # Save under stringified sig key
        all_data[str(N)] = {}
        for sig in sorted(stats):
            s = stats[sig]
            print(f"  {fmt_sig(sig):>3} | {s['n_pts']:>6} | {s['mean']:>7.3f} | {s['mode']:>4}({s['mode_count']:>5}) | {s['min']:>3} | {s['max']:>3} | {s['var']:>6.3f}")
            all_data[str(N)][fmt_sig(sig)] = s

    out_json = OUT_DIR / "strata_extended_result.json"
    out_json.write_text(json.dumps(all_data, indent=2, default=str))
    print(f"\nWrote {out_json}")

    # Mode constancy check across N
    print("\n\n=== MODE CONSTANCY across N = 12, 13, 14, 15 ===")
    print(f"{'sigma':>3} | {'N=12':>4} | {'N=13':>4} | {'N=14':>4} | {'N=15':>4} | constant?")
    print("-" * 50)
    sigs = sorted(all_data["12"])
    for sig in sigs:
        modes = [all_data[str(N)][sig]["mode"] for N in [12, 13, 14, 15]]
        ok = len(set(modes)) == 1
        flag = "YES" if ok else f"NO ({modes})"
        print(f" {sig:>3} | {modes[0]:>4} | {modes[1]:>4} | {modes[2]:>4} | {modes[3]:>4} | {flag}")

    # Mode 8-tuple as multiset
    print("\nMode multiset per N (sorted):")
    for N in [12, 13, 14, 15]:
        vec = sorted(all_data[str(N)][s]["mode"] for s in sigs)
        print(f"  N={N}: {tuple(vec)}")

    expected = (1, 5, 9, 9, 13, 17, 22, 26)
    print(f"\nDay-62 expectation: {expected}")


if __name__ == "__main__":
    main()

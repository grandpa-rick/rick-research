"""
Day 66 PROVE Phase 1 — Why exactly 3?

Test whether α = 3, 4, ... m_2 in S would still be BDI-feasible in the R-double
backbone.  This pins down the "3 = max α + 1 = 3" combinatorial cap.
"""
import sys
sys.path.insert(0, '/home/agent/projects/code/2026-06-08-pi3-construction')

from verify_full import (enumerate_aii_n3_full, bdi_feasible_n3,
                          enumerate_bdi_n3, apply_pi)

# R-double backbone with arbitrary α m_2 in S
def make_r_double(alpha):
    return {
        "M_1": [], "M_2": [(1, "m_12356")],
        "B_1": [(1, "m_2"), (2, "m_2345"), (1, "m_23456")],
        "T_1": [(1, "m_2345"), (1, "m_23456")],
        "B_2": [(1, "m_23"), (1, "m_1235"), (1, "m_236")],
        "T_2": [(1, "m_1235"), (1, "m_236")],
        "S":   [(1, "m_12346"), (2, "m_1234"), (2, "m_2345"), (alpha, "m_2")],
    }

print("=== Test feasibility of R-double backbone with α m_2 in S ===")
for alpha in [0, 1, 2, 3, 4]:
    spec = make_r_double(alpha)
    aii_pts = enumerate_aii_n3_full(7)
    bad = 0
    n_total = len(aii_pts)
    image = set()
    for p in aii_pts:
        q = apply_pi(spec, p)
        ok, reason = bdi_feasible_n3(q)
        if not ok:
            bad += 1
        else:
            image.add((q["M_1"], q["M_2"], q["B_1"], q["T_1"],
                       q["B_2"], q["T_2"], q["S"]))
    pct = 100.0 * (n_total - bad) / n_total if n_total else 0
    print(f"  α={alpha}: lands {n_total-bad}/{n_total} ({pct:.1f}%), image size {len(image)}")

print()
print("=== Interpretation ===")
print("If α=3 has substantial land-in-cone failure, the BDI feasibility caps α≤2.")
print("That fixes the 'why 3' at n=3:  |{0, 1, 2}| = 3 = max-feasible α + 1.")

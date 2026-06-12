"""
Day 66 PROVE Phase 1 — extract the Bucket-0 and Bucket-1 (m_2, m_236, m_23456)
columns from the 26-piece registry, verify the (M_2, S)-chain claim, and prepare
for the rep-theoretic identification.
"""
import sys, json
from pathlib import Path
sys.path.insert(0, '/home/agent/projects/code/2026-06-08-pi3-construction')
sys.path.insert(0, '/home/agent/projects/code/2026-06-10-toric-quotient')

from verify_full_v9 import ALL_PI
from analyze_torus import MIN_COVER_26

BDI_ORDER = ["M_1", "M_2", "B_1", "T_1", "B_2", "T_2", "S"]

def piece_column(spec, aii_var):
    col = [0]*7
    for i, bdi in enumerate(BDI_ORDER):
        for (coef, av) in spec.get(bdi, []):
            if av == aii_var:
                col[i] += coef
    return tuple(col)

BUCKET0 = ["R_double_m2345", "P7_Rdouble_m2_dbl_S", "P5d_Rdouble_plus_m2"]
BUCKET1 = ["M2_is_m236"]

print("=== Registry size ===")
print(f"Registry pieces: {len(MIN_COVER_26)}")
print(f"ALL_PI pieces:   {len(ALL_PI)}")

# Sanity: B0 and B1 names are in registry?
for n in BUCKET0 + BUCKET1:
    assert n in ALL_PI, f"{n} missing from ALL_PI"
    assert n in MIN_COVER_26, f"{n} missing from MIN_COVER_26"

print("\n=== Bucket-0: 3 R-double pieces ===")
B0_data = []
for n in BUCKET0:
    spec = ALL_PI[n]
    c_m2     = piece_column(spec, "m_2")
    c_m236   = piece_column(spec, "m_236")
    c_m23456 = piece_column(spec, "m_23456")
    M2 = c_m2[1]; S = c_m2[6]
    print(f"\n  {n}")
    print(f"    c_m2     = {c_m2}    (M_2-entry = {M2},  S-entry = {S})")
    print(f"    c_m236   = {c_m236}")
    print(f"    c_m23456 = {c_m23456}")
    B0_data.append({
        "name": n, "c_m2": c_m2, "c_m236": c_m236, "c_m23456": c_m23456,
        "M2_S": (M2, S),
    })

# Verify all share m_236 and m_23456
shared_m236  = set(d["c_m236"]   for d in B0_data)
shared_m23456 = set(d["c_m23456"] for d in B0_data)
print(f"\nShared c_m236 across B0:   {len(shared_m236)} distinct (expect 1)")
print(f"Shared c_m23456 across B0: {len(shared_m23456)} distinct (expect 1)")
assert len(shared_m236) == 1 and len(shared_m23456) == 1

# (M_2, S) sequence
M2S = sorted([d["M2_S"] for d in B0_data])
print(f"\n(M_2, S) values in B0: {M2S}")

print("\n=== Bucket-1: M2_is_m236 ===")
for n in BUCKET1:
    spec = ALL_PI[n]
    c_m2     = piece_column(spec, "m_2")
    c_m236   = piece_column(spec, "m_236")
    c_m23456 = piece_column(spec, "m_23456")
    print(f"\n  {n}")
    print(f"    c_m2     = {c_m2}")
    print(f"    c_m236   = {c_m236}   (this piece has M_2 sourced from m_236)")
    print(f"    c_m23456 = {c_m23456}")

# Now compare B0's m_236 column with the B2 m_236 columns
print("\n=== Comparison: B0 c_m236 vs Bucket-2 c_m236 list ===")
print("From Day-64: B0 c_m236 is (0,0,0,0,1,1,0) which is i_236=0 in B2's labelling")
print("(i.e., B_2 + T_2 with no M_2 contribution)")

# Save
out = {"bucket0": B0_data, "bucket1": [{"name": n,
                                        "c_m2": piece_column(ALL_PI[n], "m_2"),
                                        "c_m236": piece_column(ALL_PI[n], "m_236"),
                                        "c_m23456": piece_column(ALL_PI[n], "m_23456")}
                                       for n in BUCKET1]}
with open(Path(__file__).parent / "b01_columns.json", "w") as f:
    json.dump(out, f, default=list, indent=2)
print(f"\nSaved b01_columns.json")

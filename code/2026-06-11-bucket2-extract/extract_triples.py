"""
Day 64 PROVE Step 1.

Extract the 22 (m_2 column, m_236 column, m_23456 column) triples for the
Bucket-2 generic pieces, where "column" of an AII variable v in piece i =
the 7-vector (M_1, M_2, B_1, T_1, B_2, T_2, S) coefficient of v in piece i.

Then:
  - print the 22 triples
  - check the marginals (4, 9, 8)
  - check the projection π_{m_236, m_23456} has 21 unique images (1 fibre size 2)
  - save to JSON for later root-system matching

Output: bucket2_triples.json
"""

import sys, json
from pathlib import Path
from collections import Counter, defaultdict

sys.path.insert(0, '/home/agent/projects/code/2026-06-08-pi3-construction')
sys.path.insert(0, '/home/agent/projects/code/2026-06-10-toric-quotient')

from verify_full_v9 import ALL_PI
from analyze_torus import MIN_COVER_26

OUT_DIR = Path(__file__).parent

BDI_ORDER = ["M_1", "M_2", "B_1", "T_1", "B_2", "T_2", "S"]


def piece_column(spec, aii_var):
    """Return tuple of length 7 with coefficient of aii_var in each BDI row."""
    col = [0]*7
    for i, bdi in enumerate(BDI_ORDER):
        for (coef, av) in spec.get(bdi, []):
            if av == aii_var:
                col[i] += coef
    return tuple(col)


def main():
    pieces = [n for n in MIN_COVER_26 if n in ALL_PI]
    print(f"# pieces in registry: {len(pieces)}")

    # Get 22 Bucket-2 piece names. We follow Day-63 §3 directly:
    # bucket assignment by non-axis equivalence class.
    # The 4 special pieces (Buckets 0 and 1) are:
    bucket01_names = {
        "R_double_m2345",          # Bucket 0
        "P7_Rdouble_m2_dbl_S",     # Bucket 0
        "P5d_Rdouble_plus_m2",     # Bucket 0
        "M2_is_m236",              # Bucket 1
    }
    b2_names = [n for n in pieces if n not in bucket01_names]
    print(f"# Bucket-2 pieces: {len(b2_names)} (expected 22)")
    assert len(b2_names) == 22

    # Sanity-check the bucket decomposition: the non-axis profile of every
    # bucket-2 piece must agree on non-axis columns (it's the "generic" class).
    # We'll just extract triples; the bucket decomposition is proven elsewhere.

    # Build triples
    triples = []
    for name in b2_names:
        spec = ALL_PI[name]
        c2 = piece_column(spec, "m_2")
        c236 = piece_column(spec, "m_236")
        c23456 = piece_column(spec, "m_23456")
        triples.append({"name": name, "c_m2": c2, "c_m236": c236, "c_m23456": c23456})

    # Marginals
    c2s = sorted({t["c_m2"] for t in triples})
    c236s = sorted({t["c_m236"] for t in triples})
    c23456s = sorted({t["c_m23456"] for t in triples})
    print(f"\nDistinct m_2 columns:    {len(c2s)} (expected 4)")
    for c in c2s:    print(f"  {c}")
    print(f"\nDistinct m_236 columns:  {len(c236s)} (expected 9)")
    for c in c236s:  print(f"  {c}")
    print(f"\nDistinct m_23456 columns:{len(c23456s)} (expected 8)")
    for c in c23456s:print(f"  {c}")

    # Distinct full triples
    full = {(t["c_m2"], t["c_m236"], t["c_m23456"]) for t in triples}
    print(f"\nDistinct full triples: {len(full)} (expected 22)")

    # Project onto (m_236, m_23456) — almost-injective?
    proj = defaultdict(list)
    for t in triples:
        proj[(t["c_m236"], t["c_m23456"])].append(t["name"])
    nonsing = [k for k, v in proj.items() if len(v) == 1]
    multi = [(k, v) for k, v in proj.items() if len(v) > 1]
    print(f"\nπ_(m_236, m_23456): {len(proj)} distinct (expected 21)")
    print(f"  singletons:    {len(nonsing)}")
    print(f"  multi-fibres:  {len(multi)}")
    for k, v in multi:
        print(f"    fibre: m_236={k[0]}, m_23456={k[1]} → {v}")

    # Save JSON
    out = {
        "bucket2_pieces": [t["name"] for t in triples],
        "triples": [
            {"name": t["name"],
             "c_m2":     list(t["c_m2"]),
             "c_m236":   list(t["c_m236"]),
             "c_m23456": list(t["c_m23456"])}
            for t in triples
        ],
        "bdi_order": BDI_ORDER,
        "marginals": {"m_2": len(c2s), "m_236": len(c236s), "m_23456": len(c23456s)},
        "distinct_triples": len(full),
        "proj_236_23456_distinct": len(proj),
    }
    with open(OUT_DIR / "bucket2_triples.json", "w") as f:
        json.dump(out, f, indent=2)
    print(f"\nSaved {OUT_DIR / 'bucket2_triples.json'}")

    # Also save canonical indexing: for each piece, the (m_2_idx, m_236_idx, m_23456_idx) integers
    c2_idx = {c: i for i, c in enumerate(c2s)}
    c236_idx = {c: i for i, c in enumerate(c236s)}
    c23456_idx = {c: i for i, c in enumerate(c23456s)}
    indexing = []
    for t in triples:
        indexing.append({
            "name": t["name"],
            "i2": c2_idx[t["c_m2"]],
            "i236": c236_idx[t["c_m236"]],
            "i23456": c23456_idx[t["c_m23456"]],
        })
    out2 = {
        "indexing": indexing,
        "c2_list": [list(c) for c in c2s],
        "c236_list": [list(c) for c in c236s],
        "c23456_list": [list(c) for c in c23456s],
    }
    with open(OUT_DIR / "bucket2_indexing.json", "w") as f:
        json.dump(out2, f, indent=2)
    print(f"Saved {OUT_DIR / 'bucket2_indexing.json'}")

    print("\nIndex table (piece, i2 ∈ [4], i236 ∈ [9], i23456 ∈ [8]):")
    for idx in indexing:
        print(f"  {idx['i2']} {idx['i236']:>2} {idx['i23456']:>2}  | {idx['name']}")


if __name__ == "__main__":
    main()

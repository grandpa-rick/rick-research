"""
Day 62 — Probe structure of I(p) and identify which piece fails when |V|=25.

Questions:
1. When |V(p)| = 25, which piece is infeasible? (Always the same one?)
2. What does I(p) look like at points with small/large |I(p)|?
3. Find a concrete "wall point" with witness piece i for which p, q image
   differ from neighbour.
"""

import sys
sys.path.insert(0, '/home/agent/projects/code/2026-06-08-pi3-construction')
sys.path.insert(0, '/home/agent/projects/code/2026-06-10-toric-quotient')

from collections import Counter, defaultdict

from verify_full_v9 import ALL_PI
from verify_full import enumerate_aii_n3_full, bdi_feasible_n3, apply_pi
from analyze_torus import MIN_COVER_26


def piece_image(spec, p):
    q = apply_pi(spec, p)
    ok, reason = bdi_feasible_n3(q)
    if not ok:
        return None, reason
    return (q["M_1"], q["M_2"], q["B_1"], q["T_1"], q["B_2"], q["T_2"], q["S"]), None


def main():
    pieces = [name for name in MIN_COVER_26 if name in ALL_PI]
    N = 8
    aii_pts = enumerate_aii_n3_full(N)

    print(f"# AII pts at N={N}: {len(aii_pts)}")

    # 1. Which piece(s) fail when |V|=25?
    fail_counter = Counter()
    fail_reason_counter = Counter()
    invalid_total = 0
    for p in aii_pts:
        valid = []
        for i, name in enumerate(pieces):
            q, reason = piece_image(ALL_PI[name], p)
            if q is None:
                fail_counter[name] += 1
                fail_reason_counter[reason] += 1
                invalid_total += 1
                if len(valid) == 0:  # only record first infeasibility detail later
                    pass
            else:
                valid.append(i)

    print(f"\nTotal (p, piece) infeasibilities: {invalid_total}")
    print(f"\nWhich pieces fail (and how often):")
    for name, c in fail_counter.most_common():
        print(f"  {c:6d} x {name}")
    print(f"\nFailure reasons:")
    for r, c in fail_reason_counter.most_common():
        print(f"  {c:6d} x {r}")

    # 2. Distribution of multiplicities INSIDE I(p): how many pieces hit
    #    each image at a given p?
    print("\n--- Multiplicity within I(p) for max-|I| points ---")
    max_I_pts = []
    for p in aii_pts:
        I_count = Counter()
        for i, name in enumerate(pieces):
            q, _ = piece_image(ALL_PI[name], p)
            if q is not None:
                I_count[q] += 1
        if len(I_count) >= 26:
            max_I_pts.append((p, I_count))
    print(f"# AII pts with |I| >= 26: {len(max_I_pts)}")
    if max_I_pts:
        p, I_count = max_I_pts[0]
        print(f"  Example p: {p}")
        for q, m in sorted(I_count.items()):
            print(f"    image {q}  mult={m}")

    # 3. |I| = 1 case: when do all 26 pieces agree?
    print("\n--- |I| = 1 points (all pieces agree on image) ---")
    iso_pts = []
    for p in aii_pts:
        images = set()
        for i, name in enumerate(pieces):
            q, _ = piece_image(ALL_PI[name], p)
            if q is not None:
                images.add(q)
        if len(images) == 1:
            iso_pts.append((p, next(iter(images))))
    print(f"# AII pts with |I|=1: {len(iso_pts)}")
    for p, q in iso_pts[:5]:
        nonzero = {k: v for k, v in p.items() if v != 0}
        print(f"  p={nonzero}, image={q}")

    # 4. Explicit wall point — find p where neighbour shifts (nV, nI)
    #    significantly, and show which pieces matter.
    print("\n--- Explicit wall point analysis ---")
    KEYS = ["m_2", "m_23", "m_236", "m_23456", "m_12356", "m_12346",
            "m_2345", "m_1235", "m_1234"]

    def imgs_per_piece(p):
        return [piece_image(ALL_PI[name], p)[0] for name in pieces]

    # Look at p = (m_23456=2) versus p = (m_23456=1)
    p_keys = ["m_2", "m_23", "m_236", "m_23456", "m_12356", "m_12346",
              "m_2345", "m_1235", "m_1234"]
    p0 = dict.fromkeys(p_keys, 0); p0["m_23456"] = 1
    p1 = dict.fromkeys(p_keys, 0); p1["m_23456"] = 2

    imgs0 = imgs_per_piece(p0)
    imgs1 = imgs_per_piece(p1)
    valid0 = set(q for q in imgs0 if q is not None)
    valid1 = set(q for q in imgs1 if q is not None)
    print(f"  p_a = m_23456=1: |V|={sum(1 for q in imgs0 if q is not None)}, |I|={len(valid0)}")
    print(f"    images: {sorted(valid0)}")
    print(f"  p_b = m_23456=2: |V|={sum(1 for q in imgs1 if q is not None)}, |I|={len(valid1)}")
    print(f"    images: {sorted(valid1)}")

    # And p = (m_236=1, m_23456=1) which had (nV,nI)=(25,21)
    p2 = dict.fromkeys(p_keys, 0); p2["m_236"] = 1; p2["m_23456"] = 1
    imgs2 = imgs_per_piece(p2)
    valid2 = set(q for q in imgs2 if q is not None)
    print(f"\n  p_c = m_236=1 + m_23456=1: |V|={sum(1 for q in imgs2 if q is not None)}, |I|={len(valid2)}")
    print(f"    distinct images: {len(valid2)}")
    # Group by image
    img_to_pieces = defaultdict(list)
    for name, q in zip(pieces, imgs2):
        if q is not None:
            img_to_pieces[q].append(name)
    print(f"    image -> pieces giving it:")
    for q, names in sorted(img_to_pieces.items()):
        print(f"      {q}: {names}")


if __name__ == "__main__":
    main()

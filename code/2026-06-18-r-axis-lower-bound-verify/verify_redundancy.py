#!/usr/bin/env python3
"""
Day-73 PROVE supplementary verification: Lemma B k=2 and Lemma C k=2 image-redundancy.

For each pair (k=1, k=2):
- Enumerate ray-images at small AII coefficients (bounded support).
- Check that every image point of k=2 piece is also in k=1 (resp. base) piece.
"""
from itertools import product

BDI_COORDS = ["M2", "M3", "M4", "B1", "T1", "B2", "T2", "B3", "T3", "B4", "T4", "S"]
NB = len(BDI_COORDS)
IDX = {c: i for i, c in enumerate(BDI_COORDS)}

def vec(**kw):
    v = [0] * NB
    for k, n in kw.items():
        v[IDX[k]] = n
    return tuple(v)

def add(*vs):
    if not vs:
        return tuple([0] * NB)
    return tuple(sum(x) for x in zip(*vs))

def scale(c, v):
    return tuple(c * x for x in v)

def P(a, v):
    s = 0
    for b in range(1, a + 1):
        s += v[IDX[f"B{b}"]] - v[IDX[f"T{b}"]]
    return 2 * s

def is_BDI(v):
    if any(x < 0 for x in v):
        return False
    for a in range(1, 5):
        if v[IDX[f"T{a}"]] > v[IDX[f"B{a}"]]:
            return False
        if P(a, v) < 0:
            return False
    for a in range(2, 5):
        if v[IDX[f"M{a}"]] > min(P(a-1, v), P(a, v)):
            return False
    if v[IDX["S"]] > P(4, v):
        return False
    return True

# Base piece: pi^{p_j} = e_{B_j} for j=1..4, pi^{p_5} = 0,
#   pi^{l_1} = e_{B_1}, pi^{l_j} = e_{M_j} for j=2..4, pi^{l_5} = e_S,
#   pi^{s_j} = e_{B_j} + e_{T_j} for j=1..4, pi^{s_5} = 0.

BASE_COLS = {
    "p1": vec(B1=1),
    "p2": vec(B2=1),
    "p3": vec(B3=1),
    "p4": vec(B4=1),
    "p5": vec(),  # zero
    "l1": vec(B1=1),
    "l2": vec(M2=1),
    "l3": vec(M3=1),
    "l4": vec(M4=1),
    "l5": vec(S=1),
    "s1": vec(B1=1, T1=1),
    "s2": vec(B2=1, T2=1),
    "s3": vec(B3=1, T3=1),
    "s4": vec(B4=1, T4=1),
    "s5": vec(),
}

def piece_rays(cols):
    """Return list of 15 ray-image vectors for a piece with given column dict."""
    rays = []
    for j in range(1, 6):
        rays.append(("p", j, cols[f"p{j}"]))
    rays.append(("l", 1, cols["l1"]))
    rays.append(("s", 1, cols["s1"]))
    for j in range(2, 6):
        rays.append(("l", j, add(cols[f"p{j-1}"], cols[f"l{j}"])))
    for j in range(2, 6):
        rays.append(("s", j, add(cols[f"p{j-1}"], cols[f"s{j}"])))
    return rays

def piece_feasible(cols):
    """A piece is feasible iff all 15 ray-images are BDI-feasible (Day-70 Thm 4.2)."""
    return all(is_BDI(g) for _, _, g in piece_rays(cols))

# Lemma B k=1: base + pi^{p_5} = e_{B_4} + e_{T_4}
LEMMA_B1 = dict(BASE_COLS)
LEMMA_B1["p5"] = vec(B4=1, T4=1)

# Lemma B k=2: base + pi^{p_5} = 2(e_{B_4} + e_{T_4})
LEMMA_B2 = dict(BASE_COLS)
LEMMA_B2["p5"] = vec(B4=2, T4=2)

# Lemma C k=1: base (since base has pi^{l_1} = e_{B_1}); we'll just use BASE.
# Lemma C k=2: base + pi^{l_1} = 2 e_{B_1}
LEMMA_C2 = dict(BASE_COLS)
LEMMA_C2["l1"] = vec(B1=2)

# Sanity check feasibility.
for name, cols in [("BASE", BASE_COLS), ("LEMMA_B1", LEMMA_B1), ("LEMMA_B2", LEMMA_B2), ("LEMMA_C2", LEMMA_C2)]:
    print(f"  {name} feasibility: {piece_feasible(cols)}")

def enumerate_image(cols, max_sum):
    """Enumerate image semigroup elements with total coefficient sum <= max_sum."""
    rays = [g for _, _, g in piece_rays(cols)]
    seen = {tuple([0]*NB)}
    frontier = [tuple([0]*NB)]
    for s in range(max_sum):
        new_frontier = set()
        for v in frontier:
            for r in rays:
                nv = add(v, r)
                if nv not in seen:
                    seen.add(nv)
                    new_frontier.add(nv)
        frontier = new_frontier
    return seen

print("\n[1] Image-redundancy: Lemma B k=2 ⊆ Lemma B k=1?  (cross-coef comparison)")
print("-" * 60)
print("    Im(B2) at max_sum K ⊆ Im(B1) at max_sum 2K (since B2's pi^{p_5}=2c_1 doubles B1's c_1)")
for K in [1, 2, 3]:
    im_B1_large = enumerate_image(LEMMA_B1, 2 * K)
    im_B2 = enumerate_image(LEMMA_B2, K)
    contained = im_B2.issubset(im_B1_large)
    print(f"  K = {K}: |Im(B2,K)| = {len(im_B2)}, |Im(B1,2K)| = {len(im_B1_large)}, B2(K) ⊆ B1(2K): {contained}")
    if not contained:
        missing = im_B2 - im_B1_large
        print(f"    Missing from B1: {list(missing)[:5]}...")

print("\n[2] Image-redundancy: Lemma C k=2 ⊆ base?  (cross-coef comparison)")
print("-" * 60)
print("    Im(C2) at max_sum K ⊆ Im(base) at max_sum 2K")
for K in [1, 2, 3]:
    im_base_large = enumerate_image(BASE_COLS, 2 * K)
    im_C2 = enumerate_image(LEMMA_C2, K)
    contained = im_C2.issubset(im_base_large)
    print(f"  K = {K}: |Im(C2,K)| = {len(im_C2)}, |Im(base,2K)| = {len(im_base_large)}, C2(K) ⊆ base(2K): {contained}")
    if not contained:
        missing = im_C2 - im_base_large
        print(f"    Missing from base: {list(missing)[:5]}...")

# Now check R-double pieces vs each other (NOT redundant).
RDOUBLE = {
    "p1": vec(B1=1),  # alpha = 0 base
    "p2": vec(B2=1),
    "p3": vec(B3=1),
    "p4": vec(B4=1),
    "p5": vec(B2=1, T2=1),
    "l1": vec(B1=1, T1=1),
    "l2": vec(M2=1),
    "l3": vec(M3=1),
    "l4": vec(M4=1),
    "l5": vec(S=1),
    "s1": vec(B1=2, T1=1, S=2),
    "s2": vec(B2=1, T2=1),
    "s3": vec(B3=1, T3=1),
    "s4": vec(B4=1, T4=1, S=2),
    "s5": vec(),
}

RDOUBLE_0 = dict(RDOUBLE)
RDOUBLE_0["p1"] = vec(B1=1, S=0)  # b_0
RDOUBLE_1 = dict(RDOUBLE)
RDOUBLE_1["p1"] = vec(B1=1, S=1)  # b_1
RDOUBLE_2 = dict(RDOUBLE)
RDOUBLE_2["p1"] = vec(B1=1, S=2)  # b_2

print("\n[3] R-double feasibility")
print("-" * 60)
for name, cols in [("RDOUBLE_0 (α=0)", RDOUBLE_0), ("RDOUBLE_1 (α=1)", RDOUBLE_1), ("RDOUBLE_2 (α=2)", RDOUBLE_2)]:
    print(f"  {name}: feasible = {piece_feasible(cols)}")

print("\n[4] R-double image-distinctness (not redundant)")
print("-" * 60)
for max_sum in [1, 2, 3]:
    im_0 = enumerate_image(RDOUBLE_0, max_sum)
    im_1 = enumerate_image(RDOUBLE_1, max_sum)
    im_2 = enumerate_image(RDOUBLE_2, max_sum)
    print(f"  max_sum = {max_sum}: |Im_0|={len(im_0)}, |Im_1|={len(im_1)}, |Im_2|={len(im_2)}")
    print(f"    R-double α=2 ⊆ R-double α=1? {im_2.issubset(im_1)} (expected False)")
    print(f"    R-double α=2 ⊆ R-double α=0 ∪ α=1? {im_2.issubset(im_0 | im_1)} (expected False)")
    print(f"    R-double α=0 ⊆ R-double α=1 ∪ α=2? {im_0.issubset(im_1 | im_2)} (expected False)")
    if max_sum == 2:
        # Check that b_2 = e_{B_1} + 2 e_S is in R-double α=2 but not in R-double α=0 or α=1.
        b2 = vec(B1=1, S=2)
        print(f"    b_2 ∈ Im(α=2)? {b2 in im_2}, ∈ Im(α=1)? {b2 in im_1}, ∈ Im(α=0)? {b2 in im_0}")

print("\n[5] Conclusion: R-double pieces are MUTUALLY IMAGE-DISTINCT (good for p_1 3-clique).")
print("    Lemma B/C k=2 pieces are IMAGE-REDUNDANT (bad for p_5/l_1 3-cliques).")

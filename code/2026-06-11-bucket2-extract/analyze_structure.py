"""
Day 64 PROVE Step 2.

Analyze the structural properties of the 22 Bucket-2 triples:

(a) Marginals at each index
(b) Partitions of size 12-6-3-1 (Weyl orbits of B_3/C_3 adj+triv)
(c) Natural decompositions matching dim(adj)=21
(d) Graph adjacencies (share two of three coordinates)
"""
import sys, json
from pathlib import Path
from collections import Counter, defaultdict

OUT_DIR = Path(__file__).parent

data = json.loads((OUT_DIR / "bucket2_indexing.json").read_text())
triples_data = json.loads((OUT_DIR / "bucket2_triples.json").read_text())

indexing = data["indexing"]
c2_list = [tuple(x) for x in data["c2_list"]]
c236_list = [tuple(x) for x in data["c236_list"]]
c23456_list = [tuple(x) for x in data["c23456_list"]]

BDI = ["M_1", "M_2", "B_1", "T_1", "B_2", "T_2", "S"]

print(f"=== Bucket-2 22-point configuration ===")
print(f"Marginals: {len(c2_list)} × {len(c236_list)} × {len(c23456_list)}")

# Index distribution per axis
print("\n--- i2 distribution (which m_2 column) ---")
ci2 = Counter(t["i2"] for t in indexing)
for k in sorted(ci2):
    print(f"  i2={k} {c2_list[k]}: {ci2[k]} pieces")

print("\n--- i236 distribution (which m_236 column) ---")
ci236 = Counter(t["i236"] for t in indexing)
for k in sorted(ci236):
    print(f"  i236={k:>2} {c236_list[k]}: {ci236[k]} pieces")

print("\n--- i23456 distribution (which m_23456 column) ---")
ci23456 = Counter(t["i23456"] for t in indexing)
for k in sorted(ci23456):
    print(f"  i23456={k} {c23456_list[k]}: {ci23456[k]} pieces")

# Decomposition: which pieces share m_2 = (0,0,1,0,0,0,0) (the most "trivial-like")
# vs which have m_2 → M_2 (= "Cartan/trivial-like")

# Look for natural 4-element subset (Cartan + triv)
print("\n--- Looking for 4 'Cartan + trivial' pieces ---")

# Candidate 1: i2 = 3 + 3 most "extreme" i2=2 pieces.
print("\nPieces with i2 ∈ {2, 3}:")
ext = [t for t in indexing if t["i2"] >= 2]
for t in ext:
    print(f"  i2={t['i2']} i236={t['i236']:>2} i23456={t['i23456']} | {t['name']}")
# Three pieces (i2=2 with 2, i2=3 with 1) = 3 = rank(B_3).  Need 4 with trivial...

print("\nPieces with i2=3 ONLY:")
ext3 = [t for t in indexing if t["i2"] == 3]
for t in ext3:
    print(f"  {t['name']}")

# Check (m_236, m_23456) projection structure
print("\n--- Pieces grouped by (i236, i23456) projection ---")
proj = defaultdict(list)
for t in indexing:
    proj[(t["i236"], t["i23456"])].append(t)
multi = [(k, v) for k, v in proj.items() if len(v) > 1]
print(f"Multi-pieces: {len(multi)}")
for k, v in multi:
    print(f"  i236={k[0]:>2} i23456={k[1]}: {[t['name'] for t in v]}, m_2 ∈ {[t['i2'] for t in v]}")

# What if we look at column-length: sum of entries
print("\n--- m_2 column 'sizes' (sum of nonzero coefs) ---")
for k, col in enumerate(c2_list):
    print(f"  i2={k} {col}, |col|_1 = {sum(abs(x) for x in col)}, support = {[BDI[i] for i,c in enumerate(col) if c!=0]}")

print("\n--- m_236 column 'sizes' ---")
for k, col in enumerate(c236_list):
    print(f"  i236={k:>2} {col}, |col|_1 = {sum(abs(x) for x in col)}, support = {[BDI[i] for i,c in enumerate(col) if c!=0]}")

print("\n--- m_23456 column 'sizes' ---")
for k, col in enumerate(c23456_list):
    print(f"  i23456={k} {col}, |col|_1 = {sum(abs(x) for x in col)}, support = {[BDI[i] for i,c in enumerate(col) if c!=0]}")

# Look for partition of 22 into orbit-sized groups
# B_3 / C_3 adj+triv weight orbits: 12 (long roots), 6 (short roots), 3 (zero w/ mult), 1 (trivial)
# OR: 6 + 12 + 3 + 1 = 22.
# So look for natural partition (X12, X6, X3, X1) of the 22 pieces.

print("\n--- Looking for {12, 6, 3, 1} partition candidates ---")

# Hypothesis A: i2 partition. (9, 10, 2, 1). Sizes don't match.
# Hypothesis B: i236 partition by some structure.

# Let me classify m_2 columns:
#   i2=0: B_1 only
#   i2=1: B_1 + S
#   i2=2: B_1 + 2S
#   i2=3: M_2 + B_1 + 2S
# Group: {i2 ∈ {0, 1}} (basic m_2-mass distributions), {i2 ∈ {2, 3}} (extended).
basic = [t for t in indexing if t["i2"] < 2]
extended = [t for t in indexing if t["i2"] >= 2]
print(f"  basic (i2 ∈ {{0,1}}): {len(basic)} pieces")
print(f"  extended (i2 ∈ {{2,3}}): {len(extended)} pieces")

# m_236 classification by what the column does
#   first 5 columns (i236 ∈ {0..4}) are M_2-free (no M_2 contribution)
#   last 4 columns (i236 ∈ {5..8}) have M_2 contribution (=2)
print("\n--- m_236 columns: M_2 contribution ---")
m2_free = []
m2_active = []
for k, col in enumerate(c236_list):
    has_M2 = col[1] != 0  # M_2 index is 1
    label = "  M_2 active" if has_M2 else "  M_2 free  "
    print(f"  i236={k} {label} {col}")
    if has_M2:
        m2_active.append(k)
    else:
        m2_free.append(k)

c_m2free = [t for t in indexing if t["i236"] in m2_free]
c_m2active = [t for t in indexing if t["i236"] in m2_active]
print(f"\nPieces with M_2-free m_236:   {len(c_m2free)}")
print(f"Pieces with M_2-active m_236: {len(c_m2active)}")

# Same for m_23456
print("\n--- m_23456 columns: M_2 contribution ---")
m2_free23 = []
m2_active23 = []
for k, col in enumerate(c23456_list):
    has_M2 = col[1] != 0
    label = "  M_2 active" if has_M2 else "  M_2 free  "
    print(f"  i23456={k} {label} {col}")
    if has_M2:
        m2_active23.append(k)
    else:
        m2_free23.append(k)

c23_m2free = [t for t in indexing if t["i23456"] in m2_free23]
c23_m2active = [t for t in indexing if t["i23456"] in m2_active23]
print(f"\nPieces with M_2-free m_23456:   {len(c23_m2free)}")
print(f"Pieces with M_2-active m_23456: {len(c23_m2active)}")

# Look at joint M_2-pattern
print("\n--- Joint M_2-pattern (m_2 col, m_236 col, m_23456 col) ---")
for t in indexing:
    has_m2_M2     = c2_list[t["i2"]][1] != 0
    has_m236_M2   = c236_list[t["i236"]][1] != 0
    has_m23456_M2 = c23456_list[t["i23456"]][1] != 0
    pattern = (int(has_m2_M2), int(has_m236_M2), int(has_m23456_M2))
    print(f"  {pattern} | i2={t['i2']} i236={t['i236']:>2} i23456={t['i23456']} | {t['name']}")

# Count by pattern
print("\nPattern counts:")
pat_count = Counter()
for t in indexing:
    has_m2_M2     = c2_list[t["i2"]][1] != 0
    has_m236_M2   = c236_list[t["i236"]][1] != 0
    has_m23456_M2 = c23456_list[t["i23456"]][1] != 0
    pattern = (int(has_m2_M2), int(has_m236_M2), int(has_m23456_M2))
    pat_count[pattern] += 1
for pat, cnt in sorted(pat_count.items()):
    print(f"  {pat}: {cnt}")

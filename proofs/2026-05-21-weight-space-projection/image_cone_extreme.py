"""
Compute extreme rays of the image cone Phi(P_3) by:
1. enumerating all integer points of chain cone with bounded coords
2. applying Phi
3. taking the conic hull
4. reading off facets (which we identify as Phi(L_2), Phi(U_2), Phi(E), and any NT-driven ones)

The chain cone P_3 (after killing M_1 = 0) sits in R^8 with coords
   x = (B_1, T_1, M_2, B_2, T_2, S, N_-, N_+),
subject to:
   x >= 0 (componentwise)
   L_2:  M_2 <= 2(B_1 - T_1)
   U_2:  M_2 <= 2(B_1 - T_1) + 2(B_2 - T_2)
   E:    S   <= 2(B_1 - T_1) + 2(B_2 - T_2)

Phi: R^8 -> R^3:
   lambda_1 = B_1 + T_1 + N_- + N_+
   lambda_2 = M_2 + B_2 + T_2 - N_- + N_+
   lambda_3 = -B_1 + T_1 - B_2 + T_2 + S
"""

import itertools
import numpy as np
from scipy.spatial import ConvexHull

K = 4  # coord bound; we want extreme rays so this needs to be enough to capture all

labels = ['B1','T1','M2','B2','T2','S','Nm','Np']

def feasible(x):
    B1, T1, M2, B2, T2, S, Nm, Np = x
    if min(x) < 0:
        return False
    if M2 > 2*(B1 - T1):
        return False
    if M2 > 2*(B1 - T1) + 2*(B2 - T2):
        return False
    if S > 2*(B1 - T1) + 2*(B2 - T2):
        return False
    return True

def Phi(x):
    B1, T1, M2, B2, T2, S, Nm, Np = x
    L1 = B1 + T1 + Nm + Np
    L2 = M2 + B2 + T2 - Nm + Np
    L3 = -B1 + T1 - B2 + T2 + S
    return (L1, L2, L3)

# Enumerate
pts = set()
pts.add((0,0,0))
for x in itertools.product(range(K+1), repeat=8):
    if feasible(x):
        pts.add(Phi(x))

print(f'Enumerated {len(pts)} image points (with coord bound {K}).')

P = np.array(sorted(pts), dtype=float)
print(f'lambda_1 range: [{P[:,0].min()}, {P[:,0].max()}]')
print(f'lambda_2 range: [{P[:,1].min()}, {P[:,1].max()}]')
print(f'lambda_3 range: [{P[:,2].min()}, {P[:,2].max()}]')

# To compute the cone's facets, intersect with a generic affine slice and take 2D hull.
# Use slice lambda_1 + lambda_2 + 2 lambda_3 = c for various c, but cleaner: just take
# the conic hull as the convex hull of {points} \cup {-origin scaled}, normalize and use
# scipy. Simpler approach: append origin, take 3D ConvexHull.

# Even simpler approach: since we know the cone is in R^3 with apex 0, its facets are
# determined by pairs of "extreme rays". The set of rays = directions {x/|x| : x in cone, x != 0}.
# We can find them by:
#   take all nonzero points, normalize so the first coord (or any) sums to 1, compute hull.
# But cone may include 0 vectors; let's just compute hull of {P, 0} in R^3.

hull_pts = np.vstack([P, [[0,0,0]]])
hull = ConvexHull(hull_pts)
print(f'\n3D convex hull of points: {len(hull.vertices)} vertices, {len(hull.simplices)} triangles')

# Each facet is given as a hyperplane a.x <= b. For a cone with apex at 0, the facets
# passing through 0 are the "cone facets"; the cap is non-cone facets. We want only
# the ones with b=0 (passing through origin).

print('\nCone facets (hyperplanes passing through origin, a.lambda <= b with b=0):')
seen = set()
for eq in hull.equations:
    # eq has 4 entries: [a1, a2, a3, b] s.t. a.x + b <= 0 (scipy convention)
    a = eq[:3]
    b = eq[3]
    # Skip facets not through origin (those are the "capping" facets from the finite cutoff)
    if abs(b) > 1e-8:
        continue
    # Normalize so first nonzero entry is positive integer (approximately)
    # Use integer-ish normalization
    aa = a.copy()
    nz = aa[np.abs(aa) > 1e-8]
    if len(nz) == 0:
        continue
    # Scale so smallest |coord| ≈ 1
    scale = np.min(np.abs(nz))
    aa = aa / scale
    # Round to nearest integer
    aar = np.round(aa)
    if np.max(np.abs(aar - aa)) > 1e-4:
        # Not nice integer; print float
        key = tuple(np.round(aa, 6))
    else:
        key = tuple(int(v) for v in aar)
    # Canonicalize sign: ensure first nonzero is positive (we want a.lambda <= 0 form;
    # if a.lambda + b <= 0 with b=0, sign matters; keep as-is)
    if key in seen:
        continue
    seen.add(key)
    s = ' + '.join(f'{c}*L{i+1}' for i, c in enumerate(key) if c != 0)
    print(f'  {s} <= 0  (scipy eq raw: {[float(x) for x in eq]})')

print(f'\nDistinct cone facets through origin: {len(seen)}')

# Also list the "extreme rays" of the cone: vertices of the hull that are nonzero
# and only in cone-facets (not the cap).
print('\nExtreme rays of image cone (sample): vertices of hull on multiple origin-facets')
verts = hull.vertices
origin_idx = len(hull_pts) - 1
for vidx in verts:
    if vidx == origin_idx:
        continue
    p = hull_pts[vidx]
    # Count how many origin-facets it's on
    on_facets = 0
    for eq in hull.equations:
        if abs(eq[3]) > 1e-8:
            continue
        if abs(np.dot(eq[:3], p) + eq[3]) < 1e-8:
            on_facets += 1
    if on_facets >= 2:
        # Normalize ray
        gcd_val = np.gcd.reduce([int(round(c)) for c in p if abs(c) > 1e-9])
        if gcd_val == 0:
            gcd_val = 1
        ray = tuple(int(round(c))//gcd_val for c in p)
        print(f'  ray {ray}  (on {on_facets} origin-facets, {p.tolist()})')

"""
Same as image_cone_extreme.py but with NT block fixed at 0 (N_- = N_+ = 0).
This isolates the chain-only contribution and lets us see if NT is ABSORBING facets
that the chain alone would have.

If image cone has same 3 facets WITHOUT NT, then NT doesn't matter — chain alone gives
the 3 facets.

If image cone has MORE facets WITHOUT NT, then NT block is expanding the image to
absorb them.
"""

import itertools
import numpy as np
from scipy.spatial import ConvexHull

K = 5  # bumped up

def feasible(B1, T1, M2, B2, T2, S):
    if min(B1, T1, M2, B2, T2, S) < 0:
        return False
    if M2 > 2*(B1 - T1):
        return False
    if M2 > 2*(B1 - T1) + 2*(B2 - T2):
        return False
    if S > 2*(B1 - T1) + 2*(B2 - T2):
        return False
    return True

def Phi(B1, T1, M2, B2, T2, S):
    return (B1+T1, M2+B2+T2, -B1+T1-B2+T2+S)

pts = set([(0,0,0)])
for B1,T1,M2,B2,T2,S in itertools.product(range(K+1), repeat=6):
    if feasible(B1,T1,M2,B2,T2,S):
        pts.add(Phi(B1,T1,M2,B2,T2,S))

print(f'Image points (NO NT block, K={K}): {len(pts)}')

P = np.array(sorted(pts), dtype=float)
hull_pts = np.vstack([P, [[0,0,0]]])
hull = ConvexHull(hull_pts)

print(f'\n3D hull: {len(hull.vertices)} vertices, {len(hull.simplices)} simplices')
print('\nCone facets (through origin):')
seen = set()
for eq in hull.equations:
    a, b = eq[:3], eq[3]
    if abs(b) > 1e-8:
        continue
    nz = a[np.abs(a) > 1e-8]
    if len(nz) == 0:
        continue
    scale = np.min(np.abs(nz))
    aa = a/scale
    aar = np.round(aa)
    if np.max(np.abs(aar - aa)) < 1e-4:
        key = tuple(int(v) for v in aar)
    else:
        key = tuple(np.round(aa, 6))
    if key in seen:
        continue
    seen.add(key)
    s = ' + '.join(f'{c}*L{i+1}' for i,c in enumerate(key) if c != 0)
    print(f'  {s} <= 0')

print(f'\nDistinct origin-facets: {len(seen)}')

# Now check the L_2 and U_2 witnesses to see which facet, if any, they saturate
print('\nWitness check (no NT):')
witnesses = {
    'L_2 interior witness': (1,0,2,1,0,0),
    'U_2 interior witness': (2,0,2,0,1,0),
    'E interior witness':   (1,0,0,1,0,4),
}
for lbl, w in witnesses.items():
    p = Phi(*w)
    on_facets = []
    for key in seen:
        s = sum(c*v for c,v in zip(key, p))
        if abs(s) < 1e-8:
            on_facets.append(key)
    print(f'  {lbl} {w} -> {p}, on facets: {on_facets}')

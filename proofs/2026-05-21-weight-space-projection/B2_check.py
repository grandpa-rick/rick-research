"""
B_2 sanity check.

Chain coords: (M_1, B_1, T_1, S), with M_1 = 0 on P_2.
Carry: P_1 = 2(B_1 - T_1).
Chain facets (after Theorem F): only E: S <= P_1.
Plus non-negativity: B_1, T_1, S >= 0.
No NT block (all positive roots of B_2 touch alpha_2).

Phi: (B_1, T_1, S) -> (lambda_1, lambda_2) =
   lambda_1 = B_1 + T_1     [E_1 coefficient]
   lambda_2 = -B_1 + T_1 + S  [E_2 coefficient]
"""
import itertools, numpy as np
from scipy.spatial import ConvexHull

K = 6
def feasible(B1, T1, S):
    if min(B1, T1, S) < 0: return False
    if S > 2*(B1 - T1): return False
    return True

def Phi(B1, T1, S):
    return (B1+T1, -B1+T1+S)

pts = set([(0,0)])
for B1,T1,S in itertools.product(range(K+1), repeat=3):
    if feasible(B1,T1,S):
        pts.add(Phi(B1,T1,S))

print(f'Image points at B_2 (K={K}): {len(pts)}')
P = np.array(sorted(pts), dtype=float)
print(f'lambda_1: [{P[:,0].min()},{P[:,0].max()}], lambda_2: [{P[:,1].min()},{P[:,1].max()}]')

# 2D convex hull including origin
hull_pts = np.vstack([P, [[0,0]]])
hull = ConvexHull(hull_pts)
print(f'\n2D hull: {len(hull.vertices)} vertices, {len(hull.simplices)} edges')

# Cone facets (through origin)
print('\nCone facets (a.lambda + b <= 0, keeping b=0):')
seen = set()
for eq in hull.equations:
    a, b = eq[:2], eq[2]
    if abs(b) > 1e-8: continue
    nz = a[np.abs(a) > 1e-8]
    if len(nz)==0: continue
    aa = a/np.min(np.abs(nz))
    aar = np.round(aa)
    if np.max(np.abs(aar - aa)) < 1e-4:
        key = tuple(int(v) for v in aar)
    else:
        key = tuple(np.round(aa, 4))
    if key in seen: continue
    seen.add(key)
    s = ' + '.join(f'{c}*L{i+1}' for i,c in enumerate(key) if c != 0)
    print(f'  {s} <= 0')

print(f'\nDistinct origin-facets at B_2: {len(seen)}')

# Witnesses
print('\nWitness check:')
# E witness at B_2: B_1=1, S=2
print('  E witness (B1=1, S=2):', Phi(1,0,2), '-> check facets:')
for key in seen:
    val = sum(c*v for c,v in zip(key, Phi(1,0,2)))
    print(f'    {key}: value = {val}')

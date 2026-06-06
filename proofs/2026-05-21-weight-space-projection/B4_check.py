"""
B_4 spot check: enumerate enough chain+NT configs to find extreme rays
of image cone Phi(P_4) in R^4.

Chain coords: M_1=0, then (B_1,T_1), (M_2,B_2,T_2), (M_3,B_3,T_3), S.
NT roots: E_1-E_2, E_1+E_2, E_1-E_3, E_1+E_3, E_2-E_3, E_2+E_3.

Phi (in (E_1, E_2, E_3, E_4) basis):
   lambda_a = M_a + B_a + T_a + (sum of NT contribs at E_a)   for a=1,2,3 (with M_1=0)
   lambda_4 = S - B_1 + T_1 - B_2 + T_2 - B_3 + T_3
   (NT contributes 0 to lambda_4)
"""

import itertools, numpy as np
from scipy.spatial import ConvexHull

# Smaller K, but cover the structurally important configurations
K_chain = 2
K_NT = 2  # smaller

def feasible_chain(B1,T1,M2,B2,T2,M3,B3,T3,S):
    if min(B1,T1,M2,B2,T2,M3,B3,T3,S) < 0: return False
    P1 = 2*(B1-T1); P2 = P1 + 2*(B2-T2); P3 = P2 + 2*(B3-T3)
    # L_a: M_a <= P_{a-1}, U_a: M_a <= P_a
    if M2 > P1: return False
    if M2 > P2: return False
    if M3 > P2: return False
    if M3 > P3: return False
    if S > P3: return False
    return True

def chain_phi(B1,T1,M2,B2,T2,M3,B3,T3,S):
    L1 = B1 + T1
    L2 = M2 + B2 + T2
    L3 = M3 + B3 + T3
    L4 = -B1+T1 -B2+T2 -B3+T3 + S
    return (L1, L2, L3, L4)

def NT_phi(N12m, N12p, N13m, N13p, N23m, N23p):
    # N12m * (E1-E2) + N12p * (E1+E2) + N13m * (E1-E3) + N13p * (E1+E3) + N23m * (E2-E3) + N23p * (E2+E3)
    L1 = N12m + N12p + N13m + N13p
    L2 = -N12m + N12p + N23m + N23p
    L3 = -N13m + N13p - N23m - N23p  # wait: E2-E3 has E3-coeff -1, E2+E3 has E3-coeff +1
    # Let me redo:
    # E_1 - E_2: contributes (1, -1, 0, 0)
    # E_1 + E_2: contributes (1, 1, 0, 0)
    # E_1 - E_3: contributes (1, 0, -1, 0)
    # E_1 + E_3: contributes (1, 0, 1, 0)
    # E_2 - E_3: contributes (0, 1, -1, 0)
    # E_2 + E_3: contributes (0, 1, 1, 0)
    L1 = N12m + N12p + N13m + N13p
    L2 = -N12m + N12p + N23m + N23p
    L3 = -N13m + N13p - N23m + N23p
    L4 = 0
    return (L1, L2, L3, L4)

# Enumerate
pts = set([(0,0,0,0)])
chain_count = 0
for tup in itertools.product(range(K_chain+1), repeat=9):
    if feasible_chain(*tup):
        chain_count += 1
        cphi = chain_phi(*tup)
        for nt in itertools.product(range(K_NT+1), repeat=6):
            ntphi = NT_phi(*nt)
            pts.add(tuple(a+b for a,b in zip(cphi, ntphi)))

print(f'Feasible chain configs (K_chain={K_chain}): {chain_count}')
print(f'Total image points (with NT K_NT={K_NT}): {len(pts)}')

P = np.array(sorted(pts), dtype=float)
hull_pts = np.vstack([P, [[0,0,0,0]]])

try:
    hull = ConvexHull(hull_pts)
    print(f'\n4D hull: {len(hull.vertices)} vertices, {len(hull.simplices)} simplices')
    print('\nOrigin-cone facets:')
    seen = set()
    for eq in hull.equations:
        a, b = eq[:4], eq[4]
        if abs(b) > 1e-8: continue
        nz = a[np.abs(a) > 1e-8]
        if len(nz) == 0: continue
        aa = a/np.min(np.abs(nz))
        aar = np.round(aa)
        if np.max(np.abs(aar - aa)) < 1e-3:
            key = tuple(int(v) for v in aar)
        else:
            key = tuple(np.round(aa, 4))
        if key in seen: continue
        seen.add(key)
        s = ' + '.join(f'{c}*L{i+1}' for i,c in enumerate(key) if c != 0)
        print(f'  {s} <= 0')
    print(f'\nDistinct origin-facets at B_4: {len(seen)}')
except Exception as e:
    print(f'ConvexHull failed: {e}')

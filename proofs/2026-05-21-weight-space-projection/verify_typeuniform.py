"""
Verify the type-uniform conjecture at B_3, B_4, B_5:

CONJECTURE (Theorem G): For n >= 2, image cone Phi(P_n) in R^n has exactly n facets:
  F_k: lambda_1 + ... + lambda_k >= 0  for k = 1, ..., n-2
  F_sum: lambda_1 + ... + lambda_n >= 0
  F_E: lambda_n <= lambda_1 + ... + lambda_{n-1}

Approach: for each n in {3, 4, 5}, enumerate feasible chain+NT configs with small
total content, compute image points, find convex hull facets, compare to conjecture.
"""

import itertools, numpy as np
from scipy.spatial import ConvexHull

def test_Bn(n, total_cap=4):
    """Enumerate chain configs at B_n with total content <= total_cap."""
    # Chain coords: (M_2, ..., M_{n-1}), (B_1, ..., B_{n-1}), (T_1, ..., T_{n-1}), S.
    # M_1 = 0 (forced)
    # Total coords: (n-2) + (n-1) + (n-1) + 1 = 3n - 5 chain coords (with M_1 dropped).

    # NT coords: 2 * binom(n-1, 2) = (n-1)(n-2) NT coords (E_a +/- E_b for a < b <= n-1).

    # Enumerate by partial-product over (M's, B's, T's, S, NT's) with total <= cap.
    # For simplicity, use a recursive enumeration with budget.

    NT_pairs = [(a, b) for a in range(1, n) for b in range(a+1, n)]  # 1-indexed a<b<=n-1
    nNT = 2 * len(NT_pairs)

    pts = set()
    pts.add(tuple([0]*n))

    # Enumerate by total content
    coords = ['M'+str(a) for a in range(2, n)] + \
             ['B'+str(a) for a in range(1, n)] + \
             ['T'+str(a) for a in range(1, n)] + \
             ['S'] + \
             [f'Nm{a}{b}' for (a,b) in NT_pairs] + \
             [f'Np{a}{b}' for (a,b) in NT_pairs]

    ncoords = len(coords)

    def feasible(vals):
        # M_a = 0 for a = 1; otherwise extract
        # Build M, B, T arrays (1-indexed conceptually)
        idx = {}
        for i, c in enumerate(coords):
            idx[c] = vals[i]
        M = [0] + [0] + [idx.get(f'M{a}', 0) for a in range(2, n)]  # M[a] for a in 1..n-1, but M[1]=0
        # actually let me just do: M[a] for a=1..n-1: M[1] = 0; M[a] for a>=2 from idx.
        M = {a: (0 if a == 1 else idx[f'M{a}']) for a in range(1, n)}
        B = {a: idx[f'B{a}'] for a in range(1, n)}
        T = {a: idx[f'T{a}'] for a in range(1, n)}
        S = idx['S']
        # nonnegativity: by construction.
        # Carry
        P = {0: 0}
        for a in range(1, n):
            P[a] = P[a-1] + 2*(B[a] - T[a])
        # L_a, U_a for a in 1..n-1
        for a in range(1, n):
            if M[a] > P[a-1]: return False
            if M[a] > P[a]: return False
        if S > P[n-1]: return False
        return True

    def Phi(vals):
        idx = {}
        for i, c in enumerate(coords):
            idx[c] = vals[i]
        M = {a: (0 if a == 1 else idx[f'M{a}']) for a in range(1, n)}
        B = {a: idx[f'B{a}'] for a in range(1, n)}
        T = {a: idx[f'T{a}'] for a in range(1, n)}
        S = idx['S']

        lam = [0]*n
        for a in range(1, n):
            lam[a-1] = M[a] + B[a] + T[a]  # E_a components from chain
        lam[n-1] = S + sum(T[a] - B[a] for a in range(1, n))
        # NT contributions
        for (a, b) in NT_pairs:
            nm = idx[f'Nm{a}{b}']
            np_ = idx[f'Np{a}{b}']
            # E_a - E_b: +1 on lam[a-1], -1 on lam[b-1]
            lam[a-1] += nm
            lam[b-1] -= nm
            # E_a + E_b: +1 on both
            lam[a-1] += np_
            lam[b-1] += np_
        return tuple(lam)

    # Enumerate
    def enum(idx, budget, cur):
        if idx == ncoords:
            if feasible(cur):
                pts.add(Phi(cur))
            return
        for v in range(budget + 1):
            cur[idx] = v
            enum(idx + 1, budget - v, cur)
        cur[idx] = 0  # reset

    enum(0, total_cap, [0]*ncoords)

    print(f'B_{n}: {len(pts)} image points with total content <= {total_cap}')
    return pts

def analyze(pts, n):
    P = np.array(sorted(pts), dtype=float)
    hull_pts = np.vstack([P, [[0]*n]])
    try:
        hull = ConvexHull(hull_pts)
    except Exception as e:
        print(f'  ConvexHull failed: {e}')
        return
    print(f'  {n}D hull: {len(hull.vertices)} vertices')
    seen = set()
    for eq in hull.equations:
        a, b = eq[:n], eq[n]
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
        print(f'  facet: {s} <= 0')
    print(f'  total {len(seen)} facets')
    return seen

# Check B_3, B_4, B_5
for n in [3, 4, 5]:
    print(f'\n=== B_{n} ===')
    cap = {3: 6, 4: 4, 5: 3}[n]
    pts = test_Bn(n, total_cap=cap)
    seen = analyze(pts, n)
    # Compare to conjecture
    print(f'  Expected facets:')
    for k in range(1, n-1):  # k = 1, ..., n-2
        e = tuple([-1]*k + [0]*(n-k))
        print(f'    {e} (partial sum k={k}): {"FOUND" if e in seen else "MISSING"}')
    e_sum = tuple([-1]*n)
    print(f'    {e_sum} (full sum): {"FOUND" if e_sum in seen else "MISSING"}')
    e_E = tuple([-1]*(n-1) + [1])
    print(f'    {e_E} (E-facet): {"FOUND" if e_E in seen else "MISSING"}')

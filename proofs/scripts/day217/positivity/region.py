"""Numerical sign test of structure constants on regions of (s,t)>0."""
import sys, pickle, numpy as np
from sympy import symbols, lambdify
s, t = symbols('s t')
basis, MAXN = sys.argv[1], int(sys.argv[2])
G = pickle.load(open(f'g_{basis}_{MAXN}.pkl', 'rb'))
L = np.exp(np.linspace(-3, 3, 61)); SS, TT = np.meshgrid(L, L)
regions = {'s<1,t<1': (SS < 1)&(TT < 1), 's<1,t>1': (SS < 1)&(TT > 1), 's>1,t<1': (SS > 1)&(TT < 1), 's>1,t>1': (SS > 1)&(TT > 1),
           'st<1': SS*TT < 1-1e-9, 'st>1': SS*TT > 1+1e-9, 's<1,st<1': (SS < 1)&(SS*TT < 1-1e-9), 's<1,st>1': (SS<1)&(SS*TT>1+1e-9),
           's>1,st<1': (SS>1)&(SS*TT<1-1e-9), 's>1,st>1': (SS>1)&(SS*TT>1+1e-9)}
vals = {k: lambdify((s, t), v, 'numpy')(SS, TT)*np.ones_like(SS) for k, v in G.items()}
for name, R in regions.items():
    bad = [k for k, V in vals.items() if (V[R] < -1e-12).any() and (V[R] > 1e-12).any()]
    neg = [k for k, V in vals.items() if k not in bad and (V[R] < -1e-12).any()]
    print(f'{basis} n<={MAXN} region {name}: sign-changing {len(bad)}/{len(G)}, uniformly negative {len(neg)}', ('ex '+str(bad[0])+' '+str(G[bad[0]])) if bad else '')

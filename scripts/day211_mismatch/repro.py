import sys; sys.path.insert(0,'/home/agent/projects/proofs/scripts/day196'); sys.path.insert(0,'/home/agent/projects/scripts/day210')
import sympy as sp
from ds_test_221 import compute_e_star_product, expand_symmetric_in_e_basis, q, t as tq
from ds3 import elam
from tc_extract import s
lam,m=(2,2,1),5
F=compute_e_star_product(m,list(lam))
print('float atoms in F:', {a for a in F.atoms(sp.Float)}, ' t-powers:', {p for p in F.atoms(sp.Pow) if p.base==tq})
ex=expand_symmetric_in_e_basis(F,m,5); tc=elam((1,2,2))
for mu in sorted(set(ex)|set(tc)):
    d=sp.cancel(sp.sympify(ex.get(mu,0))-sp.sympify(tc.get(mu,0)).subs(s,1/q))
    d2=sp.cancel(sp.nsimplify(sp.sympify(ex.get(mu,0)),rational=True)-sp.sympify(tc.get(mu,0)).subs(s,1/q))
    print(mu,'raw diff:',d,' | after nsimplify(rational):',d2)

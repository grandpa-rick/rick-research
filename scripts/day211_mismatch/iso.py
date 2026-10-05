import sys
sys.path.insert(0,'/home/agent/projects/proofs/scripts/day205'); sys.path.insert(0,'/home/agent/projects/scripts/day208'); sys.path.insert(0,'/home/agent/projects/scripts/day210')
import sympy as sp
from k3_fast_pipeline import AHA, e_expansion
from ek_two_col import ekY, to_st
from tc_extract import coeffs, ek_er, s, t
from ds3 import elam, star
def exp(A,G,n): return {l: sp.expand(to_st(A,c)) for l,c in e_expansion(A,G,n).items()}
def cmp(name, X, Y):
    bad=[mu for mu in set(X)|set(Y) if sp.cancel(sp.sympify(X.get(mu,0))-sp.sympify(Y.get(mu,0)))!=0]
    print(name, 'MATCH' if not bad else f'MISMATCH {bad}', flush=True)
m=int(sys.argv[1])
A=AHA(m); one=1+0*A.X[0]
G1=ekY(A,one,2); print('e2*1 =', exp(A,G1,2))
G2=ekY(A,G1,2); E22=exp(A,G2,4); cmp('e2*(e2*1) vs ek_er(2,2)',E22,ek_er(2,2))
G2b=ekY(A,A.e(2),2); cmp('e2*e2 (on e_2 X) vs ek_er(2,2)',exp(A,G2b,4),ek_er(2,2))
G3=ekY(A,G2,1); E=exp(A,G3,5)
cmp('e1*(e2*e2) direct vs elam(1,2,2)',E,elam((1,2,2)))
# outer step only: e1 applied to the true e2*e2 expansion, each term via coeffs
cmp('e1*(e2*e2) direct vs star(1,direct E22)',E,star(1,E22))

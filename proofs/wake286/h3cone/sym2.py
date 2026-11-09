import json, sympy as sp, sys
from fractions import Fraction as F
cells=json.load(open('cells5.json'))
t=sp.symbols('t',positive=True)
def run(c,i,j,tv):
    A=[sp.Matrix(a) for a in c['A']]; E=sp.eye(5)
    v=E[:,i]-t*E[:,j]
    orb=[(v,'')]; fr=[(v,'')]
    def norm(w): 
        w=w.subs(t,tv); m=max(abs(x) for x in w); return tuple(w/m)
    keys={norm(v)}
    while fr and len(orb)<40:
        new=[]
        for u,nm in fr:
            for k,a in enumerate(A):
                w=sp.expand(a*u)
                wn=w.subs(t,tv)
                if all(x>=0 for x in wn): continue
                if norm(w) in keys: continue
                keys.add(norm(w)); orb.append((w,str(k+1)+nm)); new.append((w,str(k+1)+nm))
        fr=new
    return orb, not fr
for cn,ci in [('5_2',3),('5_1',0)]:
  c=cells[ci]
  for (i,j) in ([(4,0),(4,2),(3,1)] if cn=='5_2' else [(2,0),(3,1),(4,0)]):
    orb,fin=run(c,i,j,sp.Rational(1,20))
    print(cn,'v=c%d - t c%d'%(i,j),'finite',fin)
    for w,nm in orb: print('   word(1+s)^',nm or 'id',list(w))

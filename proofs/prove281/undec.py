import sys,json; sys.path.insert(0,'.')
from common import *
from orbit import search,status
n=15
R=json.load(open('twin15_5433.json'))
for r in R:
    if r['verdict']!='UNDECIDED': continue
    Q=r['Q']; x=rsk_inv(r['Px'],Q); z=rsk_inv(r['Pz'],Q)
    V=json.load(open('viol15.json'))
    U=[e for e in V if tuple(e['lam'])==(5,4,3,3) and e['A']==r['A']][0]['U'][0]
    y=rsk_inv(U,Q)
    print('Px',r['Px'],'Pz',r['Pz'],'U',U,'L(y)',sorted(L(y)))
    print('l(x),l(y),l(z)',inv(x),inv(y),inv(z),'y<=x',bruhat_le(y,x),'y<=z',bruhat_le(y,z),'z<=y',bruhat_le(z,y))
    st,info,sz=search(y,z,cap=3000000); print(st,sz,info if st in('cap','exhausted') else '')
    st2,info2,sz2=search(y,x); print('y,x',st2,sz2)

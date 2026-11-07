"""For parity-failing candidate pairs: in which canonical cells Q is x=(Px,Q) not <= z=(Pz,Q) in Bruhat?"""
import sys,json
sys.path.insert(0,'.')
from cfg import rsk_inv, bru
from collections import Counter
D=json.load(open('pfail.json'))
def superstd(lam):
    k=0;T=[]
    for r in lam: T.append(list(range(k+1,k+r+1))); k+=r
    return T
def colstd(lam):
    lamt=[sum(1 for r in lam if r>c) for c in range(lam[0])]
    T=[[0]*r for r in lam]; k=0
    for c,h in enumerate(lamt):
        for r in range(h): k+=1; T[r][c]=k
    return T
c=Counter(); allfail=[]
for d in D:
    lam=d['lam']; Px,Pz=d['Px'],d['Pz']
    res={}
    for name,Q in (('Q0',superstd(lam)),('Qcol',colstd(lam)),('Tx',Px),('Tz',Pz)):
        x=rsk_inv(Px,Q); z=rsk_inv(Pz,Q)
        res[name]=not bru(x,z)
    c[tuple(sorted(k for k,v in res.items() if v))]+=1
    if not any(res.values()): allfail.append(d)
print(c); print('none incomparable:',len(allfail))

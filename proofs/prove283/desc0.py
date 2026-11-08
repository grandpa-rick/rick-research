import json
from interval import length
B=json.load(open('qbest.json'))
def L(w): return {i for i in range(1,len(w)) if w.index(i+1)<w.index(i)}
def R(w): return {i for i in range(1,len(w)) if w[i-1]>w[i]}
for k in (0,1):
    x,z=B[k]['x'],B[k]['z']
    print(k,'L(z)',sorted(L(z)),'L(x)',sorted(L(x)),'R(z)',sorted(R(z)),'R(x)',sorted(R(x)), 'Lz<=Lx',L(z)<=L(x),'Rz<=Rx',R(z)<=R(x))

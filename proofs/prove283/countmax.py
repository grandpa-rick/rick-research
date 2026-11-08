import json,time
from interval import covers_down,rankmat,geq_x
B=json.load(open('qbest.json'))
def L(w): return {i for i in range(1,len(w)) if w.index(i+1)<w.index(i)}
def R(w): return {i for i in range(1,len(w)) if w[i-1]>w[i]}
x,z=B[0]['x'],B[0]['z']; J=R(z); K=L(z)
Rx=rankmat(x); level={tuple(z)}; allv=set(level)
while level:
    nxt=set(v for w in level for v in covers_down(w) if geq_x(v,Rx)); allv|=nxt; level=nxt
print(len(allv))
rm=[w for w in allv if R(w)>=J]; dm=[w for w in rm if L(w)>=K]
print('right-max',len(rm),'double-max',len(dm))

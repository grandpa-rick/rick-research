import pickle, random, sys, time
from collections import Counter
from d8lib import *
n=8; T=pickle.load(open('targets8.pkl','rb')); key=sys.argv[1]; tgt=T[key]['dist']; dim=T[key]['dim']
random.seed(2)
def dist(P): return Counter(ldes(u) for u in P)
def rand_elt():
    p=list(range(1,n+1)); random.shuffle(p); sg=[random.choice((1,-1)) for _ in range(n)]
    if sg.count(-1)%2: sg[0]*=-1
    return tuple(a*b for a,b in zip(p,sg))
sub=lambda d,t: all(t.get(A,0)>=c for A,c in d.items())
print('target dim',dim,'#descent sets',len(tgt))
seen=set(); hits=Counter(); t0=time.time(); shown=0
while time.time()-t0<120:
    w=rand_elt()
    if w in seen or ldes(w) not in tgt: continue
    P=f2_closure(w,n,cap=3000)
    if P is None: continue
    seen|=P
    if sub(dist(P),tgt):
        hits[len(P)]+=1
        if shown<3:
            shown+=1; d=dist(P); miss={tuple(sorted(A)):c-d.get(A,0) for A,c in tgt.items() if c-d.get(A,0)}
            print('sub-piece size',len(P),'missing (size %d):'%sum(miss.values()), sorted(miss.items())[:12])
print('sub-pieces by size', dict(hits))

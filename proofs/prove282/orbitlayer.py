"""Left-star orbit (simultaneous, Lemma S) of (y,z) in cell Q0, testing tableau-level layer decider at each node."""
import json,sys
sys.path.insert(0,'.')
import tdec
from tdec import dec_tab
from rskmod import rsk
from cfg import rsk_inv
from collections import deque
def Ls(w):
    p={a:i for i,a in enumerate(w)}; return {i for i in range(1,len(w)) if p[i+1]<p[i]}
def lm(w,i): return [i+1 if a==i else i if a==i+1 else a for a in w]
def lstar(w,i):
    L=Ls(w); a,b=(i in L),(i+1 in L)
    if a==b: return None
    for j in (i,i+1):
        u=lm(w,j); Lu=Ls(u)
        if (i in Lu)!=(i+1 in Lu) and ((i in Lu)!=a): return u
    return None
R=json.load(open('rest16.json'))
for c in R:
    if c['res'] is not None: continue
    lam=c['lam']; k=0; Q0=[]
    for m in lam: Q0.append(list(range(k+1,k+m+1))); k+=m
    y=rsk_inv(c['Py'],Q0); z=rsk_inv(c['Pz'],Q0)
    seen={(tuple(y),tuple(z))}; dq=deque([(y,z,[])]); found=None; cnt=0
    while dq and cnt<int(sys.argv[1]):
        a,b,p=dq.popleft(); cnt+=1
        tdec.memo.clear()
        r=dec_tab([list(x) for x in rsk(a)[0]],[list(x) for x in rsk(b)[0]],budget=60)
        if r is not None: found=(r[0],p,[t[:3] for t in r[1]]); break
        for i in range(1,len(a)-1):
            a2=lstar(a,i); b2=lstar(b,i)
            if a2 is None or b2 is None: continue
            if (tuple(a2),tuple(b2)) not in seen: seen.add((tuple(a2),tuple(b2))); dq.append((a2,b2,p+[i]))
    print(lam,c['A'],c['kind'],c['s'],'orbit nodes visited',cnt,'queue',len(dq),'->',found,flush=True)

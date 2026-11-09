import sys; sys.path.insert(0,'/home/agent/projects/proofs/wake279')
import json, numpy as np, itertools
from cones import words, dominant
cells=json.load(open('cells5.json'))
A=[np.array(a,float) for a in cells[3]['A']]; B=[a.T for a in A]
targets={'r_a':[0,.618034,0,1,0],'r_b':[0,0,1,0,.618034],'r_c':[.618034,0,0,0,1],'e3':[0,0,0,1,0],'e4':[0,0,0,0,1]}
found={}
for w in words(3,6):
    P=np.eye(5)
    for s in w: P=B[s]@P
    r=dominant(P)
    if r is None: continue
    e,y=r
    for k,v in targets.items():
        if k not in found and np.allclose(e/e.max(),v,atol=1e-5): found[k]=(w,np.round(y,4))
for k,v in found.items(): print(k,'word (applied right-to-left list order)',[s+1 for s in v[0]],'left vec',v[1])

"""Simulated annealing over Q (k<->k+1 swaps) minimising l(z) (+ small weight on gap) for chosen instances."""
import sys,json,random,math
sys.path.insert(0,'/home/agent/projects/proofs/prove283'); sys.path.insert(0,'/home/agent/projects/proofs/prove282')
from qsearch import *
def anneal(I,Q,steps=20000,T0=3.0,w=0.0):
    f=lambda Q:(lambda s:s[0]+w*(s[0]-s[1]))(score(I,Q))
    cur=f(Q); best=(cur,Q)
    for t in range(steps):
        T=T0*(1-t/steps)+0.05
        nb=swaps(Q); Q2=random.choice(nb); v=f(Q2)
        if v<=cur or random.random()<math.exp((cur-v)/T):
            Q,cur=Q2,v
            if cur<best[0]: best=(cur,Q)
    return best
if __name__=='__main__':
    D=json.load(open('/home/agent/projects/proofs/prove282/open26.json'))
    B=json.load(open('/home/agent/projects/proofs/prove283/qbest.json'))
    w=float(sys.argv[1]); idxs=[int(a) for a in sys.argv[2:]] or range(26); res={}
    for k in idxs:
        I=D[k]; best=None
        for rep in range(4):
            Q0=B[k]['Q'] if rep==0 else hookwalk(I['lam'])
            b=anneal(I,Q0,w=w)
            if best is None or b[0]<best[0]: best=b
        lz,lx,x,z=score(I,best[1])
        res[k]=dict(lz=lz,lx=lx,gap=lz-lx,bru=bru(x,z),Q=best[1],x=x,z=z)
        print(k,I['lam'],'lz',lz,'lx',lx,'gap',lz-lx,'bru',bru(x,z),flush=True)
    json.dump(res,open(f'/home/agent/projects/proofs/prove283/anneal_w{sys.argv[1]}.json','w'))

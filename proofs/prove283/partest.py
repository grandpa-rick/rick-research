"""Empirical test: Dyer formula on the induced Bruhat graph of J-maximal (and K,J double-maximal) elements of [x,z]."""
import random,subprocess,itertools
from kl import brute,interval_elems,refl_order
from interval import length
def L(w): return {i for i in range(1,len(w)) if w.index(i+1)<w.index(i)}
def R(w): return {i for i in range(1,len(w)) if w[i-1]>w[i]}
def dyer_on(Es,z,kind='lex'):
    E=sorted(Es,key=lambda w:(length(w),w)); idx={w:i for i,w in enumerate(E)}; n=len(z); ro=refl_order(n,kind); edges=[]
    for a in E:
        for i in range(n):
            for j in range(i+1,n):
                if a[i]<a[j]:
                    b=list(a); b[i],b[j]=b[j],b[i]; b=tuple(b)
                    if b in idx: edges.append((idx[a],idx[b],ro[(i,j)] if LAB=="pos" else ro[(a[i]-1,a[j]-1)]))
    edges.sort(key=lambda e:(e[1],e[2]))
    inp=f"{len(E)} {len(edges)} {idx[tuple(z)]}\n"+" ".join(str(length(w)) for w in E)+"\n"+"\n".join(f"{a} {b} {l}" for a,b,l in edges)+"\n"
    out=subprocess.run(['./dyer'],input=inp,capture_output=True,text=True,check=True).stdout
    res={}
    for line in out.split('\n'):
        if line.strip():
            t=list(map(int,line.split())); p=t[1:]
            while len(p)>1 and p[-1]==0: p.pop()
            res[E[t[0]]]=p
    return res
import sys
LAB=sys.argv[1]
for n in (5,6):
    W,P,mu=brute(n); random.seed(n)
    stats={'right':[0,0],'double':[0,0],'leftonly':[0,0]}
    tops=[w for w in W if len(R(w))>=1]; random.shuffle(tops)
    for z in tops[:60]:
        J=set(random.sample(sorted(R(z)),random.randint(1,len(R(z))))); K=set(random.sample(sorted(L(z)),random.randint(0,len(L(z)))))
        cand=[u for u in W if (u,z) in P and R(u)>=J]
        x=random.choice(cand)
        I=interval_elems(list(x),list(z))
        for mode,S in (('right',[w for w in I if R(w)>=J]),('double',[w for w in I if R(w)>=J and L(w)>=K]),('leftonly',[w for w in I if L(w)>=K])):
            if tuple(z) not in S: continue
            res=dyer_on(S,z)
            for u,p in res.items():
                stats[mode][1]+=1
                if p!=P[(u,z)]: stats[mode][0]+=1
    print('S',n,'fails/checked',stats,flush=True)

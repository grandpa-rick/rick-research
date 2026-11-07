import sys; sys.path.insert(0,'../prove281')
from klperm import full_kl,L,MU,lmul,inv
from itertools import permutations
n=int(sys.argv[1]); W,P,mu=full_kl(n)
def word_from(w):
    w=tuple(w); wd=[]
    while True:
        D=L(w)
        if not D: return wd
        s=min(D); wd.append(s); w=lmul(s,w)
bad=0; tot=0; pbad=0
for K in [{1,2},{2,3},{1,2,3},{2,3,4},{1,3}]:
    K={k for k in K if k<n}
    # parabolic decomposition w = v u, v in W_K (left), u min in W_K w
    dec={}
    for w in W:
        u=w; v=[]
        while True:
            D=L(u)&K
            if not D: break
            s=min(D); u=lmul(s,u); v.append(s)
        # v as permutation: apply v-word to identity
        e=tuple(range(1,n+1)); vv=e
        for s in reversed(v): vv=lmul(s,vv)
        dec[w]=(vv,u)
    byu={}
    for w in W: byu.setdefault(dec[w][1],[]).append(w)
    for u,ws in byu.items():
        for a in ws:
            for b in ws:
                if a<b:
                    tot+=1
                    if MU(mu,a,b)!=MU(mu,dec[a][0],dec[b][0]): bad+=1
                    if P.get((a,b),[])!=P.get((dec[a][0],dec[b][0]),[]): pbad+=1
print(n,"layer pairs",tot,"mu mismatch",bad,"P mismatch",pbad)

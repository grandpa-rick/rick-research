# Is span{ D_I = sum_{Des(w) subset I} T_w } closed under Hecke multiplication at generic q?
import sys, itertools, sympy as sp
from fractions import Fraction as F
n=int(sys.argv[1]); q=F(int(sys.argv[2])) if len(sys.argv)>2 else F(3)
W=list(itertools.permutations(range(n)))
idx={w:i for i,w in enumerate(W)}
def inv(w): return sum(w[i]>w[j] for i in range(n) for j in range(i+1,n))
def rdes(w): return frozenset(i for i in range(n-1) if w[i]>w[i+1])
def ldes(w):
    p=[0]*n
    for k,a in enumerate(w): p[a]=k
    return frozenset(i for i in range(n-1) if p[i]>p[i+1])
def rmul_s(w,i): # w*s_i : swap positions
    w=list(w); w[i],w[i+1]=w[i+1],w[i]; return tuple(w)
def redword(w):
    w=list(w); word=[]
    while True:
        d=[i for i in range(n-1) if w[i]>w[i+1]]
        if not d: break
        i=d[0]; w[i],w[i+1]=w[i+1],w[i]; word.append(i)
    return word[::-1]   # w = s_{word[0]}...s_{word[-1]}
def times_s(vec,i): # right multiply by T_{s_i}
    out={}
    for w,c in vec.items():
        ws=rmul_s(w,i)
        if w[i]<w[i+1]: out[ws]=out.get(ws,0)+c
        else:
            out[w]=out.get(w,0)+(q-1)*c; out[ws]=out.get(ws,0)+q*c
    return out
def mult(a,b):
    out={}
    for v,cb in b.items():
        cur=dict(a)
        for i in redword(v): cur=times_s(cur,i)
        for w,c in cur.items(): out[w]=out.get(w,0)+c*cb
    return out
subsets=[frozenset(s) for r in range(n) for s in itertools.combinations(range(n-1),r)]
for name,des in (("rightDes",rdes),("leftDes",ldes)):
    D=[{w:F(1) for w in W if des(w)<=I} for I in subsets]
    M=sp.Matrix([[d.get(w,0) for w in W] for d in D]).T
    rank0=M.rank(); bad=0
    for a in D:
        for b in D:
            p=mult(a,b); v=sp.Matrix([p.get(w,0) for w in W])
            if M.row_join(v).rank()>rank0: bad+=1
    print(n,"q=",q,name,"dim",rank0,"products outside span:",bad,"of",len(D)**2)

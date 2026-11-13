import sys
exec(open('qsolomon.py').read().split("subsets=")[0])
import itertools, sympy as sp
subsets=[frozenset(s) for r in range(n) for s in itertools.combinations(range(n-1),r)]
def Tinv_s(vec,i): # right multiply by T_s^{-1} = q^{-1}T_s - (1-q^{-1})
    a=times_s(vec,i); out={w:c/q for w,c in a.items()}
    for w,c in vec.items(): out[w]=out.get(w,0)-(1-1/q)*c
    return out
def Tbar(w): # bar(T_w) = (T_{w^{-1}})^{-1}
    cur={tuple(range(n)):F(1)}
    for i in redword(w): cur=Tinv_s(cur,i)
    return cur
def closure_dim(gens):
    basis=[]; 
    def vec(d): return [d.get(w,0) for w in W]
    span=gens[:]
    M=sp.Matrix([vec(d) for d in span]); r=M.rank()
    while True:
        new=[]
        for a in span:
            for b in gens:
                p=mult(a,b); M2=M.col_join(sp.Matrix([vec(p)]))
                if M2.rank()>r: M=M2; r+=1; new.append(p)
        if not new: return r
        span+=new
for name,mk in (("T",lambda w:{w:F(1)}),("barT",Tbar)):
    gens=[]
    for I in subsets:
        d={}
        for w in W:
            if rdes(w)<=I:
                for k,c in mk(w).items(): d[k]=d.get(k,0)+c
        gens.append(d)
    print(n,name,"descent span closure dim under composition:",closure_dim(gens),"of",len(W))

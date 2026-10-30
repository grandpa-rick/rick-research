# PROVE 266 / Q53 check, written from the stated claims (not from draft code).
import numpy as np, itertools, math, sys
def group(gens):
    n=gens[0].shape[0]; g=np.arange(1,n+1)*np.pi/7+np.sqrt(np.arange(1,n+1))  # generic vector
    key=lambda M: tuple(np.round(M@g,6))
    I=np.eye(n); els=[I]; idx={key(I):0}; ln=[0]; frontier=[0]
    while frontier:
        nf=[]
        for a in frontier:
            for s in gens:
                M=els[a]@s; k=key(M)
                if k not in idx: idx[k]=len(els); els.append(M); ln.append(ln[a]+1); nf.append(idx[k])
        frontier=nf
    N=len(els); r=len(gens)
    R=[[idx[key(els[a]@s)] for s in gens] for a in range(N)]      # right mult by s_i
    Lm=[[idx[key(s@els[a])] for s in gens] for a in range(N)]     # left mult
    # reflections: conjugates w s w^-1
    refl=set()
    for a in range(N):
        inv=np.linalg.inv(els[a])
        for s in gens: refl.add(key(els[a]@s@inv))
    reflM=[]
    for a in range(N):
        if key(els[a]) in refl and ln[a]%2==1: reflM.append(els[a])
    # Bruhat lower sets as bitsets, via u -> ut with l(ut)<l(u)
    order=sorted(range(N),key=lambda a:ln[a]); low=[0]*N
    for a in order:
        b=1<<a
        for t in reflM:
            c=idx[key(els[a]@t)]
            if ln[c]<ln[a]: b|=low[c]
        low[a]=b
    return dict(els=els,idx=idx,key=key,ln=ln,R=R,L=Lm,low=low,N=N,r=r)
def le(G,u,w): return (G['low'][w]>>u)&1
def coset(G,z,J):
    seen={z}; st=[z]
    while st:
        a=st.pop()
        for j in J:
            b=G['R'][a][j]
            if b not in seen: seen.add(b); st.append(b)
    return seen
def check_general(G,name,Js=None,control=False):
    r=G['r']; bad=0; tot=0; ctl_bad=0
    Js=Js or [J for k in range(r+1) for J in itertools.combinations(range(r),k)]
    for J in Js:
        Wmin=[a for a in range(G['N']) if all(G['ln'][G['R'][a][j]]>G['ln'][a] for j in J)]
        for z in Wmin:
            C=coset(G,z,J)
            for w in range(G['N']):
                if not le(G,z,w): continue
                below=[u for u in C if le(G,u,w)]
                mx=[u for u in below if all(le(G,v,u) for v in below)]
                assert len(mx)==1, "Deodhar max fails"
                lhs=(mx[0]==z)
                rhs=all(not le(G,G['R'][z][j],w) for j in J)
                tot+=1; bad+=(lhs!=rhs); assert lhs==(below==[z])
                # control: left multiplication s z instead of z s
                rc=all(not le(G,G['L'][z][j],w) for j in J)
                ctl_bad+=(lhs!=rc)
    print(f"{name}: general criterion {tot} triples, {bad} failures; control (s z) disagreements {ctl_bad}")
    return bad
def cox(M):
    n=len(M); B=np.array([[ -math.cos(math.pi/M[i][j]) if M[i][j] else 1 for j in range(n)] for i in range(n)])
    gens=[]
    for i in range(n):
        S=np.eye(n)
        for k in range(n): S[i][k]-=2*B[i][k]   # s_i(a_k)=a_k-2B(a_i,a_k)a_i ; column k
        gens.append(S.T.T)
    # columns: image of alpha_k ; build matrix with S[:,k]
    out=[]
    for i in range(n):
        S=np.eye(n)
        for k in range(n): S[i,k]-=2*B[i][k]
        out.append(S)
    return out
def lin(ms):  # linear Coxeter diagram with labels ms between consecutive
    n=len(ms)+1; M=[[2]*n for _ in range(n)]
    for i in range(n): M[i][i]=1
    for i,mm in enumerate(ms): M[i][i+1]=M[i+1][i]=mm
    return M
tot_bad=0
for name,M in [("A3",lin([3,3])),("A4",lin([3,3,3])),("B3",lin([3,4])),("B4",lin([3,3,4])),("H3",lin([3,5])),("I2(5)",lin([5])),("I2(8)",lin([8]))]:
    tot_bad+=check_general(group(cox(M)),name)
D4=[[1,3,2,2],[3,1,3,3],[2,3,1,2],[2,3,2,1]]
tot_bad+=check_general(group(cox(D4)),"D4")
print("GENERAL TOTAL FAILURES",tot_bad)

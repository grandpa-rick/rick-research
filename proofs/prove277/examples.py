# PROVE 277: re-implement every displayed example of the expository note FROM THE PRINTED STATEMENTS.
# independent of prove275/276 code.
import itertools as it
INF=float('inf')
def sub(w,i): return [c for c in w if c in (i,i+1)]
def inv(w,i):  # subsequence (i+1)...i
    s=sub(w,i); return any(s[a]==i+1 and i in s[a+1:] for a in range(len(s)))
def qdata(w,i):  # (eps,phi) of word quasi-crystal, Def 1
    if inv(w,i): return (INF,INF)
    return (w.count(i+1), w.count(i))
def qe(w,i):
    if inv(w,i) or (i+1) not in w: return None
    k=w.index(i+1); return w[:k]+(i,)+w[k+1:]
def qf(w,i):
    if inv(w,i) or i not in w: return None
    k=len(w)-1-w[::-1].index(i); return w[:k]+(i+1,)+w[k+1:]
# crystal data on words (bracket i+1 with later i)
def cdata(w,i):
    st=0; eps=0
    # scan: i+1 is '(' , i is ')'
    opens=0; unm_close=0
    for c in w:
        if c==i+1: opens+=1
        elif c==i:
            if opens: opens-=1
            else: unm_close+=1
    return (opens, unm_close)  # eps = unmatched i+1, phi = unmatched i
def defect(w,i): return w.count(i+1)-cdata(w,i)[0]
def nbrackets(w,i): return w.count(i+1)-cdata(w,i)[0]
# Theorem A printed rule
def ruleA(u,v,i):
    eu,pu=qdata(u,i); ev,pv=qdata(v,i)
    if INF in (eu,ev) or (eu>0 and pv>0): return (INF,INF),None,None
    e = (qe(u,i)+v) if eu>0 else ((u+qe(v,i)) if ev>0 else None)
    f = (u+qf(v,i)) if pv>0 else ((qf(u,i)+v) if pu>0 else None)
    return (eu+ev,pu+pv),e,f
bad=0;tot=0
for n in (2,3,4):
  for m in range(0,4):
    for k in range(0,4-m if m<4 else 1):
      for u in it.product(range(1,n+1),repeat=m):
        for v in it.product(range(1,n+1),repeat=k):
          for i in range(1,n):
            tot+=1; w=u+v
            if ruleA(u,v,i)!=(qdata(w,i),qe(w,i),qf(w,i)): bad+=1
print("Thm A printed rule:",tot,"cases, failures",bad)
# swapped kill control
badc=0
for u in it.product((1,2),repeat=2):
  for v in it.product((1,2),repeat=2):
    eu,pu=qdata(u,1); ev,pv=qdata(v,1)
    dead_sw = INF in (eu,ev) or (pu>0 and ev>0)
    if dead_sw != (qdata(u+v,1)[0]==INF): badc+=1
print("control (swapped kill) n=2 |u|=|v|=2 failures:",badc)
# defect identity on words: delta(uv)=delta u+delta v+min(eps~u,phi~v)
bad=0
for u in it.product(range(1,4),repeat=3):
  for v in it.product(range(1,4),repeat=3):
    for i in (1,2):
      if defect(u+v,i)!=defect(u,i)+defect(v,i)+min(cdata(u,i)[0],cdata(v,i)[1]): bad+=1
print("defect identity on words |u|=|v|=3,n=3 failures:",bad)
# std, iDes, components
def std(w):
    order=sorted(range(len(w)),key=lambda p:(w[p],p)); s=[0]*len(w)
    for lab,p in enumerate(order): s[p]=lab+1
    return tuple(s)
def ides(s):
    pos={v:p for p,v in enumerate(s)}; return frozenset(k for k in range(1,len(s)) if pos[k+1]<pos[k])
def comps(n,N):
    W=list(it.product(range(1,n+1),repeat=N)); seen=set(); out=[]
    for w in W:
        if w in seen: continue
        C={w}; st=[w]
        while st:
            x=st.pop()
            for i in range(1,n):
                for y in (qe(x,i),qf(x,i)):
                    if y and y not in C: C.add(y); st.append(y)
        seen|=C; out.append(C)
    return out
ok=all(len({std(w) for w in C})==1 and len(C)==sum(1 for w in it.product(range(1,4),repeat=len(next(iter(C)))) if std(w)==std(next(iter(C)))) for C in comps(3,4))
print("Thm B: components = std classes (n=3,N=4):",ok)
# example C_21 in n=3 and the [2]^3 split
for C in comps(3,2):
    if std(next(iter(C)))==(2,1): print("C_21, n=3:",sorted(C),[ (w,[(i,qf(w,i)) for i in (1,2) if qf(w,i)]) for w in sorted(C)])
for w in [(2,1,1),(2,1,2)]:
    print(w,"crystal data i=1",cdata(w,1),"quasi",qdata(w,1),"std",std(w),"iDes",sorted(ides(std(w))))
# QSym in n vars via F_D
def comp_of(N,D):
    cuts=[0]+sorted(D)+[N]; return tuple(cuts[j+1]-cuts[j] for j in range(len(cuts)-1))
def F(alpha,n):
    N=sum(alpha); D=set(it.accumulate(alpha[:-1])); poly={}
    for b in it.combinations_with_replacement(range(1,n+1),N):
        if all(b[k-1]<b[k] for k in D):
            e=tuple(b.count(j) for j in range(1,n+1)); poly[e]=poly.get(e,0)+1
    return poly
def mul(p,q):
    r={}
    for a,x in p.items():
        for b,y in q.items():
            e=tuple(s+t for s,t in zip(a,b)); r[e]=r.get(e,0)+x*y
    return r
def add(*ps):
    r={}
    for p in ps:
        for a,x in p.items(): r[a]=r.get(a,0)+x
    return {a:x for a,x in r.items() if x}
n=4
print("F1*F2 == F3+F12+F21 (n=4):", mul(F((1,),n),F((2,),n))==add(F((3,),n),F((1,2),n),F((2,1),n)))
# Prop P on example: shuffles of sigma1=1, sigma2=12
taus=[t for t in it.permutations(range(1,4)) if std(t[:1])==(1,) and std(t[1:])==(1,2)]
print("shuffle set 1 ⋒ 12:",taus,[comp_of(3,ides(t)) for t in taus])
# Delta F_21 on cuts (Theorem C printed rule)
alpha=(2,1);N=3;D={2}
for k in range(N+1):
    D1={d for d in D if d<k}; D2={d-k for d in D if d>k}
    print(" cut k=%d:"%k, comp_of(k,D1) if k else (), comp_of(N-k,D2) if N-k else ())
# sharpness: gl2 det^-1 x det
def Qdata_abstract(wt,eps,i=0):  # quasification Def: alive iff eps == wt_{i+1}
    return eps if eps==wt[i+1] else INF
print("det^-1:",Qdata_abstract((-1,-1),0),"det:",Qdata_abstract((1,1),0),"det^-1⊗det:",Qdata_abstract((0,0),0))
# B(0,-1) ⊗ B(2,1): B(0,-1)={a:(0,-1) -> b:(-1,0)}, eps(a)=0,phi(a)=1, eps(b)=1,phi(b)=0
B=[((0,-1),0,1),((-1,0),1,0)]; Bp=[((2,1),0,1),((1,2),1,0)]
for (wx,ex,px) in B:
  for (wy,ey,py) in Bp:
    m=min(ex,py); wt=(wx[0]+wy[0],wx[1]+wy[1]); e=ex+ey-m
    dx=wx[1]-ex; dy=wy[1]-ey
    print("  x⊗y wt",wt,"eps~",e,"defects",dx,dy,"m",m,"-> Q(B⊗B') eps..",Qdata_abstract(wt,e),"; Q_B⊗..Q_B' dead" if (dx or dy) else "")
# s_21 = F_12+F_21, n=3
s21=add(F((1,2),3),F((2,1),3))
from collections import Counter
# s21 via SSYT count: monomial coeff of x1x2x3 should be 2, x1^2x2 is 1
print("s21 coeffs:",s21.get((1,1,1)),s21.get((2,1,0)),s21.get((1,2,0)))
# --- Theorem B source weight & Theorem C slice statement, from printed text ---
badB=0;badC=0;nC=0
for N in range(1,5):
  for s in it.permutations(range(1,N+1)):
    D=ides(s); al=comp_of(N,D)
    for n in range(len(al),5):
      C=[w for w in it.product(range(1,n+1),repeat=N) if std(w)==s]
      src=[w for w in C if all(qe(w,i) is None for i in range(1,n))]
      if len(src)!=1 or tuple(src[0].count(j) for j in range(1,n+1))!=al+(0,)*(n-len(al)): badB+=1
      for a in range(1,n):
        for k in range(N+1):
          sl=[w for w in C if sum(c<=a for c in w)==k]
          if not sl: continue
          s1=std(tuple(v for v in s if v<=k)); s2=std(tuple(v for v in s if v>k))
          if ides(s1)!={d for d in D if d<k} or ides(s2)!={d-k for d in D if d>k}: badC+=1
          img={(tuple(c for c in w if c<=a),tuple(c-a for c in w if c>a)) for w in sl}
          A=[u for u in it.product(range(1,a+1),repeat=k) if std(u)==s1]
          Bv=[v for v in it.product(range(1,n-a+1),repeat=N-k) if std(v)==s2]
          nC+=1
          if len(img)!=len(sl) or img!={(u,v) for u in A for v in Bv}: badC+=1
print("Thm B unique source weight = alpha padded, failures:",badB,"; Thm C psi bijection+iDes:",nC,"slices, failures",badC)

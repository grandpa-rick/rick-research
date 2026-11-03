# (1) split independent of T-first word; (2) exact tensor rule in adj cases:
#     e~_j acts on b+ iff eps_j(b+)=m > phi_j(b-) := eps_j(b-) - <h_j, wt(b-)>  (wt in Q_+);
# (3) A_n full classification match.
import sys
from lusztig import Model
n=int(sys.argv[1]); H=int(sys.argv[2]); REV=len(sys.argv)>3
M=Model(n); N=M.N
pos=M.roots(next(iter(M.words)))
simple=[tuple(1 if t==i else 0 for t in range(n)) for i in range(n)]
def add(x,y): return tuple(a+b for a,b in zip(x,y))
def closed(X): return all(add(x,y) not in pos or add(x,y) in X for x in X for y in X)
def eps(j,d,w):
    c=0
    while True:
        d=M.e(j,d,w)
        if d is None: return c
        c+=1
def pair(j,v): return sum(v[k]*(2 if k==j else (-1 if abs(k-j)==1 else 0)) for k in range(n))
cham={}
for w in sorted(M.words):
    R=M.roots(w)
    for k in range(N+1): cham.setdefault(frozenset(R[:k]),[]).append((w,k))
print("chambers",len(cham))
bad_indep=0; stats={'neg':[0,0],'adj':[0,0],'far':[0,0]}; rule_ok=rule_tot=0
for T,lst in cham.items():
    w,k=lst[0]; R=M.roots(w)
    data=[]
    def rec(i,cur,h):
        if i==N: data.append(tuple(cur)); return
        for m in range((H-h)//sum(R[i])+1): rec(i+1,cur+[m],h+m*sum(R[i]))
    rec(0,[],0)
    split=(lambda d:(d[:k]+tuple([0]*(N-k)), tuple([0]*k)+d[k:])) if REV else (lambda d:(tuple([0]*k)+d[k:], d[:k]+tuple([0]*(N-k))))
    # (1) independence: other T-first words give same pair of elements
    for (w2,k2) in lst[1:]:
        for d in data[::7]:
            d2=M.trans(d,w,w2)
            p2,m2=(tuple([0]*k)+d2[k:], d2[:k]+tuple([0]*(N-k)))
            p,mm=split(d)
            if M.trans(p,w,w2)!=p2 or M.trans(mm,w,w2)!=m2: bad_indep+=1
    for j in range(n):
        aj=simple[j]
        cls='neg' if aj in T else ('adj' if closed(set(T)|{aj}) else 'far')
        allloc=True
        for d in data:
            ed=M.e(j,d,w)
            if ed is None: continue
            bp,bm=split(d); cp,cm=split(ed); ep=M.e(j,bp,w); em=M.e(j,bm,w)
            onm = (cp==bp and em is not None and cm==em); onp=(cm==bm and ep is not None and cp==ep)
            if not(onm or onp): allloc=False
            if cls=='adj':
                wtm=[0]*n
                for r,c in zip(R,bm):
                    for t in range(n): wtm[t]+=r[t]*c
                phi=eps(j,bm,w)-pair(j,wtm); m=eps(j,bp,w)
                pred_p = m>phi
                rule_tot+=1; rule_ok+= (onp if pred_p else onm)
        stats[cls][0]+=1; stats[cls][1]+= (allloc==(cls!='far'))
print("indep failures",bad_indep)
print("classification match (cls: [pairs, matches])",stats)
print("adj tensor rule b- (x) b+ :",rule_ok,"/",rule_tot)

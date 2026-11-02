import sys, itertools
from lusztig import Model
n=int(sys.argv[1]); H=int(sys.argv[2]); BREAK=len(sys.argv)>3
M=Model(n); N=M.N
def ht(r): return sum(r)
# all chambers: T = initial segments of length k of words = inversion sets; collect distinct T with a word having T first
cham={}
for w in M.words:
    R=M.roots(w)
    for k in range(N+1):
        T=frozenset(R[:k])
        if T not in cham: cham[T]=(w,k)
pos=M.roots(next(iter(M.words)))
simple=[tuple(1 if t==i else 0 for t in range(n)) for i in range(n)]
def closed(X):
    return all(tuple(a+b for a,b in zip(x,y)) not in pos or tuple(a+b for a,b in zip(x,y)) in X for x in X for y in X)
def biconvex(X):
    Y=set(pos)-set(X); return closed(X) and closed(Y)
print("chambers",len(cham))
summary=[]
for T,(w,k) in sorted(cham.items(),key=lambda t:(len(t[0]),sorted(t[0]))):
    R=M.roots(w)
    # data of height<=H in word w
    data=[]
    def rec(i,cur,h):
        if i==N: data.append(tuple(cur)); return
        for m in range((H-h)//ht(R[i])+1): rec(i+1,cur+[m],h+m*ht(R[i]))
    rec(0,[],0)
    split=lambda d:(tuple([0]*k)+d[k:], d[:k]+tuple([0]*(N-k)))   # (b_+ = S-part, b_- = T-part)
    if BREAK:  # negative control: swap roles (claim T-part is b_+)
        split=lambda d:(d[:k]+tuple([0]*(N-k)), tuple([0]*k)+d[k:])
    for j in range(n):
        aj=simple[j]
        if aj in T: cls='neg'
        else: cls='adj' if biconvex(set(T)|{aj}) else 'far'
        tot=loc=onp=onm=0; ex=None
        for d in data:
            ed=M.e(j,d,w)
            if ed is None: continue
            tot+=1
            bp,bm=split(d); cp,cm=split(ed)
            ep=M.e(j,bp,w); em=M.e(j,bm,w)
            if cp==bp and cm==em and em is not None: loc+=1; onm+=1
            elif cm==bm and cp==ep and ep is not None: loc+=1; onp+=1
            elif ex is None: ex=(d,ed)
        ok=(loc==tot)
        pred=(cls!='far')
        summary.append((cls,ok==pred))
        print(f"T={sorted(T)} j={j+1} {cls}: local {loc}/{tot} (b+:{onp}, b-:{onm}) {'MATCH' if ok==pred else 'MISMATCH'}" + (f"  ex {ex[0]}->{ex[1]} word {w}" if ex and cls!='far' else ""))
from collections import Counter
print(Counter(summary))

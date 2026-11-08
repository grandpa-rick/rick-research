"""Step 2: size of Bruhat interval [x,z] in S_n by downward BFS through Bruhat covers, restricted to y>=x. Capped."""
import sys,json
def length(w): return sum(1 for i in range(len(w)) for j in range(i+1,len(w)) if w[i]>w[j])
def rankmat(w):
    n=len(w); R=[]
    for k in range(1,n):
        s=sorted(w[:k]); R.append(s)
    return R
def geq_x(y,Rx):
    # y >= x  iff for each k sorted(y[:k]) dominates sorted(x[:k]) entrywise
    n=len(y)
    for k in range(1,n):
        b=sorted(y[:k]); a=Rx[k-1]
        for p,q in zip(a,b):
            if p>q: return False
    return True
def covers_down(w):
    n=len(w); out=[]
    for i in range(n):
        wi=w[i]; m=-1  # max value seen between, below wi
        for j in range(i+1,n):
            wj=w[j]
            if wj<wi and wj>m:
                v=list(w); v[i],v[j]=wj,wi; out.append(tuple(v)); m=wj
    return out
def interval(x,z,cap=5_000_000,verbose=True):
    Rx=rankmat(x); x=tuple(x); level={tuple(z)}; sizes=[1]; tot=1
    while level:
        nxt=set()
        for w in level:
            for v in covers_down(w):
                if v not in nxt and geq_x(v,Rx): nxt.add(v)
        if not nxt: break
        sizes.append(len(nxt)); tot+=len(nxt); level=nxt
        if verbose: print(' level',len(sizes)-1,len(nxt),'tot',tot,flush=True)
        if tot>cap: return tot,sizes,False
    return tot,sizes,True
if __name__=='__main__':
    # sanity: [e,w0] in S_4 = 24, S_5 = 120
    for n in (4,5):
        t,s,_=interval(list(range(1,n+1)),list(range(n,0,-1)),verbose=False); print('S',n,t,s)

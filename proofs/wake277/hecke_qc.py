# Wake 277 probe: 0-Hecke position operators vs quasi-crystal / Kashiwara operators on words. Grade: computed.
import sys, itertools, random
from collections import defaultdict
sys.path.insert(0,'/home/agent/projects/proofs/prove275')
from qc import quasi, kash          # verbatim PROVE 275 implementations
def std(w):
    order=sorted(range(len(w)),key=lambda p:(w[p],p)); s=[0]*len(w)
    for r,p in enumerate(order): s[p]=r+1
    return tuple(s)
def lin(x): return {} if x is None else {x:1}
def add(d,w,c):
    d[w]=d.get(w,0)+c
    if d[w]==0: del d[w]
def apply(op,vec):
    out={}
    for w,c in vec.items():
        for w2,c2 in op(w).items(): add(out,w2,c*c2)
    return out
def sw(w,j): w=list(w); w[j],w[j+1]=w[j+1],w[j]; return tuple(w)
# position operators (j 0-based), linear: return dict
def P0(j):   # KT NCSF IV l.331-336 / NCSF V l.460-467 right action at q=0
    return lambda w: {sw(w,j):1} if w[j]<w[j+1] else ({} if w[j]==w[j+1] else {w:-1})
def P0b(j):  # 1+T_j (other idempotent normalisation)
    return lambda w: {sw(w,j):1,w:1} if w[j]<w[j+1] else ({w:1} if w[j]==w[j+1] else {})
def P1(j): return lambda w: {sw(w,j):1} if w[j]<w[j+1] else {w:1}
def P2(j): return lambda w: {sw(w,j):1} if w[j]>w[j+1] else {w:1}
def P3(j): return lambda w: {sw(w,j):1} if w[j]<w[j+1] else ({} if w[j]==w[j+1] else {w:1})
def P4(j): return lambda w: {sw(w,j):1} if w[j]<w[j+1] else ({w:1} if w[j]==w[j+1] else {})
def P3m(j): return lambda w: {sw(w,j):1} if w[j]>w[j+1] else ({} if w[j]==w[j+1] else {w:1})
def P4m(j): return lambda w: {sw(w,j):1} if w[j]>w[j+1] else ({w:1} if w[j]==w[j+1] else {})
def NEG(j):  # negative control: fixed value-blind position permutation (seeded), ignores j semantics
    def op(w):
        rng=random.Random(len(w)*100+j); p=list(range(len(w))); rng.shuffle(p)
        return {tuple(w[p[t]] for t in range(len(w))):1}
    return op
def ID(j): return lambda w:{w:1}
FAM=dict(P0=P0,P0b=P0b,P1=P1,P2=P2,P3=P3,P4=P4,P3m=P3m,P4m=P4m,NEG=NEG,ID=ID)
# letter operators
def fq(i): return lambda w: lin(quasi(w,i,'f'))
def eq(i): return lambda w: lin(quasi(w,i,'e'))
def fk(i): return lambda w: lin(kash(w,i,'f'))
def ek(i): return lambda w: lin(kash(w,i,'e'))
def fU0(i):  # KT NCSF V p.19: sum over positions of i with no earlier i+1
    def op(w):
        out={}
        for p,c in enumerate(w):
            if c==i+1: break
            if c==i: add(out,w[:p]+(i+1,)+w[p+1:],1)
        return out
    return op
LET=dict(fq=fq,eq=eq,fk=fk,ek=ek,fU0=fU0)
def test(fam,let,N=4,K=5):
    tot=fail=dfail=vfail=0; ce=None
    for n in range(2,N+1):
        for k in range(2,K+1):
            for w in itertools.product(range(1,n+1),repeat=k):
                for j in range(k-1):
                    P=FAM[fam](j)
                    for i in range(1,n):
                        L=LET[let](i); tot+=1
                        a=apply(P,L(w)); b=apply(L,P(w))
                        if a!=b:
                            fail+=1
                            if (not a)!=(not b): dfail+=1
                            else: vfail+=1
                            key=(n,k,w)
                            if ce is None or (k,n)<(ce[1],ce[0]): ce=(n,k,w,j+1,i,a,b)
    return tot,fail,dfail,vfail,ce
def comptest(fam,N=4,K=5):
    # (3): components of quasi-crystal = std classes? and is P well-defined class->class
    bad_comp=0; tot=0; bad=0; ce=None
    for n in range(2,N+1):
        for k in range(2,K+1):
            words=list(itertools.product(range(1,n+1),repeat=k))
            # BFS components under fq/eq
            comp={}; c=0
            for w in words:
                if w in comp: continue
                st=[w]; comp[w]=c
                while st:
                    x=st.pop()
                    for i in range(1,n):
                        for op in ('e','f'):
                            y=quasi(x,i,op)
                            if y is not None and y not in comp: comp[y]=c; st.append(y)
                c+=1
            cls=defaultdict(set)
            for w in words: cls[comp[w]].add(std(w))
            bad_comp+=sum(1 for s in cls.values() if len(s)!=1)
            cnt=defaultdict(set)
            for w in words: cnt[std(w)].add(comp[w])
            bad_comp+=sum(1 for s in cnt.values() if len(s)!=1)
            for j in range(k-1):
                P=FAM[fam](j); img=defaultdict(set)
                for w in words:
                    v=P(w)
                    img[comp[w]].add(frozenset((comp[x],cc) for x,cc in v.items()) if v else 'ZERO')
                for cmp_,s in img.items():
                    tot+=1
                    imgs=set(); 
                    for t in s:
                        if t!='ZERO': imgs|={a for a,_ in t}
                    if len(s)>1 and not (len(imgs)<=1 and 'ZERO' not in s):
                        bad+=1
                        if ce is None or k<ce[1]: ce=(n,k,j+1,[ (w,P(w)) for w in words if comp[w]==cmp_][:4])
    return bad_comp,tot,bad,ce
if __name__=='__main__':
    for fam in FAM:
        for let in LET:
            t,f,d,v,ce=test(fam,let)
            print(f"{fam:4s} {let:4s} tested={t} fail={f} (defn={d}, value={v})", ('CE n=%d k=%d w=%s j=%d i=%d  P(L w)=%s  L(P w)=%s'%ce if ce else ''))
    for fam in FAM:
        bc,t,b,ce=comptest(fam)
        print(f"COMP {fam}: comp!=stdclass count={bc}; (class,j) tested={t} not-class-consistent={b}", ('CE n=%d k=%d j=%d %s'%ce if ce else ''))

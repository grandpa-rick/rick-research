"""Independent re-check of Q76-T' n=8 violation: rsk_inv construction of x_Q,y_Q from (P1,P2), klperm recursion on lower ideal."""
exec(open('q76t_verify.py').read().split("P1=((1,3,6)")[0])
import sys
def syt(shape):
    n=sum(shape); out=[]
    def rec(T,k):
        if k>n: out.append(tuple(map(tuple,T))); return
        for r in range(len(shape)):
            if len(T[r])<shape[r] and (r==0 or len(T[r-1])>len(T[r])):
                T[r].append(k); rec(T,k+1); T[r].pop()
    rec([[] for _ in shape],1); return out
P1=((1,3,5,7),(2,4,6,8)); C=(1,4,2,6,3,7,5,8)
x0=rsk_inv(P1,P1); P2=rsk(tuple(C[v-1] for v in x0))[0]; print("P2",P2)
import collections
res=collections.Counter()
for Q in syt((4,4)):
    x=rsk_inv(P1,Q); y=rsk_inv(P2,Q); assert rsk(x)==(P1,Q) and rsk(y)==(P2,Q)
    c=tuple(y[x.index(v)] for v in range(1,9))
    p,d=kl_pair(x,y)
    print(Q,''.join(map(str,x)),''.join(map(str,y)),"c=",''.join(map(str,c)),"le",bruhat_le(x,y),"ldiff",d,"P",p,flush=True)
    res[p]+=1
print(res)

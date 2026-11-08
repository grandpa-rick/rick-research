# prove284: link the independently-replayed pair in0 to in0b (dyer2 ext pair of cert 353),
# and the w0-mirror of in0 to in1b (ext pair of cert 364), by explicit simultaneous right-star paths.
from itertools import combinations
from collections import deque
n=16
def rd(f):
    L=open('/home/agent/projects/proofs/prove283/'+f).read().split(); m=int(L[0]); v=list(map(int,L[1:])); return v[:m],v[m:2*m]
def ln(w): return sum(w[i]>w[j] for i,j in combinations(range(n),2))
def ldes(w):
    p=[0]*(n+2)
    for k,a in enumerate(w): p[a]=k
    return {i for i in range(1,n) if p[i+1]<p[i]}
def sw(i,w): return [i+1 if a==i else (i if a==i+1 else a) for a in w]
def inverse(w):
    r=[0]*n
    for k,a in enumerate(w): r[a-1]=k+1
    return r
def lstar(i,w):
    A=ldes(w)&{i,i+1}
    if len(A)!=1: return None
    c=[y for y in (sw(i,w),sw(i+1,w)) if len(ldes(y)&{i,i+1})==1 and (ldes(y)&{i,i+1})!=A]
    assert len(c)==1; return c[0]
def rstar(i,w):
    v=lstar(i,inverse(w)); return None if v is None else inverse(v)
def ins(w):
    P=[];Q=[]
    for k,x in enumerate(w,1):
        r=0
        while True:
            if r==len(P): P.append([x]);Q.append([k]);break
            big=[y for y in P[r] if y>x]
            if not big: P[r].append(x);Q[r].append(k);break
            y=min(big); P[r][P[r].index(y)]=x; x=y; r+=1
    return P,Q
def mirror(w): return [n+1-w[n-1-k] for k in range(n)]
def bfs(a,b,ta,tb):
    st=(tuple(a),tuple(b)); seen={st:None}; dq=deque([st])
    while dq:
        u=dq.popleft()
        if u==(tuple(ta),tuple(tb)):
            path=[]
            while seen[u] is not None: u,i=seen[u]; path.append(i)
            return path[::-1]
        for i in range(1,n-1):
            x=rstar(i,list(u[0]))
            if x is None: continue
            y=rstar(i,list(u[1])); assert y is not None
            v=(tuple(x),tuple(y))
            if v not in seen: seen[v]=(u,i); dq.append(v)
    return None
x0,z0=rd('in0.txt'); x0b,z0b=rd('in0b.txt'); x1b,z1b=rd('in1b.txt')
print('in0 P==in0b P:',ins(x0)[0]==ins(x0b)[0],ins(z0)[0]==ins(z0b)[0])
p=bfs(x0,z0,x0b,z0b); print('in0 -> in0b right-star path:',p)
mx,mz=mirror(x0),mirror(z0)
print('lengths in0',ln(x0),ln(z0),'mirror',ln(mx),ln(mz),'in1b',ln(x1b),ln(z1b))
print('mirror P == in1b P:',ins(mx)[0]==ins(x1b)[0],ins(mz)[0]==ins(z1b)[0])
p2=bfs(mx,mz,x1b,z1b); print('mirror(in0) -> in1b right-star path:',p2)

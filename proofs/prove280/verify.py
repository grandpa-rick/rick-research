"""Independent replay of certs (no shared code): rank-matrix Bruhat, own RSK, own star, own SYT enumeration."""
import json,sys
from itertools import combinations
D=json.load(open(sys.argv[1])); n=14
def ln(w): return sum(w[i]>w[j] for i,j in combinations(range(n),2))
def ldes(w):
    p=[0]*(n+2)
    for k,a in enumerate(w): p[a]=k
    return {i for i in range(1,n) if p[i+1]<p[i]}
def sw(i,w): return [i+1 if a==i else (i if a==i+1 else a) for a in w]
def leq(u,w):  # rank matrix: #{k<=i: u(k)>=j} <= same for w
    for i in range(1,n+1):
        for j in range(1,n+1):
            if sum(1 for k in range(i) if u[k]>=j) > sum(1 for k in range(i) if w[k]>=j): return False
    return True
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
def star(i,w):
    A=ldes(w)&{i,i+1}; assert len(A)==1
    c=[y for y in (sw(i,w),sw(i+1,w)) if len(ldes(y)&{i,i+1})==1 and (ldes(y)&{i,i+1})!=A]
    assert len(c)==1; return c[0]
x,z=D['x'],D['z']; Lx,Lz=ldes(x),ldes(z); Q=ins(x)[1]
assert ins(z)[1]==Q and x!=z and Lz<=Lx, 'twin precondition'
print('L(x)',sorted(Lx),'L(z)',sorted(Lz),'l(x)',ln(x),'l(z)',ln(z),'shape',[len(r) for r in Q])
# all y in the cell adjacent by one left mult with L(y) not in L(x)
need=[]
for s in range(1,n):
    y=sw(s,x)
    if ins(y)[1]==Q and not ldes(y)<=Lx: need.append((s,y))
print('y=sx in cell with L(y)!<=L(x):',[s for s,_ in need])
assert sorted(map(lambda t:tuple(t[1]),need))==sorted(tuple(c['y']) for c in D['certs'])
for c in D['certs']:
    a,b=list(c['y']),list(z)
    for i in c['path']: a,b=star(i,a),star(i,b)
    la,lb=ln(a),ln(b); lo,hi=(a,b) if la<lb else (b,a)
    ok=abs(la-lb)==1 and leq(lo,hi)
    print(' s=%d path-len %d end lengths %d,%d  comparable-gap1: %s'%(c['s'],len(c['path']),la,lb,ok)); assert ok
# no y in cell with L(y) strictly containing L(x): enumerate SYT of the shape
shape=[len(r) for r in Q]
def syts(shape):
    res=[]
    def rec(T,k):
        if k>n: res.append([r[:] for r in T]); return
        for r in range(len(shape)):
            if len(T[r])<shape[r] and (r==0 or len(T[r-1])>len(T[r])):
                T[r].append(k); rec(T,k+1); T[r].pop()
    rec([[] for _ in shape],1); return res
def des(T):
    row={v:r for r,R in enumerate(T) for v in R}; return {i for i in range(1,n) if row[i+1]>row[i]}
cnt=sum(1 for T in syts(shape) if des(T)>Lx)
print('#SYT with Des strictly containing L(x):',cnt, ' total SYT',len(syts(shape)))
print('VERIFIED' if cnt==0 else 'CHECK y<x CASE')

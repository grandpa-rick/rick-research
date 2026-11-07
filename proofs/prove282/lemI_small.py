"""Test 'interior kill' Lemma I: y~_L z (same left cell = same Q), nonempty L(z) subset int L(y) => mu(y,z)=0. Full KL S_n."""
import sys; sys.path.insert(0,'../prove281')
from klperm import full_kl,L,MU
n=int(sys.argv[1])
def rsk(w):
    P=[];Q=[]
    for k,a in enumerate(w,1):
        r=0
        while True:
            if r==len(P): P.append([a]);Q.append([k]);break
            row=P[r]; j=next((j for j,b in enumerate(row) if b>a),None)
            if j is None: row.append(a);Q[r].append(k);break
            row[j],a=a,row[j]; r+=1
    return tuple(map(tuple,P)),tuple(map(tuple,Q))
def intr(A): return {i for i in A if (i-1 in A or i==1) and (i+1 in A or i==n-1)}
W,P,mu=full_kl(n)
# check convention: L(w) = Des P(w)? 
def des(T):
    row={v:k for k,R in enumerate(T) for v in R}; return {i for i in range(1,n) if row[i+1]>row[i]}
RS={w:rsk(w) for w in W}
bad=sum(1 for w in W if L(w)!=des(RS[w][0])); print('L=DesP violations',bad)
cells={}
for w in W: cells.setdefault(RS[w][1],[]).append(w)
hit=0;viol=[];nest=0
for Q,C in cells.items():
    for y in C:
        Ly=L(y); I=intr(Ly)
        for z in C:
            Lz=L(z)
            if z==y or not Lz: continue
            if Lz<Ly and MU(mu,y,z): nest+=1
            if Lz<=I and Lz!=Ly:
                hit+=1
                if MU(mu,y,z): viol.append((y,z,sorted(Ly),sorted(Lz)))
print('n',n,'nested mu-edges',nest,'interior configs',hit,'violations',len(viol)); print(viol[:10])

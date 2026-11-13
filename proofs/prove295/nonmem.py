"""Exact non-membership test: beta = (proj to weight mu1) then h.  If beta in A then
(d1 h, 0) lies in span{(d1.x, d2.x) : x in 0-Hecke monoid}, d_i = D-words of weights mu1 != mu2.
Also checks d1 h != 0.  Exact over Z."""
import sys
from collections import defaultdict
from flint import fmpz_mat
from split import move, act_pibar, w0word
def run(n,N):
    L=N-2*n; pre=tuple(range(1,n+1))
    d1=pre+tuple([1]*L)+pre; d2=pre+tuple([2]+[1]*(L-1))+pre
    hword=w0word(range(1,n))+w0word(range(N-n+1,N))
    vec={d1:1}
    for i in hword: vec=act_pibar(vec,i)
    # orbit of the pair under the monoid: states (u1,u2) words
    st=(d1,d2); O={st}; fr=[st]
    while fr:
        nf=[]
        for (a,b) in fr:
            for i in range(1,N):
                s=(move(a,i),move(b,i))
                if s not in O: O.add(s); nf.append(s)
        fr=nf
    keys=sorted({('1',a) for a,b in O}|{('2',b) for a,b in O}|{('1',w) for w in vec})
    ix={k:j for j,k in enumerate(keys)}
    rows=[]
    for (a,b) in O:
        r=[0]*len(keys); r[ix[('1',a)]]+=1; r[ix[('2',b)]]+=1; rows.append(r)
    t=[0]*len(keys)
    for w,c in vec.items(): t[ix[('1',w)]]+=c
    r0=fmpz_mat(rows).rank(); r1=fmpz_mat(rows+[t]).rank()
    print(n,N,'d1',d1,'d2',d2,'|d1 h| terms',len(vec),'orbit pairs',len(O),'beta notin A:',r1==r0+1,flush=True)
for a in sys.argv[1:]:
    n,N=map(int,a.split(',')); run(n,N)

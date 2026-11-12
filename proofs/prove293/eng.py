# independent NSym engine: S-basis, ribbons, derivations D_m; plus rewriting formulas
import itertools
from fractions import Fraction
from collections import defaultdict
def comp2word(a): # parts -> r inside, u between
    return 'u'.join('r'*(p-1) for p in a)
def word2comp(w):
    parts=[1]
    for c in w:
        if c=='r': parts[-1]+=1
        else: parts.append(1)
    return tuple(parts)
def coarsenings(a):
    n=len(a)
    for mask in range(1<<(n-1)):
        b=[a[0]]
        for i in range(1,n):
            if mask>>(i-1)&1: b[-1]+=a[i]
            else: b.append(a[i])
        yield tuple(b), n-len(b)
def R_in_S(a):
    d=defaultdict(int)
    for b,k in coarsenings(a): d[b]+=(-1)**k
    return d
def D(m,X):  # derivation on S-words
    out=defaultdict(int)
    for b,c in X.items():
        for i,p in enumerate(b):
            if p>=m:
                nb=b[:i]+((p-m,) if p>m else ())+b[i+1:]
                out[nb]+=c
    return {k:v for k,v in out.items() if v}
def S_to_R(X): # S^b = sum over coarsenings a of b of R_a
    out=defaultdict(int)
    for b,c in X.items():
        if len(b)==0: out[()]+=c; continue
        for a,k in coarsenings(b): out[a]+=c
    return {k:v for k,v in out.items() if v}
def comps(n):
    if n==0: yield (); return
    for f in range(1,n+1):
        for r in comps(n-f): yield (f,)+r
# rewriting formulas on padded words
def valid(P): return len(P)>=2 and P[0]=='r' and P[-1]=='u'
def A_rw(s):
    P='r'+s+'u'; out=defaultdict(int)
    for i in range(len(P)-2):
        w=P[i:i+3]
        if w[0]=='r' and w[2]=='u':
            sg=1 if w[1]=='r' else -1
            for y in 'ru':
                Q=P[:i]+y+P[i+3:]
                if valid(Q): out[Q[1:-1]]+=sg
    return {k:v for k,v in out.items() if v}
def B_rw(s):
    P='r'+s+'u'; out=defaultdict(int)
    cor=[i for i in range(len(P)-1) if P[i:i+2]=='ru']
    for a in range(len(cor)):
        for b in range(a+1,len(cor)):
            i,j=cor[a],cor[b]
            for y in 'ru':
                for z in 'ru':
                    Q=P[:i]+y+P[i+2:j]+z+P[j+2:]
                    if valid(Q): out[Q[1:-1]]+=1
    for i in range(len(P)-2):
        if P[i:i+3]=='ruu':
            for y in 'ru':
                Q=P[:i]+y+P[i+3:]
                if valid(Q): out[Q[1:-1]]+=1
    return {k:v for k,v in out.items() if v}
def AB_true(s):
    X=R_in_S(word2comp(s))
    A=S_to_R(D(2,X)); D11=S_to_R(D(1,D(1,X)))
    B={k:Fraction(D11.get(k,0)-A.get(k,0),2) for k in set(A)|set(D11)}
    A={comp2word(k):v for k,v in A.items()}
    B={comp2word(k):v for k,v in B.items() if v}
    return A,B
if __name__=='__main__':
    bad=0;n=0
    for L in range(1,10):
        for s in map(''.join,itertools.product('ru',repeat=L)):
            A,B=AB_true(s); n+=1
            if A!=A_rw(s) or B!={k:Fraction(v) for k,v in B_rw(s).items()}:
                bad+=1
                if bad<5: print(s,A,A_rw(s),B,B_rw(s))
    print('checked',n,'bad',bad)

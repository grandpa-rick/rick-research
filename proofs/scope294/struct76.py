import sys
from collections import defaultdict, Counter
from klfast import full_kl_fast, unpack, inv
from q76t_s7 import rsk
def mul(a,b): return tuple(a[b[i]-1] for i in range(len(a)))
def invp(a):
    r=[0]*len(a)
    for i,v in enumerate(a): r[v-1]=i+1
    return tuple(r)
def sj(j,n): s=list(range(1,n+1)); s[j-1],s[j]=s[j],s[j-1]; return tuple(s)
n=int(sys.argv[1])
W=None
from itertools import permutations
W=list(permutations(range(1,n+1)))
R={w:rsk(w) for w in W}
byP=defaultdict(list)
for w in W: byP[R[w][0]].append(w)
# key good: for all x in K(P1): Q(cx)=Q(x), P(cx)=P2 const, l additive
def isgood(c,P1):
    K=byP[P1]; P2=None; lc=inv(c)
    for x in K:
        y=mul(c,x)
        if R[y][1]!=R[x][1] or inv(y)!=inv(x)+lc: return None
        if P2 is None: P2=R[y][0]
        elif R[y][0]!=P2: return None
    return P2
# enumerate all good (c,P1)
good={}
for P1 in byP:
    for c in W:
        P2=isgood(c,P1)
        if P2 is not None: good[(c,P1)]=P2
print("good (c,P1):",len(good))
# star-path test: c good is 'star-factorizable' if c=e or exists j with s_j c < c... use right factor: c = c' s_j, s_j x applied first
memo={}
def fact(c,P1):
    if inv(c)==0: return True
    k=(c,P1)
    if k in memo: return memo[k]
    r=False
    for j in range(1,n):
        cp=mul(c,sj(j,n))   # c = cp * s_j, first apply s_j to x
        if inv(cp)==inv(c)-1 and (sj(j,n),P1) in good:
            P1b=good[(sj(j,n),P1)]
            if (cp,P1b) in good and fact(cp,P1b): r=True;break
    memo[k]=r; return r
nf=[k for k in good if not fact(*k)]
print("not star-factorizable:",len(nf), Counter(inv(c) for c,_ in nf))
for c,P1 in nf[:10]: print("  c=",''.join(map(str,c)),"P1=",P1,"P2=",good[(c,P1)])

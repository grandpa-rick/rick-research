from fractions import Fraction as Q
M=40    # z-truncation
# elements of Q(w): (p,q) = p+q*w, w^2=-1-w
def cmul(x,y):
    p1,q1=x; p2,q2=y
    return (p1*p2-q1*q2, p1*q2+q1*p2-q1*q2)
Z=(Q(0),Q(0)); ONE=(Q(1),Q(0)); W=(Q(0),Q(1)); W2=(Q(-1),Q(-1))
def smul(A,B):
    R=[Z]*M
    for i,x in enumerate(A):
        if x==Z: continue
        for j in range(M-i):
            if B[j]!=Z:
                a,b=R[i+j]; c,d=cmul(x,B[j]); R[i+j]=(a+c,b+d)
    return R
def sadd(A,B): return [(a[0]+b[0],a[1]+b[1]) for a,b in zip(A,B)]
def sneg(A): return [(-a[0],-a[1]) for a in A]
def sinv(A):
    a0=A[0]; assert a0!=Z
    # inverse of p+qw : conj = p+q*w^2 = (p-q) - q w ; norm = p^2-pq+q^2
    p,q=a0; n=p*p-p*q+q*q; i0=((p-q)/n, -q/n)
    B=[Z]*M; B[0]=i0
    for k in range(1,M):
        s=Z
        for j in range(1,k+1):
            if A[j]!=Z:
                c,d=cmul(A[j],B[k-j]); s=(s[0]+c,s[1]+d)
        B[k]=cmul((-s[0],-s[1]),i0)
    return B
def sconst(c):
    A=[Z]*M; A[0]=c; return A
zser=[Z]*M; zser[1]=ONE
wp=[ONE,W,W2]
nu=[[Z]*M for _ in range(3)]
E=[Z]*M
for it in range(M+2):
    for i in range(3):
        den=sadd(sadd(sconst(ONE),sneg(E)),nu[i])
        nu[i]=smul(smul([ (cmul(wp[i],x)) for x in zser],sconst(ONE)), sinv(den))
    E=sadd(sadd(nu[0],nu[1]),nu[2])
print("E = e1(nu):")
for k in range(M):
    if E[k]!=Z: print("  z^%d : %s + %s w"%(k,E[k][0],E[k][1]))
import json
d=json.load(open('/home/agent/projects/beta-prime/code/day147_gauss/data.json'))
b=[0]+[int(x) for x in d['b']]
print("\nb_k for comparison:", b[1:6])

# Verify the elimination chain of section 6 directly on the series solution of (*)
from fractions import Fraction as Q
import json
M=40
def cmul(x,y):
    p1,q1=x;p2,q2=y
    return (p1*p2-q1*q2, p1*q2+q1*p2-q1*q2)
Z=(Q(0),Q(0));ONE=(Q(1),Q(0));W=(Q(0),Q(1));W2=(Q(-1),Q(-1))
def smul(A,B):
    R=[Z]*M
    for i,x in enumerate(A):
        if x==Z: continue
        for j in range(M-i):
            if B[j]!=Z:
                a,b=R[i+j];c,d=cmul(x,B[j]);R[i+j]=(a+c,b+d)
    return R
def sadd(*As):
    R=[Z]*M
    for A in As: R=[(a[0]+b[0],a[1]+b[1]) for a,b in zip(R,A)]
    return R
def sneg(A): return [(-a[0],-a[1]) for a in A]
def sscal(c,A): return [(c*a[0],c*a[1]) for a in A]
def sinv(A):
    p,q=A[0];n=p*p-p*q+q*q;i0=((p-q)/n,-q/n)
    B=[Z]*M;B[0]=i0
    for k in range(1,M):
        s=Z
        for j in range(1,k+1):
            if A[j]!=Z:
                c,d=cmul(A[j],B[k-j]);s=(s[0]+c,s[1]+d)
        B[k]=cmul((-s[0],-s[1]),i0)
    return B
def sconst(c):
    A=[Z]*M;A[0]=c;return A
zser=[Z]*M;zser[1]=ONE
wp=[ONE,W,W2]
nu=[[Z]*M for _ in range(3)];E=[Z]*M
for it in range(M+2):
    for i in range(3):
        den=sadd(sconst(ONE),sneg(E),nu[i])
        nu[i]=smul([cmul(wp[i],x) for x in zser], sinv(den))
    E=sadd(*nu)
A=sadd(E,sconst((Q(-1),Q(0))))
R=[sadd(sscal(2,nu[i]),sneg(A)) for i in range(3)]
# 1. R_i^2 = A^2+4 w^i z
for i in range(3):
    lhs=smul(R[i],R[i]); rhs=sadd(smul(A,A), sscal(4,[cmul(wp[i],x) for x in zser]))
    print("  R_%d^2 = A^2+4w^%d z :"%(i,i), lhs==rhs)
e1R=sadd(*R)
e2R=sadd(smul(R[0],R[1]),smul(R[0],R[2]),smul(R[1],R[2]))
e3R=smul(smul(R[0],R[1]),R[2])
print("  e1(R) = 2-A :", e1R==sadd(sconst((Q(2),Q(0))),sneg(A)))
print("  e2(R) = 2-2A-A^2 :", e2R==sadd(sconst((Q(2),Q(0))),sscal(-2,A),sneg(smul(A,A))))
A2=smul(A,A);A4=smul(A2,A2);A6=smul(A4,A2)
print("  e2(R)^2-2e1(R)e3(R) = 3A^4 :", sadd(smul(e2R,e2R),sscal(-2,smul(e1R,e3R)))==sscal(3,A4))
v=[Z]*M; v[3]=ONE           # vartheta = z^3
print("  e3(R)^2 = A^6+64*vartheta :", smul(e3R,e3R)==sadd(A6,sscal(64,v)))
# 2. F = e2(nu) = E/2, and the quintic
e2nu=sadd(smul(nu[0],nu[1]),smul(nu[0],nu[2]),smul(nu[1],nu[2]))
print("  e2(nu) = E/2 :", e2nu==sscal(Q(1,2),E))
F=e2nu
d=json.load(open('/home/agent/projects/beta-prime/code/day147_gauss/data.json'))
b=[0]+[int(x) for x in d['b']]
print("  F coeffs == b_k :", all(F[3*k]==(Q(b[k]),Q(0)) for k in range(1,13)) and all(F[j]==Z for j in range(M) if j%3))
Fm1=sadd(F,sconst((Q(-1),Q(0))))
L=smul(smul(F,smul(smul(Fm1,Fm1),Fm1)), sadd(sscal(4,F),sconst((Q(-3),Q(0)))))
t=sadd(sscal(2,F),sconst((Q(-3),Q(0))))
Rq=smul(v,smul(t,t))
print("  QUINTIC F(F-1)^3(4F-3) = v(2F-3)^2 :", L==Rq)

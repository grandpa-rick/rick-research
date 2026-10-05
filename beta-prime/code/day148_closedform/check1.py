from fractions import Fraction as Q
import json
d=json.load(open('/home/agent/projects/beta-prime/code/day147_gauss/data.json'))
bb=[0]+[int(x) for x in d['b']]; hh=[int(x) for x in d['h']]
N=15
def mul(A,B,n):
    R=[Q(0)]*(n+1)
    for i,x in enumerate(A):
        if x==0: continue
        for j,y in enumerate(B):
            if i+j>n: break
            R[i+j]+=x*y
    return R
def inv(A,n):
    assert A[0]!=0
    B=[Q(0)]*(n+1); B[0]=Q(1)/A[0]
    for k in range(1,n+1):
        B[k]=-sum(A[j]*B[k-j] for j in range(1,k+1))/A[0]
    return B
F=[Q(0)]+[Q(bb[k]) for k in range(1,N+1)]
def poly_in(F,coeffs,n):   # coeffs[j] * F^j
    R=[Q(0)]*(n+1); P=[Q(1)]+[Q(0)]*n
    for j,c in enumerate(coeffs):
        if c: R=[x+Q(c)*y for x,y in zip(R,P)]
        P=mul(P,F,n)
    return R
# LHS = F(F-1)^3(4F-3) ; RHS = v (2F-3)^2
Fm1=[F[0]-1]+F[1:]
L=mul(mul(F,mul(mul(Fm1,Fm1,N),Fm1,N),N),[Q(-3)+4*F[0]]+[4*x for x in F[1:]],N)
t=[Q(-3)+2*F[0]]+[2*x for x in F[1:]]
R=mul(t,t,N); R=[Q(0)]+R[:N]      # multiply by v
print("F(F-1)^3(4F-3) == v(2F-3)^2 up to v^%d ?"%N, L==R)
print("  residual coeffs:", [str(L[i]-R[i]) for i in range(N+1)])
# H = (2F-3)/((F-1)^2 (4F-3))
den=mul(mul(Fm1,Fm1,N),[Q(-3)+4*F[0]]+[4*x for x in F[1:]],N)
H=mul(t,inv(den,N),N)
print("\nH from formula == tabulated h_j ?", [int(x) for x in H]==hh, [str(x) for x in H[:6]])
# G = F/3 integral? and Lagrange
G=[x/3 for x in F]
print("\nG=F/3 integral?", all(x.denominator==1 for x in G))
print("G coeffs:", [str(x) for x in G[1:]])
# check G = v * (2G-1)^2 / ((3G-1)^3 (4G-1))
u2=[2*G[0]-1]+[2*x for x in G[1:]]
u3=[3*G[0]-1]+[3*x for x in G[1:]]
u4=[4*G[0]-1]+[4*x for x in G[1:]]
phi=mul(mul(u2,u2,N), inv(mul(mul(mul(u3,u3,N),u3,N),u4,N),N),N)
rhs=[Q(0)]+mul([Q(1)]+[Q(0)]*N,phi,N)[:N]
print("G == v*phi(G)?", G==rhs)
print("phi(G) series (should be integral):", [str(x) for x in phi[:8]])

from fractions import Fraction as Q
import json
K=22; N=K
# Solve G = v*(2G-1)^2 / ((3G-1)^3 (4G-1))  by iteration in Z[[v]]
def mul(A,B,n=N):
    R=[Q(0)]*(n+1)
    for i,x in enumerate(A):
        if x==0: continue
        for j,y in enumerate(B):
            if i+j>n: break
            R[i+j]+=x*y
    return R
def inv(A,n=N):
    B=[Q(0)]*(n+1); B[0]=Q(1)/A[0]
    for k in range(1,n+1):
        B[k]=-sum(A[j]*B[k-j] for j in range(1,k+1))/A[0]
    return B
G=[Q(0)]*(N+1)
for it in range(N+2):
    u2=[2*G[0]-1]+[2*x for x in G[1:]]
    u3=[3*G[0]-1]+[3*x for x in G[1:]]
    u4=[4*G[0]-1]+[4*x for x in G[1:]]
    phi=mul(mul(u2,u2),inv(mul(mul(mul(u3,u3),u3),u4)))
    G=[Q(0)]+phi[:N]
b=[3*x for x in G]
print("all integral?", all(x.denominator==1 for x in b))
print("all divisible by 3?", all((x*1).numerator%3==0 for x in b[1:]))
p=(1<<61)-1
d=json.load(open('/tmp/fastout_3_2.json'))
comp=d['bmod']
print("\n k   predicted b_k                                    match(mod p)?")
ok=True
for k in range(1,K+1):
    pv=int(b[k])
    m = (pv%p==comp[k-1])
    ok &= m
    print("%3d  %-46d %s"%(k,pv,m))
print("\nALL MATCH:",ok)

import sys
p=(1<<61)-1                      # Mersenne prime
K=int(sys.argv[1]) if len(sys.argv)>1 else 22
E1,E2 = (int(sys.argv[2]),int(sys.argv[3])) if len(sys.argv)>3 else (3,2)
NT=3*K-1
L=K+1                            # truncation in E3
def mul(A,B):
    R=[0]*L
    for i,x in enumerate(A):
        if x:
            for j in range(L-i):
                if B[j]: R[i+j]=(R[i+j]+x*B[j])%p
    return R
def add(A,B): return [(x+y)%p for x,y in zip(A,B)]
def smul(k,A): return [(k*x)%p for x in A]
def inv(A):
    a0=A[0]%p; assert a0!=0
    i0=pow(a0,p-2,p); B=[0]*L; B[0]=i0
    for k in range(1,L):
        s=0
        for j in range(1,k+1):
            if A[j]: s+=A[j]*B[k-j]
        B[k]=(-s%p)*i0%p
    return B
def const(c): 
    A=[0]*L; A[0]=c%p; return A
# roots of t^3 - E1 t^2 + E2 t - E3 as series in E3, starting from roots of t^2-E1t+E2 and 0
import itertools
r0=[0]
for t in range(-50,50):
    if t*t-E1*t+E2==0 and t!=0: r0.append(t)
assert len(r0)==3, (r0,"pick E1,E2 with distinct nonzero integer roots")
X=[0]*L; X[1]=1     # the variable E3
us=[]
for a0 in r0:
    u=const(a0)
    for _ in range(K+2):
        f=add(add(mul(mul(u,u),u), smul(-E1,mul(u,u))), add(smul(E2,u), smul(-1,X)))
        fp=add(smul(3,mul(u,u)), add(smul(-2*E1,u), const(E2)))
        u=add(u, smul(-1,mul(f,inv(fp))))
    us.append(u)
# sanity: e1,e2,e3
e1=add(add(us[0],us[1]),us[2]); e2=add(add(mul(us[0],us[1]),mul(us[0],us[2])),mul(us[1],us[2])); e3=mul(mul(us[0],us[1]),us[2])
assert e1==const(E1) and e2==const(E2) and e3==X, "root solve failed"
print("roots ok, base point E1=%d E2=%d"%(E1,E2))
MM=2*NT+2
poch=[]
for u in us:
    row=[const(1)]
    for m in range(1,MM+1): row.append(mul(row[-1], add(u,const(m-1))))
    poch.append(row)
d12=add(us[0],smul(-1,us[1])); d13=add(us[0],smul(-1,us[2])); d23=add(us[1],smul(-1,us[2]))
Vinv=inv(mul(mul(d12,d13),d23))
fact=[1]*(NT+2)
for i in range(1,NT+2): fact[i]=fact[i-1]*i%p
ifact=[pow(f,p-2,p) for f in fact]
FP=[]
for n in range(NT+1):
    acc=[0]*L
    for a in range(n+1):
        for b in range(n+1-a):
            c=n-a-b
            co=ifact[a]*ifact[b]%p*ifact[c]%p
            t=mul(mul(poch[0][a+b],poch[1][a+c]),poch[2][b+c])
            num=mul(mul(add(d12,const(b-c)),add(d13,const(a-c))),add(d23,const(a-b)))
            acc=add(acc, smul(co, mul(t,num)))
    FP.append(mul(acc,Vinv))
assert FP[0]==const(1)
# log
LG=[[0]*L for _ in range(NT+1)]
for n in range(1,NT+1):
    acc=smul(n,FP[n])
    for j in range(1,n):
        acc=add(acc, smul(-j, mul(LG[j],FP[n-j])))
    LG[n]=smul(pow(n,p-2,p),acc)
out=[]
for k in range(1,K+1):
    n=3*k-1
    # check vanishing: [E3^k] of LG[b] for b<3k-1 should be 0
    viol=[b for b in range(1,n) if LG[b][k]!=0]
    out.append((k, n*LG[n][k]%p, len(viol)))
print("k, b_k mod p, #vanishing-violations")
for k,v,vi in out: print("  ",k,v,vi)
import json
json.dump({"p":p,"bmod":[x[1] for x in out],"K":K},open('/tmp/fastout_%d_%d.json'%(E1,E2),'w'))

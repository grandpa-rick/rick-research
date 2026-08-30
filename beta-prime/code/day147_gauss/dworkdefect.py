import json
from fractions import Fraction as Q
D=json.load(open('/home/agent/projects/beta-prime/code/day147_gauss/data.json'))
h=[Q(x) for x in D["h"]]; N=len(h)-1
def mul(A,B,n): return [sum(A[i]*B[k-i] for i in range(k+1)) for k in range(n+1)]
H3=mul(mul(h,h,N),h,N)
Hp=[Q(0)]*(N+1)
for j in range(N//3+1): Hp[3*j]=h[j]
inv=[Q(0)]*(N+1); inv[0]=Q(1)
for k in range(1,N+1): inv[k]=-sum(Hp[i]*inv[k-i] for i in range(1,k+1))
R=mul(H3,inv,N)   # H(z)^3 / H(z^3)
def v3(fr):
    if fr==0: return 'inf'
    n,d=fr.numerator,fr.denominator; v=0
    while n%3==0: n//=3;v+=1
    while d%3==0: d//=3;v-=1
    return v
print("K := Hcal(z)^3 / Hcal(z^3).  Dieudonne-Dwork needs K in 1+3z Z_3[[z]], i.e. v3>=1 for n>=1.")
print(" n   v3([z^n]K)   coefficient")
for n in range(0,N+1):
    print(" %-3d %-12s %s"%(n, v3(R[n]), R[n]))
print()
print("min v3 over n>=1:", min(v3(R[n]) for n in range(1,N+1) if R[n]!=0))
# Richardson on ratios to estimate singularity
print()
r=[float(h[j+1]/h[j]) for j in range(N)]
print("ratios r_j:", [round(x,4) for x in r])
print("Richardson (j*r_j-(j-1)*r_{j-1}) -> radius^-1 estimate:")
print([round(j*r[j]-(j-1)*r[j-1],4) for j in range(1,N)])
